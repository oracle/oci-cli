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


@cli.command(cli_util.override('kms_management_root_group.command_name', 'kms-management'), cls=CommandGroupWithAlias, help=cli_util.override('kms_management_root_group.help', """API for managing and performing operations with keys and vaults."""), short_help=cli_util.override('kms_management_root_group.short_help', """Key Management Service API"""))
@cli_util.help_option_group
def kms_management_root_group():
    pass


@click.command(cli_util.override('key_version_group.command_name', 'key-version'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def key_version_group():
    pass


@click.command(cli_util.override('key_group.command_name', 'key'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def key_group():
    pass


kms_management_root_group.add_command(key_version_group)
kms_management_root_group.add_command(key_group)


@key_group.command(name=cli_util.override('create_key.command_name', 'create'), help="""Creates a new key.

The top level --endpoint parameter must be supplied for this operation.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment that contains this key.""")
@cli_util.option('--display-name', required=True, help="""A user-friendly name for the key. It does not have to be unique, and it is changeable. Avoid entering confidential information.""")
@cli_util.option('--key-shape', required=True, type=custom_types.CLI_COMPLEX_TYPE, help="""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'key-shape': {'module': 'key_management', 'class': 'KeyShape'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'key-shape': {'module': 'key_management', 'class': 'KeyShape'}}, output_type={'module': 'key_management', 'class': 'Key'})
@cli_util.wrap_exceptions
def create_key(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, key_shape):
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['compartmentId'] = compartment_id
    details['displayName'] = display_name
    details['keyShape'] = cli_util.parse_json_parameter("key_shape", key_shape)

    client = cli_util.build_client('kms_management', ctx)
    result = client.create_key(
        create_key_details=details,
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@key_version_group.command(name=cli_util.override('create_key_version.command_name', 'create'), help="""Generates new cryptographic material for a key. Key must be in an `ENABLED` state to be rotated.

The top level --endpoint parameter must be supplied for this operation.""")
@cli_util.option('--key-id', required=True, help="""The OCID of the key.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'KeyVersion'})
@cli_util.wrap_exceptions
def create_key_version(ctx, from_json, key_id):

    if isinstance(key_id, six.string_types) and len(key_id.strip()) == 0:
        raise click.UsageError('Parameter --key-id cannot be whitespace or empty string')
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('kms_management', ctx)
    result = client.create_key_version(
        key_id=key_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@key_group.command(name=cli_util.override('disable_key.command_name', 'disable'), help="""Disables a key to make it unavailable for encryption or decryption.

The top level --endpoint parameter must be supplied for this operation.""")
@cli_util.option('--key-id', required=True, help="""The OCID of the key.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
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
    client = cli_util.build_client('kms_management', ctx)
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@key_group.command(name=cli_util.override('enable_key.command_name', 'enable'), help="""Enables a key to make it available for encryption or decryption.

The top level --endpoint parameter must be supplied for this operation.""")
@cli_util.option('--key-id', required=True, help="""The OCID of the key.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
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
    client = cli_util.build_client('kms_management', ctx)
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@key_group.command(name=cli_util.override('get_key.command_name', 'get'), help="""Gets information about the specified key.

The top level --endpoint parameter must be supplied for this operation.""")
@cli_util.option('--key-id', required=True, help="""The OCID of the key.""")
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
    client = cli_util.build_client('kms_management', ctx)
    result = client.get_key(
        key_id=key_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@key_version_group.command(name=cli_util.override('get_key_version.command_name', 'get'), help="""Gets information about the specified key version.

The top level --endpoint parameter must be supplied for this operation.""")
@cli_util.option('--key-id', required=True, help="""The OCID of the key.""")
@cli_util.option('--key-version-id', required=True, help="""The OCID of the key version.""")
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
    client = cli_util.build_client('kms_management', ctx)
    result = client.get_key_version(
        key_id=key_id,
        key_version_id=key_version_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@key_version_group.command(name=cli_util.override('list_key_versions.command_name', 'list'), help="""Lists all key versions for the specified key.

The top level --endpoint parameter must be supplied for this operation.""")
@cli_util.option('--key-id', required=True, help="""The OCID of the key.""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by. You can specify only one sort order. The default order for TIMECREATED is descending. The default order for DISPLAYNAME is ascending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
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
    client = cli_util.build_client('kms_management', ctx)
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


@key_group.command(name=cli_util.override('list_keys.command_name', 'list'), help="""Lists the keys in the specified vault and compartment.

The top level --endpoint parameter must be supplied for this operation.""")
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
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'list[KeySummary]'})
@cli_util.wrap_exceptions
def list_keys(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_by, sort_order):

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
    client = cli_util.build_client('kms_management', ctx)
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


@key_group.command(name=cli_util.override('update_key.command_name', 'update'), help="""Updates the properties of a key. Specifically, you can only update the `displayName` property. Furthermore, the key must in an `ACTIVE` or `CREATING` state.

The top level --endpoint parameter must be supplied for this operation.""")
@cli_util.option('--key-id', required=True, help="""The OCID of the key.""")
@cli_util.option('--display-name', help="""A user-friendly name for the key. It does not have to be unique, and it is changeable. Avoid entering confidential information.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'Key'})
@cli_util.wrap_exceptions
def update_key(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, key_id, display_name, if_match):

    if isinstance(key_id, six.string_types) and len(key_id.strip()) == 0:
        raise click.UsageError('Parameter --key-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('kms_management', ctx)
    result = client.update_key(
        key_id=key_id,
        update_key_details=details,
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
