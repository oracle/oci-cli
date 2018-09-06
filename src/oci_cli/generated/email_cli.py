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


@cli.command(cli_util.override('email_root_group.command_name', 'email'), cls=CommandGroupWithAlias, help=cli_util.override('email_root_group.help', """API spec for managing OCI Email Delivery services."""), short_help=cli_util.override('email_root_group.short_help', """Email Delivery Service API"""))
@cli_util.help_option_group
def email_root_group():
    pass


@click.command(cli_util.override('sender_group.command_name', 'sender'), cls=CommandGroupWithAlias, help="""The full information representing an approved sender.""")
@cli_util.help_option_group
def sender_group():
    pass


@click.command(cli_util.override('suppression_group.command_name', 'suppression'), cls=CommandGroupWithAlias, help="""The full information representing an email suppression.""")
@cli_util.help_option_group
def suppression_group():
    pass


email_root_group.add_command(sender_group)
email_root_group.add_command(suppression_group)


@sender_group.command(name=cli_util.override('create_sender.command_name', 'create'), help="""Creates a sender for a tenancy in a given compartment.""")
@cli_util.option('--compartment-id', help="""The OCID of the compartment that contains the sender.""")
@cli_util.option('--email-address', help="""The email address of the sender.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'email', 'class': 'Sender'})
@cli_util.wrap_exceptions
def create_sender(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, email_address):
    kwargs = {}

    details = {}

    if compartment_id is not None:
        details['compartmentId'] = compartment_id

    if email_address is not None:
        details['emailAddress'] = email_address

    client = cli_util.build_client('email', ctx)
    result = client.create_sender(
        create_sender_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_sender') and callable(getattr(client, 'get_sender')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_sender(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@suppression_group.command(name=cli_util.override('create_suppression.command_name', 'create'), help="""Adds recipient email addresses to the suppression list for a tenancy.""")
@cli_util.option('--compartment-id', help="""The OCID of the compartment to contain the suppression. Since suppressions are at the customer level, this must be the tenancy OCID.""")
@cli_util.option('--email-address', help="""The recipient email address of the suppression.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'email', 'class': 'Suppression'})
@cli_util.wrap_exceptions
def create_suppression(ctx, from_json, compartment_id, email_address):
    kwargs = {}

    details = {}

    if compartment_id is not None:
        details['compartmentId'] = compartment_id

    if email_address is not None:
        details['emailAddress'] = email_address

    client = cli_util.build_client('email', ctx)
    result = client.create_suppression(
        create_suppression_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@sender_group.command(name=cli_util.override('delete_sender.command_name', 'delete'), help="""Deletes an approved sender for a tenancy in a given compartment for a provided `senderId`.""")
@cli_util.option('--sender-id', required=True, help="""The unique OCID of the sender.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_sender(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, sender_id):

    if isinstance(sender_id, six.string_types) and len(sender_id.strip()) == 0:
        raise click.UsageError('Parameter --sender-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('email', ctx)
    result = client.delete_sender(
        sender_id=sender_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_sender') and callable(getattr(client, 'get_sender')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_sender(sender_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@suppression_group.command(name=cli_util.override('delete_suppression.command_name', 'delete'), help="""Removes a suppressed recipient email address from the suppression list for a tenancy in a given compartment for a provided `suppressionId`.""")
@cli_util.option('--suppression-id', required=True, help="""The unique OCID of the suppression.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_suppression(ctx, from_json, suppression_id):

    if isinstance(suppression_id, six.string_types) and len(suppression_id.strip()) == 0:
        raise click.UsageError('Parameter --suppression-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('email', ctx)
    result = client.delete_suppression(
        suppression_id=suppression_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@sender_group.command(name=cli_util.override('get_sender.command_name', 'get'), help="""Gets an approved sender for a given `senderId`.""")
@cli_util.option('--sender-id', required=True, help="""The unique OCID of the sender.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'email', 'class': 'Sender'})
@cli_util.wrap_exceptions
def get_sender(ctx, from_json, sender_id):

    if isinstance(sender_id, six.string_types) and len(sender_id.strip()) == 0:
        raise click.UsageError('Parameter --sender-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('email', ctx)
    result = client.get_sender(
        sender_id=sender_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@suppression_group.command(name=cli_util.override('get_suppression.command_name', 'get'), help="""Gets the details of a suppressed recipient email address for a given `suppressionId`. Each suppression is given a unique OCID.""")
@cli_util.option('--suppression-id', required=True, help="""The unique OCID of the suppression.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'email', 'class': 'Suppression'})
@cli_util.wrap_exceptions
def get_suppression(ctx, from_json, suppression_id):

    if isinstance(suppression_id, six.string_types) and len(suppression_id.strip()) == 0:
        raise click.UsageError('Parameter --suppression-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('email', ctx)
    result = client.get_suppression(
        suppression_id=suppression_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@sender_group.command(name=cli_util.override('list_senders.command_name', 'list'), help="""Gets a collection of approved sender email addresses and sender IDs.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID for the compartment.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED"]), help="""The current state of a sender.""")
@cli_util.option('--email-address', help="""The email address of the approved sender.""")
@cli_util.option('--page', help="""The value of the `opc-next-page` response header from the previous GET request.""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return in a paginated GET request.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "EMAILADDRESS"]), help="""The field to sort by. The `TIMECREATED` value returns the list in in descending order by default. The `EMAILADDRESS` value returns the list in ascending order by default. Use the `SortOrderQueryParam` to change the direction of the returned list of items.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending or descending order.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'email', 'class': 'list[SenderSummary]'})
@cli_util.wrap_exceptions
def list_senders(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, email_address, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if email_address is not None:
        kwargs['email_address'] = email_address
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    client = cli_util.build_client('email', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_senders,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_senders,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_senders(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@suppression_group.command(name=cli_util.override('list_suppressions.command_name', 'list'), help="""Gets a list of suppressed recipient email addresses for a user. The `compartmentId` for suppressions must be a tenancy OCID. The returned list is sorted by creation time in descending order.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID for the compartment.""")
@cli_util.option('--email-address', help="""The email address of the suppression.""")
@cli_util.option('--time-created-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help="""Search for suppressions that were created within a specific date range, using this parameter to specify the earliest creation date for the returned list (inclusive). Specifying this parameter without the corresponding `timeCreatedLessThan` parameter will retrieve suppressions created from the given `timeCreatedGreaterThanOrEqualTo` to the current time, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339.

**Example:** 2016-12-19T16:39:57.600Z""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-created-less-than', type=custom_types.CLI_DATETIME, help="""Search for suppressions that were created within a specific date range, using this parameter to specify the latest creation date for the returned list (exclusive). Specifying this parameter without the corresponding `timeCreatedGreaterThanOrEqualTo` parameter will retrieve all suppressions created before the specified end date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339.

**Example:** 2016-12-19T16:39:57.600Z""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--page', help="""The value of the `opc-next-page` response header from the previous GET request.""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return in a paginated GET request.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "EMAILADDRESS"]), help="""The field to sort by. The `TIMECREATED` value returns the list in in descending order by default. The `EMAILADDRESS` value returns the list in ascending order by default. Use the `SortOrderQueryParam` to change the direction of the returned list of items.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending or descending order.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'email', 'class': 'list[SuppressionSummary]'})
@cli_util.wrap_exceptions
def list_suppressions(ctx, from_json, all_pages, page_size, compartment_id, email_address, time_created_greater_than_or_equal_to, time_created_less_than, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if email_address is not None:
        kwargs['email_address'] = email_address
    if time_created_greater_than_or_equal_to is not None:
        kwargs['time_created_greater_than_or_equal_to'] = time_created_greater_than_or_equal_to
    if time_created_less_than is not None:
        kwargs['time_created_less_than'] = time_created_less_than
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    client = cli_util.build_client('email', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_suppressions,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_suppressions,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_suppressions(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)
