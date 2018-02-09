# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

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


@cli.command(cli_util.override('blockstorage_group.command_name', 'blockstorage'), cls=CommandGroupWithAlias, help=cli_util.override('blockstorage_group.help', """APIs for Networking Service, Compute Service, and Block Volume Service."""))
@cli_util.help_option_group
def blockstorage_group():
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


@click.command(cli_util.override('boot_volume_group.command_name', 'boot-volume'), cls=CommandGroupWithAlias, help="""A detachable boot volume device that contains the image used to boot an Compute instance. For more information, see
[Overview of Boot Volumes].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access, see
[Getting Started with Policies].""")
@cli_util.help_option_group
def boot_volume_group():
    pass


@click.command(cli_util.override('volume_backup_group.command_name', 'volume-backup'), cls=CommandGroupWithAlias, help="""A point-in-time copy of a volume that can then be used to create a new block volume
or recover a block volume. For more information, see
[Overview of Cloud Volume Storage].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access, see
[Getting Started with Policies].""")
@cli_util.help_option_group
def volume_backup_group():
    pass


@click.command(cli_util.override('volume_backup_policy_assignment_group.command_name', 'volume-backup-policy-assignment'), cls=CommandGroupWithAlias, help="""Specifies that a particular volume backup policy is assigned to an asset such as a volume.""")
@cli_util.help_option_group
def volume_backup_policy_assignment_group():
    pass


@click.command(cli_util.override('volume_backup_policy_group.command_name', 'volume-backup-policy'), cls=CommandGroupWithAlias, help="""A policy for automatically creating volume backups according to a recurring schedule. Has a set of one or more schedules that control when and how backups are created.""")
@cli_util.help_option_group
def volume_backup_policy_group():
    pass


@volume_group.command(name=cli_util.override('create_volume.command_name', 'create'), help="""Creates a new volume in the specified compartment. Volumes can be created in sizes ranging from 50 GB (51200 MB) to 16 TB (16777216 MB), in 1 GB (1024 MB) increments. By default, volumes are 1 TB (1048576 MB). For general information about block volumes, see [Overview of Block Volume Service].

A volume and instance can be in separate compartments but must be in the same Availability Domain. For information about access control and compartments, see [Overview of the IAM Service]. For information about Availability Domains, see [Regions and Availability Domains]. To get a list of Availability Domains, use the `ListAvailabilityDomains` operation in the Identity and Access Management Service API.

You may optionally specify a *display name* for the volume, which is simply a friendly name or description. It does not have to be unique, and you can change it. Avoid entering confidential information.""")
@click.option('--availability-domain', callback=cli_util.handle_required_param, help="""The Availability Domain of the volume.

Example: `Uocm:PHX-AD-1` [required]""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The OCID of the compartment that contains the volume. [required]""")
@click.option('--backup-policy-id', callback=cli_util.handle_optional_param, help="""If provided, specifies the ID of the volume backup policy to assign to the newly created volume. If omitted, no policy will be assigned.""")
@click.option('--defined-tags', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--display-name', callback=cli_util.handle_optional_param, help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@click.option('--freeform-tags', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--size-in-gbs', callback=cli_util.handle_optional_param, type=click.INT, help="""The size of the volume in GBs.""")
@click.option('--size-in-mbs', callback=cli_util.handle_optional_param, type=click.INT, help="""The size of the volume in MBs. The value must be a multiple of 1024. This field is deprecated. Use sizeInGBs instead.""")
@click.option('--source-details', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Specifies the volume source details for a new Block volume. The volume source is either another Block volume in the same Availability Domain or a Block volume backup. This is an optional field. If not specified or set to null, the new Block volume will be empty. When specified, the new Block volume will contain data from the source volume or backup.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--volume-backup-id', callback=cli_util.handle_optional_param, help="""The OCID of the volume backup from which the data should be restored on the newly created volume. This field is deprecated. Use the sourceDetails field instead to specify the backup for the volume.""")
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'source-details': {'module': 'core', 'class': 'VolumeSourceDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'source-details': {'module': 'core', 'class': 'VolumeSourceDetails'}}, output_type={'module': 'core', 'class': 'Volume'})
@cli_util.wrap_exceptions
def create_volume(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, compartment_id, backup_policy_id, defined_tags, display_name, freeform_tags, size_in_gbs, size_in_mbs, source_details, volume_backup_id):
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
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_volume, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@volume_backup_group.command(name=cli_util.override('create_volume_backup.command_name', 'create'), help="""Creates a new backup of the specified volume. For general information about volume backups, see [Overview of Block Volume Service Backups]

When the request is received, the backup object is in a REQUEST_RECEIVED state. When the data is imaged, it goes into a CREATING state. After the backup is fully uploaded to the cloud, it goes into an AVAILABLE state.""")
@click.option('--volume-id', callback=cli_util.handle_required_param, help="""The OCID of the volume that needs to be backed up. [required]""")
@click.option('--defined-tags', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--display-name', callback=cli_util.handle_optional_param, help="""A user-friendly name for the volume backup. Does not have to be unique and it's changeable. Avoid entering confidential information.""")
@click.option('--freeform-tags', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--type', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["FULL", "INCREMENTAL"]), help="""The type of backup to create. If omitted, defaults to INCREMENTAL.""")
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
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
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_volume_backup, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@volume_backup_policy_assignment_group.command(name=cli_util.override('create_volume_backup_policy_assignment.command_name', 'create'), help="""Assigns a policy to the specified asset, such as a volume. Note that a given asset can only have one policy assigned to it; if this method is called for an asset that previously has a different policy assigned, the prior assignment will be silently deleted.""")
@click.option('--asset-id', callback=cli_util.handle_required_param, help="""The OCID of the asset (e.g. a volume) to which to assign the policy. [required]""")
@click.option('--policy-id', callback=cli_util.handle_required_param, help="""The OCID of the volume backup policy to assign to an asset. [required]""")
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


@boot_volume_group.command(name=cli_util.override('delete_boot_volume.command_name', 'delete'), help="""Deletes the specified boot volume. The volume cannot have an active connection to an instance. To disconnect the boot volume from a connected instance, see [Disconnecting From a Boot Volume]. **Warning:** All data on the boot volume will be permanently lost when the boot volume is deleted.""")
@click.option('--boot-volume-id', callback=cli_util.handle_required_param, help="""The OCID of the boot volume. [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
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
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_boot_volume, boot_volume_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@volume_group.command(name=cli_util.override('delete_volume.command_name', 'delete'), help="""Deletes the specified volume. The volume cannot have an active connection to an instance. To disconnect the volume from a connected instance, see [Disconnecting From a Volume]. **Warning:** All data on the volume will be permanently lost when the volume is deleted.""")
@click.option('--volume-id', callback=cli_util.handle_required_param, help="""The OCID of the volume. [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
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
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_volume, volume_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@volume_backup_group.command(name=cli_util.override('delete_volume_backup.command_name', 'delete'), help="""Deletes a volume backup.""")
@click.option('--volume-backup-id', callback=cli_util.handle_required_param, help="""The OCID of the volume backup. [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
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
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_volume_backup, volume_backup_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@volume_backup_policy_assignment_group.command(name=cli_util.override('delete_volume_backup_policy_assignment.command_name', 'delete'), help="""Deletes a volume backup policy assignment (i.e. unassigns the policy from an asset).""")
@click.option('--policy-assignment-id', callback=cli_util.handle_required_param, help="""The OCID of the volume backup policy assignment. [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
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


@boot_volume_group.command(name=cli_util.override('get_boot_volume.command_name', 'get'), help="""Gets information for the specified boot volume.""")
@click.option('--boot-volume-id', callback=cli_util.handle_required_param, help="""The OCID of the boot volume. [required]""")
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


@volume_group.command(name=cli_util.override('get_volume.command_name', 'get'), help="""Gets information for the specified volume.""")
@click.option('--volume-id', callback=cli_util.handle_required_param, help="""The OCID of the volume. [required]""")
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
@click.option('--volume-backup-id', callback=cli_util.handle_required_param, help="""The OCID of the volume backup. [required]""")
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
@click.option('--policy-id', callback=cli_util.handle_required_param, help="""The OCID of the volume backup policy. [required]""")
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
@click.option('--asset-id', callback=cli_util.handle_required_param, help="""The OCID of an asset (e.g. a volume). [required]""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
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
@click.option('--policy-assignment-id', callback=cli_util.handle_required_param, help="""The OCID of the volume backup policy assignment. [required]""")
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


@boot_volume_group.command(name=cli_util.override('list_boot_volumes.command_name', 'list'), help="""Lists the boot volumes in the specified compartment and Availability Domain.""")
@click.option('--availability-domain', callback=cli_util.handle_required_param, help="""The name of the Availability Domain.

Example: `Uocm:PHX-AD-1` [required]""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The OCID of the compartment. [required]""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[BootVolume]'})
@cli_util.wrap_exceptions
def list_boot_volumes(ctx, from_json, all_pages, page_size, availability_domain, compartment_id, limit, page):

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

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_boot_volumes,
            availability_domain=availability_domain,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
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

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_volume_backup_policies,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The OCID of the compartment. [required]""")
@click.option('--volume-id', callback=cli_util.handle_optional_param, help="""The OCID of the volume.""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--display-name', callback=cli_util.handle_optional_param, help="""A filter to return only resources that match the given display name exactly.""")
@click.option('--sort-by', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by Availability Domain if the scope of the resource type is within a single Availability Domain. If you call one of these \"List\" operations without specifying an Availability Domain, the resources are grouped by Availability Domain, then sorted.""")
@click.option('--sort-order', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@click.option('--lifecycle-state', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), help="""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[VolumeBackup]'})
@cli_util.wrap_exceptions
def list_volume_backups(ctx, from_json, all_pages, page_size, compartment_id, volume_id, limit, page, display_name, sort_by, sort_order, lifecycle_state):

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

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_volume_backups,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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


@volume_group.command(name=cli_util.override('list_volumes.command_name', 'list'), help="""Lists the volumes in the specified compartment and Availability Domain.""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The OCID of the compartment. [required]""")
@click.option('--availability-domain', callback=cli_util.handle_optional_param, help="""The name of the Availability Domain.

Example: `Uocm:PHX-AD-1`""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--display-name', callback=cli_util.handle_optional_param, help="""A filter to return only resources that match the given display name exactly.""")
@click.option('--sort-by', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by Availability Domain if the scope of the resource type is within a single Availability Domain. If you call one of these \"List\" operations without specifying an Availability Domain, the resources are grouped by Availability Domain, then sorted.""")
@click.option('--sort-order', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@click.option('--lifecycle-state', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), help="""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[Volume]'})
@cli_util.wrap_exceptions
def list_volumes(ctx, from_json, all_pages, page_size, compartment_id, availability_domain, limit, page, display_name, sort_by, sort_order, lifecycle_state):

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

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_volumes,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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


@boot_volume_group.command(name=cli_util.override('update_boot_volume.command_name', 'update'), help="""Updates the specified boot volume's display name.""")
@click.option('--boot-volume-id', callback=cli_util.handle_required_param, help="""The OCID of the boot volume. [required]""")
@click.option('--display-name', callback=cli_util.handle_optional_param, help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'BootVolume'})
@cli_util.wrap_exceptions
def update_boot_volume(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, boot_volume_id, display_name, if_match):

    if isinstance(boot_volume_id, six.string_types) and len(boot_volume_id.strip()) == 0:
        raise click.UsageError('Parameter --boot-volume-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

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
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_boot_volume, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@volume_group.command(name=cli_util.override('update_volume.command_name', 'update'), help="""Updates the specified volume's display name. Avoid entering confidential information.""")
@click.option('--volume-id', callback=cli_util.handle_required_param, help="""The OCID of the volume. [required]""")
@click.option('--defined-tags', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--display-name', callback=cli_util.handle_optional_param, help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@click.option('--freeform-tags', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--force', callback=cli_util.handle_optional_param, help="""Perform update without prompting for confirmation.""", is_flag=True)
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'Volume'})
@cli_util.wrap_exceptions
def update_volume(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, volume_id, defined_tags, display_name, freeform_tags, if_match):

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
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_volume, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@volume_backup_group.command(name=cli_util.override('update_volume_backup.command_name', 'update'), help="""Updates the display name for the specified volume backup. Avoid entering confidential information.""")
@click.option('--volume-backup-id', callback=cli_util.handle_required_param, help="""The OCID of the volume backup. [required]""")
@click.option('--defined-tags', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--display-name', callback=cli_util.handle_optional_param, help="""A friendly user-specified name for the volume backup. Avoid entering confidential information.""")
@click.option('--freeform-tags', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--force', callback=cli_util.handle_optional_param, help="""Perform update without prompting for confirmation.""", is_flag=True)
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
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
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_volume_backup, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
