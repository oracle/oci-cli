# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('email.email_root_group.command_name', 'email'), cls=CommandGroupWithAlias, help=cli_util.override('email.email_root_group.help', """API for the Email Delivery service. Use this API to send high-volume, application-generated
emails. For more information, see [Overview of the Email Delivery Service].


**Note:** Write actions (POST, UPDATE, DELETE) may take several minutes to propagate and be reflected by the API. If a subsequent read request fails to reflect your changes, wait a few minutes and try again."""), short_help=cli_util.override('email.email_root_group.short_help', """Email Delivery API"""))
@cli_util.help_option_group
def email_root_group():
    pass


@click.command(cli_util.override('email.sender_group.command_name', 'sender'), cls=CommandGroupWithAlias, help="""The full information representing an approved sender.""")
@cli_util.help_option_group
def sender_group():
    pass


@click.command(cli_util.override('email.suppression_group.command_name', 'suppression'), cls=CommandGroupWithAlias, help="""The full information representing an email suppression.""")
@cli_util.help_option_group
def suppression_group():
    pass


email_root_group.add_command(sender_group)
email_root_group.add_command(suppression_group)


@sender_group.command(name=cli_util.override('email.change_sender_compartment.command_name', 'change-compartment'), help=u"""Moves a sender into a different compartment. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeSenderCompartment)""")
@cli_util.option('--sender-id', required=True, help=u"""The unique OCID of the sender.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the sender should be moved.""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_sender_compartment(ctx, from_json, sender_id, compartment_id, if_match):

    if isinstance(sender_id, six.string_types) and len(sender_id.strip()) == 0:
        raise click.UsageError('Parameter --sender-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('email', 'email', ctx)
    result = client.change_sender_compartment(
        sender_id=sender_id,
        change_sender_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@sender_group.command(name=cli_util.override('email.create_sender.command_name', 'create'), help=u"""Creates a sender for a tenancy in a given compartment. \n[Command Reference](createSender)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment that contains the sender.""")
@cli_util.option('--email-address', required=True, help=u"""The email address of the sender.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'email', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'email', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'email', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'email', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'email', 'class': 'Sender'})
@cli_util.wrap_exceptions
def create_sender(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, email_address, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['emailAddress'] = email_address

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('email', 'email', ctx)
    result = client.create_sender(
        create_sender_details=_details,
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


@suppression_group.command(name=cli_util.override('email.create_suppression.command_name', 'create'), help=u"""Adds recipient email addresses to the suppression list for a tenancy. Addresses added to the suppression list via the API are denoted as \"MANUAL\" in the `reason` field. *Note:* All email addresses added to the suppression list are normalized to include only lowercase letters. \n[Command Reference](createSuppression)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to contain the suppression. Since suppressions are at the customer level, this must be the tenancy OCID.""")
@cli_util.option('--email-address', required=True, help=u"""The recipient email address of the suppression.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'email', 'class': 'Suppression'})
@cli_util.wrap_exceptions
def create_suppression(ctx, from_json, compartment_id, email_address):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['emailAddress'] = email_address

    client = cli_util.build_client('email', 'email', ctx)
    result = client.create_suppression(
        create_suppression_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@sender_group.command(name=cli_util.override('email.delete_sender.command_name', 'delete'), help=u"""Deletes an approved sender for a tenancy in a given compartment for a provided `senderId`. \n[Command Reference](deleteSender)""")
@cli_util.option('--sender-id', required=True, help=u"""The unique OCID of the sender.""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_sender(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, sender_id, if_match):

    if isinstance(sender_id, six.string_types) and len(sender_id.strip()) == 0:
        raise click.UsageError('Parameter --sender-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('email', 'email', ctx)
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


@suppression_group.command(name=cli_util.override('email.delete_suppression.command_name', 'delete'), help=u"""Removes a suppressed recipient email address from the suppression list for a tenancy in a given compartment for a provided `suppressionId`. \n[Command Reference](deleteSuppression)""")
@cli_util.option('--suppression-id', required=True, help=u"""The unique OCID of the suppression.""")
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
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('email', 'email', ctx)
    result = client.delete_suppression(
        suppression_id=suppression_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@sender_group.command(name=cli_util.override('email.get_sender.command_name', 'get'), help=u"""Gets an approved sender for a given `senderId`. \n[Command Reference](getSender)""")
@cli_util.option('--sender-id', required=True, help=u"""The unique OCID of the sender.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'email', 'class': 'Sender'})
@cli_util.wrap_exceptions
def get_sender(ctx, from_json, sender_id):

    if isinstance(sender_id, six.string_types) and len(sender_id.strip()) == 0:
        raise click.UsageError('Parameter --sender-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('email', 'email', ctx)
    result = client.get_sender(
        sender_id=sender_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@suppression_group.command(name=cli_util.override('email.get_suppression.command_name', 'get'), help=u"""Gets the details of a suppressed recipient email address for a given `suppressionId`. Each suppression is given a unique OCID. \n[Command Reference](getSuppression)""")
@cli_util.option('--suppression-id', required=True, help=u"""The unique OCID of the suppression.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'email', 'class': 'Suppression'})
@cli_util.wrap_exceptions
def get_suppression(ctx, from_json, suppression_id):

    if isinstance(suppression_id, six.string_types) and len(suppression_id.strip()) == 0:
        raise click.UsageError('Parameter --suppression-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('email', 'email', ctx)
    result = client.get_suppression(
        suppression_id=suppression_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@sender_group.command(name=cli_util.override('email.list_senders.command_name', 'list'), help=u"""Gets a collection of approved sender email addresses and sender IDs. \n[Command Reference](listSenders)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID for the compartment.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED"]), help=u"""The current state of a sender.""")
@cli_util.option('--email-address', help=u"""The email address of the approved sender.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the opc-next-page response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. `1` is the minimum, `1000` is the maximum. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "EMAILADDRESS"]), help=u"""The field to sort by. The `TIMECREATED` value returns the list in in descending order by default. The `EMAILADDRESS` value returns the list in ascending order by default. Use the `SortOrderQueryParam` to change the direction of the returned list of items.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending or descending order.""")
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
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('email', 'email', ctx)
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


@suppression_group.command(name=cli_util.override('email.list_suppressions.command_name', 'list'), help=u"""Gets a list of suppressed recipient email addresses for a user. The `compartmentId` for suppressions must be a tenancy OCID. The returned list is sorted by creation time in descending order. \n[Command Reference](listSuppressions)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID for the compartment.""")
@cli_util.option('--email-address', help=u"""The email address of the suppression.""")
@cli_util.option('--time-created-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""Search for suppressions that were created within a specific date range, using this parameter to specify the earliest creation date for the returned list (inclusive). Specifying this parameter without the corresponding `timeCreatedLessThan` parameter will retrieve suppressions created from the given `timeCreatedGreaterThanOrEqualTo` to the current time, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339.

**Example:** 2016-12-19T16:39:57.600Z""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-created-less-than', type=custom_types.CLI_DATETIME, help=u"""Search for suppressions that were created within a specific date range, using this parameter to specify the latest creation date for the returned list (exclusive). Specifying this parameter without the corresponding `timeCreatedGreaterThanOrEqualTo` parameter will retrieve all suppressions created before the specified end date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339.

**Example:** 2016-12-19T16:39:57.600Z""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--page', help=u"""For list pagination. The value of the opc-next-page response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. `1` is the minimum, `1000` is the maximum. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "EMAILADDRESS"]), help=u"""The field to sort by. The `TIMECREATED` value returns the list in in descending order by default. The `EMAILADDRESS` value returns the list in ascending order by default. Use the `SortOrderQueryParam` to change the direction of the returned list of items.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending or descending order.""")
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
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('email', 'email', ctx)
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


@sender_group.command(name=cli_util.override('email.update_sender.command_name', 'update'), help=u"""Replaces the set of tags for a sender with the tags provided. If either freeform or defined tags are omitted, the tags for that set remain the same. Each set must include the full set of tags for the sender, partial updates are not permitted. For more information about tagging, see [Resource Tags]. \n[Command Reference](updateSender)""")
@cli_util.option('--sender-id', required=True, help=u"""The unique OCID of the sender.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'email', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'email', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'email', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'email', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'email', 'class': 'Sender'})
@cli_util.wrap_exceptions
def update_sender(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, sender_id, freeform_tags, defined_tags, if_match):

    if isinstance(sender_id, six.string_types) and len(sender_id.strip()) == 0:
        raise click.UsageError('Parameter --sender-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('email', 'email', ctx)
    result = client.update_sender(
        sender_id=sender_id,
        update_sender_details=_details,
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
