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
from services.tenant_manager_control_plane.src.oci_cli_tenant_manager_control_plane.generated import organizations_service_cli


@click.command(cli_util.override('domain_governance.domain_governance_root_group.command_name', 'domain-governance'), cls=CommandGroupWithAlias, help=cli_util.override('domain_governance.domain_governance_root_group.help', """The Organizations API allows you to consolidate multiple OCI tenancies into an organization, and centrally manage your tenancies and its resources."""), short_help=cli_util.override('domain_governance.domain_governance_root_group.short_help', """Organizations API"""))
@cli_util.help_option_group
def domain_governance_root_group():
    pass


@click.command(cli_util.override('domain_governance.domain_governance_group.command_name', 'domain-governance'), cls=CommandGroupWithAlias, help="""The model for a domain governance entity.""")
@cli_util.help_option_group
def domain_governance_group():
    pass


organizations_service_cli.organizations_service_group.add_command(domain_governance_root_group)
domain_governance_root_group.add_command(domain_governance_group)


@domain_governance_group.command(name=cli_util.override('domain_governance.create_domain_governance.command_name', 'create'), help=u"""Adds domain governance to a claimed domain. \n[Command Reference](createDomainGovernance)""")
@cli_util.option('--compartment-id', required=True, help=u"""OCID of the tenancy.""")
@cli_util.option('--domain-id', required=True, help=u"""OCID of the domain.""")
@cli_util.option('--subscription-email', required=True, help=u"""The email to notify the user, and that the ONS subscription will be created with.""")
@cli_util.option('--ons-topic-id', required=True, help=u"""The ONS topic associated with this domain governance entity.""")
@cli_util.option('--ons-subscription-id', required=True, help=u"""The ONS subscription associated with this domain governance entity.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'tenant_manager_control_plane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'tenant_manager_control_plane', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'tenant_manager_control_plane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'tenant_manager_control_plane', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'tenant_manager_control_plane', 'class': 'DomainGovernance'})
@cli_util.wrap_exceptions
def create_domain_governance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, domain_id, subscription_email, ons_topic_id, ons_subscription_id, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['domainId'] = domain_id
    _details['subscriptionEmail'] = subscription_email
    _details['onsTopicId'] = ons_topic_id
    _details['onsSubscriptionId'] = ons_subscription_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('tenant_manager_control_plane', 'domain_governance', ctx)
    result = client.create_domain_governance(
        create_domain_governance_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_domain_governance') and callable(getattr(client, 'get_domain_governance')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_domain_governance(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@domain_governance_group.command(name=cli_util.override('domain_governance.delete_domain_governance.command_name', 'delete'), help=u"""Removes domain governance from a claimed domain. \n[Command Reference](deleteDomainGovernance)""")
@cli_util.option('--domain-governance-id', required=True, help=u"""The domain governance OCID.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_domain_governance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, domain_governance_id, if_match):

    if isinstance(domain_governance_id, six.string_types) and len(domain_governance_id.strip()) == 0:
        raise click.UsageError('Parameter --domain-governance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'domain_governance', ctx)
    result = client.delete_domain_governance(
        domain_governance_id=domain_governance_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_domain_governance') and callable(getattr(client, 'get_domain_governance')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_domain_governance(domain_governance_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@domain_governance_group.command(name=cli_util.override('domain_governance.get_domain_governance.command_name', 'get'), help=u"""Gets information about the domain governance entity. \n[Command Reference](getDomainGovernance)""")
@cli_util.option('--domain-governance-id', required=True, help=u"""The domain governance OCID.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'tenant_manager_control_plane', 'class': 'DomainGovernance'})
@cli_util.wrap_exceptions
def get_domain_governance(ctx, from_json, domain_governance_id):

    if isinstance(domain_governance_id, six.string_types) and len(domain_governance_id.strip()) == 0:
        raise click.UsageError('Parameter --domain-governance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'domain_governance', ctx)
    result = client.get_domain_governance(
        domain_governance_id=domain_governance_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@domain_governance_group.command(name=cli_util.override('domain_governance.list_domain_governances.command_name', 'list'), help=u"""Return a (paginated) list of domain governance entities. \n[Command Reference](listDomainGovernances)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--domain-id', help=u"""The domain OCID.""")
@cli_util.option('--domain-governance-id', help=u"""The domain governance OCID.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "FAILED", "TERMINATED"]), help=u"""The lifecycle state of the resource.""")
@cli_util.option('--name', help=u"""A filter to return only resources that exactly match the name given.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order can be provided. * The default order for timeCreated is descending. * The default order for displayName is ascending. * If no value is specified, timeCreated is the default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, whether 'asc' or 'desc'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'tenant_manager_control_plane', 'class': 'DomainGovernanceCollection'})
@cli_util.wrap_exceptions
def list_domain_governances(ctx, from_json, all_pages, page_size, compartment_id, domain_id, domain_governance_id, lifecycle_state, name, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if domain_id is not None:
        kwargs['domain_id'] = domain_id
    if domain_governance_id is not None:
        kwargs['domain_governance_id'] = domain_governance_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if name is not None:
        kwargs['name'] = name
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'domain_governance', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_domain_governances,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_domain_governances,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_domain_governances(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@domain_governance_group.command(name=cli_util.override('domain_governance.update_domain_governance.command_name', 'update'), help=u"""Updates the domain governance entity. \n[Command Reference](updateDomainGovernance)""")
@cli_util.option('--domain-governance-id', required=True, help=u"""The domain governance OCID.""")
@cli_util.option('--subscription-email', help=u"""The email to notify the user, and that the ONS subscription will be created with. The ONS subscription for the previous email will also be deleted.""")
@cli_util.option('--is-governance-enabled', type=click.BOOL, help=u"""Indicates whether governance is enabled for this domain.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'tenant_manager_control_plane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'tenant_manager_control_plane', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'tenant_manager_control_plane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'tenant_manager_control_plane', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'tenant_manager_control_plane', 'class': 'DomainGovernance'})
@cli_util.wrap_exceptions
def update_domain_governance(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, domain_governance_id, subscription_email, is_governance_enabled, freeform_tags, defined_tags, if_match):

    if isinstance(domain_governance_id, six.string_types) and len(domain_governance_id.strip()) == 0:
        raise click.UsageError('Parameter --domain-governance-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if subscription_email is not None:
        _details['subscriptionEmail'] = subscription_email

    if is_governance_enabled is not None:
        _details['isGovernanceEnabled'] = is_governance_enabled

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('tenant_manager_control_plane', 'domain_governance', ctx)
    result = client.update_domain_governance(
        domain_governance_id=domain_governance_id,
        update_domain_governance_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_domain_governance') and callable(getattr(client, 'get_domain_governance')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_domain_governance(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
