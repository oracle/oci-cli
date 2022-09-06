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


@click.command(cli_util.override('db_management.db_management_root_group.command_name', 'db-management'), cls=CommandGroupWithAlias, help=cli_util.override('db_management.db_management_root_group.help', """Use the Database Management API to perform tasks such as obtaining performance and resource usage metrics
for a fleet of Managed Databases or a specific Managed Database, creating Managed Database Groups, and
running a SQL job on a Managed Database or Managed Database Group."""), short_help=cli_util.override('db_management.db_management_root_group.short_help', """Database Management API"""))
@cli_util.help_option_group
def db_management_root_group():
    pass


@click.command(cli_util.override('db_management.addm_tasks_collection_group.command_name', 'addm-tasks-collection'), cls=CommandGroupWithAlias, help="""The list of ADDM task metadata.""")
@cli_util.help_option_group
def addm_tasks_collection_group():
    pass


@click.command(cli_util.override('db_management.snapshot_details_group.command_name', 'snapshot-details'), cls=CommandGroupWithAlias, help="""The details of the newly generated AWR snapshot.""")
@cli_util.help_option_group
def snapshot_details_group():
    pass


@click.command(cli_util.override('db_management.historic_addm_result_group.command_name', 'historic-addm-result'), cls=CommandGroupWithAlias, help="""The details of the historic ADDM task.""")
@cli_util.help_option_group
def historic_addm_result_group():
    pass


@click.command(cli_util.override('db_management.cluster_cache_metric_group.command_name', 'cluster-cache-metric'), cls=CommandGroupWithAlias, help="""The response containing the cluster cache metrics for the Oracle Real Application Clusters (Oracle RAC) database.""")
@cli_util.help_option_group
def cluster_cache_metric_group():
    pass


@click.command(cli_util.override('db_management.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""A log message from the execution of a work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('db_management.managed_database_group_group.command_name', 'managed-database-group'), cls=CommandGroupWithAlias, help="""The details of a Managed Database Group.""")
@cli_util.help_option_group
def managed_database_group_group():
    pass


@click.command(cli_util.override('db_management.pdb_metrics_group.command_name', 'pdb-metrics'), cls=CommandGroupWithAlias, help="""The summary of Pluggable Databases (PDBs) and their resource usage metrics, within a specific Container Database (CDB).""")
@cli_util.help_option_group
def pdb_metrics_group():
    pass


@click.command(cli_util.override('db_management.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""A description of the work request status.""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('db_management.database_home_metrics_group.command_name', 'database-home-metrics'), cls=CommandGroupWithAlias, help="""The response containing the metric collection for a specific Managed Database.""")
@cli_util.help_option_group
def database_home_metrics_group():
    pass


@click.command(cli_util.override('db_management.database_fleet_health_metrics_group.command_name', 'database-fleet-health-metrics'), cls=CommandGroupWithAlias, help="""The details of the fleet health metrics.""")
@cli_util.help_option_group
def database_fleet_health_metrics_group():
    pass


@click.command(cli_util.override('db_management.tablespace_group.command_name', 'tablespace'), cls=CommandGroupWithAlias, help="""The details of a tablespace.""")
@cli_util.help_option_group
def tablespace_group():
    pass


@click.command(cli_util.override('db_management.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('db_management.db_management_private_endpoint_group.command_name', 'db-management-private-endpoint'), cls=CommandGroupWithAlias, help="""A Database Management private endpoint allows Database Management to connect to databases in a Virtual Cloud Network (VCN).""")
@cli_util.help_option_group
def db_management_private_endpoint_group():
    pass


@click.command(cli_util.override('db_management.job_executions_status_summary_collection_group.command_name', 'job-executions-status-summary-collection'), cls=CommandGroupWithAlias, help="""A collection of job execution status summary objects.""")
@cli_util.help_option_group
def job_executions_status_summary_collection_group():
    pass


@click.command(cli_util.override('db_management.managed_database_group.command_name', 'managed-database'), cls=CommandGroupWithAlias, help="""The details of a Managed Database.""")
@cli_util.help_option_group
def managed_database_group():
    pass


@click.command(cli_util.override('db_management.job_run_group.command_name', 'job-run'), cls=CommandGroupWithAlias, help="""The details of a specific job run.""")
@cli_util.help_option_group
def job_run_group():
    pass


@click.command(cli_util.override('db_management.job_execution_group.command_name', 'job-execution'), cls=CommandGroupWithAlias, help="""The details of a job execution.""")
@cli_util.help_option_group
def job_execution_group():
    pass


@click.command(cli_util.override('db_management.associated_database_summary_group.command_name', 'associated-database-summary'), cls=CommandGroupWithAlias, help="""The summary of a database currently using a Database Management private endpoint.""")
@cli_util.help_option_group
def associated_database_summary_group():
    pass


@click.command(cli_util.override('db_management.job_group.command_name', 'job'), cls=CommandGroupWithAlias, help="""The details of the job.""")
@cli_util.help_option_group
def job_group():
    pass


@click.command(cli_util.override('db_management.preferred_credential_group.command_name', 'preferred-credential'), cls=CommandGroupWithAlias, help="""The details of the preferred credential.""")
@cli_util.help_option_group
def preferred_credential_group():
    pass


database_management_service_cli.database_management_service_group.add_command(db_management_root_group)
db_management_root_group.add_command(addm_tasks_collection_group)
db_management_root_group.add_command(snapshot_details_group)
db_management_root_group.add_command(historic_addm_result_group)
db_management_root_group.add_command(cluster_cache_metric_group)
db_management_root_group.add_command(work_request_log_entry_group)
db_management_root_group.add_command(managed_database_group_group)
db_management_root_group.add_command(pdb_metrics_group)
db_management_root_group.add_command(work_request_group)
db_management_root_group.add_command(database_home_metrics_group)
db_management_root_group.add_command(database_fleet_health_metrics_group)
db_management_root_group.add_command(tablespace_group)
db_management_root_group.add_command(work_request_error_group)
db_management_root_group.add_command(db_management_private_endpoint_group)
db_management_root_group.add_command(job_executions_status_summary_collection_group)
db_management_root_group.add_command(managed_database_group)
db_management_root_group.add_command(job_run_group)
db_management_root_group.add_command(job_execution_group)
db_management_root_group.add_command(associated_database_summary_group)
db_management_root_group.add_command(job_group)
db_management_root_group.add_command(preferred_credential_group)


@tablespace_group.command(name=cli_util.override('db_management.add_data_files.command_name', 'add'), help=u"""Adds data files or temp files to the tablespace. \n[Command Reference](addDataFiles)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--tablespace-name', required=True, help=u"""The name of the tablespace.""")
@cli_util.option('--credential-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--file-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["DATAFILE", "TEMPFILE"]), help=u"""Specifies whether the file is a data file or temp file.""")
@cli_util.option('--data-files', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of data files or temp files added to the tablespace.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--file-count', type=click.INT, help=u"""The number of data files or temp files to be added for the tablespace. This is for Oracle Managed Files only.""")
@cli_util.option('--file-size', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The size of each data file or temp file.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-reusable', type=click.BOOL, help=u"""Specifies whether Oracle can reuse the data file or temp file. Reuse is only allowed when the file name is provided.""")
@cli_util.option('--is-auto-extensible', type=click.BOOL, help=u"""Specifies whether the data file or temp file can be extended automatically.""")
@cli_util.option('--auto-extend-next-size', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The size of the next increment of disk space to be allocated automatically when more extents are required.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--auto-extend-max-size', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The maximum disk space allowed for automatic extension of the data files or temp files.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-max-size-unlimited', type=click.BOOL, help=u"""Specifies whether the disk space of the data file or temp file can be limited.""")
@json_skeleton_utils.get_cli_json_input_option({'credential-details': {'module': 'database_management', 'class': 'TablespaceAdminCredentialDetails'}, 'data-files': {'module': 'database_management', 'class': 'list[string]'}, 'file-size': {'module': 'database_management', 'class': 'TablespaceStorageSize'}, 'auto-extend-next-size': {'module': 'database_management', 'class': 'TablespaceStorageSize'}, 'auto-extend-max-size': {'module': 'database_management', 'class': 'TablespaceStorageSize'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'credential-details': {'module': 'database_management', 'class': 'TablespaceAdminCredentialDetails'}, 'data-files': {'module': 'database_management', 'class': 'list[string]'}, 'file-size': {'module': 'database_management', 'class': 'TablespaceStorageSize'}, 'auto-extend-next-size': {'module': 'database_management', 'class': 'TablespaceStorageSize'}, 'auto-extend-max-size': {'module': 'database_management', 'class': 'TablespaceStorageSize'}}, output_type={'module': 'database_management', 'class': 'TablespaceAdminStatus'})
@cli_util.wrap_exceptions
def add_data_files(ctx, from_json, managed_database_id, tablespace_name, credential_details, file_type, data_files, file_count, file_size, is_reusable, is_auto_extensible, auto_extend_next_size, auto_extend_max_size, is_max_size_unlimited):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(tablespace_name, six.string_types) and len(tablespace_name.strip()) == 0:
        raise click.UsageError('Parameter --tablespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['credentialDetails'] = cli_util.parse_json_parameter("credential_details", credential_details)
    _details['fileType'] = file_type

    if data_files is not None:
        _details['dataFiles'] = cli_util.parse_json_parameter("data_files", data_files)

    if file_count is not None:
        _details['fileCount'] = file_count

    if file_size is not None:
        _details['fileSize'] = cli_util.parse_json_parameter("file_size", file_size)

    if is_reusable is not None:
        _details['isReusable'] = is_reusable

    if is_auto_extensible is not None:
        _details['isAutoExtensible'] = is_auto_extensible

    if auto_extend_next_size is not None:
        _details['autoExtendNextSize'] = cli_util.parse_json_parameter("auto_extend_next_size", auto_extend_next_size)

    if auto_extend_max_size is not None:
        _details['autoExtendMaxSize'] = cli_util.parse_json_parameter("auto_extend_max_size", auto_extend_max_size)

    if is_max_size_unlimited is not None:
        _details['isMaxSizeUnlimited'] = is_max_size_unlimited

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.add_data_files(
        managed_database_id=managed_database_id,
        tablespace_name=tablespace_name,
        add_data_files_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group_group.command(name=cli_util.override('db_management.add_managed_database_to_managed_database_group.command_name', 'add'), help=u"""Adds a Managed Database to a specific Managed Database Group. After the database is added, it will be included in the management activities performed on the Managed Database Group. \n[Command Reference](addManagedDatabaseToManagedDatabaseGroup)""")
@cli_util.option('--managed-database-group-id', required=True, help=u"""The [OCID] of the Managed Database Group.""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def add_managed_database_to_managed_database_group(ctx, from_json, managed_database_group_id, managed_database_id):

    if isinstance(managed_database_group_id, six.string_types) and len(managed_database_group_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-group-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['managedDatabaseId'] = managed_database_id

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.add_managed_database_to_managed_database_group(
        managed_database_group_id=managed_database_group_id,
        add_managed_database_to_managed_database_group_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@addm_tasks_collection_group.command(name=cli_util.override('db_management.addm_tasks.command_name', 'add'), help=u"""Lists the metadata for each ADDM task who's end snapshot time falls within the provided start and end time. Details include the name of the ADDM task, description, user, status and creation date time. \n[Command Reference](addmTasks)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--time-start', required=True, type=custom_types.CLI_DATETIME, help=u"""The beginning of the time range to search for ADDM tasks as defined by date-time RFC3339 format.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-end', required=True, type=custom_types.CLI_DATETIME, help=u"""The end of the time range to search for ADDM tasks as defined by date-time RFC3339 format.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TASK_NAME", "TASK_ID", "DESCRIPTION", "DB_USER", "STATUS", "TIME_CREATED", "BEGIN_TIME", "END_TIME"]), help=u"""The option to sort the list of ADDM tasks.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the default order.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'AddmTasksCollection'})
@cli_util.wrap_exceptions
def addm_tasks(ctx, from_json, managed_database_id, time_start, time_end, page, limit, sort_by, sort_order):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.addm_tasks(
        managed_database_id=managed_database_id,
        time_start=time_start,
        time_end=time_end,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.change_database_parameters.command_name', 'change-database-parameters'), help=u"""Changes database parameter values. There are two kinds of database parameters:

- Dynamic parameters: They can be changed for the current Oracle Database instance. The changes take effect immediately. - Static parameters: They cannot be changed for the current instance. You must change these parameters and then restart the database before changes take effect.

**Note:** If the instance is started using a text initialization parameter file, the parameter changes are applicable only for the current instance. You must update them manually to be passed to a future instance. \n[Command Reference](changeDatabaseParameters)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--credentials', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--scope', required=True, type=custom_types.CliCaseInsensitiveChoice(["MEMORY", "SPFILE", "BOTH"]), help=u"""The clause used to specify when the parameter change takes effect.

Use `MEMORY` to make the change in memory and affect it immediately. Use `SPFILE` to make the change in the server parameter file. The change takes effect when the database is next shut down and started up again. Use `BOTH` to make the change in memory and in the server parameter file. The change takes effect immediately and persists after the database is shut down and started up again.""")
@cli_util.option('--parameters', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of database parameters and their values.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'credentials': {'module': 'database_management', 'class': 'DatabaseCredentials'}, 'parameters': {'module': 'database_management', 'class': 'list[ChangeDatabaseParameterDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'credentials': {'module': 'database_management', 'class': 'DatabaseCredentials'}, 'parameters': {'module': 'database_management', 'class': 'list[ChangeDatabaseParameterDetails]'}}, output_type={'module': 'database_management', 'class': 'UpdateDatabaseParametersResult'})
@cli_util.wrap_exceptions
def change_database_parameters(ctx, from_json, managed_database_id, credentials, scope, parameters):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['credentials'] = cli_util.parse_json_parameter("credentials", credentials)
    _details['scope'] = scope
    _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.change_database_parameters(
        managed_database_id=managed_database_id,
        change_database_parameters_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@db_management_private_endpoint_group.command(name=cli_util.override('db_management.change_db_management_private_endpoint_compartment.command_name', 'change-compartment'), help=u"""Moves the Database Management private endpoint and its dependent resources to the specified compartment. \n[Command Reference](changeDbManagementPrivateEndpointCompartment)""")
@cli_util.option('--db-management-private-endpoint-id', required=True, help=u"""The [OCID] of the Database Management private endpoint.""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment to which the Database Management private endpoint needs to be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_db_management_private_endpoint_compartment(ctx, from_json, db_management_private_endpoint_id, compartment_id, if_match):

    if isinstance(db_management_private_endpoint_id, six.string_types) and len(db_management_private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --db-management-private-endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.change_db_management_private_endpoint_compartment(
        db_management_private_endpoint_id=db_management_private_endpoint_id,
        change_db_management_private_endpoint_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('db_management.change_job_compartment.command_name', 'change-compartment'), help=u"""Moves a job. \n[Command Reference](changeJobCompartment)""")
@cli_util.option('--job-id', required=True, help=u"""The identifier of the job.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to which the job should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_job_compartment(ctx, from_json, job_id, compartment_id, if_match):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.change_job_compartment(
        job_id=job_id,
        change_job_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group_group.command(name=cli_util.override('db_management.change_managed_database_group_compartment.command_name', 'change-compartment'), help=u"""Moves a Managed Database Group to a different compartment. The destination compartment must not have a Managed Database Group with the same name. \n[Command Reference](changeManagedDatabaseGroupCompartment)""")
@cli_util.option('--managed-database-group-id', required=True, help=u"""The [OCID] of the Managed Database Group.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to which the Managed Database Group should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_managed_database_group_compartment(ctx, from_json, managed_database_group_id, compartment_id, if_match):

    if isinstance(managed_database_group_id, six.string_types) and len(managed_database_group_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-group-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.change_managed_database_group_compartment(
        managed_database_group_id=managed_database_group_id,
        change_managed_database_group_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@db_management_private_endpoint_group.command(name=cli_util.override('db_management.create_db_management_private_endpoint.command_name', 'create'), help=u"""Creates a new Database Management private endpoint. \n[Command Reference](createDbManagementPrivateEndpoint)""")
@cli_util.option('--name', required=True, help=u"""The display name of the Database Management private endpoint.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--subnet-id', required=True, help=u"""The [OCID] of the subnet.""")
@cli_util.option('--is-cluster', type=click.BOOL, help=u"""Specifies whether the Database Management private endpoint will be used for Oracle Databases in a cluster.""")
@cli_util.option('--description', help=u"""The description of the private endpoint.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The OCIDs of the Network Security Groups to which the Database Management private endpoint belongs.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'nsg-ids': {'module': 'database_management', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'nsg-ids': {'module': 'database_management', 'class': 'list[string]'}}, output_type={'module': 'database_management', 'class': 'DbManagementPrivateEndpoint'})
@cli_util.wrap_exceptions
def create_db_management_private_endpoint(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, compartment_id, subnet_id, is_cluster, description, nsg_ids):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['compartmentId'] = compartment_id
    _details['subnetId'] = subnet_id

    if is_cluster is not None:
        _details['isCluster'] = is_cluster

    if description is not None:
        _details['description'] = description

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.create_db_management_private_endpoint(
        create_db_management_private_endpoint_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('db_management.create_job.command_name', 'create'), help=u"""Creates a job to be executed on a Managed Database or Managed Database Group. Only one of the parameters, managedDatabaseId or managedDatabaseGroupId should be provided as input in CreateJobDetails resource in request body. \n[Command Reference](createJob)""")
@cli_util.option('--name', required=True, help=u"""The name of the job. Valid characters are uppercase or lowercase letters, numbers, and \"_\". The name of the job cannot be modified. It must be unique in the compartment and must begin with an alphabetic character.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which the job resides.""")
@cli_util.option('--schedule-type', required=True, help=u"""The schedule type of the job.""")
@cli_util.option('--job-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["SQL"]), help=u"""The type of job.""")
@cli_util.option('--description', help=u"""The description of the job.""")
@cli_util.option('--managed-database-group-id', help=u"""The [OCID] of the Managed Database Group where the job has to be executed.""")
@cli_util.option('--managed-database-id', help=u"""The [OCID] of the Managed Database where the job has to be executed.""")
@cli_util.option('--database-sub-type', type=custom_types.CliCaseInsensitiveChoice(["CDB", "PDB", "NON_CDB", "ACD", "ADB"]), help=u"""The subtype of the Oracle Database where the job has to be executed. Only applicable when managedDatabaseGroupId is provided.""")
@cli_util.option('--timeout', help=u"""The job timeout duration, which is expressed like \"1h 10m 15s\".""")
@cli_util.option('--result-location', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--schedule-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'result-location': {'module': 'database_management', 'class': 'JobExecutionResultLocation'}, 'schedule-details': {'module': 'database_management', 'class': 'JobScheduleDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'result-location': {'module': 'database_management', 'class': 'JobExecutionResultLocation'}, 'schedule-details': {'module': 'database_management', 'class': 'JobScheduleDetails'}}, output_type={'module': 'database_management', 'class': 'Job'})
@cli_util.wrap_exceptions
def create_job(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, compartment_id, schedule_type, job_type, description, managed_database_group_id, managed_database_id, database_sub_type, timeout, result_location, schedule_details):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['compartmentId'] = compartment_id
    _details['scheduleType'] = schedule_type
    _details['jobType'] = job_type

    if description is not None:
        _details['description'] = description

    if managed_database_group_id is not None:
        _details['managedDatabaseGroupId'] = managed_database_group_id

    if managed_database_id is not None:
        _details['managedDatabaseId'] = managed_database_id

    if database_sub_type is not None:
        _details['databaseSubType'] = database_sub_type

    if timeout is not None:
        _details['timeout'] = timeout

    if result_location is not None:
        _details['resultLocation'] = cli_util.parse_json_parameter("result_location", result_location)

    if schedule_details is not None:
        _details['scheduleDetails'] = cli_util.parse_json_parameter("schedule_details", schedule_details)

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.create_job(
        create_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('db_management.create_job_create_sql_job_details.command_name', 'create-job-create-sql-job-details'), help=u"""Creates a job to be executed on a Managed Database or Managed Database Group. Only one of the parameters, managedDatabaseId or managedDatabaseGroupId should be provided as input in CreateJobDetails resource in request body. \n[Command Reference](createJob)""")
@cli_util.option('--name', required=True, help=u"""The name of the job. Valid characters are uppercase or lowercase letters, numbers, and \"_\". The name of the job cannot be modified. It must be unique in the compartment and must begin with an alphabetic character.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which the job resides.""")
@cli_util.option('--schedule-type', required=True, help=u"""The schedule type of the job.""")
@cli_util.option('--operation-type', required=True, help=u"""The SQL operation type.""")
@cli_util.option('--description', help=u"""The description of the job.""")
@cli_util.option('--managed-database-group-id', help=u"""The [OCID] of the Managed Database Group where the job has to be executed.""")
@cli_util.option('--managed-database-id', help=u"""The [OCID] of the Managed Database where the job has to be executed.""")
@cli_util.option('--database-sub-type', type=custom_types.CliCaseInsensitiveChoice(["CDB", "PDB", "NON_CDB", "ACD", "ADB"]), help=u"""The subtype of the Oracle Database where the job has to be executed. Only applicable when managedDatabaseGroupId is provided.""")
@cli_util.option('--timeout', help=u"""The job timeout duration, which is expressed like \"1h 10m 15s\".""")
@cli_util.option('--result-location', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--schedule-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--sql-text', help=u"""The SQL text to be executed as part of the job.""")
@cli_util.option('--sql-type', help=u"""""")
@cli_util.option('--user-name', help=u"""The database user name used to execute the SQL job. If the job is being executed on a Managed Database Group, then the user name should exist on all the databases in the group with the same password.""")
@cli_util.option('--password', help=u"""The password for the database user name used to execute the SQL job.""")
@cli_util.option('--secret-id', help=u"""The [OCID] of the secret containing the user password.""")
@cli_util.option('--role', help=u"""The role of the database user. Indicates whether the database user is a normal user or sysdba.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'result-location': {'module': 'database_management', 'class': 'JobExecutionResultLocation'}, 'schedule-details': {'module': 'database_management', 'class': 'JobScheduleDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'result-location': {'module': 'database_management', 'class': 'JobExecutionResultLocation'}, 'schedule-details': {'module': 'database_management', 'class': 'JobScheduleDetails'}}, output_type={'module': 'database_management', 'class': 'Job'})
@cli_util.wrap_exceptions
def create_job_create_sql_job_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, compartment_id, schedule_type, operation_type, description, managed_database_group_id, managed_database_id, database_sub_type, timeout, result_location, schedule_details, sql_text, sql_type, user_name, password, secret_id, role):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['compartmentId'] = compartment_id
    _details['scheduleType'] = schedule_type
    _details['operationType'] = operation_type

    if description is not None:
        _details['description'] = description

    if managed_database_group_id is not None:
        _details['managedDatabaseGroupId'] = managed_database_group_id

    if managed_database_id is not None:
        _details['managedDatabaseId'] = managed_database_id

    if database_sub_type is not None:
        _details['databaseSubType'] = database_sub_type

    if timeout is not None:
        _details['timeout'] = timeout

    if result_location is not None:
        _details['resultLocation'] = cli_util.parse_json_parameter("result_location", result_location)

    if schedule_details is not None:
        _details['scheduleDetails'] = cli_util.parse_json_parameter("schedule_details", schedule_details)

    if sql_text is not None:
        _details['sqlText'] = sql_text

    if sql_type is not None:
        _details['sqlType'] = sql_type

    if user_name is not None:
        _details['userName'] = user_name

    if password is not None:
        _details['password'] = password

    if secret_id is not None:
        _details['secretId'] = secret_id

    if role is not None:
        _details['role'] = role

    _details['jobType'] = 'SQL'

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.create_job(
        create_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('db_management.create_job_object_storage_job_execution_result_location.command_name', 'create-job-object-storage-job-execution-result-location'), help=u"""Creates a job to be executed on a Managed Database or Managed Database Group. Only one of the parameters, managedDatabaseId or managedDatabaseGroupId should be provided as input in CreateJobDetails resource in request body. \n[Command Reference](createJob)""")
@cli_util.option('--name', required=True, help=u"""The name of the job. Valid characters are uppercase or lowercase letters, numbers, and \"_\". The name of the job cannot be modified. It must be unique in the compartment and must begin with an alphabetic character.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which the job resides.""")
@cli_util.option('--schedule-type', required=True, help=u"""The schedule type of the job.""")
@cli_util.option('--description', help=u"""The description of the job.""")
@cli_util.option('--managed-database-group-id', help=u"""The [OCID] of the Managed Database Group where the job has to be executed.""")
@cli_util.option('--managed-database-id', help=u"""The [OCID] of the Managed Database where the job has to be executed.""")
@cli_util.option('--database-sub-type', type=custom_types.CliCaseInsensitiveChoice(["CDB", "PDB", "NON_CDB", "ACD", "ADB"]), help=u"""The subtype of the Oracle Database where the job has to be executed. Only applicable when managedDatabaseGroupId is provided.""")
@cli_util.option('--timeout', help=u"""The job timeout duration, which is expressed like \"1h 10m 15s\".""")
@cli_util.option('--schedule-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--result-location-namespace-name', help=u"""The Object Storage namespace used for job execution result storage.""")
@cli_util.option('--result-location-bucket-name', help=u"""The name of the bucket used for job execution result storage.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'schedule-details': {'module': 'database_management', 'class': 'JobScheduleDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'schedule-details': {'module': 'database_management', 'class': 'JobScheduleDetails'}}, output_type={'module': 'database_management', 'class': 'Job'})
@cli_util.wrap_exceptions
def create_job_object_storage_job_execution_result_location(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, compartment_id, schedule_type, description, managed_database_group_id, managed_database_id, database_sub_type, timeout, schedule_details, result_location_namespace_name, result_location_bucket_name):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['resultLocation'] = {}
    _details['name'] = name
    _details['compartmentId'] = compartment_id
    _details['scheduleType'] = schedule_type

    if description is not None:
        _details['description'] = description

    if managed_database_group_id is not None:
        _details['managedDatabaseGroupId'] = managed_database_group_id

    if managed_database_id is not None:
        _details['managedDatabaseId'] = managed_database_id

    if database_sub_type is not None:
        _details['databaseSubType'] = database_sub_type

    if timeout is not None:
        _details['timeout'] = timeout

    if schedule_details is not None:
        _details['scheduleDetails'] = cli_util.parse_json_parameter("schedule_details", schedule_details)

    if result_location_namespace_name is not None:
        _details['resultLocation']['namespaceName'] = result_location_namespace_name

    if result_location_bucket_name is not None:
        _details['resultLocation']['bucketName'] = result_location_bucket_name

    _details['resultLocation']['type'] = 'OBJECT_STORAGE'

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.create_job(
        create_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@managed_database_group_group.command(name=cli_util.override('db_management.create_managed_database_group.command_name', 'create'), help=u"""Creates a Managed Database Group. The group does not contain any Managed Databases when it is created, and they must be added later. \n[Command Reference](createManagedDatabaseGroup)""")
@cli_util.option('--name', required=True, help=u"""The name of the Managed Database Group. Valid characters are uppercase or lowercase letters, numbers, and \"_\". The name of the Managed Database Group cannot be modified. It must be unique in the compartment and must begin with an alphabetic character.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which the Managed Database Group resides.""")
@cli_util.option('--description', help=u"""The information specified by the user about the Managed Database Group.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'ManagedDatabaseGroup'})
@cli_util.wrap_exceptions
def create_managed_database_group(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, compartment_id, description):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['compartmentId'] = compartment_id

    if description is not None:
        _details['description'] = description

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.create_managed_database_group(
        create_managed_database_group_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_managed_database_group') and callable(getattr(client, 'get_managed_database_group')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_managed_database_group(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@tablespace_group.command(name=cli_util.override('db_management.create_tablespace.command_name', 'create'), help=u"""Creates a tablespace within the Managed Database specified by managedDatabaseId. \n[Command Reference](createTablespace)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--credential-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--name', required=True, help=u"""The name of the tablespace. It must be unique within a database.""")
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["PERMANENT", "TEMPORARY"]), help=u"""The type of tablespace.""")
@cli_util.option('--is-bigfile', type=click.BOOL, help=u"""Specifies whether the tablespace is a bigfile or smallfile tablespace. A bigfile tablespace contains only one data file or temp file, which can contain up to approximately 4 billion (232) blocks. A smallfile tablespace is a traditional Oracle tablespace, which can contain 1022 data files or temp files, each of which can contain up to approximately 4 million (222) blocks.""")
@cli_util.option('--data-files', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of data files or temp files created for the tablespace.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--file-count', type=click.INT, help=u"""The number of data files or temp files created for the tablespace. This is for Oracle Managed Files only.""")
@cli_util.option('--file-size', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The size of each data file or temp file.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-reusable', type=click.BOOL, help=u"""Specifies whether Oracle can reuse the data file or temp file. Reuse is only allowed when the file name is provided.""")
@cli_util.option('--is-auto-extensible', type=click.BOOL, help=u"""Specifies whether the data file or temp file can be extended automatically.""")
@cli_util.option('--auto-extend-next-size', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The size of the next increment of disk space to be allocated automatically when more extents are required.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--auto-extend-max-size', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The maximum disk space allowed for automatic extension of the data files or temp files.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-max-size-unlimited', type=click.BOOL, help=u"""Specifies whether the disk space of the data file or temp file can be limited.""")
@cli_util.option('--block-size-in-kilobytes', type=click.INT, help=u"""Block size for the tablespace.""")
@cli_util.option('--is-encrypted', type=click.BOOL, help=u"""Indicates whether the tablespace is encrypted.""")
@cli_util.option('--encryption-algorithm', help=u"""The name of the encryption algorithm to be used for tablespace encryption.""")
@cli_util.option('--default-compress', type=custom_types.CliCaseInsensitiveChoice(["NO_COMPRESS", "BASIC_COMPRESS"]), help=u"""The default compression of data for all tables created in the tablespace.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["READ_ONLY", "READ_WRITE"]), help=u"""The status of the tablespace.""")
@cli_util.option('--extent-management', type=custom_types.CliCaseInsensitiveChoice(["AUTOALLOCATE", "UNIFORM"]), help=u"""Specifies how the extents of the tablespace should be managed.""")
@cli_util.option('--extent-uniform-size', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The size of the extent when the tablespace is managed with uniform extents of a specific size.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--segment-management', type=custom_types.CliCaseInsensitiveChoice(["AUTO", "MANUAL"]), help=u"""Specifies whether tablespace segment management should be automatic or manual.""")
@cli_util.option('--is-default', type=click.BOOL, help=u"""Specifies whether the tablespace is the default tablespace.""")
@json_skeleton_utils.get_cli_json_input_option({'credential-details': {'module': 'database_management', 'class': 'TablespaceAdminCredentialDetails'}, 'data-files': {'module': 'database_management', 'class': 'list[string]'}, 'file-size': {'module': 'database_management', 'class': 'TablespaceStorageSize'}, 'auto-extend-next-size': {'module': 'database_management', 'class': 'TablespaceStorageSize'}, 'auto-extend-max-size': {'module': 'database_management', 'class': 'TablespaceStorageSize'}, 'extent-uniform-size': {'module': 'database_management', 'class': 'TablespaceStorageSize'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'credential-details': {'module': 'database_management', 'class': 'TablespaceAdminCredentialDetails'}, 'data-files': {'module': 'database_management', 'class': 'list[string]'}, 'file-size': {'module': 'database_management', 'class': 'TablespaceStorageSize'}, 'auto-extend-next-size': {'module': 'database_management', 'class': 'TablespaceStorageSize'}, 'auto-extend-max-size': {'module': 'database_management', 'class': 'TablespaceStorageSize'}, 'extent-uniform-size': {'module': 'database_management', 'class': 'TablespaceStorageSize'}}, output_type={'module': 'database_management', 'class': 'Tablespace'})
@cli_util.wrap_exceptions
def create_tablespace(ctx, from_json, managed_database_id, credential_details, name, type, is_bigfile, data_files, file_count, file_size, is_reusable, is_auto_extensible, auto_extend_next_size, auto_extend_max_size, is_max_size_unlimited, block_size_in_kilobytes, is_encrypted, encryption_algorithm, default_compress, status, extent_management, extent_uniform_size, segment_management, is_default):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['credentialDetails'] = cli_util.parse_json_parameter("credential_details", credential_details)
    _details['name'] = name

    if type is not None:
        _details['type'] = type

    if is_bigfile is not None:
        _details['isBigfile'] = is_bigfile

    if data_files is not None:
        _details['dataFiles'] = cli_util.parse_json_parameter("data_files", data_files)

    if file_count is not None:
        _details['fileCount'] = file_count

    if file_size is not None:
        _details['fileSize'] = cli_util.parse_json_parameter("file_size", file_size)

    if is_reusable is not None:
        _details['isReusable'] = is_reusable

    if is_auto_extensible is not None:
        _details['isAutoExtensible'] = is_auto_extensible

    if auto_extend_next_size is not None:
        _details['autoExtendNextSize'] = cli_util.parse_json_parameter("auto_extend_next_size", auto_extend_next_size)

    if auto_extend_max_size is not None:
        _details['autoExtendMaxSize'] = cli_util.parse_json_parameter("auto_extend_max_size", auto_extend_max_size)

    if is_max_size_unlimited is not None:
        _details['isMaxSizeUnlimited'] = is_max_size_unlimited

    if block_size_in_kilobytes is not None:
        _details['blockSizeInKilobytes'] = block_size_in_kilobytes

    if is_encrypted is not None:
        _details['isEncrypted'] = is_encrypted

    if encryption_algorithm is not None:
        _details['encryptionAlgorithm'] = encryption_algorithm

    if default_compress is not None:
        _details['defaultCompress'] = default_compress

    if status is not None:
        _details['status'] = status

    if extent_management is not None:
        _details['extentManagement'] = extent_management

    if extent_uniform_size is not None:
        _details['extentUniformSize'] = cli_util.parse_json_parameter("extent_uniform_size", extent_uniform_size)

    if segment_management is not None:
        _details['segmentManagement'] = segment_management

    if is_default is not None:
        _details['isDefault'] = is_default

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.create_tablespace(
        managed_database_id=managed_database_id,
        create_tablespace_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@db_management_private_endpoint_group.command(name=cli_util.override('db_management.delete_db_management_private_endpoint.command_name', 'delete'), help=u"""Deletes a specific Database Management private endpoint. \n[Command Reference](deleteDbManagementPrivateEndpoint)""")
@cli_util.option('--db-management-private-endpoint-id', required=True, help=u"""The [OCID] of the Database Management private endpoint.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_db_management_private_endpoint(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, db_management_private_endpoint_id, if_match):

    if isinstance(db_management_private_endpoint_id, six.string_types) and len(db_management_private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --db-management-private-endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.delete_db_management_private_endpoint(
        db_management_private_endpoint_id=db_management_private_endpoint_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('db_management.delete_job.command_name', 'delete'), help=u"""Deletes the job specified by jobId. \n[Command Reference](deleteJob)""")
@cli_util.option('--job-id', required=True, help=u"""The identifier of the job.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_job(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, job_id, if_match):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.delete_job(
        job_id=job_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_job(job_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@managed_database_group_group.command(name=cli_util.override('db_management.delete_managed_database_group.command_name', 'delete'), help=u"""Deletes the Managed Database Group specified by managedDatabaseGroupId. If the group contains Managed Databases, then it cannot be deleted. \n[Command Reference](deleteManagedDatabaseGroup)""")
@cli_util.option('--managed-database-group-id', required=True, help=u"""The [OCID] of the Managed Database Group.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_managed_database_group(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, managed_database_group_id, if_match):

    if isinstance(managed_database_group_id, six.string_types) and len(managed_database_group_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-group-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.delete_managed_database_group(
        managed_database_group_id=managed_database_group_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_managed_database_group') and callable(getattr(client, 'get_managed_database_group')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_managed_database_group(managed_database_group_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@preferred_credential_group.command(name=cli_util.override('db_management.delete_preferred_credential.command_name', 'delete'), help=u"""Deletes the preferred credential based on the credentialName. \n[Command Reference](deletePreferredCredential)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--credential-name', required=True, help=u"""The name of the preferred credential.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_preferred_credential(ctx, from_json, managed_database_id, credential_name):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(credential_name, six.string_types) and len(credential_name.strip()) == 0:
        raise click.UsageError('Parameter --credential-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.delete_preferred_credential(
        managed_database_id=managed_database_id,
        credential_name=credential_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@tablespace_group.command(name=cli_util.override('db_management.drop_tablespace.command_name', 'drop'), help=u"""Drops the tablespace specified by tablespaceName within the Managed Database specified by managedDatabaseId. \n[Command Reference](dropTablespace)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--tablespace-name', required=True, help=u"""The name of the tablespace.""")
@cli_util.option('--credential-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-including-contents', type=click.BOOL, help=u"""Specifies whether all the contents of the tablespace being dropped should be dropped.""")
@cli_util.option('--is-dropping-data-files', type=click.BOOL, help=u"""Specifies whether all the associated data files of the tablespace being dropped should be dropped.""")
@cli_util.option('--is-cascade-constraints', type=click.BOOL, help=u"""Specifies whether all the constraints on the tablespace being dropped should be dropped.""")
@json_skeleton_utils.get_cli_json_input_option({'credential-details': {'module': 'database_management', 'class': 'TablespaceAdminCredentialDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'credential-details': {'module': 'database_management', 'class': 'TablespaceAdminCredentialDetails'}}, output_type={'module': 'database_management', 'class': 'TablespaceAdminStatus'})
@cli_util.wrap_exceptions
def drop_tablespace(ctx, from_json, managed_database_id, tablespace_name, credential_details, is_including_contents, is_dropping_data_files, is_cascade_constraints):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(tablespace_name, six.string_types) and len(tablespace_name.strip()) == 0:
        raise click.UsageError('Parameter --tablespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['credentialDetails'] = cli_util.parse_json_parameter("credential_details", credential_details)

    if is_including_contents is not None:
        _details['isIncludingContents'] = is_including_contents

    if is_dropping_data_files is not None:
        _details['isDroppingDataFiles'] = is_dropping_data_files

    if is_cascade_constraints is not None:
        _details['isCascadeConstraints'] = is_cascade_constraints

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.drop_tablespace(
        managed_database_id=managed_database_id,
        tablespace_name=tablespace_name,
        drop_tablespace_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@tablespace_group.command(name=cli_util.override('db_management.drop_tablespace_tablespace_admin_password_credential_details.command_name', 'drop-tablespace-tablespace-admin-password-credential-details'), help=u"""Drops the tablespace specified by tablespaceName within the Managed Database specified by managedDatabaseId. \n[Command Reference](dropTablespace)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--tablespace-name', required=True, help=u"""The name of the tablespace.""")
@cli_util.option('--credential-details-username', required=True, help=u"""The user to connect to the database.""")
@cli_util.option('--credential-details-role', required=True, type=custom_types.CliCaseInsensitiveChoice(["NORMAL", "SYSDBA"]), help=u"""The role of the database user.""")
@cli_util.option('--credential-details-password', required=True, help=u"""The database user's password encoded using BASE64 scheme.""")
@cli_util.option('--is-including-contents', type=click.BOOL, help=u"""Specifies whether all the contents of the tablespace being dropped should be dropped.""")
@cli_util.option('--is-dropping-data-files', type=click.BOOL, help=u"""Specifies whether all the associated data files of the tablespace being dropped should be dropped.""")
@cli_util.option('--is-cascade-constraints', type=click.BOOL, help=u"""Specifies whether all the constraints on the tablespace being dropped should be dropped.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'TablespaceAdminStatus'})
@cli_util.wrap_exceptions
def drop_tablespace_tablespace_admin_password_credential_details(ctx, from_json, managed_database_id, tablespace_name, credential_details_username, credential_details_role, credential_details_password, is_including_contents, is_dropping_data_files, is_cascade_constraints):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(tablespace_name, six.string_types) and len(tablespace_name.strip()) == 0:
        raise click.UsageError('Parameter --tablespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['credentialDetails'] = {}
    _details['credentialDetails']['username'] = credential_details_username
    _details['credentialDetails']['role'] = credential_details_role
    _details['credentialDetails']['password'] = credential_details_password

    if is_including_contents is not None:
        _details['isIncludingContents'] = is_including_contents

    if is_dropping_data_files is not None:
        _details['isDroppingDataFiles'] = is_dropping_data_files

    if is_cascade_constraints is not None:
        _details['isCascadeConstraints'] = is_cascade_constraints

    _details['credentialDetails']['tablespaceAdminCredentialType'] = 'PASSWORD'

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.drop_tablespace(
        managed_database_id=managed_database_id,
        tablespace_name=tablespace_name,
        drop_tablespace_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@tablespace_group.command(name=cli_util.override('db_management.drop_tablespace_tablespace_admin_secret_credential_details.command_name', 'drop-tablespace-tablespace-admin-secret-credential-details'), help=u"""Drops the tablespace specified by tablespaceName within the Managed Database specified by managedDatabaseId. \n[Command Reference](dropTablespace)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--tablespace-name', required=True, help=u"""The name of the tablespace.""")
@cli_util.option('--credential-details-username', required=True, help=u"""The user to connect to the database.""")
@cli_util.option('--credential-details-role', required=True, type=custom_types.CliCaseInsensitiveChoice(["NORMAL", "SYSDBA"]), help=u"""The role of the database user.""")
@cli_util.option('--credential-details-password-secret-id', required=True, help=u"""The [OCID] of the Secret where the database password is stored.""")
@cli_util.option('--is-including-contents', type=click.BOOL, help=u"""Specifies whether all the contents of the tablespace being dropped should be dropped.""")
@cli_util.option('--is-dropping-data-files', type=click.BOOL, help=u"""Specifies whether all the associated data files of the tablespace being dropped should be dropped.""")
@cli_util.option('--is-cascade-constraints', type=click.BOOL, help=u"""Specifies whether all the constraints on the tablespace being dropped should be dropped.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'TablespaceAdminStatus'})
@cli_util.wrap_exceptions
def drop_tablespace_tablespace_admin_secret_credential_details(ctx, from_json, managed_database_id, tablespace_name, credential_details_username, credential_details_role, credential_details_password_secret_id, is_including_contents, is_dropping_data_files, is_cascade_constraints):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(tablespace_name, six.string_types) and len(tablespace_name.strip()) == 0:
        raise click.UsageError('Parameter --tablespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['credentialDetails'] = {}
    _details['credentialDetails']['username'] = credential_details_username
    _details['credentialDetails']['role'] = credential_details_role
    _details['credentialDetails']['passwordSecretId'] = credential_details_password_secret_id

    if is_including_contents is not None:
        _details['isIncludingContents'] = is_including_contents

    if is_dropping_data_files is not None:
        _details['isDroppingDataFiles'] = is_dropping_data_files

    if is_cascade_constraints is not None:
        _details['isCascadeConstraints'] = is_cascade_constraints

    _details['credentialDetails']['tablespaceAdminCredentialType'] = 'SECRET'

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.drop_tablespace(
        managed_database_id=managed_database_id,
        tablespace_name=tablespace_name,
        drop_tablespace_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@snapshot_details_group.command(name=cli_util.override('db_management.generate_awr_snapshot.command_name', 'generate-awr-snapshot'), help=u"""Creates an AWR snapshot for the target database. \n[Command Reference](generateAwrSnapshot)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'SnapshotDetails'})
@cli_util.wrap_exceptions
def generate_awr_snapshot(ctx, from_json, managed_database_id):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.generate_awr_snapshot(
        managed_database_id=managed_database_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.get_awr_db_report.command_name', 'get-awr-db-report'), help=u"""Gets the AWR report for the specific database. \n[Command Reference](getAwrDbReport)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--awr-db-id', required=True, help=u"""The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs""")
@cli_util.option('--inst-nums', multiple=True, help=u"""The optional multiple value query parameter to filter the database instance numbers.""")
@cli_util.option('--begin-sn-id-greater-than-or-equal-to', type=click.INT, help=u"""The optional greater than or equal to filter on the snapshot ID.""")
@cli_util.option('--end-sn-id-less-than-or-equal-to', type=click.INT, help=u"""The optional less than or equal to query parameter to filter the snapshot ID.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--report-type', type=custom_types.CliCaseInsensitiveChoice(["AWR", "ASH"]), help=u"""The query parameter to filter the AWR report types.""")
@cli_util.option('--container-id', type=click.INT, help=u"""The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges""")
@cli_util.option('--report-format', type=custom_types.CliCaseInsensitiveChoice(["HTML", "TEXT"]), help=u"""The format of the AWR report.""")
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
        kwargs['inst_nums'] = inst_nums
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


@managed_database_group.command(name=cli_util.override('db_management.get_awr_db_sql_report.command_name', 'get-awr-db-sql-report'), help=u"""Gets the SQL health check report for one SQL of the specific database. \n[Command Reference](getAwrDbSqlReport)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--awr-db-id', required=True, help=u"""The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs""")
@cli_util.option('--sql-id', required=True, help=u"""The parameter to filter SQL by ID. Note that the SQL ID is generated internally by Oracle for each SQL statement and can be retrieved from AWR Report API (/managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbReport) or Performance Hub API (/internal/managedDatabases/{managedDatabaseId}/actions/retrievePerformanceData)""")
@cli_util.option('--inst-num', help=u"""The optional single value query parameter to filter the database instance number.""")
@cli_util.option('--begin-sn-id-greater-than-or-equal-to', type=click.INT, help=u"""The optional greater than or equal to filter on the snapshot ID.""")
@cli_util.option('--end-sn-id-less-than-or-equal-to', type=click.INT, help=u"""The optional less than or equal to query parameter to filter the snapshot ID.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--report-format', type=custom_types.CliCaseInsensitiveChoice(["HTML", "TEXT"]), help=u"""The format of the AWR report.""")
@cli_util.option('--container-id', type=click.INT, help=u"""The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'AwrDbSqlReport'})
@cli_util.wrap_exceptions
def get_awr_db_sql_report(ctx, from_json, managed_database_id, awr_db_id, sql_id, inst_num, begin_sn_id_greater_than_or_equal_to, end_sn_id_less_than_or_equal_to, time_greater_than_or_equal_to, time_less_than_or_equal_to, report_format, container_id):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(awr_db_id, six.string_types) and len(awr_db_id.strip()) == 0:
        raise click.UsageError('Parameter --awr-db-id cannot be whitespace or empty string')

    kwargs = {}
    if inst_num is not None:
        kwargs['inst_num'] = inst_num
    if begin_sn_id_greater_than_or_equal_to is not None:
        kwargs['begin_sn_id_greater_than_or_equal_to'] = begin_sn_id_greater_than_or_equal_to
    if end_sn_id_less_than_or_equal_to is not None:
        kwargs['end_sn_id_less_than_or_equal_to'] = end_sn_id_less_than_or_equal_to
    if time_greater_than_or_equal_to is not None:
        kwargs['time_greater_than_or_equal_to'] = time_greater_than_or_equal_to
    if time_less_than_or_equal_to is not None:
        kwargs['time_less_than_or_equal_to'] = time_less_than_or_equal_to
    if report_format is not None:
        kwargs['report_format'] = report_format
    if container_id is not None:
        kwargs['container_id'] = container_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.get_awr_db_sql_report(
        managed_database_id=managed_database_id,
        awr_db_id=awr_db_id,
        sql_id=sql_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cluster_cache_metric_group.command(name=cli_util.override('db_management.get_cluster_cache_metric.command_name', 'get'), help=u"""Gets the metrics related to cluster cache for the Oracle Real Application Clusters (Oracle RAC) database specified by managedDatabaseId. \n[Command Reference](getClusterCacheMetric)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--start-time', required=True, help=u"""The start time of the time range to retrieve the health metrics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".""")
@cli_util.option('--end-time', required=True, help=u"""The end time of the time range to retrieve the health metrics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'ClusterCacheMetric'})
@cli_util.wrap_exceptions
def get_cluster_cache_metric(ctx, from_json, managed_database_id, start_time, end_time):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.get_cluster_cache_metric(
        managed_database_id=managed_database_id,
        start_time=start_time,
        end_time=end_time,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_fleet_health_metrics_group.command(name=cli_util.override('db_management.get_database_fleet_health_metrics.command_name', 'get'), help=u"""Gets the health metrics for a fleet of databases in a compartment or in a Managed Database Group. Either the CompartmentId or the ManagedDatabaseGroupId query parameters must be provided to retrieve the health metrics. \n[Command Reference](getDatabaseFleetHealthMetrics)""")
@cli_util.option('--compare-baseline-time', required=True, help=u"""The baseline time for metrics comparison.""")
@cli_util.option('--compare-target-time', required=True, help=u"""The target time for metrics comparison.""")
@cli_util.option('--managed-database-group-id', help=u"""The [OCID] of the Managed Database Group.""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment.""")
@cli_util.option('--compare-type', type=custom_types.CliCaseInsensitiveChoice(["HOUR", "DAY", "WEEK"]), help=u"""The time window used for metrics comparison.""")
@cli_util.option('--filter-by-metric-names', help=u"""The filter used to retrieve a specific set of metrics by passing the desired metric names with a comma separator. Note that, by default, the service returns all supported metrics.""")
@cli_util.option('--filter-by-database-type', help=u"""The filter used to filter the databases in the fleet by a specific Oracle Database type.""")
@cli_util.option('--filter-by-database-sub-type', help=u"""The filter used to filter the databases in the fleet by a specific Oracle Database subtype.""")
@cli_util.option('--filter-by-database-deployment-type', help=u"""The filter used to filter the databases in the fleet by a specific Oracle Database deployment type.""")
@cli_util.option('--filter-by-database-version', help=u"""The filter used to filter the databases in the fleet by a specific Oracle Database version.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'DatabaseFleetHealthMetrics'})
@cli_util.wrap_exceptions
def get_database_fleet_health_metrics(ctx, from_json, compare_baseline_time, compare_target_time, managed_database_group_id, compartment_id, compare_type, filter_by_metric_names, filter_by_database_type, filter_by_database_sub_type, filter_by_database_deployment_type, filter_by_database_version):

    kwargs = {}
    if managed_database_group_id is not None:
        kwargs['managed_database_group_id'] = managed_database_group_id
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if compare_type is not None:
        kwargs['compare_type'] = compare_type
    if filter_by_metric_names is not None:
        kwargs['filter_by_metric_names'] = filter_by_metric_names
    if filter_by_database_type is not None:
        kwargs['filter_by_database_type'] = filter_by_database_type
    if filter_by_database_sub_type is not None:
        kwargs['filter_by_database_sub_type'] = filter_by_database_sub_type
    if filter_by_database_deployment_type is not None:
        kwargs['filter_by_database_deployment_type'] = filter_by_database_deployment_type
    if filter_by_database_version is not None:
        kwargs['filter_by_database_version'] = filter_by_database_version
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.get_database_fleet_health_metrics(
        compare_baseline_time=compare_baseline_time,
        compare_target_time=compare_target_time,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_home_metrics_group.command(name=cli_util.override('db_management.get_database_home_metrics.command_name', 'get'), help=u"""Gets a summary of the activity and resource usage metrics like DB Time, CPU, User I/O, Wait, Storage, and Memory for a Managed Database. \n[Command Reference](getDatabaseHomeMetrics)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--start-time', required=True, help=u"""The start time of the time range to retrieve the health metrics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".""")
@cli_util.option('--end-time', required=True, help=u"""The end time of the time range to retrieve the health metrics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'DatabaseHomeMetrics'})
@cli_util.wrap_exceptions
def get_database_home_metrics(ctx, from_json, managed_database_id, start_time, end_time):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.get_database_home_metrics(
        managed_database_id=managed_database_id,
        start_time=start_time,
        end_time=end_time,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@db_management_private_endpoint_group.command(name=cli_util.override('db_management.get_db_management_private_endpoint.command_name', 'get'), help=u"""Gets the details of a specific Database Management private endpoint. \n[Command Reference](getDbManagementPrivateEndpoint)""")
@cli_util.option('--db-management-private-endpoint-id', required=True, help=u"""The [OCID] of the Database Management private endpoint.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'DbManagementPrivateEndpoint'})
@cli_util.wrap_exceptions
def get_db_management_private_endpoint(ctx, from_json, db_management_private_endpoint_id):

    if isinstance(db_management_private_endpoint_id, six.string_types) and len(db_management_private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --db-management-private-endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.get_db_management_private_endpoint(
        db_management_private_endpoint_id=db_management_private_endpoint_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('db_management.get_job.command_name', 'get'), help=u"""Gets the details for the job specified by jobId. \n[Command Reference](getJob)""")
@cli_util.option('--job-id', required=True, help=u"""The identifier of the job.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'Job'})
@cli_util.wrap_exceptions
def get_job(ctx, from_json, job_id):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.get_job(
        job_id=job_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@job_execution_group.command(name=cli_util.override('db_management.get_job_execution.command_name', 'get'), help=u"""Gets the details for the job execution specified by jobExecutionId. \n[Command Reference](getJobExecution)""")
@cli_util.option('--job-execution-id', required=True, help=u"""The identifier of the job execution.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'JobExecution'})
@cli_util.wrap_exceptions
def get_job_execution(ctx, from_json, job_execution_id):

    if isinstance(job_execution_id, six.string_types) and len(job_execution_id.strip()) == 0:
        raise click.UsageError('Parameter --job-execution-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.get_job_execution(
        job_execution_id=job_execution_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@job_run_group.command(name=cli_util.override('db_management.get_job_run.command_name', 'get'), help=u"""Gets the details for the job run specified by jobRunId. \n[Command Reference](getJobRun)""")
@cli_util.option('--job-run-id', required=True, help=u"""The identifier of the job run.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'JobRun'})
@cli_util.wrap_exceptions
def get_job_run(ctx, from_json, job_run_id):

    if isinstance(job_run_id, six.string_types) and len(job_run_id.strip()) == 0:
        raise click.UsageError('Parameter --job-run-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.get_job_run(
        job_run_id=job_run_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.get_managed_database.command_name', 'get'), help=u"""Gets the details for the Managed Database specified by managedDatabaseId. \n[Command Reference](getManagedDatabase)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'ManagedDatabase'})
@cli_util.wrap_exceptions
def get_managed_database(ctx, from_json, managed_database_id):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.get_managed_database(
        managed_database_id=managed_database_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group_group.command(name=cli_util.override('db_management.get_managed_database_group.command_name', 'get'), help=u"""Gets the details for the Managed Database Group specified by managedDatabaseGroupId. \n[Command Reference](getManagedDatabaseGroup)""")
@cli_util.option('--managed-database-group-id', required=True, help=u"""The [OCID] of the Managed Database Group.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'ManagedDatabaseGroup'})
@cli_util.wrap_exceptions
def get_managed_database_group(ctx, from_json, managed_database_group_id):

    if isinstance(managed_database_group_id, six.string_types) and len(managed_database_group_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-group-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.get_managed_database_group(
        managed_database_group_id=managed_database_group_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.get_optimizer_statistics_advisor_execution.command_name', 'get-optimizer-statistics-advisor-execution'), help=u"""Gets a comprehensive report of the Optimizer Statistics Advisor execution, which includes details of the Managed Database, findings, recommendations, rationale, and examples. \n[Command Reference](getOptimizerStatisticsAdvisorExecution)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--execution-name', required=True, help=u"""The name of the Optimizer Statistics Advisor execution.""")
@cli_util.option('--task-name', required=True, help=u"""The name of the optimizer statistics collection execution task.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'OptimizerStatisticsAdvisorExecution'})
@cli_util.wrap_exceptions
def get_optimizer_statistics_advisor_execution(ctx, from_json, managed_database_id, execution_name, task_name):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(execution_name, six.string_types) and len(execution_name.strip()) == 0:
        raise click.UsageError('Parameter --execution-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.get_optimizer_statistics_advisor_execution(
        managed_database_id=managed_database_id,
        execution_name=execution_name,
        task_name=task_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.get_optimizer_statistics_advisor_execution_script.command_name', 'get-optimizer-statistics-advisor-execution-script'), help=u"""Gets the Oracle system-generated script for the specified Optimizer Statistics Advisor execution. \n[Command Reference](getOptimizerStatisticsAdvisorExecutionScript)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--execution-name', required=True, help=u"""The name of the Optimizer Statistics Advisor execution.""")
@cli_util.option('--task-name', required=True, help=u"""The name of the optimizer statistics collection execution task.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'OptimizerStatisticsAdvisorExecutionScript'})
@cli_util.wrap_exceptions
def get_optimizer_statistics_advisor_execution_script(ctx, from_json, managed_database_id, execution_name, task_name):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(execution_name, six.string_types) and len(execution_name.strip()) == 0:
        raise click.UsageError('Parameter --execution-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.get_optimizer_statistics_advisor_execution_script(
        managed_database_id=managed_database_id,
        execution_name=execution_name,
        task_name=task_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.get_optimizer_statistics_collection_operation.command_name', 'get-optimizer-statistics-collection-operation'), help=u"""Gets a detailed report of the Optimizer Statistics Collection operation for the specified Managed Database. \n[Command Reference](getOptimizerStatisticsCollectionOperation)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--optimizer-statistics-collection-operation-id', required=True, type=click.FLOAT, help=u"""The ID of the Optimizer Statistics Collection operation.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'OptimizerStatisticsCollectionOperation'})
@cli_util.wrap_exceptions
def get_optimizer_statistics_collection_operation(ctx, from_json, managed_database_id, optimizer_statistics_collection_operation_id):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(optimizer_statistics_collection_operation_id, six.string_types) and len(optimizer_statistics_collection_operation_id.strip()) == 0:
        raise click.UsageError('Parameter --optimizer-statistics-collection-operation-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.get_optimizer_statistics_collection_operation(
        managed_database_id=managed_database_id,
        optimizer_statistics_collection_operation_id=optimizer_statistics_collection_operation_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@pdb_metrics_group.command(name=cli_util.override('db_management.get_pdb_metrics.command_name', 'get'), help=u"""Gets a summary of the resource usage metrics such as CPU, User I/O, and Storage for each PDB within a specific CDB. If comparmentId is specified, then the metrics for each PDB (within the CDB) in the specified compartment are retrieved. If compartmentId is not specified, then the metrics for all the PDBs within the CDB are retrieved. \n[Command Reference](getPdbMetrics)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--start-time', required=True, help=u"""The start time of the time range to retrieve the health metrics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".""")
@cli_util.option('--end-time', required=True, help=u"""The end time of the time range to retrieve the health metrics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment.""")
@cli_util.option('--compare-type', type=custom_types.CliCaseInsensitiveChoice(["HOUR", "DAY", "WEEK"]), help=u"""The time window used for metrics comparison.""")
@cli_util.option('--filter-by-metric-names', help=u"""The filter used to retrieve a specific set of metrics by passing the desired metric names with a comma separator. Note that, by default, the service returns all supported metrics.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'PdbMetrics'})
@cli_util.wrap_exceptions
def get_pdb_metrics(ctx, from_json, managed_database_id, start_time, end_time, compartment_id, compare_type, filter_by_metric_names):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if compare_type is not None:
        kwargs['compare_type'] = compare_type
    if filter_by_metric_names is not None:
        kwargs['filter_by_metric_names'] = filter_by_metric_names
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.get_pdb_metrics(
        managed_database_id=managed_database_id,
        start_time=start_time,
        end_time=end_time,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@preferred_credential_group.command(name=cli_util.override('db_management.get_preferred_credential.command_name', 'get'), help=u"""Gets the preferred credential details for a Managed Database based on credentialName. \n[Command Reference](getPreferredCredential)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--credential-name', required=True, help=u"""The name of the preferred credential.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'PreferredCredential'})
@cli_util.wrap_exceptions
def get_preferred_credential(ctx, from_json, managed_database_id, credential_name):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(credential_name, six.string_types) and len(credential_name.strip()) == 0:
        raise click.UsageError('Parameter --credential-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.get_preferred_credential(
        managed_database_id=managed_database_id,
        credential_name=credential_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@tablespace_group.command(name=cli_util.override('db_management.get_tablespace.command_name', 'get'), help=u"""Gets the details of the tablespace specified by tablespaceName within the Managed Database specified by managedDatabaseId. \n[Command Reference](getTablespace)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--tablespace-name', required=True, help=u"""The name of the tablespace.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'Tablespace'})
@cli_util.wrap_exceptions
def get_tablespace(ctx, from_json, managed_database_id, tablespace_name):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(tablespace_name, six.string_types) and len(tablespace_name.strip()) == 0:
        raise click.UsageError('Parameter --tablespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.get_tablespace(
        managed_database_id=managed_database_id,
        tablespace_name=tablespace_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.get_user.command_name', 'get-user'), help=u"""Gets the details of the user specified by managedDatabaseId and userName. \n[Command Reference](getUser)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--user-name', required=True, help=u"""The name of the user whose details are to be viewed.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'User'})
@cli_util.wrap_exceptions
def get_user(ctx, from_json, managed_database_id, user_name):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(user_name, six.string_types) and len(user_name.strip()) == 0:
        raise click.UsageError('Parameter --user-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.get_user(
        managed_database_id=managed_database_id,
        user_name=user_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('db_management.get_work_request.command_name', 'get'), help=u"""Gets the status of the work request with the given Work Request ID \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the asynchronous work request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.implement_optimizer_statistics_advisor_recommendations.command_name', 'implement-optimizer-statistics-advisor-recommendations'), help=u"""Asynchronously implements the findings and recommendations of the Optimizer Statistics Advisor execution. \n[Command Reference](implementOptimizerStatisticsAdvisorRecommendations)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--execution-name', required=True, help=u"""The name of the Optimizer Statistics Advisor execution.""")
@cli_util.option('--task-name', required=True, help=u"""The name of the task.""")
@cli_util.option('--job-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'job-details': {'module': 'database_management', 'class': 'ImplementOptimizerStatisticsAdvisorRecommendationsJob'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'job-details': {'module': 'database_management', 'class': 'ImplementOptimizerStatisticsAdvisorRecommendationsJob'}}, output_type={'module': 'database_management', 'class': 'Job'})
@cli_util.wrap_exceptions
def implement_optimizer_statistics_advisor_recommendations(ctx, from_json, managed_database_id, execution_name, task_name, job_details):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(execution_name, six.string_types) and len(execution_name.strip()) == 0:
        raise click.UsageError('Parameter --execution-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['taskName'] = task_name
    _details['jobDetails'] = cli_util.parse_json_parameter("job_details", job_details)

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.implement_optimizer_statistics_advisor_recommendations(
        managed_database_id=managed_database_id,
        execution_name=execution_name,
        implement_optimizer_statistics_advisor_recommendations_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.list_asm_properties.command_name', 'list-asm-properties'), help=u"""Gets the list of ASM properties for the specified managedDatabaseId. \n[Command Reference](listAsmProperties)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "NAME"]), help=u"""The field to sort information by. Only one sortOrder can be used. The default sort order for \u2018TIMECREATED\u2019 is descending and the default sort order for \u2018NAME\u2019 is ascending. The \u2018NAME\u2019 sort order is case-sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the default order.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'AsmPropertyCollection'})
@cli_util.wrap_exceptions
def list_asm_properties(ctx, from_json, all_pages, page_size, managed_database_id, name, sort_by, sort_order, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_asm_properties,
            managed_database_id=managed_database_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_asm_properties,
            limit,
            page_size,
            managed_database_id=managed_database_id,
            **kwargs
        )
    else:
        result = client.list_asm_properties(
            managed_database_id=managed_database_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@associated_database_summary_group.command(name=cli_util.override('db_management.list_associated_databases.command_name', 'list-associated-databases'), help=u"""Gets the list of databases using a specific Database Management private endpoint. \n[Command Reference](listAssociatedDatabases)""")
@cli_util.option('--db-management-private-endpoint-id', required=True, help=u"""The [OCID] of the Database Management private endpoint.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the default order.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeRegistered"]), help=u"""The option to sort databases using a specific Database Management private endpoint.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'AssociatedDatabaseCollection'})
@cli_util.wrap_exceptions
def list_associated_databases(ctx, from_json, all_pages, page_size, db_management_private_endpoint_id, compartment_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(db_management_private_endpoint_id, six.string_types) and len(db_management_private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --db-management-private-endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_associated_databases,
            db_management_private_endpoint_id=db_management_private_endpoint_id,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_associated_databases,
            limit,
            page_size,
            db_management_private_endpoint_id=db_management_private_endpoint_id,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_associated_databases(
            db_management_private_endpoint_id=db_management_private_endpoint_id,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.list_awr_db_snapshots.command_name', 'list-awr-db-snapshots'), help=u"""Lists AWR snapshots for the specified database in the AWR. \n[Command Reference](listAwrDbSnapshots)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--awr-db-id', required=True, help=u"""The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs""")
@cli_util.option('--inst-num', help=u"""The optional single value query parameter to filter the database instance number.""")
@cli_util.option('--begin-sn-id-greater-than-or-equal-to', type=click.INT, help=u"""The optional greater than or equal to filter on the snapshot ID.""")
@cli_util.option('--end-sn-id-less-than-or-equal-to', type=click.INT, help=u"""The optional less than or equal to query parameter to filter the snapshot ID.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--container-id', type=click.INT, help=u"""The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_BEGIN", "SNAPSHOT_ID"]), help=u"""The option to sort the AWR snapshot summary data.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the default order.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'AwrDbSnapshotCollection'})
@cli_util.wrap_exceptions
def list_awr_db_snapshots(ctx, from_json, all_pages, page_size, managed_database_id, awr_db_id, inst_num, begin_sn_id_greater_than_or_equal_to, end_sn_id_less_than_or_equal_to, time_greater_than_or_equal_to, time_less_than_or_equal_to, container_id, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(awr_db_id, six.string_types) and len(awr_db_id.strip()) == 0:
        raise click.UsageError('Parameter --awr-db-id cannot be whitespace or empty string')

    kwargs = {}
    if inst_num is not None:
        kwargs['inst_num'] = inst_num
    if begin_sn_id_greater_than_or_equal_to is not None:
        kwargs['begin_sn_id_greater_than_or_equal_to'] = begin_sn_id_greater_than_or_equal_to
    if end_sn_id_less_than_or_equal_to is not None:
        kwargs['end_sn_id_less_than_or_equal_to'] = end_sn_id_less_than_or_equal_to
    if time_greater_than_or_equal_to is not None:
        kwargs['time_greater_than_or_equal_to'] = time_greater_than_or_equal_to
    if time_less_than_or_equal_to is not None:
        kwargs['time_less_than_or_equal_to'] = time_less_than_or_equal_to
    if container_id is not None:
        kwargs['container_id'] = container_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_awr_db_snapshots,
            managed_database_id=managed_database_id,
            awr_db_id=awr_db_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_awr_db_snapshots,
            limit,
            page_size,
            managed_database_id=managed_database_id,
            awr_db_id=awr_db_id,
            **kwargs
        )
    else:
        result = client.list_awr_db_snapshots(
            managed_database_id=managed_database_id,
            awr_db_id=awr_db_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.list_awr_dbs.command_name', 'list-awr-dbs'), help=u"""Gets the list of databases and their snapshot summary details available in the AWR of the specified Managed Database. \n[Command Reference](listAwrDbs)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--name', help=u"""The optional single value query parameter to filter the entity name.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["END_INTERVAL_TIME", "NAME"]), help=u"""The option to sort the AWR summary data.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the default order.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'AwrDbCollection'})
@cli_util.wrap_exceptions
def list_awr_dbs(ctx, from_json, all_pages, page_size, managed_database_id, name, time_greater_than_or_equal_to, time_less_than_or_equal_to, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
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
    client = cli_util.build_client('database_management', 'db_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_awr_dbs,
            managed_database_id=managed_database_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_awr_dbs,
            limit,
            page_size,
            managed_database_id=managed_database_id,
            **kwargs
        )
    else:
        result = client.list_awr_dbs(
            managed_database_id=managed_database_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.list_consumer_group_privileges.command_name', 'list-consumer-group-privileges'), help=u"""Gets the list of consumer group privileges granted to a specific user. \n[Command Reference](listConsumerGroupPrivileges)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--user-name', required=True, help=u"""The name of the user whose details are to be viewed.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["NAME"]), help=u"""The field to sort information by. Only one sortOrder can be used. The default sort order for \u2018NAME\u2019 is ascending. The \u2018NAME\u2019 sort order is case-sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the default order.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'ConsumerGroupPrivilegeCollection'})
@cli_util.wrap_exceptions
def list_consumer_group_privileges(ctx, from_json, all_pages, page_size, managed_database_id, user_name, name, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(user_name, six.string_types) and len(user_name.strip()) == 0:
        raise click.UsageError('Parameter --user-name cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_consumer_group_privileges,
            managed_database_id=managed_database_id,
            user_name=user_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_consumer_group_privileges,
            limit,
            page_size,
            managed_database_id=managed_database_id,
            user_name=user_name,
            **kwargs
        )
    else:
        result = client.list_consumer_group_privileges(
            managed_database_id=managed_database_id,
            user_name=user_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.list_data_access_containers.command_name', 'list-data-access-containers'), help=u"""Gets the list of containers for a specific user. This is only applicable if ALL_CONTAINERS !='Y'. \n[Command Reference](listDataAccessContainers)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--user-name', required=True, help=u"""The name of the user whose details are to be viewed.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["NAME"]), help=u"""The field to sort information by. Only one sortOrder can be used. The default sort order for \u2018NAME\u2019 is ascending. The \u2018NAME\u2019 sort order is case-sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the default order.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'DataAccessContainerCollection'})
@cli_util.wrap_exceptions
def list_data_access_containers(ctx, from_json, all_pages, page_size, managed_database_id, user_name, name, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(user_name, six.string_types) and len(user_name.strip()) == 0:
        raise click.UsageError('Parameter --user-name cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_data_access_containers,
            managed_database_id=managed_database_id,
            user_name=user_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_data_access_containers,
            limit,
            page_size,
            managed_database_id=managed_database_id,
            user_name=user_name,
            **kwargs
        )
    else:
        result = client.list_data_access_containers(
            managed_database_id=managed_database_id,
            user_name=user_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.list_database_parameters.command_name', 'list-database-parameters'), help=u"""Gets the list of database parameters for the specified Managed Database. The parameters are listed in alphabetical order, along with their current values. \n[Command Reference](listDatabaseParameters)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--source', type=custom_types.CliCaseInsensitiveChoice(["CURRENT", "SPFILE"]), help=u"""The source used to list database parameters. `CURRENT` is used to get the database parameters that are currently in effect for the database instance. `SPFILE` is used to list parameters from the server parameter file. Default is `CURRENT`.""")
@cli_util.option('--name', help=u"""A filter to return all parameters that have the text given in their names.""")
@cli_util.option('--is-allowed-values-included', type=click.BOOL, help=u"""When true, results include a list of valid values for parameters (if applicable).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["NAME"]), help=u"""The field to sort information by. Only one sortOrder can be used. The default sort order for `NAME` is ascending and it is case-sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the default order.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'DatabaseParametersCollection'})
@cli_util.wrap_exceptions
def list_database_parameters(ctx, from_json, all_pages, managed_database_id, source, name, is_allowed_values_included, sort_by, sort_order):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    if source is not None:
        kwargs['source'] = source
    if name is not None:
        kwargs['name'] = name
    if is_allowed_values_included is not None:
        kwargs['is_allowed_values_included'] = is_allowed_values_included
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.list_database_parameters(
        managed_database_id=managed_database_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@db_management_private_endpoint_group.command(name=cli_util.override('db_management.list_db_management_private_endpoints.command_name', 'list'), help=u"""Gets a list of Database Management private endpoints. \n[Command Reference](listDbManagementPrivateEndpoints)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name.""")
@cli_util.option('--vcn-id', help=u"""The [OCID] of the VCN.""")
@cli_util.option('--is-cluster', type=click.BOOL, help=u"""The option to filter Database Management private endpoints that can used for Oracle Databases in a cluster. This should be used along with the vcnId query parameter.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The lifecycle state of a resource.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the default order.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "NAME"]), help=u"""The field to sort information by. Only one sortOrder can be used. The default sort order for \u2018TIMECREATED\u2019 is descending and the default sort order for \u2018NAME\u2019 is ascending. The \u2018NAME\u2019 sort order is case-sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'DbManagementPrivateEndpointCollection'})
@cli_util.wrap_exceptions
def list_db_management_private_endpoints(ctx, from_json, all_pages, page_size, compartment_id, name, vcn_id, is_cluster, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if vcn_id is not None:
        kwargs['vcn_id'] = vcn_id
    if is_cluster is not None:
        kwargs['is_cluster'] = is_cluster
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_db_management_private_endpoints,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_db_management_private_endpoints,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_db_management_private_endpoints(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@job_execution_group.command(name=cli_util.override('db_management.list_job_executions.command_name', 'list'), help=u"""Gets the job execution for a specific ID or the list of job executions for a job, job run, Managed Database or Managed Database Group in a specific compartment. Only one of the parameters, ID, jobId, jobRunId, managedDatabaseId or managedDatabaseGroupId should be provided. If none of these parameters is provided, all the job executions in the compartment are listed. Job executions can also be filtered based on the name and status parameters. \n[Command Reference](listJobExecutions)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--id', help=u"""The identifier of the resource.""")
@cli_util.option('--job-id', help=u"""The identifier of the job.""")
@cli_util.option('--managed-database-id', help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--managed-database-group-id', help=u"""The [OCID] of the Managed Database Group.""")
@cli_util.option('--status', help=u"""The status of the job execution.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "NAME"]), help=u"""The field to sort information by. Only one sortOrder can be used. The default sort order for \u2018TIMECREATED\u2019 is descending and the default sort order for \u2018NAME\u2019 is ascending. The \u2018NAME\u2019 sort order is case-sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the default order.""")
@cli_util.option('--job-run-id', help=u"""The identifier of the job run.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'JobExecutionCollection'})
@cli_util.wrap_exceptions
def list_job_executions(ctx, from_json, all_pages, page_size, compartment_id, id, job_id, managed_database_id, managed_database_group_id, status, name, limit, page, sort_by, sort_order, job_run_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if job_id is not None:
        kwargs['job_id'] = job_id
    if managed_database_id is not None:
        kwargs['managed_database_id'] = managed_database_id
    if managed_database_group_id is not None:
        kwargs['managed_database_group_id'] = managed_database_group_id
    if status is not None:
        kwargs['status'] = status
    if name is not None:
        kwargs['name'] = name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if job_run_id is not None:
        kwargs['job_run_id'] = job_run_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_job_executions,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_job_executions,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_job_executions(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@job_run_group.command(name=cli_util.override('db_management.list_job_runs.command_name', 'list'), help=u"""Gets the job run for a specific ID or the list of job runs for a job, Managed Database or Managed Database Group in a specific compartment. Only one of the parameters, ID, jobId, managedDatabaseId, or managedDatabaseGroupId should be provided. If none of these parameters is provided, all the job runs in the compartment are listed. Job runs can also be filtered based on name and runStatus parameters. \n[Command Reference](listJobRuns)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--id', help=u"""The identifier of the resource.""")
@cli_util.option('--job-id', help=u"""The identifier of the job.""")
@cli_util.option('--managed-database-id', help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--managed-database-group-id', help=u"""The [OCID] of the Managed Database Group.""")
@cli_util.option('--run-status', help=u"""The status of the job run.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "NAME"]), help=u"""The field to sort information by. Only one sortOrder can be used. The default sort order for \u2018TIMECREATED\u2019 is descending and the default sort order for \u2018NAME\u2019 is ascending. The \u2018NAME\u2019 sort order is case-sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the default order.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'JobRunCollection'})
@cli_util.wrap_exceptions
def list_job_runs(ctx, from_json, all_pages, page_size, compartment_id, id, job_id, managed_database_id, managed_database_group_id, run_status, name, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if job_id is not None:
        kwargs['job_id'] = job_id
    if managed_database_id is not None:
        kwargs['managed_database_id'] = managed_database_id
    if managed_database_group_id is not None:
        kwargs['managed_database_group_id'] = managed_database_group_id
    if run_status is not None:
        kwargs['run_status'] = run_status
    if name is not None:
        kwargs['name'] = name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_job_runs,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_job_runs,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_job_runs(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('db_management.list_jobs.command_name', 'list'), help=u"""Gets the job for a specific ID or the list of jobs for a Managed Database or Managed Database Group in a specific compartment. Only one of the parameters, ID, managedDatabaseId or managedDatabaseGroupId, should be provided. If none of these parameters is provided, all the jobs in the compartment are listed. Jobs can also be filtered based on the name and lifecycleState parameters. \n[Command Reference](listJobs)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--id', help=u"""The identifier of the resource.""")
@cli_util.option('--managed-database-group-id', help=u"""The [OCID] of the Managed Database Group.""")
@cli_util.option('--managed-database-id', help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), help=u"""The lifecycle state of the job.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "NAME"]), help=u"""The field to sort information by. Only one sortOrder can be used. The default sort order for \u2018TIMECREATED\u2019 is descending and the default sort order for \u2018NAME\u2019 is ascending. The \u2018NAME\u2019 sort order is case-sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the default order.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'JobCollection'})
@cli_util.wrap_exceptions
def list_jobs(ctx, from_json, all_pages, page_size, compartment_id, id, managed_database_group_id, managed_database_id, name, lifecycle_state, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if managed_database_group_id is not None:
        kwargs['managed_database_group_id'] = managed_database_group_id
    if managed_database_id is not None:
        kwargs['managed_database_id'] = managed_database_id
    if name is not None:
        kwargs['name'] = name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_jobs,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_jobs,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_jobs(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_database_group_group.command(name=cli_util.override('db_management.list_managed_database_groups.command_name', 'list'), help=u"""Gets the Managed Database Group for a specific ID or the list of Managed Database Groups in a specific compartment. Managed Database Groups can also be filtered based on the name parameter. Only one of the parameters, ID or name should be provided. If none of these parameters is provided, all the Managed Database Groups in the compartment are listed. \n[Command Reference](listManagedDatabaseGroups)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--id', help=u"""The identifier of the resource.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The lifecycle state of a resource.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "NAME"]), help=u"""The field to sort information by. Only one sortOrder can be used. The default sort order for \u2018TIMECREATED\u2019 is descending and the default sort order for \u2018NAME\u2019 is ascending. The \u2018NAME\u2019 sort order is case-sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the default order.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'ManagedDatabaseGroupCollection'})
@cli_util.wrap_exceptions
def list_managed_database_groups(ctx, from_json, all_pages, page_size, compartment_id, id, name, lifecycle_state, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if name is not None:
        kwargs['name'] = name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_managed_database_groups,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_managed_database_groups,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_managed_database_groups(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.list_managed_databases.command_name', 'list'), help=u"""Gets the Managed Database for a specific ID or the list of Managed Databases in a specific compartment. Managed Databases can be filtered based on the name parameter. Only one of the parameters, ID or name should be provided. If neither of these parameters is provided, all the Managed Databases in the compartment are listed. Managed Databases can also be filtered based on the deployment type and management option. If the deployment type is not specified or if it is `ONPREMISE`, then the management option is not considered and Managed Databases with `ADVANCED` management option are listed. \n[Command Reference](listManagedDatabases)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--id', help=u"""The identifier of the resource.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name.""")
@cli_util.option('--management-option', type=custom_types.CliCaseInsensitiveChoice(["BASIC", "ADVANCED"]), help=u"""A filter to return Managed Databases with the specified management option.""")
@cli_util.option('--deployment-type', type=custom_types.CliCaseInsensitiveChoice(["ONPREMISE", "BM", "VM", "EXADATA", "EXADATA_CC", "AUTONOMOUS"]), help=u"""A filter to return Managed Databases of the specified deployment type.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "NAME"]), help=u"""The field to sort information by. Only one sortOrder can be used. The default sort order for \u2018TIMECREATED\u2019 is descending and the default sort order for \u2018NAME\u2019 is ascending. The \u2018NAME\u2019 sort order is case-sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the default order.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'ManagedDatabaseCollection'})
@cli_util.wrap_exceptions
def list_managed_databases(ctx, from_json, all_pages, page_size, compartment_id, id, name, management_option, deployment_type, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if name is not None:
        kwargs['name'] = name
    if management_option is not None:
        kwargs['management_option'] = management_option
    if deployment_type is not None:
        kwargs['deployment_type'] = deployment_type
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_managed_databases,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_managed_databases,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_managed_databases(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.list_object_privileges.command_name', 'list-object-privileges'), help=u"""Gets the list of object privileges granted to a specific user. \n[Command Reference](listObjectPrivileges)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--user-name', required=True, help=u"""The name of the user whose details are to be viewed.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["NAME"]), help=u"""The field to sort information by. Only one sortOrder can be used. The default sort order for \u2018NAME\u2019 is ascending. The \u2018NAME\u2019 sort order is case-sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the default order.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'ObjectPrivilegeCollection'})
@cli_util.wrap_exceptions
def list_object_privileges(ctx, from_json, all_pages, page_size, managed_database_id, user_name, name, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(user_name, six.string_types) and len(user_name.strip()) == 0:
        raise click.UsageError('Parameter --user-name cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_object_privileges,
            managed_database_id=managed_database_id,
            user_name=user_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_object_privileges,
            limit,
            page_size,
            managed_database_id=managed_database_id,
            user_name=user_name,
            **kwargs
        )
    else:
        result = client.list_object_privileges(
            managed_database_id=managed_database_id,
            user_name=user_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.list_optimizer_statistics_advisor_executions.command_name', 'list-optimizer-statistics-advisor-executions'), help=u"""Lists the details of the Optimizer Statistics Advisor task executions, such as their duration, and the number of findings, if any. Optionally, you can specify a date-time range (of seven days) to obtain the list of executions that fall within the specified time range. If the date-time range is not specified, then the executions in the last seven days are listed. \n[Command Reference](listOptimizerStatisticsAdvisorExecutions)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--start-time-greater-than-or-equal-to', help=u"""The start time of the time range to retrieve the optimizer statistics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".""")
@cli_util.option('--end-time-less-than-or-equal-to', help=u"""The end time of the time range to retrieve the optimizer statistics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'OptimizerStatisticsAdvisorExecutionsCollection'})
@cli_util.wrap_exceptions
def list_optimizer_statistics_advisor_executions(ctx, from_json, all_pages, managed_database_id, start_time_greater_than_or_equal_to, end_time_less_than_or_equal_to):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    if start_time_greater_than_or_equal_to is not None:
        kwargs['start_time_greater_than_or_equal_to'] = start_time_greater_than_or_equal_to
    if end_time_less_than_or_equal_to is not None:
        kwargs['end_time_less_than_or_equal_to'] = end_time_less_than_or_equal_to
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.list_optimizer_statistics_advisor_executions(
        managed_database_id=managed_database_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.list_optimizer_statistics_collection_aggregations.command_name', 'list-optimizer-statistics-collection-aggregations'), help=u"""Gets a list of the optimizer statistics collection operations per hour, grouped by task or object status for the specified Managed Database. You must specify a value for GroupByQueryParam to determine whether the data should be grouped by task status or task object status. Optionally, you can specify a date-time range (of seven days) to obtain collection aggregations within the specified time range. If the date-time range is not specified, then the operations in the last seven days are listed. You can further filter the results by providing the optional type of TaskTypeQueryParam. If the task type not provided, then both Auto and Manual tasks are considered for aggregation. \n[Command Reference](listOptimizerStatisticsCollectionAggregations)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--group-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["TASK_STATUS", "TASK_OBJECTS_STATUS"]), help=u"""The optimizer statistics tasks grouped by type.""")
@cli_util.option('--start-time-greater-than-or-equal-to', help=u"""The start time of the time range to retrieve the optimizer statistics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".""")
@cli_util.option('--end-time-less-than-or-equal-to', help=u"""The end time of the time range to retrieve the optimizer statistics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".""")
@cli_util.option('--task-type', type=custom_types.CliCaseInsensitiveChoice(["ALL", "MANUAL", "AUTO"]), help=u"""The filter types of the optimizer statistics tasks.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'OptimizerStatisticsCollectionAggregationsCollection'})
@cli_util.wrap_exceptions
def list_optimizer_statistics_collection_aggregations(ctx, from_json, all_pages, page_size, managed_database_id, group_type, start_time_greater_than_or_equal_to, end_time_less_than_or_equal_to, task_type, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    if start_time_greater_than_or_equal_to is not None:
        kwargs['start_time_greater_than_or_equal_to'] = start_time_greater_than_or_equal_to
    if end_time_less_than_or_equal_to is not None:
        kwargs['end_time_less_than_or_equal_to'] = end_time_less_than_or_equal_to
    if task_type is not None:
        kwargs['task_type'] = task_type
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_optimizer_statistics_collection_aggregations,
            managed_database_id=managed_database_id,
            group_type=group_type,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_optimizer_statistics_collection_aggregations,
            limit,
            page_size,
            managed_database_id=managed_database_id,
            group_type=group_type,
            **kwargs
        )
    else:
        result = client.list_optimizer_statistics_collection_aggregations(
            managed_database_id=managed_database_id,
            group_type=group_type,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.list_optimizer_statistics_collection_operations.command_name', 'list-optimizer-statistics-collection-operations'), help=u"""Lists the Optimizer Statistics Collection (Auto and Manual) task operation summary for the specified Managed Database. The summary includes the details of each operation and the number of tasks grouped by status: Completed, In Progress, Failed, and so on. Optionally, you can specify a date-time range (of seven days) to obtain the list of operations that fall within the specified time range. If the date-time range is not specified, then the operations in the last seven days are listed. This API also enables the pagination of results and the opc-next-page response header indicates whether there is a next page. If you use the same header value in a consecutive request, the next page records are returned. To obtain the required results, you can apply the different types of filters supported by this API. \n[Command Reference](listOptimizerStatisticsCollectionOperations)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--start-time-greater-than-or-equal-to', help=u"""The start time of the time range to retrieve the optimizer statistics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".""")
@cli_util.option('--end-time-less-than-or-equal-to', help=u"""The end time of the time range to retrieve the optimizer statistics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".""")
@cli_util.option('--task-type', type=custom_types.CliCaseInsensitiveChoice(["ALL", "MANUAL", "AUTO"]), help=u"""The filter types of the optimizer statistics tasks.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--filter-by', help=u"""The parameter used to filter the optimizer statistics operations. Any property of the OptimizerStatisticsCollectionOperationSummary can be used to define the filter condition. The allowed conditional operators are AND or OR, and the allowed binary operators are are >, < and =. Any other operator is regarded invalid. Example: jobName=<replace with job name> AND status=<replace with status>""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["START_TIME", "END_TIME", "STATUS"]), help=u"""Sorts the list of optimizer statistics operations based on a specific attribute.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the default order.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'OptimizerStatisticsCollectionOperationsCollection'})
@cli_util.wrap_exceptions
def list_optimizer_statistics_collection_operations(ctx, from_json, all_pages, page_size, managed_database_id, start_time_greater_than_or_equal_to, end_time_less_than_or_equal_to, task_type, limit, page, filter_by, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    if start_time_greater_than_or_equal_to is not None:
        kwargs['start_time_greater_than_or_equal_to'] = start_time_greater_than_or_equal_to
    if end_time_less_than_or_equal_to is not None:
        kwargs['end_time_less_than_or_equal_to'] = end_time_less_than_or_equal_to
    if task_type is not None:
        kwargs['task_type'] = task_type
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if filter_by is not None:
        kwargs['filter_by'] = filter_by
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_optimizer_statistics_collection_operations,
            managed_database_id=managed_database_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_optimizer_statistics_collection_operations,
            limit,
            page_size,
            managed_database_id=managed_database_id,
            **kwargs
        )
    else:
        result = client.list_optimizer_statistics_collection_operations(
            managed_database_id=managed_database_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@preferred_credential_group.command(name=cli_util.override('db_management.list_preferred_credentials.command_name', 'list'), help=u"""Gets the list of preferred credentials for a given Managed Database. \n[Command Reference](listPreferredCredentials)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'PreferredCredentialCollection'})
@cli_util.wrap_exceptions
def list_preferred_credentials(ctx, from_json, all_pages, managed_database_id):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.list_preferred_credentials(
        managed_database_id=managed_database_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.list_proxied_for_users.command_name', 'list-proxied-for-users'), help=u"""Gets the list of users on whose behalf the current user acts as proxy. \n[Command Reference](listProxiedForUsers)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--user-name', required=True, help=u"""The name of the user whose details are to be viewed.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["NAME"]), help=u"""The field to sort information by. Only one sortOrder can be used. The default sort order for \u2018NAME\u2019 is ascending. The \u2018NAME\u2019 sort order is case-sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the default order.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'ProxiedForUserCollection'})
@cli_util.wrap_exceptions
def list_proxied_for_users(ctx, from_json, all_pages, page_size, managed_database_id, user_name, name, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(user_name, six.string_types) and len(user_name.strip()) == 0:
        raise click.UsageError('Parameter --user-name cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_proxied_for_users,
            managed_database_id=managed_database_id,
            user_name=user_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_proxied_for_users,
            limit,
            page_size,
            managed_database_id=managed_database_id,
            user_name=user_name,
            **kwargs
        )
    else:
        result = client.list_proxied_for_users(
            managed_database_id=managed_database_id,
            user_name=user_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.list_proxy_users.command_name', 'list-proxy-users'), help=u"""Gets the list of proxy users for the current user. \n[Command Reference](listProxyUsers)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--user-name', required=True, help=u"""The name of the user whose details are to be viewed.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["NAME"]), help=u"""The field to sort information by. Only one sortOrder can be used. The default sort order for \u2018NAME\u2019 is ascending. The \u2018NAME\u2019 sort order is case-sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the default order.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'ProxyUserCollection'})
@cli_util.wrap_exceptions
def list_proxy_users(ctx, from_json, all_pages, page_size, managed_database_id, user_name, name, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(user_name, six.string_types) and len(user_name.strip()) == 0:
        raise click.UsageError('Parameter --user-name cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_proxy_users,
            managed_database_id=managed_database_id,
            user_name=user_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_proxy_users,
            limit,
            page_size,
            managed_database_id=managed_database_id,
            user_name=user_name,
            **kwargs
        )
    else:
        result = client.list_proxy_users(
            managed_database_id=managed_database_id,
            user_name=user_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.list_roles.command_name', 'list-roles'), help=u"""Gets the list of roles granted to a specific user. \n[Command Reference](listRoles)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--user-name', required=True, help=u"""The name of the user whose details are to be viewed.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["NAME"]), help=u"""The field to sort information by. Only one sortOrder can be used. The default sort order for \u2018NAME\u2019 is ascending. The \u2018NAME\u2019 sort order is case-sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the default order.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'RoleCollection'})
@cli_util.wrap_exceptions
def list_roles(ctx, from_json, all_pages, page_size, managed_database_id, user_name, name, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(user_name, six.string_types) and len(user_name.strip()) == 0:
        raise click.UsageError('Parameter --user-name cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_roles,
            managed_database_id=managed_database_id,
            user_name=user_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_roles,
            limit,
            page_size,
            managed_database_id=managed_database_id,
            user_name=user_name,
            **kwargs
        )
    else:
        result = client.list_roles(
            managed_database_id=managed_database_id,
            user_name=user_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.list_system_privileges.command_name', 'list-system-privileges'), help=u"""Gets the list of system privileges granted to a specific user. \n[Command Reference](listSystemPrivileges)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--user-name', required=True, help=u"""The name of the user whose details are to be viewed.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["NAME"]), help=u"""The field to sort information by. Only one sortOrder can be used. The default sort order for \u2018NAME\u2019 is ascending. The \u2018NAME\u2019 sort order is case-sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the default order.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'SystemPrivilegeCollection'})
@cli_util.wrap_exceptions
def list_system_privileges(ctx, from_json, all_pages, page_size, managed_database_id, user_name, name, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(user_name, six.string_types) and len(user_name.strip()) == 0:
        raise click.UsageError('Parameter --user-name cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_system_privileges,
            managed_database_id=managed_database_id,
            user_name=user_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_system_privileges,
            limit,
            page_size,
            managed_database_id=managed_database_id,
            user_name=user_name,
            **kwargs
        )
    else:
        result = client.list_system_privileges(
            managed_database_id=managed_database_id,
            user_name=user_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.list_table_statistics.command_name', 'list-table-statistics'), help=u"""Lists the database table statistics grouped by different statuses such as Not Stale Stats, Stale Stats, and No Stats. This also includes the percentage of each status. \n[Command Reference](listTableStatistics)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'TableStatisticsCollection'})
@cli_util.wrap_exceptions
def list_table_statistics(ctx, from_json, all_pages, managed_database_id):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.list_table_statistics(
        managed_database_id=managed_database_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@tablespace_group.command(name=cli_util.override('db_management.list_tablespaces.command_name', 'list'), help=u"""Gets the list of tablespaces for the specified managedDatabaseId. \n[Command Reference](listTablespaces)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "NAME"]), help=u"""The field to sort information by. Only one sortOrder can be used. The default sort order for \u2018TIMECREATED\u2019 is descending and the default sort order for \u2018NAME\u2019 is ascending. The \u2018NAME\u2019 sort order is case-sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the default order.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'TablespaceCollection'})
@cli_util.wrap_exceptions
def list_tablespaces(ctx, from_json, all_pages, page_size, managed_database_id, name, sort_by, sort_order, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_tablespaces,
            managed_database_id=managed_database_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_tablespaces,
            limit,
            page_size,
            managed_database_id=managed_database_id,
            **kwargs
        )
    else:
        result = client.list_tablespaces(
            managed_database_id=managed_database_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.list_users.command_name', 'list-users'), help=u"""Gets the list of users for the specified managedDatabaseId. \n[Command Reference](listUsers)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "NAME"]), help=u"""The field to sort information by. Only one sortOrder can be used. The default sort order for \u2018TIMECREATED\u2019 is descending and the default sort order for \u2018NAME\u2019 is ascending. The \u2018NAME\u2019 sort order is case-sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the default order.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'UserCollection'})
@cli_util.wrap_exceptions
def list_users(ctx, from_json, all_pages, page_size, managed_database_id, name, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_users,
            managed_database_id=managed_database_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_users,
            limit,
            page_size,
            managed_database_id=managed_database_id,
            **kwargs
        )
    else:
        result = client.list_users(
            managed_database_id=managed_database_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('db_management.list_work_request_errors.command_name', 'list'), help=u"""Returns a paginated list of errors for a given work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the asynchronous work request.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided and the default order for timeAccepted is descending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the default order.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'WorkRequestErrorCollection'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_errors,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_errors,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_errors(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_log_entry_group.command(name=cli_util.override('db_management.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Returns a paginated list of logs for a given work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the asynchronous work request.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided and the default order for timeAccepted is descending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the default order.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'WorkRequestLogEntryCollection'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_logs,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_logs,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_logs(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('db_management.list_work_requests.command_name', 'list'), help=u"""The list of work requests in a specific compartment was retrieved successfully. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-id', help=u"""The [OCID] of the resource affected by the work request.""")
@cli_util.option('--work-request-id', help=u"""The [OCID] of the asynchronous work request.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help=u"""A filter that returns the resources whose status matches the given WorkRequestStatus.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the default order.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided and the default order for timeAccepted is descending.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'WorkRequestCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, resource_id, work_request_id, status, sort_order, sort_by, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if resource_id is not None:
        kwargs['resource_id'] = resource_id
    if work_request_id is not None:
        kwargs['work_request_id'] = work_request_id
    if status is not None:
        kwargs['status'] = status
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@tablespace_group.command(name=cli_util.override('db_management.remove_data_file.command_name', 'remove'), help=u"""Removes a data file or temp file from the tablespace. \n[Command Reference](removeDataFile)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--tablespace-name', required=True, help=u"""The name of the tablespace.""")
@cli_util.option('--credential-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--file-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["DATAFILE", "TEMPFILE"]), help=u"""Specifies whether the file is a data file or temp file.""")
@cli_util.option('--data-file', required=True, help=u"""Name of the data file or temp file to be removed from the tablespace.""")
@json_skeleton_utils.get_cli_json_input_option({'credential-details': {'module': 'database_management', 'class': 'TablespaceAdminCredentialDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'credential-details': {'module': 'database_management', 'class': 'TablespaceAdminCredentialDetails'}}, output_type={'module': 'database_management', 'class': 'TablespaceAdminStatus'})
@cli_util.wrap_exceptions
def remove_data_file(ctx, from_json, managed_database_id, tablespace_name, credential_details, file_type, data_file):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(tablespace_name, six.string_types) and len(tablespace_name.strip()) == 0:
        raise click.UsageError('Parameter --tablespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['credentialDetails'] = cli_util.parse_json_parameter("credential_details", credential_details)
    _details['fileType'] = file_type
    _details['dataFile'] = data_file

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.remove_data_file(
        managed_database_id=managed_database_id,
        tablespace_name=tablespace_name,
        remove_data_file_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@tablespace_group.command(name=cli_util.override('db_management.remove_data_file_tablespace_admin_password_credential_details.command_name', 'remove-data-file-tablespace-admin-password-credential-details'), help=u"""Removes a data file or temp file from the tablespace. \n[Command Reference](removeDataFile)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--tablespace-name', required=True, help=u"""The name of the tablespace.""")
@cli_util.option('--file-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["DATAFILE", "TEMPFILE"]), help=u"""Specifies whether the file is a data file or temp file.""")
@cli_util.option('--data-file', required=True, help=u"""Name of the data file or temp file to be removed from the tablespace.""")
@cli_util.option('--credential-details-username', required=True, help=u"""The user to connect to the database.""")
@cli_util.option('--credential-details-role', required=True, type=custom_types.CliCaseInsensitiveChoice(["NORMAL", "SYSDBA"]), help=u"""The role of the database user.""")
@cli_util.option('--credential-details-password', required=True, help=u"""The database user's password encoded using BASE64 scheme.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'TablespaceAdminStatus'})
@cli_util.wrap_exceptions
def remove_data_file_tablespace_admin_password_credential_details(ctx, from_json, managed_database_id, tablespace_name, file_type, data_file, credential_details_username, credential_details_role, credential_details_password):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(tablespace_name, six.string_types) and len(tablespace_name.strip()) == 0:
        raise click.UsageError('Parameter --tablespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['credentialDetails'] = {}
    _details['fileType'] = file_type
    _details['dataFile'] = data_file
    _details['credentialDetails']['username'] = credential_details_username
    _details['credentialDetails']['role'] = credential_details_role
    _details['credentialDetails']['password'] = credential_details_password

    _details['credentialDetails']['tablespaceAdminCredentialType'] = 'PASSWORD'

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.remove_data_file(
        managed_database_id=managed_database_id,
        tablespace_name=tablespace_name,
        remove_data_file_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@tablespace_group.command(name=cli_util.override('db_management.remove_data_file_tablespace_admin_secret_credential_details.command_name', 'remove-data-file-tablespace-admin-secret-credential-details'), help=u"""Removes a data file or temp file from the tablespace. \n[Command Reference](removeDataFile)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--tablespace-name', required=True, help=u"""The name of the tablespace.""")
@cli_util.option('--file-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["DATAFILE", "TEMPFILE"]), help=u"""Specifies whether the file is a data file or temp file.""")
@cli_util.option('--data-file', required=True, help=u"""Name of the data file or temp file to be removed from the tablespace.""")
@cli_util.option('--credential-details-username', required=True, help=u"""The user to connect to the database.""")
@cli_util.option('--credential-details-role', required=True, type=custom_types.CliCaseInsensitiveChoice(["NORMAL", "SYSDBA"]), help=u"""The role of the database user.""")
@cli_util.option('--credential-details-password-secret-id', required=True, help=u"""The [OCID] of the Secret where the database password is stored.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'TablespaceAdminStatus'})
@cli_util.wrap_exceptions
def remove_data_file_tablespace_admin_secret_credential_details(ctx, from_json, managed_database_id, tablespace_name, file_type, data_file, credential_details_username, credential_details_role, credential_details_password_secret_id):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(tablespace_name, six.string_types) and len(tablespace_name.strip()) == 0:
        raise click.UsageError('Parameter --tablespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['credentialDetails'] = {}
    _details['fileType'] = file_type
    _details['dataFile'] = data_file
    _details['credentialDetails']['username'] = credential_details_username
    _details['credentialDetails']['role'] = credential_details_role
    _details['credentialDetails']['passwordSecretId'] = credential_details_password_secret_id

    _details['credentialDetails']['tablespaceAdminCredentialType'] = 'SECRET'

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.remove_data_file(
        managed_database_id=managed_database_id,
        tablespace_name=tablespace_name,
        remove_data_file_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group_group.command(name=cli_util.override('db_management.remove_managed_database_from_managed_database_group.command_name', 'remove'), help=u"""Removes a Managed Database from a Managed Database Group. Any management activities that are currently running on this database will continue to run to completion. However, any activities scheduled to run in the future will not be performed on this database. \n[Command Reference](removeManagedDatabaseFromManagedDatabaseGroup)""")
@cli_util.option('--managed-database-group-id', required=True, help=u"""The [OCID] of the Managed Database Group.""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def remove_managed_database_from_managed_database_group(ctx, from_json, managed_database_group_id, managed_database_id):

    if isinstance(managed_database_group_id, six.string_types) and len(managed_database_group_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-group-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['managedDatabaseId'] = managed_database_id

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.remove_managed_database_from_managed_database_group(
        managed_database_group_id=managed_database_group_id,
        remove_managed_database_from_managed_database_group_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.reset_database_parameters.command_name', 'reset-database-parameters'), help=u"""Resets database parameter values to their default or startup values. \n[Command Reference](resetDatabaseParameters)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--credentials', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--scope', required=True, type=custom_types.CliCaseInsensitiveChoice(["MEMORY", "SPFILE", "BOTH"]), help=u"""The clause used to specify when the parameter change takes effect.

Use `MEMORY` to make the change in memory and ensure that it takes effect immediately. Use `SPFILE` to make the change in the server parameter file. The change takes effect when the database is next shut down and started up again. Use `BOTH` to make the change in memory and in the server parameter file. The change takes effect immediately and persists after the database is shut down and started up again.""")
@cli_util.option('--parameters', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of database parameter names.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'credentials': {'module': 'database_management', 'class': 'DatabaseCredentials'}, 'parameters': {'module': 'database_management', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'credentials': {'module': 'database_management', 'class': 'DatabaseCredentials'}, 'parameters': {'module': 'database_management', 'class': 'list[string]'}}, output_type={'module': 'database_management', 'class': 'UpdateDatabaseParametersResult'})
@cli_util.wrap_exceptions
def reset_database_parameters(ctx, from_json, managed_database_id, credentials, scope, parameters):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['credentials'] = cli_util.parse_json_parameter("credentials", credentials)
    _details['scope'] = scope
    _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.reset_database_parameters(
        managed_database_id=managed_database_id,
        reset_database_parameters_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@tablespace_group.command(name=cli_util.override('db_management.resize_data_file.command_name', 'resize-data-file'), help=u"""Resizes a data file or temp file within the tablespace. \n[Command Reference](resizeDataFile)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--tablespace-name', required=True, help=u"""The name of the tablespace.""")
@cli_util.option('--credential-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--file-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["DATAFILE", "TEMPFILE"]), help=u"""Specifies whether the file is a data file or temp file.""")
@cli_util.option('--data-file', required=True, help=u"""Name of the data file or temp file to be resized.""")
@cli_util.option('--file-size', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The new size of the data file or temp file.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-auto-extensible', type=click.BOOL, help=u"""Specifies whether the data file or temp file can be extended automatically.""")
@cli_util.option('--auto-extend-next-size', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The size of the next increment of disk space to be allocated automatically when more extents are required.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--auto-extend-max-size', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The maximum disk space allowed for automatic extension of the data files or temp files.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-max-size-unlimited', type=click.BOOL, help=u"""Specifies whether the disk space of the data file or temp file can be limited.""")
@json_skeleton_utils.get_cli_json_input_option({'credential-details': {'module': 'database_management', 'class': 'TablespaceAdminCredentialDetails'}, 'file-size': {'module': 'database_management', 'class': 'TablespaceStorageSize'}, 'auto-extend-next-size': {'module': 'database_management', 'class': 'TablespaceStorageSize'}, 'auto-extend-max-size': {'module': 'database_management', 'class': 'TablespaceStorageSize'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'credential-details': {'module': 'database_management', 'class': 'TablespaceAdminCredentialDetails'}, 'file-size': {'module': 'database_management', 'class': 'TablespaceStorageSize'}, 'auto-extend-next-size': {'module': 'database_management', 'class': 'TablespaceStorageSize'}, 'auto-extend-max-size': {'module': 'database_management', 'class': 'TablespaceStorageSize'}}, output_type={'module': 'database_management', 'class': 'TablespaceAdminStatus'})
@cli_util.wrap_exceptions
def resize_data_file(ctx, from_json, managed_database_id, tablespace_name, credential_details, file_type, data_file, file_size, is_auto_extensible, auto_extend_next_size, auto_extend_max_size, is_max_size_unlimited):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(tablespace_name, six.string_types) and len(tablespace_name.strip()) == 0:
        raise click.UsageError('Parameter --tablespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['credentialDetails'] = cli_util.parse_json_parameter("credential_details", credential_details)
    _details['fileType'] = file_type
    _details['dataFile'] = data_file

    if file_size is not None:
        _details['fileSize'] = cli_util.parse_json_parameter("file_size", file_size)

    if is_auto_extensible is not None:
        _details['isAutoExtensible'] = is_auto_extensible

    if auto_extend_next_size is not None:
        _details['autoExtendNextSize'] = cli_util.parse_json_parameter("auto_extend_next_size", auto_extend_next_size)

    if auto_extend_max_size is not None:
        _details['autoExtendMaxSize'] = cli_util.parse_json_parameter("auto_extend_max_size", auto_extend_max_size)

    if is_max_size_unlimited is not None:
        _details['isMaxSizeUnlimited'] = is_max_size_unlimited

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.resize_data_file(
        managed_database_id=managed_database_id,
        tablespace_name=tablespace_name,
        resize_data_file_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@historic_addm_result_group.command(name=cli_util.override('db_management.run_historic_addm.command_name', 'run-historic-addm'), help=u"""Creates and executes a historic ADDM task using the specified AWR snapshot IDs. If an existing ADDM task uses the provided awr snapshot IDs, the existing task will be returned. \n[Command Reference](runHistoricAddm)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--start-snapshot-id', required=True, type=click.INT, help=u"""The ID number of the beginning AWR snapshot.""")
@cli_util.option('--end-snapshot-id', required=True, type=click.INT, help=u"""The ID of the ending AWR snapshot.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'HistoricAddmResult'})
@cli_util.wrap_exceptions
def run_historic_addm(ctx, from_json, managed_database_id, start_snapshot_id, end_snapshot_id):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['startSnapshotId'] = start_snapshot_id
    _details['endSnapshotId'] = end_snapshot_id

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.run_historic_addm(
        managed_database_id=managed_database_id,
        run_historic_addm_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.summarize_awr_db_cpu_usages.command_name', 'summarize-awr-db-cpu-usages'), help=u"""Summarizes the AWR CPU resource limits and metrics for the specified database in AWR. \n[Command Reference](summarizeAwrDbCpuUsages)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--awr-db-id', required=True, help=u"""The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs""")
@cli_util.option('--inst-num', help=u"""The optional single value query parameter to filter the database instance number.""")
@cli_util.option('--begin-sn-id-greater-than-or-equal-to', type=click.INT, help=u"""The optional greater than or equal to filter on the snapshot ID.""")
@cli_util.option('--end-sn-id-less-than-or-equal-to', type=click.INT, help=u"""The optional less than or equal to query parameter to filter the snapshot ID.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--session-type', type=custom_types.CliCaseInsensitiveChoice(["FOREGROUND", "BACKGROUND", "ALL"]), help=u"""The optional query parameter to filter ASH activities by FOREGROUND or BACKGROUND.""")
@cli_util.option('--container-id', type=click.INT, help=u"""The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in large paginated response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_SAMPLED", "AVG_VALUE"]), help=u"""The option to sort the AWR CPU usage summary data.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the default order.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'AwrDbCpuUsageCollection'})
@cli_util.wrap_exceptions
def summarize_awr_db_cpu_usages(ctx, from_json, managed_database_id, awr_db_id, inst_num, begin_sn_id_greater_than_or_equal_to, end_sn_id_less_than_or_equal_to, time_greater_than_or_equal_to, time_less_than_or_equal_to, session_type, container_id, page, limit, sort_by, sort_order):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(awr_db_id, six.string_types) and len(awr_db_id.strip()) == 0:
        raise click.UsageError('Parameter --awr-db-id cannot be whitespace or empty string')

    kwargs = {}
    if inst_num is not None:
        kwargs['inst_num'] = inst_num
    if begin_sn_id_greater_than_or_equal_to is not None:
        kwargs['begin_sn_id_greater_than_or_equal_to'] = begin_sn_id_greater_than_or_equal_to
    if end_sn_id_less_than_or_equal_to is not None:
        kwargs['end_sn_id_less_than_or_equal_to'] = end_sn_id_less_than_or_equal_to
    if time_greater_than_or_equal_to is not None:
        kwargs['time_greater_than_or_equal_to'] = time_greater_than_or_equal_to
    if time_less_than_or_equal_to is not None:
        kwargs['time_less_than_or_equal_to'] = time_less_than_or_equal_to
    if session_type is not None:
        kwargs['session_type'] = session_type
    if container_id is not None:
        kwargs['container_id'] = container_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.summarize_awr_db_cpu_usages(
        managed_database_id=managed_database_id,
        awr_db_id=awr_db_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.summarize_awr_db_metrics.command_name', 'summarize-awr-db-metrics'), help=u"""Summarizes the metric samples for the specified database in the AWR. The metric samples are summarized based on the Time dimension for each metric. \n[Command Reference](summarizeAwrDbMetrics)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--awr-db-id', required=True, help=u"""The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs""")
@cli_util.option('--name', required=True, multiple=True, help=u"""The required multiple value query parameter to filter the entity name.""")
@cli_util.option('--inst-num', help=u"""The optional single value query parameter to filter the database instance number.""")
@cli_util.option('--begin-sn-id-greater-than-or-equal-to', type=click.INT, help=u"""The optional greater than or equal to filter on the snapshot ID.""")
@cli_util.option('--end-sn-id-less-than-or-equal-to', type=click.INT, help=u"""The optional less than or equal to query parameter to filter the snapshot ID.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--container-id', type=click.INT, help=u"""The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in large paginated response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMESTAMP", "NAME"]), help=u"""The option to sort the AWR time series summary data.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the default order.""")
@json_skeleton_utils.get_cli_json_input_option({'name': {'module': 'database_management', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'name': {'module': 'database_management', 'class': 'list[string]'}}, output_type={'module': 'database_management', 'class': 'AwrDbMetricCollection'})
@cli_util.wrap_exceptions
def summarize_awr_db_metrics(ctx, from_json, managed_database_id, awr_db_id, name, inst_num, begin_sn_id_greater_than_or_equal_to, end_sn_id_less_than_or_equal_to, time_greater_than_or_equal_to, time_less_than_or_equal_to, container_id, page, limit, sort_by, sort_order):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(awr_db_id, six.string_types) and len(awr_db_id.strip()) == 0:
        raise click.UsageError('Parameter --awr-db-id cannot be whitespace or empty string')

    kwargs = {}
    if inst_num is not None:
        kwargs['inst_num'] = inst_num
    if begin_sn_id_greater_than_or_equal_to is not None:
        kwargs['begin_sn_id_greater_than_or_equal_to'] = begin_sn_id_greater_than_or_equal_to
    if end_sn_id_less_than_or_equal_to is not None:
        kwargs['end_sn_id_less_than_or_equal_to'] = end_sn_id_less_than_or_equal_to
    if time_greater_than_or_equal_to is not None:
        kwargs['time_greater_than_or_equal_to'] = time_greater_than_or_equal_to
    if time_less_than_or_equal_to is not None:
        kwargs['time_less_than_or_equal_to'] = time_less_than_or_equal_to
    if container_id is not None:
        kwargs['container_id'] = container_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.summarize_awr_db_metrics(
        managed_database_id=managed_database_id,
        awr_db_id=awr_db_id,
        name=name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.summarize_awr_db_parameter_changes.command_name', 'summarize-awr-db-parameter-changes'), help=u"""Summarizes the database parameter change history for one database parameter of the specified database in AWR. One change history record contains the previous value, the changed value, and the corresponding time range. If the database parameter value was changed multiple times within the time range, then multiple change history records are created for the same parameter. Note that this API only returns information on change history details for one database parameter. To get a list of all the database parameters whose values were changed during a specified time range, use the following API endpoint: /managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbParameters \n[Command Reference](summarizeAwrDbParameterChanges)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--awr-db-id', required=True, help=u"""The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs""")
@cli_util.option('--name', required=True, help=u"""The required single value query parameter to filter the entity name.""")
@cli_util.option('--inst-num', help=u"""The optional single value query parameter to filter the database instance number.""")
@cli_util.option('--begin-sn-id-greater-than-or-equal-to', type=click.INT, help=u"""The optional greater than or equal to filter on the snapshot ID.""")
@cli_util.option('--end-sn-id-less-than-or-equal-to', type=click.INT, help=u"""The optional less than or equal to query parameter to filter the snapshot ID.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--container-id', type=click.INT, help=u"""The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in large paginated response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["IS_CHANGED", "NAME"]), help=u"""The option to sort the AWR database parameter change history data.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the default order.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'AwrDbParameterChangeCollection'})
@cli_util.wrap_exceptions
def summarize_awr_db_parameter_changes(ctx, from_json, managed_database_id, awr_db_id, name, inst_num, begin_sn_id_greater_than_or_equal_to, end_sn_id_less_than_or_equal_to, time_greater_than_or_equal_to, time_less_than_or_equal_to, container_id, page, limit, sort_by, sort_order):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(awr_db_id, six.string_types) and len(awr_db_id.strip()) == 0:
        raise click.UsageError('Parameter --awr-db-id cannot be whitespace or empty string')

    kwargs = {}
    if inst_num is not None:
        kwargs['inst_num'] = inst_num
    if begin_sn_id_greater_than_or_equal_to is not None:
        kwargs['begin_sn_id_greater_than_or_equal_to'] = begin_sn_id_greater_than_or_equal_to
    if end_sn_id_less_than_or_equal_to is not None:
        kwargs['end_sn_id_less_than_or_equal_to'] = end_sn_id_less_than_or_equal_to
    if time_greater_than_or_equal_to is not None:
        kwargs['time_greater_than_or_equal_to'] = time_greater_than_or_equal_to
    if time_less_than_or_equal_to is not None:
        kwargs['time_less_than_or_equal_to'] = time_less_than_or_equal_to
    if container_id is not None:
        kwargs['container_id'] = container_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.summarize_awr_db_parameter_changes(
        managed_database_id=managed_database_id,
        awr_db_id=awr_db_id,
        name=name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.summarize_awr_db_parameters.command_name', 'summarize-awr-db-parameters'), help=u"""Summarizes the database parameter history for the specified database in AWR. This includes the list of database parameters, with information on whether the parameter values were modified within the query time range. Note that each database parameter is only listed once. Depending on the optional query parameters, the returned summary gets all the database parameters, which include:

- Each parameter whose value was changed during the time range:  (valueChanged =\"Y\") - Each parameter whose value was unchanged during the time range:  (valueChanged =\"N\") - Each parameter whose value was changed at the system level during the time range: (valueChanged =\"Y\"  and valueModified = \"SYSTEM_MOD\") - Each parameter whose value was unchanged during the time range, however, the value is not the default value: (valueChanged =\"N\" and  valueDefault = \"FALSE\")

Note that this API does not return information on the number of times each database parameter has been changed within the time range. To get the database parameter value change history for a specific parameter, use the following API endpoint: /managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbParameterChanges \n[Command Reference](summarizeAwrDbParameters)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--awr-db-id', required=True, help=u"""The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs""")
@cli_util.option('--inst-num', help=u"""The optional single value query parameter to filter the database instance number.""")
@cli_util.option('--begin-sn-id-greater-than-or-equal-to', type=click.INT, help=u"""The optional greater than or equal to filter on the snapshot ID.""")
@cli_util.option('--end-sn-id-less-than-or-equal-to', type=click.INT, help=u"""The optional less than or equal to query parameter to filter the snapshot ID.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--container-id', type=click.INT, help=u"""The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges""")
@cli_util.option('--name', multiple=True, help=u"""The optional multiple value query parameter to filter the entity name.""")
@cli_util.option('--name-contains', help=u"""The optional contains query parameter to filter the entity name by any part of the name.""")
@cli_util.option('--value-changed', type=custom_types.CliCaseInsensitiveChoice(["Y", "N"]), help=u"""The optional query parameter to filter database parameters whose values were changed.""")
@cli_util.option('--value-default', type=custom_types.CliCaseInsensitiveChoice(["TRUE", "FALSE"]), help=u"""The optional query parameter to filter the database parameters that had the default value in the last snapshot.""")
@cli_util.option('--value-modified', type=custom_types.CliCaseInsensitiveChoice(["MODIFIED", "SYSTEM_MOD", "FALSE"]), help=u"""The optional query parameter to filter the database parameters that had a modified value in the last snapshot.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in large paginated response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["IS_CHANGED", "NAME"]), help=u"""The option to sort the AWR database parameter change history data.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the default order.""")
@json_skeleton_utils.get_cli_json_input_option({'name': {'module': 'database_management', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'name': {'module': 'database_management', 'class': 'list[string]'}}, output_type={'module': 'database_management', 'class': 'AwrDbParameterCollection'})
@cli_util.wrap_exceptions
def summarize_awr_db_parameters(ctx, from_json, managed_database_id, awr_db_id, inst_num, begin_sn_id_greater_than_or_equal_to, end_sn_id_less_than_or_equal_to, time_greater_than_or_equal_to, time_less_than_or_equal_to, container_id, name, name_contains, value_changed, value_default, value_modified, page, limit, sort_by, sort_order):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(awr_db_id, six.string_types) and len(awr_db_id.strip()) == 0:
        raise click.UsageError('Parameter --awr-db-id cannot be whitespace or empty string')

    kwargs = {}
    if inst_num is not None:
        kwargs['inst_num'] = inst_num
    if begin_sn_id_greater_than_or_equal_to is not None:
        kwargs['begin_sn_id_greater_than_or_equal_to'] = begin_sn_id_greater_than_or_equal_to
    if end_sn_id_less_than_or_equal_to is not None:
        kwargs['end_sn_id_less_than_or_equal_to'] = end_sn_id_less_than_or_equal_to
    if time_greater_than_or_equal_to is not None:
        kwargs['time_greater_than_or_equal_to'] = time_greater_than_or_equal_to
    if time_less_than_or_equal_to is not None:
        kwargs['time_less_than_or_equal_to'] = time_less_than_or_equal_to
    if container_id is not None:
        kwargs['container_id'] = container_id
    if name is not None and len(name) > 0:
        kwargs['name'] = name
    if name_contains is not None:
        kwargs['name_contains'] = name_contains
    if value_changed is not None:
        kwargs['value_changed'] = value_changed
    if value_default is not None:
        kwargs['value_default'] = value_default
    if value_modified is not None:
        kwargs['value_modified'] = value_modified
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.summarize_awr_db_parameters(
        managed_database_id=managed_database_id,
        awr_db_id=awr_db_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.summarize_awr_db_snapshot_ranges.command_name', 'summarize-awr-db-snapshot-ranges'), help=u"""Summarizes the AWR snapshot ranges that contain continuous snapshots, for the specified Managed Database. \n[Command Reference](summarizeAwrDbSnapshotRanges)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--name', help=u"""The optional single value query parameter to filter the entity name.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["END_INTERVAL_TIME", "NAME"]), help=u"""The option to sort the AWR summary data.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the default order.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'AwrDbSnapshotRangeCollection'})
@cli_util.wrap_exceptions
def summarize_awr_db_snapshot_ranges(ctx, from_json, managed_database_id, name, time_greater_than_or_equal_to, time_less_than_or_equal_to, page, limit, sort_by, sort_order):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
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
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.summarize_awr_db_snapshot_ranges(
        managed_database_id=managed_database_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.summarize_awr_db_sysstats.command_name', 'summarize-awr-db-sysstats'), help=u"""Summarizes the AWR SYSSTAT sample data for the specified database in AWR. The statistical data is summarized based on the Time dimension for each statistic. \n[Command Reference](summarizeAwrDbSysstats)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--awr-db-id', required=True, help=u"""The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs""")
@cli_util.option('--name', required=True, multiple=True, help=u"""The required multiple value query parameter to filter the entity name.""")
@cli_util.option('--inst-num', help=u"""The optional single value query parameter to filter the database instance number.""")
@cli_util.option('--begin-sn-id-greater-than-or-equal-to', type=click.INT, help=u"""The optional greater than or equal to filter on the snapshot ID.""")
@cli_util.option('--end-sn-id-less-than-or-equal-to', type=click.INT, help=u"""The optional less than or equal to query parameter to filter the snapshot ID.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--container-id', type=click.INT, help=u"""The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in large paginated response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_BEGIN", "NAME"]), help=u"""The option to sort the data within a time period.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the default order.""")
@json_skeleton_utils.get_cli_json_input_option({'name': {'module': 'database_management', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'name': {'module': 'database_management', 'class': 'list[string]'}}, output_type={'module': 'database_management', 'class': 'AwrDbSysstatCollection'})
@cli_util.wrap_exceptions
def summarize_awr_db_sysstats(ctx, from_json, managed_database_id, awr_db_id, name, inst_num, begin_sn_id_greater_than_or_equal_to, end_sn_id_less_than_or_equal_to, time_greater_than_or_equal_to, time_less_than_or_equal_to, container_id, page, limit, sort_by, sort_order):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(awr_db_id, six.string_types) and len(awr_db_id.strip()) == 0:
        raise click.UsageError('Parameter --awr-db-id cannot be whitespace or empty string')

    kwargs = {}
    if inst_num is not None:
        kwargs['inst_num'] = inst_num
    if begin_sn_id_greater_than_or_equal_to is not None:
        kwargs['begin_sn_id_greater_than_or_equal_to'] = begin_sn_id_greater_than_or_equal_to
    if end_sn_id_less_than_or_equal_to is not None:
        kwargs['end_sn_id_less_than_or_equal_to'] = end_sn_id_less_than_or_equal_to
    if time_greater_than_or_equal_to is not None:
        kwargs['time_greater_than_or_equal_to'] = time_greater_than_or_equal_to
    if time_less_than_or_equal_to is not None:
        kwargs['time_less_than_or_equal_to'] = time_less_than_or_equal_to
    if container_id is not None:
        kwargs['container_id'] = container_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.summarize_awr_db_sysstats(
        managed_database_id=managed_database_id,
        awr_db_id=awr_db_id,
        name=name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.summarize_awr_db_top_wait_events.command_name', 'summarize-awr-db-top-wait-events'), help=u"""Summarizes the AWR top wait events. \n[Command Reference](summarizeAwrDbTopWaitEvents)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--awr-db-id', required=True, help=u"""The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs""")
@cli_util.option('--inst-num', help=u"""The optional single value query parameter to filter the database instance number.""")
@cli_util.option('--begin-sn-id-greater-than-or-equal-to', type=click.INT, help=u"""The optional greater than or equal to filter on the snapshot ID.""")
@cli_util.option('--end-sn-id-less-than-or-equal-to', type=click.INT, help=u"""The optional less than or equal to query parameter to filter the snapshot ID.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--session-type', type=custom_types.CliCaseInsensitiveChoice(["FOREGROUND", "BACKGROUND", "ALL"]), help=u"""The optional query parameter to filter ASH activities by FOREGROUND or BACKGROUND.""")
@cli_util.option('--container-id', type=click.INT, help=u"""The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges""")
@cli_util.option('--top-n', type=click.INT, help=u"""The optional query parameter to filter the number of top categories to be returned.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["WAITS_PERSEC", "AVG_WAIT_TIME_PERSEC"]), help=u"""The option to sort the AWR top event summary data.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the default order.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'AwrDbTopWaitEventCollection'})
@cli_util.wrap_exceptions
def summarize_awr_db_top_wait_events(ctx, from_json, managed_database_id, awr_db_id, inst_num, begin_sn_id_greater_than_or_equal_to, end_sn_id_less_than_or_equal_to, time_greater_than_or_equal_to, time_less_than_or_equal_to, session_type, container_id, top_n, sort_by, sort_order):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(awr_db_id, six.string_types) and len(awr_db_id.strip()) == 0:
        raise click.UsageError('Parameter --awr-db-id cannot be whitespace or empty string')

    kwargs = {}
    if inst_num is not None:
        kwargs['inst_num'] = inst_num
    if begin_sn_id_greater_than_or_equal_to is not None:
        kwargs['begin_sn_id_greater_than_or_equal_to'] = begin_sn_id_greater_than_or_equal_to
    if end_sn_id_less_than_or_equal_to is not None:
        kwargs['end_sn_id_less_than_or_equal_to'] = end_sn_id_less_than_or_equal_to
    if time_greater_than_or_equal_to is not None:
        kwargs['time_greater_than_or_equal_to'] = time_greater_than_or_equal_to
    if time_less_than_or_equal_to is not None:
        kwargs['time_less_than_or_equal_to'] = time_less_than_or_equal_to
    if session_type is not None:
        kwargs['session_type'] = session_type
    if container_id is not None:
        kwargs['container_id'] = container_id
    if top_n is not None:
        kwargs['top_n'] = top_n
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.summarize_awr_db_top_wait_events(
        managed_database_id=managed_database_id,
        awr_db_id=awr_db_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.summarize_awr_db_wait_event_buckets.command_name', 'summarize-awr-db-wait-event-buckets'), help=u"""Summarizes AWR wait event data into value buckets and frequency, for the specified database in the AWR. \n[Command Reference](summarizeAwrDbWaitEventBuckets)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--awr-db-id', required=True, help=u"""The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs""")
@cli_util.option('--name', required=True, help=u"""The required single value query parameter to filter the entity name.""")
@cli_util.option('--inst-num', help=u"""The optional single value query parameter to filter the database instance number.""")
@cli_util.option('--begin-sn-id-greater-than-or-equal-to', type=click.INT, help=u"""The optional greater than or equal to filter on the snapshot ID.""")
@cli_util.option('--end-sn-id-less-than-or-equal-to', type=click.INT, help=u"""The optional less than or equal to query parameter to filter the snapshot ID.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--num-bucket', type=click.INT, help=u"""The number of buckets within the histogram.""")
@cli_util.option('--min-value', help=u"""The minimum value of the histogram.""")
@cli_util.option('--max-value', help=u"""The maximum value of the histogram.""")
@cli_util.option('--container-id', type=click.INT, help=u"""The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in large paginated response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["CATEGORY", "PERCENTAGE"]), help=u"""The option to sort distribution data.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the default order.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'AwrDbWaitEventBucketCollection'})
@cli_util.wrap_exceptions
def summarize_awr_db_wait_event_buckets(ctx, from_json, managed_database_id, awr_db_id, name, inst_num, begin_sn_id_greater_than_or_equal_to, end_sn_id_less_than_or_equal_to, time_greater_than_or_equal_to, time_less_than_or_equal_to, num_bucket, min_value, max_value, container_id, page, limit, sort_by, sort_order):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(awr_db_id, six.string_types) and len(awr_db_id.strip()) == 0:
        raise click.UsageError('Parameter --awr-db-id cannot be whitespace or empty string')

    kwargs = {}
    if inst_num is not None:
        kwargs['inst_num'] = inst_num
    if begin_sn_id_greater_than_or_equal_to is not None:
        kwargs['begin_sn_id_greater_than_or_equal_to'] = begin_sn_id_greater_than_or_equal_to
    if end_sn_id_less_than_or_equal_to is not None:
        kwargs['end_sn_id_less_than_or_equal_to'] = end_sn_id_less_than_or_equal_to
    if time_greater_than_or_equal_to is not None:
        kwargs['time_greater_than_or_equal_to'] = time_greater_than_or_equal_to
    if time_less_than_or_equal_to is not None:
        kwargs['time_less_than_or_equal_to'] = time_less_than_or_equal_to
    if num_bucket is not None:
        kwargs['num_bucket'] = num_bucket
    if min_value is not None:
        kwargs['min_value'] = min_value
    if max_value is not None:
        kwargs['max_value'] = max_value
    if container_id is not None:
        kwargs['container_id'] = container_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.summarize_awr_db_wait_event_buckets(
        managed_database_id=managed_database_id,
        awr_db_id=awr_db_id,
        name=name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('db_management.summarize_awr_db_wait_events.command_name', 'summarize-awr-db-wait-events'), help=u"""Summarizes the AWR wait event sample data for the specified database in the AWR. The event data is summarized based on the Time dimension for each event. \n[Command Reference](summarizeAwrDbWaitEvents)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--awr-db-id', required=True, help=u"""The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs""")
@cli_util.option('--inst-num', help=u"""The optional single value query parameter to filter the database instance number.""")
@cli_util.option('--begin-sn-id-greater-than-or-equal-to', type=click.INT, help=u"""The optional greater than or equal to filter on the snapshot ID.""")
@cli_util.option('--end-sn-id-less-than-or-equal-to', type=click.INT, help=u"""The optional less than or equal to query parameter to filter the snapshot ID.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--name', multiple=True, help=u"""The optional multiple value query parameter to filter the entity name.""")
@cli_util.option('--session-type', type=custom_types.CliCaseInsensitiveChoice(["FOREGROUND", "BACKGROUND", "ALL"]), help=u"""The optional query parameter to filter ASH activities by FOREGROUND or BACKGROUND.""")
@cli_util.option('--container-id', type=click.INT, help=u"""The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in large paginated response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_BEGIN", "NAME"]), help=u"""The option to sort the data within a time period.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the default order.""")
@json_skeleton_utils.get_cli_json_input_option({'name': {'module': 'database_management', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'name': {'module': 'database_management', 'class': 'list[string]'}}, output_type={'module': 'database_management', 'class': 'AwrDbWaitEventCollection'})
@cli_util.wrap_exceptions
def summarize_awr_db_wait_events(ctx, from_json, managed_database_id, awr_db_id, inst_num, begin_sn_id_greater_than_or_equal_to, end_sn_id_less_than_or_equal_to, time_greater_than_or_equal_to, time_less_than_or_equal_to, name, session_type, container_id, page, limit, sort_by, sort_order):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(awr_db_id, six.string_types) and len(awr_db_id.strip()) == 0:
        raise click.UsageError('Parameter --awr-db-id cannot be whitespace or empty string')

    kwargs = {}
    if inst_num is not None:
        kwargs['inst_num'] = inst_num
    if begin_sn_id_greater_than_or_equal_to is not None:
        kwargs['begin_sn_id_greater_than_or_equal_to'] = begin_sn_id_greater_than_or_equal_to
    if end_sn_id_less_than_or_equal_to is not None:
        kwargs['end_sn_id_less_than_or_equal_to'] = end_sn_id_less_than_or_equal_to
    if time_greater_than_or_equal_to is not None:
        kwargs['time_greater_than_or_equal_to'] = time_greater_than_or_equal_to
    if time_less_than_or_equal_to is not None:
        kwargs['time_less_than_or_equal_to'] = time_less_than_or_equal_to
    if name is not None and len(name) > 0:
        kwargs['name'] = name
    if session_type is not None:
        kwargs['session_type'] = session_type
    if container_id is not None:
        kwargs['container_id'] = container_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.summarize_awr_db_wait_events(
        managed_database_id=managed_database_id,
        awr_db_id=awr_db_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@job_executions_status_summary_collection_group.command(name=cli_util.override('db_management.summarize_job_executions_statuses.command_name', 'summarize-job-executions-statuses'), help=u"""Gets the number of job executions grouped by status for a job, Managed Database, or Database Group in a specific compartment. Only one of the parameters, jobId, managedDatabaseId, or managedDatabaseGroupId should be provided. \n[Command Reference](summarizeJobExecutionsStatuses)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--start-time', required=True, help=u"""The start time of the time range to retrieve the status summary of job executions in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".""")
@cli_util.option('--end-time', required=True, help=u"""The end time of the time range to retrieve the status summary of job executions in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".""")
@cli_util.option('--id', help=u"""The identifier of the resource.""")
@cli_util.option('--managed-database-group-id', help=u"""The [OCID] of the Managed Database Group.""")
@cli_util.option('--managed-database-id', help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "NAME"]), help=u"""The field to sort information by. Only one sortOrder can be used. The default sort order for \u2018TIMECREATED\u2019 is descending and the default sort order for \u2018NAME\u2019 is ascending. The \u2018NAME\u2019 sort order is case-sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the default order.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'JobExecutionsStatusSummaryCollection'})
@cli_util.wrap_exceptions
def summarize_job_executions_statuses(ctx, from_json, compartment_id, start_time, end_time, id, managed_database_group_id, managed_database_id, name, sort_by, sort_order):

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if managed_database_group_id is not None:
        kwargs['managed_database_group_id'] = managed_database_group_id
    if managed_database_id is not None:
        kwargs['managed_database_id'] = managed_database_id
    if name is not None:
        kwargs['name'] = name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.summarize_job_executions_statuses(
        compartment_id=compartment_id,
        start_time=start_time,
        end_time=end_time,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@preferred_credential_group.command(name=cli_util.override('db_management.test_preferred_credential.command_name', 'test'), help=u"""Tests the preferred credential. \n[Command Reference](testPreferredCredential)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--credential-name', required=True, help=u"""The name of the preferred credential.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["BASIC"]), help=u"""The type of preferred credential. Only 'BASIC' is supported currently.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'TestPreferredCredentialStatus'})
@cli_util.wrap_exceptions
def test_preferred_credential(ctx, from_json, managed_database_id, credential_name, type):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(credential_name, six.string_types) and len(credential_name.strip()) == 0:
        raise click.UsageError('Parameter --credential-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['type'] = type

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.test_preferred_credential(
        managed_database_id=managed_database_id,
        credential_name=credential_name,
        test_preferred_credential_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@preferred_credential_group.command(name=cli_util.override('db_management.test_preferred_credential_test_basic_preferred_credential_details.command_name', 'test-preferred-credential-test-basic-preferred-credential-details'), help=u"""Tests the preferred credential. \n[Command Reference](testPreferredCredential)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--credential-name', required=True, help=u"""The name of the preferred credential.""")
@cli_util.option('--user-name', help=u"""The user name used to connect to the database.""")
@cli_util.option('--role', type=custom_types.CliCaseInsensitiveChoice(["NORMAL", "SYSDBA"]), help=u"""The role of the database user.""")
@cli_util.option('--password-secret-id', help=u"""The [OCID] of the Vault service secret that contains the database user password.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'TestPreferredCredentialStatus'})
@cli_util.wrap_exceptions
def test_preferred_credential_test_basic_preferred_credential_details(ctx, from_json, managed_database_id, credential_name, user_name, role, password_secret_id):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(credential_name, six.string_types) and len(credential_name.strip()) == 0:
        raise click.UsageError('Parameter --credential-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if user_name is not None:
        _details['userName'] = user_name

    if role is not None:
        _details['role'] = role

    if password_secret_id is not None:
        _details['passwordSecretId'] = password_secret_id

    _details['type'] = 'BASIC'

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.test_preferred_credential(
        managed_database_id=managed_database_id,
        credential_name=credential_name,
        test_preferred_credential_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@db_management_private_endpoint_group.command(name=cli_util.override('db_management.update_db_management_private_endpoint.command_name', 'update'), help=u"""Updates one or more attributes of a specific Database Management private endpoint. \n[Command Reference](updateDbManagementPrivateEndpoint)""")
@cli_util.option('--db-management-private-endpoint-id', required=True, help=u"""The [OCID] of the Database Management private endpoint.""")
@cli_util.option('--name', help=u"""The display name of the private endpoint.""")
@cli_util.option('--description', help=u"""The description of the private endpoint.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The OCIDs of the Network Security Groups to which the Database Management private endpoint belongs.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'nsg-ids': {'module': 'database_management', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'nsg-ids': {'module': 'database_management', 'class': 'list[string]'}}, output_type={'module': 'database_management', 'class': 'DbManagementPrivateEndpoint'})
@cli_util.wrap_exceptions
def update_db_management_private_endpoint(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, db_management_private_endpoint_id, name, description, nsg_ids, if_match):

    if isinstance(db_management_private_endpoint_id, six.string_types) and len(db_management_private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --db-management-private-endpoint-id cannot be whitespace or empty string')
    if not force:
        if nsg_ids:
            if not click.confirm("WARNING: Updates to nsg-ids will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.update_db_management_private_endpoint(
        db_management_private_endpoint_id=db_management_private_endpoint_id,
        update_db_management_private_endpoint_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_db_management_private_endpoint') and callable(getattr(client, 'get_db_management_private_endpoint')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_db_management_private_endpoint(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('db_management.update_job.command_name', 'update'), help=u"""Updates the details for the recurring scheduled job specified by jobId. Note that non-recurring (one time) jobs cannot be updated. \n[Command Reference](updateJob)""")
@cli_util.option('--job-id', required=True, help=u"""The identifier of the job.""")
@cli_util.option('--description', help=u"""The description of the job.""")
@cli_util.option('--job-type', type=custom_types.CliCaseInsensitiveChoice(["SQL"]), help=u"""The type of job.""")
@cli_util.option('--timeout', help=u"""The job timeout duration, which is expressed like \"1h 10m 15s\".""")
@cli_util.option('--result-location', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--schedule-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'result-location': {'module': 'database_management', 'class': 'JobExecutionResultLocation'}, 'schedule-details': {'module': 'database_management', 'class': 'JobScheduleDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'result-location': {'module': 'database_management', 'class': 'JobExecutionResultLocation'}, 'schedule-details': {'module': 'database_management', 'class': 'JobScheduleDetails'}}, output_type={'module': 'database_management', 'class': 'Job'})
@cli_util.wrap_exceptions
def update_job(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, job_id, description, job_type, timeout, result_location, schedule_details, if_match):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')
    if not force:
        if result_location or schedule_details:
            if not click.confirm("WARNING: Updates to result-location and schedule-details will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if job_type is not None:
        _details['jobType'] = job_type

    if timeout is not None:
        _details['timeout'] = timeout

    if result_location is not None:
        _details['resultLocation'] = cli_util.parse_json_parameter("result_location", result_location)

    if schedule_details is not None:
        _details['scheduleDetails'] = cli_util.parse_json_parameter("schedule_details", schedule_details)

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.update_job(
        job_id=job_id,
        update_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('db_management.update_job_update_sql_job_details.command_name', 'update-job-update-sql-job-details'), help=u"""Updates the details for the recurring scheduled job specified by jobId. Note that non-recurring (one time) jobs cannot be updated. \n[Command Reference](updateJob)""")
@cli_util.option('--job-id', required=True, help=u"""The identifier of the job.""")
@cli_util.option('--description', help=u"""The description of the job.""")
@cli_util.option('--timeout', help=u"""The job timeout duration, which is expressed like \"1h 10m 15s\".""")
@cli_util.option('--result-location', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--schedule-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--sql-text', help=u"""The SQL text to be executed as part of the job.""")
@cli_util.option('--sql-type', help=u"""""")
@cli_util.option('--user-name', help=u"""The database user name used to execute the SQL job. If the job is being executed on a Managed Database Group, then the user name should exist on all the databases in the group with the same password.""")
@cli_util.option('--password', help=u"""The password for the database user name used to execute the SQL job.""")
@cli_util.option('--secret-id', help=u"""The [OCID] of the secret containing the user password.""")
@cli_util.option('--role', help=u"""The role of the database user. Indicates whether the database user is a normal user or sysdba.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'result-location': {'module': 'database_management', 'class': 'JobExecutionResultLocation'}, 'schedule-details': {'module': 'database_management', 'class': 'JobScheduleDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'result-location': {'module': 'database_management', 'class': 'JobExecutionResultLocation'}, 'schedule-details': {'module': 'database_management', 'class': 'JobScheduleDetails'}}, output_type={'module': 'database_management', 'class': 'Job'})
@cli_util.wrap_exceptions
def update_job_update_sql_job_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, job_id, description, timeout, result_location, schedule_details, sql_text, sql_type, user_name, password, secret_id, role, if_match):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')
    if not force:
        if result_location or schedule_details:
            if not click.confirm("WARNING: Updates to result-location and schedule-details will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if timeout is not None:
        _details['timeout'] = timeout

    if result_location is not None:
        _details['resultLocation'] = cli_util.parse_json_parameter("result_location", result_location)

    if schedule_details is not None:
        _details['scheduleDetails'] = cli_util.parse_json_parameter("schedule_details", schedule_details)

    if sql_text is not None:
        _details['sqlText'] = sql_text

    if sql_type is not None:
        _details['sqlType'] = sql_type

    if user_name is not None:
        _details['userName'] = user_name

    if password is not None:
        _details['password'] = password

    if secret_id is not None:
        _details['secretId'] = secret_id

    if role is not None:
        _details['role'] = role

    _details['jobType'] = 'SQL'

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.update_job(
        job_id=job_id,
        update_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('db_management.update_job_object_storage_job_execution_result_location.command_name', 'update-job-object-storage-job-execution-result-location'), help=u"""Updates the details for the recurring scheduled job specified by jobId. Note that non-recurring (one time) jobs cannot be updated. \n[Command Reference](updateJob)""")
@cli_util.option('--job-id', required=True, help=u"""The identifier of the job.""")
@cli_util.option('--description', help=u"""The description of the job.""")
@cli_util.option('--timeout', help=u"""The job timeout duration, which is expressed like \"1h 10m 15s\".""")
@cli_util.option('--schedule-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--result-location-namespace-name', help=u"""The Object Storage namespace used for job execution result storage.""")
@cli_util.option('--result-location-bucket-name', help=u"""The name of the bucket used for job execution result storage.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'schedule-details': {'module': 'database_management', 'class': 'JobScheduleDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'schedule-details': {'module': 'database_management', 'class': 'JobScheduleDetails'}}, output_type={'module': 'database_management', 'class': 'Job'})
@cli_util.wrap_exceptions
def update_job_object_storage_job_execution_result_location(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, job_id, description, timeout, schedule_details, if_match, result_location_namespace_name, result_location_bucket_name):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')
    if not force:
        if schedule_details:
            if not click.confirm("WARNING: Updates to schedule-details will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['resultLocation'] = {}

    if description is not None:
        _details['description'] = description

    if timeout is not None:
        _details['timeout'] = timeout

    if schedule_details is not None:
        _details['scheduleDetails'] = cli_util.parse_json_parameter("schedule_details", schedule_details)

    if result_location_namespace_name is not None:
        _details['resultLocation']['namespaceName'] = result_location_namespace_name

    if result_location_bucket_name is not None:
        _details['resultLocation']['bucketName'] = result_location_bucket_name

    _details['resultLocation']['type'] = 'OBJECT_STORAGE'

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.update_job(
        job_id=job_id,
        update_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@managed_database_group_group.command(name=cli_util.override('db_management.update_managed_database_group.command_name', 'update'), help=u"""Updates the Managed Database Group specified by managedDatabaseGroupId. \n[Command Reference](updateManagedDatabaseGroup)""")
@cli_util.option('--managed-database-group-id', required=True, help=u"""The [OCID] of the Managed Database Group.""")
@cli_util.option('--description', help=u"""The information specified by the user about the Managed Database Group.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'ManagedDatabaseGroup'})
@cli_util.wrap_exceptions
def update_managed_database_group(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, managed_database_group_id, description, if_match):

    if isinstance(managed_database_group_id, six.string_types) and len(managed_database_group_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-group-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.update_managed_database_group(
        managed_database_group_id=managed_database_group_id,
        update_managed_database_group_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_managed_database_group') and callable(getattr(client, 'get_managed_database_group')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_managed_database_group(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@preferred_credential_group.command(name=cli_util.override('db_management.update_preferred_credential.command_name', 'update'), help=u"""Updates the preferred credential based on the credentialName. \n[Command Reference](updatePreferredCredential)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--credential-name', required=True, help=u"""The name of the preferred credential.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["BASIC"]), help=u"""The type of preferred credential.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'PreferredCredential'})
@cli_util.wrap_exceptions
def update_preferred_credential(ctx, from_json, managed_database_id, credential_name, type, if_match):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(credential_name, six.string_types) and len(credential_name.strip()) == 0:
        raise click.UsageError('Parameter --credential-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['type'] = type

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.update_preferred_credential(
        managed_database_id=managed_database_id,
        credential_name=credential_name,
        update_preferred_credential_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@preferred_credential_group.command(name=cli_util.override('db_management.update_preferred_credential_update_basic_preferred_credential_details.command_name', 'update-preferred-credential-update-basic-preferred-credential-details'), help=u"""Updates the preferred credential based on the credentialName. \n[Command Reference](updatePreferredCredential)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--credential-name', required=True, help=u"""The name of the preferred credential.""")
@cli_util.option('--user-name', help=u"""The user name used to connect to the database.""")
@cli_util.option('--role', type=custom_types.CliCaseInsensitiveChoice(["NORMAL", "SYSDBA"]), help=u"""The role of the database user.""")
@cli_util.option('--password-secret-id', help=u"""The [OCID] of the Vault service secret that contains the database user password.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'PreferredCredential'})
@cli_util.wrap_exceptions
def update_preferred_credential_update_basic_preferred_credential_details(ctx, from_json, managed_database_id, credential_name, user_name, role, password_secret_id, if_match):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(credential_name, six.string_types) and len(credential_name.strip()) == 0:
        raise click.UsageError('Parameter --credential-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if user_name is not None:
        _details['userName'] = user_name

    if role is not None:
        _details['role'] = role

    if password_secret_id is not None:
        _details['passwordSecretId'] = password_secret_id

    _details['type'] = 'BASIC'

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.update_preferred_credential(
        managed_database_id=managed_database_id,
        credential_name=credential_name,
        update_preferred_credential_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@tablespace_group.command(name=cli_util.override('db_management.update_tablespace.command_name', 'update'), help=u"""Updates the attributes of the tablespace specified by tablespaceName within the Managed Database specified by managedDatabaseId. \n[Command Reference](updateTablespace)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--tablespace-name', required=True, help=u"""The name of the tablespace.""")
@cli_util.option('--credential-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--name', help=u"""The name of the tablespace. It must be unique within a database.""")
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["PERMANENT", "TEMPORARY"]), help=u"""The type of tablespace.""")
@cli_util.option('--file-size', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The size of each data file or temp file.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["READ_ONLY", "READ_WRITE"]), help=u"""The status of the tablespace.""")
@cli_util.option('--is-auto-extensible', type=click.BOOL, help=u"""Specifies whether the data file or temp file can be extended automatically.""")
@cli_util.option('--auto-extend-next-size', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The size of the next increment of disk space to be allocated automatically when more extents are required.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--auto-extend-max-size', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The maximum disk space allowed for automatic extension of the data files or temp files.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-max-size-unlimited', type=click.BOOL, help=u"""Specifies whether the disk space of the data file or temp file can be limited.""")
@cli_util.option('--is-default', type=click.BOOL, help=u"""Specifies whether the tablespace is the default tablespace.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'credential-details': {'module': 'database_management', 'class': 'TablespaceAdminCredentialDetails'}, 'file-size': {'module': 'database_management', 'class': 'TablespaceStorageSize'}, 'auto-extend-next-size': {'module': 'database_management', 'class': 'TablespaceStorageSize'}, 'auto-extend-max-size': {'module': 'database_management', 'class': 'TablespaceStorageSize'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'credential-details': {'module': 'database_management', 'class': 'TablespaceAdminCredentialDetails'}, 'file-size': {'module': 'database_management', 'class': 'TablespaceStorageSize'}, 'auto-extend-next-size': {'module': 'database_management', 'class': 'TablespaceStorageSize'}, 'auto-extend-max-size': {'module': 'database_management', 'class': 'TablespaceStorageSize'}}, output_type={'module': 'database_management', 'class': 'Tablespace'})
@cli_util.wrap_exceptions
def update_tablespace(ctx, from_json, force, managed_database_id, tablespace_name, credential_details, name, type, file_size, status, is_auto_extensible, auto_extend_next_size, auto_extend_max_size, is_max_size_unlimited, is_default):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    if isinstance(tablespace_name, six.string_types) and len(tablespace_name.strip()) == 0:
        raise click.UsageError('Parameter --tablespace-name cannot be whitespace or empty string')
    if not force:
        if credential_details or file_size or auto_extend_next_size or auto_extend_max_size:
            if not click.confirm("WARNING: Updates to credential-details and file-size and auto-extend-next-size and auto-extend-max-size will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['credentialDetails'] = cli_util.parse_json_parameter("credential_details", credential_details)

    if name is not None:
        _details['name'] = name

    if type is not None:
        _details['type'] = type

    if file_size is not None:
        _details['fileSize'] = cli_util.parse_json_parameter("file_size", file_size)

    if status is not None:
        _details['status'] = status

    if is_auto_extensible is not None:
        _details['isAutoExtensible'] = is_auto_extensible

    if auto_extend_next_size is not None:
        _details['autoExtendNextSize'] = cli_util.parse_json_parameter("auto_extend_next_size", auto_extend_next_size)

    if auto_extend_max_size is not None:
        _details['autoExtendMaxSize'] = cli_util.parse_json_parameter("auto_extend_max_size", auto_extend_max_size)

    if is_max_size_unlimited is not None:
        _details['isMaxSizeUnlimited'] = is_max_size_unlimited

    if is_default is not None:
        _details['isDefault'] = is_default

    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.update_tablespace(
        managed_database_id=managed_database_id,
        tablespace_name=tablespace_name,
        update_tablespace_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
