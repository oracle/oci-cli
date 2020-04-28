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
from services.ons.src.oci_cli_ons.generated import ons_service_cli


@click.command(cli_util.override('notification_data_plane.notification_data_plane_root_group.command_name', 'notification-data-plane'), cls=CommandGroupWithAlias, help=cli_util.override('notification_data_plane.notification_data_plane_root_group.help', """Use the Notifications API to broadcast messages to distributed components by topic, using a publish-subscribe pattern.
For information about managing topics, subscriptions, and messages, see [Notifications Overview]."""), short_help=cli_util.override('notification_data_plane.notification_data_plane_root_group.short_help', """Notifications API"""))
@cli_util.help_option_group
def notification_data_plane_root_group():
    pass


@click.command(cli_util.override('notification_data_plane.subscription_group.command_name', 'subscription'), cls=CommandGroupWithAlias, help="""The subscription's configuration. For general information about subscriptions, see [Notifications Overview].""")
@cli_util.help_option_group
def subscription_group():
    pass


@click.command(cli_util.override('notification_data_plane.notification_topic_group.command_name', 'notification-topic'), cls=CommandGroupWithAlias, help="""The properties that define a topic. For general information about topics, see [Notifications Overview].""")
@cli_util.help_option_group
def notification_topic_group():
    pass


ons_service_cli.ons_service_group.add_command(notification_data_plane_root_group)
notification_data_plane_root_group.add_command(subscription_group)
notification_data_plane_root_group.add_command(notification_topic_group)


@subscription_group.command(name=cli_util.override('notification_data_plane.change_subscription_compartment.command_name', 'change-compartment'), help=u"""Moves a subscription into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment].

Transactions Per Minute (TPM) per-tenancy limit for this operation: 60.""")
@cli_util.option('--subscription-id', required=True, help=u"""The [OCID] of the subscription to move.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the specified topic or subscription to.""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_subscription_compartment(ctx, from_json, subscription_id, compartment_id, if_match):

    if isinstance(subscription_id, six.string_types) and len(subscription_id.strip()) == 0:
        raise click.UsageError('Parameter --subscription-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('ons', 'notification_data_plane', ctx)
    result = client.change_subscription_compartment(
        subscription_id=subscription_id,
        change_subscription_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@subscription_group.command(name=cli_util.override('notification_data_plane.create_subscription.command_name', 'create'), help=u"""Creates a subscription for the specified topic and sends a subscription confirmation URL to the endpoint. The subscription remains in \"Pending\" status until it has been confirmed. For information about confirming subscriptions, see [To confirm a subscription].

Transactions Per Minute (TPM) per-tenancy limit for this operation: 60.""")
@cli_util.option('--topic-id', required=True, help=u"""The [OCID] of the topic for the subscription.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment for the subscription.""")
@cli_util.option('--protocol', required=True, help=u"""The protocol used for the subscription.

Allowed values:   * `CUSTOM_HTTPS`   * `EMAIL`   * `HTTPS` (deprecated; for PagerDuty endpoints, use `PAGERDUTY`)   * `PAGERDUTY`   * `SLACK`   * `ORACLE_FUNCTIONS`

For information about subscription protocols, see [To create a subscription].""")
@cli_util.option('--endpoint-parameterconflict', required=True, help=u"""A locator that corresponds to the subscription protocol. For example, an email address for a subscription that uses the `EMAIL` protocol, or a URL for a subscription that uses an HTTP-based protocol. HTTP-based protocols use URL endpoints that begin with \"http:\" or \"https:\". A URL cannot exceed 512 characters. Avoid entering confidential information.

For protocol-specific endpoint formats and steps to get or create endpoints, see [To create a subscription].""")
@cli_util.option('--metadata', help=u"""Metadata for the subscription.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PENDING", "ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'ons', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ons', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ons', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ons', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ons', 'class': 'Subscription'})
@cli_util.wrap_exceptions
def create_subscription(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, topic_id, compartment_id, protocol, endpoint_parameterconflict, metadata, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['topicId'] = topic_id
    _details['compartmentId'] = compartment_id
    _details['protocol'] = protocol
    _details['endpoint'] = endpoint_parameterconflict

    if metadata is not None:
        _details['metadata'] = metadata

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('ons', 'notification_data_plane', ctx)
    result = client.create_subscription(
        create_subscription_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_subscription') and callable(getattr(client, 'get_subscription')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_subscription(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@subscription_group.command(name=cli_util.override('notification_data_plane.delete_subscription.command_name', 'delete'), help=u"""Deletes the specified subscription.

Transactions Per Minute (TPM) per-tenancy limit for this operation: 60.""")
@cli_util.option('--subscription-id', required=True, help=u"""The [OCID] of the subscription to delete.""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PENDING", "ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_subscription(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, subscription_id, if_match):

    if isinstance(subscription_id, six.string_types) and len(subscription_id.strip()) == 0:
        raise click.UsageError('Parameter --subscription-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ons', 'notification_data_plane', ctx)
    result = client.delete_subscription(
        subscription_id=subscription_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_subscription') and callable(getattr(client, 'get_subscription')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_subscription(subscription_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@subscription_group.command(name=cli_util.override('notification_data_plane.get_confirm_subscription.command_name', 'get-confirm'), help=u"""Gets the confirmation details for the specified subscription.

Transactions Per Minute (TPM) per-tenancy limit for this operation: 60.""")
@cli_util.option('--id', required=True, help=u"""The [OCID] of the subscription to get the confirmation details for.""")
@cli_util.option('--token', required=True, help=u"""The subscription confirmation token.""")
@cli_util.option('--protocol', required=True, help=u"""The protocol used for the subscription.

Allowed values:   * `CUSTOM_HTTPS`   * `EMAIL`   * `HTTPS` (deprecated; for PagerDuty endpoints, use `PAGERDUTY`)   * `PAGERDUTY`   * `SLACK`   * `ORACLE_FUNCTIONS`

For information about subscription protocols, see [To create a subscription].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ons', 'class': 'ConfirmationResult'})
@cli_util.wrap_exceptions
def get_confirm_subscription(ctx, from_json, id, token, protocol):

    if isinstance(id, six.string_types) and len(id.strip()) == 0:
        raise click.UsageError('Parameter --id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ons', 'notification_data_plane', ctx)
    result = client.get_confirm_subscription(
        id=id,
        token=token,
        protocol=protocol,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@subscription_group.command(name=cli_util.override('notification_data_plane.get_subscription.command_name', 'get'), help=u"""Gets the specified subscription's configuration information.

Transactions Per Minute (TPM) per-tenancy limit for this operation: 60.""")
@cli_util.option('--subscription-id', required=True, help=u"""The [OCID] of the subscription to retrieve.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ons', 'class': 'Subscription'})
@cli_util.wrap_exceptions
def get_subscription(ctx, from_json, subscription_id):

    if isinstance(subscription_id, six.string_types) and len(subscription_id.strip()) == 0:
        raise click.UsageError('Parameter --subscription-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ons', 'notification_data_plane', ctx)
    result = client.get_subscription(
        subscription_id=subscription_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@subscription_group.command(name=cli_util.override('notification_data_plane.get_unsubscription.command_name', 'get-un'), help=u"""Gets the unsubscription details for the specified subscription.

Transactions Per Minute (TPM) per-tenancy limit for this operation: 60.""")
@cli_util.option('--id', required=True, help=u"""The [OCID] of the subscription to unsubscribe from.""")
@cli_util.option('--token', required=True, help=u"""The subscription confirmation token.""")
@cli_util.option('--protocol', required=True, help=u"""The protocol used for the subscription.

Allowed values:   * `CUSTOM_HTTPS`   * `EMAIL`   * `HTTPS` (deprecated; for PagerDuty endpoints, use `PAGERDUTY`)   * `PAGERDUTY`   * `SLACK`   * `ORACLE_FUNCTIONS`

For information about subscription protocols, see [To create a subscription].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_unsubscription(ctx, from_json, id, token, protocol):

    if isinstance(id, six.string_types) and len(id.strip()) == 0:
        raise click.UsageError('Parameter --id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ons', 'notification_data_plane', ctx)
    result = client.get_unsubscription(
        id=id,
        token=token,
        protocol=protocol,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@subscription_group.command(name=cli_util.override('notification_data_plane.list_subscriptions.command_name', 'list'), help=u"""Lists the subscriptions in the specified compartment or topic.

Transactions Per Minute (TPM) per-tenancy limit for this operation: 60.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--topic-id', help=u"""Return all subscriptions that are subscribed to the given topic OCID. Either this query parameter or the compartmentId query parameter must be set.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the opc-next-page response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ons', 'class': 'list[SubscriptionSummary]'})
@cli_util.wrap_exceptions
def list_subscriptions(ctx, from_json, all_pages, page_size, compartment_id, topic_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if topic_id is not None:
        kwargs['topic_id'] = topic_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ons', 'notification_data_plane', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_subscriptions,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_subscriptions,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_subscriptions(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@notification_topic_group.command(name=cli_util.override('notification_data_plane.publish_message.command_name', 'publish-message'), help=u"""Publishes a message to the specified topic.

The topic endpoint is required for this operation. To get the topic endpoint, use [GetTopic] and review the `apiEndpoint` value in the response ([NotificationTopic]).

Limits information follows.

Message size limit per request: 64KB.

Message delivery rate limit per endpoint: 60 messages per minute for HTTP-based protocols, 10 messages per minute for the `EMAIL` protocol. HTTP-based protocols use URL endpoints that begin with \"http:\" or \"https:\".

Transactions Per Minute (TPM) per-tenancy limit for this operation: 60 per topic.

For more information about publishing messages, see [Publishing Messages]. For steps to request a limit increase, see [Requesting a Service Limit Increase].""")
@cli_util.option('--topic-id', required=True, help=u"""The [OCID] of the topic.""")
@cli_util.option('--body', required=True, help=u"""The body of the message to be published. For `messageType` of JSON, a default key-value pair is required. Example: `{\"default\": \"Alarm breached\", \"Email\": \"Alarm breached: <url>\"}.` Avoid entering confidential information.""")
@cli_util.option('--title', help=u"""The title of the message to be published. Avoid entering confidential information.""")
@cli_util.option('--message-type', type=custom_types.CliCaseInsensitiveChoice(["JSON", "RAW_TEXT"]), help=u"""Type of message body in the request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ons', 'class': 'PublishResult'})
@cli_util.wrap_exceptions
def publish_message(ctx, from_json, topic_id, body, title, message_type):

    if isinstance(topic_id, six.string_types) and len(topic_id.strip()) == 0:
        raise click.UsageError('Parameter --topic-id cannot be whitespace or empty string')

    kwargs = {}
    if message_type is not None:
        kwargs['message_type'] = message_type
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['body'] = body

    if title is not None:
        _details['title'] = title

    client = cli_util.build_client('ons', 'notification_data_plane', ctx)
    result = client.publish_message(
        topic_id=topic_id,
        message_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@subscription_group.command(name=cli_util.override('notification_data_plane.resend_subscription_confirmation.command_name', 'resend-subscription-confirmation'), help=u"""Resends the confirmation details for the specified subscription.

Transactions Per Minute (TPM) per-tenancy limit for this operation: 60.""")
@cli_util.option('--id', required=True, help=u"""The [OCID] of the subscription to resend the confirmation for.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ons', 'class': 'Subscription'})
@cli_util.wrap_exceptions
def resend_subscription_confirmation(ctx, from_json, id):

    if isinstance(id, six.string_types) and len(id.strip()) == 0:
        raise click.UsageError('Parameter --id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ons', 'notification_data_plane', ctx)
    result = client.resend_subscription_confirmation(
        id=id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@subscription_group.command(name=cli_util.override('notification_data_plane.update_subscription.command_name', 'update'), help=u"""Updates the specified subscription's configuration.

Transactions Per Minute (TPM) per-tenancy limit for this operation: 60.""")
@cli_util.option('--subscription-id', required=True, help=u"""The [OCID] of the subscription to update.""")
@cli_util.option('--delivery-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The delivery policy of the subscription. Stored as a JSON string.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'delivery-policy': {'module': 'ons', 'class': 'DeliveryPolicy'}, 'freeform-tags': {'module': 'ons', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ons', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'delivery-policy': {'module': 'ons', 'class': 'DeliveryPolicy'}, 'freeform-tags': {'module': 'ons', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ons', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ons', 'class': 'UpdateSubscriptionDetails'})
@cli_util.wrap_exceptions
def update_subscription(ctx, from_json, force, subscription_id, delivery_policy, freeform_tags, defined_tags, if_match):

    if isinstance(subscription_id, six.string_types) and len(subscription_id.strip()) == 0:
        raise click.UsageError('Parameter --subscription-id cannot be whitespace or empty string')
    if not force:
        if delivery_policy or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to delivery-policy and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if delivery_policy is not None:
        _details['deliveryPolicy'] = cli_util.parse_json_parameter("delivery_policy", delivery_policy)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('ons', 'notification_data_plane', ctx)
    result = client.update_subscription(
        subscription_id=subscription_id,
        update_subscription_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
