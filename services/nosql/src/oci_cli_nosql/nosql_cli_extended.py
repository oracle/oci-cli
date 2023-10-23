# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli.aliasing import CommandGroupWithAlias
from services.nosql.src.oci_cli_nosql.generated import nosql_cli

# Override the name of the service for top-level index
nosql_cli.nosql_root_group.short_help = "NoSQL Database"

# Override help for the table group
cli_util.override_command_short_help_and_help(nosql_cli.table_group, "NoSQL tables")

# Override help for query group
cli_util.override_command_short_help_and_help(nosql_cli.query_result_collection_group, "Queries on table contents")

# oci nosql query-result-collection ... -> oci nosql query ...
# oci nosql query prepare-statement -> oci nosql query prepare
cli_util.rename_command(nosql_cli, nosql_cli.nosql_root_group, nosql_cli.query_result_collection_group, "query")
cli_util.rename_command(nosql_cli, nosql_cli.query_result_collection_group, nosql_cli.prepare_statement, "prepare")

# oci nosql query-result-collection summarize-statement -> removed
nosql_cli.query_result_collection_group.commands.pop("summarize-statement")
nosql_cli.query_result_collection_group.commands.pop("query")

# Override help for workrequest group
cli_util.override_command_short_help_and_help(nosql_cli.work_request_group, "Monitoring of async operations")


# oci nosql work-request list-work-request-errors -> oci nosql work-request-error list
@click.command('work-request-error', cls=CommandGroupWithAlias, help="""Error messages associated with a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


nosql_cli.nosql_root_group.add_command(work_request_error_group)
work_request_error_group.add_command(nosql_cli.list_work_request_errors)
nosql_cli.work_request_group.commands.pop(nosql_cli.list_work_request_errors.name)
cli_util.rename_command(nosql_cli, work_request_error_group, nosql_cli.list_work_request_errors, "list")


# oci nosql work-request list-work-request-logs -> oci nosql work-request-log list
@click.command('work-request-log', cls=CommandGroupWithAlias, help="""Log messages associated with a work request.""")
@cli_util.help_option_group
def work_request_log_group():
    pass


nosql_cli.nosql_root_group.add_command(work_request_log_group)
work_request_log_group.add_command(nosql_cli.list_work_request_logs)
nosql_cli.work_request_group.commands.pop(nosql_cli.list_work_request_logs.name)
cli_util.rename_command(nosql_cli, work_request_log_group, nosql_cli.list_work_request_logs, "list")


# Override help for query group
cli_util.override_command_short_help_and_help(nosql_cli.row_group, "Table rows")


# row update --is_ttl_use_table_default -> --ttl_use_default
@cli_util.copy_params_from_generated_command(nosql_cli.update_row, params_to_exclude=['is_ttl_use_table_default'])
@nosql_cli.row_group.command(name='update', help=nosql_cli.update_row.help)
@cli_util.option('--ttl-use-default', type=click.BOOL, help="""If true, set time-to-live for this row to the table's default.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'value': {'module': 'nosql', 'class': 'dict(str, object)'}}, output_type={'module': 'nosql', 'class': 'UpdateRowResult'})
@cli_util.wrap_exceptions
def update_row_extended(ctx, **kwargs):

    if 'ttl_use_default' in kwargs:
        kwargs['is_ttl_use_table_default'] = kwargs['ttl_use_default']

    del kwargs['ttl_use_default']

    ctx.invoke(nosql_cli.update_row, **kwargs)


# oci nosql query query -> oci nosql query execute
cli_util.rename_command(nosql_cli, nosql_cli.query_result_collection_group, nosql_cli.query, "execute")


# Override help for index group
cli_util.override_command_short_help_and_help(nosql_cli.index_group, "Secondary indexes on tables")


# create index --name -> create index --index-name
@cli_util.copy_params_from_generated_command(nosql_cli.create_index, params_to_exclude=['name'])
@nosql_cli.index_group.command(name='create', help=nosql_cli.create_index.help)
@cli_util.option('--index-name', required=True, help="""Index name.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'keys': {'module': 'nosql', 'class': 'list[IndexKey]'}})
@cli_util.wrap_exceptions
def create_index_extended(ctx, **kwargs):

    if 'index_name' in kwargs:
        kwargs['name'] = kwargs['index_name']

    del kwargs['index_name']

    ctx.invoke(nosql_cli.create_index, **kwargs)


@cli_util.copy_params_from_generated_command(nosql_cli.create_replica, params_to_exclude=['region_parameterconflict'])
@nosql_cli.table_group.command(name=nosql_cli.create_replica.name, help=nosql_cli.create_replica.help)
@cli_util.option('--replica-region', required=True, help=u"""Name of the remote region in standard OCI format, i.e. us-ashburn-1 [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def create_replica_extended(ctx, **kwargs):

    if 'replica_region' in kwargs:
        kwargs['region_parameterconflict'] = kwargs['replica_region']
        kwargs.pop('replica_region')

    ctx.invoke(nosql_cli.create_replica, **kwargs)


@cli_util.copy_params_from_generated_command(nosql_cli.delete_replica, params_to_exclude=['region_parameterconflict'])
@nosql_cli.table_group.command(name=nosql_cli.delete_replica.name, help=nosql_cli.delete_replica.help)
@cli_util.option('--replica-region', required=True, help=u"""A customer-facing region identifier [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_replica_extended(ctx, **kwargs):

    if 'replica_region' in kwargs:
        kwargs['region_parameterconflict'] = kwargs['replica_region']
        kwargs.pop('replica_region')

    ctx.invoke(nosql_cli.delete_replica, **kwargs)
