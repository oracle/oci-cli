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


@cli.command(cli_util.override('kms_vault_root_group.command_name', 'kms-vault'), cls=CommandGroupWithAlias, help=cli_util.override('kms_vault_root_group.help', """API for managing and performing operations with keys and vaults."""), short_help=cli_util.override('kms_vault_root_group.short_help', """Key Management Service API"""))
@cli_util.help_option_group
def kms_vault_root_group():
    pass


@click.command(cli_util.override('vault_group.command_name', 'vault'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def vault_group():
    pass


kms_vault_root_group.add_command(vault_group)


@vault_group.command(name=cli_util.override('cancel_vault_deletion.command_name', 'cancel-vault-deletion'), help="""Cancels the scheduled deletion of the specified Vault, which must be in PendingDeletion state. The Vault and all Keys in it will be moved back to their previous states before the deletion was scheduled.""")
@cli_util.option('--vault-id', required=True, help="""The OCID of the vault.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
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
    client = cli_util.build_client('kms_vault', ctx)
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@vault_group.command(name=cli_util.override('create_vault.command_name', 'create'), help="""Creates a new vault. The type of vault you create determines key placement, pricing, and available options. Options include storage isolation, a dedicated service endpoint instead of a shared service endpoint for API calls, and a dedicated HSM or a multitenant HSM.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment where you want to create this vault.""")
@cli_util.option('--display-name', required=True, help="""A user-friendly name for the vault. It does not have to be unique, and it is changeable. Avoid entering confidential information.""")
@cli_util.option('--vault-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["VIRTUAL_PRIVATE"]), help="""The type of vault to create. Each type of vault stores the key with different degrees of isolation and has different options and pricing.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'Vault'})
@cli_util.wrap_exceptions
def create_vault(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, vault_type):
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['compartmentId'] = compartment_id
    details['displayName'] = display_name
    details['vaultType'] = vault_type

    client = cli_util.build_client('kms_vault', ctx)
    result = client.create_vault(
        create_vault_details=details,
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@vault_group.command(name=cli_util.override('get_vault.command_name', 'get'), help="""Gets the specified vault's configuration information.""")
@cli_util.option('--vault-id', required=True, help="""The OCID of the vault.""")
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
    client = cli_util.build_client('kms_vault', ctx)
    result = client.get_vault(
        vault_id=vault_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vault_group.command(name=cli_util.override('list_vaults.command_name', 'list'), help="""Lists vaults in the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by. You can specify only one sort order. The default order for TIMECREATED is descending. The default order for DISPLAYNAME is ascending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
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
    client = cli_util.build_client('kms_vault', ctx)
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


@vault_group.command(name=cli_util.override('schedule_vault_deletion.command_name', 'schedule-vault-deletion'), help="""Schedules the deletion of the specified Vault. The Vault and all Keys in it will be moved to PendingDeletion state and deleted after the retention period.""")
@cli_util.option('--vault-id', required=True, help="""The OCID of the vault.""")
@cli_util.option('--time-of-deletion', type=custom_types.CLI_DATETIME, help="""An optional property to indicate the deletion time of the Vault. The time format should comply with RFC-3339 standards. This time must be between 7 to 30 days from the time when the request is received. If the property is missing, it will be set to 30 days from request time by default.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
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

    details = {}

    if time_of_deletion is not None:
        details['timeOfDeletion'] = time_of_deletion

    client = cli_util.build_client('kms_vault', ctx)
    result = client.schedule_vault_deletion(
        vault_id=vault_id,
        schedule_vault_deletion_details=details,
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@vault_group.command(name=cli_util.override('update_vault.command_name', 'update'), help="""Updates the properties of a vault. Specifically, you can only update the `displayName` property. Furthermore, the vault must be in an `ACTIVE` or `CREATING` state.""")
@cli_util.option('--vault-id', required=True, help="""The OCID of the vault.""")
@cli_util.option('--display-name', help="""A user-friendly name for the vault. It does not have to be unique, and it is changeable. Avoid entering confidential information.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'Vault'})
@cli_util.wrap_exceptions
def update_vault(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, vault_id, display_name, if_match):

    if isinstance(vault_id, six.string_types) and len(vault_id.strip()) == 0:
        raise click.UsageError('Parameter --vault-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('kms_vault', ctx)
    result = client.update_vault(
        vault_id=vault_id,
        update_vault_details=details,
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
