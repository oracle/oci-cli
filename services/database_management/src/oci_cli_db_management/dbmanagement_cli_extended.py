# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.database_management.src.oci_cli_db_management.generated import dbmanagement_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci database-management database-fleet-health-metrics -> oci database-management fleet-health-metrics
cli_util.rename_command(dbmanagement_cli, dbmanagement_cli.database_management_root_group, dbmanagement_cli.database_fleet_health_metrics_group, "fleet-health-metrics")


# oci database-management database-home-metrics -> oci database-management summary-metrics
cli_util.rename_command(dbmanagement_cli, dbmanagement_cli.database_management_root_group, dbmanagement_cli.database_home_metrics_group, "summary-metrics")


# oci database-management job create-job-create-sql-job-details -> oci database-management job create-sql-job
cli_util.rename_command(dbmanagement_cli, dbmanagement_cli.job_group, dbmanagement_cli.create_job_create_sql_job_details, "create-sql-job")


# Remove create from oci database-management job
dbmanagement_cli.job_group.commands.pop(dbmanagement_cli.create_job.name)


# Remove create-job-object-storage-job-execution-result-location from oci database-management job
dbmanagement_cli.job_group.commands.pop(dbmanagement_cli.create_job_object_storage_job_execution_result_location.name)
