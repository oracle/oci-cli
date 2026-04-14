# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.dbmulticloud.src.oci_cli_oracle_db_azure_vault.generated import oracledbazurevault_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401
from services.dbmulticloud.src.oci_cli_dbmulticloud.generated import dbmulticloud_service_cli

# Move commands under 'oci dbmulticloud oracle-db-azure-vault oracle-db-azure-vault' -> 'oci dbmulticloud oracle-db-azure-vault'
# Remove oracle_db_azure_vault_group from root group
oracledbazurevault_cli.oracle_db_azure_vault_root_group.commands.pop(oracledbazurevault_cli.oracle_db_azure_vault_group.name)
# Add oracle_db_azure_vault_group to dbmulticloud_service_group
dbmulticloud_service_cli.dbmulticloud_service_group.add_command(oracledbazurevault_cli.oracle_db_azure_vault_group)
