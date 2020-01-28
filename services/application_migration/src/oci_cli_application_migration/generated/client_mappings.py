# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.application_migration import ApplicationMigrationClient

MODULE_TO_TYPE_MAPPINGS["application_migration"] = oci.application_migration.models.application_migration_type_mapping
CLIENT_MAP["application_migration"] = ApplicationMigrationClient
