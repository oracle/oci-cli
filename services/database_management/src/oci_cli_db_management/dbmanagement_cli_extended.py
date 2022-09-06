# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
import six
from services.database_management.src.oci_cli_db_management.generated import dbmanagement_cli
from services.database_management.src.oci_cli_database_management.generated import database_management_service_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci database-management database-fleet-health-metrics -> oci database-management fleet-health-metrics
cli_util.rename_command(dbmanagement_cli, dbmanagement_cli.db_management_root_group, dbmanagement_cli.database_fleet_health_metrics_group, "fleet-health-metrics")


# oci database-management database-home-metrics -> oci database-management summary-metrics
cli_util.rename_command(dbmanagement_cli, dbmanagement_cli.db_management_root_group, dbmanagement_cli.database_home_metrics_group, "summary-metrics")


# oci database-management job create-job-create-sql-job-details -> oci database-management job create-sql-job
cli_util.rename_command(dbmanagement_cli, dbmanagement_cli.job_group, dbmanagement_cli.create_job_create_sql_job_details, "create-sql-job")


# Remove create from oci database-management job
dbmanagement_cli.job_group.commands.pop(dbmanagement_cli.create_job.name)


# Remove create-job-object-storage-job-execution-result-location from oci database-management job
dbmanagement_cli.job_group.commands.pop(dbmanagement_cli.create_job_object_storage_job_execution_result_location.name)


# Fix for handling inst-nums parameter
dbmanagement_cli.managed_database_group.commands.pop(dbmanagement_cli.get_awr_db_report.name)


@dbmanagement_cli.managed_database_group.command(name=cli_util.override('database_management.get_awr_db_report.command_name', 'get-awr-db-report'), help=u"""Gets the AWR database report for one database. \n[Command Reference](getAwrDbReport)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--awr-db-id', required=True, help=u"""Exact match filter on the internal identity of the database.""")
@cli_util.option('--inst-nums', multiple=True, help=u"""Optional multiple value filter to match the database instance numbers exactly.""")
@cli_util.option('--begin-sn-id-greater-than-or-equal-to', type=click.INT, help=u"""The optional greater than or equal to filter on the snapshot identity.""")
@cli_util.option('--end-sn-id-less-than-or-equal-to', type=click.INT, help=u"""The optional less than or equal to filter on the snapshot identity.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to filter on the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to filter on the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--report-type', type=custom_types.CliCaseInsensitiveChoice(["AWR", "ASH"]), help=u"""Exact match filter on the report types of AWR database.""")
@cli_util.option('--container-id', type=click.INT, help=u"""The exact match filter on the identity of the database container. The identity can be retrieved from the endpoint /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges.""")
@cli_util.option('--report-format', type=custom_types.CliCaseInsensitiveChoice(["HTML", "TEXT"]), help=u"""The format of the AWR report content.""")
@json_skeleton_utils.get_cli_json_input_option({'inst-nums': {'module': 'database_management', 'class': 'list[integer]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'inst-nums': {'module': 'database_management', 'class': 'list[integer]'}}, output_type={'module': 'database_management', 'class': 'AwrDbReport'})
@cli_util.wrap_exceptions
def get_awr_db_report(ctx, from_json, managed_database_id, awr_db_id, inst_nums, begin_sn_id_greater_than_or_equal_to, end_sn_id_less_than_or_equal_to, time_greater_than_or_equal_to, time_less_than_or_equal_to, report_type, container_id, report_format):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(awr_db_id, six.string_types) and len(awr_db_id.strip()) == 0:
        raise click.UsageError('Parameter --awr-db-id cannot be whitespace or empty string')

    kwargs = {}
    if inst_nums is not None and len(inst_nums) > 0:
        kwargs['inst_nums'] = list(map(str, inst_nums))
    if begin_sn_id_greater_than_or_equal_to is not None:
        kwargs['begin_sn_id_greater_than_or_equal_to'] = begin_sn_id_greater_than_or_equal_to
    if end_sn_id_less_than_or_equal_to is not None:
        kwargs['end_sn_id_less_than_or_equal_to'] = end_sn_id_less_than_or_equal_to
    if time_greater_than_or_equal_to is not None:
        kwargs['time_greater_than_or_equal_to'] = time_greater_than_or_equal_to
    if time_less_than_or_equal_to is not None:
        kwargs['time_less_than_or_equal_to'] = time_less_than_or_equal_to
    if report_type is not None:
        kwargs['report_type'] = report_type
    if container_id is not None:
        kwargs['container_id'] = container_id
    if report_format is not None:
        kwargs['report_format'] = report_format
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.get_awr_db_report(
        managed_database_id=managed_database_id,
        awr_db_id=awr_db_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


# oci database-management db-management-private-endpoint -> oci database-management private-endpoint
cli_util.rename_command(dbmanagement_cli, dbmanagement_cli.db_management_root_group, dbmanagement_cli.db_management_private_endpoint_group, "private-endpoint")


@cli_util.copy_params_from_generated_command(dbmanagement_cli.change_db_management_private_endpoint_compartment, params_to_exclude=['db_management_private_endpoint_id'])
@dbmanagement_cli.db_management_private_endpoint_group.command(name=dbmanagement_cli.change_db_management_private_endpoint_compartment.name, help=dbmanagement_cli.change_db_management_private_endpoint_compartment.help)
@cli_util.option('--private-endpoint-id', required=True, help=u"""The [OCID] of the Database Management private endpoint. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_db_management_private_endpoint_compartment_extended(ctx, **kwargs):
    if 'private_endpoint_id' in kwargs:
        kwargs['db_management_private_endpoint_id'] = kwargs['private_endpoint_id']
        kwargs.pop('private_endpoint_id')

    ctx.invoke(dbmanagement_cli.change_db_management_private_endpoint_compartment, **kwargs)


@cli_util.copy_params_from_generated_command(dbmanagement_cli.delete_db_management_private_endpoint, params_to_exclude=['db_management_private_endpoint_id'])
@dbmanagement_cli.db_management_private_endpoint_group.command(name=dbmanagement_cli.delete_db_management_private_endpoint.name, help=dbmanagement_cli.delete_db_management_private_endpoint.help)
@cli_util.option('--private-endpoint-id', required=True, help=u"""The [OCID] of the Database Management private endpoint. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_db_management_private_endpoint_extended(ctx, **kwargs):
    if 'private_endpoint_id' in kwargs:
        kwargs['db_management_private_endpoint_id'] = kwargs['private_endpoint_id']
        kwargs.pop('private_endpoint_id')

    ctx.invoke(dbmanagement_cli.delete_db_management_private_endpoint, **kwargs)


@cli_util.copy_params_from_generated_command(dbmanagement_cli.get_db_management_private_endpoint, params_to_exclude=['db_management_private_endpoint_id'])
@dbmanagement_cli.db_management_private_endpoint_group.command(name=dbmanagement_cli.get_db_management_private_endpoint.name, help=dbmanagement_cli.get_db_management_private_endpoint.help)
@cli_util.option('--private-endpoint-id', required=True, help=u"""The [OCID] of the Database Management private endpoint. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'DbManagementPrivateEndpoint'})
@cli_util.wrap_exceptions
def get_db_management_private_endpoint_extended(ctx, **kwargs):
    if 'private_endpoint_id' in kwargs:
        kwargs['db_management_private_endpoint_id'] = kwargs['private_endpoint_id']
        kwargs.pop('private_endpoint_id')

    ctx.invoke(dbmanagement_cli.get_db_management_private_endpoint, **kwargs)


@cli_util.copy_params_from_generated_command(dbmanagement_cli.update_db_management_private_endpoint, params_to_exclude=['db_management_private_endpoint_id'])
@dbmanagement_cli.db_management_private_endpoint_group.command(name=dbmanagement_cli.update_db_management_private_endpoint.name, help=dbmanagement_cli.update_db_management_private_endpoint.help)
@cli_util.option('--private-endpoint-id', required=True, help=u"""The [OCID] of the Database Management private endpoint. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'nsg-ids': {'module': 'database_management', 'class': 'list[string]'}}, output_type={'module': 'database_management', 'class': 'DbManagementPrivateEndpoint'})
@cli_util.wrap_exceptions
def update_db_management_private_endpoint_extended(ctx, **kwargs):
    if 'private_endpoint_id' in kwargs:
        kwargs['db_management_private_endpoint_id'] = kwargs['private_endpoint_id']
        kwargs.pop('private_endpoint_id')

    ctx.invoke(dbmanagement_cli.update_db_management_private_endpoint, **kwargs)


# oci database-management job update-job-object-storage-job-execution-result-location -> oci database-management job update-result-location
cli_util.rename_command(dbmanagement_cli, dbmanagement_cli.job_group, dbmanagement_cli.update_job_object_storage_job_execution_result_location, "update-result-location")


# oci database-management job update-job-update-sql-job-details -> oci database-management job update-sql-job-details
cli_util.rename_command(dbmanagement_cli, dbmanagement_cli.job_group, dbmanagement_cli.update_job_update_sql_job_details, "update-sql-job-details")


# oci database-management job-executions-status-summary-collection -> oci database-management job-executions-status
cli_util.rename_command(dbmanagement_cli, dbmanagement_cli.db_management_root_group, dbmanagement_cli.job_executions_status_summary_collection_group, "job-executions-status")


# oci database-management job-executions-status-summary-collection summarize-job-executions-statuses -> oci database-management job-executions-status-summary-collection summarize
cli_util.rename_command(dbmanagement_cli, dbmanagement_cli.job_executions_status_summary_collection_group, dbmanagement_cli.summarize_job_executions_statuses, "summarize")


@cli_util.copy_params_from_generated_command(dbmanagement_cli.update_job_object_storage_job_execution_result_location, params_to_exclude=['result_location_bucket_name', 'result_location_namespace_name'])
@dbmanagement_cli.job_group.command(name=dbmanagement_cli.update_job_object_storage_job_execution_result_location.name, help=dbmanagement_cli.update_job_object_storage_job_execution_result_location.help)
@cli_util.option('--bucket-name', help=u"""The name of the bucket used for job execution result storage.""")
@cli_util.option('--namespace-name', help=u"""The Object Storage namespace used for job execution result storage.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'schedule-details': {'module': 'database_management', 'class': 'JobScheduleDetails'}}, output_type={'module': 'database_management', 'class': 'Job'})
@cli_util.wrap_exceptions
def update_job_object_storage_job_execution_result_location_extended(ctx, **kwargs):
    if 'bucket_name' in kwargs:
        kwargs['result_location_bucket_name'] = kwargs['bucket_name']
        kwargs.pop('bucket_name')

    if 'namespace_name' in kwargs:
        kwargs['result_location_namespace_name'] = kwargs['namespace_name']
        kwargs.pop('namespace_name')

    ctx.invoke(dbmanagement_cli.update_job_object_storage_job_execution_result_location, **kwargs)


@cli_util.copy_params_from_generated_command(dbmanagement_cli.list_associated_databases, params_to_exclude=['db_management_private_endpoint_id'])
@dbmanagement_cli.associated_database_summary_group.command(name=dbmanagement_cli.list_associated_databases.name, help=dbmanagement_cli.list_associated_databases.help)
@cli_util.option('--private-endpoint-id', required=True, help=u"""The [OCID] of the Database Management private endpoint. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'AssociatedDatabaseCollection'})
@cli_util.wrap_exceptions
def list_associated_databases_extended(ctx, **kwargs):
    if 'private_endpoint_id' in kwargs:
        kwargs['db_management_private_endpoint_id'] = kwargs['private_endpoint_id']
        kwargs.pop('private_endpoint_id')

    ctx.invoke(dbmanagement_cli.list_associated_databases, **kwargs)


# oci database-management user get -> oci database-management user get-user
# cli_util.rename_command(dbmanagement_cli, dbmanagement_cli.user_group, dbmanagement_cli.get_user, "get-user")

# oci database-management user get-user -> oci database-management managed-database get-user
# dbmanagement_cli.db_management_root_group.commands.pop(dbmanagement_cli.user_group.name)
dbmanagement_cli.managed_database_group.add_command(dbmanagement_cli.get_user)


# Move commands under 'oci database-management db-management' -> 'oci database-management'
database_management_service_cli.database_management_service_group.commands.pop(dbmanagement_cli.db_management_root_group.name)
database_management_service_cli.database_management_service_group.add_command(dbmanagement_cli.cluster_cache_metric_group)
database_management_service_cli.database_management_service_group.add_command(dbmanagement_cli.work_request_log_entry_group)
database_management_service_cli.database_management_service_group.add_command(dbmanagement_cli.managed_database_group_group)
database_management_service_cli.database_management_service_group.add_command(dbmanagement_cli.pdb_metrics_group)
database_management_service_cli.database_management_service_group.add_command(dbmanagement_cli.work_request_group)
database_management_service_cli.database_management_service_group.add_command(dbmanagement_cli.database_home_metrics_group)
database_management_service_cli.database_management_service_group.add_command(dbmanagement_cli.database_fleet_health_metrics_group)
database_management_service_cli.database_management_service_group.add_command(dbmanagement_cli.tablespace_group)
database_management_service_cli.database_management_service_group.add_command(dbmanagement_cli.work_request_error_group)
database_management_service_cli.database_management_service_group.add_command(dbmanagement_cli.db_management_private_endpoint_group)
database_management_service_cli.database_management_service_group.add_command(dbmanagement_cli.job_executions_status_summary_collection_group)
database_management_service_cli.database_management_service_group.add_command(dbmanagement_cli.managed_database_group)
database_management_service_cli.database_management_service_group.add_command(dbmanagement_cli.job_run_group)
database_management_service_cli.database_management_service_group.add_command(dbmanagement_cli.job_execution_group)
database_management_service_cli.database_management_service_group.add_command(dbmanagement_cli.associated_database_summary_group)
database_management_service_cli.database_management_service_group.add_command(dbmanagement_cli.job_group)
database_management_service_cli.database_management_service_group.add_command(dbmanagement_cli.preferred_credential_group)
# database_management_service_cli.database_management_service_group.add_command(dbmanagement_cli.user_group)


# oci database-management tablespace drop-tablespace-tablespace-admin-password-credential-details -> oci database-management tablespace drop-with-pwd
cli_util.rename_command(dbmanagement_cli, dbmanagement_cli.tablespace_group, dbmanagement_cli.drop_tablespace_tablespace_admin_password_credential_details, "drop-with-pwd")


# oci database-management tablespace drop-tablespace-tablespace-admin-secret-credential-details -> oci database-management tablespace drop-with-secret
cli_util.rename_command(dbmanagement_cli, dbmanagement_cli.tablespace_group, dbmanagement_cli.drop_tablespace_tablespace_admin_secret_credential_details, "drop-with-secret")


# oci database-management tablespace remove-data-file-tablespace-admin-password-credential-details -> oci database-management tablespace remove-datafile-with-pwd
cli_util.rename_command(dbmanagement_cli, dbmanagement_cli.tablespace_group, dbmanagement_cli.remove_data_file_tablespace_admin_password_credential_details, "remove-datafile-with-pwd")


# oci database-management tablespace remove-data-file-tablespace-admin-secret-credential-details -> oci database-management tablespace remove-datafile-with-secret
cli_util.rename_command(dbmanagement_cli, dbmanagement_cli.tablespace_group, dbmanagement_cli.remove_data_file_tablespace_admin_secret_credential_details, "remove-datafile-with-secret")


@cli_util.copy_params_from_generated_command(dbmanagement_cli.drop_tablespace_tablespace_admin_password_credential_details, params_to_exclude=['credential_details_password', 'credential_details_role', 'credential_details_username'])
@dbmanagement_cli.tablespace_group.command(name=dbmanagement_cli.drop_tablespace_tablespace_admin_password_credential_details.name, help=dbmanagement_cli.drop_tablespace_tablespace_admin_password_credential_details.help)
@cli_util.option('--password', required=True, help=u"""The database user's password encoded using BASE64 scheme. [required]""")
@cli_util.option('--role', required=True, type=custom_types.CliCaseInsensitiveChoice(["NORMAL", "SYSDBA"]), help=u"""The role of the database user. [required]""")
@cli_util.option('--username', required=True, help=u"""The user to connect to the database. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'TablespaceAdminStatus'})
@cli_util.wrap_exceptions
def drop_tablespace_tablespace_admin_password_credential_details_extended(ctx, **kwargs):
    if 'password' in kwargs:
        kwargs['credential_details_password'] = kwargs['password']
        kwargs.pop('password')

    if 'role' in kwargs:
        kwargs['credential_details_role'] = kwargs['role']
        kwargs.pop('role')

    if 'username' in kwargs:
        kwargs['credential_details_username'] = kwargs['username']
        kwargs.pop('username')

    ctx.invoke(dbmanagement_cli.drop_tablespace_tablespace_admin_password_credential_details, **kwargs)


@cli_util.copy_params_from_generated_command(dbmanagement_cli.drop_tablespace_tablespace_admin_secret_credential_details, params_to_exclude=['credential_details_password_secret_id', 'credential_details_role', 'credential_details_username'])
@dbmanagement_cli.tablespace_group.command(name=dbmanagement_cli.drop_tablespace_tablespace_admin_secret_credential_details.name, help=dbmanagement_cli.drop_tablespace_tablespace_admin_secret_credential_details.help)
@cli_util.option('--secret', required=True, help=u"""The [OCID] of the Secret where the database password is stored. [required]""")
@cli_util.option('--role', required=True, type=custom_types.CliCaseInsensitiveChoice(["NORMAL", "SYSDBA"]), help=u"""The role of the database user. [required]""")
@cli_util.option('--username', required=True, help=u"""The user to connect to the database. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'TablespaceAdminStatus'})
@cli_util.wrap_exceptions
def drop_tablespace_tablespace_admin_secret_credential_details_extended(ctx, **kwargs):
    if 'secret' in kwargs:
        kwargs['credential_details_password_secret_id'] = kwargs['secret']
        kwargs.pop('secret')

    if 'role' in kwargs:
        kwargs['credential_details_role'] = kwargs['role']
        kwargs.pop('role')

    if 'username' in kwargs:
        kwargs['credential_details_username'] = kwargs['username']
        kwargs.pop('username')

    ctx.invoke(dbmanagement_cli.drop_tablespace_tablespace_admin_secret_credential_details, **kwargs)


@cli_util.copy_params_from_generated_command(dbmanagement_cli.remove_data_file_tablespace_admin_password_credential_details, params_to_exclude=['credential_details_password', 'credential_details_role', 'credential_details_username'])
@dbmanagement_cli.tablespace_group.command(name=dbmanagement_cli.remove_data_file_tablespace_admin_password_credential_details.name, help=dbmanagement_cli.remove_data_file_tablespace_admin_password_credential_details.help)
@cli_util.option('--password', required=True, help=u"""The database user's password encoded using BASE64 scheme. [required]""")
@cli_util.option('--role', required=True, type=custom_types.CliCaseInsensitiveChoice(["NORMAL", "SYSDBA"]), help=u"""The role of the database user. [required]""")
@cli_util.option('--username', required=True, help=u"""The user to connect to the database. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'TablespaceAdminStatus'})
@cli_util.wrap_exceptions
def remove_data_file_tablespace_admin_password_credential_details_extended(ctx, **kwargs):
    if 'password' in kwargs:
        kwargs['credential_details_password'] = kwargs['password']
        kwargs.pop('password')

    if 'role' in kwargs:
        kwargs['credential_details_role'] = kwargs['role']
        kwargs.pop('role')

    if 'username' in kwargs:
        kwargs['credential_details_username'] = kwargs['username']
        kwargs.pop('username')

    ctx.invoke(dbmanagement_cli.remove_data_file_tablespace_admin_password_credential_details, **kwargs)


@cli_util.copy_params_from_generated_command(dbmanagement_cli.remove_data_file_tablespace_admin_secret_credential_details, params_to_exclude=['credential_details_password_secret_id', 'credential_details_role', 'credential_details_username'])
@dbmanagement_cli.tablespace_group.command(name=dbmanagement_cli.remove_data_file_tablespace_admin_secret_credential_details.name, help=dbmanagement_cli.remove_data_file_tablespace_admin_secret_credential_details.help)
@cli_util.option('--secret', required=True, help=u"""The [OCID] of the Secret where the database password is stored. [required]""")
@cli_util.option('--role', required=True, type=custom_types.CliCaseInsensitiveChoice(["NORMAL", "SYSDBA"]), help=u"""The role of the database user. [required]""")
@cli_util.option('--username', required=True, help=u"""The user to connect to the database. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'TablespaceAdminStatus'})
@cli_util.wrap_exceptions
def remove_data_file_tablespace_admin_secret_credential_details_extended(ctx, **kwargs):
    if 'secret' in kwargs:
        kwargs['credential_details_password_secret_id'] = kwargs['secret']
        kwargs.pop('secret')

    if 'role' in kwargs:
        kwargs['credential_details_role'] = kwargs['role']
        kwargs.pop('role')

    if 'username' in kwargs:
        kwargs['credential_details_username'] = kwargs['username']
        kwargs.pop('username')

    ctx.invoke(dbmanagement_cli.remove_data_file_tablespace_admin_secret_credential_details, **kwargs)


# oci database-management preferred-credential test-preferred-credential-test-basic-preferred-credential-details -> oci database-management preferred-credential test-basic-preferred-credential-details
cli_util.rename_command(dbmanagement_cli, dbmanagement_cli.preferred_credential_group, dbmanagement_cli.test_preferred_credential_test_basic_preferred_credential_details, "test-basic-preferred-credential-details")


# oci database-management preferred-credential update-preferred-credential-update-basic-preferred-credential-details -> oci database-management preferred-credential update-basic-preferred-credential-details
cli_util.rename_command(dbmanagement_cli, dbmanagement_cli.preferred_credential_group, dbmanagement_cli.update_preferred_credential_update_basic_preferred_credential_details, "update-basic-preferred-credential-details")
