# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
import sys
from .generated import identity_cli
from . import cli_util
from . import json_skeleton_utils
from . import retry_utils

identity_cli.identity_group.add_command(identity_cli.availability_domain_group)
identity_cli.identity_group.add_command(identity_cli.compartment_group)
identity_cli.identity_group.add_command(identity_cli.customer_secret_key_group)
identity_cli.identity_group.add_command(identity_cli.group_group)
identity_cli.identity_group.add_command(identity_cli.policy_group)
identity_cli.identity_group.add_command(identity_cli.region_group)
identity_cli.identity_group.add_command(identity_cli.region_subscription_group)
identity_cli.identity_group.add_command(identity_cli.user_group)
identity_cli.user_group.add_command(identity_cli.api_key_group)
identity_cli.user_group.add_command(identity_cli.swift_password_group)
identity_cli.user_group.add_command(identity_cli.ui_password_group)

cli_util.get_param(identity_cli.create_policy, 'version_date').type = click.STRING

# help for oci iam policy create --statements
identity_policy_create_statements_example = """'["statement 1","statement 2"]'"""
identity_policy_create_statements_help = cli_util.GENERIC_JSON_FORMAT_HELP
cli_util.update_param_help(identity_cli.create_policy, 'statements', identity_policy_create_statements_help, append=True, example=identity_policy_create_statements_example)


@identity_cli.user_group.command(name='list-groups', help="""Lists the groups for which the specified user is a member. You must specify your tenancy's OCID as the value for the compartment ID (remember that the tenancy is simply the root compartment). See [Where to Get the Tenancy's OCID and User's OCID].""")
@click.option('--compartment-id', help="""The OCID of the compartment (remember that the tenancy is simply the root compartment). [required]""")
@click.option('--user-id', help="""The OCID of the user. [required]""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--limit', type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.""")
@click.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[Group]'})
@cli_util.wrap_exceptions
def list_groups_for_user(ctx, generate_full_command_json_input, generate_param_json_input, from_json, compartment_id, user_id, page, limit, all_pages, page_size):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    compartment_id = cli_util.coalesce_provided_and_default_value(ctx, 'compartment-id', compartment_id, True)
    user_id = cli_util.coalesce_provided_and_default_value(ctx, 'user-id', user_id, True)
    limit = cli_util.coalesce_provided_and_default_value(ctx, 'limit', limit, False)
    page = cli_util.coalesce_provided_and_default_value(ctx, 'page', page, False)
    all_pages = cli_util.coalesce_provided_and_default_value(ctx, 'all', all_pages, False)
    page_size = cli_util.coalesce_provided_and_default_value(ctx, 'page-size', page_size, False)
    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    client = cli_util.build_client('identity', ctx)
    args = {}

    args['user_id'] = user_id

    if page is not None:
        args['page'] = page

    if limit is not None:
        args['limit'] = limit

    if all_pages:
        if page_size:
            args['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_user_group_memberships,
            compartment_id=compartment_id,
            **args
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
            client.list_user_group_memberships,
            limit,
            page_size,
            compartment_id=compartment_id,
            **args
        )
    else:
        result = client.list_user_group_memberships(compartment_id=compartment_id, ** args)

    groups = []

    for membership in result.data:
        groups.append(client.get_group(membership.group_id).data)

    cli_util.render(groups, result.headers, ctx)


@identity_cli.group_group.command(name='list-users', help="""Lists the users in the specified group. You must specify your tenancy's OCID as the value for the compartment ID (remember that the tenancy is simply the root compartment). See [Where to Get the Tenancy's OCID and User's OCID].""")
@click.option('--compartment-id',
              help="""The OCID of the compartment (remember that the tenancy is simply the root compartment). [required]""")
@click.option('--group-id', help="""The OCID of the user. [required]""")
@click.option('--page',
              help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--limit', type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.""")
@click.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[User]'})
@cli_util.wrap_exceptions
def list_users_for_group(ctx, generate_full_command_json_input, generate_param_json_input, from_json, compartment_id, group_id, page, limit, all_pages, page_size):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    compartment_id = cli_util.coalesce_provided_and_default_value(ctx, 'compartment-id', compartment_id, True)
    group_id = cli_util.coalesce_provided_and_default_value(ctx, 'group-id', group_id, True)
    limit = cli_util.coalesce_provided_and_default_value(ctx, 'limit', limit, False)
    page = cli_util.coalesce_provided_and_default_value(ctx, 'page', page, False)
    all_pages = cli_util.coalesce_provided_and_default_value(ctx, 'all', all_pages, False)
    page_size = cli_util.coalesce_provided_and_default_value(ctx, 'page-size', page_size, False)
    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    client = cli_util.build_client('identity', ctx)
    args = {}

    args['group_id'] = group_id

    if page is not None:
        args['page'] = page

    if limit is not None:
        args['limit'] = limit

    if all_pages:
        if page_size:
            args['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_user_group_memberships,
            compartment_id=compartment_id,
            **args
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
            client.list_user_group_memberships,
            limit,
            page_size,
            compartment_id=compartment_id,
            **args
        )
    else:
        result = client.list_user_group_memberships(compartment_id=compartment_id, **args)

    users = []

    for membership in result.data:
        users.append(client.get_user(membership.user_id).data)

    cli_util.render(users, result.headers, ctx)


@identity_cli.group_group.command(name='add-user', help="""Adds the specified user to the specified group.""")
@click.option('--user-id', help="""The OCID of the user. [required]""")
@click.option('--group-id', help="""The OCID of the group. [required]""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'UserGroupMembership'})
@cli_util.wrap_exceptions
def add_user_to_group(ctx, generate_full_command_json_input, generate_param_json_input, from_json, user_id, group_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    user_id = cli_util.coalesce_provided_and_default_value(ctx, 'user-id', user_id, True)
    group_id = cli_util.coalesce_provided_and_default_value(ctx, 'group-id', group_id, True)

    client = cli_util.build_client('identity', ctx)
    result = client.add_user_to_group(add_user_to_group_details={"userId": user_id, "groupId": group_id})
    cli_util.render_response(result, ctx)


@identity_cli.group_group.command(name='remove-user', help="""Removes a user from a group.""")
@click.option('--compartment-id', help="""The OCID of the compartment (remember that the tenancy is simply the root compartment). [required]""")
@click.option('--user-id', help="""The OCID of the user. [required]""")
@click.option('--group-id', help="""The OCID of the group. [required]""")
@click.confirmation_option("--force", prompt="Are you sure you want to remove the given user from the given group?", help="Perform removal without prompting for confirmation.")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def remove_user_from_group(ctx, generate_full_command_json_input, generate_param_json_input, from_json, compartment_id, user_id, group_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    compartment_id = cli_util.coalesce_provided_and_default_value(ctx, 'compartment-id', compartment_id, True)
    user_id = cli_util.coalesce_provided_and_default_value(ctx, 'user-id', user_id, True)
    group_id = cli_util.coalesce_provided_and_default_value(ctx, 'group-id', group_id, True)

    client = cli_util.build_client('identity', ctx)
    memberships = client.list_user_group_memberships(compartment_id=compartment_id, user_id=user_id, group_id=group_id).data

    if memberships and len(memberships) == 1:
        cli_util.render_response(client.remove_user_from_group(user_group_membership_id=memberships[0].id), ctx)
    else:
        sys.exit('User {!r} is not a member of group {!r}'.format(user_id, group_id))


@identity_cli.policy_group.command(name='update', help="""Updates the specified policy. You can update the description or the policy statements themselves.

Policy changes take effect typically within 10 seconds.""")
@click.option('--policy-id', help="""The OCID of the policy. [required]""")
@click.option('--description', help="""The description you assign to the policy. Does not have to be unique, and it's changeable.""")
@click.option('--statements', help="""A JSON array of policy statements written in the policy language. See [How Policies Work] and [Common Policies]. Example: '["statement 1","statement 2"]' (The single quotes are required.)""")
@click.option('--version-date', help="""The version of the policy. If set to an empty string, when a request comes in for authorization, the policy will be evaluated according to the current behavior of the services at that moment. If set to a particular date (YYYY-MM-DD), the policy will be evaluated according to the behavior of the services on that date.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({'statements': {'module': 'identity', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={'statements': {'module': 'identity', 'class': 'list[string]'}}, output_type={'module': 'identity', 'class': 'Policy'})
@cli_util.wrap_exceptions
def update_policy(ctx, generate_full_command_json_input, generate_param_json_input, from_json, policy_id, description, statements, version_date, if_match, force):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    policy_id = cli_util.coalesce_provided_and_default_value(ctx, 'policy-id', policy_id, True)
    description = cli_util.coalesce_provided_and_default_value(ctx, 'description', description, False)
    statements = cli_util.coalesce_provided_and_default_value(ctx, 'statements', statements, False)
    version_date = cli_util.coalesce_provided_and_default_value(ctx, 'version-date', version_date, False)
    if_match = cli_util.coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)
    force = cli_util.coalesce_provided_and_default_value(ctx, 'force', force, False)

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
    cli_util.render_response(result, ctx)
