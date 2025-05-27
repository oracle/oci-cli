# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.capacity_management.src.oci_cli_demand_signal.generated import demandsignal_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


@cli_util.copy_params_from_generated_command(demandsignal_cli.create_occm_demand_signal_item, params_to_exclude=['region_parameterconflict'])
@demandsignal_cli.occm_demand_signal_item_group.command(name=demandsignal_cli.create_occm_demand_signal_item.name, help=demandsignal_cli.create_occm_demand_signal_item.help)
@cli_util.option('--target-region', required=True, help=u"""The name of region for which you want to request the OCI resource. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'resource-properties': {'module': 'capacity_management', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'capacity_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'capacity_management', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'capacity_management', 'class': 'OccmDemandSignalItem'})
@cli_util.wrap_exceptions
def create_occm_demand_signal_item_extended(ctx, **kwargs):

    if 'target_region' in kwargs:
        kwargs['region_parameterconflict'] = kwargs['target_region']
        kwargs.pop('target_region')

    ctx.invoke(demandsignal_cli.create_occm_demand_signal_item, **kwargs)


@cli_util.copy_params_from_generated_command(demandsignal_cli.update_occm_demand_signal_item, params_to_exclude=['region_parameterconflict'])
@demandsignal_cli.occm_demand_signal_item_group.command(name=demandsignal_cli.update_occm_demand_signal_item.name, help=demandsignal_cli.update_occm_demand_signal_item.help)
@cli_util.option('--target-region', help=u"""The region for which you want to request the resource for.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'resource-properties': {'module': 'capacity_management', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'capacity_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'capacity_management', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'capacity_management', 'class': 'OccmDemandSignalItem'})
@cli_util.wrap_exceptions
def update_occm_demand_signal_item_extended(ctx, **kwargs):

    if 'target_region' in kwargs:
        kwargs['region_parameterconflict'] = kwargs['target_region']
        kwargs.pop('target_region')

    ctx.invoke(demandsignal_cli.update_occm_demand_signal_item, **kwargs)
