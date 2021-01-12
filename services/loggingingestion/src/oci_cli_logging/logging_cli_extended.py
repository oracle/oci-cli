# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


import click

from services.loggingingestion.src.oci_cli_logging.generated import logging_cli
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types

# Override the name of the service for top-level index
logging_cli.logging_ingestion_root_group.short_help = "Logging Ingestion"

# oci logging-ingestion log-entry put-logs -> oci logging-ingestion put-logs
logging_cli.logging_ingestion_root_group.commands.pop(logging_cli.log_entry_group.name)
logging_cli.logging_ingestion_root_group.add_command(logging_cli.put_logs)


# Shorten parameters longer than 25 chars: --timestamp-opc-agent-processing to --agent-timestamp
# from
#   oci loggingingestion put-logs ... --timestamp-opc-agent-processing ...
# to
#   oci loggingingestion put-logs ... --agent-timestamp ...
@cli_util.copy_params_from_generated_command(logging_cli.put_logs, params_to_exclude=['timestamp_opc_agent_processing'])
@cli_util.option('--agent-timestamp', type=custom_types.CLI_DATETIME, help=u"""Effective timestamp, for when the agent started processing the log segment being sent. An RFC3339 formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@logging_cli.logging_ingestion_root_group.command(name=cli_util.override('logging.put_logs.command_name', 'put-logs'), help=logging_cli.put_logs.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'log-entry-batches': {'module': 'loggingingestion', 'class': 'list[LogEntryBatch]'}})
@cli_util.wrap_exceptions
def put_logs_extended(ctx, **kwargs):
    if 'agent_timestamp' in kwargs:
        kwargs['timestamp_opc_agent_processing'] = kwargs['agent_timestamp']
        kwargs.pop('agent_timestamp')
    ctx.invoke(logging_cli.put_logs, **kwargs)
