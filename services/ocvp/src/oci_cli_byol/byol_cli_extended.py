# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.ocvp.src.oci_cli_byol.generated import byol_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci ocvs byol byol-summary list-byols -> oci ocvs byol byol-summary list
cli_util.rename_command(byol_cli, byol_cli.byol_summary_group, byol_cli.list_byols, "list")


# Move commands under 'oci ocvs byol byol' -> 'oci ocvs byol'
byol_cli.byol_root_group.commands.pop(byol_cli.byol_group.name)
byol_cli.byol_root_group.add_command(byol_cli.change_byol_compartment)
byol_cli.byol_root_group.add_command(byol_cli.create_byol)
byol_cli.byol_root_group.add_command(byol_cli.delete_byol)
byol_cli.byol_root_group.add_command(byol_cli.get_byol)
byol_cli.byol_root_group.add_command(byol_cli.retrieve_byol_realm_allocations)
byol_cli.byol_root_group.add_command(byol_cli.update_byol)


# Move commands under 'oci ocvs byol byol-summary' -> 'oci ocvs byol'
byol_cli.byol_root_group.commands.pop(byol_cli.byol_summary_group.name)
byol_cli.byol_root_group.add_command(byol_cli.list_byols)


@cli_util.copy_params_from_generated_command(byol_cli.list_byols, params_to_exclude=['available_units_greater_than_or_equal_to'])
@byol_cli.byol_summary_group.command(name=byol_cli.list_byols.name, help=byol_cli.list_byols.help)
@cli_util.option('--available-units-gte', type=click.FLOAT, help=u"""A filter to return only resources whose availableUnits greater than or equal to the given value.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ocvp', 'class': 'ByolCollection'})
@cli_util.wrap_exceptions
def list_byols_extended(ctx, **kwargs):

    if 'available_units_gte' in kwargs:
        kwargs['available_units_greater_than_or_equal_to'] = kwargs['available_units_gte']
        kwargs.pop('available_units_gte')

    ctx.invoke(byol_cli.list_byols, **kwargs)
