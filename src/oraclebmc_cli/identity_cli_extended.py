# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
import sys
from .generated import identity_cli
from . import cli_util

identity_cli.identity_group.add_command(identity_cli.availability_domain_group)
identity_cli.identity_group.add_command(identity_cli.compartment_group)
identity_cli.identity_group.add_command(identity_cli.group_group)
identity_cli.identity_group.add_command(identity_cli.policy_group)
identity_cli.identity_group.add_command(identity_cli.region_group)
identity_cli.identity_group.add_command(identity_cli.region_subscription_group)
identity_cli.identity_group.add_command(identity_cli.user_group)
identity_cli.user_group.add_command(identity_cli.api_key_group)
identity_cli.user_group.add_command(identity_cli.swift_password_group)
identity_cli.user_group.add_command(identity_cli.ui_password_group)


# help for bmcs iam policy create --statements
identity_policy_create_statements_example = """'["statement 1","statement 2"]'"""
identity_policy_create_statements_help = cli_util.GENERIC_JSON_FORMAT_HELP
cli_util.update_param_help(identity_cli.create_policy, 'statements', identity_policy_create_statements_help, append=True, example=identity_policy_create_statements_example)


@identity_cli.user_group.command(name='list-groups', help="""Lists the groups for which the specified user is a member. You must specify your tenancy's OCID as the value for the compartment ID (remember that the tenancy is simply the root compartment). See [Where to Get the Tenancy's OCID and User's OCID].""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment (remember that the tenancy is simply the root compartment).""")
@click.option('--user-id', required=True, help="""The OCID of the user.""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--limit', help="""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_groups_for_user(ctx, compartment_id, user_id, page, limit):
    client = cli_util.build_client('identity', ctx)
    args = {}

    args['user_id'] = user_id

    if page is not None:
        args['page'] = page

    if limit is not None:
        args['limit'] = limit

    result = client.list_user_group_memberships(compartment_id=compartment_id, ** args)

    groups = []

    for membership in result.data:
        groups.append(client.get_group(membership.group_id).data)

    cli_util.render(groups, result.headers)


@identity_cli.group_group.command(name='list-users', help="""Lists the users in the specified group. You must specify your tenancy's OCID as the value for the compartment ID (remember that the tenancy is simply the root compartment). See [Where to Get the Tenancy's OCID and User's OCID].""")
@click.option('--compartment-id', required=True,
              help="""The OCID of the compartment (remember that the tenancy is simply the root compartment).""")
@click.option('--group-id', required=True, help="""The OCID of the user.""")
@click.option('--page',
              help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--limit', help="""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_users_for_group(ctx, compartment_id, group_id, page, limit):
    client = cli_util.build_client('identity', ctx)
    args = {}

    args['group_id'] = group_id

    if page is not None:
        args['page'] = page

    if limit is not None:
        args['limit'] = limit

    result = client.list_user_group_memberships(compartment_id=compartment_id, **args)

    users = []

    for membership in result.data:
        users.append(client.get_user(membership.user_id).data)

    cli_util.render(users, result.headers)


@identity_cli.group_group.command(name='add-user', help="""Adds the specified user to the specified group.""")
@click.option('--user-id', required=True, help="""The OCID of the user.""")
@click.option('--group-id', required=True, help="""The OCID of the group.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def add_user_to_group(ctx, user_id, group_id):
    client = cli_util.build_client('identity', ctx)
    result = client.add_user_to_group(add_user_to_group_details={"userId": user_id, "groupId": group_id})
    cli_util.render_response(result)


@identity_cli.group_group.command(name='remove-user', help="""Removes a user from a group.""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment (remember that the tenancy is simply the root compartment).""")
@click.option('--user-id', required=True, help="""The OCID of the user.""")
@click.option('--group-id', required=True, help="""The OCID of the group.""")
@click.confirmation_option("--force", prompt="Are you sure you want to remove the given user from the given group?", help="Perform removal without prompting for confirmation.")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def remove_user_from_group(ctx, compartment_id, user_id, group_id):
    client = cli_util.build_client('identity', ctx)
    memberships = client.list_user_group_memberships(compartment_id=compartment_id, user_id=user_id, group_id=group_id).data

    if memberships and len(memberships) == 1:
        cli_util.render_response(client.remove_user_from_group(user_group_membership_id=memberships[0].id))
    else:
        sys.exit('User {!r} is not a member of group {!r}'.format(user_id, group_id))


@identity_cli.policy_group.command(name='update', help="""Updates the specified policy. You can update the description or the policy statements themselves.

Policy changes take effect typically within 10 seconds.""")
@click.option('--policy-id', required=True, help="""The OCID of the policy.""")
@click.option('--description', help="""The description you assign to the policy. Does not have to be unique, and it's changeable.""")
@click.option('--statements', help="""A JSON array of policy statements written in the policy language. See [How Policies Work] and [Common Policies]. Example: '["statement 1","statement 2"]' (The single quotes are required.)""")
@click.option('--version-date', help="""The version of the policy. If set to an empty string, when a request comes in for authorization, the policy will be evaluated according to the current behavior of the services at that moment. If set to a particular date (YYYY-MM-DD), the policy will be evaluated according to the behavior of the services on that date.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def update_policy(ctx, policy_id, description, statements, version_date, if_match, force):
    client = cli_util.build_client('identity', ctx)
    if statements or version_date:
        if statements is None or version_date is None:
            sys.exit('If updating either statements or version date, both parameters must be specified.')

        if not force:
            result = client.get_policy(policy_id=policy_id)
            etag = result.headers['etag']

            if (if_match and etag != if_match):
                sys.exit('If-match {!r} does not match the current etag, {!r}.'.format(if_match, result.headers['etag']))

            if_match = etag

            existing_statements = cli_util.formatted_flat_dict(result.data.statements)
            if not click.confirm("WARNING: The value passed to statements will overwrite all existing statements for this policy. The existing statements are:\n" + existing_statements + "\nAre you sure you want to continue?"):
                ctx.abort()

    args = {}

    if if_match is not None:
        args['if_match'] = if_match

    details = {}

    if description:
        details['description'] = description
    if statements:
        details['statements'] = cli_util.parse_json_parameter("statements", statements)
    if version_date:
        if len(version_date) == 0:
            version_date = None
        details['versionDate'] = version_date

    result = client.update_policy(policy_id=policy_id, update_policy_details=details, ** args)
    cli_util.render_response(result)
