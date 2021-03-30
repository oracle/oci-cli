# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
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


@click.command(cli_util.override('kms_vault.kms_vault_root_group.command_name', 'kms-vault'), cls=CommandGroupWithAlias, help=cli_util.override('kms_vault.kms_vault_root_group.help', """API for managing and performing operations with keys and vaults. (For the API for managing secrets, see the Vault Service
Secret Management API. For the API for retrieving secrets, see the Vault Service Secret Retrieval API.)"""), short_help=cli_util.override('kms_vault.kms_vault_root_group.short_help', """Vault Service Key Management API"""))
@cli_util.help_option_group
def kms_vault_root_group():
    pass


@click.command(cli_util.override('kms_vault.vault_usage_group.command_name', 'vault-usage'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def vault_usage_group():
    pass


@click.command(cli_util.override('kms_vault.vault_group.command_name', 'vault'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def vault_group():
    pass


kms_service_cli.kms_service_group.add_command(kms_vault_root_group)
kms_vault_root_group.add_command(vault_usage_group)
kms_vault_root_group.add_command(vault_group)


@vault_group.command(name=cli_util.override('kms_vault.backup_vault.command_name', 'backup'), help=u"""Backs up an encrypted file that contains all the metadata of a vault so that you can restore the vault later. You can backup a vault whether or not it contains keys. This operation only backs up the metadata of the vault, and does not include key metadata. \n[Command Reference](backupVault)""")
@cli_util.option('--vault-id', required=True, help=u"""The OCID of the vault.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--backup-location', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-include-keys', type=click.BOOL, help=u"""""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'backup-location': {'module': 'key_management', 'class': 'BackupLocation'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backup-location': {'module': 'key_management', 'class': 'BackupLocation'}}, output_type={'module': 'key_management', 'class': 'Vault'})
@cli_util.wrap_exceptions
def backup_vault(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, vault_id, if_match, backup_location, is_include_keys):

    if isinstance(vault_id, six.string_types) and len(vault_id.strip()) == 0:
        raise click.UsageError('Parameter --vault-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if backup_location is not None:
        _details['backupLocation'] = cli_util.parse_json_parameter("backup_location", backup_location)

    if is_include_keys is not None:
        _details['isIncludeKeys'] = is_include_keys

    client = cli_util.build_client('key_management', 'kms_vault', ctx)
    result = client.backup_vault(
        vault_id=vault_id,
        backup_vault_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_vault') and callable(getattr(client, 'get_vault')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_vault(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@vault_group.command(name=cli_util.override('kms_vault.backup_vault_backup_location_bucket.command_name', 'backup-vault-backup-location-bucket'), help=u"""Backs up an encrypted file that contains all the metadata of a vault so that you can restore the vault later. You can backup a vault whether or not it contains keys. This operation only backs up the metadata of the vault, and does not include key metadata. \n[Command Reference](backupVault)""")
@cli_util.option('--vault-id', required=True, help=u"""The OCID of the vault.""")
@cli_util.option('--backup-location-namespace', required=True, help=u"""""")
@cli_util.option('--backup-location-bucket-name', required=True, help=u"""""")
@cli_util.option('--backup-location-object-name', required=True, help=u"""""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--is-include-keys', type=click.BOOL, help=u"""""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'Vault'})
@cli_util.wrap_exceptions
def backup_vault_backup_location_bucket(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, vault_id, backup_location_namespace, backup_location_bucket_name, backup_location_object_name, if_match, is_include_keys):

    if isinstance(vault_id, six.string_types) and len(vault_id.strip()) == 0:
        raise click.UsageError('Parameter --vault-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['backupLocation'] = {}
    _details['backupLocation']['namespace'] = backup_location_namespace
    _details['backupLocation']['bucketName'] = backup_location_bucket_name
    _details['backupLocation']['objectName'] = backup_location_object_name

    if is_include_keys is not None:
        _details['isIncludeKeys'] = is_include_keys

    _details['backupLocation']['destination'] = 'BUCKET'

    client = cli_util.build_client('key_management', 'kms_vault', ctx)
    result = client.backup_vault(
        vault_id=vault_id,
        backup_vault_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_vault') and callable(getattr(client, 'get_vault')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_vault(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@vault_group.command(name=cli_util.override('kms_vault.backup_vault_backup_location_uri.command_name', 'backup-vault-backup-location-uri'), help=u"""Backs up an encrypted file that contains all the metadata of a vault so that you can restore the vault later. You can backup a vault whether or not it contains keys. This operation only backs up the metadata of the vault, and does not include key metadata. \n[Command Reference](backupVault)""")
@cli_util.option('--vault-id', required=True, help=u"""The OCID of the vault.""")
@cli_util.option('--backup-location-uri', required=True, help=u"""""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--is-include-keys', type=click.BOOL, help=u"""""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'Vault'})
@cli_util.wrap_exceptions
def backup_vault_backup_location_uri(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, vault_id, backup_location_uri, if_match, is_include_keys):

    if isinstance(vault_id, six.string_types) and len(vault_id.strip()) == 0:
        raise click.UsageError('Parameter --vault-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['backupLocation'] = {}
    _details['backupLocation']['uri'] = backup_location_uri

    if is_include_keys is not None:
        _details['isIncludeKeys'] = is_include_keys

    _details['backupLocation']['destination'] = 'PRE_AUTHENTICATED_REQUEST_URI'

    client = cli_util.build_client('key_management', 'kms_vault', ctx)
    result = client.backup_vault(
        vault_id=vault_id,
        backup_vault_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_vault') and callable(getattr(client, 'get_vault')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_vault(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@vault_group.command(name=cli_util.override('kms_vault.cancel_vault_deletion.command_name', 'cancel-vault-deletion'), help=u"""Cancels the scheduled deletion of the specified vault. Canceling a scheduled deletion restores the vault and all keys in it to their respective states from before their scheduled deletion. All keys that were scheduled for deletion prior to vault deletion retain their lifecycle state and time of deletion.

As a provisioning operation, this call is subject to a Key Management limit that applies to the total number of requests across all provisioning write operations. Key Management might throttle this call to reject an otherwise valid request when the total rate of provisioning write operations exceeds 10 requests per second for a given tenancy. \n[Command Reference](cancelVaultDeletion)""")
@cli_util.option('--vault-id', required=True, help=u"""The OCID of the vault.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'Vault'})
@cli_util.wrap_exceptions
def cancel_vault_deletion(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, vault_id, if_match):

    if isinstance(vault_id, six.string_types) and len(vault_id.strip()) == 0:
        raise click.UsageError('Parameter --vault-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('key_management', 'kms_vault', ctx)
    result = client.cancel_vault_deletion(
        vault_id=vault_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_vault') and callable(getattr(client, 'get_vault')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_vault(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@vault_group.command(name=cli_util.override('kms_vault.change_vault_compartment.command_name', 'change-compartment'), help=u"""Moves a vault into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment].

When provided, if-match is checked against the ETag values of the resource.

As a provisioning operation, this call is subject to a Key Management limit that applies to the total number of requests across all provisioning write operations. Key Management might throttle this call to reject an otherwise valid request when the total rate of provisioning write operations exceeds 10 requests per second for a given tenancy. \n[Command Reference](changeVaultCompartment)""")
@cli_util.option('--vault-id', required=True, help=u"""The OCID of the vault.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the vault to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_vault_compartment(ctx, from_json, vault_id, compartment_id, if_match):

    if isinstance(vault_id, six.string_types) and len(vault_id.strip()) == 0:
        raise click.UsageError('Parameter --vault-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('key_management', 'kms_vault', ctx)
    result = client.change_vault_compartment(
        vault_id=vault_id,
        change_vault_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vault_group.command(name=cli_util.override('kms_vault.create_vault.command_name', 'create'), help=u"""Creates a new vault. The type of vault you create determines key placement, pricing, and available options. Options include storage isolation, a dedicated service endpoint instead of a shared service endpoint for API calls, and either a dedicated hardware security module (HSM) or a multitenant HSM.

As a provisioning operation, this call is subject to a Key Management limit that applies to the total number of requests across all provisioning write operations. Key Management might throttle this call to reject an otherwise valid request when the total rate of provisioning write operations exceeds 10 requests per second for a given tenancy. \n[Command Reference](createVault)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment where you want to create this vault.""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly name for the vault. It does not have to be unique, and it is changeable. Avoid entering confidential information.""")
@cli_util.option('--vault-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["VIRTUAL_PRIVATE", "DEFAULT"]), help=u"""The type of vault to create. Each type of vault stores the key with different degrees of isolation and has different options and pricing.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'key_management', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'key_management', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'key_management', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'key_management', 'class': 'dict(str, string)'}}, output_type={'module': 'key_management', 'class': 'Vault'})
@cli_util.wrap_exceptions
def create_vault(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, vault_type, defined_tags, freeform_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['vaultType'] = vault_type

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('key_management', 'kms_vault', ctx)
    result = client.create_vault(
        create_vault_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_vault') and callable(getattr(client, 'get_vault')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_vault(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@vault_group.command(name=cli_util.override('kms_vault.create_vault_replica.command_name', 'create-vault-replica'), help=u"""Creates a replica for the vault in another region in the same realm

The API is a no-op if called for same region that a vault is already replicated to. 409 if called on a vault that is already replicated to a different region. Users need to delete existing replica first before calling it with a different region.

As a provisioning operation, this call is subject to a Key Management limit that applies to the total number of requests across all provisioning write operations. Key Management might throttle this call to reject an otherwise valid request when the total rate of provisioning write operations exceeds 10 requests per second for a given tenancy. \n[Command Reference](createVaultReplica)""")
@cli_util.option('--vault-id', required=True, help=u"""The OCID of the vault.""")
@cli_util.option('--replica-region', required=True, help=u"""The region in the realm to which the vault need to be replicated to""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def create_vault_replica(ctx, from_json, vault_id, replica_region, if_match):

    if isinstance(vault_id, six.string_types) and len(vault_id.strip()) == 0:
        raise click.UsageError('Parameter --vault-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['replicaRegion'] = replica_region

    client = cli_util.build_client('key_management', 'kms_vault', ctx)
    result = client.create_vault_replica(
        vault_id=vault_id,
        create_vault_replica_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vault_group.command(name=cli_util.override('kms_vault.delete_vault_replica.command_name', 'delete-vault-replica'), help=u"""Deletes a vault replica

As a provisioning operation, this call is subject to a Key Management limit that applies to the total number of requests across all provisioning write operations. Key Management might throttle this call to reject an otherwise valid request when the total rate of provisioning write operations exceeds 10 requests per second for a given tenancy. \n[Command Reference](deleteVaultReplica)""")
@cli_util.option('--vault-id', required=True, help=u"""The OCID of the vault.""")
@cli_util.option('--replica-region', required=True, help=u"""The region in the realm on which the replica should be deleted""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_vault_replica(ctx, from_json, vault_id, replica_region, if_match):

    if isinstance(vault_id, six.string_types) and len(vault_id.strip()) == 0:
        raise click.UsageError('Parameter --vault-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['replicaRegion'] = replica_region

    client = cli_util.build_client('key_management', 'kms_vault', ctx)
    result = client.delete_vault_replica(
        vault_id=vault_id,
        delete_vault_replica_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vault_group.command(name=cli_util.override('kms_vault.get_vault.command_name', 'get'), help=u"""Gets the specified vault's configuration information.

As a provisioning operation, this call is subject to a Key Management limit that applies to the total number of requests across all provisioning read operations. Key Management might throttle this call to reject an otherwise valid request when the total rate of provisioning read operations exceeds 10 requests per second for a given tenancy. \n[Command Reference](getVault)""")
@cli_util.option('--vault-id', required=True, help=u"""The OCID of the vault.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'Vault'})
@cli_util.wrap_exceptions
def get_vault(ctx, from_json, vault_id):

    if isinstance(vault_id, six.string_types) and len(vault_id.strip()) == 0:
        raise click.UsageError('Parameter --vault-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('key_management', 'kms_vault', ctx)
    result = client.get_vault(
        vault_id=vault_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vault_usage_group.command(name=cli_util.override('kms_vault.get_vault_usage.command_name', 'get'), help=u"""Gets the count of keys and key versions in the specified vault to calculate usage against service limits. \n[Command Reference](getVaultUsage)""")
@cli_util.option('--vault-id', required=True, help=u"""The OCID of the vault.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'VaultUsage'})
@cli_util.wrap_exceptions
def get_vault_usage(ctx, from_json, vault_id):

    if isinstance(vault_id, six.string_types) and len(vault_id.strip()) == 0:
        raise click.UsageError('Parameter --vault-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('key_management', 'kms_vault', ctx)
    result = client.get_vault_usage(
        vault_id=vault_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vault_group.command(name=cli_util.override('kms_vault.list_vault_replicas.command_name', 'list-vault-replicas'), help=u"""Lists the replicas for a vault

As a provisioning operation, this call is subject to a Key Management limit that applies to the total number of requests across all provisioning write operations. Key Management might throttle this call to reject an otherwise valid request when the total rate of provisioning write operations exceeds 10 requests per second for a given tenancy. \n[Command Reference](listVaultReplicas)""")
@cli_util.option('--vault-id', required=True, help=u"""The OCID of the vault.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can specify only one sort order. The default order for `TIMECREATED` is descending. The default order for `DISPLAYNAME` is ascending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'list[VaultReplicaSummary]'})
@cli_util.wrap_exceptions
def list_vault_replicas(ctx, from_json, all_pages, page_size, vault_id, if_match, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(vault_id, six.string_types) and len(vault_id.strip()) == 0:
        raise click.UsageError('Parameter --vault-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('key_management', 'kms_vault', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_vault_replicas,
            vault_id=vault_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_vault_replicas,
            limit,
            page_size,
            vault_id=vault_id,
            **kwargs
        )
    else:
        result = client.list_vault_replicas(
            vault_id=vault_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@vault_group.command(name=cli_util.override('kms_vault.list_vaults.command_name', 'list'), help=u"""Lists the vaults in the specified compartment.

As a provisioning operation, this call is subject to a Key Management limit that applies to the total number of requests across all provisioning read operations. Key Management might throttle this call to reject an otherwise valid request when the total rate of provisioning read operations exceeds 10 requests per second for a given tenancy. \n[Command Reference](listVaults)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can specify only one sort order. The default order for `TIMECREATED` is descending. The default order for `DISPLAYNAME` is ascending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'list[VaultSummary]'})
@cli_util.wrap_exceptions
def list_vaults(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_by, sort_order):

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
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('key_management', 'kms_vault', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_vaults,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_vaults,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_vaults(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@vault_group.command(name=cli_util.override('kms_vault.restore_vault_from_file.command_name', 'restore-vault-from-file'), help=u"""Restores a vault from an encrypted backup file. If a vault with the same OCID already exists, this operation returns a response with a 409 HTTP status error code. \n[Command Reference](restoreVaultFromFile)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--restore-vault-from-file-details', required=True, help=u"""The encrypted backup file to upload to restore the vault.""")
@cli_util.option('--content-length', type=click.INT, help=u"""The content length of the body.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--content-md5', help=u"""The base64-encoded MD5 hash value of the body, as described in [RFC 2616], section 14.15. If the Content-MD5 header is present, Key Management performs an integrity check on the body of the HTTP request by computing the MD5 hash for the body and comparing it to the MD5 hash supplied in the header. If the two hashes don't match, the object is rejected and a response with 400 Unmatched Content MD5 error is returned, along with the message: \"The computed MD5 of the request body (ACTUAL_MD5) does not match the Content-MD5 header (HEADER_MD5).\"""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'Vault'})
@cli_util.wrap_exceptions
def restore_vault_from_file(ctx, from_json, compartment_id, restore_vault_from_file_details, content_length, if_match, content_md5):

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

    client = cli_util.build_client('key_management', 'kms_vault', ctx)
    result = client.restore_vault_from_file(
        compartment_id=compartment_id,
        restore_vault_from_file_details=restore_vault_from_file_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vault_group.command(name=cli_util.override('kms_vault.restore_vault_from_object_store.command_name', 'restore-vault-from-object-store'), help=u"""Restores a vault from an encrypted backup file stored in Oracle Cloud Infrastructure Object Storage. If a vault with the same OCID already exists, this operation returns a response with a 409 HTTP status error code. \n[Command Reference](restoreVaultFromObjectStore)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--backup-location', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'backup-location': {'module': 'key_management', 'class': 'BackupLocation'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backup-location': {'module': 'key_management', 'class': 'BackupLocation'}}, output_type={'module': 'key_management', 'class': 'Vault'})
@cli_util.wrap_exceptions
def restore_vault_from_object_store(ctx, from_json, compartment_id, if_match, backup_location):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if backup_location is not None:
        _details['backupLocation'] = cli_util.parse_json_parameter("backup_location", backup_location)

    client = cli_util.build_client('key_management', 'kms_vault', ctx)
    result = client.restore_vault_from_object_store(
        compartment_id=compartment_id,
        restore_vault_from_object_store_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vault_group.command(name=cli_util.override('kms_vault.restore_vault_from_object_store_backup_location_bucket.command_name', 'restore-vault-from-object-store-backup-location-bucket'), help=u"""Restores a vault from an encrypted backup file stored in Oracle Cloud Infrastructure Object Storage. If a vault with the same OCID already exists, this operation returns a response with a 409 HTTP status error code. \n[Command Reference](restoreVaultFromObjectStore)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--backup-location-namespace', required=True, help=u"""""")
@cli_util.option('--backup-location-bucket-name', required=True, help=u"""""")
@cli_util.option('--backup-location-object-name', required=True, help=u"""""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'Vault'})
@cli_util.wrap_exceptions
def restore_vault_from_object_store_backup_location_bucket(ctx, from_json, compartment_id, backup_location_namespace, backup_location_bucket_name, backup_location_object_name, if_match):

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

    client = cli_util.build_client('key_management', 'kms_vault', ctx)
    result = client.restore_vault_from_object_store(
        compartment_id=compartment_id,
        restore_vault_from_object_store_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vault_group.command(name=cli_util.override('kms_vault.restore_vault_from_object_store_backup_location_uri.command_name', 'restore-vault-from-object-store-backup-location-uri'), help=u"""Restores a vault from an encrypted backup file stored in Oracle Cloud Infrastructure Object Storage. If a vault with the same OCID already exists, this operation returns a response with a 409 HTTP status error code. \n[Command Reference](restoreVaultFromObjectStore)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--backup-location-uri', required=True, help=u"""""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'Vault'})
@cli_util.wrap_exceptions
def restore_vault_from_object_store_backup_location_uri(ctx, from_json, compartment_id, backup_location_uri, if_match):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['backupLocation'] = {}
    _details['backupLocation']['uri'] = backup_location_uri

    _details['backupLocation']['destination'] = 'PRE_AUTHENTICATED_REQUEST_URI'

    client = cli_util.build_client('key_management', 'kms_vault', ctx)
    result = client.restore_vault_from_object_store(
        compartment_id=compartment_id,
        restore_vault_from_object_store_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vault_group.command(name=cli_util.override('kms_vault.schedule_vault_deletion.command_name', 'schedule-vault-deletion'), help=u"""Schedules the deletion of the specified vault. This sets the lifecycle state of the vault and all keys in it that are not already scheduled for deletion to `PENDING_DELETION` and then deletes them after the retention period ends. The lifecycle state and time of deletion for keys already scheduled for deletion won't change. If any keys in the vault are scheduled to be deleted after the specified time of deletion for the vault, the call is rejected with the error code 409.

As a provisioning operation, this call is subject to a Key Management limit that applies to the total number of requests across all provisioning write operations. Key Management might throttle this call to reject an otherwise valid request when the total rate of provisioning write operations exceeds 10 requests per second for a given tenancy. \n[Command Reference](scheduleVaultDeletion)""")
@cli_util.option('--vault-id', required=True, help=u"""The OCID of the vault.""")
@cli_util.option('--time-of-deletion', type=custom_types.CLI_DATETIME, help=u"""An optional property indicating when to delete the vault, expressed in [RFC 3339] timestamp format. The specified time must be between 7 and 30 days from the time when the request is received. If this property is missing, it will be set to 30 days from the time of the request by default.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'Vault'})
@cli_util.wrap_exceptions
def schedule_vault_deletion(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, vault_id, time_of_deletion, if_match):

    if isinstance(vault_id, six.string_types) and len(vault_id.strip()) == 0:
        raise click.UsageError('Parameter --vault-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if time_of_deletion is not None:
        _details['timeOfDeletion'] = time_of_deletion

    client = cli_util.build_client('key_management', 'kms_vault', ctx)
    result = client.schedule_vault_deletion(
        vault_id=vault_id,
        schedule_vault_deletion_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_vault') and callable(getattr(client, 'get_vault')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_vault(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@vault_group.command(name=cli_util.override('kms_vault.update_vault.command_name', 'update'), help=u"""Updates the properties of a vault. Specifically, you can update the `displayName`, `freeformTags`, and `definedTags` properties. Furthermore, the vault must be in an ACTIVE or CREATING state to be updated.

As a provisioning operation, this call is subject to a Key Management limit that applies to the total number of requests across all provisioning write operations. Key Management might throttle this call to reject an otherwise valid request when the total rate of provisioning write operations exceeds 10 requests per second for a given tenancy. \n[Command Reference](updateVault)""")
@cli_util.option('--vault-id', required=True, help=u"""The OCID of the vault.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name for the vault. It does not have to be unique, and it is changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'key_management', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'key_management', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'key_management', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'key_management', 'class': 'dict(str, string)'}}, output_type={'module': 'key_management', 'class': 'Vault'})
@cli_util.wrap_exceptions
def update_vault(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, vault_id, defined_tags, display_name, freeform_tags, if_match):

    if isinstance(vault_id, six.string_types) and len(vault_id.strip()) == 0:
        raise click.UsageError('Parameter --vault-id cannot be whitespace or empty string')
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

    client = cli_util.build_client('key_management', 'kms_vault', ctx)
    result = client.update_vault(
        vault_id=vault_id,
        update_vault_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_vault') and callable(getattr(client, 'get_vault')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_vault(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
