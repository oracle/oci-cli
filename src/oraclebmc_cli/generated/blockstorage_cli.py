# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
from ..cli_root import cli
from .. import cli_util


@cli.group(cli_util.override('blockstorage_group.command_name', 'blockstorage'), help=cli_util.override('blockstorage_group.help', """APIs for Networking Service, Compute Service, and Block Volume Service."""))
@cli_util.help_option_group
def blockstorage_group():
    pass


@click.group(cli_util.override('volume_group.command_name', 'volume'), help="""A detachable block volume device that allows you to dynamically expand
the storage capacity of an instance. For more information, see
[Overview of Cloud Volume Storage].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access, see
[Getting Started with Policies].""")
@cli_util.help_option_group
def volume_group():
    pass


@click.group(cli_util.override('volume_backup_group.command_name', 'volume-backup'), help="""A point-in-time copy of a volume that can then be used to create a new block volume
or recover a block volume. For more information, see
[Overview of Cloud Volume Storage].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access, see
[Getting Started with Policies].""")
@cli_util.help_option_group
def volume_backup_group():
    pass


@volume_group.command(name=cli_util.override('create_volume.command_name', 'create'), help="""Creates a new volume in the specified compartment. Volumes can be created in sizes ranging from 50 GB (51200 MB) to 2 TB (2097152 MB), in 1 GB (1024 MB) increments. By default, volumes are 1 TB (1048576 MB). For general information about block volumes, see [Overview of Block Volume Service].

A volume and instance can be in separate compartments but must be in the same Availability Domain. For information about access control and compartments, see [Overview of the IAM Service]. For information about Availability Domains, see [Regions and Availability Domains]. To get a list of Availability Domains, use the `ListAvailabilityDomains` operation in the Identity and Access Management Service API.

You may optionally specify a *display name* for the volume, which is simply a friendly name or description. It does not have to be unique, and you can change it. Avoid entering confidential information.""")
@click.option('--availability-domain', required=True, help="""The Availability Domain of the volume.

Example: `Uocm:PHX-AD-1`""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment that contains the volume.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@click.option('--size-in-mbs', help="""The size of the volume in MBs.""")
@click.option('--volume-backup-id', help="""The OCID of the volume backup from which the data should be restored on the newly created volume.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def create_volume(ctx, availability_domain, compartment_id, display_name, size_in_mbs, volume_backup_id):
    kwargs = {}

    details = {}
    details['availabilityDomain'] = availability_domain
    details['compartmentId'] = compartment_id

    if display_name is not None:
        details['displayName'] = display_name

    if size_in_mbs is not None:
        details['sizeInMBs'] = size_in_mbs

    if volume_backup_id is not None:
        details['volumeBackupId'] = volume_backup_id

    client = cli_util.build_client('blockstorage', ctx)
    result = client.create_volume(
        create_volume_details=details,
        **kwargs
    )
    cli_util.render_response(result)


@volume_backup_group.command(name=cli_util.override('create_volume_backup.command_name', 'create'), help="""Creates a new backup of the specified volume. For general information about volume backups, see [Overview of Block Volume Service Backups]

When the request is received, the backup object is in a REQUEST_RECEIVED state. When the data is imaged, it goes into a CREATING state. After the backup is fully uploaded to the cloud, it goes into an AVAILABLE state.""")
@click.option('--volume-id', required=True, help="""The OCID of the volume that needs to be backed up.""")
@click.option('--display-name', help="""A user-friendly name for the volume backup. Does not have to be unique and it's changeable. Avoid entering confidential information.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def create_volume_backup(ctx, volume_id, display_name):
    kwargs = {}

    details = {}
    details['volumeId'] = volume_id

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('blockstorage', ctx)
    result = client.create_volume_backup(
        create_volume_backup_details=details,
        **kwargs
    )
    cli_util.render_response(result)


@volume_group.command(name=cli_util.override('delete_volume.command_name', 'delete'), help="""Deletes the specified volume. The volume cannot have an active connection to an instance. To disconnect the volume from a connected instance, see [Disconnecting From a Volume]. **Warning:** All data on the volume will be permanently lost when the volume is deleted.""")
@click.option('--volume-id', required=True, help="""The OCID of the volume.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def delete_volume(ctx, volume_id, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('blockstorage', ctx)
    result = client.delete_volume(
        volume_id=volume_id,
        **kwargs
    )
    cli_util.render_response(result)


@volume_backup_group.command(name=cli_util.override('delete_volume_backup.command_name', 'delete'), help="""Deletes a volume backup.""")
@click.option('--volume-backup-id', required=True, help="""The OCID of the volume backup.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def delete_volume_backup(ctx, volume_backup_id, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('blockstorage', ctx)
    result = client.delete_volume_backup(
        volume_backup_id=volume_backup_id,
        **kwargs
    )
    cli_util.render_response(result)


@volume_group.command(name=cli_util.override('get_volume.command_name', 'get'), help="""Gets information for the specified volume.""")
@click.option('--volume-id', required=True, help="""The OCID of the volume.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def get_volume(ctx, volume_id):
    kwargs = {}
    client = cli_util.build_client('blockstorage', ctx)
    result = client.get_volume(
        volume_id=volume_id,
        **kwargs
    )
    cli_util.render_response(result)


@volume_backup_group.command(name=cli_util.override('get_volume_backup.command_name', 'get'), help="""Gets information for the specified volume backup.""")
@click.option('--volume-backup-id', required=True, help="""The OCID of the volume backup.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def get_volume_backup(ctx, volume_backup_id):
    kwargs = {}
    client = cli_util.build_client('blockstorage', ctx)
    result = client.get_volume_backup(
        volume_backup_id=volume_backup_id,
        **kwargs
    )
    cli_util.render_response(result)


@volume_backup_group.command(name=cli_util.override('list_volume_backups.command_name', 'list'), help="""Lists the volume backups in the specified compartment. You can filter the results by volume.""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@click.option('--volume-id', help="""The OCID of the volume.""")
@click.option('--limit', help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_volume_backups(ctx, compartment_id, volume_id, limit, page):
    kwargs = {}
    if volume_id is not None:
        kwargs['volume_id'] = volume_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('blockstorage', ctx)
    result = client.list_volume_backups(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result)


@volume_group.command(name=cli_util.override('list_volumes.command_name', 'list'), help="""Lists the volumes in the specified compartment and Availability Domain.""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@click.option('--availability-domain', help="""The name of the Availability Domain.

Example: `Uocm:PHX-AD-1`""")
@click.option('--limit', help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_volumes(ctx, compartment_id, availability_domain, limit, page):
    kwargs = {}
    if availability_domain is not None:
        kwargs['availability_domain'] = availability_domain
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('blockstorage', ctx)
    result = client.list_volumes(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result)


@volume_group.command(name=cli_util.override('update_volume.command_name', 'update'), help="""Updates the specified volume's display name. Avoid entering confidential information.""")
@click.option('--volume-id', required=True, help="""The OCID of the volume.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def update_volume(ctx, volume_id, display_name, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('blockstorage', ctx)
    result = client.update_volume(
        volume_id=volume_id,
        update_volume_details=details,
        **kwargs
    )
    cli_util.render_response(result)


@volume_backup_group.command(name=cli_util.override('update_volume_backup.command_name', 'update'), help="""Updates the display name for the specified volume backup. Avoid entering confidential information.""")
@click.option('--volume-backup-id', required=True, help="""The OCID of the volume backup.""")
@click.option('--display-name', help="""A friendly user-specified name for the volume backup. Avoid entering confidential information.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def update_volume_backup(ctx, volume_backup_id, display_name, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('blockstorage', ctx)
    result = client.update_volume_backup(
        volume_backup_id=volume_backup_id,
        update_volume_backup_details=details,
        **kwargs
    )
    cli_util.render_response(result)
