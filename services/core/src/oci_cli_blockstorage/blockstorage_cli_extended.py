# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
import json

from oci_cli_blockstorage.generated import blockstorage_cli

from oci_cli.cli_root import cli
from oci_cli import cli_util
from oci_cli import json_skeleton_utils

cli_util.rename_command(cli, blockstorage_cli.blockstorage_root_group, "bv")
blockstorage_cli.volume_group.commands.pop(blockstorage_cli.create_volume.name)
blockstorage_cli.boot_volume_group.commands.pop(blockstorage_cli.create_boot_volume.name)
cli_util.rename_command(blockstorage_cli.blockstorage_root_group, blockstorage_cli.volume_backup_group, "backup")
blockstorage_cli.blockstorage_root_group.help = "Block Volume Service CLI"
blockstorage_cli.blockstorage_root_group.short_help = "Block Volume Service"

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
