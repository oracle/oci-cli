# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.application_migration import ApplicationMigrationClient

MODULE_TO_TYPE_MAPPINGS["application_migration"] = oci.application_migration.models.application_migration_type_mapping
if CLIENT_MAP.get("application_migration") is None:
    CLIENT_MAP["application_migration"] = {}
CLIENT_MAP["application_migration"]["application_migration"] = ApplicationMigrationClient
