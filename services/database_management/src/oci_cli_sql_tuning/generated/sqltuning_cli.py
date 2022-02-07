# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.database_management.src.oci_cli_database_management.generated import database_management_service_cli


@click.command(cli_util.override('sql_tuning.sql_tuning_root_group.command_name', 'sql-tuning'), cls=CommandGroupWithAlias, help=cli_util.override('sql_tuning.sql_tuning_root_group.help', """Use the Database Management API to perform tasks such as obtaining performance and resource usage metrics
for a fleet of Managed Databases or a specific Managed Database, creating Managed Database Groups, and
running a SQL job on a Managed Database or Managed Database Group."""), short_help=cli_util.override('sql_tuning.sql_tuning_root_group.short_help', """Database Management API"""))
@cli_util.help_option_group
def sql_tuning_root_group():
    pass


@click.command(cli_util.override('sql_tuning.managed_database_group.command_name', 'managed-database'), cls=CommandGroupWithAlias, help="""The details of a Managed Database.""")
@cli_util.help_option_group
def managed_database_group():
    pass


database_management_service_cli.database_management_service_group.add_command(sql_tuning_root_group)
sql_tuning_root_group.add_command(managed_database_group)


@managed_database_group.command(name=cli_util.override('sql_tuning.clone_sql_tuning_task.command_name', 'clone-sql-tuning-task'), help=u"""Clones and runs a SQL tuning task in the database. \n[Command Reference](cloneSqlTuningTask)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--task-name', required=True, help=u"""The name of the SQL tuning task. The name is unique per user in a database, and it is case-sensitive.""")
@cli_util.option('--original-task-id', required=True, type=click.INT, help=u"""The identifier of the SQL tuning task being cloned. This is not the [OCID]. It can be retrieved from the following endpoint [ListSqlTuningAdvisorTasks].""")
@cli_util.option('--credential-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--task-description', help=u"""The description of the SQL tuning task.""")
@json_skeleton_utils.get_cli_json_input_option({'credential-details': {'module': 'database_management', 'class': 'SqlTuningTaskCredentialDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'credential-details': {'module': 'database_management', 'class': 'SqlTuningTaskCredentialDetails'}}, output_type={'module': 'database_management', 'class': 'SqlTuningTaskReturn'})
@cli_util.wrap_exceptions
def clone_sql_tuning_task(ctx, from_json, managed_database_id, task_name, original_task_id, credential_details, task_description):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['taskName'] = task_name
    _details['originalTaskId'] = original_task_id
    _details['credentialDetails'] = cli_util.parse_json_parameter("credential_details", credential_details)

    if task_description is not None:
        _details['taskDescription'] = task_description

    client = cli_util.build_client('database_management', 'sql_tuning', ctx)
    result = client.clone_sql_tuning_task(
        managed_database_id=managed_database_id,
        clone_sql_tuning_task_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('sql_tuning.clone_sql_tuning_task_sql_tuning_task_secret_credential_details.command_name', 'clone-sql-tuning-task-sql-tuning-task-secret-credential-details'), help=u"""Clones and runs a SQL tuning task in the database. \n[Command Reference](cloneSqlTuningTask)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--task-name', required=True, help=u"""The name of the SQL tuning task. The name is unique per user in a database, and it is case-sensitive.""")
@cli_util.option('--original-task-id', required=True, type=click.INT, help=u"""The identifier of the SQL tuning task being cloned. This is not the [OCID]. It can be retrieved from the following endpoint [ListSqlTuningAdvisorTasks].""")
@cli_util.option('--credential-details-username', required=True, help=u"""The user name used to connect to the database.""")
@cli_util.option('--credential-details-role', required=True, type=custom_types.CliCaseInsensitiveChoice(["NORMAL", "SYSDBA"]), help=u"""The role of the database user.""")
@cli_util.option('--credential-details-password-secret-id', required=True, help=u"""The [OCID] of the Secret where the database password is stored.""")
@cli_util.option('--task-description', help=u"""The description of the SQL tuning task.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'SqlTuningTaskReturn'})
@cli_util.wrap_exceptions
def clone_sql_tuning_task_sql_tuning_task_secret_credential_details(ctx, from_json, managed_database_id, task_name, original_task_id, credential_details_username, credential_details_role, credential_details_password_secret_id, task_description):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['credentialDetails'] = {}
    _details['taskName'] = task_name
    _details['originalTaskId'] = original_task_id
    _details['credentialDetails']['username'] = credential_details_username
    _details['credentialDetails']['role'] = credential_details_role
    _details['credentialDetails']['passwordSecretId'] = credential_details_password_secret_id

    if task_description is not None:
        _details['taskDescription'] = task_description

    _details['credentialDetails']['sqlTuningTaskCredentialType'] = 'SECRET'

    client = cli_util.build_client('database_management', 'sql_tuning', ctx)
    result = client.clone_sql_tuning_task(
        managed_database_id=managed_database_id,
        clone_sql_tuning_task_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('sql_tuning.clone_sql_tuning_task_sql_tuning_task_password_credential_details.command_name', 'clone-sql-tuning-task-sql-tuning-task-password-credential-details'), help=u"""Clones and runs a SQL tuning task in the database. \n[Command Reference](cloneSqlTuningTask)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--task-name', required=True, help=u"""The name of the SQL tuning task. The name is unique per user in a database, and it is case-sensitive.""")
@cli_util.option('--original-task-id', required=True, type=click.INT, help=u"""The identifier of the SQL tuning task being cloned. This is not the [OCID]. It can be retrieved from the following endpoint [ListSqlTuningAdvisorTasks].""")
@cli_util.option('--credential-details-username', required=True, help=u"""The user name used to connect to the database.""")
@cli_util.option('--credential-details-role', required=True, type=custom_types.CliCaseInsensitiveChoice(["NORMAL", "SYSDBA"]), help=u"""The role of the database user.""")
@cli_util.option('--credential-details-password', required=True, help=u"""The database user's password encoded using BASE64 scheme.""")
@cli_util.option('--task-description', help=u"""The description of the SQL tuning task.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'SqlTuningTaskReturn'})
@cli_util.wrap_exceptions
def clone_sql_tuning_task_sql_tuning_task_password_credential_details(ctx, from_json, managed_database_id, task_name, original_task_id, credential_details_username, credential_details_role, credential_details_password, task_description):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['credentialDetails'] = {}
    _details['taskName'] = task_name
    _details['originalTaskId'] = original_task_id
    _details['credentialDetails']['username'] = credential_details_username
    _details['credentialDetails']['role'] = credential_details_role
    _details['credentialDetails']['password'] = credential_details_password

    if task_description is not None:
        _details['taskDescription'] = task_description

    _details['credentialDetails']['sqlTuningTaskCredentialType'] = 'PASSWORD'

    client = cli_util.build_client('database_management', 'sql_tuning', ctx)
    result = client.clone_sql_tuning_task(
        managed_database_id=managed_database_id,
        clone_sql_tuning_task_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('sql_tuning.drop_sql_tuning_task.command_name', 'drop-sql-tuning-task'), help=u"""Drops a SQL tuning task and its related results from the database. \n[Command Reference](dropSqlTuningTask)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--task-id', required=True, type=click.INT, help=u"""The identifier of the SQL tuning task being dropped. This is not the [OCID]. It can be retrieved from the following endpoint [ListSqlTuningAdvisorTasks].""")
@cli_util.option('--credential-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'credential-details': {'module': 'database_management', 'class': 'SqlTuningTaskCredentialDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'credential-details': {'module': 'database_management', 'class': 'SqlTuningTaskCredentialDetails'}})
@cli_util.wrap_exceptions
def drop_sql_tuning_task(ctx, from_json, managed_database_id, task_id, credential_details):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['taskId'] = task_id
    _details['credentialDetails'] = cli_util.parse_json_parameter("credential_details", credential_details)

    client = cli_util.build_client('database_management', 'sql_tuning', ctx)
    result = client.drop_sql_tuning_task(
        managed_database_id=managed_database_id,
        drop_sql_tuning_task_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('sql_tuning.drop_sql_tuning_task_sql_tuning_task_secret_credential_details.command_name', 'drop-sql-tuning-task-sql-tuning-task-secret-credential-details'), help=u"""Drops a SQL tuning task and its related results from the database. \n[Command Reference](dropSqlTuningTask)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--task-id', required=True, type=click.INT, help=u"""The identifier of the SQL tuning task being dropped. This is not the [OCID]. It can be retrieved from the following endpoint [ListSqlTuningAdvisorTasks].""")
@cli_util.option('--credential-details-username', required=True, help=u"""The user name used to connect to the database.""")
@cli_util.option('--credential-details-role', required=True, type=custom_types.CliCaseInsensitiveChoice(["NORMAL", "SYSDBA"]), help=u"""The role of the database user.""")
@cli_util.option('--credential-details-password-secret-id', required=True, help=u"""The [OCID] of the Secret where the database password is stored.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def drop_sql_tuning_task_sql_tuning_task_secret_credential_details(ctx, from_json, managed_database_id, task_id, credential_details_username, credential_details_role, credential_details_password_secret_id):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['credentialDetails'] = {}
    _details['taskId'] = task_id
    _details['credentialDetails']['username'] = credential_details_username
    _details['credentialDetails']['role'] = credential_details_role
    _details['credentialDetails']['passwordSecretId'] = credential_details_password_secret_id

    _details['credentialDetails']['sqlTuningTaskCredentialType'] = 'SECRET'

    client = cli_util.build_client('database_management', 'sql_tuning', ctx)
    result = client.drop_sql_tuning_task(
        managed_database_id=managed_database_id,
        drop_sql_tuning_task_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('sql_tuning.drop_sql_tuning_task_sql_tuning_task_password_credential_details.command_name', 'drop-sql-tuning-task-sql-tuning-task-password-credential-details'), help=u"""Drops a SQL tuning task and its related results from the database. \n[Command Reference](dropSqlTuningTask)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--task-id', required=True, type=click.INT, help=u"""The identifier of the SQL tuning task being dropped. This is not the [OCID]. It can be retrieved from the following endpoint [ListSqlTuningAdvisorTasks].""")
@cli_util.option('--credential-details-username', required=True, help=u"""The user name used to connect to the database.""")
@cli_util.option('--credential-details-role', required=True, type=custom_types.CliCaseInsensitiveChoice(["NORMAL", "SYSDBA"]), help=u"""The role of the database user.""")
@cli_util.option('--credential-details-password', required=True, help=u"""The database user's password encoded using BASE64 scheme.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def drop_sql_tuning_task_sql_tuning_task_password_credential_details(ctx, from_json, managed_database_id, task_id, credential_details_username, credential_details_role, credential_details_password):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['credentialDetails'] = {}
    _details['taskId'] = task_id
    _details['credentialDetails']['username'] = credential_details_username
    _details['credentialDetails']['role'] = credential_details_role
    _details['credentialDetails']['password'] = credential_details_password

    _details['credentialDetails']['sqlTuningTaskCredentialType'] = 'PASSWORD'

    client = cli_util.build_client('database_management', 'sql_tuning', ctx)
    result = client.drop_sql_tuning_task(
        managed_database_id=managed_database_id,
        drop_sql_tuning_task_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('sql_tuning.get_execution_plan_stats_comparision.command_name', 'get-execution-plan-stats-comparision'), help=u"""Retrieves a comparison of the existing SQL execution plan and a new plan. A SQL tuning task may suggest a new execution plan for a SQL, and this API retrieves the comparison report of the statistics of the two plans. \n[Command Reference](getExecutionPlanStatsComparision)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--sql-tuning-advisor-task-id', required=True, type=click.INT, help=u"""The SQL tuning task identifier. This is not the [OCID].""")
@cli_util.option('--sql-object-id', required=True, type=click.INT, help=u"""The SQL object ID for the SQL tuning task. This is not the [OCID].""")
@cli_util.option('--execution-id', required=True, type=click.INT, help=u"""The execution ID for an execution of a SQL tuning task. This is not the [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'ExecutionPlanStatsComparision'})
@cli_util.wrap_exceptions
def get_execution_plan_stats_comparision(ctx, from_json, managed_database_id, sql_tuning_advisor_task_id, sql_object_id, execution_id):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(sql_tuning_advisor_task_id, six.string_types) and len(sql_tuning_advisor_task_id.strip()) == 0:
        raise click.UsageError('Parameter --sql-tuning-advisor-task-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'sql_tuning', ctx)
    result = client.get_execution_plan_stats_comparision(
        managed_database_id=managed_database_id,
        sql_tuning_advisor_task_id=sql_tuning_advisor_task_id,
        sql_object_id=sql_object_id,
        execution_id=execution_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('sql_tuning.get_sql_execution_plan.command_name', 'get-sql-execution-plan'), help=u"""Retrieves a SQL execution plan for the SQL being tuned. \n[Command Reference](getSqlExecutionPlan)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--sql-tuning-advisor-task-id', required=True, type=click.INT, help=u"""The SQL tuning task identifier. This is not the [OCID].""")
@cli_util.option('--sql-object-id', required=True, type=click.INT, help=u"""The SQL object ID for the SQL tuning task. This is not the [OCID].""")
@cli_util.option('--attribute', required=True, type=custom_types.CliCaseInsensitiveChoice(["ORIGINAL", "ORIGINAL_WITH_ADJUSTED_COST", "USING_SQL_PROFILE", "USING_NEW_INDICES"]), help=u"""The attribute of the SQL execution plan.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'SqlTuningAdvisorTaskSqlExecutionPlan'})
@cli_util.wrap_exceptions
def get_sql_execution_plan(ctx, from_json, managed_database_id, sql_tuning_advisor_task_id, sql_object_id, attribute):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(sql_tuning_advisor_task_id, six.string_types) and len(sql_tuning_advisor_task_id.strip()) == 0:
        raise click.UsageError('Parameter --sql-tuning-advisor-task-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'sql_tuning', ctx)
    result = client.get_sql_execution_plan(
        managed_database_id=managed_database_id,
        sql_tuning_advisor_task_id=sql_tuning_advisor_task_id,
        sql_object_id=sql_object_id,
        attribute=attribute,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('sql_tuning.get_sql_tuning_advisor_task_summary_report.command_name', 'get-sql-tuning-advisor-task-summary-report'), help=u"""Gets the summary report for the specified SQL Tuning Advisor task. \n[Command Reference](getSqlTuningAdvisorTaskSummaryReport)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--sql-tuning-advisor-task-id', required=True, type=click.INT, help=u"""The SQL tuning task identifier. This is not the [OCID].""")
@cli_util.option('--search-period', type=custom_types.CliCaseInsensitiveChoice(["LAST_24HR", "LAST_7DAY", "LAST_31DAY", "SINCE_LAST", "ALL"]), help=u"""How far back the API will search for begin and end exec id. Unused if neither exec ids nor time filter query params are supplied. This is applicable only for Auto SQL Tuning tasks.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to query parameter to filter the timestamp. This is applicable only for Auto SQL Tuning tasks.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to query parameter to filter the timestamp. This is applicable only for Auto SQL Tuning tasks.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--begin-exec-id-greater-than-or-equal-to', type=click.INT, help=u"""The optional greater than or equal to filter on the execution ID related to a specific SQL Tuning Advisor task. This is applicable only for Auto SQL Tuning tasks.""")
@cli_util.option('--end-exec-id-less-than-or-equal-to', type=click.INT, help=u"""The optional less than or equal to query parameter to filter on the execution ID related to a specific SQL Tuning Advisor task. This is applicable only for Auto SQL Tuning tasks.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'SqlTuningAdvisorTaskSummaryReport'})
@cli_util.wrap_exceptions
def get_sql_tuning_advisor_task_summary_report(ctx, from_json, managed_database_id, sql_tuning_advisor_task_id, search_period, time_greater_than_or_equal_to, time_less_than_or_equal_to, begin_exec_id_greater_than_or_equal_to, end_exec_id_less_than_or_equal_to):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(sql_tuning_advisor_task_id, six.string_types) and len(sql_tuning_advisor_task_id.strip()) == 0:
        raise click.UsageError('Parameter --sql-tuning-advisor-task-id cannot be whitespace or empty string')

    kwargs = {}
    if search_period is not None:
        kwargs['search_period'] = search_period
    if time_greater_than_or_equal_to is not None:
        kwargs['time_greater_than_or_equal_to'] = time_greater_than_or_equal_to
    if time_less_than_or_equal_to is not None:
        kwargs['time_less_than_or_equal_to'] = time_less_than_or_equal_to
    if begin_exec_id_greater_than_or_equal_to is not None:
        kwargs['begin_exec_id_greater_than_or_equal_to'] = begin_exec_id_greater_than_or_equal_to
    if end_exec_id_less_than_or_equal_to is not None:
        kwargs['end_exec_id_less_than_or_equal_to'] = end_exec_id_less_than_or_equal_to
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'sql_tuning', ctx)
    result = client.get_sql_tuning_advisor_task_summary_report(
        managed_database_id=managed_database_id,
        sql_tuning_advisor_task_id=sql_tuning_advisor_task_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('sql_tuning.list_sql_tuning_advisor_task_findings.command_name', 'list-sql-tuning-advisor-task-findings'), help=u"""Gets an array of the details of the findings that match specific filters. \n[Command Reference](listSqlTuningAdvisorTaskFindings)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--sql-tuning-advisor-task-id', required=True, type=click.INT, help=u"""The SQL tuning task identifier. This is not the [OCID].""")
@cli_util.option('--begin-exec-id', type=click.INT, help=u"""The optional greater than or equal to filter on the execution ID related to a specific SQL Tuning Advisor task.""")
@cli_util.option('--end-exec-id', type=click.INT, help=u"""The optional less than or equal to query parameter to filter on the execution ID related to a specific SQL Tuning Advisor task.""")
@cli_util.option('--search-period', type=custom_types.CliCaseInsensitiveChoice(["LAST_24HR", "LAST_7DAY", "LAST_31DAY", "SINCE_LAST", "ALL"]), help=u"""The search period during which the API will search for begin and end exec id, if not supplied. Unused if beginExecId and endExecId optional query params are both supplied.""")
@cli_util.option('--finding-filter', type=custom_types.CliCaseInsensitiveChoice(["none", "FINDINGS", "NOFINDINGS", "ERRORS", "PROFILES", "INDICES", "STATS", "RESTRUCTURE", "ALTERNATIVE", "AUTO_PROFILES", "OTHER_PROFILES"]), help=u"""The filter used to display specific findings in the report.""")
@cli_util.option('--stats-hash-filter', help=u"""The hash value of the object for the statistic finding search.""")
@cli_util.option('--index-hash-filter', help=u"""The hash value of the index table name.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["DBTIME_BENEFIT", "PARSING_SCHEMA", "SQL_ID", "STATS", "PROFILES", "SQL_BENEFIT", "DATE", "INDICES", "RESTRUCTURE", "ALTERNATIVE", "MISC", "ERROR", "TIMEOUTS"]), help=u"""The possible sortBy values of an object's recommendations.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the default order.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'SqlTuningAdvisorTaskFindingCollection'})
@cli_util.wrap_exceptions
def list_sql_tuning_advisor_task_findings(ctx, from_json, all_pages, page_size, managed_database_id, sql_tuning_advisor_task_id, begin_exec_id, end_exec_id, search_period, finding_filter, stats_hash_filter, index_hash_filter, sort_by, sort_order, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(sql_tuning_advisor_task_id, six.string_types) and len(sql_tuning_advisor_task_id.strip()) == 0:
        raise click.UsageError('Parameter --sql-tuning-advisor-task-id cannot be whitespace or empty string')

    kwargs = {}
    if begin_exec_id is not None:
        kwargs['begin_exec_id'] = begin_exec_id
    if end_exec_id is not None:
        kwargs['end_exec_id'] = end_exec_id
    if search_period is not None:
        kwargs['search_period'] = search_period
    if finding_filter is not None:
        kwargs['finding_filter'] = finding_filter
    if stats_hash_filter is not None:
        kwargs['stats_hash_filter'] = stats_hash_filter
    if index_hash_filter is not None:
        kwargs['index_hash_filter'] = index_hash_filter
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'sql_tuning', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_sql_tuning_advisor_task_findings,
            managed_database_id=managed_database_id,
            sql_tuning_advisor_task_id=sql_tuning_advisor_task_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_sql_tuning_advisor_task_findings,
            limit,
            page_size,
            managed_database_id=managed_database_id,
            sql_tuning_advisor_task_id=sql_tuning_advisor_task_id,
            **kwargs
        )
    else:
        result = client.list_sql_tuning_advisor_task_findings(
            managed_database_id=managed_database_id,
            sql_tuning_advisor_task_id=sql_tuning_advisor_task_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('sql_tuning.list_sql_tuning_advisor_task_recommendations.command_name', 'list-sql-tuning-advisor-task-recommendations'), help=u"""Gets the findings and possible actions for a given object in a SQL tuning task. The task ID and object ID are used to retrieve the findings and recommendations. \n[Command Reference](listSqlTuningAdvisorTaskRecommendations)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--sql-tuning-advisor-task-id', required=True, type=click.INT, help=u"""The SQL tuning task identifier. This is not the [OCID].""")
@cli_util.option('--sql-object-id', required=True, type=click.INT, help=u"""The SQL object ID for the SQL tuning task. This is not the [OCID].""")
@cli_util.option('--execution-id', required=True, type=click.INT, help=u"""The execution ID for an execution of a SQL tuning task. This is not the [OCID].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["RECOMMENDATION_TYPE", "BENEFIT"]), help=u"""The possible sortBy values of an object's recommendations.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the default order.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'SqlTuningAdvisorTaskRecommendationCollection'})
@cli_util.wrap_exceptions
def list_sql_tuning_advisor_task_recommendations(ctx, from_json, all_pages, page_size, managed_database_id, sql_tuning_advisor_task_id, sql_object_id, execution_id, sort_by, sort_order, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(sql_tuning_advisor_task_id, six.string_types) and len(sql_tuning_advisor_task_id.strip()) == 0:
        raise click.UsageError('Parameter --sql-tuning-advisor-task-id cannot be whitespace or empty string')

    kwargs = {}
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'sql_tuning', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_sql_tuning_advisor_task_recommendations,
            managed_database_id=managed_database_id,
            sql_tuning_advisor_task_id=sql_tuning_advisor_task_id,
            sql_object_id=sql_object_id,
            execution_id=execution_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_sql_tuning_advisor_task_recommendations,
            limit,
            page_size,
            managed_database_id=managed_database_id,
            sql_tuning_advisor_task_id=sql_tuning_advisor_task_id,
            sql_object_id=sql_object_id,
            execution_id=execution_id,
            **kwargs
        )
    else:
        result = client.list_sql_tuning_advisor_task_recommendations(
            managed_database_id=managed_database_id,
            sql_tuning_advisor_task_id=sql_tuning_advisor_task_id,
            sql_object_id=sql_object_id,
            execution_id=execution_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('sql_tuning.list_sql_tuning_advisor_tasks.command_name', 'list-sql-tuning-advisor-tasks'), help=u"""Lists the SQL Tuning Advisor tasks for the specified Managed Database. \n[Command Reference](listSqlTuningAdvisorTasks)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--name', help=u"""The optional query parameter to filter the SQL Tuning Advisor task list by name.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["INITIAL", "EXECUTING", "INTERRUPTED", "COMPLETED", "ERROR"]), help=u"""The optional query parameter to filter the SQL Tuning Advisor task list by status.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["NAME", "START_TIME"]), help=u"""The option to sort the SQL Tuning Advisor task summary data.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the default order.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'SqlTuningAdvisorTaskCollection'})
@cli_util.wrap_exceptions
def list_sql_tuning_advisor_tasks(ctx, from_json, all_pages, page_size, managed_database_id, name, status, time_greater_than_or_equal_to, time_less_than_or_equal_to, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if status is not None:
        kwargs['status'] = status
    if time_greater_than_or_equal_to is not None:
        kwargs['time_greater_than_or_equal_to'] = time_greater_than_or_equal_to
    if time_less_than_or_equal_to is not None:
        kwargs['time_less_than_or_equal_to'] = time_less_than_or_equal_to
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'sql_tuning', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_sql_tuning_advisor_tasks,
            managed_database_id=managed_database_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_sql_tuning_advisor_tasks,
            limit,
            page_size,
            managed_database_id=managed_database_id,
            **kwargs
        )
    else:
        result = client.list_sql_tuning_advisor_tasks(
            managed_database_id=managed_database_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('sql_tuning.start_sql_tuning_task.command_name', 'start-sql-tuning-task'), help=u"""Starts a SQL tuning task for a given set of SQL statements from the active session history top SQL statements. \n[Command Reference](startSqlTuningTask)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--task-name', required=True, help=u"""The name of the SQL tuning task. The name is unique per user in a database, and it is case-sensitive.""")
@cli_util.option('--credential-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--total-time-limit-in-minutes', required=True, type=click.INT, help=u"""The time limit for running the SQL tuning task.""")
@cli_util.option('--scope', required=True, type=custom_types.CliCaseInsensitiveChoice(["LIMITED", "COMPREHENSIVE"]), help=u"""The scope for the SQL tuning task. For LIMITED scope, the SQL profile recommendation is excluded, so the task is executed faster. For COMPREHENSIVE scope, the SQL profile recommendation is included.""")
@cli_util.option('--sql-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The array of the details of SQL statement on which tuning is performed.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--time-started', required=True, type=custom_types.CLI_DATETIME, help=u"""The start time of the period in which SQL statements are running.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-ended', required=True, type=custom_types.CLI_DATETIME, help=u"""The end time of the period in which SQL statements are running.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--task-description', help=u"""The description of the SQL tuning task.""")
@cli_util.option('--statement-time-limit-in-minutes', type=click.INT, help=u"""The time limit per SQL statement (in minutes). This is for a task with the COMPREHENSIVE scope. The time limit per SQL statement should not be more than the total time limit.""")
@json_skeleton_utils.get_cli_json_input_option({'credential-details': {'module': 'database_management', 'class': 'SqlTuningTaskCredentialDetails'}, 'sql-details': {'module': 'database_management', 'class': 'list[SqlTuningTaskSqlDetail]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'credential-details': {'module': 'database_management', 'class': 'SqlTuningTaskCredentialDetails'}, 'sql-details': {'module': 'database_management', 'class': 'list[SqlTuningTaskSqlDetail]'}}, output_type={'module': 'database_management', 'class': 'SqlTuningTaskReturn'})
@cli_util.wrap_exceptions
def start_sql_tuning_task(ctx, from_json, managed_database_id, task_name, credential_details, total_time_limit_in_minutes, scope, sql_details, time_started, time_ended, task_description, statement_time_limit_in_minutes):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['taskName'] = task_name
    _details['credentialDetails'] = cli_util.parse_json_parameter("credential_details", credential_details)
    _details['totalTimeLimitInMinutes'] = total_time_limit_in_minutes
    _details['scope'] = scope
    _details['sqlDetails'] = cli_util.parse_json_parameter("sql_details", sql_details)
    _details['timeStarted'] = time_started
    _details['timeEnded'] = time_ended

    if task_description is not None:
        _details['taskDescription'] = task_description

    if statement_time_limit_in_minutes is not None:
        _details['statementTimeLimitInMinutes'] = statement_time_limit_in_minutes

    client = cli_util.build_client('database_management', 'sql_tuning', ctx)
    result = client.start_sql_tuning_task(
        managed_database_id=managed_database_id,
        start_sql_tuning_task_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('sql_tuning.start_sql_tuning_task_sql_tuning_task_secret_credential_details.command_name', 'start-sql-tuning-task-sql-tuning-task-secret-credential-details'), help=u"""Starts a SQL tuning task for a given set of SQL statements from the active session history top SQL statements. \n[Command Reference](startSqlTuningTask)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--task-name', required=True, help=u"""The name of the SQL tuning task. The name is unique per user in a database, and it is case-sensitive.""")
@cli_util.option('--total-time-limit-in-minutes', required=True, type=click.INT, help=u"""The time limit for running the SQL tuning task.""")
@cli_util.option('--scope', required=True, type=custom_types.CliCaseInsensitiveChoice(["LIMITED", "COMPREHENSIVE"]), help=u"""The scope for the SQL tuning task. For LIMITED scope, the SQL profile recommendation is excluded, so the task is executed faster. For COMPREHENSIVE scope, the SQL profile recommendation is included.""")
@cli_util.option('--sql-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The array of the details of SQL statement on which tuning is performed.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--time-started', required=True, type=custom_types.CLI_DATETIME, help=u"""The start time of the period in which SQL statements are running.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-ended', required=True, type=custom_types.CLI_DATETIME, help=u"""The end time of the period in which SQL statements are running.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--credential-details-username', required=True, help=u"""The user name used to connect to the database.""")
@cli_util.option('--credential-details-role', required=True, type=custom_types.CliCaseInsensitiveChoice(["NORMAL", "SYSDBA"]), help=u"""The role of the database user.""")
@cli_util.option('--credential-details-password-secret-id', required=True, help=u"""The [OCID] of the Secret where the database password is stored.""")
@cli_util.option('--task-description', help=u"""The description of the SQL tuning task.""")
@cli_util.option('--statement-time-limit-in-minutes', type=click.INT, help=u"""The time limit per SQL statement (in minutes). This is for a task with the COMPREHENSIVE scope. The time limit per SQL statement should not be more than the total time limit.""")
@json_skeleton_utils.get_cli_json_input_option({'sql-details': {'module': 'database_management', 'class': 'list[SqlTuningTaskSqlDetail]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'sql-details': {'module': 'database_management', 'class': 'list[SqlTuningTaskSqlDetail]'}}, output_type={'module': 'database_management', 'class': 'SqlTuningTaskReturn'})
@cli_util.wrap_exceptions
def start_sql_tuning_task_sql_tuning_task_secret_credential_details(ctx, from_json, managed_database_id, task_name, total_time_limit_in_minutes, scope, sql_details, time_started, time_ended, credential_details_username, credential_details_role, credential_details_password_secret_id, task_description, statement_time_limit_in_minutes):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['credentialDetails'] = {}
    _details['taskName'] = task_name
    _details['totalTimeLimitInMinutes'] = total_time_limit_in_minutes
    _details['scope'] = scope
    _details['sqlDetails'] = cli_util.parse_json_parameter("sql_details", sql_details)
    _details['timeStarted'] = time_started
    _details['timeEnded'] = time_ended
    _details['credentialDetails']['username'] = credential_details_username
    _details['credentialDetails']['role'] = credential_details_role
    _details['credentialDetails']['passwordSecretId'] = credential_details_password_secret_id

    if task_description is not None:
        _details['taskDescription'] = task_description

    if statement_time_limit_in_minutes is not None:
        _details['statementTimeLimitInMinutes'] = statement_time_limit_in_minutes

    _details['credentialDetails']['sqlTuningTaskCredentialType'] = 'SECRET'

    client = cli_util.build_client('database_management', 'sql_tuning', ctx)
    result = client.start_sql_tuning_task(
        managed_database_id=managed_database_id,
        start_sql_tuning_task_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('sql_tuning.start_sql_tuning_task_sql_tuning_task_password_credential_details.command_name', 'start-sql-tuning-task-sql-tuning-task-password-credential-details'), help=u"""Starts a SQL tuning task for a given set of SQL statements from the active session history top SQL statements. \n[Command Reference](startSqlTuningTask)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--task-name', required=True, help=u"""The name of the SQL tuning task. The name is unique per user in a database, and it is case-sensitive.""")
@cli_util.option('--total-time-limit-in-minutes', required=True, type=click.INT, help=u"""The time limit for running the SQL tuning task.""")
@cli_util.option('--scope', required=True, type=custom_types.CliCaseInsensitiveChoice(["LIMITED", "COMPREHENSIVE"]), help=u"""The scope for the SQL tuning task. For LIMITED scope, the SQL profile recommendation is excluded, so the task is executed faster. For COMPREHENSIVE scope, the SQL profile recommendation is included.""")
@cli_util.option('--sql-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The array of the details of SQL statement on which tuning is performed.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--time-started', required=True, type=custom_types.CLI_DATETIME, help=u"""The start time of the period in which SQL statements are running.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-ended', required=True, type=custom_types.CLI_DATETIME, help=u"""The end time of the period in which SQL statements are running.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--credential-details-username', required=True, help=u"""The user name used to connect to the database.""")
@cli_util.option('--credential-details-role', required=True, type=custom_types.CliCaseInsensitiveChoice(["NORMAL", "SYSDBA"]), help=u"""The role of the database user.""")
@cli_util.option('--credential-details-password', required=True, help=u"""The database user's password encoded using BASE64 scheme.""")
@cli_util.option('--task-description', help=u"""The description of the SQL tuning task.""")
@cli_util.option('--statement-time-limit-in-minutes', type=click.INT, help=u"""The time limit per SQL statement (in minutes). This is for a task with the COMPREHENSIVE scope. The time limit per SQL statement should not be more than the total time limit.""")
@json_skeleton_utils.get_cli_json_input_option({'sql-details': {'module': 'database_management', 'class': 'list[SqlTuningTaskSqlDetail]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'sql-details': {'module': 'database_management', 'class': 'list[SqlTuningTaskSqlDetail]'}}, output_type={'module': 'database_management', 'class': 'SqlTuningTaskReturn'})
@cli_util.wrap_exceptions
def start_sql_tuning_task_sql_tuning_task_password_credential_details(ctx, from_json, managed_database_id, task_name, total_time_limit_in_minutes, scope, sql_details, time_started, time_ended, credential_details_username, credential_details_role, credential_details_password, task_description, statement_time_limit_in_minutes):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['credentialDetails'] = {}
    _details['taskName'] = task_name
    _details['totalTimeLimitInMinutes'] = total_time_limit_in_minutes
    _details['scope'] = scope
    _details['sqlDetails'] = cli_util.parse_json_parameter("sql_details", sql_details)
    _details['timeStarted'] = time_started
    _details['timeEnded'] = time_ended
    _details['credentialDetails']['username'] = credential_details_username
    _details['credentialDetails']['role'] = credential_details_role
    _details['credentialDetails']['password'] = credential_details_password

    if task_description is not None:
        _details['taskDescription'] = task_description

    if statement_time_limit_in_minutes is not None:
        _details['statementTimeLimitInMinutes'] = statement_time_limit_in_minutes

    _details['credentialDetails']['sqlTuningTaskCredentialType'] = 'PASSWORD'

    client = cli_util.build_client('database_management', 'sql_tuning', ctx)
    result = client.start_sql_tuning_task(
        managed_database_id=managed_database_id,
        start_sql_tuning_task_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
