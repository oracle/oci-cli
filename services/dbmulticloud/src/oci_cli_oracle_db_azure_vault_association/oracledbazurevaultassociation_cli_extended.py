# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.dbmulticloud.src.oci_cli_oracle_db_azure_vault_association.generated import oracledbazurevaultassociation_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# Move commands under 'oci dbmulticloud oracle-db-azure-vault-association oracle-db-azure-vault-association' -> 'oci dbmulticloud oracle-db-azure-vault-association'
oracledbazurevaultassociation_cli.oracle_db_azure_vault_association_root_group.commands.pop(oracledbazurevaultassociation_cli.oracle_db_azure_vault_association_group.name)
oracledbazurevaultassociation_cli.oracle_db_azure_vault_association_root_group.add_command(oracledbazurevaultassociation_cli.cascading_delete_oracle_db_azure_vault_association)
oracledbazurevaultassociation_cli.oracle_db_azure_vault_association_root_group.add_command(oracledbazurevaultassociation_cli.change_oracle_db_azure_vault_association_compartment)
oracledbazurevaultassociation_cli.oracle_db_azure_vault_association_root_group.add_command(oracledbazurevaultassociation_cli.create_oracle_db_azure_vault_association)
oracledbazurevaultassociation_cli.oracle_db_azure_vault_association_root_group.add_command(oracledbazurevaultassociation_cli.delete_oracle_db_azure_vault_association)
oracledbazurevaultassociation_cli.oracle_db_azure_vault_association_root_group.add_command(oracledbazurevaultassociation_cli.get_oracle_db_azure_vault_association)
oracledbazurevaultassociation_cli.oracle_db_azure_vault_association_root_group.add_command(oracledbazurevaultassociation_cli.list_oracle_db_azure_vault_associations)
oracledbazurevaultassociation_cli.oracle_db_azure_vault_association_root_group.add_command(oracledbazurevaultassociation_cli.update_oracle_db_azure_vault_association)
