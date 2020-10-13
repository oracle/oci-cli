# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
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


@cli.command(cli_util.override('logging_ingestion.logging_ingestion_root_group.command_name', 'logging-ingestion'), cls=CommandGroupWithAlias, help=cli_util.override('logging_ingestion.logging_ingestion_root_group.help', """Use the Logging Ingestion API to ingest your application logs."""), short_help=cli_util.override('logging_ingestion.logging_ingestion_root_group.short_help', """Logging Ingestion API"""))
@cli_util.help_option_group
def logging_ingestion_root_group():
    pass


@click.command(cli_util.override('logging_ingestion.log_entry_group.command_name', 'log-entry'), cls=CommandGroupWithAlias, help="""Contains the log content with the associated timestamp and ID. Each entry should be less than 1 MB size.""")
@cli_util.help_option_group
def log_entry_group():
    pass


logging_ingestion_root_group.add_command(log_entry_group)


@log_entry_group.command(name=cli_util.override('logging_ingestion.put_logs.command_name', 'put-logs'), help=u"""This API allows ingesting logs associated with a logId. A success response implies the data has been accepted. \n[Command Reference](putLogs)""")
@cli_util.option('--log-id', required=True, help=u"""OCID of a log to work with.""")
@cli_util.option('--specversion', required=True, help=u"""Required for identifying the version of the data format being used. Permitted values include: \"1.0\"""")
@cli_util.option('--log-entry-batches', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of log-batches. Each batch has a single source, type and subject.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--timestamp-opc-agent-processing', type=custom_types.CLI_DATETIME, help=u"""Effective timestamp, for when the agent started processing the log segment being sent. An RFC3339-formatted date-time string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--opc-agent-version', help=u"""Version of the agent sending the request.""")
@json_skeleton_utils.get_cli_json_input_option({'log-entry-batches': {'module': 'loggingingestion', 'class': 'list[LogEntryBatch]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'log-entry-batches': {'module': 'loggingingestion', 'class': 'list[LogEntryBatch]'}})
@cli_util.wrap_exceptions
def put_logs(ctx, from_json, log_id, specversion, log_entry_batches, timestamp_opc_agent_processing, opc_agent_version):

    if isinstance(log_id, six.string_types) and len(log_id.strip()) == 0:
        raise click.UsageError('Parameter --log-id cannot be whitespace or empty string')

    kwargs = {}
    if timestamp_opc_agent_processing is not None:
        kwargs['timestamp_opc_agent_processing'] = timestamp_opc_agent_processing
    if opc_agent_version is not None:
        kwargs['opc_agent_version'] = opc_agent_version
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['specversion'] = specversion
    _details['logEntryBatches'] = cli_util.parse_json_parameter("log_entry_batches", log_entry_batches)

    client = cli_util.build_client('loggingingestion', 'logging', ctx)
    result = client.put_logs(
        log_id=log_id,
        put_logs_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
