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
from services.tenant_manager_control_plane.src.oci_cli_tenant_manager_control_plane.generated import organizations_service_cli


@click.command(cli_util.override('organization.organization_root_group.command_name', 'organization'), cls=CommandGroupWithAlias, help=cli_util.override('organization.organization_root_group.help', """The Organizations API allows you to consolidate multiple OCI tenancies into an organization, and centrally manage your tenancies and its resources."""), short_help=cli_util.override('organization.organization_root_group.short_help', """Organizations API"""))
@cli_util.help_option_group
def organization_root_group():
    pass


@click.command(cli_util.override('organization.organization_tenancy_group.command_name', 'organization-tenancy'), cls=CommandGroupWithAlias, help="""The information about the OrganizationTenancy.""")
@cli_util.help_option_group
def organization_tenancy_group():
    pass


@click.command(cli_util.override('organization.organization_group.command_name', 'organization'), cls=CommandGroupWithAlias, help="""An organization entity.""")
@cli_util.help_option_group
def organization_group():
    pass


@click.command(cli_util.override('organization.child_tenancy_group.command_name', 'child-tenancy'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def child_tenancy_group():
    pass


organizations_service_cli.organizations_service_group.add_command(organization_root_group)
organization_root_group.add_command(organization_tenancy_group)
organization_root_group.add_command(organization_group)
organization_root_group.add_command(child_tenancy_group)


@organization_tenancy_group.command(name=cli_util.override('organization.approve_organization_tenancy_for_transfer.command_name', 'approve-organization-tenancy-for-transfer'), help=u"""Approve an organization's child tenancy for transfer. \n[Command Reference](approveOrganizationTenancyForTransfer)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--organization-tenancy-id', required=True, help=u"""OCID of the child tenancy.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'tenant_manager_control_plane', 'class': 'OrganizationTenancy'})
@cli_util.wrap_exceptions
def approve_organization_tenancy_for_transfer(ctx, from_json, compartment_id, organization_tenancy_id, if_match):

    if isinstance(organization_tenancy_id, six.string_types) and len(organization_tenancy_id.strip()) == 0:
        raise click.UsageError('Parameter --organization-tenancy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'organization', ctx)
    result = client.approve_organization_tenancy_for_transfer(
        compartment_id=compartment_id,
        organization_tenancy_id=organization_tenancy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@child_tenancy_group.command(name=cli_util.override('organization.create_child_tenancy.command_name', 'create'), help=u"""Creates a child tenancy asynchronously. \n[Command Reference](createChildTenancy)""")
@cli_util.option('--compartment-id', required=True, help=u"""The tenancy ID of the parent tenancy.""")
@cli_util.option('--tenancy-name', required=True, help=u"""The tenancy name to use for the child tenancy.""")
@cli_util.option('--home-region', required=True, help=u"""The home region to use for the child tenancy. This must be a region where the parent tenancy is subscribed.""")
@cli_util.option('--admin-email', required=True, help=u"""The email address of the administrator of the child tenancy.""")
@cli_util.option('--policy-name', help=u"""The name to use for the administrator policy in the child tenancy. Must contain only letters and underscores.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def create_child_tenancy(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, tenancy_name, home_region, admin_email, policy_name):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['tenancyName'] = tenancy_name
    _details['homeRegion'] = home_region
    _details['adminEmail'] = admin_email

    if policy_name is not None:
        _details['policyName'] = policy_name

    client = cli_util.build_client('tenant_manager_control_plane', 'organization', ctx)
    result = client.create_child_tenancy(
        create_child_tenancy_details=_details,
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


@organization_tenancy_group.command(name=cli_util.override('organization.delete_organization_tenancy.command_name', 'delete'), help=u"""If certain validations are successful, initiate tenancy termination. \n[Command Reference](deleteOrganizationTenancy)""")
@cli_util.option('--organization-tenancy-id', required=True, help=u"""OCID of the tenancy to be terminated.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_organization_tenancy(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, organization_tenancy_id, if_match):

    if isinstance(organization_tenancy_id, six.string_types) and len(organization_tenancy_id.strip()) == 0:
        raise click.UsageError('Parameter --organization-tenancy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'organization', ctx)
    result = client.delete_organization_tenancy(
        organization_tenancy_id=organization_tenancy_id,
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


@organization_group.command(name=cli_util.override('organization.get_organization.command_name', 'get'), help=u"""Gets information about the organization. \n[Command Reference](getOrganization)""")
@cli_util.option('--organization-id', required=True, help=u"""OCID of the organization to retrieve.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'tenant_manager_control_plane', 'class': 'Organization'})
@cli_util.wrap_exceptions
def get_organization(ctx, from_json, organization_id):

    if isinstance(organization_id, six.string_types) and len(organization_id.strip()) == 0:
        raise click.UsageError('Parameter --organization-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'organization', ctx)
    result = client.get_organization(
        organization_id=organization_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@organization_tenancy_group.command(name=cli_util.override('organization.get_organization_tenancy.command_name', 'get'), help=u"""Gets information about the organization's tenancy. \n[Command Reference](getOrganizationTenancy)""")
@cli_util.option('--organization-id', required=True, help=u"""OCID of the organization.""")
@cli_util.option('--tenancy-id', required=True, help=u"""OCID of the tenancy to retrieve.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'tenant_manager_control_plane', 'class': 'OrganizationTenancy'})
@cli_util.wrap_exceptions
def get_organization_tenancy(ctx, from_json, organization_id, tenancy_id):

    if isinstance(organization_id, six.string_types) and len(organization_id.strip()) == 0:
        raise click.UsageError('Parameter --organization-id cannot be whitespace or empty string')

    if isinstance(tenancy_id, six.string_types) and len(tenancy_id.strip()) == 0:
        raise click.UsageError('Parameter --tenancy-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'organization', ctx)
    result = client.get_organization_tenancy(
        organization_id=organization_id,
        tenancy_id=tenancy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@organization_group.command(name=cli_util.override('organization.list_organization_tenancies.command_name', 'list-organization-tenancies'), help=u"""Gets a list of tenancies in the organization. \n[Command Reference](listOrganizationTenancies)""")
@cli_util.option('--organization-id', required=True, help=u"""OCID of the organization.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'tenant_manager_control_plane', 'class': 'OrganizationTenancyCollection'})
@cli_util.wrap_exceptions
def list_organization_tenancies(ctx, from_json, all_pages, page_size, organization_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(organization_id, six.string_types) and len(organization_id.strip()) == 0:
        raise click.UsageError('Parameter --organization-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'organization', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_organization_tenancies,
            organization_id=organization_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_organization_tenancies,
            limit,
            page_size,
            organization_id=organization_id,
            **kwargs
        )
    else:
        result = client.list_organization_tenancies(
            organization_id=organization_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@organization_group.command(name=cli_util.override('organization.list_organizations.command_name', 'list'), help=u"""Lists organizations associated with the caller. \n[Command Reference](listOrganizations)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'tenant_manager_control_plane', 'class': 'OrganizationCollection'})
@cli_util.wrap_exceptions
def list_organizations(ctx, from_json, all_pages, page_size, compartment_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'organization', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_organizations,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_organizations,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_organizations(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@organization_tenancy_group.command(name=cli_util.override('organization.restore_organization_tenancy.command_name', 'restore'), help=u"""An asynchronous API to restore tenancy. \n[Command Reference](restoreOrganizationTenancy)""")
@cli_util.option('--organization-tenancy-id', required=True, help=u"""OCID of the tenancy to be restored.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def restore_organization_tenancy(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, organization_tenancy_id, if_match):

    if isinstance(organization_tenancy_id, six.string_types) and len(organization_tenancy_id.strip()) == 0:
        raise click.UsageError('Parameter --organization-tenancy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'organization', ctx)
    result = client.restore_organization_tenancy(
        organization_tenancy_id=organization_tenancy_id,
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


@organization_tenancy_group.command(name=cli_util.override('organization.unapprove_organization_tenancy_for_transfer.command_name', 'unapprove-organization-tenancy-for-transfer'), help=u"""Cancel an organization's child tenancy for transfer. \n[Command Reference](unapproveOrganizationTenancyForTransfer)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--organization-tenancy-id', required=True, help=u"""OCID of the child tenancy.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'tenant_manager_control_plane', 'class': 'OrganizationTenancy'})
@cli_util.wrap_exceptions
def unapprove_organization_tenancy_for_transfer(ctx, from_json, compartment_id, organization_tenancy_id, if_match):

    if isinstance(organization_tenancy_id, six.string_types) and len(organization_tenancy_id.strip()) == 0:
        raise click.UsageError('Parameter --organization-tenancy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'organization', ctx)
    result = client.unapprove_organization_tenancy_for_transfer(
        compartment_id=compartment_id,
        organization_tenancy_id=organization_tenancy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@organization_group.command(name=cli_util.override('organization.update_organization.command_name', 'update'), help=u"""Assign the default subscription to the organization. \n[Command Reference](updateOrganization)""")
@cli_util.option('--organization-id', required=True, help=u"""OCID of the organization.""")
@cli_util.option('--default-ucm-subscription-id', required=True, help=u"""OCID of the default UCM subscription. Any tenancy joining the organization will automatically get assigned this subscription if a subscription if not explictly assigned.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_organization(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, organization_id, default_ucm_subscription_id, if_match):

    if isinstance(organization_id, six.string_types) and len(organization_id.strip()) == 0:
        raise click.UsageError('Parameter --organization-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['defaultUcmSubscriptionId'] = default_ucm_subscription_id

    client = cli_util.build_client('tenant_manager_control_plane', 'organization', ctx)
    result = client.update_organization(
        organization_id=organization_id,
        update_organization_details=_details,
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
