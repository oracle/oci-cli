# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.ocvp.src.oci_cli_byol_allocation.generated import byolallocation_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci ocvs byol-allocation byol-allocation-summary list-byol-allocations -> oci ocvs byol-allocation byol-allocation-summary list
cli_util.rename_command(byolallocation_cli, byolallocation_cli.byol_allocation_summary_group, byolallocation_cli.list_byol_allocations, "list")


# Move commands under 'oci ocvs byol-allocation byol-allocation' -> 'oci ocvs byol-allocation'
byolallocation_cli.byol_allocation_root_group.commands.pop(byolallocation_cli.byol_allocation_group.name)
byolallocation_cli.byol_allocation_root_group.add_command(byolallocation_cli.change_byol_allocation_compartment)
byolallocation_cli.byol_allocation_root_group.add_command(byolallocation_cli.create_byol_allocation)
byolallocation_cli.byol_allocation_root_group.add_command(byolallocation_cli.delete_byol_allocation)
byolallocation_cli.byol_allocation_root_group.add_command(byolallocation_cli.get_byol_allocation)
byolallocation_cli.byol_allocation_root_group.add_command(byolallocation_cli.update_byol_allocation)


# Move commands under 'oci ocvs byol-allocation byol-allocation-summary' -> 'oci ocvs byol-allocation'
byolallocation_cli.byol_allocation_root_group.commands.pop(byolallocation_cli.byol_allocation_summary_group.name)
byolallocation_cli.byol_allocation_root_group.add_command(byolallocation_cli.list_byol_allocations)


@cli_util.copy_params_from_generated_command(byolallocation_cli.list_byol_allocations, params_to_exclude=['available_units_greater_than_or_equal_to'])
@byolallocation_cli.byol_allocation_summary_group.command(name=byolallocation_cli.list_byol_allocations.name, help=byolallocation_cli.list_byol_allocations.help)
@cli_util.option('--available-units-gte', type=click.FLOAT, help=u"""A filter to return only resources whose availableUnits greater than or equal to the given value.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ocvp', 'class': 'ByolAllocationCollection'})
@cli_util.wrap_exceptions
def list_byol_allocations_extended(ctx, **kwargs):

    if 'available_units_gte' in kwargs:
        kwargs['available_units_greater_than_or_equal_to'] = kwargs['available_units_gte']
        kwargs.pop('available_units_gte')

    ctx.invoke(byolallocation_cli.list_byol_allocations, **kwargs)
