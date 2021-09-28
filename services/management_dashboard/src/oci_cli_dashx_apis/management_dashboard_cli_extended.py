# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import six
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from services.management_dashboard.src.oci_cli_dashx_apis.generated import dashxapis_cli

'''
From:
oci management-dashboard management-dashboard
oci management-dashboard management-saved-search
oci management-dashboard management-dashboard-import-details export-dashboard
oci management-dashboard management-dashboard-import-details import-dashboard

To:
oci management-dashboard dashboard
oci management-dashboard saved-search
oci management-dashboard dashboard export
oci management-dashboard dashboard import

First two are groups, bottom two are commands.
'''
dashxapis_cli.management_dashboard_root_group.commands.pop(dashxapis_cli.management_dashboard_import_details_group.name)
cli_util.rename_command(dashxapis_cli, dashxapis_cli.management_dashboard_root_group, dashxapis_cli.management_dashboard_group, "dashboard")
cli_util.rename_command(dashxapis_cli, dashxapis_cli.management_dashboard_root_group, dashxapis_cli.management_saved_search_group, "saved-search")
dashxapis_cli.management_dashboard_group.add_command(dashxapis_cli.import_dashboard)
cli_util.rename_command(dashxapis_cli, dashxapis_cli.management_dashboard_group, dashxapis_cli.import_dashboard, "import")


@dashxapis_cli.management_dashboard_group.command(name=cli_util.override('dashxapis_cli.export_dashboard.command_name', 'export'), help=u"""Exports an array of dashboards and their saved searches. Export is designed to work with importDashboard. Here's an example of how you can use CLI to export a dashboard. $oci management-dashboard dashboard export --query data --export-dashboard-id \"{\\\"dashboardIds\\\":[\\\"ocid1.managementdashboard.oc1..dashboardId1\\\"]}\"  > dashboards.json \n[Command Reference](exportDashboard)""")
@cli_util.option('--export-dashboard-id', required=True, help=u"""List of dashboardIds in plain text. The syntax is '{\"dashboardIds\":[\"dashboardId1\", \"dashboardId2\", ...]}'. Escaping is needed when using in OCI CLI. For example, \"{\\\"dashboardIds\\\":[\\\"ocid1.managementdashboard.oc1..dashboardId1\\\"]}\" .""")
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

    if result.data:
        try:
            data = cli_util.to_dict(result.data)

            for dashboard in data["dashboards"]:
                for saved_search in dashboard["saved-searches"]:
                    if "widget-vm" in saved_search:

                        saved_search["widget-v-m"] = saved_search["widget-vm"]
                        del saved_search["widget-vm"]
            result.data = data
        except Exception:
            pass
    cli_util.render_response(result, ctx)
