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
from services.limits.src.oci_cli_limits.generated import limits_service_cli


@click.command(cli_util.override('quotas.quotas_root_group.command_name', 'quotas'), cls=CommandGroupWithAlias, help=cli_util.override('quotas.quotas_root_group.help', """APIs that interact with the resource limits of a specific resource type"""), short_help=cli_util.override('quotas.quotas_root_group.short_help', """Service limits APIs"""))
@cli_util.help_option_group
def quotas_root_group():
    pass


@click.command(cli_util.override('quotas.quota_group.command_name', 'quota'), cls=CommandGroupWithAlias, help="""Quotas are applied on top of the service limits and inherited through the nested compartment hierarchy. They allow compartment admins to limit resource consumption and set boundaries around acceptable resource use. The word \"quota\" is used by people in different ways:   * An individual statement written in the declarative language   * A collection of statements in a single, named \"quota\" object (which has an Oracle Cloud ID (OCID) assigned to it)   * The overall body of quotas your organization uses to control access to resources""")
@cli_util.help_option_group
def quota_group():
    pass


limits_service_cli.limits_service_group.add_command(quotas_root_group)
quotas_root_group.add_command(quota_group)


@quota_group.command(name=cli_util.override('quotas.create_quota.command_name', 'create'), help=u"""Creates a new quota with the details supplied.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment containing the resource this quota applies to.""")
@cli_util.option('--description', required=True, help=u"""The description you assign to the quota.""")
@cli_util.option('--name', required=True, help=u"""The name you assign to the quota during creation. The name must be unique across all quotas in the tenancy and cannot be changed.""")
@cli_util.option('--statements', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of quota statements written in the declarative quota statement language.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'statements': {'module': 'limits', 'class': 'list[string]'}, 'freeform-tags': {'module': 'limits', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'limits', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'statements': {'module': 'limits', 'class': 'list[string]'}, 'freeform-tags': {'module': 'limits', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'limits', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'limits', 'class': 'Quota'})
@cli_util.wrap_exceptions
def create_quota(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, description, name, statements, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['description'] = description
    _details['name'] = name
    _details['statements'] = cli_util.parse_json_parameter("statements", statements)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('limits', 'quotas', ctx)
    result = client.create_quota(
        create_quota_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_quota') and callable(getattr(client, 'get_quota')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_quota(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@quota_group.command(name=cli_util.override('quotas.delete_quota.command_name', 'delete'), help=u"""Deletes the quota corresponding to the given OCID.""")
@cli_util.option('--quota-id', required=True, help=u"""The OCID of the quota.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_quota(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, quota_id, if_match):

    if isinstance(quota_id, six.string_types) and len(quota_id.strip()) == 0:
        raise click.UsageError('Parameter --quota-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('limits', 'quotas', ctx)
    result = client.delete_quota(
        quota_id=quota_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_quota') and callable(getattr(client, 'get_quota')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_quota(quota_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@quota_group.command(name=cli_util.override('quotas.get_quota.command_name', 'get'), help=u"""Gets the quota for the OCID specified.""")
@cli_util.option('--quota-id', required=True, help=u"""The OCID of the quota.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'limits', 'class': 'Quota'})
@cli_util.wrap_exceptions
def get_quota(ctx, from_json, quota_id):

    if isinstance(quota_id, six.string_types) and len(quota_id.strip()) == 0:
        raise click.UsageError('Parameter --quota-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('limits', 'quotas', ctx)
    result = client.get_quota(
        quota_id=quota_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@quota_group.command(name=cli_util.override('quotas.list_quotas.command_name', 'list'), help=u"""Lists all quotas on resources from the given compartment""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the parent compartment (remember that the tenancy is simply the root compartment).""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--name', help=u"""name""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), help=u"""Filters returned quotas based on whether the given state.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'. By default it will be ascending.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["NAME", "TIMECREATED"]), help=u"""The field to sort by. Only one sort order may be provided. Time created is default ordered as descending. Display name is default ordered as ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'limits', 'class': 'list[QuotaSummary]'})
@cli_util.wrap_exceptions
def list_quotas(ctx, from_json, all_pages, page_size, compartment_id, page, limit, name, lifecycle_state, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if name is not None:
        kwargs['name'] = name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('limits', 'quotas', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_quotas,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_quotas,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_quotas(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@quota_group.command(name=cli_util.override('quotas.update_quota.command_name', 'update'), help=u"""Updates the quota corresponding to given OCID with the details supplied.""")
@cli_util.option('--quota-id', required=True, help=u"""The OCID of the quota.""")
@cli_util.option('--description', help=u"""The description you assign to the quota.""")
@cli_util.option('--statements', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of quota statements written in the declarative quota statement language.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'statements': {'module': 'limits', 'class': 'list[string]'}, 'freeform-tags': {'module': 'limits', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'limits', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'statements': {'module': 'limits', 'class': 'list[string]'}, 'freeform-tags': {'module': 'limits', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'limits', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'limits', 'class': 'Quota'})
@cli_util.wrap_exceptions
def update_quota(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, quota_id, description, statements, freeform_tags, defined_tags, if_match):

    if isinstance(quota_id, six.string_types) and len(quota_id.strip()) == 0:
        raise click.UsageError('Parameter --quota-id cannot be whitespace or empty string')
    if not force:
        if statements or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to statements and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if statements is not None:
        _details['statements'] = cli_util.parse_json_parameter("statements", statements)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('limits', 'quotas', ctx)
    result = client.update_quota(
        quota_id=quota_id,
        update_quota_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_quota') and callable(getattr(client, 'get_quota')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_quota(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
