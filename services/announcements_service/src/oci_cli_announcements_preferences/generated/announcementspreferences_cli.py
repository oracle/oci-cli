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
from services.announcements_service.src.oci_cli_announcements_service.generated import announce_service_cli


@click.command(cli_util.override('announcements_preferences.announcements_preferences_root_group.command_name', 'announcements-preferences'), cls=CommandGroupWithAlias, help=cli_util.override('announcements_preferences.announcements_preferences_root_group.help', """Manage Oracle Cloud Infrastructure console announcements."""), short_help=cli_util.override('announcements_preferences.announcements_preferences_root_group.short_help', """Announcements Service API"""))
@cli_util.help_option_group
def announcements_preferences_root_group():
    pass


@click.command(cli_util.override('announcements_preferences.announcements_preferences_group.command_name', 'announcements-preferences'), cls=CommandGroupWithAlias, help="""The object for announcement email preferences.""")
@cli_util.help_option_group
def announcements_preferences_group():
    pass


announce_service_cli.announce_service_group.add_command(announcements_preferences_root_group)
announcements_preferences_root_group.add_command(announcements_preferences_group)


@announcements_preferences_group.command(name=cli_util.override('announcements_preferences.create_announcements_preference.command_name', 'create'), help=u"""Creates a request that specifies preferences for the tenancy regarding receiving announcements by email. \n[Command Reference](createAnnouncementsPreference)""")
@cli_util.option('--type', required=True, help=u"""The entity type, which specifies a model that either creates new announcement email preferences or updates existing preferences.""")
@cli_util.option('--preference-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["OPT_IN_TENANT_ANNOUNCEMENTS", "OPT_IN_TENANT_AND_INFORMATIONAL_ANNOUNCEMENTS", "OPT_OUT_ALL_ANNOUNCEMENTS"]), help=u"""The string representing the user's preference, whether to opt in to only required announcements, to opt in to all announcements, including informational announcements, or to opt out of all announcements.""")
@cli_util.option('--is-unsubscribed', type=click.BOOL, help=u"""A Boolean value to indicate whether the specified compartment chooses to not to receive informational announcements by email. (Manage preferences for receiving announcements by email by specifying the `preferenceType` attribute instead.)""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment for which you want to manage announcement email preferences. (Specify the tenancy by providing the root compartment OCID.)""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'announcements_service', 'class': 'AnnouncementsPreferencesSummary'})
@cli_util.wrap_exceptions
def create_announcements_preference(ctx, from_json, type, preference_type, is_unsubscribed, compartment_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['type'] = type
    _details['preferenceType'] = preference_type

    if is_unsubscribed is not None:
        _details['isUnsubscribed'] = is_unsubscribed

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    _details['type'] = 'CreateAnnouncementsPreferencesDetails'

    client = cli_util.build_client('announcements_service', 'announcements_preferences', ctx)
    result = client.create_announcements_preference(
        announcements_preference_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@announcements_preferences_group.command(name=cli_util.override('announcements_preferences.get_announcements_preference.command_name', 'get'), help=u"""Gets the current preferences of the tenancy regarding receiving announcements by email. \n[Command Reference](getAnnouncementsPreference)""")
@cli_util.option('--preference-id', required=True, help=u"""The ID of the preference.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'announcements_service', 'class': 'AnnouncementsPreferences'})
@cli_util.wrap_exceptions
def get_announcements_preference(ctx, from_json, preference_id):

    if isinstance(preference_id, six.string_types) and len(preference_id.strip()) == 0:
        raise click.UsageError('Parameter --preference-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('announcements_service', 'announcements_preferences', ctx)
    result = client.get_announcements_preference(
        preference_id=preference_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@announcements_preferences_group.command(name=cli_util.override('announcements_preferences.list_announcements_preferences.command_name', 'list'), help=u"""Gets the current preferences of the tenancy regarding receiving announcements by email. \n[Command Reference](listAnnouncementsPreferences)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment. Because announcements are specific to a tenancy, this is the OCID of the root compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'announcements_service', 'class': 'list[AnnouncementsPreferencesSummary]'})
@cli_util.wrap_exceptions
def list_announcements_preferences(ctx, from_json, all_pages, page_size, compartment_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('announcements_service', 'announcements_preferences', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_announcements_preferences,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_announcements_preferences,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_announcements_preferences(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@announcements_preferences_group.command(name=cli_util.override('announcements_preferences.update_announcements_preference.command_name', 'update'), help=u"""Updates the preferences of the tenancy regarding receiving announcements by email. \n[Command Reference](updateAnnouncementsPreference)""")
@cli_util.option('--preference-id', required=True, help=u"""The ID of the preference.""")
@cli_util.option('--type', required=True, help=u"""The entity type, which specifies a model that either creates new announcement email preferences or updates existing preferences.""")
@cli_util.option('--preference-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["OPT_IN_TENANT_ANNOUNCEMENTS", "OPT_IN_TENANT_AND_INFORMATIONAL_ANNOUNCEMENTS", "OPT_OUT_ALL_ANNOUNCEMENTS"]), help=u"""The string representing the user's preference, whether to opt in to only required announcements, to opt in to all announcements, including informational announcements, or to opt out of all announcements.""")
@cli_util.option('--is-unsubscribed', type=click.BOOL, help=u"""A Boolean value to indicate whether the specified compartment chooses to not to receive informational announcements by email. (Manage preferences for receiving announcements by email by specifying the `preferenceType` attribute instead.)""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment for which you want to manage announcement email preferences. (Specify the tenancy by providing the root compartment OCID.)""")
@cli_util.option('--if-match', help=u"""The locking version, used for optimistic concurrency control.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'announcements_service', 'class': 'AnnouncementsPreferencesSummary'})
@cli_util.wrap_exceptions
def update_announcements_preference(ctx, from_json, preference_id, type, preference_type, is_unsubscribed, compartment_id, if_match):

    if isinstance(preference_id, six.string_types) and len(preference_id.strip()) == 0:
        raise click.UsageError('Parameter --preference-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['type'] = type
    _details['preferenceType'] = preference_type

    if is_unsubscribed is not None:
        _details['isUnsubscribed'] = is_unsubscribed

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    _details['type'] = 'UpdateAnnouncementsPreferencesDetails'

    client = cli_util.build_client('announcements_service', 'announcements_preferences', ctx)
    result = client.update_announcements_preference(
        preference_id=preference_id,
        announcements_preference_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
