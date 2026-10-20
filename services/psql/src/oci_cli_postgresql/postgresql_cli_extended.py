# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click
from oci_cli import cli_util
from oci_cli import custom_types
from oci_cli import json_skeleton_utils
from services.psql.src.oci_cli_postgresql.generated import postgresql_cli

# DEX-25968: the generated enum-array option is missing multiple=True.


@cli_util.copy_params_from_generated_command(postgresql_cli.upgrade_db_system, params_to_exclude=['options'])
@postgresql_cli.db_system_group.command(name='upgrade', help=postgresql_cli.upgrade_db_system.help)
@cli_util.option('--options', multiple=True, type=custom_types.CliCaseInsensitiveChoice(["RUN_POST_UPGRADE_VERIFICATION", "RUN_POST_UPGRADE_VACUUM"]), help=u"""Optional post-upgrade operations to run. Verification and vacuum are skipped unless their corresponding options are included. If omitted or empty, both operations are skipped.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def upgrade_db_system_extended(ctx, **kwargs):
    ctx.invoke(postgresql_cli.upgrade_db_system, **kwargs)
