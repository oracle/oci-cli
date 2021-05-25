# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
import six
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
