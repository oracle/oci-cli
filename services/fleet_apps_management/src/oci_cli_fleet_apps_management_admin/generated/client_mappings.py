# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.fleet_apps_management import FleetAppsManagementAdminClient

MODULE_TO_TYPE_MAPPINGS["fleet_apps_management"] = oci.fleet_apps_management.models.fleet_apps_management_type_mapping
if CLIENT_MAP.get("fleet_apps_management") is None:
    CLIENT_MAP["fleet_apps_management"] = {}
CLIENT_MAP["fleet_apps_management"]["fleet_apps_management_admin"] = FleetAppsManagementAdminClient
