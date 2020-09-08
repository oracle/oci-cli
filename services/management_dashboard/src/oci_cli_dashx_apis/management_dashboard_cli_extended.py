# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
from oci_cli import cli_util
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
dashxapis_cli.management_dashboard_group.add_command(dashxapis_cli.export_dashboard)
cli_util.rename_command(dashxapis_cli, dashxapis_cli.management_dashboard_group, dashxapis_cli.export_dashboard, "export")
dashxapis_cli.management_dashboard_group.add_command(dashxapis_cli.import_dashboard)
cli_util.rename_command(dashxapis_cli, dashxapis_cli.management_dashboard_group, dashxapis_cli.import_dashboard, "import")
