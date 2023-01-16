# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci_cli.cli_root import cli
from oci_cli import cli_util
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('sql_tuning.database_management_service_group.command_name', 'database-management'), cls=CommandGroupWithAlias, help=cli_util.override('sql_tuning.database_management_service_group.help', """Use the Database Management API to perform tasks such as obtaining performance and resource usage metrics
for a fleet of Managed Databases or a specific Managed Database, creating Managed Database Groups, and
running a SQL job on a Managed Database or Managed Database Group."""), short_help=cli_util.override('sql_tuning.database_management_service_group.short_help', """Database Management API"""))
@cli_util.help_option_group
def database_management_service_group():
    pass
