# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from ..generated import audit_cli
from .. import cli_util
from .. import custom_types
from .. import json_skeleton_utils

import click

audit_cli.configuration_group.commands.pop(audit_cli.update_configuration.name)

cli_util.get_param(audit_cli.list_events, 'start_time').type = custom_types.CLI_DATETIME_ROUNDED_MINUTE
cli_util.get_param(audit_cli.list_events, 'end_time').type = custom_types.CLI_DATETIME_ROUNDED_MINUTE

audit_start_time_help = """Returns events that were processed at or after this start date and time. For example, a start value of `2017-01-15T11:30:00Z` will retrieve a list of all events processed since 30 minutes after the 11th hour of January 15, 2017, in Coordinated Universal Time (UTC).
You can specify a value with granularity to the minute. If seconds are provided then this will be rounded to the nearest minute, with greater than or equal to 30 seconds rounding up and less than 30 seconds rounding down.
""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE
cli_util.update_param_help(audit_cli.list_events, 'start_time', audit_start_time_help, append=False)
audit_end_time_help = """Returns events that were processed before this end date and time. For example, a start value of `2017-01-01T00:00:00Z` and an end value of `2017-01-02T00:00:00Z` will retrieve a list of all events processed on January 1, 2017. Similarly, a start value of `2017-01-01T00:00:00Z` and an end value of `2017-02-01T00:00:00Z` will result in a list of all events processed between January 1, 2017 and January 31, 2017.
You can specify a value with granularity to the minute. If seconds are provided then this will be rounded to the nearest minute, with greater than or equal to 30 seconds rounding up and less than 30 seconds rounding down.
""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE
cli_util.update_param_help(audit_cli.list_events, 'end_time', audit_end_time_help, append=False)


@cli_util.copy_params_from_generated_command(audit_cli.update_configuration, params_to_exclude=['wait_for_state', 'max_wait_seconds', 'wait_interval_seconds'])
@audit_cli.configuration_group.command(name=cli_util.override('update_configuration.command_name', 'update'), help="""Update the configuration""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'PrivateIp'})
@cli_util.wrap_exceptions
def update_configuration(ctx, **kwargs):
    ctx.invoke(audit_cli.update_configuration, **kwargs)
