# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
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
from services.key_management.src.oci_cli_key_management.generated import kms_service_cli


@click.command(cli_util.override('kms_management.kms_management_root_group.command_name', 'kms-management'), cls=CommandGroupWithAlias, help=cli_util.override('kms_management.kms_management_root_group.help', """API for managing and performing operations with keys and vaults. (For the API for managing secrets, see the Vault Service
Secret Management API. For the API for retrieving secrets, see the Vault Service Secret Retrieval API.)"""), short_help=cli_util.override('kms_management.kms_management_root_group.short_help', """Vault Service Key Management API"""))
@cli_util.help_option_group
def kms_management_root_group():
    pass


@click.command(cli_util.override('kms_management.wrapping_key_group.command_name', 'wrapping-key'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def wrapping_key_group():
    pass


@click.command(cli_util.override('kms_management.key_version_group.command_name', 'key-version'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def key_version_group():
    pass


@click.command(cli_util.override('kms_management.key_group.command_name', 'key'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def key_group():
    pass


@click.command(cli_util.override('kms_management.replication_status_details_group.command_name', 'replication-status-details'), cls=CommandGroupWithAlias, help="""Details of replication status across all replica regions""")
@cli_util.help_option_group
def replication_status_details_group():
    pass


kms_service_cli.kms_service_group.add_command(kms_management_root_group)
kms_management_root_group.add_command(wrapping_key_group)
kms_management_root_group.add_command(key_version_group)
kms_management_root_group.add_command(key_group)
kms_management_root_group.add_command(replication_status_details_group)


@key_group.command(name=cli_util.override('kms_management.backup_key.command_name', 'backup'), help=u"""Backs up an encrypted file that contains all key versions and metadata of the specified key so that you can restore the key later. The file also contains the metadata of the vault that the key belonged to.

The top level --endpoint parameter must be supplied for this operation. \n[Command Reference](backupKey)""")
@cli_util.option('--key-id', required=True, help=u"""The OCID of the key.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--backup-location', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'backup-location': {'module': 'key_management', 'class': 'BackupLocation'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backup-location': {'module': 'key_management', 'class': 'BackupLocation'}}, output_type={'module': 'key_management', 'class': 'Key'})
@cli_util.wrap_exceptions
def backup_key(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, key_id, if_match, backup_location):

    if isinstance(key_id, six.string_types) and len(key_id.strip()) == 0:
        raise click.UsageError('Parameter --key-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if backup_location is not None:
        _details['backupLocation'] = cli_util.parse_json_parameter("backup_location", backup_location)

    client = cli_util.build_client('key_management', 'kms_management', ctx)
    result = client.backup_key(
        key_id=key_id,
        backup_key_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_key') and callable(getattr(client, 'get_key')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_key(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@key_group.command(name=cli_util.override('kms_management.backup_key_backup_location_bucket.command_name', 'backup-key-backup-location-bucket'), help=u"""Backs up an encrypted file that contains all key versions and metadata of the specified key so that you can restore the key later. The file also contains the metadata of the vault that the key belonged to.

The top level --endpoint parameter must be supplied for this operation. \n[Command Reference](backupKey)""")
@cli_util.option('--key-id', required=True, help=u"""The OCID of the key.""")
@cli_util.option('--backup-location-namespace', required=True, help=u"""""")
@cli_util.option('--backup-location-bucket-name', required=True, help=u"""""")
@cli_util.option('--backup-location-object-name', required=True, help=u"""""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'Key'})
@cli_util.wrap_exceptions
def backup_key_backup_location_bucket(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, key_id, backup_location_namespace, backup_location_bucket_name, backup_location_object_name, if_match):

    if isinstance(key_id, six.string_types) and len(key_id.strip()) == 0:
        raise click.UsageError('Parameter --key-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['backupLocation'] = {}
    _details['backupLocation']['namespace'] = backup_location_namespace
    _details['backupLocation']['bucketName'] = backup_location_bucket_name
    _details['backupLocation']['objectName'] = backup_location_object_name

    _details['backupLocation']['destination'] = 'BUCKET'

    client = cli_util.build_client('key_management', 'kms_management', ctx)
    result = client.backup_key(
        key_id=key_id,
        backup_key_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_key') and callable(getattr(client, 'get_key')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_key(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@key_group.command(name=cli_util.override('kms_management.backup_key_backup_location_uri.command_name', 'backup-key-backup-location-uri'), help=u"""Backs up an encrypted file that contains all key versions and metadata of the specified key so that you can restore the key later. The file also contains the metadata of the vault that the key belonged to.

The top level --endpoint parameter must be supplied for this operation. \n[Command Reference](backupKey)""")
@cli_util.option('--key-id', required=True, help=u"""The OCID of the key.""")
@cli_util.option('--backup-location-uri', required=True, help=u"""""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'Key'})
@cli_util.wrap_exceptions
def backup_key_backup_location_uri(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, key_id, backup_location_uri, if_match):

    if isinstance(key_id, six.string_types) and len(key_id.strip()) == 0:
        raise click.UsageError('Parameter --key-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['backupLocation'] = {}
    _details['backupLocation']['uri'] = backup_location_uri

    _details['backupLocation']['destination'] = 'PRE_AUTHENTICATED_REQUEST_URI'

    client = cli_util.build_client('key_management', 'kms_management', ctx)
    result = client.backup_key(
        key_id=key_id,
        backup_key_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_key') and callable(getattr(client, 'get_key')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_key(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@key_group.command(name=cli_util.override('kms_management.cancel_key_deletion.command_name', 'cancel-key-deletion'), help=u"""Cancels the scheduled deletion of the specified key. Canceling a scheduled deletion restores the key's lifecycle state to what it was before its scheduled deletion.

As a provisioning operation, this call is subject to a Key Management limit that applies to the total number of requests across all provisioning write operations. Key Management might throttle this call to reject an otherwise valid request when the total rate of provisioning write operations exceeds 10 requests per second for a given tenancy.

The top level --endpoint parameter must be supplied for this operation. \n[Command Reference](cancelKeyDeletion)""")
@cli_util.option('--key-id', required=True, help=u"""The OCID of the key.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'Key'})
@cli_util.wrap_exceptions
def cancel_key_deletion(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, key_id, if_match):

    if isinstance(key_id, six.string_types) and len(key_id.strip()) == 0:
        raise click.UsageError('Parameter --key-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('key_management', 'kms_management', ctx)
    result = client.cancel_key_deletion(
        key_id=key_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_key') and callable(getattr(client, 'get_key')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_key(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@key_version_group.command(name=cli_util.override('kms_management.cancel_key_version_deletion.command_name', 'cancel-key-version-deletion'), help=u"""Cancels the scheduled deletion of the specified key version. Canceling a scheduled deletion restores the key version to its lifecycle state from before its scheduled deletion.

As a provisioning operation, this call is subject to a Key Management limit that applies to the total number of requests across all provisioning write operations. Key Management might throttle this call to reject an otherwise valid request when the total rate of provisioning write operations exceeds 10 requests per second for a given tenancy.

The top level --endpoint parameter must be supplied for this operation. \n[Command Reference](cancelKeyVersionDeletion)""")
@cli_util.option('--key-id', required=True, help=u"""The OCID of the key.""")
@cli_util.option('--key-version-id', required=True, help=u"""The OCID of the key version.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'KeyVersion'})
@cli_util.wrap_exceptions
def cancel_key_version_deletion(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, key_id, key_version_id, if_match):

    if isinstance(key_id, six.string_types) and len(key_id.strip()) == 0:
        raise click.UsageError('Parameter --key-id cannot be whitespace or empty string')

    if isinstance(key_version_id, six.string_types) and len(key_version_id.strip()) == 0:
        raise click.UsageError('Parameter --key-version-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('key_management', 'kms_management', ctx)
    result = client.cancel_key_version_deletion(
        key_id=key_id,
        key_version_id=key_version_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_key_version') and callable(getattr(client, 'get_key_version')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_key_version(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@key_group.command(name=cli_util.override('kms_management.change_key_compartment.command_name', 'change-compartment'), help=u"""Moves a key into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment].

When provided, if-match is checked against the ETag values of the key.

As a provisioning operation, this call is subject to a Key Management limit that applies to the total number of requests across all provisioning write operations. Key Management might throttle this call to reject an otherwise valid request when the total rate of provisioning write operations exceeds 10 requests per second for a given tenancy.

The top level --endpoint parameter must be supplied for this operation. \n[Command Reference](changeKeyCompartment)""")
@cli_util.option('--key-id', required=True, help=u"""The OCID of the key.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment that you want to move the key to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_key_compartment(ctx, from_json, key_id, compartment_id, if_match):

    if isinstance(key_id, six.string_types) and len(key_id.strip()) == 0:
        raise click.UsageError('Parameter --key-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('key_management', 'kms_management', ctx)
    result = client.change_key_compartment(
        key_id=key_id,
        change_key_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@key_group.command(name=cli_util.override('kms_management.create_key.command_name', 'create'), help=u"""Creates a new master encryption key.

As a management operation, this call is subject to a Key Management limit that applies to the total number of requests across all management write operations. Key Management might throttle this call to reject an otherwise valid request when the total rate of management write operations exceeds 10 requests per second for a given tenancy.

The top level --endpoint parameter must be supplied for this operation. \n[Command Reference](createKey)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment where you want to create the master encryption key.""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly name for the key. It does not have to be unique, and it is changeable. Avoid entering confidential information.""")
@cli_util.option('--key-shape', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--protection-mode', type=custom_types.CliCaseInsensitiveChoice(["HSM", "SOFTWARE"]), help=u"""The key's protection mode indicates how the key persists and where cryptographic operations that use the key are performed. A protection mode of `HSM` means that the key persists on a hardware security module (HSM) and all cryptographic operations are performed inside the HSM. A protection mode of `SOFTWARE` means that the key persists on the server, protected by the vault's RSA wrapping key which persists on the HSM. All cryptographic operations that use a key with a protection mode of `SOFTWARE` are performed on the server. By default, a key's protection mode is set to `HSM`. You can't change a key's protection mode after the key is created or imported.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'key_management', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'key_management', 'class': 'dict(str, string)'}, 'key-shape': {'module': 'key_management', 'class': 'KeyShape'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'key_management', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'key_management', 'class': 'dict(str, string)'}, 'key-shape': {'module': 'key_management', 'class': 'KeyShape'}}, output_type={'module': 'key_management', 'class': 'Key'})
@cli_util.wrap_exceptions
def create_key(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, key_shape, defined_tags, freeform_tags, protection_mode):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['keyShape'] = cli_util.parse_json_parameter("key_shape", key_shape)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if protection_mode is not None:
        _details['protectionMode'] = protection_mode

    client = cli_util.build_client('key_management', 'kms_management', ctx)
    result = client.create_key(
        create_key_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_key') and callable(getattr(client, 'get_key')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_key(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@key_version_group.command(name=cli_util.override('kms_management.create_key_version.command_name', 'create'), help=u"""Generates a new [KeyVersion] resource that provides new cryptographic material for a master encryption key. The key must be in an `ENABLED` state to be rotated.

As a management operation, this call is subject to a Key Management limit that applies to the total number of requests across all  management write operations. Key Management might throttle this call to reject an otherwise valid request when the total rate of management write operations exceeds 10 requests per second for a given tenancy.

The top level --endpoint parameter must be supplied for this operation. \n[Command Reference](createKeyVersion)""")
@cli_util.option('--key-id', required=True, help=u"""The OCID of the key.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'KeyVersion'})
@cli_util.wrap_exceptions
def create_key_version(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, key_id):

    if isinstance(key_id, six.string_types) and len(key_id.strip()) == 0:
        raise click.UsageError('Parameter --key-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('key_management', 'kms_management', ctx)
    result = client.create_key_version(
        key_id=key_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_key_version') and callable(getattr(client, 'get_key_version')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_key_version(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@key_group.command(name=cli_util.override('kms_management.disable_key.command_name', 'disable'), help=u"""Disables a master encryption key so it can no longer be used for encryption, decryption, or generating new data encryption keys.

As a management operation, this call is subject to a Key Management limit that applies to the total number of requests across all management write operations. Key Management might throttle this call to reject an otherwise valid request when the total rate of management write operations exceeds 10 requests per second for a given tenancy.

The top level --endpoint parameter must be supplied for this operation. \n[Command Reference](disableKey)""")
@cli_util.option('--key-id', required=True, help=u"""The OCID of the key.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'Key'})
@cli_util.wrap_exceptions
def disable_key(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, key_id, if_match):

    if isinstance(key_id, six.string_types) and len(key_id.strip()) == 0:
        raise click.UsageError('Parameter --key-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('key_management', 'kms_management', ctx)
    result = client.disable_key(
        key_id=key_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_key') and callable(getattr(client, 'get_key')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_key(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@key_group.command(name=cli_util.override('kms_management.enable_key.command_name', 'enable'), help=u"""Enables a master encryption key so it can be used for encryption, decryption, or generating new data encryption keys.

As a management operation, this call is subject to a Key Management limit that applies to the total number of requests across all management write operations. Key Management might throttle this call to reject an otherwise valid request when the total rate of management write operations exceeds 10 requests per second for a given tenancy.

The top level --endpoint parameter must be supplied for this operation. \n[Command Reference](enableKey)""")
@cli_util.option('--key-id', required=True, help=u"""The OCID of the key.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'Key'})
@cli_util.wrap_exceptions
def enable_key(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, key_id, if_match):

    if isinstance(key_id, six.string_types) and len(key_id.strip()) == 0:
        raise click.UsageError('Parameter --key-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('key_management', 'kms_management', ctx)
    result = client.enable_key(
        key_id=key_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_key') and callable(getattr(client, 'get_key')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_key(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@key_group.command(name=cli_util.override('kms_management.get_key.command_name', 'get'), help=u"""Gets information about the specified master encryption key.

As a management operation, this call is subject to a Key Management limit that applies to the total number of requests across all management read operations. Key Management might throttle this call to reject an otherwise valid request when the total rate of management read operations exceeds 10 requests per second for a given tenancy.

The top level --endpoint parameter must be supplied for this operation. \n[Command Reference](getKey)""")
@cli_util.option('--key-id', required=True, help=u"""The OCID of the key.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'Key'})
@cli_util.wrap_exceptions
def get_key(ctx, from_json, key_id):

    if isinstance(key_id, six.string_types) and len(key_id.strip()) == 0:
        raise click.UsageError('Parameter --key-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('key_management', 'kms_management', ctx)
    result = client.get_key(
        key_id=key_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@key_version_group.command(name=cli_util.override('kms_management.get_key_version.command_name', 'get'), help=u"""Gets information about the specified key version.

As a management operation, this call is subject to a Key Management limit that applies to the total number of requests across all management read operations. Key Management might throttle this call to reject an otherwise valid request when the total rate of management read operations exceeds 10 requests per second for a given tenancy.

The top level --endpoint parameter must be supplied for this operation. \n[Command Reference](getKeyVersion)""")
@cli_util.option('--key-id', required=True, help=u"""The OCID of the key.""")
@cli_util.option('--key-version-id', required=True, help=u"""The OCID of the key version.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'KeyVersion'})
@cli_util.wrap_exceptions
def get_key_version(ctx, from_json, key_id, key_version_id):

    if isinstance(key_id, six.string_types) and len(key_id.strip()) == 0:
        raise click.UsageError('Parameter --key-id cannot be whitespace or empty string')

    if isinstance(key_version_id, six.string_types) and len(key_version_id.strip()) == 0:
        raise click.UsageError('Parameter --key-version-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('key_management', 'kms_management', ctx)
    result = client.get_key_version(
        key_id=key_id,
        key_version_id=key_version_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@replication_status_details_group.command(name=cli_util.override('kms_management.get_replication_status.command_name', 'get-replication-status'), help=u"""When a vault has a replica, each operation on the vault or its resources, such as keys, is replicated and has an associated replicationId. Replication status provides details about whether the operation associated with the given replicationId has been successfully applied across replicas.

The top level --endpoint parameter must be supplied for this operation. \n[Command Reference](getReplicationStatus)""")
@cli_util.option('--replication-id', required=True, help=u"""replicationId associated with an operation on a resource""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'ReplicationStatusDetails'})
@cli_util.wrap_exceptions
def get_replication_status(ctx, from_json, replication_id):

    if isinstance(replication_id, six.string_types) and len(replication_id.strip()) == 0:
        raise click.UsageError('Parameter --replication-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('key_management', 'kms_management', ctx)
    result = client.get_replication_status(
        replication_id=replication_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@wrapping_key_group.command(name=cli_util.override('kms_management.get_wrapping_key.command_name', 'get'), help=u"""Gets details about the public RSA wrapping key associated with the vault in the endpoint. Each vault has an RSA key-pair that wraps and unwraps AES key material for import into Key Management.

The top level --endpoint parameter must be supplied for this operation. \n[Command Reference](getWrappingKey)""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'WrappingKey'})
@cli_util.wrap_exceptions
def get_wrapping_key(ctx, from_json, ):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('key_management', 'kms_management', ctx)
    result = client.get_wrapping_key(
        **kwargs
    )
    cli_util.render_response(result, ctx)


@key_group.command(name=cli_util.override('kms_management.import_key.command_name', 'import'), help=u"""Imports AES key material to create a new key with. The key material must be base64-encoded and wrapped by the vault's public RSA wrapping key before you can import it. Key Management supports AES symmetric keys that are exactly 16, 24, or 32 bytes. Furthermore, the key length must match what you specify at the time of import.

The top level --endpoint parameter must be supplied for this operation. \n[Command Reference](importKey)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment that contains this key.""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly name for the key. It does not have to be unique, and it is changeable. Avoid entering confidential information.""")
@cli_util.option('--key-shape', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wrapped-import-key', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"foo-value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--protection-mode', type=custom_types.CliCaseInsensitiveChoice(["HSM", "SOFTWARE"]), help=u"""The key's protection mode indicates how the key persists and where cryptographic operations that use the key are performed. A protection mode of `HSM` means that the key persists on a hardware security module (HSM) and all cryptographic operations are performed inside the HSM. A protection mode of `SOFTWARE` means that the key persists on the server, protected by the vault's RSA wrapping key which persists on the HSM. All cryptographic operations that use a key with a protection mode of `SOFTWARE` are performed on the server. By default, a key's protection mode is set to `HSM`. You can't change a key's protection mode after the key is created or imported.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'key_management', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'key_management', 'class': 'dict(str, string)'}, 'key-shape': {'module': 'key_management', 'class': 'KeyShape'}, 'wrapped-import-key': {'module': 'key_management', 'class': 'WrappedImportKey'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'key_management', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'key_management', 'class': 'dict(str, string)'}, 'key-shape': {'module': 'key_management', 'class': 'KeyShape'}, 'wrapped-import-key': {'module': 'key_management', 'class': 'WrappedImportKey'}}, output_type={'module': 'key_management', 'class': 'Key'})
@cli_util.wrap_exceptions
def import_key(ctx, from_json, compartment_id, display_name, key_shape, wrapped_import_key, defined_tags, freeform_tags, protection_mode):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['keyShape'] = cli_util.parse_json_parameter("key_shape", key_shape)
    _details['wrappedImportKey'] = cli_util.parse_json_parameter("wrapped_import_key", wrapped_import_key)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if protection_mode is not None:
        _details['protectionMode'] = protection_mode

    client = cli_util.build_client('key_management', 'kms_management', ctx)
    result = client.import_key(
        import_key_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@key_version_group.command(name=cli_util.override('kms_management.import_key_version.command_name', 'import'), help=u"""Imports AES key material to create a new key version with, and then rotates the key to begin using the new key version. The key material must be base64-encoded and wrapped by the vault's public RSA wrapping key before you can import it. Key Management supports AES symmetric keys that are exactly 16, 24, or 32 bytes. Furthermore, the key length must match the length of the specified key and what you specify as the length at the time of import.

The top level --endpoint parameter must be supplied for this operation. \n[Command Reference](importKeyVersion)""")
@cli_util.option('--key-id', required=True, help=u"""The OCID of the key.""")
@cli_util.option('--wrapped-import-key', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'key_management', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'key_management', 'class': 'dict(str, string)'}, 'wrapped-import-key': {'module': 'key_management', 'class': 'WrappedImportKey'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'key_management', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'key_management', 'class': 'dict(str, string)'}, 'wrapped-import-key': {'module': 'key_management', 'class': 'WrappedImportKey'}}, output_type={'module': 'key_management', 'class': 'KeyVersion'})
@cli_util.wrap_exceptions
def import_key_version(ctx, from_json, key_id, wrapped_import_key, defined_tags, freeform_tags):

    if isinstance(key_id, six.string_types) and len(key_id.strip()) == 0:
        raise click.UsageError('Parameter --key-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['wrappedImportKey'] = cli_util.parse_json_parameter("wrapped_import_key", wrapped_import_key)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('key_management', 'kms_management', ctx)
    result = client.import_key_version(
        key_id=key_id,
        import_key_version_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@key_version_group.command(name=cli_util.override('kms_management.list_key_versions.command_name', 'list'), help=u"""Lists all [KeyVersion] resources for the specified master encryption key.

As a management operation, this call is subject to a Key Management limit that applies to the total number of requests across all management read operations. Key Management might throttle this call to reject an otherwise valid request when the total rate of management read operations exceeds 10 requests per second for a given tenancy.

The top level --endpoint parameter must be supplied for this operation. \n[Command Reference](listKeyVersions)""")
@cli_util.option('--key-id', required=True, help=u"""The OCID of the key.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can specify only one sort order. The default order for `TIMECREATED` is descending. The default order for `DISPLAYNAME` is ascending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'list[KeyVersionSummary]'})
@cli_util.wrap_exceptions
def list_key_versions(ctx, from_json, all_pages, page_size, key_id, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(key_id, six.string_types) and len(key_id.strip()) == 0:
        raise click.UsageError('Parameter --key-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('key_management', 'kms_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_key_versions,
            key_id=key_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_key_versions,
            limit,
            page_size,
            key_id=key_id,
            **kwargs
        )
    else:
        result = client.list_key_versions(
            key_id=key_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@key_group.command(name=cli_util.override('kms_management.list_keys.command_name', 'list'), help=u"""Lists the master encryption keys in the specified vault and compartment.

As a management operation, this call is subject to a Key Management limit that applies to the total number of requests across all management read operations. Key Management might throttle this call to reject an otherwise valid request when the total rate of management read operations exceeds 10 requests per second for a given tenancy.

The top level --endpoint parameter must be supplied for this operation. \n[Command Reference](listKeys)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can specify only one sort order. The default order for `TIMECREATED` is descending. The default order for `DISPLAYNAME` is ascending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--protection-mode', type=custom_types.CliCaseInsensitiveChoice(["HSM", "SOFTWARE"]), help=u"""A key's protection mode indicates how the key persists and where cryptographic operations that use the key are performed. A protection mode of `HSM` means that the key persists on a hardware security module (HSM) and all cryptographic operations are performed inside the HSM. A protection mode of `SOFTWARE` means that the key persists on the server, protected by the vault's RSA wrapping key which persists on the HSM. All cryptographic operations that use a key with a protection mode of `SOFTWARE` are performed on the server.""")
@cli_util.option('--algorithm', type=custom_types.CliCaseInsensitiveChoice(["AES", "RSA", "ECDSA"]), help=u"""The algorithm used by a key's key versions to encrypt or decrypt data. Currently, support includes AES, RSA, and ECDSA algorithms.""")
@cli_util.option('--length', type=click.INT, help=u"""The length of the key in bytes, expressed as an integer. Supported values include 16, 24, or 32.""")
@cli_util.option('--curve-id', type=custom_types.CliCaseInsensitiveChoice(["NIST_P256", "NIST_P384", "NIST_P521"]), help=u"""The curve ID of the keys. (This pertains only to ECDSA keys.)""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'list[KeySummary]'})
@cli_util.wrap_exceptions
def list_keys(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_by, sort_order, protection_mode, algorithm, length, curve_id):

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
    if protection_mode is not None:
        kwargs['protection_mode'] = protection_mode
    if algorithm is not None:
        kwargs['algorithm'] = algorithm
    if length is not None:
        kwargs['length'] = length
    if curve_id is not None:
        kwargs['curve_id'] = curve_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('key_management', 'kms_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_keys,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_keys,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_keys(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@key_group.command(name=cli_util.override('kms_management.restore_key_from_file.command_name', 'restore-key-from-file'), help=u"""Restores the specified key to the specified vault, based on information in the backup file provided. If the vault doesn't exist, the operation returns a response with a 404 HTTP status error code. You need to first restore the vault associated with the key.

The top level --endpoint parameter must be supplied for this operation. \n[Command Reference](restoreKeyFromFile)""")
@cli_util.option('--restore-key-from-file-details', required=True, help=u"""The encrypted backup file to upload to restore the key.""")
@cli_util.option('--content-length', type=click.INT, help=u"""The content length of the body.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--content-md5', help=u"""The base64-encoded MD5 hash value of the body, as described in [RFC 2616], section 14.15. If the Content-MD5 header is present, Key Management performs an integrity check on the body of the HTTP request by computing the MD5 hash for the body and comparing it to the MD5 hash supplied in the header. If the two hashes don't match, the object is rejected and a response with 400 Unmatched Content MD5 error is returned, along with the message: \"The computed MD5 of the request body (ACTUAL_MD5) does not match the Content-MD5 header (HEADER_MD5).\"""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'Key'})
@cli_util.wrap_exceptions
def restore_key_from_file(ctx, from_json, restore_key_from_file_details, content_length, if_match, content_md5):

    kwargs = {}
    if content_length is not None:
        kwargs['content_length'] = content_length
    if if_match is not None:
        kwargs['if_match'] = if_match
    if content_md5 is not None:
        kwargs['content_md5'] = content_md5
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    # do not automatically retry operations with binary inputs
    kwargs['retry_strategy'] = oci.retry.NoneRetryStrategy()

    client = cli_util.build_client('key_management', 'kms_management', ctx)
    result = client.restore_key_from_file(
        restore_key_from_file_details=restore_key_from_file_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@key_group.command(name=cli_util.override('kms_management.restore_key_from_object_store.command_name', 'restore-key-from-object-store'), help=u"""Restores the specified key to the specified vault from an Oracle Cloud Infrastructure Object Storage location. If the vault doesn't exist, the operation returns a response with a 404 HTTP status error code. You need to first restore the vault associated with the key.

The top level --endpoint parameter must be supplied for this operation. \n[Command Reference](restoreKeyFromObjectStore)""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--backup-location', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'backup-location': {'module': 'key_management', 'class': 'BackupLocation'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backup-location': {'module': 'key_management', 'class': 'BackupLocation'}}, output_type={'module': 'key_management', 'class': 'Key'})
@cli_util.wrap_exceptions
def restore_key_from_object_store(ctx, from_json, if_match, backup_location):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if backup_location is not None:
        _details['backupLocation'] = cli_util.parse_json_parameter("backup_location", backup_location)

    client = cli_util.build_client('key_management', 'kms_management', ctx)
    result = client.restore_key_from_object_store(
        restore_key_from_object_store_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@key_group.command(name=cli_util.override('kms_management.restore_key_from_object_store_backup_location_bucket.command_name', 'restore-key-from-object-store-backup-location-bucket'), help=u"""Restores the specified key to the specified vault from an Oracle Cloud Infrastructure Object Storage location. If the vault doesn't exist, the operation returns a response with a 404 HTTP status error code. You need to first restore the vault associated with the key.

The top level --endpoint parameter must be supplied for this operation. \n[Command Reference](restoreKeyFromObjectStore)""")
@cli_util.option('--backup-location-namespace', required=True, help=u"""""")
@cli_util.option('--backup-location-bucket-name', required=True, help=u"""""")
@cli_util.option('--backup-location-object-name', required=True, help=u"""""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'Key'})
@cli_util.wrap_exceptions
def restore_key_from_object_store_backup_location_bucket(ctx, from_json, backup_location_namespace, backup_location_bucket_name, backup_location_object_name, if_match):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['backupLocation'] = {}
    _details['backupLocation']['namespace'] = backup_location_namespace
    _details['backupLocation']['bucketName'] = backup_location_bucket_name
    _details['backupLocation']['objectName'] = backup_location_object_name

    _details['backupLocation']['destination'] = 'BUCKET'

    client = cli_util.build_client('key_management', 'kms_management', ctx)
    result = client.restore_key_from_object_store(
        restore_key_from_object_store_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@key_group.command(name=cli_util.override('kms_management.restore_key_from_object_store_backup_location_uri.command_name', 'restore-key-from-object-store-backup-location-uri'), help=u"""Restores the specified key to the specified vault from an Oracle Cloud Infrastructure Object Storage location. If the vault doesn't exist, the operation returns a response with a 404 HTTP status error code. You need to first restore the vault associated with the key.

The top level --endpoint parameter must be supplied for this operation. \n[Command Reference](restoreKeyFromObjectStore)""")
@cli_util.option('--backup-location-uri', required=True, help=u"""""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'Key'})
@cli_util.wrap_exceptions
def restore_key_from_object_store_backup_location_uri(ctx, from_json, backup_location_uri, if_match):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['backupLocation'] = {}
    _details['backupLocation']['uri'] = backup_location_uri

    _details['backupLocation']['destination'] = 'PRE_AUTHENTICATED_REQUEST_URI'

    client = cli_util.build_client('key_management', 'kms_management', ctx)
    result = client.restore_key_from_object_store(
        restore_key_from_object_store_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@key_group.command(name=cli_util.override('kms_management.schedule_key_deletion.command_name', 'schedule-key-deletion'), help=u"""Schedules the deletion of the specified key. This sets the lifecycle state of the key to `PENDING_DELETION` and then deletes it after the specified retention period ends.

As a provisioning operation, this call is subject to a Key Management limit that applies to the total number of requests across all provisioning write operations. Key Management might throttle this call to reject an otherwise valid request when the total rate of provisioning write operations exceeds 10 requests per second for a given tenancy.

The top level --endpoint parameter must be supplied for this operation. \n[Command Reference](scheduleKeyDeletion)""")
@cli_util.option('--key-id', required=True, help=u"""The OCID of the key.""")
@cli_util.option('--time-of-deletion', type=custom_types.CLI_DATETIME, help=u"""An optional property to indicate when to delete the vault, expressed in [RFC 3339] timestamp format. The specified time must be between 7 and 30 days from when the request is received. If this property is missing, it will be set to 30 days from the time of the request by default.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'Key'})
@cli_util.wrap_exceptions
def schedule_key_deletion(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, key_id, time_of_deletion, if_match):

    if isinstance(key_id, six.string_types) and len(key_id.strip()) == 0:
        raise click.UsageError('Parameter --key-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if time_of_deletion is not None:
        _details['timeOfDeletion'] = time_of_deletion

    client = cli_util.build_client('key_management', 'kms_management', ctx)
    result = client.schedule_key_deletion(
        key_id=key_id,
        schedule_key_deletion_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_key') and callable(getattr(client, 'get_key')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_key(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@key_version_group.command(name=cli_util.override('kms_management.schedule_key_version_deletion.command_name', 'schedule-key-version-deletion'), help=u"""Schedules the deletion of the specified key version. This sets the lifecycle state of the key version to `PENDING_DELETION` and then deletes it after the specified retention period ends.

As a provisioning operation, this call is subject to a Key Management limit that applies to the total number of requests across all provisioning write operations. Key Management might throttle this call to reject an otherwise valid request when the total rate of provisioning write operations exceeds 10 requests per second for a given tenancy.

The top level --endpoint parameter must be supplied for this operation. \n[Command Reference](scheduleKeyVersionDeletion)""")
@cli_util.option('--key-id', required=True, help=u"""The OCID of the key.""")
@cli_util.option('--key-version-id', required=True, help=u"""The OCID of the key version.""")
@cli_util.option('--time-of-deletion', type=custom_types.CLI_DATETIME, help=u"""An optional property to indicate when to delete the key version, expressed in [RFC 3339] timestamp format. The specified time must be between 7 and 30 days from the time when the request is received. If this property is missing, it will be set to 30 days from the time of the request by default.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'KeyVersion'})
@cli_util.wrap_exceptions
def schedule_key_version_deletion(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, key_id, key_version_id, time_of_deletion, if_match):

    if isinstance(key_id, six.string_types) and len(key_id.strip()) == 0:
        raise click.UsageError('Parameter --key-id cannot be whitespace or empty string')

    if isinstance(key_version_id, six.string_types) and len(key_version_id.strip()) == 0:
        raise click.UsageError('Parameter --key-version-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if time_of_deletion is not None:
        _details['timeOfDeletion'] = time_of_deletion

    client = cli_util.build_client('key_management', 'kms_management', ctx)
    result = client.schedule_key_version_deletion(
        key_id=key_id,
        key_version_id=key_version_id,
        schedule_key_version_deletion_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_key_version') and callable(getattr(client, 'get_key_version')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_key_version(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@key_group.command(name=cli_util.override('kms_management.update_key.command_name', 'update'), help=u"""Updates the properties of a master encryption key. Specifically, you can update the `displayName`, `freeformTags`, and `definedTags` properties. Furthermore, the key must be in an `ENABLED` or `CREATING` state to be updated.

As a management operation, this call is subject to a Key Management limit that applies to the total number of requests across all management write operations. Key Management might throttle this call to reject an otherwise valid request when the total rate of management write operations exceeds 10 requests per second for a given tenancy.

The top level --endpoint parameter must be supplied for this operation. \n[Command Reference](updateKey)""")
@cli_util.option('--key-id', required=True, help=u"""The OCID of the key.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name for the key. It does not have to be unique, and it is changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'key_management', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'key_management', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'key_management', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'key_management', 'class': 'dict(str, string)'}}, output_type={'module': 'key_management', 'class': 'Key'})
@cli_util.wrap_exceptions
def update_key(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, key_id, defined_tags, display_name, freeform_tags, if_match):

    if isinstance(key_id, six.string_types) and len(key_id.strip()) == 0:
        raise click.UsageError('Parameter --key-id cannot be whitespace or empty string')
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

    client = cli_util.build_client('key_management', 'kms_management', ctx)
    result = client.update_key(
        key_id=key_id,
        update_key_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_key') and callable(getattr(client, 'get_key')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_key(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
