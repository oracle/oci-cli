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


@click.command(cli_util.override('blockstorage.blockstorage_root_group.command_name', 'blockstorage'), cls=CommandGroupWithAlias, help=cli_util.override('blockstorage.blockstorage_root_group.help', """API covering the [Networking],
[Compute], and
[Block Volume] services. Use this API
to manage resources such as virtual cloud networks (VCNs), compute instances, and
block storage volumes."""), short_help=cli_util.override('blockstorage.blockstorage_root_group.short_help', """Core Services API"""))
@cli_util.help_option_group
def blockstorage_root_group():
    pass


@click.command(cli_util.override('blockstorage.boot_volume_kms_key_group.command_name', 'boot-volume-kms-key'), cls=CommandGroupWithAlias, help="""The Key Management master encryption key associated with this volume.""")
@cli_util.help_option_group
def boot_volume_kms_key_group():
    pass


@click.command(cli_util.override('blockstorage.volume_group.command_name', 'volume'), cls=CommandGroupWithAlias, help="""A detachable block volume device that allows you to dynamically expand the storage capacity of an instance. For more information, see [Overview of Cloud Volume Storage].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def volume_group():
    pass


@click.command(cli_util.override('blockstorage.boot_volume_backup_group.command_name', 'boot-volume-backup'), cls=CommandGroupWithAlias, help="""A point-in-time copy of a boot volume that can then be used to create a new boot volume or recover a boot volume. For more information, see [Overview of Boot Volume Backups] To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def boot_volume_backup_group():
    pass


@click.command(cli_util.override('blockstorage.boot_volume_group.command_name', 'boot-volume'), cls=CommandGroupWithAlias, help="""A detachable boot volume device that contains the image used to boot a Compute instance. For more information, see [Overview of Boot Volumes].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def boot_volume_group():
    pass


@click.command(cli_util.override('blockstorage.volume_backup_group.command_name', 'volume-backup'), cls=CommandGroupWithAlias, help="""A point-in-time copy of a volume that can then be used to create a new block volume or recover a block volume. For more information, see [Overview of Cloud Volume Storage].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def volume_backup_group():
    pass


@click.command(cli_util.override('blockstorage.volume_group_backup_group.command_name', 'volume-group-backup'), cls=CommandGroupWithAlias, help="""A point-in-time copy of a volume group that can then be used to create a new volume group or restore a volume group. For more information, see [Volume Groups].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def volume_group_backup_group():
    pass


@click.command(cli_util.override('blockstorage.volume_backup_policy_assignment_group.command_name', 'volume-backup-policy-assignment'), cls=CommandGroupWithAlias, help="""Specifies the volume that the volume backup policy is assigned to.

For more information about Oracle defined backup policies and custom backup policies, see [Policy-Based Backups].""")
@cli_util.help_option_group
def volume_backup_policy_assignment_group():
    pass


@click.command(cli_util.override('blockstorage.volume_group_group.command_name', 'volume-group'), cls=CommandGroupWithAlias, help="""Specifies a volume group which is a collection of volumes. For more information, see [Volume Groups].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def volume_group_group():
    pass


@click.command(cli_util.override('blockstorage.volume_backup_policy_group.command_name', 'volume-backup-policy'), cls=CommandGroupWithAlias, help="""A policy for automatically creating volume backups according to a recurring schedule. Has a set of one or more schedules that control when and how backups are created.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def volume_backup_policy_group():
    pass


@click.command(cli_util.override('blockstorage.volume_kms_key_group.command_name', 'volume-kms-key'), cls=CommandGroupWithAlias, help="""The Key Management master encryption key associated with this volume.""")
@cli_util.help_option_group
def volume_kms_key_group():
    pass


core_service_cli.core_service_group.add_command(blockstorage_root_group)
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


@boot_volume_backup_group.command(name=cli_util.override('blockstorage.change_boot_volume_backup_compartment.command_name', 'change-compartment'), help=u"""Moves a boot volume backup into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeBootVolumeBackupCompartment)""")
@cli_util.option('--boot-volume-backup-id', required=True, help=u"""The OCID of the boot volume backup.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the boot volume backup to.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_boot_volume_backup_compartment(ctx, from_json, boot_volume_backup_id, compartment_id):

    if isinstance(boot_volume_backup_id, six.string_types) and len(boot_volume_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --boot-volume-backup-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.change_boot_volume_backup_compartment(
        boot_volume_backup_id=boot_volume_backup_id,
        change_boot_volume_backup_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@boot_volume_group.command(name=cli_util.override('blockstorage.change_boot_volume_compartment.command_name', 'change-compartment'), help=u"""Moves a boot volume into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeBootVolumeCompartment)""")
@cli_util.option('--boot-volume-id', required=True, help=u"""The OCID of the boot volume.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the boot volume to.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_boot_volume_compartment(ctx, from_json, boot_volume_id, compartment_id):

    if isinstance(boot_volume_id, six.string_types) and len(boot_volume_id.strip()) == 0:
        raise click.UsageError('Parameter --boot-volume-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.change_boot_volume_compartment(
        boot_volume_id=boot_volume_id,
        change_boot_volume_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_backup_group.command(name=cli_util.override('blockstorage.change_volume_backup_compartment.command_name', 'change-compartment'), help=u"""Moves a volume backup into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeVolumeBackupCompartment)""")
@cli_util.option('--volume-backup-id', required=True, help=u"""The OCID of the volume backup.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the volume backup to.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_volume_backup_compartment(ctx, from_json, volume_backup_id, compartment_id):

    if isinstance(volume_backup_id, six.string_types) and len(volume_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-backup-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.change_volume_backup_compartment(
        volume_backup_id=volume_backup_id,
        change_volume_backup_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_group.command(name=cli_util.override('blockstorage.change_volume_compartment.command_name', 'change-compartment'), help=u"""Moves a volume into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeVolumeCompartment)""")
@cli_util.option('--volume-id', required=True, help=u"""The OCID of the volume.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the volume to.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_volume_compartment(ctx, from_json, volume_id, compartment_id):

    if isinstance(volume_id, six.string_types) and len(volume_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.change_volume_compartment(
        volume_id=volume_id,
        change_volume_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_group_backup_group.command(name=cli_util.override('blockstorage.change_volume_group_backup_compartment.command_name', 'change-compartment'), help=u"""Moves a volume group backup into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeVolumeGroupBackupCompartment)""")
@cli_util.option('--volume-group-backup-id', required=True, help=u"""The Oracle Cloud ID (OCID) that uniquely identifies the volume group backup.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the volume group backup to.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_volume_group_backup_compartment(ctx, from_json, volume_group_backup_id, compartment_id):

    if isinstance(volume_group_backup_id, six.string_types) and len(volume_group_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-group-backup-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.change_volume_group_backup_compartment(
        volume_group_backup_id=volume_group_backup_id,
        change_volume_group_backup_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_group_group.command(name=cli_util.override('blockstorage.change_volume_group_compartment.command_name', 'change-compartment'), help=u"""Moves a volume group into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeVolumeGroupCompartment)""")
@cli_util.option('--volume-group-id', required=True, help=u"""The Oracle Cloud ID (OCID) that uniquely identifies the volume group.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the volume group to.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_volume_group_compartment(ctx, from_json, volume_group_id, compartment_id):

    if isinstance(volume_group_id, six.string_types) and len(volume_group_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-group-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.change_volume_group_compartment(
        volume_group_id=volume_group_id,
        change_volume_group_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@boot_volume_backup_group.command(name=cli_util.override('blockstorage.copy_boot_volume_backup.command_name', 'copy'), help=u"""Creates a boot volume backup copy in specified region. For general information about volume backups, see [Overview of Boot Volume Backups] \n[Command Reference](copyBootVolumeBackup)""")
@cli_util.option('--boot-volume-backup-id', required=True, help=u"""The OCID of the boot volume backup.""")
@cli_util.option('--destination-region', required=True, help=u"""The name of the destination region.

Example: `us-ashburn-1`""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the boot volume backup. Does not have to be unique and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--kms-key-id', help=u"""The OCID of the Key Management key in the destination region which will be the master encryption key for the copied boot volume backup. If you do not specify this attribute the boot volume backup will be encrypted with the Oracle-provided encryption key when it is copied to the destination region.

 For more information about the Key Management service and encryption keys, see [Overview of Key Management] and [Using Keys].""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'BootVolumeBackup'})
@cli_util.wrap_exceptions
def copy_boot_volume_backup(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, boot_volume_backup_id, destination_region, display_name, kms_key_id):

    if isinstance(boot_volume_backup_id, six.string_types) and len(boot_volume_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --boot-volume-backup-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['destinationRegion'] = destination_region

    if display_name is not None:
        _details['displayName'] = display_name

    if kms_key_id is not None:
        _details['kmsKeyId'] = kms_key_id

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.copy_boot_volume_backup(
        boot_volume_backup_id=boot_volume_backup_id,
        copy_boot_volume_backup_details=_details,
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


@volume_backup_group.command(name=cli_util.override('blockstorage.copy_volume_backup.command_name', 'copy'), help=u"""Creates a volume backup copy in specified region. For general information about volume backups, see [Overview of Block Volume Service Backups] \n[Command Reference](copyVolumeBackup)""")
@cli_util.option('--volume-backup-id', required=True, help=u"""The OCID of the volume backup.""")
@cli_util.option('--destination-region', required=True, help=u"""The name of the destination region.

Example: `us-ashburn-1`""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the volume backup. Does not have to be unique and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--kms-key-id', help=u"""The OCID of the Key Management key in the destination region which will be the master encryption key for the copied volume backup. If you do not specify this attribute the volume backup will be encrypted with the Oracle-provided encryption key when it is copied to the destination region.

 For more information about the Key Management service and encryption keys, see [Overview of Key Management] and [Using Keys].""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VolumeBackup'})
@cli_util.wrap_exceptions
def copy_volume_backup(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, volume_backup_id, destination_region, display_name, kms_key_id):

    if isinstance(volume_backup_id, six.string_types) and len(volume_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-backup-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['destinationRegion'] = destination_region

    if display_name is not None:
        _details['displayName'] = display_name

    if kms_key_id is not None:
        _details['kmsKeyId'] = kms_key_id

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.copy_volume_backup(
        volume_backup_id=volume_backup_id,
        copy_volume_backup_details=_details,
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


@boot_volume_group.command(name=cli_util.override('blockstorage.create_boot_volume.command_name', 'create'), help=u"""Creates a new boot volume in the specified compartment from an existing boot volume or a boot volume backup. For general information about boot volumes, see [Boot Volumes]. You may optionally specify a *display name* for the volume, which is simply a friendly name or description. It does not have to be unique, and you can change it. Avoid entering confidential information. \n[Command Reference](createBootVolume)""")
@cli_util.option('--availability-domain', required=True, help=u"""The availability domain of the boot volume.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment that contains the boot volume.""")
@cli_util.option('--source-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Specifies the boot volume source details for a new boot volume. The volume source is either another boot volume in the same availability domain or a boot volume backup. This is a mandatory field for a boot volume.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--backup-policy-id', help=u"""If provided, specifies the ID of the boot volume backup policy to assign to the newly created boot volume. If omitted, no policy will be assigned.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--kms-key-id', help=u"""The OCID of the Key Management key to assign as the master encryption key for the boot volume.""")
@cli_util.option('--size-in-gbs', type=click.INT, help=u"""The size of the volume in GBs.""")
@cli_util.option('--vpus-per-gb', type=click.INT, help=u"""The number of volume performance units (VPUs) that will be applied to this volume per GB, representing the Block Volume service's elastic performance options. See [Block Volume Elastic Performance] for more information.

Allowed values:

  * `10`: Represents Balanced option.

  * `20`: Represents Higher Performance option.""")
@cli_util.option('--is-auto-tune-enabled', type=click.BOOL, help=u"""Specifies whether the auto-tune performance is enabled for this boot volume.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'source-details': {'module': 'core', 'class': 'BootVolumeSourceDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'source-details': {'module': 'core', 'class': 'BootVolumeSourceDetails'}}, output_type={'module': 'core', 'class': 'BootVolume'})
@cli_util.wrap_exceptions
def create_boot_volume(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, compartment_id, source_details, backup_policy_id, defined_tags, display_name, freeform_tags, kms_key_id, size_in_gbs, vpus_per_gb, is_auto_tune_enabled):

    kwargs = {}

    _details = {}
    _details['availabilityDomain'] = availability_domain
    _details['compartmentId'] = compartment_id
    _details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)

    if backup_policy_id is not None:
        _details['backupPolicyId'] = backup_policy_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if kms_key_id is not None:
        _details['kmsKeyId'] = kms_key_id

    if size_in_gbs is not None:
        _details['sizeInGBs'] = size_in_gbs

    if vpus_per_gb is not None:
        _details['vpusPerGB'] = vpus_per_gb

    if is_auto_tune_enabled is not None:
        _details['isAutoTuneEnabled'] = is_auto_tune_enabled

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.create_boot_volume(
        create_boot_volume_details=_details,
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


@boot_volume_group.command(name=cli_util.override('blockstorage.create_boot_volume_boot_volume_source_from_boot_volume_backup_details.command_name', 'create-boot-volume-boot-volume-source-from-boot-volume-backup-details'), help=u"""Creates a new boot volume in the specified compartment from an existing boot volume or a boot volume backup. For general information about boot volumes, see [Boot Volumes]. You may optionally specify a *display name* for the volume, which is simply a friendly name or description. It does not have to be unique, and you can change it. Avoid entering confidential information. \n[Command Reference](createBootVolume)""")
@cli_util.option('--availability-domain', required=True, help=u"""The availability domain of the boot volume.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment that contains the boot volume.""")
@cli_util.option('--source-details-id', required=True, help=u"""The OCID of the boot volume backup.""")
@cli_util.option('--backup-policy-id', help=u"""If provided, specifies the ID of the boot volume backup policy to assign to the newly created boot volume. If omitted, no policy will be assigned.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--kms-key-id', help=u"""The OCID of the Key Management key to assign as the master encryption key for the boot volume.""")
@cli_util.option('--size-in-gbs', type=click.INT, help=u"""The size of the volume in GBs.""")
@cli_util.option('--vpus-per-gb', type=click.INT, help=u"""The number of volume performance units (VPUs) that will be applied to this volume per GB, representing the Block Volume service's elastic performance options. See [Block Volume Elastic Performance] for more information.

Allowed values:

  * `10`: Represents Balanced option.

  * `20`: Represents Higher Performance option.""")
@cli_util.option('--is-auto-tune-enabled', type=click.BOOL, help=u"""Specifies whether the auto-tune performance is enabled for this boot volume.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'BootVolume'})
@cli_util.wrap_exceptions
def create_boot_volume_boot_volume_source_from_boot_volume_backup_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, compartment_id, source_details_id, backup_policy_id, defined_tags, display_name, freeform_tags, kms_key_id, size_in_gbs, vpus_per_gb, is_auto_tune_enabled):

    kwargs = {}

    _details = {}
    _details['sourceDetails'] = {}
    _details['availabilityDomain'] = availability_domain
    _details['compartmentId'] = compartment_id
    _details['sourceDetails']['id'] = source_details_id

    if backup_policy_id is not None:
        _details['backupPolicyId'] = backup_policy_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if kms_key_id is not None:
        _details['kmsKeyId'] = kms_key_id

    if size_in_gbs is not None:
        _details['sizeInGBs'] = size_in_gbs

    if vpus_per_gb is not None:
        _details['vpusPerGB'] = vpus_per_gb

    if is_auto_tune_enabled is not None:
        _details['isAutoTuneEnabled'] = is_auto_tune_enabled

    _details['sourceDetails']['type'] = 'bootVolumeBackup'

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.create_boot_volume(
        create_boot_volume_details=_details,
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


@boot_volume_group.command(name=cli_util.override('blockstorage.create_boot_volume_boot_volume_source_from_boot_volume_details.command_name', 'create-boot-volume-boot-volume-source-from-boot-volume-details'), help=u"""Creates a new boot volume in the specified compartment from an existing boot volume or a boot volume backup. For general information about boot volumes, see [Boot Volumes]. You may optionally specify a *display name* for the volume, which is simply a friendly name or description. It does not have to be unique, and you can change it. Avoid entering confidential information. \n[Command Reference](createBootVolume)""")
@cli_util.option('--availability-domain', required=True, help=u"""The availability domain of the boot volume.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment that contains the boot volume.""")
@cli_util.option('--source-details-id', required=True, help=u"""The OCID of the boot volume.""")
@cli_util.option('--backup-policy-id', help=u"""If provided, specifies the ID of the boot volume backup policy to assign to the newly created boot volume. If omitted, no policy will be assigned.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--kms-key-id', help=u"""The OCID of the Key Management key to assign as the master encryption key for the boot volume.""")
@cli_util.option('--size-in-gbs', type=click.INT, help=u"""The size of the volume in GBs.""")
@cli_util.option('--vpus-per-gb', type=click.INT, help=u"""The number of volume performance units (VPUs) that will be applied to this volume per GB, representing the Block Volume service's elastic performance options. See [Block Volume Elastic Performance] for more information.

Allowed values:

  * `10`: Represents Balanced option.

  * `20`: Represents Higher Performance option.""")
@cli_util.option('--is-auto-tune-enabled', type=click.BOOL, help=u"""Specifies whether the auto-tune performance is enabled for this boot volume.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'BootVolume'})
@cli_util.wrap_exceptions
def create_boot_volume_boot_volume_source_from_boot_volume_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, compartment_id, source_details_id, backup_policy_id, defined_tags, display_name, freeform_tags, kms_key_id, size_in_gbs, vpus_per_gb, is_auto_tune_enabled):

    kwargs = {}

    _details = {}
    _details['sourceDetails'] = {}
    _details['availabilityDomain'] = availability_domain
    _details['compartmentId'] = compartment_id
    _details['sourceDetails']['id'] = source_details_id

    if backup_policy_id is not None:
        _details['backupPolicyId'] = backup_policy_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if kms_key_id is not None:
        _details['kmsKeyId'] = kms_key_id

    if size_in_gbs is not None:
        _details['sizeInGBs'] = size_in_gbs

    if vpus_per_gb is not None:
        _details['vpusPerGB'] = vpus_per_gb

    if is_auto_tune_enabled is not None:
        _details['isAutoTuneEnabled'] = is_auto_tune_enabled

    _details['sourceDetails']['type'] = 'bootVolume'

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.create_boot_volume(
        create_boot_volume_details=_details,
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


@boot_volume_backup_group.command(name=cli_util.override('blockstorage.create_boot_volume_backup.command_name', 'create'), help=u"""Creates a new boot volume backup of the specified boot volume. For general information about boot volume backups, see [Overview of Boot Volume Backups]

When the request is received, the backup object is in a REQUEST_RECEIVED state. When the data is imaged, it goes into a CREATING state. After the backup is fully uploaded to the cloud, it goes into an AVAILABLE state. \n[Command Reference](createBootVolumeBackup)""")
@cli_util.option('--boot-volume-id', required=True, help=u"""The OCID of the boot volume that needs to be backed up.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name for the boot volume backup. Does not have to be unique and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["FULL", "INCREMENTAL"]), help=u"""The type of backup to create. If omitted, defaults to incremental.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'BootVolumeBackup'})
@cli_util.wrap_exceptions
def create_boot_volume_backup(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, boot_volume_id, defined_tags, display_name, freeform_tags, type):

    kwargs = {}

    _details = {}
    _details['bootVolumeId'] = boot_volume_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if type is not None:
        _details['type'] = type

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.create_boot_volume_backup(
        create_boot_volume_backup_details=_details,
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


@volume_group.command(name=cli_util.override('blockstorage.create_volume.command_name', 'create'), help=u"""Creates a new volume in the specified compartment. Volumes can be created in sizes ranging from 50 GB (51200 MB) to 32 TB (33554432 MB), in 1 GB (1024 MB) increments. By default, volumes are 1 TB (1048576 MB). For general information about block volumes, see [Overview of Block Volume Service].

A volume and instance can be in separate compartments but must be in the same availability domain. For information about access control and compartments, see [Overview of the IAM Service]. For information about availability domains, see [Regions and Availability Domains]. To get a list of availability domains, use the `ListAvailabilityDomains` operation in the Identity and Access Management Service API.

You may optionally specify a *display name* for the volume, which is simply a friendly name or description. It does not have to be unique, and you can change it. Avoid entering confidential information. \n[Command Reference](createVolume)""")
@cli_util.option('--availability-domain', required=True, help=u"""The availability domain of the volume.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment that contains the volume.""")
@cli_util.option('--backup-policy-id', help=u"""If provided, specifies the ID of the volume backup policy to assign to the newly created volume. If omitted, no policy will be assigned.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--kms-key-id', help=u"""The OCID of the Key Management key to assign as the master encryption key for the volume.""")
@cli_util.option('--vpus-per-gb', type=click.INT, help=u"""The number of volume performance units (VPUs) that will be applied to this volume per GB, representing the Block Volume service's elastic performance options. See [Block Volume Elastic Performance] for more information.

Allowed values:

  * `0`: Represents Lower Cost option.

  * `10`: Represents Balanced option.

  * `20`: Represents Higher Performance option.""")
@cli_util.option('--size-in-gbs', type=click.INT, help=u"""The size of the volume in GBs.""")
@cli_util.option('--size-in-mbs', type=click.INT, help=u"""The size of the volume in MBs. The value must be a multiple of 1024. This field is deprecated. Use sizeInGBs instead.""")
@cli_util.option('--source-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Specifies the volume source details for a new Block volume. The volume source is either another Block volume in the same availability domain or a Block volume backup. This is an optional field. If not specified or set to null, the new Block volume will be empty. When specified, the new Block volume will contain data from the source volume or backup.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--volume-backup-id', help=u"""The OCID of the volume backup from which the data should be restored on the newly created volume. This field is deprecated. Use the sourceDetails field instead to specify the backup for the volume.""")
@cli_util.option('--is-auto-tune-enabled', type=click.BOOL, help=u"""Specifies whether the auto-tune performance is enabled for this volume.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'source-details': {'module': 'core', 'class': 'VolumeSourceDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'source-details': {'module': 'core', 'class': 'VolumeSourceDetails'}}, output_type={'module': 'core', 'class': 'Volume'})
@cli_util.wrap_exceptions
def create_volume(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, compartment_id, backup_policy_id, defined_tags, display_name, freeform_tags, kms_key_id, vpus_per_gb, size_in_gbs, size_in_mbs, source_details, volume_backup_id, is_auto_tune_enabled):

    kwargs = {}

    _details = {}
    _details['availabilityDomain'] = availability_domain
    _details['compartmentId'] = compartment_id

    if backup_policy_id is not None:
        _details['backupPolicyId'] = backup_policy_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if kms_key_id is not None:
        _details['kmsKeyId'] = kms_key_id

    if vpus_per_gb is not None:
        _details['vpusPerGB'] = vpus_per_gb

    if size_in_gbs is not None:
        _details['sizeInGBs'] = size_in_gbs

    if size_in_mbs is not None:
        _details['sizeInMBs'] = size_in_mbs

    if source_details is not None:
        _details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)

    if volume_backup_id is not None:
        _details['volumeBackupId'] = volume_backup_id

    if is_auto_tune_enabled is not None:
        _details['isAutoTuneEnabled'] = is_auto_tune_enabled

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.create_volume(
        create_volume_details=_details,
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


@volume_group.command(name=cli_util.override('blockstorage.create_volume_volume_source_from_volume_details.command_name', 'create-volume-volume-source-from-volume-details'), help=u"""Creates a new volume in the specified compartment. Volumes can be created in sizes ranging from 50 GB (51200 MB) to 32 TB (33554432 MB), in 1 GB (1024 MB) increments. By default, volumes are 1 TB (1048576 MB). For general information about block volumes, see [Overview of Block Volume Service].

A volume and instance can be in separate compartments but must be in the same availability domain. For information about access control and compartments, see [Overview of the IAM Service]. For information about availability domains, see [Regions and Availability Domains]. To get a list of availability domains, use the `ListAvailabilityDomains` operation in the Identity and Access Management Service API.

You may optionally specify a *display name* for the volume, which is simply a friendly name or description. It does not have to be unique, and you can change it. Avoid entering confidential information. \n[Command Reference](createVolume)""")
@cli_util.option('--availability-domain', required=True, help=u"""The availability domain of the volume.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment that contains the volume.""")
@cli_util.option('--source-details-id', required=True, help=u"""The OCID of the volume.""")
@cli_util.option('--backup-policy-id', help=u"""If provided, specifies the ID of the volume backup policy to assign to the newly created volume. If omitted, no policy will be assigned.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--kms-key-id', help=u"""The OCID of the Key Management key to assign as the master encryption key for the volume.""")
@cli_util.option('--vpus-per-gb', type=click.INT, help=u"""The number of volume performance units (VPUs) that will be applied to this volume per GB, representing the Block Volume service's elastic performance options. See [Block Volume Elastic Performance] for more information.

Allowed values:

  * `0`: Represents Lower Cost option.

  * `10`: Represents Balanced option.

  * `20`: Represents Higher Performance option.""")
@cli_util.option('--size-in-gbs', type=click.INT, help=u"""The size of the volume in GBs.""")
@cli_util.option('--size-in-mbs', type=click.INT, help=u"""The size of the volume in MBs. The value must be a multiple of 1024. This field is deprecated. Use sizeInGBs instead.""")
@cli_util.option('--volume-backup-id', help=u"""The OCID of the volume backup from which the data should be restored on the newly created volume. This field is deprecated. Use the sourceDetails field instead to specify the backup for the volume.""")
@cli_util.option('--is-auto-tune-enabled', type=click.BOOL, help=u"""Specifies whether the auto-tune performance is enabled for this volume.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'Volume'})
@cli_util.wrap_exceptions
def create_volume_volume_source_from_volume_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, compartment_id, source_details_id, backup_policy_id, defined_tags, display_name, freeform_tags, kms_key_id, vpus_per_gb, size_in_gbs, size_in_mbs, volume_backup_id, is_auto_tune_enabled):

    kwargs = {}

    _details = {}
    _details['sourceDetails'] = {}
    _details['availabilityDomain'] = availability_domain
    _details['compartmentId'] = compartment_id
    _details['sourceDetails']['id'] = source_details_id

    if backup_policy_id is not None:
        _details['backupPolicyId'] = backup_policy_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if kms_key_id is not None:
        _details['kmsKeyId'] = kms_key_id

    if vpus_per_gb is not None:
        _details['vpusPerGB'] = vpus_per_gb

    if size_in_gbs is not None:
        _details['sizeInGBs'] = size_in_gbs

    if size_in_mbs is not None:
        _details['sizeInMBs'] = size_in_mbs

    if volume_backup_id is not None:
        _details['volumeBackupId'] = volume_backup_id

    if is_auto_tune_enabled is not None:
        _details['isAutoTuneEnabled'] = is_auto_tune_enabled

    _details['sourceDetails']['type'] = 'volume'

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.create_volume(
        create_volume_details=_details,
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


@volume_group.command(name=cli_util.override('blockstorage.create_volume_volume_source_from_volume_backup_details.command_name', 'create-volume-volume-source-from-volume-backup-details'), help=u"""Creates a new volume in the specified compartment. Volumes can be created in sizes ranging from 50 GB (51200 MB) to 32 TB (33554432 MB), in 1 GB (1024 MB) increments. By default, volumes are 1 TB (1048576 MB). For general information about block volumes, see [Overview of Block Volume Service].

A volume and instance can be in separate compartments but must be in the same availability domain. For information about access control and compartments, see [Overview of the IAM Service]. For information about availability domains, see [Regions and Availability Domains]. To get a list of availability domains, use the `ListAvailabilityDomains` operation in the Identity and Access Management Service API.

You may optionally specify a *display name* for the volume, which is simply a friendly name or description. It does not have to be unique, and you can change it. Avoid entering confidential information. \n[Command Reference](createVolume)""")
@cli_util.option('--availability-domain', required=True, help=u"""The availability domain of the volume.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment that contains the volume.""")
@cli_util.option('--source-details-id', required=True, help=u"""The OCID of the volume backup.""")
@cli_util.option('--backup-policy-id', help=u"""If provided, specifies the ID of the volume backup policy to assign to the newly created volume. If omitted, no policy will be assigned.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--kms-key-id', help=u"""The OCID of the Key Management key to assign as the master encryption key for the volume.""")
@cli_util.option('--vpus-per-gb', type=click.INT, help=u"""The number of volume performance units (VPUs) that will be applied to this volume per GB, representing the Block Volume service's elastic performance options. See [Block Volume Elastic Performance] for more information.

Allowed values:

  * `0`: Represents Lower Cost option.

  * `10`: Represents Balanced option.

  * `20`: Represents Higher Performance option.""")
@cli_util.option('--size-in-gbs', type=click.INT, help=u"""The size of the volume in GBs.""")
@cli_util.option('--size-in-mbs', type=click.INT, help=u"""The size of the volume in MBs. The value must be a multiple of 1024. This field is deprecated. Use sizeInGBs instead.""")
@cli_util.option('--volume-backup-id', help=u"""The OCID of the volume backup from which the data should be restored on the newly created volume. This field is deprecated. Use the sourceDetails field instead to specify the backup for the volume.""")
@cli_util.option('--is-auto-tune-enabled', type=click.BOOL, help=u"""Specifies whether the auto-tune performance is enabled for this volume.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'Volume'})
@cli_util.wrap_exceptions
def create_volume_volume_source_from_volume_backup_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, compartment_id, source_details_id, backup_policy_id, defined_tags, display_name, freeform_tags, kms_key_id, vpus_per_gb, size_in_gbs, size_in_mbs, volume_backup_id, is_auto_tune_enabled):

    kwargs = {}

    _details = {}
    _details['sourceDetails'] = {}
    _details['availabilityDomain'] = availability_domain
    _details['compartmentId'] = compartment_id
    _details['sourceDetails']['id'] = source_details_id

    if backup_policy_id is not None:
        _details['backupPolicyId'] = backup_policy_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if kms_key_id is not None:
        _details['kmsKeyId'] = kms_key_id

    if vpus_per_gb is not None:
        _details['vpusPerGB'] = vpus_per_gb

    if size_in_gbs is not None:
        _details['sizeInGBs'] = size_in_gbs

    if size_in_mbs is not None:
        _details['sizeInMBs'] = size_in_mbs

    if volume_backup_id is not None:
        _details['volumeBackupId'] = volume_backup_id

    if is_auto_tune_enabled is not None:
        _details['isAutoTuneEnabled'] = is_auto_tune_enabled

    _details['sourceDetails']['type'] = 'volumeBackup'

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.create_volume(
        create_volume_details=_details,
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


@volume_backup_group.command(name=cli_util.override('blockstorage.create_volume_backup.command_name', 'create'), help=u"""Creates a new backup of the specified volume. For general information about volume backups, see [Overview of Block Volume Service Backups]

When the request is received, the backup object is in a REQUEST_RECEIVED state. When the data is imaged, it goes into a CREATING state. After the backup is fully uploaded to the cloud, it goes into an AVAILABLE state. \n[Command Reference](createVolumeBackup)""")
@cli_util.option('--volume-id', required=True, help=u"""The OCID of the volume that needs to be backed up.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name for the volume backup. Does not have to be unique and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["FULL", "INCREMENTAL"]), help=u"""The type of backup to create. If omitted, defaults to INCREMENTAL.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'VolumeBackup'})
@cli_util.wrap_exceptions
def create_volume_backup(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, volume_id, defined_tags, display_name, freeform_tags, type):

    kwargs = {}

    _details = {}
    _details['volumeId'] = volume_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if type is not None:
        _details['type'] = type

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.create_volume_backup(
        create_volume_backup_details=_details,
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


@volume_backup_policy_group.command(name=cli_util.override('blockstorage.create_volume_backup_policy.command_name', 'create'), help=u"""Creates a new user defined backup policy.

For more information about Oracle defined backup policies and user defined backup policies, see [Policy-Based Backups]. \n[Command Reference](createVolumeBackupPolicy)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the volume backup policy. Does not have to be unique and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--destination-region', help=u"""The paired destination region for copying scheduled backups to. Example: `us-ashburn-1`. See [Region Pairs] for details about paired regions.""")
@cli_util.option('--schedules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The collection of schedules for the volume backup policy. See see [Schedules] in [Policy-Based Backups] for more information.

This option is a JSON list with items of type VolumeBackupSchedule.  For documentation on VolumeBackupSchedule please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/VolumeBackupSchedule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'schedules': {'module': 'core', 'class': 'list[VolumeBackupSchedule]'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'schedules': {'module': 'core', 'class': 'list[VolumeBackupSchedule]'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'VolumeBackupPolicy'})
@cli_util.wrap_exceptions
def create_volume_backup_policy(ctx, from_json, compartment_id, display_name, destination_region, schedules, defined_tags, freeform_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if destination_region is not None:
        _details['destinationRegion'] = destination_region

    if schedules is not None:
        _details['schedules'] = cli_util.parse_json_parameter("schedules", schedules)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.create_volume_backup_policy(
        create_volume_backup_policy_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_backup_policy_assignment_group.command(name=cli_util.override('blockstorage.create_volume_backup_policy_assignment.command_name', 'create'), help=u"""Assigns a volume backup policy to the specified volume. Note that a given volume can only have one backup policy assigned to it. If this operation is used for a volume that already has a different backup policy assigned, the prior backup policy will be silently unassigned. \n[Command Reference](createVolumeBackupPolicyAssignment)""")
@cli_util.option('--asset-id', required=True, help=u"""The OCID of the volume to assign the policy to.""")
@cli_util.option('--policy-id', required=True, help=u"""The OCID of the volume backup policy to assign to the volume.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VolumeBackupPolicyAssignment'})
@cli_util.wrap_exceptions
def create_volume_backup_policy_assignment(ctx, from_json, asset_id, policy_id):

    kwargs = {}

    _details = {}
    _details['assetId'] = asset_id
    _details['policyId'] = policy_id

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.create_volume_backup_policy_assignment(
        create_volume_backup_policy_assignment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_group_group.command(name=cli_util.override('blockstorage.create_volume_group.command_name', 'create'), help=u"""Creates a new volume group in the specified compartment. A volume group is a collection of volumes and may be created from a list of volumes, cloning an existing volume group, or by restoring a volume group backup. A volume group can contain up to 64 volumes. You may optionally specify a *display name* for the volume group, which is simply a friendly name or description. It does not have to be unique, and you can change it. Avoid entering confidential information.

For more information, see [Volume Groups]. \n[Command Reference](createVolumeGroup)""")
@cli_util.option('--availability-domain', required=True, help=u"""The availability domain of the volume group.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment that contains the volume group.""")
@cli_util.option('--source-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Specifies the volume group source details for a new volume group. The volume source is either another a list of volume ids in the same availability domain, another volume group or a volume group backup.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name for the volume group. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'source-details': {'module': 'core', 'class': 'VolumeGroupSourceDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'source-details': {'module': 'core', 'class': 'VolumeGroupSourceDetails'}}, output_type={'module': 'core', 'class': 'VolumeGroup'})
@cli_util.wrap_exceptions
def create_volume_group(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, compartment_id, source_details, defined_tags, display_name, freeform_tags):

    kwargs = {}

    _details = {}
    _details['availabilityDomain'] = availability_domain
    _details['compartmentId'] = compartment_id
    _details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.create_volume_group(
        create_volume_group_details=_details,
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


@volume_group_group.command(name=cli_util.override('blockstorage.create_volume_group_volume_group_source_from_volume_group_details.command_name', 'create-volume-group-volume-group-source-from-volume-group-details'), help=u"""Creates a new volume group in the specified compartment. A volume group is a collection of volumes and may be created from a list of volumes, cloning an existing volume group, or by restoring a volume group backup. A volume group can contain up to 64 volumes. You may optionally specify a *display name* for the volume group, which is simply a friendly name or description. It does not have to be unique, and you can change it. Avoid entering confidential information.

For more information, see [Volume Groups]. \n[Command Reference](createVolumeGroup)""")
@cli_util.option('--availability-domain', required=True, help=u"""The availability domain of the volume group.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment that contains the volume group.""")
@cli_util.option('--source-details-volume-group-id', required=True, help=u"""The OCID of the volume group to clone from.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name for the volume group. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'VolumeGroup'})
@cli_util.wrap_exceptions
def create_volume_group_volume_group_source_from_volume_group_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, compartment_id, source_details_volume_group_id, defined_tags, display_name, freeform_tags):

    kwargs = {}

    _details = {}
    _details['sourceDetails'] = {}
    _details['availabilityDomain'] = availability_domain
    _details['compartmentId'] = compartment_id
    _details['sourceDetails']['volumeGroupId'] = source_details_volume_group_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    _details['sourceDetails']['type'] = 'volumeGroupId'

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.create_volume_group(
        create_volume_group_details=_details,
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


@volume_group_group.command(name=cli_util.override('blockstorage.create_volume_group_volume_group_source_from_volumes_details.command_name', 'create-volume-group-volume-group-source-from-volumes-details'), help=u"""Creates a new volume group in the specified compartment. A volume group is a collection of volumes and may be created from a list of volumes, cloning an existing volume group, or by restoring a volume group backup. A volume group can contain up to 64 volumes. You may optionally specify a *display name* for the volume group, which is simply a friendly name or description. It does not have to be unique, and you can change it. Avoid entering confidential information.

For more information, see [Volume Groups]. \n[Command Reference](createVolumeGroup)""")
@cli_util.option('--availability-domain', required=True, help=u"""The availability domain of the volume group.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment that contains the volume group.""")
@cli_util.option('--source-details-volume-ids', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""OCIDs for the volumes in this volume group.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name for the volume group. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'source-details-volume-ids': {'module': 'core', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'source-details-volume-ids': {'module': 'core', 'class': 'list[string]'}}, output_type={'module': 'core', 'class': 'VolumeGroup'})
@cli_util.wrap_exceptions
def create_volume_group_volume_group_source_from_volumes_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, compartment_id, source_details_volume_ids, defined_tags, display_name, freeform_tags):

    kwargs = {}

    _details = {}
    _details['sourceDetails'] = {}
    _details['availabilityDomain'] = availability_domain
    _details['compartmentId'] = compartment_id
    _details['sourceDetails']['volumeIds'] = cli_util.parse_json_parameter("source_details_volume_ids", source_details_volume_ids)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    _details['sourceDetails']['type'] = 'volumeIds'

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.create_volume_group(
        create_volume_group_details=_details,
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


@volume_group_group.command(name=cli_util.override('blockstorage.create_volume_group_volume_group_source_from_volume_group_backup_details.command_name', 'create-volume-group-volume-group-source-from-volume-group-backup-details'), help=u"""Creates a new volume group in the specified compartment. A volume group is a collection of volumes and may be created from a list of volumes, cloning an existing volume group, or by restoring a volume group backup. A volume group can contain up to 64 volumes. You may optionally specify a *display name* for the volume group, which is simply a friendly name or description. It does not have to be unique, and you can change it. Avoid entering confidential information.

For more information, see [Volume Groups]. \n[Command Reference](createVolumeGroup)""")
@cli_util.option('--availability-domain', required=True, help=u"""The availability domain of the volume group.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment that contains the volume group.""")
@cli_util.option('--source-details-volume-group-backup-id', required=True, help=u"""The OCID of the volume group backup to restore from.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name for the volume group. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'VolumeGroup'})
@cli_util.wrap_exceptions
def create_volume_group_volume_group_source_from_volume_group_backup_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, compartment_id, source_details_volume_group_backup_id, defined_tags, display_name, freeform_tags):

    kwargs = {}

    _details = {}
    _details['sourceDetails'] = {}
    _details['availabilityDomain'] = availability_domain
    _details['compartmentId'] = compartment_id
    _details['sourceDetails']['volumeGroupBackupId'] = source_details_volume_group_backup_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    _details['sourceDetails']['type'] = 'volumeGroupBackupId'

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.create_volume_group(
        create_volume_group_details=_details,
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


@volume_group_backup_group.command(name=cli_util.override('blockstorage.create_volume_group_backup.command_name', 'create'), help=u"""Creates a new backup volume group of the specified volume group. For more information, see [Volume Groups]. \n[Command Reference](createVolumeGroupBackup)""")
@cli_util.option('--volume-group-id', required=True, help=u"""The OCID of the volume group that needs to be backed up.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment that will contain the volume group backup. This parameter is optional, by default backup will be created in the same compartment and source volume group.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name for the volume group backup. Does not have to be unique and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["FULL", "INCREMENTAL"]), help=u"""The type of backup to create. If omitted, defaults to incremental.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "COMMITTED", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'VolumeGroupBackup'})
@cli_util.wrap_exceptions
def create_volume_group_backup(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, volume_group_id, compartment_id, defined_tags, display_name, freeform_tags, type):

    kwargs = {}

    _details = {}
    _details['volumeGroupId'] = volume_group_id

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if type is not None:
        _details['type'] = type

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.create_volume_group_backup(
        create_volume_group_backup_details=_details,
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


@boot_volume_group.command(name=cli_util.override('blockstorage.delete_boot_volume.command_name', 'delete'), help=u"""Deletes the specified boot volume. The volume cannot have an active connection to an instance. To disconnect the boot volume from a connected instance, see [Disconnecting From a Boot Volume]. **Warning:** All data on the boot volume will be permanently lost when the boot volume is deleted. \n[Command Reference](deleteBootVolume)""")
@cli_util.option('--boot-volume-id', required=True, help=u"""The OCID of the boot volume.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
    client = cli_util.build_client('core', 'blockstorage', ctx)
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


@boot_volume_backup_group.command(name=cli_util.override('blockstorage.delete_boot_volume_backup.command_name', 'delete'), help=u"""Deletes a boot volume backup. \n[Command Reference](deleteBootVolumeBackup)""")
@cli_util.option('--boot-volume-backup-id', required=True, help=u"""The OCID of the boot volume backup.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
    client = cli_util.build_client('core', 'blockstorage', ctx)
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


@boot_volume_kms_key_group.command(name=cli_util.override('blockstorage.delete_boot_volume_kms_key.command_name', 'delete'), help=u"""Removes the specified boot volume's assigned Key Management encryption key. \n[Command Reference](deleteBootVolumeKmsKey)""")
@cli_util.option('--boot-volume-id', required=True, help=u"""The OCID of the boot volume.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
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
    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.delete_boot_volume_kms_key(
        boot_volume_id=boot_volume_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_group.command(name=cli_util.override('blockstorage.delete_volume.command_name', 'delete'), help=u"""Deletes the specified volume. The volume cannot have an active connection to an instance. To disconnect the volume from a connected instance, see [Disconnecting From a Volume]. **Warning:** All data on the volume will be permanently lost when the volume is deleted. \n[Command Reference](deleteVolume)""")
@cli_util.option('--volume-id', required=True, help=u"""The OCID of the volume.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
    client = cli_util.build_client('core', 'blockstorage', ctx)
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


@volume_backup_group.command(name=cli_util.override('blockstorage.delete_volume_backup.command_name', 'delete'), help=u"""Deletes a volume backup. \n[Command Reference](deleteVolumeBackup)""")
@cli_util.option('--volume-backup-id', required=True, help=u"""The OCID of the volume backup.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
    client = cli_util.build_client('core', 'blockstorage', ctx)
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


@volume_backup_policy_group.command(name=cli_util.override('blockstorage.delete_volume_backup_policy.command_name', 'delete'), help=u"""Deletes a user defined backup policy.  For more information about user defined backup policies,  see [Policy-Based Backups].

 Avoid entering confidential information. \n[Command Reference](deleteVolumeBackupPolicy)""")
@cli_util.option('--policy-id', required=True, help=u"""The OCID of the volume backup policy.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_volume_backup_policy(ctx, from_json, policy_id, if_match):

    if isinstance(policy_id, six.string_types) and len(policy_id.strip()) == 0:
        raise click.UsageError('Parameter --policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.delete_volume_backup_policy(
        policy_id=policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_backup_policy_assignment_group.command(name=cli_util.override('blockstorage.delete_volume_backup_policy_assignment.command_name', 'delete'), help=u"""Deletes a volume backup policy assignment. \n[Command Reference](deleteVolumeBackupPolicyAssignment)""")
@cli_util.option('--policy-assignment-id', required=True, help=u"""The OCID of the volume backup policy assignment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
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
    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.delete_volume_backup_policy_assignment(
        policy_assignment_id=policy_assignment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_group_group.command(name=cli_util.override('blockstorage.delete_volume_group.command_name', 'delete'), help=u"""Deletes the specified volume group. Individual volumes are not deleted, only the volume group is deleted. For more information, see [Volume Groups]. \n[Command Reference](deleteVolumeGroup)""")
@cli_util.option('--volume-group-id', required=True, help=u"""The Oracle Cloud ID (OCID) that uniquely identifies the volume group.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
    client = cli_util.build_client('core', 'blockstorage', ctx)
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


@volume_group_backup_group.command(name=cli_util.override('blockstorage.delete_volume_group_backup.command_name', 'delete'), help=u"""Deletes a volume group backup. This operation deletes all the backups in the volume group. For more information, see [Volume Groups]. \n[Command Reference](deleteVolumeGroupBackup)""")
@cli_util.option('--volume-group-backup-id', required=True, help=u"""The Oracle Cloud ID (OCID) that uniquely identifies the volume group backup.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "COMMITTED", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
    client = cli_util.build_client('core', 'blockstorage', ctx)
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


@volume_kms_key_group.command(name=cli_util.override('blockstorage.delete_volume_kms_key.command_name', 'delete'), help=u"""Removes the specified volume's assigned Key Management encryption key. \n[Command Reference](deleteVolumeKmsKey)""")
@cli_util.option('--volume-id', required=True, help=u"""The OCID of the volume.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
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
    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.delete_volume_kms_key(
        volume_id=volume_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@boot_volume_group.command(name=cli_util.override('blockstorage.get_boot_volume.command_name', 'get'), help=u"""Gets information for the specified boot volume. \n[Command Reference](getBootVolume)""")
@cli_util.option('--boot-volume-id', required=True, help=u"""The OCID of the boot volume.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'BootVolume'})
@cli_util.wrap_exceptions
def get_boot_volume(ctx, from_json, boot_volume_id):

    if isinstance(boot_volume_id, six.string_types) and len(boot_volume_id.strip()) == 0:
        raise click.UsageError('Parameter --boot-volume-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.get_boot_volume(
        boot_volume_id=boot_volume_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@boot_volume_backup_group.command(name=cli_util.override('blockstorage.get_boot_volume_backup.command_name', 'get'), help=u"""Gets information for the specified boot volume backup. \n[Command Reference](getBootVolumeBackup)""")
@cli_util.option('--boot-volume-backup-id', required=True, help=u"""The OCID of the boot volume backup.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'BootVolumeBackup'})
@cli_util.wrap_exceptions
def get_boot_volume_backup(ctx, from_json, boot_volume_backup_id):

    if isinstance(boot_volume_backup_id, six.string_types) and len(boot_volume_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --boot-volume-backup-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.get_boot_volume_backup(
        boot_volume_backup_id=boot_volume_backup_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@boot_volume_kms_key_group.command(name=cli_util.override('blockstorage.get_boot_volume_kms_key.command_name', 'get'), help=u"""Gets the Key Management encryption key assigned to the specified boot volume. \n[Command Reference](getBootVolumeKmsKey)""")
@cli_util.option('--boot-volume-id', required=True, help=u"""The OCID of the boot volume.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
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
    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.get_boot_volume_kms_key(
        boot_volume_id=boot_volume_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_group.command(name=cli_util.override('blockstorage.get_volume.command_name', 'get'), help=u"""Gets information for the specified volume. \n[Command Reference](getVolume)""")
@cli_util.option('--volume-id', required=True, help=u"""The OCID of the volume.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Volume'})
@cli_util.wrap_exceptions
def get_volume(ctx, from_json, volume_id):

    if isinstance(volume_id, six.string_types) and len(volume_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.get_volume(
        volume_id=volume_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_backup_group.command(name=cli_util.override('blockstorage.get_volume_backup.command_name', 'get'), help=u"""Gets information for the specified volume backup. \n[Command Reference](getVolumeBackup)""")
@cli_util.option('--volume-backup-id', required=True, help=u"""The OCID of the volume backup.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VolumeBackup'})
@cli_util.wrap_exceptions
def get_volume_backup(ctx, from_json, volume_backup_id):

    if isinstance(volume_backup_id, six.string_types) and len(volume_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-backup-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.get_volume_backup(
        volume_backup_id=volume_backup_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_backup_policy_group.command(name=cli_util.override('blockstorage.get_volume_backup_policy.command_name', 'get'), help=u"""Gets information for the specified volume backup policy. \n[Command Reference](getVolumeBackupPolicy)""")
@cli_util.option('--policy-id', required=True, help=u"""The OCID of the volume backup policy.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VolumeBackupPolicy'})
@cli_util.wrap_exceptions
def get_volume_backup_policy(ctx, from_json, policy_id):

    if isinstance(policy_id, six.string_types) and len(policy_id.strip()) == 0:
        raise click.UsageError('Parameter --policy-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.get_volume_backup_policy(
        policy_id=policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_backup_policy_assignment_group.command(name=cli_util.override('blockstorage.get_volume_backup_policy_asset_assignment.command_name', 'get-volume-backup-policy-asset-assignment'), help=u"""Gets the volume backup policy assignment for the specified volume. The `assetId` query parameter is required, and the returned list will contain at most one item, since volume can only have one volume backup policy assigned at a time. \n[Command Reference](getVolumeBackupPolicyAssetAssignment)""")
@cli_util.option('--asset-id', required=True, help=u"""The OCID of an asset (e.g. a volume).""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
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
    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.get_volume_backup_policy_asset_assignment(
        asset_id=asset_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_backup_policy_assignment_group.command(name=cli_util.override('blockstorage.get_volume_backup_policy_assignment.command_name', 'get'), help=u"""Gets information for the specified volume backup policy assignment. \n[Command Reference](getVolumeBackupPolicyAssignment)""")
@cli_util.option('--policy-assignment-id', required=True, help=u"""The OCID of the volume backup policy assignment.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VolumeBackupPolicyAssignment'})
@cli_util.wrap_exceptions
def get_volume_backup_policy_assignment(ctx, from_json, policy_assignment_id):

    if isinstance(policy_assignment_id, six.string_types) and len(policy_assignment_id.strip()) == 0:
        raise click.UsageError('Parameter --policy-assignment-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.get_volume_backup_policy_assignment(
        policy_assignment_id=policy_assignment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_group_group.command(name=cli_util.override('blockstorage.get_volume_group.command_name', 'get'), help=u"""Gets information for the specified volume group. For more information, see [Volume Groups]. \n[Command Reference](getVolumeGroup)""")
@cli_util.option('--volume-group-id', required=True, help=u"""The Oracle Cloud ID (OCID) that uniquely identifies the volume group.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VolumeGroup'})
@cli_util.wrap_exceptions
def get_volume_group(ctx, from_json, volume_group_id):

    if isinstance(volume_group_id, six.string_types) and len(volume_group_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-group-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.get_volume_group(
        volume_group_id=volume_group_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_group_backup_group.command(name=cli_util.override('blockstorage.get_volume_group_backup.command_name', 'get'), help=u"""Gets information for the specified volume group backup. For more information, see [Volume Groups]. \n[Command Reference](getVolumeGroupBackup)""")
@cli_util.option('--volume-group-backup-id', required=True, help=u"""The Oracle Cloud ID (OCID) that uniquely identifies the volume group backup.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VolumeGroupBackup'})
@cli_util.wrap_exceptions
def get_volume_group_backup(ctx, from_json, volume_group_backup_id):

    if isinstance(volume_group_backup_id, six.string_types) and len(volume_group_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-group-backup-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.get_volume_group_backup(
        volume_group_backup_id=volume_group_backup_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_kms_key_group.command(name=cli_util.override('blockstorage.get_volume_kms_key.command_name', 'get'), help=u"""Gets the Key Management encryption key assigned to the specified volume. \n[Command Reference](getVolumeKmsKey)""")
@cli_util.option('--volume-id', required=True, help=u"""The OCID of the volume.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
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
    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.get_volume_kms_key(
        volume_id=volume_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@boot_volume_backup_group.command(name=cli_util.override('blockstorage.list_boot_volume_backups.command_name', 'list'), help=u"""Lists the boot volume backups in the specified compartment. You can filter the results by boot volume. \n[Command Reference](listBootVolumeBackups)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--boot-volume-id', help=u"""The OCID of the boot volume.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--source-boot-volume-backup-id', help=u"""A filter to return only resources that originated from the given source boot volume backup.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), help=u"""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[BootVolumeBackup]'})
@cli_util.wrap_exceptions
def list_boot_volume_backups(ctx, from_json, all_pages, page_size, compartment_id, boot_volume_id, limit, page, display_name, source_boot_volume_backup_id, sort_by, sort_order, lifecycle_state):

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
    if source_boot_volume_backup_id is not None:
        kwargs['source_boot_volume_backup_id'] = source_boot_volume_backup_id
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('core', 'blockstorage', ctx)
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


@boot_volume_group.command(name=cli_util.override('blockstorage.list_boot_volumes.command_name', 'list'), help=u"""Lists the boot volumes in the specified compartment and availability domain. \n[Command Reference](listBootVolumes)""")
@cli_util.option('--availability-domain', required=True, help=u"""The name of the availability domain.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--volume-group-id', help=u"""The OCID of the volume group.""")
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
    client = cli_util.build_client('core', 'blockstorage', ctx)
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


@volume_backup_policy_group.command(name=cli_util.override('blockstorage.list_volume_backup_policies.command_name', 'list'), help=u"""Lists all the volume backup policies available in the specified compartment.

For more information about Oracle defined backup policies and user defined backup policies, see [Policy-Based Backups]. \n[Command Reference](listVolumeBackupPolicies)""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment. If no compartment is specified, the Oracle defined backup policies are listed.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[VolumeBackupPolicy]'})
@cli_util.wrap_exceptions
def list_volume_backup_policies(ctx, from_json, all_pages, page_size, limit, page, compartment_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    client = cli_util.build_client('core', 'blockstorage', ctx)
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


@volume_backup_group.command(name=cli_util.override('blockstorage.list_volume_backups.command_name', 'list'), help=u"""Lists the volume backups in the specified compartment. You can filter the results by volume. \n[Command Reference](listVolumeBackups)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--volume-id', help=u"""The OCID of the volume.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--source-volume-backup-id', help=u"""A filter to return only resources that originated from the given source volume backup.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), help=u"""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
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
    client = cli_util.build_client('core', 'blockstorage', ctx)
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


@volume_group_backup_group.command(name=cli_util.override('blockstorage.list_volume_group_backups.command_name', 'list'), help=u"""Lists the volume group backups in the specified compartment. You can filter the results by volume group. For more information, see [Volume Groups]. \n[Command Reference](listVolumeGroupBackups)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--volume-group-id', help=u"""The OCID of the volume group.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
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
    client = cli_util.build_client('core', 'blockstorage', ctx)
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


@volume_group_group.command(name=cli_util.override('blockstorage.list_volume_groups.command_name', 'list'), help=u"""Lists the volume groups in the specified compartment and availability domain. For more information, see [Volume Groups]. \n[Command Reference](listVolumeGroups)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--availability-domain', help=u"""The name of the availability domain.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), help=u"""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
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
    client = cli_util.build_client('core', 'blockstorage', ctx)
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


@volume_group.command(name=cli_util.override('blockstorage.list_volumes.command_name', 'list'), help=u"""Lists the volumes in the specified compartment and availability domain. \n[Command Reference](listVolumes)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--availability-domain', help=u"""The name of the availability domain.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--volume-group-id', help=u"""The OCID of the volume group.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), help=u"""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
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
    client = cli_util.build_client('core', 'blockstorage', ctx)
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


@boot_volume_group.command(name=cli_util.override('blockstorage.update_boot_volume.command_name', 'update'), help=u"""Updates the specified boot volume's display name, defined tags, and free-form tags. \n[Command Reference](updateBootVolume)""")
@cli_util.option('--boot-volume-id', required=True, help=u"""The OCID of the boot volume.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--size-in-gbs', type=click.INT, help=u"""The size to resize the volume to in GBs. Has to be larger than the current size.""")
@cli_util.option('--vpus-per-gb', type=click.INT, help=u"""The number of volume performance units (VPUs) that will be applied to this volume per GB, representing the Block Volume service's elastic performance options. See [Block Volume Elastic Performance] for more information.

Allowed values:

  * `10`: Represents Balanced option.

  * `20`: Represents Higher Performance option.""")
@cli_util.option('--is-auto-tune-enabled', type=click.BOOL, help=u"""Specifies whether the auto-tune performance is enabled for this boot volume.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'BootVolume'})
@cli_util.wrap_exceptions
def update_boot_volume(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, boot_volume_id, defined_tags, display_name, freeform_tags, size_in_gbs, vpus_per_gb, is_auto_tune_enabled, if_match):

    if isinstance(boot_volume_id, six.string_types) and len(boot_volume_id.strip()) == 0:
        raise click.UsageError('Parameter --boot-volume-id cannot be whitespace or empty string')
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

    if size_in_gbs is not None:
        _details['sizeInGBs'] = size_in_gbs

    if vpus_per_gb is not None:
        _details['vpusPerGB'] = vpus_per_gb

    if is_auto_tune_enabled is not None:
        _details['isAutoTuneEnabled'] = is_auto_tune_enabled

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.update_boot_volume(
        boot_volume_id=boot_volume_id,
        update_boot_volume_details=_details,
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


@boot_volume_backup_group.command(name=cli_util.override('blockstorage.update_boot_volume_backup.command_name', 'update'), help=u"""Updates the display name for the specified boot volume backup. Avoid entering confidential information. \n[Command Reference](updateBootVolumeBackup)""")
@cli_util.option('--boot-volume-backup-id', required=True, help=u"""The OCID of the boot volume backup.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A friendly user-specified name for the boot volume backup. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.update_boot_volume_backup(
        boot_volume_backup_id=boot_volume_backup_id,
        update_boot_volume_backup_details=_details,
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


@boot_volume_kms_key_group.command(name=cli_util.override('blockstorage.update_boot_volume_kms_key.command_name', 'update'), help=u"""Updates the specified volume with a new Key Management master encryption key. \n[Command Reference](updateBootVolumeKmsKey)""")
@cli_util.option('--boot-volume-id', required=True, help=u"""The OCID of the boot volume.""")
@cli_util.option('--kms-key-id', help=u"""The OCID of the new Key Management key to assign to protect the specified volume. This key has to be a valid Key Management key, and policies must exist to allow the user and the Block Volume service to access this key. If you specify the same OCID as the previous key's OCID, the Block Volume service will use it to regenerate a volume encryption key.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
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

    _details = {}

    if kms_key_id is not None:
        _details['kmsKeyId'] = kms_key_id

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.update_boot_volume_kms_key(
        boot_volume_id=boot_volume_id,
        update_boot_volume_kms_key_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_group.command(name=cli_util.override('blockstorage.update_volume.command_name', 'update'), help=u"""Updates the specified volume's display name. Avoid entering confidential information. \n[Command Reference](updateVolume)""")
@cli_util.option('--volume-id', required=True, help=u"""The OCID of the volume.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vpus-per-gb', type=click.INT, help=u"""The number of volume performance units (VPUs) that will be applied to this volume per GB, representing the Block Volume service's elastic performance options. See [Block Volume Elastic Performance] for more information.

Allowed values:

  * `0`: Represents Lower Cost option.

  * `10`: Represents Balanced option.

  * `20`: Represents Higher Performance option.""")
@cli_util.option('--size-in-gbs', type=click.INT, help=u"""The size to resize the volume to in GBs. Has to be larger than the current size.""")
@cli_util.option('--is-auto-tune-enabled', type=click.BOOL, help=u"""Specifies whether the auto-tune performance is enabled for this volume.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'Volume'})
@cli_util.wrap_exceptions
def update_volume(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, volume_id, defined_tags, display_name, freeform_tags, vpus_per_gb, size_in_gbs, is_auto_tune_enabled, if_match):

    if isinstance(volume_id, six.string_types) and len(volume_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-id cannot be whitespace or empty string')
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

    if vpus_per_gb is not None:
        _details['vpusPerGB'] = vpus_per_gb

    if size_in_gbs is not None:
        _details['sizeInGBs'] = size_in_gbs

    if is_auto_tune_enabled is not None:
        _details['isAutoTuneEnabled'] = is_auto_tune_enabled

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.update_volume(
        volume_id=volume_id,
        update_volume_details=_details,
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


@volume_backup_group.command(name=cli_util.override('blockstorage.update_volume_backup.command_name', 'update'), help=u"""Updates the display name for the specified volume backup. Avoid entering confidential information. \n[Command Reference](updateVolumeBackup)""")
@cli_util.option('--volume-backup-id', required=True, help=u"""The OCID of the volume backup.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name for the volume backup. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.update_volume_backup(
        volume_backup_id=volume_backup_id,
        update_volume_backup_details=_details,
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


@volume_backup_policy_group.command(name=cli_util.override('blockstorage.update_volume_backup_policy.command_name', 'update'), help=u"""Updates a user defined backup policy.  For more information about user defined backup policies,  see [Policy-Based Backups].

 Avoid entering confidential information. \n[Command Reference](updateVolumeBackupPolicy)""")
@cli_util.option('--policy-id', required=True, help=u"""The OCID of the volume backup policy.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the volume backup policy. Does not have to be unique and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--destination-region', help=u"""The paired destination region for copying scheduled backups to. Example: `us-ashburn-1`. Specify `none` to reset the `destinationRegion` parameter. See [Region Pairs] for details about paired regions.""")
@cli_util.option('--schedules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The collection of schedules for the volume backup policy. See see [Schedules] in [Policy-Based Backups] for more information.

This option is a JSON list with items of type VolumeBackupSchedule.  For documentation on VolumeBackupSchedule please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/VolumeBackupSchedule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'schedules': {'module': 'core', 'class': 'list[VolumeBackupSchedule]'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'schedules': {'module': 'core', 'class': 'list[VolumeBackupSchedule]'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'VolumeBackupPolicy'})
@cli_util.wrap_exceptions
def update_volume_backup_policy(ctx, from_json, force, policy_id, display_name, destination_region, schedules, defined_tags, freeform_tags, if_match):

    if isinstance(policy_id, six.string_types) and len(policy_id.strip()) == 0:
        raise click.UsageError('Parameter --policy-id cannot be whitespace or empty string')
    if not force:
        if schedules or defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to schedules and defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if destination_region is not None:
        _details['destinationRegion'] = destination_region

    if schedules is not None:
        _details['schedules'] = cli_util.parse_json_parameter("schedules", schedules)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.update_volume_backup_policy(
        policy_id=policy_id,
        update_volume_backup_policy_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_group_group.command(name=cli_util.override('blockstorage.update_volume_group.command_name', 'update'), help=u"""Updates the set of volumes in a volume group along with the display name. Use this operation to add or remove volumes in a volume group. Specify the full list of volume IDs to include in the volume group. If the volume ID is not specified in the call, it will be removed from the volume group. Avoid entering confidential information.

For more information, see [Volume Groups]. \n[Command Reference](updateVolumeGroup)""")
@cli_util.option('--volume-group-id', required=True, help=u"""The Oracle Cloud ID (OCID) that uniquely identifies the volume group.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name for the volume group. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--volume-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""OCIDs for the volumes in this volume group.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if volume_ids is not None:
        _details['volumeIds'] = cli_util.parse_json_parameter("volume_ids", volume_ids)

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.update_volume_group(
        volume_group_id=volume_group_id,
        update_volume_group_details=_details,
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


@volume_group_backup_group.command(name=cli_util.override('blockstorage.update_volume_group_backup.command_name', 'update'), help=u"""Updates the display name for the specified volume group backup. For more information, see [Volume Groups]. \n[Command Reference](updateVolumeGroupBackup)""")
@cli_util.option('--volume-group-backup-id', required=True, help=u"""The Oracle Cloud ID (OCID) that uniquely identifies the volume group backup.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name for the volume group backup. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "COMMITTED", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.update_volume_group_backup(
        volume_group_backup_id=volume_group_backup_id,
        update_volume_group_backup_details=_details,
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


@volume_kms_key_group.command(name=cli_util.override('blockstorage.update_volume_kms_key.command_name', 'update'), help=u"""Updates the specified volume with a new Key Management master encryption key. \n[Command Reference](updateVolumeKmsKey)""")
@cli_util.option('--volume-id', required=True, help=u"""The OCID of the volume.""")
@cli_util.option('--kms-key-id', help=u"""The OCID of the new Key Management key to assign to protect the specified volume. This key has to be a valid Key Management key, and policies must exist to allow the user and the Block Volume service to access this key. If you specify the same OCID as the previous key's OCID, the Block Volume service will use it to regenerate a volume encryption key.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
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

    _details = {}

    if kms_key_id is not None:
        _details['kmsKeyId'] = kms_key_id

    client = cli_util.build_client('core', 'blockstorage', ctx)
    result = client.update_volume_kms_key(
        volume_id=volume_id,
        update_volume_kms_key_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
