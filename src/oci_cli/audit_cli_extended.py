# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .generated import audit_cli
from . import cli_util
from . import json_skeleton_utils

import click

audit_cli.audit_group.add_command(audit_cli.audit_event_group)
audit_cli.audit_group.add_command(audit_cli.configuration_group)
audit_cli.configuration_group.commands.pop(audit_cli.update_configuration.name)


@cli_util.copy_params_from_generated_command(audit_cli.update_configuration, params_to_exclude=['wait_for_state', 'max_wait_seconds', 'wait_interval_seconds'])
@audit_cli.configuration_group.command(name=cli_util.override('update_configuration.command_name', 'update'), help="""Update the configuration""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'PrivateIp'})
@cli_util.wrap_exceptions
def update_configuration(ctx, **kwargs):
    ctx.invoke(audit_cli.update_configuration, **kwargs)
