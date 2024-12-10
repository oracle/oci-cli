# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import six
import sys
from services.identity.src.oci_cli_identity.generated import identity_cli
from oci_cli import cli_exceptions
from oci_cli import custom_types
from oci_cli import json_skeleton_utils
from oci_cli import cli_util
from oci_cli.cli_util import get_tenancy_from_config
import oci_cli.cli_root as cli_root
import oci_cli.final_command_processor as final_command_processor
from oci_cli.aliasing import CommandGroupWithAlias
import oci
import time
import os
from pathlib import Path
from oci_cli import cli_setup
import datetime
DEFAULT_DIRECTORY = os.path.join(os.path.expanduser('~'), '.oci')


def get_iam_commands_that_use_tenancy_defaults():
    iam_tenancy_defaults = {
        'availability-domain': ['list'],
        'compartment': ['list'],
        'dynamic-group': ['create', 'list'],
        'group': ['add-user', 'create', 'list', 'list-users', 'remove-user'],
        'user': ['create', 'list', 'list-groups'],
        'region-subscription': ['list']
    }
    return iam_tenancy_defaults


# Many iam commands accept the compartment-id or tenany-id as a parameter.
# In most cases, except policy, we can use the tenancy from the config file as a default for the tenancy-id or
# root compartment-id.
def cli_util_func(ctx, param_name):
    iam_tenancy_defaults = get_iam_commands_that_use_tenancy_defaults()
    if ctx.parent.command.name in iam_tenancy_defaults.keys():
        if ctx.command.name in iam_tenancy_defaults[ctx.parent.command.name]:
            if param_name in ['compartment-id', 'tenancy-id']:
                value = get_tenancy_from_config(ctx)
                return value


# Many iam commands accept the compartment-id or tenany-id as a parameter.
# In most cases, except policy, we can use the tenancy from the config file as a default for the tenancy-id or
# root compartment-id.
def set_iam_default_tenancy_help():
    iam_tenancy_defaults = get_iam_commands_that_use_tenancy_defaults()

    if not cli_root.cli.commands.get('iam', None):
        return
    iam_command = cli_root.cli.commands.get('iam')
    for _, entitycommand in six.iteritems(iam_command.commands):
        if entitycommand.name in iam_tenancy_defaults.keys():
            for _, subcommand in six.iteritems(entitycommand.commands):
                for param in subcommand.params:
                    if subcommand.name in iam_tenancy_defaults[entitycommand.name]:
                        if param.name == 'compartment_id' or param.name == 'tenancy_id':
                            if param.help.endswith(' [required]'):
                                # Remove ' [required]'
                                param.help = ' '.join(param.help.split(' ')[:-1])
                                # Add help text
                                param.help = param.help + \
                                    " If not provided, this parameter will use the " + \
                                    "tenancy's OCID (root compartment's OCID) from the config file."


cli_util.SERVICE_FUNCTIONS_TO_EXECUTE['iam'] = cli_util_func
final_command_processor.SERVICE_FUNCTIONS_TO_EXECUTE.append(set_iam_default_tenancy_help)


identity_cli.iam_root_group.commands.pop(identity_cli.idp_group_mapping_group.name)
identity_cli.iam_root_group.commands.pop(identity_cli.user_group_membership_group.name)
identity_cli.iam_root_group.commands.pop(identity_cli.api_key_group.name)
identity_cli.iam_root_group.commands.pop(identity_cli.swift_password_group.name)
identity_cli.iam_root_group.commands.pop(identity_cli.ui_password_group.name)

identity_cli.user_group.add_command(identity_cli.api_key_group)
identity_cli.user_group.add_command(identity_cli.swift_password_group)
identity_cli.user_group.add_command(identity_cli.ui_password_group)

identity_cli.tag_group.commands.pop(identity_cli.update_tag.name)

identity_cli.tag_namespace_group.commands.pop(identity_cli.update_tag_namespace.name)

identity_cli.api_key_group.commands.pop(identity_cli.upload_api_key.name)
identity_cli.tag_group.commands.pop(identity_cli.create_tag_default_tag_definition_validator.name)
identity_cli.tag_group.commands.pop(identity_cli.create_tag_enum_tag_definition_validator.name)
identity_cli.tag_group.commands.pop(identity_cli.update_tag_default_tag_definition_validator.name)
identity_cli.tag_group.commands.pop(identity_cli.update_tag_enum_tag_definition_validator.name)

# Disable subclass commands
identity_cli.identity_provider_group.commands.pop(identity_cli.create_identity_provider_create_saml2_identity_provider_details.name)
identity_cli.identity_provider_group.commands.pop(identity_cli.update_identity_provider_update_saml2_identity_provider_details.name)

cli_util.get_param(identity_cli.create_policy, 'version_date').type = click.STRING

# help for oci iam policy create --statements
identity_policy_create_statements_example = """'["statement 1","statement 2"]'"""
identity_policy_create_statements_help = cli_util.GENERIC_JSON_FORMAT_HELP
cli_util.update_param_help(identity_cli.create_policy, 'statements', identity_policy_create_statements_help, append=True, example=identity_policy_create_statements_example)

# revised short help for tagging operations
identity_cli.create_tag.short_help = 'Create new tag in a given tagNamespace'
identity_cli.get_tag.short_help = 'Gets the specified tag''s information'
identity_cli.list_tags.short_help = 'List tags in a given tagNamespace'
identity_cli.create_tag_namespace.short_help = 'Create new tagNamespace in a compartment'
identity_cli.get_tag_namespace.short_help = 'Get a tagNamespace''s information'
identity_cli.list_tag_namespaces.short_help = 'List the tagNamespaces in a compartment'


# Rename oci iam bulk-action-resource-type-collection list-bulk-action-resource-types -> oci iam bulk-action-resource-type-collection list
cli_util.rename_command(identity_cli, identity_cli.bulk_action_resource_type_collection_group, identity_cli.list_bulk_action_resource_types, "list")


# Rename oci iam bulk-edit-tags-resource-type-collection list-bulk-edit-tags-resource-types -> oci iam bulk-edit-tags-resource-type-collection list
cli_util.rename_command(identity_cli, identity_cli.bulk_edit_tags_resource_type_collection_group, identity_cli.list_bulk_edit_tags_resource_types, "list")

# we are moving "oci iam bulk-edit-tags-resource-type-collection list" to "oci iam tag bulk-edit-tags-resource-type-collection list"
identity_cli.iam_root_group.commands.pop(identity_cli.bulk_edit_tags_resource_type_collection_group.name)

identity_cli.tag_group.add_command(identity_cli.bulk_edit_tags_resource_type_collection_group)

# Rename oci iam tag bulk-edit-tags-resource-type-collection list -> oci iam tag bulk-edit-tags-resource-type list
cli_util.rename_command(identity_cli, identity_cli.tag_group, identity_cli.bulk_edit_tags_resource_type_collection_group, "bulk-edit-tags-resource-type")


@identity_cli.user_group.command(name='list-groups', help="""Lists the groups for which the specified user is a member. You must specify your tenancy's OCID as the value for the compartment ID (remember that the tenancy is simply the root compartment). See [Where to Get the Tenancy's OCID and User's OCID].""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment (remember that the tenancy is simply the root compartment).""")
@cli_util.option('--user-id', required=True, help="""The OCID of the user.""")
@cli_util.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[Group]'})
@cli_util.wrap_exceptions
def list_groups_for_user(ctx, from_json, compartment_id, user_id, page, limit, all_pages, page_size):
    cli_util.load_context_obj_values_from_defaults(ctx)
    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    client = cli_util.build_client('identity', 'identity', ctx)
    args = {}

    args['user_id'] = user_id

    if page is not None:
        args['page'] = page

    if limit is not None:
        args['limit'] = limit

    if all_pages:
        if page_size:
            args['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_user_group_memberships,
            compartment_id=compartment_id,
            **args
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
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
@cli_util.option('--compartment-id', required=True,
                 help="""The OCID of the compartment (remember that the tenancy is simply the root compartment).""")
@cli_util.option('--group-id', required=True, help="""The OCID of the group.""")
@cli_util.option('--page',
                 help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[User]'})
@cli_util.wrap_exceptions
def list_users_for_group(ctx, from_json, compartment_id, group_id, page, limit, all_pages, page_size):
    cli_util.load_context_obj_values_from_defaults(ctx)
    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    client = cli_util.build_client('identity', 'identity', ctx)
    args = {}

    args['group_id'] = group_id

    if page is not None:
        args['page'] = page

    if limit is not None:
        args['limit'] = limit

    if all_pages:
        if page_size:
            args['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_user_group_memberships,
            compartment_id=compartment_id,
            **args
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
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
@cli_util.option('--user-id', required=True, help="""The OCID of the user.""")
@cli_util.option('--group-id', required=True, help="""The OCID of the group.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'UserGroupMembership'})
@cli_util.wrap_exceptions
def add_user_to_group(ctx, from_json, user_id, group_id):
    cli_util.load_context_obj_values_from_defaults(ctx)
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.add_user_to_group(add_user_to_group_details={"userId": user_id, "groupId": group_id})
    cli_util.render_response(result, ctx)


@identity_cli.group_group.command(name='remove-user', help="""Removes a user from a group.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment (remember that the tenancy is simply the root compartment).""")
@cli_util.option('--user-id', required=True, help="""The OCID of the user.""")
@cli_util.option('--group-id', required=True, help="""The OCID of the group.""")
@cli_util.option("--force", is_flag=True, help="Perform removal without prompting for confirmation.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def remove_user_from_group(ctx, from_json, compartment_id, user_id, group_id, force):
    cli_util.load_context_obj_values_from_defaults(ctx)

    if not force:
        if not click.confirm("Are you sure you want to remove the given user from the given group?"):
            ctx.abort()

    client = cli_util.build_client('identity', 'identity', ctx)
    memberships = client.list_user_group_memberships(compartment_id=compartment_id, user_id=user_id, group_id=group_id).data

    if memberships and len(memberships) == 1:
        cli_util.render_response(client.remove_user_from_group(user_group_membership_id=memberships[0].id), ctx)
    else:
        sys.exit('User {!r} is not a member of group {!r}'.format(user_id, group_id))


@identity_cli.policy_group.command(name='update', help="""Updates the specified policy. You can update the description or the policy statements themselves.

Policy changes take effect typically within 10 seconds.""")
@cli_util.option('--policy-id', required=True, help="""The OCID of the policy.""")
@cli_util.option('--description', help="""The description you assign to the policy. Does not have to be unique, and it's changeable.""")
@cli_util.option('--statements', help="""A JSON array of policy statements written in the policy language. See [How Policies Work] and [Common Policies]. Example: '["statement 1","statement 2"]' (The single quotes are required.)""")
@cli_util.option('--version-date', help="""The version of the policy. If set to an empty string, when a request comes in for authorization, the policy will be evaluated according to the current behavior of the services at that moment. If set to a particular date (YYYY-MM-DD), the policy will be evaluated according to the behavior of the services on that date.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"foo-value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'statements': {'module': 'identity', 'class': 'list[string]'}, 'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'statements': {'module': 'identity', 'class': 'list[string]'}, 'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'identity', 'class': 'Policy'})
@cli_util.wrap_exceptions
def update_policy(ctx, from_json, policy_id, description, statements, version_date, if_match, force, defined_tags, freeform_tags):
    cli_util.load_context_obj_values_from_defaults(ctx)

    client = cli_util.build_client('identity', 'identity', ctx)
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

    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
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
    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)
    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    result = client.update_policy(policy_id=policy_id, update_policy_details=details, ** args)
    cli_util.render_response(result, ctx)


@cli_util.copy_params_from_generated_command(identity_cli.update_tag, params_to_exclude=['is_retired'])
@identity_cli.tag_group.command(name=cli_util.override('update_tag.command_name', 'update'), help="""Updates the the specified tag""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}, 'validator': {'module': 'identity', 'class': 'BaseTagDefinitionValidator'}}, output_type={'module': 'identity', 'class': 'Tag'})
@cli_util.wrap_exceptions
def update_tag_description(ctx, **kwargs):
    ctx.invoke(identity_cli.update_tag, **kwargs)


@identity_cli.tag_group.command(name='retire', short_help='Retire tag and related rules', help="""Retires a tag so that it cannot be used to tag resources. Retiring a tag will also retire the related rules. You can not create a tag with the same name as a retired tag. Tags must be unique within their tag namespace but can be repeated across namespaces. You cannot add a tag with the same name as a retired tag in the same tag namespace.""")
@cli_util.option('--tag-namespace-id', required=True, help="""The OCID of the tag namespace.""")
@cli_util.option('--tag-name', required=True, help="""The name of the tag.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'Tag'})
@cli_util.wrap_exceptions
def retire_tag(ctx, **kwargs):
    tag_namespace_id = kwargs['tag_namespace_id']
    tag_name = kwargs['tag_name']

    if isinstance(tag_namespace_id, six.string_types) and len(tag_namespace_id.strip()) == 0:
        raise click.UsageError('Parameter --tag-namespace-id cannot be whitespace or empty string')

    if isinstance(tag_name, six.string_types) and len(tag_name.strip()) == 0:
        raise click.UsageError('Parameter --tag-name cannot be whitespace or empty string')

    service_kwargs = {}
    details = {'isRetired': True}

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.update_tag(
        tag_namespace_id=tag_namespace_id,
        tag_name=tag_name,
        update_tag_details=details,
        **service_kwargs
    )
    cli_util.render_response(result, ctx)


@identity_cli.tag_group.command(name='reactivate', help="""Reactivate tag so it can be used""")
@cli_util.option('--tag-namespace-id', required=True, help="""The OCID of the tag namespace.""")
@cli_util.option('--tag-name', required=True, help="""The name of the tag.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'Tag'})
@cli_util.wrap_exceptions
def reactivate_tag(ctx, **kwargs):
    tag_namespace_id = kwargs['tag_namespace_id']
    tag_name = kwargs['tag_name']

    if isinstance(tag_namespace_id, six.string_types) and len(tag_namespace_id.strip()) == 0:
        raise click.UsageError('Parameter --tag-namespace-id cannot be whitespace or empty string')

    if isinstance(tag_name, six.string_types) and len(tag_name.strip()) == 0:
        raise click.UsageError('Parameter --tag-name cannot be whitespace or empty string')

    service_kwargs = {}
    details = {'isRetired': False}

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.update_tag(
        tag_namespace_id=tag_namespace_id,
        tag_name=tag_name,
        update_tag_details=details,
        **service_kwargs
    )
    cli_util.render_response(result, ctx)


@cli_util.copy_params_from_generated_command(identity_cli.update_tag_namespace, params_to_exclude=['is_retired'])
@identity_cli.tag_namespace_group.command(name=cli_util.override('update_tag_namespace.command_name', 'update'), help="""Updates the specified tagNamespace""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'identity', 'class': 'TagNamespace'})
@cli_util.wrap_exceptions
def update_tag_namespace_description(ctx, **kwargs):
    tag_namespace_id = kwargs['tag_namespace_id']
    description = kwargs.get('description')
    freeform_tags = kwargs.get('freeform_tags')
    defined_tags = kwargs.get('defined_tags')

    if isinstance(tag_namespace_id, six.string_types) and len(tag_namespace_id.strip()) == 0:
        raise click.UsageError('Parameter --tag-namespace-id cannot be whitespace or empty string')

    if not kwargs.get('force'):
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    service_kwargs = {}
    details = {}

    if description is not None:
        details['description'] = description

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.update_tag_namespace(
        tag_namespace_id=tag_namespace_id,
        update_tag_namespace_details=details,
        **service_kwargs
    )
    cli_util.render_response(result, ctx)


@identity_cli.tag_namespace_group.command(name='retire', short_help='Retire namespace and its tags and rules', help="""Retire the namespace, all the contained tags and the related rules. Reactivating a namespace  will not reactivate any tag definition that is retired when the namespace was retired. They will have to be individually reactivated *after* the namespace is reactivated. You can't add a namespace with the same name as a retired namespace in the same tenant.""")
@cli_util.option('--tag-namespace-id', required=True, help="""The OCID of the tag namespace.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'TagNamespace'})
@cli_util.wrap_exceptions
def retire_tag_namespace(ctx, **kwargs):
    tag_namespace_id = kwargs['tag_namespace_id']

    service_kwargs = {}
    details = {'isRetired': True}

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.update_tag_namespace(
        tag_namespace_id=tag_namespace_id,
        update_tag_namespace_details=details,
        **service_kwargs
    )
    cli_util.render_response(result, ctx)


@identity_cli.tag_namespace_group.command(name='reactivate', short_help='Reactivate namespace (only)', help="""Reactivates a namespace. Reactivating a namespace will not reactivate any tag definition that is retired when the namespace was retired. They will have to be individually reactivated *after* the namespace is reactivated.""")
@cli_util.option('--tag-namespace-id', required=True, help="""The OCID of the tag namespace.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'TagNamespace'})
@cli_util.wrap_exceptions
def reactivate_tag_namespace(ctx, **kwargs):
    tag_namespace_id = kwargs['tag_namespace_id']

    service_kwargs = {}
    details = {'isRetired': False}

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.update_tag_namespace(
        tag_namespace_id=tag_namespace_id,
        update_tag_namespace_details=details,
        **service_kwargs
    )
    cli_util.render_response(result, ctx)


@cli_util.copy_params_from_generated_command(identity_cli.list_compartments)
@identity_cli.compartment_group.command(name='list', help=identity_cli.list_compartments.help)
@cli_util.option('--include-root', 'with_root', is_flag=True, help="""Include root compartment""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[Compartment]'})
@cli_util.wrap_exceptions
def list_compartments(ctx, from_json, all_pages, page_size, compartment_id, page, limit, access_level, compartment_id_in_subtree, name, sort_by, sort_order, lifecycle_state, with_root):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if access_level is not None:
        kwargs['access_level'] = access_level
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    if name is not None:
        kwargs['name'] = name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('identity', 'identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_compartments,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_compartments,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_compartments(
            compartment_id=compartment_id,
            **kwargs
        )
    if with_root:
        tenancy_id = get_tenancy_from_config(ctx)
        tenancy_result = client.get_compartment(
            compartment_id=tenancy_id,
        )
        if limit is not None and result.data:
            # remove from list as root will be one compartment
            result.data.pop()

        result.data.insert(0, tenancy_result.data)

    cli_util.render_response(result, ctx)


@cli_util.copy_params_from_generated_command(identity_cli.create_compartment)
@identity_cli.compartment_group.command(name='create', help=identity_cli.create_compartment.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'identity', 'class': 'Compartment'})
@cli_util.wrap_exceptions
def create_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, name, description, freeform_tags, defined_tags):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['name'] = name
    _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.create_compartment(
        create_compartment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_compartment') and callable(getattr(client, 'get_compartment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                # There is a delay to get_compartment after create_compartment. Please see DEX-9701
                time.sleep(10)
                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_compartment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@cli_util.copy_params_from_generated_command(identity_cli.upload_api_key, params_to_exclude=['key'])
@identity_cli.api_key_group.command(name='upload', help=identity_cli.upload_api_key.help)
@cli_util.option('--key', help="""The public key.  Must be an RSA key in PEM format. Either this option or --key-file must be specified""")
@cli_util.option('--key-file', type=click.File('r'), help="""A file containing the public key.  Must be an RSA key in PEM format. Either this option or --key must be specified""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'ApiKey'})
@cli_util.wrap_exceptions
def upload_api_key(ctx, **kwargs):
    if not kwargs.get('key') and not kwargs.get('key_file'):
        raise cli_exceptions.RequiredValueNotInDefaultOrUserInputError('Must specify either --key or --key-file.')

    if kwargs.get('key') and kwargs.get('key_file'):
        raise cli_exceptions.RequiredValueNotInDefaultOrUserInputError('Cannot specify both --key and --key-file.')

    key_file = kwargs.get('key_file')
    if key_file:
        kwargs['key'] = key_file.read()

    # remove this since it wont be recognized by identity_cli.upload_api_key
    kwargs.pop('key_file')

    ctx.invoke(identity_cli.upload_api_key, **kwargs)


# move oauth2 commands under new subcommand (e.g. oci iam user create-o-auth-client-credential -> oci iam user oauth2-credential create)
@click.command('oauth2-credential', cls=CommandGroupWithAlias, help="""The *OAuth 2.0 Client Credentials* grant type is used by clients to obtain an access token outside of the context of a user.

For more information about OAuth 2.0 client credentials, see [User Credentials].""")
@cli_util.help_option_group
def oauth2_credential_group():
    pass


# create new sub command oauth2-credential
identity_cli.user_group.add_command(oauth2_credential_group)

# move create-o-auth-client-credential under oauth2-credential and rename to create
identity_cli.user_group.commands.pop(identity_cli.create_o_auth_client_credential.name)
oauth2_credential_group.add_command(identity_cli.create_o_auth_client_credential)
cli_util.rename_command(identity_cli, oauth2_credential_group, identity_cli.create_o_auth_client_credential, "create")

# move delete-o-auth-client-credential under oauth2-credential and rename to delete
identity_cli.user_group.commands.pop(identity_cli.delete_o_auth_client_credential.name)
oauth2_credential_group.add_command(identity_cli.delete_o_auth_client_credential)
cli_util.rename_command(identity_cli, oauth2_credential_group, identity_cli.delete_o_auth_client_credential, "delete")

# move list-o-auth-client-credential under oauth2-credential and rename to list
identity_cli.user_group.commands.pop(identity_cli.list_o_auth_client_credentials.name)
oauth2_credential_group.add_command(identity_cli.list_o_auth_client_credentials)
cli_util.rename_command(identity_cli, oauth2_credential_group, identity_cli.list_o_auth_client_credentials, "list")

# move update-o-auth-client-credential under oauth2-credential and rename to update
identity_cli.user_group.commands.pop(identity_cli.update_o_auth_client_credential.name)
oauth2_credential_group.add_command(identity_cli.update_o_auth_client_credential)
cli_util.rename_command(identity_cli, oauth2_credential_group, identity_cli.update_o_auth_client_credential, "update")


# oci iam domain list-allowed-domain-license-types -> oci iam domain list-license-types
cli_util.rename_command(identity_cli, identity_cli.domain_group, identity_cli.list_allowed_domain_license_types, "list-license-types")


@click.command('db-token', cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def db_token_group():
    pass


identity_cli.iam_root_group.add_command(db_token_group)


@db_token_group.command(name=cli_util.override('identity_data_plane.get_db_token.command_name', 'get'), help=u"""

This token is used to access Oracle cloud databases from database clients.  The database client or application requests the db-token using one of a number of principal tokens. Claims can be made as part of the db-token request and will be part of the db-token.

When running this command inside the Cloud Shell, it will by default use the delegation token for the IAM user to request the db-token. Outside of the cloud shell, this command will default to use the API-key in the default profile in the default OCI configuration.

In order to use a temporary security token, use --auth security-token. Instead of using the default (API-key), this will use the existing valid security token for the user.  If one doesn’t exist, OCI CLI will open a browser window to allow the user to authenticate with IAM. For more detail, please visit https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm""")
@cli_util.option('--scope', default='urn:oracle:db::id::*', help=u"""If a scope isn’t provided, the default will be the tenancy scope.  Adding scope allows you to constrain access by the db-token databases in one or more compartments.

Example scope values:

  urn:oracle:db::id::*

  urn:oracle:db::id::ocid1.tenancy.oc1..xxxx

  urn:oracle:db::id::ocid1.compartment.oc1..xxxx

  urn:oracle:db::id::ocid1.compartment.oc1..xxxx::ocid1.autonomousdatabase.oc1.phx.xxxx

  urn:oracle:db::path::mytenantname

  urn:oracle:db::path::mytenantname:mycompartmentname

  urn:oracle:db::path::mytenantname:mycompartmentname::ocid1.autonomousdatabase.oc1.phx.xxxx

""")
@cli_util.option('--db-token-location', default=os.path.join(DEFAULT_DIRECTORY, 'db-token'), help=u"""Provide the directory where you would like to store token and private/public key. Default is ~/.oci/db-token""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity_dataplane', 'class': 'SecurityToken'})
@cli_util.wrap_exceptions
def get_db_token(ctx, from_json, scope, db_token_location):

    if scope and "urn:oracle:db:" not in scope:
        click.echo("scope must be a db scope i.e --scope 'urn:oracle:db::id::*'")
        ctx.exit(1)

    kwargs = {}
    private_key = cli_util.generate_key()
    public_key = private_key.public_key()
    db_token_path = os.path.normpath(os.path.expanduser(db_token_location))
    Path(db_token_path).mkdir(parents=True, exist_ok=True)
    private_key_file_path = os.path.join(db_token_path, "oci_db_key.pem")
    public_key_file_path = os.path.join(db_token_path, "oci_db_key_public.pem")
    if not cli_setup.write_public_key_to_file(public_key_file_path, public_key, True, True):
        click.echo("Error: Unable to write public key at {}".format(public_key_file_path))
        ctx.exit(1)

    with open(public_key_file_path, mode='r') as public_file:
        public_key_from_file = public_file.read()
    _details = {
        'scope': scope,
        'publicKey': public_key_from_file}

    client = cli_util.build_client('identity_data_plane', 'dataplane', ctx)
    result = client.generate_scoped_access_token(
        generate_scoped_access_token_details=_details,
        **kwargs
    )
    response = cli_util.to_dict(result.data)

    # persist private key and result db_token
    if not cli_setup.write_private_key_to_file(private_key_file_path, private_key, '', True, True, add_private_key_label=False):
        click.echo("Error: Unable to write private key at: {}".format(private_key_file_path))
        ctx.exit(1)
    else:
        click.echo("Private key written at {}".format(private_key_file_path))
    db_token_path = os.path.join(db_token_path, "token")
    with open(db_token_path, "w") as f:
        f.write(response['token'])
        click.echo('db-token written at: {}'.format(db_token_path))
    cli_util.apply_user_only_access_permissions(db_token_path)
    with open(db_token_path, 'r') as db_token_file:
        token = db_token_file.read()

    db_token_container = oci.auth.security_token_container.SecurityTokenContainer(None, token)

    db_token_file = db_token_container.get_jwt()
    expiry_time = datetime.datetime.fromtimestamp(db_token_file['exp']).strftime("%Y-%m-%d %H:%M:%S")
    click.echo("db-token is valid until " + expiry_time, file=sys.stderr)
