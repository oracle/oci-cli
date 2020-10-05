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


@cli.command(cli_util.override('management_dashboard.management_dashboard_root_group.command_name', 'management-dashboard'), cls=CommandGroupWithAlias, help=cli_util.override('management_dashboard.management_dashboard_root_group.help', """Management Dashboard micro-service provides a set of CRUD, import, export, and compartment related APIs (such as change compartment)   to support dashboard and saved search metadata preservation.  These APIs are mainly for client UIs, for various UI activities such as get list of all saved searches in a compartment, create a dashboard, open a saved search, etc.  Use export to retrieve  dashboards and their saved searches, then edit the Json if necessary (for example change compartmentIds), then import the result to  destination dashboard service.
APIs validate all required properties to ensure properties are present and have correct type and values."""), short_help=cli_util.override('management_dashboard.management_dashboard_root_group.short_help', """ManagementDashboard API"""))
@cli_util.help_option_group
def management_dashboard_root_group():
    pass


@click.command(cli_util.override('management_dashboard.management_saved_search_group.command_name', 'management-saved-search'), cls=CommandGroupWithAlias, help="""Properties of a saved search.""")
@cli_util.help_option_group
def management_saved_search_group():
    pass


@click.command(cli_util.override('management_dashboard.management_dashboard_import_details_group.command_name', 'management-dashboard-import-details'), cls=CommandGroupWithAlias, help="""Array of dashboards to import.""")
@cli_util.help_option_group
def management_dashboard_import_details_group():
    pass


@click.command(cli_util.override('management_dashboard.management_dashboard_group.command_name', 'management-dashboard'), cls=CommandGroupWithAlias, help="""Properties for a dashboard, including dashboard id.""")
@cli_util.help_option_group
def management_dashboard_group():
    pass


management_dashboard_root_group.add_command(management_saved_search_group)
management_dashboard_root_group.add_command(management_dashboard_import_details_group)
management_dashboard_root_group.add_command(management_dashboard_group)


@management_dashboard_group.command(name=cli_util.override('management_dashboard.change_management_dashboards_compartment.command_name', 'change-compartment'), help=u"""Move the dashboard from existing compartment to a new compartment. \n[Command Reference](changeManagementDashboardsCompartment)""")
@cli_util.option('--management-dashboard-id', required=True, help=u"""unique dashboard identifier""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_management_dashboards_compartment(ctx, from_json, management_dashboard_id, compartment_id, if_match):

    if isinstance(management_dashboard_id, six.string_types) and len(management_dashboard_id.strip()) == 0:
        raise click.UsageError('Parameter --management-dashboard-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('management_dashboard', 'dashx_apis', ctx)
    result = client.change_management_dashboards_compartment(
        management_dashboard_id=management_dashboard_id,
        change_management_dashboards_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@management_saved_search_group.command(name=cli_util.override('management_dashboard.change_management_saved_searches_compartment.command_name', 'change-compartment'), help=u"""Move the saved search from existing compartment to a new compartment. \n[Command Reference](changeManagementSavedSearchesCompartment)""")
@cli_util.option('--management-saved-search-id', required=True, help=u"""unique saved search identifier""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_management_saved_searches_compartment(ctx, from_json, management_saved_search_id, compartment_id, if_match):

    if isinstance(management_saved_search_id, six.string_types) and len(management_saved_search_id.strip()) == 0:
        raise click.UsageError('Parameter --management-saved-search-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('management_dashboard', 'dashx_apis', ctx)
    result = client.change_management_saved_searches_compartment(
        management_saved_search_id=management_saved_search_id,
        change_management_saved_searches_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@management_dashboard_group.command(name=cli_util.override('management_dashboard.create_management_dashboard.command_name', 'create'), help=u"""Creates a new dashboard.  Limit for number of saved searches in a dashboard is 20. \n[Command Reference](createManagementDashboard)""")
@cli_util.option('--provider-id', required=True, help=u"""Provider Id.""")
@cli_util.option('--provider-name', required=True, help=u"""Provider name.""")
@cli_util.option('--provider-version', required=True, help=u"""Provider version.""")
@cli_util.option('--tiles', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Dashboard tiles array.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', required=True, help=u"""Display name for dashboard.""")
@cli_util.option('--description', required=True, help=u"""Dashboard's description.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ocid of the compartment that owns the dashboard.""")
@cli_util.option('--is-oob-dashboard', required=True, type=click.BOOL, help=u"""String boolean (\"true\" or \"false\").  OOB (Out of the Box) dashboards are only provided by Oracle.  They cannot be modified by non-Oracle.""")
@cli_util.option('--is-show-in-home', required=True, type=click.BOOL, help=u"""String boolean (\"true\" or \"false\").  When false, dashboard is not shown in dashboard home.""")
@cli_util.option('--metadata-version', required=True, help=u"""Version of the metadata.""")
@cli_util.option('--is-show-description', required=True, type=click.BOOL, help=u"""String boolean (\"true\" or \"false\").  Whether to show the dashboard description.""")
@cli_util.option('--screen-image', required=True, help=u"""screen image.""")
@cli_util.option('--nls', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Json for internationalization.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ui-config', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Json to contain options for UI.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-config', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Array of Json to contain options for source of data.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--type', required=True, help=u"""NORMAL means single dashboard, or SET means dashboard set.""")
@cli_util.option('--is-favorite', required=True, type=click.BOOL, help=u"""String boolean (\"true\" or \"false\").""")
@cli_util.option('--dashboard-id', help=u"""Dashboard Id. Must be providied if OOB, otherwise must not be provided.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'tiles': {'module': 'management_dashboard', 'class': 'list[ManagementDashboardTileDetails]'}, 'nls': {'module': 'management_dashboard', 'class': 'object'}, 'ui-config': {'module': 'management_dashboard', 'class': 'object'}, 'data-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'freeform-tags': {'module': 'management_dashboard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'management_dashboard', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'tiles': {'module': 'management_dashboard', 'class': 'list[ManagementDashboardTileDetails]'}, 'nls': {'module': 'management_dashboard', 'class': 'object'}, 'ui-config': {'module': 'management_dashboard', 'class': 'object'}, 'data-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'freeform-tags': {'module': 'management_dashboard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'management_dashboard', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'management_dashboard', 'class': 'ManagementDashboard'})
@cli_util.wrap_exceptions
def create_management_dashboard(ctx, from_json, provider_id, provider_name, provider_version, tiles, display_name, description, compartment_id, is_oob_dashboard, is_show_in_home, metadata_version, is_show_description, screen_image, nls, ui_config, data_config, type, is_favorite, dashboard_id, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['providerId'] = provider_id
    _details['providerName'] = provider_name
    _details['providerVersion'] = provider_version
    _details['tiles'] = cli_util.parse_json_parameter("tiles", tiles)
    _details['displayName'] = display_name
    _details['description'] = description
    _details['compartmentId'] = compartment_id
    _details['isOobDashboard'] = is_oob_dashboard
    _details['isShowInHome'] = is_show_in_home
    _details['metadataVersion'] = metadata_version
    _details['isShowDescription'] = is_show_description
    _details['screenImage'] = screen_image
    _details['nls'] = cli_util.parse_json_parameter("nls", nls)
    _details['uiConfig'] = cli_util.parse_json_parameter("ui_config", ui_config)
    _details['dataConfig'] = cli_util.parse_json_parameter("data_config", data_config)
    _details['type'] = type
    _details['isFavorite'] = is_favorite

    if dashboard_id is not None:
        _details['dashboardId'] = dashboard_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('management_dashboard', 'dashx_apis', ctx)
    result = client.create_management_dashboard(
        create_management_dashboard_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@management_saved_search_group.command(name=cli_util.override('management_dashboard.create_management_saved_search.command_name', 'create'), help=u"""Creates a new saved search. \n[Command Reference](createManagementSavedSearch)""")
@cli_util.option('--id', required=True, help=u"""id for saved search.  Must be provided if OOB, otherwise must not be provided.""")
@cli_util.option('--display-name', required=True, help=u"""Display name for saved search.""")
@cli_util.option('--provider-id', required=True, help=u"""Id for application (LA, APM, etc.) that owners this saved search.  Each owner has a unique Id.""")
@cli_util.option('--provider-version', required=True, help=u"""Version.""")
@cli_util.option('--provider-name', required=True, help=u"""Name for application (LA, APM, etc.) that owners this saved search.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ocid of the compartment that owns the saved search.""")
@cli_util.option('--is-oob-saved-search', required=True, type=click.BOOL, help=u"""String boolean (\"true\" or \"false\") to indicate Out Of the Box saved search.""")
@cli_util.option('--description', required=True, help=u"""Description.""")
@cli_util.option('--nls', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Json for internationalization.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["SEARCH_SHOW_IN_DASHBOARD", "SEARCH_DONT_SHOW_IN_DASHBOARD", "WIDGET_SHOW_IN_DASHBOARD", "WIDGET_DONT_SHOW_IN_DASHBOARD"]), help=u"""How to show the saved search.""")
@cli_util.option('--ui-config', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Json to contain options for UI.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-config', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Array of Json to contain options for source of data.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--screen-image', required=True, help=u"""Screenshot.""")
@cli_util.option('--metadata-version', required=True, help=u"""Version of the metadata.""")
@cli_util.option('--widget-template', required=True, help=u"""Template.""")
@cli_util.option('--widget-vm', required=True, help=u"""View Model""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'nls': {'module': 'management_dashboard', 'class': 'object'}, 'ui-config': {'module': 'management_dashboard', 'class': 'object'}, 'data-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'freeform-tags': {'module': 'management_dashboard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'management_dashboard', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'nls': {'module': 'management_dashboard', 'class': 'object'}, 'ui-config': {'module': 'management_dashboard', 'class': 'object'}, 'data-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'freeform-tags': {'module': 'management_dashboard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'management_dashboard', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'management_dashboard', 'class': 'ManagementSavedSearch'})
@cli_util.wrap_exceptions
def create_management_saved_search(ctx, from_json, id, display_name, provider_id, provider_version, provider_name, compartment_id, is_oob_saved_search, description, nls, type, ui_config, data_config, screen_image, metadata_version, widget_template, widget_vm, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['id'] = id
    _details['displayName'] = display_name
    _details['providerId'] = provider_id
    _details['providerVersion'] = provider_version
    _details['providerName'] = provider_name
    _details['compartmentId'] = compartment_id
    _details['isOobSavedSearch'] = is_oob_saved_search
    _details['description'] = description
    _details['nls'] = cli_util.parse_json_parameter("nls", nls)
    _details['type'] = type
    _details['uiConfig'] = cli_util.parse_json_parameter("ui_config", ui_config)
    _details['dataConfig'] = cli_util.parse_json_parameter("data_config", data_config)
    _details['screenImage'] = screen_image
    _details['metadataVersion'] = metadata_version
    _details['widgetTemplate'] = widget_template
    _details['widgetVM'] = widget_vm

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('management_dashboard', 'dashx_apis', ctx)
    result = client.create_management_saved_search(
        create_management_saved_search_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@management_dashboard_group.command(name=cli_util.override('management_dashboard.delete_management_dashboard.command_name', 'delete'), help=u"""Deletes a Dashboard by id. \n[Command Reference](deleteManagementDashboard)""")
@cli_util.option('--management-dashboard-id', required=True, help=u"""unique dashboard identifier""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_management_dashboard(ctx, from_json, management_dashboard_id, if_match):

    if isinstance(management_dashboard_id, six.string_types) and len(management_dashboard_id.strip()) == 0:
        raise click.UsageError('Parameter --management-dashboard-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_dashboard', 'dashx_apis', ctx)
    result = client.delete_management_dashboard(
        management_dashboard_id=management_dashboard_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@management_saved_search_group.command(name=cli_util.override('management_dashboard.delete_management_saved_search.command_name', 'delete'), help=u"""Deletes a saved search by Id \n[Command Reference](deleteManagementSavedSearch)""")
@cli_util.option('--management-saved-search-id', required=True, help=u"""unique saved search identifier""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_management_saved_search(ctx, from_json, management_saved_search_id, if_match):

    if isinstance(management_saved_search_id, six.string_types) and len(management_saved_search_id.strip()) == 0:
        raise click.UsageError('Parameter --management-saved-search-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_dashboard', 'dashx_apis', ctx)
    result = client.delete_management_saved_search(
        management_saved_search_id=management_saved_search_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@management_dashboard_import_details_group.command(name=cli_util.override('management_dashboard.export_dashboard.command_name', 'export-dashboard'), help=u"""Exports an array of dashboards and their saved searches. \n[Command Reference](exportDashboard)""")
@cli_util.option('--export-dashboard-id', required=True, help=u"""{\"dashboardIds\":[\"dashboardId1\", \"dashboardId2\", ...]}""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_dashboard', 'class': 'ManagementDashboardExportDetails'})
@cli_util.wrap_exceptions
def export_dashboard(ctx, from_json, export_dashboard_id):

    if isinstance(export_dashboard_id, six.string_types) and len(export_dashboard_id.strip()) == 0:
        raise click.UsageError('Parameter --export-dashboard-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_dashboard', 'dashx_apis', ctx)
    result = client.export_dashboard(
        export_dashboard_id=export_dashboard_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@management_dashboard_group.command(name=cli_util.override('management_dashboard.get_management_dashboard.command_name', 'get'), help=u"""Get a Dashboard and its saved searches by id.  Deleted or unauthorized saved searches are marked by tile's state property. \n[Command Reference](getManagementDashboard)""")
@cli_util.option('--management-dashboard-id', required=True, help=u"""unique dashboard identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_dashboard', 'class': 'ManagementDashboard'})
@cli_util.wrap_exceptions
def get_management_dashboard(ctx, from_json, management_dashboard_id):

    if isinstance(management_dashboard_id, six.string_types) and len(management_dashboard_id.strip()) == 0:
        raise click.UsageError('Parameter --management-dashboard-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_dashboard', 'dashx_apis', ctx)
    result = client.get_management_dashboard(
        management_dashboard_id=management_dashboard_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@management_saved_search_group.command(name=cli_util.override('management_dashboard.get_management_saved_search.command_name', 'get'), help=u"""Get a saved search by Id. \n[Command Reference](getManagementSavedSearch)""")
@cli_util.option('--management-saved-search-id', required=True, help=u"""unique saved search identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_dashboard', 'class': 'ManagementSavedSearch'})
@cli_util.wrap_exceptions
def get_management_saved_search(ctx, from_json, management_saved_search_id):

    if isinstance(management_saved_search_id, six.string_types) and len(management_saved_search_id.strip()) == 0:
        raise click.UsageError('Parameter --management-saved-search-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_dashboard', 'dashx_apis', ctx)
    result = client.get_management_saved_search(
        management_saved_search_id=management_saved_search_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@management_dashboard_import_details_group.command(name=cli_util.override('management_dashboard.import_dashboard.command_name', 'import-dashboard'), help=u"""Import an array of dashboards and their saved searches. \n[Command Reference](importDashboard)""")
@cli_util.option('--dashboards', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Array of dashboards""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'dashboards': {'module': 'management_dashboard', 'class': 'list[ManagementDashboardForImportExportDetails]'}, 'freeform-tags': {'module': 'management_dashboard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'management_dashboard', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'dashboards': {'module': 'management_dashboard', 'class': 'list[ManagementDashboardForImportExportDetails]'}, 'freeform-tags': {'module': 'management_dashboard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'management_dashboard', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def import_dashboard(ctx, from_json, dashboards, freeform_tags, defined_tags, if_match):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dashboards'] = cli_util.parse_json_parameter("dashboards", dashboards)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('management_dashboard', 'dashx_apis', ctx)
    result = client.import_dashboard(
        management_dashboard_import_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@management_dashboard_group.command(name=cli_util.override('management_dashboard.list_management_dashboards.command_name', 'list'), help=u"""Gets list of dashboards and their saved searches for compartment with pagination.  Returned properties are a summary. \n[Command Reference](listManagementDashboards)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_dashboard', 'class': 'ManagementDashboardCollection'})
@cli_util.wrap_exceptions
def list_management_dashboards(ctx, from_json, all_pages, page_size, compartment_id, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_dashboard', 'dashx_apis', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_management_dashboards,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_management_dashboards,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_management_dashboards(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@management_saved_search_group.command(name=cli_util.override('management_dashboard.list_management_saved_searches.command_name', 'list'), help=u"""Gets list of saved searches with pagination.  Returned properties are a summary. \n[Command Reference](listManagementSavedSearches)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_dashboard', 'class': 'ManagementSavedSearchCollection'})
@cli_util.wrap_exceptions
def list_management_saved_searches(ctx, from_json, all_pages, page_size, compartment_id, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_dashboard', 'dashx_apis', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_management_saved_searches,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_management_saved_searches,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_management_saved_searches(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@management_dashboard_group.command(name=cli_util.override('management_dashboard.update_management_dashboard.command_name', 'update'), help=u"""Updates an existing dashboard identified by id path parameter.  Limit for number of saved searches in a dashboard is 20. \n[Command Reference](updateManagementDashboard)""")
@cli_util.option('--management-dashboard-id', required=True, help=u"""unique dashboard identifier""")
@cli_util.option('--provider-id', help=u"""Provider Id.""")
@cli_util.option('--provider-name', help=u"""Provider name.""")
@cli_util.option('--provider-version', help=u"""Provider version.""")
@cli_util.option('--tiles', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Dashboard tiles array.

This option is a JSON list with items of type ManagementDashboardTileDetails.  For documentation on ManagementDashboardTileDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/dashxapis/20200901/datatypes/ManagementDashboardTileDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Display name for dashboard.""")
@cli_util.option('--description', help=u"""Dashboard's description.""")
@cli_util.option('--compartment-id', help=u"""The ocid of the compartment that owns the dashboard.""")
@cli_util.option('--is-oob-dashboard', type=click.BOOL, help=u"""String boolean (\"true\" or \"false\").  OOB (Out of the Box) dashboards are only provided by Oracle.  They cannot be modified by non-Oracle.""")
@cli_util.option('--is-show-in-home', type=click.BOOL, help=u"""String boolean (\"true\" or \"false\").  When false, dashboard is not shown in dashboard home.""")
@cli_util.option('--metadata-version', help=u"""Version of the metadata.""")
@cli_util.option('--is-show-description', type=click.BOOL, help=u"""String boolean (\"true\" or \"false\").  Whether to show the dashboard description.""")
@cli_util.option('--screen-image', help=u"""Screen image.""")
@cli_util.option('--nls', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Json for internationalization.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ui-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Json to contain options for UI.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Array of Json to contain options for source of data.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--type', help=u"""NORMAL meaning single dashboard, or SET meaning dashboard set.""")
@cli_util.option('--is-favorite', type=click.BOOL, help=u"""String boolean (\"true\" or \"false\").""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'tiles': {'module': 'management_dashboard', 'class': 'list[ManagementDashboardTileDetails]'}, 'nls': {'module': 'management_dashboard', 'class': 'object'}, 'ui-config': {'module': 'management_dashboard', 'class': 'object'}, 'data-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'freeform-tags': {'module': 'management_dashboard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'management_dashboard', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'tiles': {'module': 'management_dashboard', 'class': 'list[ManagementDashboardTileDetails]'}, 'nls': {'module': 'management_dashboard', 'class': 'object'}, 'ui-config': {'module': 'management_dashboard', 'class': 'object'}, 'data-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'freeform-tags': {'module': 'management_dashboard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'management_dashboard', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'management_dashboard', 'class': 'ManagementDashboard'})
@cli_util.wrap_exceptions
def update_management_dashboard(ctx, from_json, force, management_dashboard_id, provider_id, provider_name, provider_version, tiles, display_name, description, compartment_id, is_oob_dashboard, is_show_in_home, metadata_version, is_show_description, screen_image, nls, ui_config, data_config, type, is_favorite, freeform_tags, defined_tags, if_match):

    if isinstance(management_dashboard_id, six.string_types) and len(management_dashboard_id.strip()) == 0:
        raise click.UsageError('Parameter --management-dashboard-id cannot be whitespace or empty string')
    if not force:
        if tiles or nls or ui_config or data_config or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to tiles and nls and ui-config and data-config and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if provider_id is not None:
        _details['providerId'] = provider_id

    if provider_name is not None:
        _details['providerName'] = provider_name

    if provider_version is not None:
        _details['providerVersion'] = provider_version

    if tiles is not None:
        _details['tiles'] = cli_util.parse_json_parameter("tiles", tiles)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if is_oob_dashboard is not None:
        _details['isOobDashboard'] = is_oob_dashboard

    if is_show_in_home is not None:
        _details['isShowInHome'] = is_show_in_home

    if metadata_version is not None:
        _details['metadataVersion'] = metadata_version

    if is_show_description is not None:
        _details['isShowDescription'] = is_show_description

    if screen_image is not None:
        _details['screenImage'] = screen_image

    if nls is not None:
        _details['nls'] = cli_util.parse_json_parameter("nls", nls)

    if ui_config is not None:
        _details['uiConfig'] = cli_util.parse_json_parameter("ui_config", ui_config)

    if data_config is not None:
        _details['dataConfig'] = cli_util.parse_json_parameter("data_config", data_config)

    if type is not None:
        _details['type'] = type

    if is_favorite is not None:
        _details['isFavorite'] = is_favorite

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('management_dashboard', 'dashx_apis', ctx)
    result = client.update_management_dashboard(
        management_dashboard_id=management_dashboard_id,
        update_management_dashboard_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@management_saved_search_group.command(name=cli_util.override('management_dashboard.update_management_saved_search.command_name', 'update'), help=u"""Update an existing saved search.  Id cannot be updated. \n[Command Reference](updateManagementSavedSearch)""")
@cli_util.option('--management-saved-search-id', required=True, help=u"""unique saved search identifier""")
@cli_util.option('--display-name', help=u"""Display name for saved search.""")
@cli_util.option('--provider-id', help=u"""Id for application (LA, APM, etc.) that owners this saved search.  Each owner has a unique Id.""")
@cli_util.option('--provider-version', help=u"""Version.""")
@cli_util.option('--provider-name', help=u"""Name for application (LA, APM, etc.) that owners this saved search.""")
@cli_util.option('--compartment-id', help=u"""The ocid of the compartment that owns the saved search.""")
@cli_util.option('--is-oob-saved-search', type=click.BOOL, help=u"""String boolean (\"true\" or \"false\") to indicate Out Of the Box saved search.""")
@cli_util.option('--description', help=u"""Description.""")
@cli_util.option('--nls', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Json for internationalization.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["SEARCH_SHOW_IN_DASHBOARD", "SEARCH_DONT_SHOW_IN_DASHBOARD", "WIDGET_SHOW_IN_DASHBOARD", "WIDGET_DONT_SHOW_IN_DASHBOARD"]), help=u"""How to show the saved search.""")
@cli_util.option('--ui-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Json to contain options for UI.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Array of Json to contain options for source of data.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--screen-image', help=u"""Screenshot.""")
@cli_util.option('--metadata-version', help=u"""Version of the metadata.""")
@cli_util.option('--widget-template', help=u"""Template.""")
@cli_util.option('--widget-vm', help=u"""View Model""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'nls': {'module': 'management_dashboard', 'class': 'object'}, 'ui-config': {'module': 'management_dashboard', 'class': 'object'}, 'data-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'freeform-tags': {'module': 'management_dashboard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'management_dashboard', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'nls': {'module': 'management_dashboard', 'class': 'object'}, 'ui-config': {'module': 'management_dashboard', 'class': 'object'}, 'data-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'freeform-tags': {'module': 'management_dashboard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'management_dashboard', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'management_dashboard', 'class': 'ManagementSavedSearch'})
@cli_util.wrap_exceptions
def update_management_saved_search(ctx, from_json, force, management_saved_search_id, display_name, provider_id, provider_version, provider_name, compartment_id, is_oob_saved_search, description, nls, type, ui_config, data_config, screen_image, metadata_version, widget_template, widget_vm, freeform_tags, defined_tags, if_match):

    if isinstance(management_saved_search_id, six.string_types) and len(management_saved_search_id.strip()) == 0:
        raise click.UsageError('Parameter --management-saved-search-id cannot be whitespace or empty string')
    if not force:
        if nls or ui_config or data_config or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to nls and ui-config and data-config and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if provider_id is not None:
        _details['providerId'] = provider_id

    if provider_version is not None:
        _details['providerVersion'] = provider_version

    if provider_name is not None:
        _details['providerName'] = provider_name

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if is_oob_saved_search is not None:
        _details['isOobSavedSearch'] = is_oob_saved_search

    if description is not None:
        _details['description'] = description

    if nls is not None:
        _details['nls'] = cli_util.parse_json_parameter("nls", nls)

    if type is not None:
        _details['type'] = type

    if ui_config is not None:
        _details['uiConfig'] = cli_util.parse_json_parameter("ui_config", ui_config)

    if data_config is not None:
        _details['dataConfig'] = cli_util.parse_json_parameter("data_config", data_config)

    if screen_image is not None:
        _details['screenImage'] = screen_image

    if metadata_version is not None:
        _details['metadataVersion'] = metadata_version

    if widget_template is not None:
        _details['widgetTemplate'] = widget_template

    if widget_vm is not None:
        _details['widgetVM'] = widget_vm

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('management_dashboard', 'dashx_apis', ctx)
    result = client.update_management_saved_search(
        management_saved_search_id=management_saved_search_id,
        update_management_saved_search_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
