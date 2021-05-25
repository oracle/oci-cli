# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('database_management.database_management_root_group.command_name', 'database-management'), cls=CommandGroupWithAlias, help=cli_util.override('database_management.database_management_root_group.help', """Use the Database Management API to perform tasks such as obtaining performance and resource usage metrics
for a fleet of Managed Databases or a specific Managed Database, creating Managed Database Groups, and
running a SQL job on a Managed Database or Managed Database Group."""), short_help=cli_util.override('database_management.database_management_root_group.short_help', """Database Management API"""))
@cli_util.help_option_group
def database_management_root_group():
    pass


@click.command(cli_util.override('database_management.database_fleet_health_metrics_group.command_name', 'database-fleet-health-metrics'), cls=CommandGroupWithAlias, help="""The details of the fleet health metrics.""")
@cli_util.help_option_group
def database_fleet_health_metrics_group():
    pass


@click.command(cli_util.override('database_management.tablespace_group.command_name', 'tablespace'), cls=CommandGroupWithAlias, help="""The details of a tablespace.""")
@cli_util.help_option_group
def tablespace_group():
    pass


@click.command(cli_util.override('database_management.managed_database_group.command_name', 'managed-database'), cls=CommandGroupWithAlias, help="""The details of a Managed Database.""")
@cli_util.help_option_group
def managed_database_group():
    pass


@click.command(cli_util.override('database_management.cluster_cache_metric_group.command_name', 'cluster-cache-metric'), cls=CommandGroupWithAlias, help="""The response containing the cluster cache metrics for the Oracle Real Application Clusters (Oracle RAC) database.""")
@cli_util.help_option_group
def cluster_cache_metric_group():
    pass


@click.command(cli_util.override('database_management.job_run_group.command_name', 'job-run'), cls=CommandGroupWithAlias, help="""The details of a specific job run.""")
@cli_util.help_option_group
def job_run_group():
    pass


@click.command(cli_util.override('database_management.job_execution_group.command_name', 'job-execution'), cls=CommandGroupWithAlias, help="""The details of a job execution.""")
@cli_util.help_option_group
def job_execution_group():
    pass


@click.command(cli_util.override('database_management.managed_database_group_group.command_name', 'managed-database-group'), cls=CommandGroupWithAlias, help="""The details of a Managed Database Group.""")
@cli_util.help_option_group
def managed_database_group_group():
    pass


@click.command(cli_util.override('database_management.database_home_metrics_group.command_name', 'database-home-metrics'), cls=CommandGroupWithAlias, help="""The response containing the metric collection for a specific database.""")
@cli_util.help_option_group
def database_home_metrics_group():
    pass


@click.command(cli_util.override('database_management.job_group.command_name', 'job'), cls=CommandGroupWithAlias, help="""The details of the job.""")
@cli_util.help_option_group
def job_group():
    pass


database_management_root_group.add_command(database_fleet_health_metrics_group)
database_management_root_group.add_command(tablespace_group)
database_management_root_group.add_command(managed_database_group)
database_management_root_group.add_command(cluster_cache_metric_group)
database_management_root_group.add_command(job_run_group)
database_management_root_group.add_command(job_execution_group)
database_management_root_group.add_command(managed_database_group_group)
database_management_root_group.add_command(database_home_metrics_group)
database_management_root_group.add_command(job_group)


@managed_database_group_group.command(name=cli_util.override('database_management.add_managed_database_to_managed_database_group.command_name', 'add'), help=u"""Adds a Managed Database to a specific Managed Database Group. After the database is added, it will be included in the management activities performed on the Managed Database Group. \n[Command Reference](addManagedDatabaseToManagedDatabaseGroup)""")
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


@managed_database_group.command(name=cli_util.override('database_management.change_database_parameters.command_name', 'change-database-parameters'), help=u"""Changes database parameter values. There are two kinds of database parameters:

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


@job_group.command(name=cli_util.override('database_management.change_job_compartment.command_name', 'change-compartment'), help=u"""Moves a job. \n[Command Reference](changeJobCompartment)""")
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


@managed_database_group_group.command(name=cli_util.override('database_management.change_managed_database_group_compartment.command_name', 'change-compartment'), help=u"""Moves a Managed Database Group to a different compartment. The destination compartment must not have a Managed Database Group with the same name. \n[Command Reference](changeManagedDatabaseGroupCompartment)""")
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


@job_group.command(name=cli_util.override('database_management.create_job.command_name', 'create'), help=u"""Creates a job to be executed on a Managed Database or Managed Database Group. Only one of the parameters, managedDatabaseId or managedDatabaseGroupId should be provided as input in CreateJobDetails resource in request body. \n[Command Reference](createJob)""")
@cli_util.option('--name', required=True, help=u"""The name of the job. Valid characters are uppercase or lowercase letters, numbers, and \"_\". The name of the job cannot be modified. It must be unique in the compartment and must begin with an alphabetic character.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which the job resides.""")
@cli_util.option('--schedule-type', required=True, help=u"""The schedule type of the job.""")
@cli_util.option('--job-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["SQL"]), help=u"""The type of job.""")
@cli_util.option('--description', help=u"""The description of the job.""")
@cli_util.option('--managed-database-group-id', help=u"""The [OCID] of the Managed Database Group where the job has to be executed.""")
@cli_util.option('--managed-database-id', help=u"""The [OCID] of the Managed Database where the job has to be executed.""")
@cli_util.option('--database-sub-type', type=custom_types.CliCaseInsensitiveChoice(["CDB", "PDB", "NON_CDB"]), help=u"""The subtype of the Oracle Database where the job has to be executed. Only applicable when managedDatabaseGroupId is provided.""")
@cli_util.option('--timeout', help=u"""The job timeout duration, which is expressed like \"1h 10m 15s\".""")
@cli_util.option('--result-location', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'result-location': {'module': 'database_management', 'class': 'JobExecutionResultLocation'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'result-location': {'module': 'database_management', 'class': 'JobExecutionResultLocation'}}, output_type={'module': 'database_management', 'class': 'Job'})
@cli_util.wrap_exceptions
def create_job(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, compartment_id, schedule_type, job_type, description, managed_database_group_id, managed_database_id, database_sub_type, timeout, result_location):

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


@job_group.command(name=cli_util.override('database_management.create_job_create_sql_job_details.command_name', 'create-job-create-sql-job-details'), help=u"""Creates a job to be executed on a Managed Database or Managed Database Group. Only one of the parameters, managedDatabaseId or managedDatabaseGroupId should be provided as input in CreateJobDetails resource in request body. \n[Command Reference](createJob)""")
@cli_util.option('--name', required=True, help=u"""The name of the job. Valid characters are uppercase or lowercase letters, numbers, and \"_\". The name of the job cannot be modified. It must be unique in the compartment and must begin with an alphabetic character.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which the job resides.""")
@cli_util.option('--schedule-type', required=True, help=u"""The schedule type of the job.""")
@cli_util.option('--operation-type', required=True, help=u"""The SQL operation type.""")
@cli_util.option('--description', help=u"""The description of the job.""")
@cli_util.option('--managed-database-group-id', help=u"""The [OCID] of the Managed Database Group where the job has to be executed.""")
@cli_util.option('--managed-database-id', help=u"""The [OCID] of the Managed Database where the job has to be executed.""")
@cli_util.option('--database-sub-type', type=custom_types.CliCaseInsensitiveChoice(["CDB", "PDB", "NON_CDB"]), help=u"""The subtype of the Oracle Database where the job has to be executed. Only applicable when managedDatabaseGroupId is provided.""")
@cli_util.option('--timeout', help=u"""The job timeout duration, which is expressed like \"1h 10m 15s\".""")
@cli_util.option('--result-location', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--sql-text', help=u"""The SQL text to be executed as part of the job.""")
@cli_util.option('--sql-type', help=u"""""")
@cli_util.option('--user-name', help=u"""The database user name used to execute the SQL job. If the job is being executed on a Managed Database Group, then the user name should exist on all the databases in the group with the same password.""")
@cli_util.option('--password', help=u"""The password for the database user name used to execute the SQL job.""")
@cli_util.option('--role', help=u"""The role of the database user. Indicates whether the database user is a normal user or sysdba.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'result-location': {'module': 'database_management', 'class': 'JobExecutionResultLocation'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'result-location': {'module': 'database_management', 'class': 'JobExecutionResultLocation'}}, output_type={'module': 'database_management', 'class': 'Job'})
@cli_util.wrap_exceptions
def create_job_create_sql_job_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, compartment_id, schedule_type, operation_type, description, managed_database_group_id, managed_database_id, database_sub_type, timeout, result_location, sql_text, sql_type, user_name, password, role):

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

    if sql_text is not None:
        _details['sqlText'] = sql_text

    if sql_type is not None:
        _details['sqlType'] = sql_type

    if user_name is not None:
        _details['userName'] = user_name

    if password is not None:
        _details['password'] = password

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


@job_group.command(name=cli_util.override('database_management.create_job_object_storage_job_execution_result_location.command_name', 'create-job-object-storage-job-execution-result-location'), help=u"""Creates a job to be executed on a Managed Database or Managed Database Group. Only one of the parameters, managedDatabaseId or managedDatabaseGroupId should be provided as input in CreateJobDetails resource in request body. \n[Command Reference](createJob)""")
@cli_util.option('--name', required=True, help=u"""The name of the job. Valid characters are uppercase or lowercase letters, numbers, and \"_\". The name of the job cannot be modified. It must be unique in the compartment and must begin with an alphabetic character.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which the job resides.""")
@cli_util.option('--schedule-type', required=True, help=u"""The schedule type of the job.""")
@cli_util.option('--description', help=u"""The description of the job.""")
@cli_util.option('--managed-database-group-id', help=u"""The [OCID] of the Managed Database Group where the job has to be executed.""")
@cli_util.option('--managed-database-id', help=u"""The [OCID] of the Managed Database where the job has to be executed.""")
@cli_util.option('--database-sub-type', type=custom_types.CliCaseInsensitiveChoice(["CDB", "PDB", "NON_CDB"]), help=u"""The subtype of the Oracle Database where the job has to be executed. Only applicable when managedDatabaseGroupId is provided.""")
@cli_util.option('--timeout', help=u"""The job timeout duration, which is expressed like \"1h 10m 15s\".""")
@cli_util.option('--result-location-namespace-name', help=u"""The Object Storage namespace used for job execution result storage.""")
@cli_util.option('--result-location-bucket-name', help=u"""The name of the bucket used for job execution result storage.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'Job'})
@cli_util.wrap_exceptions
def create_job_object_storage_job_execution_result_location(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, compartment_id, schedule_type, description, managed_database_group_id, managed_database_id, database_sub_type, timeout, result_location_namespace_name, result_location_bucket_name):

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


@managed_database_group_group.command(name=cli_util.override('database_management.create_managed_database_group.command_name', 'create'), help=u"""Creates a Managed Database Group. The group does not contain any Managed Databases when it is created, and they must be added later. \n[Command Reference](createManagedDatabaseGroup)""")
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


@job_group.command(name=cli_util.override('database_management.delete_job.command_name', 'delete'), help=u"""Deletes the job specified by jobId. \n[Command Reference](deleteJob)""")
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


@managed_database_group_group.command(name=cli_util.override('database_management.delete_managed_database_group.command_name', 'delete'), help=u"""Deletes the Managed Database Group specified by managedDatabaseGroupId. If the group contains Managed Databases, then it cannot be deleted. \n[Command Reference](deleteManagedDatabaseGroup)""")
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


@managed_database_group.command(name=cli_util.override('database_management.get_awr_db_report.command_name', 'get-awr-db-report'), help=u"""Gets the AWR report for the specified Managed Database. \n[Command Reference](getAwrDbReport)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--awr-db-id', required=True, help=u"""The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs:""")
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


@managed_database_group.command(name=cli_util.override('database_management.get_awr_db_sql_report.command_name', 'get-awr-db-sql-report'), help=u"""Get a AWR SQL report for one SQL. \n[Command Reference](getAwrDbSqlReport)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--awr-db-id', required=True, help=u"""The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs:""")
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


@cluster_cache_metric_group.command(name=cli_util.override('database_management.get_cluster_cache_metric.command_name', 'get'), help=u"""Gets the metrics related to cluster cache for the Oracle Real Application Clusters (Oracle RAC) database specified by managedDatabaseId. \n[Command Reference](getClusterCacheMetric)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--start-time', required=True, help=u"""The start time for the time range to retrieve the health metrics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".""")
@cli_util.option('--end-time', required=True, help=u"""The end time for the time range to retrieve the health metrics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".""")
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


@database_fleet_health_metrics_group.command(name=cli_util.override('database_management.get_database_fleet_health_metrics.command_name', 'get'), help=u"""Gets the health metrics for a fleet of databases in a compartment or in a Managed Database Group. Either the CompartmentId or the ManagedDatabaseGroupId query parameters must be provided to retrieve the health metrics. \n[Command Reference](getDatabaseFleetHealthMetrics)""")
@cli_util.option('--compare-baseline-time', required=True, help=u"""The baseline time for metrics comparison.""")
@cli_util.option('--compare-target-time', required=True, help=u"""The target time for metrics comparison.""")
@cli_util.option('--managed-database-group-id', help=u"""The [OCID] of the Managed Database Group.""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment.""")
@cli_util.option('--compare-type', type=custom_types.CliCaseInsensitiveChoice(["HOUR", "DAY"]), help=u"""The time window used for metrics comparison.""")
@cli_util.option('--filter-by-metric-names', help=u"""The filter used to retrieve a specific set of metrics by passing the desired metric names with a comma separator. Note that, by default, the service returns all supported metrics.""")
@cli_util.option('--filter-by-database-type', help=u"""The filter used to filter the databases in the fleet by a specific Oracle Database type.""")
@cli_util.option('--filter-by-database-sub-type', help=u"""The filter used to filter the databases in the fleet by a specific Oracle Database subtype.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'DatabaseFleetHealthMetrics'})
@cli_util.wrap_exceptions
def get_database_fleet_health_metrics(ctx, from_json, compare_baseline_time, compare_target_time, managed_database_group_id, compartment_id, compare_type, filter_by_metric_names, filter_by_database_type, filter_by_database_sub_type):

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
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'db_management', ctx)
    result = client.get_database_fleet_health_metrics(
        compare_baseline_time=compare_baseline_time,
        compare_target_time=compare_target_time,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_home_metrics_group.command(name=cli_util.override('database_management.get_database_home_metrics.command_name', 'get'), help=u"""Gets a summary of the activity and resource usage metrics like DB Time, CPU, User I/O, Wait, Storage, and Memory for a Managed Database. \n[Command Reference](getDatabaseHomeMetrics)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--start-time', required=True, help=u"""The start time for the time range to retrieve the health metrics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".""")
@cli_util.option('--end-time', required=True, help=u"""The end time for the time range to retrieve the health metrics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".""")
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


@job_group.command(name=cli_util.override('database_management.get_job.command_name', 'get'), help=u"""Gets the details for the job specified by jobId. \n[Command Reference](getJob)""")
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


@job_execution_group.command(name=cli_util.override('database_management.get_job_execution.command_name', 'get'), help=u"""Gets the details for the job execution specified by jobExecutionId. \n[Command Reference](getJobExecution)""")
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


@job_run_group.command(name=cli_util.override('database_management.get_job_run.command_name', 'get'), help=u"""Gets the details for the job run specified by jobRunId. \n[Command Reference](getJobRun)""")
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


@managed_database_group.command(name=cli_util.override('database_management.get_managed_database.command_name', 'get'), help=u"""Gets the details for the Managed Database specified by managedDatabaseId. \n[Command Reference](getManagedDatabase)""")
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


@managed_database_group_group.command(name=cli_util.override('database_management.get_managed_database_group.command_name', 'get'), help=u"""Gets the details for the Managed Database Group specified by managedDatabaseGroupId. \n[Command Reference](getManagedDatabaseGroup)""")
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


@managed_database_group.command(name=cli_util.override('database_management.list_awr_db_snapshots.command_name', 'list-awr-db-snapshots'), help=u"""Lists AWR snapshots for the specified database in the AWR. \n[Command Reference](listAwrDbSnapshots)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--awr-db-id', required=True, help=u"""The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs:""")
@cli_util.option('--inst-num', help=u"""The optional single value query parameter to filter the database instance number.""")
@cli_util.option('--begin-sn-id-greater-than-or-equal-to', type=click.INT, help=u"""The optional greater than or equal to filter on the snapshot ID.""")
@cli_util.option('--end-sn-id-less-than-or-equal-to', type=click.INT, help=u"""The optional less than or equal to query parameter to filter the snapshot ID.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--container-id', type=click.INT, help=u"""The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges""")
@cli_util.option('--page', help=u"""The page token representing the page, from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in paginated response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_BEGIN", "SNAPSHOT_ID"]), help=u"""The option to sort the AWR snapshot summary data.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the the default order.""")
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


@managed_database_group.command(name=cli_util.override('database_management.list_awr_dbs.command_name', 'list-awr-dbs'), help=u"""Gets the list of databases and their snapshot summary details available in the AWR of the specified Managed Database. \n[Command Reference](listAwrDbs)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--name', help=u"""The optional single value query parameter to filter the entity name.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--page', help=u"""The page token representing the page, from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in paginated response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["END_INTERVAL_TIME", "NAME"]), help=u"""The option to sort the AWR summary data.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the the default order.""")
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


@managed_database_group.command(name=cli_util.override('database_management.list_database_parameters.command_name', 'list-database-parameters'), help=u"""Gets the list of database parameters for the specified Managed Database. The parameters are listed in alphabetical order, along with their current values. \n[Command Reference](listDatabaseParameters)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--source', type=custom_types.CliCaseInsensitiveChoice(["CURRENT", "SPFILE"]), help=u"""The source used to list database parameters. `CURRENT` is used to get the database parameters that are currently in effect for the database instance. `SPFILE` is used to list parameters from the server parameter file. Default is `CURRENT`.""")
@cli_util.option('--name', help=u"""A filter to return all parameters that have the text given in their names.""")
@cli_util.option('--is-allowed-values-included', type=click.BOOL, help=u"""When true, results include a list of valid values for parameters (if applicable).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["NAME"]), help=u"""The field to sort information by. Only one sortOrder can be used. The default sort order for `NAME` is ascending and it is case-sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the the default order.""")
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


@job_execution_group.command(name=cli_util.override('database_management.list_job_executions.command_name', 'list'), help=u"""Gets the job execution for a specific ID or the list of job executions for a job, Managed Database or Managed Database Group in a specific compartment. Only one of the parameters, ID, jobId, managedDatabaseId or managedDatabaseGroupId should be provided. If none of these parameters is provided, all the job executions in the compartment are listed. Job executions can also be filtered based on the name and status parameters. \n[Command Reference](listJobExecutions)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--id', help=u"""The identifier of the resource.""")
@cli_util.option('--job-id', help=u"""The identifier of the job.""")
@cli_util.option('--managed-database-id', help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--managed-database-group-id', help=u"""The [OCID] of the Managed Database Group.""")
@cli_util.option('--status', help=u"""The status of the job execution.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in paginated response.""")
@cli_util.option('--page', help=u"""The page token representing the page, from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "NAME"]), help=u"""The field to sort information by. Only one sortOrder can be used. The default sort order for \u2018TIMECREATED\u2019 is descending and the default sort order for \u2018NAME\u2019 is ascending. The \u2018NAME\u2019 sort order is case-sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the the default order.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'JobExecutionCollection'})
@cli_util.wrap_exceptions
def list_job_executions(ctx, from_json, all_pages, page_size, compartment_id, id, job_id, managed_database_id, managed_database_group_id, status, name, limit, page, sort_by, sort_order):

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


@job_run_group.command(name=cli_util.override('database_management.list_job_runs.command_name', 'list'), help=u"""Gets the job run for a specific ID or the list of job runs for a job, Managed Database or Managed Database Group in a specific compartment. Only one of the parameters, ID, jobId, managedDatabaseId, or managedDatabaseGroupId should be provided. If none of these parameters is provided, all the job runs in the compartment are listed. Job runs can also be filtered based on name and runStatus parameters. \n[Command Reference](listJobRuns)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--id', help=u"""The identifier of the resource.""")
@cli_util.option('--job-id', help=u"""The identifier of the job.""")
@cli_util.option('--managed-database-id', help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--managed-database-group-id', help=u"""The [OCID] of the Managed Database Group.""")
@cli_util.option('--run-status', help=u"""The status of the job run.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in paginated response.""")
@cli_util.option('--page', help=u"""The page token representing the page, from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "NAME"]), help=u"""The field to sort information by. Only one sortOrder can be used. The default sort order for \u2018TIMECREATED\u2019 is descending and the default sort order for \u2018NAME\u2019 is ascending. The \u2018NAME\u2019 sort order is case-sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the the default order.""")
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


@job_group.command(name=cli_util.override('database_management.list_jobs.command_name', 'list'), help=u"""Gets the job for a specific ID or the list of jobs for a Managed Database or Managed Database Group in a specific compartment. Only one of the parameters, ID, managedDatabaseId or managedDatabaseGroupId, should be provided. If none of these parameters is provided, all the jobs in the compartment are listed. Jobs can also be filtered based on the name and lifecycleState parameters. \n[Command Reference](listJobs)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--id', help=u"""The identifier of the resource.""")
@cli_util.option('--managed-database-group-id', help=u"""The [OCID] of the Managed Database Group.""")
@cli_util.option('--managed-database-id', help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), help=u"""The lifecycle state of the job.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in paginated response.""")
@cli_util.option('--page', help=u"""The page token representing the page, from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "NAME"]), help=u"""The field to sort information by. Only one sortOrder can be used. The default sort order for \u2018TIMECREATED\u2019 is descending and the default sort order for \u2018NAME\u2019 is ascending. The \u2018NAME\u2019 sort order is case-sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the the default order.""")
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


@managed_database_group_group.command(name=cli_util.override('database_management.list_managed_database_groups.command_name', 'list'), help=u"""Gets the Managed Database Group for a specific ID or the list of Managed Database Groups in a specific compartment. Managed Database Groups can also be filtered based on the name parameter. Only one of the parameters, ID or name should be provided. If none of these parameters is provided, all the Managed Database Groups in the compartment are listed. \n[Command Reference](listManagedDatabaseGroups)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--id', help=u"""The identifier of the resource.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The lifecycle state of a resource.""")
@cli_util.option('--page', help=u"""The page token representing the page, from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in paginated response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "NAME"]), help=u"""The field to sort information by. Only one sortOrder can be used. The default sort order for \u2018TIMECREATED\u2019 is descending and the default sort order for \u2018NAME\u2019 is ascending. The \u2018NAME\u2019 sort order is case-sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the the default order.""")
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


@managed_database_group.command(name=cli_util.override('database_management.list_managed_databases.command_name', 'list'), help=u"""Gets the Managed Database for a specific ID or the list of Managed Databases in a specific compartment. Managed Databases can also be filtered based on the name parameter. Only one of the parameters, ID or name should be provided. If none of these parameters is provided, all the Managed Databases in the compartment are listed. \n[Command Reference](listManagedDatabases)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--id', help=u"""The identifier of the resource.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name.""")
@cli_util.option('--page', help=u"""The page token representing the page, from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in paginated response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "NAME"]), help=u"""The field to sort information by. Only one sortOrder can be used. The default sort order for \u2018TIMECREATED\u2019 is descending and the default sort order for \u2018NAME\u2019 is ascending. The \u2018NAME\u2019 sort order is case-sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the the default order.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'ManagedDatabaseCollection'})
@cli_util.wrap_exceptions
def list_managed_databases(ctx, from_json, all_pages, page_size, compartment_id, id, name, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if name is not None:
        kwargs['name'] = name
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


@tablespace_group.command(name=cli_util.override('database_management.list_tablespaces.command_name', 'list'), help=u"""Gets the list of tablespaces for the specified managedDatabaseId. \n[Command Reference](listTablespaces)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "NAME"]), help=u"""The field to sort information by. Only one sortOrder can be used. The default sort order for \u2018TIMECREATED\u2019 is descending and the default sort order for \u2018NAME\u2019 is ascending. The \u2018NAME\u2019 sort order is case-sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the the default order.""")
@cli_util.option('--page', help=u"""The page token representing the page, from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in paginated response.""")
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


@managed_database_group_group.command(name=cli_util.override('database_management.remove_managed_database_from_managed_database_group.command_name', 'remove'), help=u"""Removes a Managed Database from a Managed Database Group. Any management activities that are currently running on this database will continue to run to completion. However, any activities scheduled to run in the future will not be performed on this database. \n[Command Reference](removeManagedDatabaseFromManagedDatabaseGroup)""")
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


@managed_database_group.command(name=cli_util.override('database_management.reset_database_parameters.command_name', 'reset-database-parameters'), help=u"""Resets database parameter values to their default or startup values. \n[Command Reference](resetDatabaseParameters)""")
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


@managed_database_group.command(name=cli_util.override('database_management.summarize_awr_db_cpu_usages.command_name', 'summarize-awr-db-cpu-usages'), help=u"""Summarizes the AWR CPU resource limits and metrics for the specified database in AWR. \n[Command Reference](summarizeAwrDbCpuUsages)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--awr-db-id', required=True, help=u"""The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs:""")
@cli_util.option('--inst-num', help=u"""The optional single value query parameter to filter the database instance number.""")
@cli_util.option('--begin-sn-id-greater-than-or-equal-to', type=click.INT, help=u"""The optional greater than or equal to filter on the snapshot ID.""")
@cli_util.option('--end-sn-id-less-than-or-equal-to', type=click.INT, help=u"""The optional less than or equal to query parameter to filter the snapshot ID.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--session-type', type=custom_types.CliCaseInsensitiveChoice(["FOREGROUND", "BACKGROUND", "ALL"]), help=u"""The optional query parameter to filter ASH activities by FOREGROUND or BACKGROUND.""")
@cli_util.option('--container-id', type=click.INT, help=u"""The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges""")
@cli_util.option('--page', help=u"""The page token representing the page, from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in large paginated response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_SAMPLED", "AVG_VALUE"]), help=u"""The option to sort the AWR CPU usage summary data.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the the default order.""")
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


@managed_database_group.command(name=cli_util.override('database_management.summarize_awr_db_metrics.command_name', 'summarize-awr-db-metrics'), help=u"""Summarizes the metric samples for the specified database in the AWR. The metric samples are summarized based on the Time dimension for each metric. \n[Command Reference](summarizeAwrDbMetrics)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--awr-db-id', required=True, help=u"""The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs:""")
@cli_util.option('--name', required=True, multiple=True, help=u"""The required multiple value query parameter to filter the entity name.""")
@cli_util.option('--inst-num', help=u"""The optional single value query parameter to filter the database instance number.""")
@cli_util.option('--begin-sn-id-greater-than-or-equal-to', type=click.INT, help=u"""The optional greater than or equal to filter on the snapshot ID.""")
@cli_util.option('--end-sn-id-less-than-or-equal-to', type=click.INT, help=u"""The optional less than or equal to query parameter to filter the snapshot ID.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--container-id', type=click.INT, help=u"""The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges""")
@cli_util.option('--page', help=u"""The page token representing the page, from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in large paginated response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMESTAMP", "NAME"]), help=u"""The option to sort the AWR time series summary data.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the the default order.""")
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


@managed_database_group.command(name=cli_util.override('database_management.summarize_awr_db_parameter_changes.command_name', 'summarize-awr-db-parameter-changes'), help=u"""Summarizes the AWR database parameter change history for one database parameter of the specified Managed Database. One change history record contains the previous value, the changed value, and the corresponding time range. If the database parameter value was changed multiple times within the time range, then multiple change history records are created for the same parameter. Note that this API only returns information on change history details for one database parameter. To get a list of all the database parameters whose values were changed during a specified time range, use the following API endpoint: /managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbParameters \n[Command Reference](summarizeAwrDbParameterChanges)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--awr-db-id', required=True, help=u"""The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs:""")
@cli_util.option('--name', required=True, help=u"""The required single value query parameter to filter the entity name.""")
@cli_util.option('--inst-num', help=u"""The optional single value query parameter to filter the database instance number.""")
@cli_util.option('--begin-sn-id-greater-than-or-equal-to', type=click.INT, help=u"""The optional greater than or equal to filter on the snapshot ID.""")
@cli_util.option('--end-sn-id-less-than-or-equal-to', type=click.INT, help=u"""The optional less than or equal to query parameter to filter the snapshot ID.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--container-id', type=click.INT, help=u"""The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges""")
@cli_util.option('--page', help=u"""The page token representing the page, from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in large paginated response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["IS_CHANGED", "NAME"]), help=u"""The option to sort the AWR database parameter change history data.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the the default order.""")
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


@managed_database_group.command(name=cli_util.override('database_management.summarize_awr_db_parameters.command_name', 'summarize-awr-db-parameters'), help=u"""Summarizes the AWR database parameter history for the specified Managed Database. This includes the list of database parameters, with information on whether the parameter values were modified within the query time range. Note that each database parameter is only listed once. The returned summary gets all the database parameters, which include:  -Each parameter whose value was changed during the time range: AwrDbParameterValueOptionalQueryParam (valueChanged =\"Y\")  -Each parameter whose value was unchanged during the time range: AwrDbParameterValueOptionalQueryParam (valueChanged =\"N\")  -Each parameter whose value was changed at the system level during the time range: (valueChanged =\"Y\"  and valueModified = \"SYSTEM_MOD\").  -Each parameter whose value was unchanged during the time range, however, the value is not the default value: (valueChanged =\"N\" and  valueDefault = \"FALSE\") Note that this API does not return information on the number of times each database parameter has been changed within the time range. To get the database parameter value change history for a specific parameter, use the following API endpoint: /managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbParameterChanges \n[Command Reference](summarizeAwrDbParameters)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--awr-db-id', required=True, help=u"""The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs:""")
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
@cli_util.option('--page', help=u"""The page token representing the page, from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in large paginated response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["IS_CHANGED", "NAME"]), help=u"""The option to sort the AWR database parameter change history data.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the the default order.""")
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


@managed_database_group.command(name=cli_util.override('database_management.summarize_awr_db_snapshot_ranges.command_name', 'summarize-awr-db-snapshot-ranges'), help=u"""Summarizes the AWR snapshot ranges that contain continuous snapshots, for the specified Managed Database. \n[Command Reference](summarizeAwrDbSnapshotRanges)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--name', help=u"""The optional single value query parameter to filter the entity name.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--page', help=u"""The page token representing the page, from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in paginated response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["END_INTERVAL_TIME", "NAME"]), help=u"""The option to sort the AWR summary data.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the the default order.""")
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


@managed_database_group.command(name=cli_util.override('database_management.summarize_awr_db_sysstats.command_name', 'summarize-awr-db-sysstats'), help=u"""Summarizes the AWR SYSSTAT sample data for the specified database in AWR. The statistical data is summarized based on the Time dimension for each statistic. \n[Command Reference](summarizeAwrDbSysstats)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--awr-db-id', required=True, help=u"""The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs:""")
@cli_util.option('--name', required=True, multiple=True, help=u"""The required multiple value query parameter to filter the entity name.""")
@cli_util.option('--inst-num', help=u"""The optional single value query parameter to filter the database instance number.""")
@cli_util.option('--begin-sn-id-greater-than-or-equal-to', type=click.INT, help=u"""The optional greater than or equal to filter on the snapshot ID.""")
@cli_util.option('--end-sn-id-less-than-or-equal-to', type=click.INT, help=u"""The optional less than or equal to query parameter to filter the snapshot ID.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--container-id', type=click.INT, help=u"""The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges""")
@cli_util.option('--page', help=u"""The page token representing the page, from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in large paginated response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_BEGIN", "NAME"]), help=u"""The option to sort the data within a time period.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the the default order.""")
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


@managed_database_group.command(name=cli_util.override('database_management.summarize_awr_db_top_wait_events.command_name', 'summarize-awr-db-top-wait-events'), help=u"""Summarizes the AWR top wait events. \n[Command Reference](summarizeAwrDbTopWaitEvents)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--awr-db-id', required=True, help=u"""The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs:""")
@cli_util.option('--inst-num', help=u"""The optional single value query parameter to filter the database instance number.""")
@cli_util.option('--begin-sn-id-greater-than-or-equal-to', type=click.INT, help=u"""The optional greater than or equal to filter on the snapshot ID.""")
@cli_util.option('--end-sn-id-less-than-or-equal-to', type=click.INT, help=u"""The optional less than or equal to query parameter to filter the snapshot ID.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--session-type', type=custom_types.CliCaseInsensitiveChoice(["FOREGROUND", "BACKGROUND", "ALL"]), help=u"""The optional query parameter to filter ASH activities by FOREGROUND or BACKGROUND.""")
@cli_util.option('--container-id', type=click.INT, help=u"""The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges""")
@cli_util.option('--top-n', type=click.INT, help=u"""The optional query parameter to filter the number of top categories to be returned.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["WAITS_PERSEC", "AVG_WAIT_TIME_PERSEC"]), help=u"""The option to sort the AWR top event summary data.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the the default order.""")
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


@managed_database_group.command(name=cli_util.override('database_management.summarize_awr_db_wait_event_buckets.command_name', 'summarize-awr-db-wait-event-buckets'), help=u"""Summarizes AWR wait event data into value buckets and frequency, for the specified database in the AWR. \n[Command Reference](summarizeAwrDbWaitEventBuckets)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--awr-db-id', required=True, help=u"""The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs:""")
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
@cli_util.option('--page', help=u"""The page token representing the page, from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in large paginated response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["CATEGORY", "PERCENTAGE"]), help=u"""The option to sort distribution data.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the the default order.""")
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


@managed_database_group.command(name=cli_util.override('database_management.summarize_awr_db_wait_events.command_name', 'summarize-awr-db-wait-events'), help=u"""Summarizes the AWR wait event sample data for the specified database in the AWR. The event data is summarized based on the Time dimension for each event. \n[Command Reference](summarizeAwrDbWaitEvents)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--awr-db-id', required=True, help=u"""The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs:""")
@cli_util.option('--inst-num', help=u"""The optional single value query parameter to filter the database instance number.""")
@cli_util.option('--begin-sn-id-greater-than-or-equal-to', type=click.INT, help=u"""The optional greater than or equal to filter on the snapshot ID.""")
@cli_util.option('--end-sn-id-less-than-or-equal-to', type=click.INT, help=u"""The optional less than or equal to query parameter to filter the snapshot ID.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to query parameter to filter the timestamp.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--name', multiple=True, help=u"""The optional multiple value query parameter to filter the entity name.""")
@cli_util.option('--session-type', type=custom_types.CliCaseInsensitiveChoice(["FOREGROUND", "BACKGROUND", "ALL"]), help=u"""The optional query parameter to filter ASH activities by FOREGROUND or BACKGROUND.""")
@cli_util.option('--container-id', type=click.INT, help=u"""The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges""")
@cli_util.option('--page', help=u"""The page token representing the page, from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in large paginated response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_BEGIN", "NAME"]), help=u"""The option to sort the data within a time period.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the the default order.""")
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


@managed_database_group_group.command(name=cli_util.override('database_management.update_managed_database_group.command_name', 'update'), help=u"""Updates the Managed Database Group specified by managedDatabaseGroupId. \n[Command Reference](updateManagedDatabaseGroup)""")
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
