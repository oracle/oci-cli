# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.database_management.src.oci_cli_sql_tuning.generated import sqltuning_cli
from services.database_management.src.oci_cli_database_management.generated import database_management_service_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


# Move commands under 'oci database-management sql-tuning managed-database' -> 'oci database-management sql-tuning-task'
sqltuning_cli.sql_tuning_root_group.commands.pop(sqltuning_cli.managed_database_group.name)
database_management_service_cli.database_management_service_group.commands.pop(sqltuning_cli.sql_tuning_root_group.name)


@click.command('sql-tuning-task', cls=CommandGroupWithAlias, help="sql Tuning Tasks")
@cli_util.help_option_group
def sql_tuning_task_group():
    pass


database_management_service_cli.database_management_service_group.add_command(sql_tuning_task_group)

# oci database-management clone-sql-tuning-task -> oci database-management sql-tuning-task clone
sql_tuning_task_group.add_command(sqltuning_cli.clone_sql_tuning_task)
cli_util.rename_command(sqltuning_cli, sql_tuning_task_group, sqltuning_cli.clone_sql_tuning_task, "clone")

# oci database-management clone-sql-tuning-task-sql-tuning-task-password-credential-details -> oci database-management sql-tuning-task clone-with-pwd
sql_tuning_task_group.add_command(sqltuning_cli.clone_sql_tuning_task_sql_tuning_task_password_credential_details)
cli_util.rename_command(sqltuning_cli, sql_tuning_task_group, sqltuning_cli.clone_sql_tuning_task_sql_tuning_task_password_credential_details, "clone-with-pwd")

# oci database-management clone-sql-tuning-task-sql-tuning-task-secret-credential-details -> oci database-management sql-tuning-task clone-with-secret
sql_tuning_task_group.add_command(sqltuning_cli.clone_sql_tuning_task_sql_tuning_task_secret_credential_details)
cli_util.rename_command(sqltuning_cli, sql_tuning_task_group, sqltuning_cli.clone_sql_tuning_task_sql_tuning_task_secret_credential_details, "clone-with-secret")

# oci database-management start-sql-tuning-task -> oci database-management sql-tuning-task start
sql_tuning_task_group.add_command(sqltuning_cli.start_sql_tuning_task)
cli_util.rename_command(sqltuning_cli, sql_tuning_task_group, sqltuning_cli.start_sql_tuning_task, "start")

# oci database-management start-sql-tuning-task-sql-tuning-task-password-credential-details -> oci database-management sql-tuning-task start-with-pwd
sql_tuning_task_group.add_command(sqltuning_cli.start_sql_tuning_task_sql_tuning_task_password_credential_details)
cli_util.rename_command(sqltuning_cli, sql_tuning_task_group, sqltuning_cli.start_sql_tuning_task_sql_tuning_task_password_credential_details, "start-with-pwd")

# oci database-management start-sql-tuning-task-sql-tuning-task-secret-credential-details ->oci database-management sql-tuning-task start-with-secret
sql_tuning_task_group.add_command(sqltuning_cli.start_sql_tuning_task_sql_tuning_task_secret_credential_details)
cli_util.rename_command(sqltuning_cli, sql_tuning_task_group, sqltuning_cli.start_sql_tuning_task_sql_tuning_task_secret_credential_details, "start-with-secret")

# oci database-management drop-sql-tuning-task -> oci database-management sql-tuning-task drop
sql_tuning_task_group.add_command(sqltuning_cli.drop_sql_tuning_task)
cli_util.rename_command(sqltuning_cli, sql_tuning_task_group, sqltuning_cli.drop_sql_tuning_task, "drop")

# oci database-management drop-sql-tuning-task-sql-tuning-task-password-credential-details -> oci database-management sql-tuning-task drop-with-pwd
sql_tuning_task_group.add_command(sqltuning_cli.drop_sql_tuning_task_sql_tuning_task_password_credential_details)
cli_util.rename_command(sqltuning_cli, sql_tuning_task_group, sqltuning_cli.drop_sql_tuning_task_sql_tuning_task_password_credential_details, "drop-with-pwd")

# oci database-management drop-sql-tuning-task-sql-tuning-task-secret-credential-details -> oci database-management sql-tuning-task drop-with-secret
sql_tuning_task_group.add_command(sqltuning_cli.drop_sql_tuning_task_sql_tuning_task_secret_credential_details)
cli_util.rename_command(sqltuning_cli, sql_tuning_task_group, sqltuning_cli.drop_sql_tuning_task_sql_tuning_task_secret_credential_details, "drop-with-secret")

# oci database-management get-sql-tuning-advisor-task-summary-report -> oci database-management sql-tuning-task get-summary-report
sql_tuning_task_group.add_command(sqltuning_cli.get_sql_tuning_advisor_task_summary_report)
cli_util.rename_command(sqltuning_cli, sql_tuning_task_group, sqltuning_cli.get_sql_tuning_advisor_task_summary_report, "get-summary-report")

# oci database-management get-execution-plan-stats-comparision -> oci database-management sql-tuning-task get-exec-plan-stats-compare
sql_tuning_task_group.add_command(sqltuning_cli.get_execution_plan_stats_comparision)
cli_util.rename_command(sqltuning_cli, sql_tuning_task_group, sqltuning_cli.get_execution_plan_stats_comparision, "get-exec-plan-stats-compare")

# oci database-management get-sql-execution-plan -> oci database-management sql-tuning-task get-sql-exec-plan
sql_tuning_task_group.add_command(sqltuning_cli.get_sql_execution_plan)
cli_util.rename_command(sqltuning_cli, sql_tuning_task_group, sqltuning_cli.get_sql_execution_plan, "get-sql-exec-plan")

# oci database-management list-sql-tuning-advisor-task-findings -> oci database-management sql-tuning-task list-findings
sql_tuning_task_group.add_command(sqltuning_cli.list_sql_tuning_advisor_task_findings)
cli_util.rename_command(sqltuning_cli, sql_tuning_task_group, sqltuning_cli.list_sql_tuning_advisor_task_findings, "list-findings")

# oci database-management list-sql-tuning-advisor-task-recommendations -> oci database-management sql-tuning-task list-recommendations
sql_tuning_task_group.add_command(sqltuning_cli.list_sql_tuning_advisor_task_recommendations)
cli_util.rename_command(sqltuning_cli, sql_tuning_task_group, sqltuning_cli.list_sql_tuning_advisor_task_recommendations, "list-recommendations")

# oci database-management list-sql-tuning-advisor-tasks -> oci database-management sql-tuning-task list-tasks
sql_tuning_task_group.add_command(sqltuning_cli.list_sql_tuning_advisor_tasks)
cli_util.rename_command(sqltuning_cli, sql_tuning_task_group, sqltuning_cli.list_sql_tuning_advisor_tasks, "list-tasks")
