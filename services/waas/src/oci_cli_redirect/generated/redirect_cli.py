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
from services.waas.src.oci_cli_waas.generated import waas_service_cli


@click.command(cli_util.override('redirect.redirect_root_group.command_name', 'redirect'), cls=CommandGroupWithAlias, help=cli_util.override('redirect.redirect_root_group.help', """OCI Web Application Acceleration and Security Services"""), short_help=cli_util.override('redirect.redirect_root_group.short_help', """Web Application Acceleration and Security Services API"""))
@cli_util.help_option_group
def redirect_root_group():
    pass


@click.command(cli_util.override('redirect.http_redirect_group.command_name', 'http-redirect'), cls=CommandGroupWithAlias, help="""The details of a HTTP Redirect configuration to allow redirecting HTTP traffic from a request domain to a new target.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def http_redirect_group():
    pass


waas_service_cli.waas_service_group.add_command(redirect_root_group)
redirect_root_group.add_command(http_redirect_group)


@http_redirect_group.command(name=cli_util.override('redirect.change_http_redirect_compartment.command_name', 'change-compartment'), help=u"""Moves HTTP Redirect into a different compartment. When provided, If-Match is checked against ETag values of the WAAS policy. \n[Command Reference](changeHttpRedirectCompartment)""")
@cli_util.option('--http-redirect-id', required=True, help=u"""The [OCID] of the HTTP Redirect.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_http_redirect_compartment(ctx, from_json, http_redirect_id, compartment_id, if_match):

    if isinstance(http_redirect_id, six.string_types) and len(http_redirect_id.strip()) == 0:
        raise click.UsageError('Parameter --http-redirect-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('waas', 'redirect', ctx)
    result = client.change_http_redirect_compartment(
        http_redirect_id=http_redirect_id,
        change_http_redirect_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@http_redirect_group.command(name=cli_util.override('redirect.create_http_redirect.command_name', 'create'), help=u"""Creates a new HTTP Redirect on the WAF edge. \n[Command Reference](createHttpRedirect)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the HTTP Redirects compartment.""")
@cli_util.option('--domain', required=True, help=u"""The domain from which traffic will be redirected.""")
@cli_util.option('--target', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The redirect target object including all the redirect data.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The user-friendly name of the HTTP Redirect. The name can be changed and does not need to be unique.""")
@cli_util.option('--response-code', type=click.INT, help=u"""The response code returned for the redirect to the client. For more information, see [RFC 7231].""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'target': {'module': 'waas', 'class': 'HttpRedirectTarget'}, 'freeform-tags': {'module': 'waas', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waas', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'target': {'module': 'waas', 'class': 'HttpRedirectTarget'}, 'freeform-tags': {'module': 'waas', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waas', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_http_redirect(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, domain, target, display_name, response_code, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['domain'] = domain
    _details['target'] = cli_util.parse_json_parameter("target", target)

    if display_name is not None:
        _details['displayName'] = display_name

    if response_code is not None:
        _details['responseCode'] = response_code

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('waas', 'redirect', ctx)
    result = client.create_http_redirect(
        create_http_redirect_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@http_redirect_group.command(name=cli_util.override('redirect.delete_http_redirect.command_name', 'delete'), help=u"""Deletes a redirect. \n[Command Reference](deleteHttpRedirect)""")
@cli_util.option('--http-redirect-id', required=True, help=u"""The [OCID] of the HTTP Redirect.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_http_redirect(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, http_redirect_id, if_match):

    if isinstance(http_redirect_id, six.string_types) and len(http_redirect_id.strip()) == 0:
        raise click.UsageError('Parameter --http-redirect-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'redirect', ctx)
    result = client.delete_http_redirect(
        http_redirect_id=http_redirect_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@http_redirect_group.command(name=cli_util.override('redirect.get_http_redirect.command_name', 'get'), help=u"""Gets the details of a HTTP Redirect. \n[Command Reference](getHttpRedirect)""")
@cli_util.option('--http-redirect-id', required=True, help=u"""The [OCID] of the HTTP Redirect.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'HttpRedirect'})
@cli_util.wrap_exceptions
def get_http_redirect(ctx, from_json, http_redirect_id):

    if isinstance(http_redirect_id, six.string_types) and len(http_redirect_id.strip()) == 0:
        raise click.UsageError('Parameter --http-redirect-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'redirect', ctx)
    result = client.get_http_redirect(
        http_redirect_id=http_redirect_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@http_redirect_group.command(name=cli_util.override('redirect.list_http_redirects.command_name', 'list'), help=u"""Gets a list of HTTP Redirects. \n[Command Reference](listHttpRedirects)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment. This number is generated when the compartment is created.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous paginated call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The value of the sorting direction of resources in a paginated 'List' call. If unspecified, defaults to `DESC`.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "domain", "target", "displayName"]), help=u"""The field to sort the results of the List query.""")
@cli_util.option('--id', multiple=True, help=u"""Filter redirects using a list of redirect OCIDs.""")
@cli_util.option('--display-name', multiple=True, help=u"""Filter redirects using a display name.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"]), multiple=True, help=u"""Filter redirects using a list of lifecycle states.""")
@cli_util.option('--time-created-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""A filter that matches redirects created on or after the specified date and time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-created-less-than', type=custom_types.CLI_DATETIME, help=u"""A filter that matches redirects created before the specified date-time. Default to 1 day before now.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'id': {'module': 'waas', 'class': 'list[string]'}, 'display-name': {'module': 'waas', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'waas', 'class': 'list[string]'}, 'display-name': {'module': 'waas', 'class': 'list[string]'}}, output_type={'module': 'waas', 'class': 'list[HttpRedirectSummary]'})
@cli_util.wrap_exceptions
def list_http_redirects(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_order, sort_by, id, display_name, lifecycle_state, time_created_greater_than_or_equal_to, time_created_less_than):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if id is not None and len(id) > 0:
        kwargs['id'] = id
    if display_name is not None and len(display_name) > 0:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None and len(lifecycle_state) > 0:
        kwargs['lifecycle_state'] = lifecycle_state
    if time_created_greater_than_or_equal_to is not None:
        kwargs['time_created_greater_than_or_equal_to'] = time_created_greater_than_or_equal_to
    if time_created_less_than is not None:
        kwargs['time_created_less_than'] = time_created_less_than
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'redirect', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_http_redirects,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_http_redirects,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_http_redirects(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@http_redirect_group.command(name=cli_util.override('redirect.update_http_redirect.command_name', 'update'), help=u"""Updates the details of a HTTP Redirect, including target and tags. Only the fields specified in the request body will be updated; all other properties will remain unchanged. \n[Command Reference](updateHttpRedirect)""")
@cli_util.option('--http-redirect-id', required=True, help=u"""The [OCID] of the HTTP Redirect.""")
@cli_util.option('--display-name', help=u"""The user-friendly name of the HTTP Redirect. The name can be changed and does not need to be unique.""")
@cli_util.option('--target', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The redirect target object including all the redirect data.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--response-code', type=click.INT, help=u"""The response code returned for the redirect to the client. For more information, see [RFC 7231].""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'target': {'module': 'waas', 'class': 'HttpRedirectTarget'}, 'freeform-tags': {'module': 'waas', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waas', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'target': {'module': 'waas', 'class': 'HttpRedirectTarget'}, 'freeform-tags': {'module': 'waas', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waas', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_http_redirect(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, http_redirect_id, display_name, target, response_code, freeform_tags, defined_tags, if_match):

    if isinstance(http_redirect_id, six.string_types) and len(http_redirect_id.strip()) == 0:
        raise click.UsageError('Parameter --http-redirect-id cannot be whitespace or empty string')
    if not force:
        if target or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to target and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if target is not None:
        _details['target'] = cli_util.parse_json_parameter("target", target)

    if response_code is not None:
        _details['responseCode'] = response_code

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('waas', 'redirect', ctx)
    result = client.update_http_redirect(
        http_redirect_id=http_redirect_id,
        update_http_redirect_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
