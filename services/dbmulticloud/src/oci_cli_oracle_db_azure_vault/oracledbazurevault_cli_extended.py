# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.dbmulticloud.src.oci_cli_oracle_db_azure_vault.generated import oracledbazurevault_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# Move commands under 'oci dbmulticloud oracle-db-azure-vault oracle-db-azure-vault' -> 'oci dbmulticloud oracle-db-azure-vault'
oracledbazurevault_cli.oracle_db_azure_vault_root_group.commands.pop(oracledbazurevault_cli.oracle_db_azure_vault_group.name)
oracledbazurevault_cli.oracle_db_azure_vault_root_group.add_command(oracledbazurevault_cli.change_oracle_db_azure_vault_compartment)
oracledbazurevault_cli.oracle_db_azure_vault_root_group.add_command(oracledbazurevault_cli.create_oracle_db_azure_vault)
oracledbazurevault_cli.oracle_db_azure_vault_root_group.add_command(oracledbazurevault_cli.delete_oracle_db_azure_vault)
oracledbazurevault_cli.oracle_db_azure_vault_root_group.add_command(oracledbazurevault_cli.get_oracle_db_azure_vault)
oracledbazurevault_cli.oracle_db_azure_vault_root_group.add_command(oracledbazurevault_cli.list_oracle_db_azure_vaults)
oracledbazurevault_cli.oracle_db_azure_vault_root_group.add_command(oracledbazurevault_cli.refresh_oracle_db_azure_vault)
oracledbazurevault_cli.oracle_db_azure_vault_root_group.add_command(oracledbazurevault_cli.update_oracle_db_azure_vault)
