# coding: utf-8
# Copyright (c) 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci_cli import cli_util
from services.compute_cloud_at_customer.src.oci_cli_compute_cloud_at_customer.generated \
    import computecloudatcustomer_cli
from oci_cli import json_skeleton_utils
import click


# Update the intermediate commands to remove the prefix ccc- (duplicated information)
cli_util.rename_command(computecloudatcustomer_cli, computecloudatcustomer_cli.ccc_root_group,
                        computecloudatcustomer_cli.ccc_infrastructure_group, "infrastructure")
cli_util.rename_command(computecloudatcustomer_cli, computecloudatcustomer_cli.ccc_root_group,
                        computecloudatcustomer_cli.ccc_upgrade_schedule_group, "upgrade-schedule")

# Update sub-commands to remove redundant 'ccc', these have to come before the moves
cli_util.rename_command(computecloudatcustomer_cli, computecloudatcustomer_cli.ccc_infrastructure_collection_group,
                        computecloudatcustomer_cli.list_ccc_infrastructures, "list")
cli_util.rename_command(computecloudatcustomer_cli, computecloudatcustomer_cli.ccc_upgrade_schedule_collection_group,
                        computecloudatcustomer_cli.list_ccc_upgrade_schedules, "list")

# Move the -collection commands over to the simple roots (upgrade-schedule and infrastructure)
computecloudatcustomer_cli.ccc_root_group.commands.pop(
    computecloudatcustomer_cli.ccc_upgrade_schedule_collection_group.name)
computecloudatcustomer_cli.ccc_root_group.commands.pop(
    computecloudatcustomer_cli.ccc_infrastructure_collection_group.name)
computecloudatcustomer_cli.ccc_upgrade_schedule_group.add_command(computecloudatcustomer_cli.list_ccc_upgrade_schedules)
computecloudatcustomer_cli.ccc_infrastructure_group.add_command(computecloudatcustomer_cli.list_ccc_infrastructures)


# Update the parameters to remove the prefix ccc- (duplicated information)
@cli_util.copy_params_from_generated_command(computecloudatcustomer_cli.create_ccc_infrastructure,
                                             params_to_exclude=['ccc_upgrade_schedule_id'])
@computecloudatcustomer_cli.ccc_infrastructure_group.command(
    name=cli_util.override('create_ccc_infrastructure.command_name', 'create'),
    help="""Creates a Compute Cloud@Customer infrastructure. Once created, Oracle Services must connect the rack in the data center to this Oracle Cloud Infrastructure resource.""")
@cli_util.option('--upgrade-schedule-id', required=False,
                 help=u"""Schedule used for upgrades. If no schedule is associated with the infrastructure, it can be updated at any time.""")
@json_skeleton_utils.get_cli_json_input_option({})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'compute_cloud_at_customer', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'compute_cloud_at_customer', 'class': 'dict(str, string)'}})
@cli_util.wrap_exceptions
def create_ccc_infrastructure(ctx, **kwargs):
    if 'upgrade_schedule_id' in kwargs:
        kwargs['ccc_upgrade_schedule_id'] = kwargs['upgrade_schedule_id']
        kwargs.pop('upgrade_schedule_id')
    ctx.invoke(computecloudatcustomer_cli.create_ccc_infrastructure, **kwargs)


@cli_util.copy_params_from_generated_command(computecloudatcustomer_cli.update_ccc_infrastructure,
                                             params_to_exclude=['ccc_infrastructure_id',
                                                                'ccc_upgrade_schedule_id'])
@computecloudatcustomer_cli.ccc_infrastructure_group.command(
    name=cli_util.override('update_ccc_infrastructure.command_name', 'update'),
    help="""Updates Compute Cloud@Customer infrastructure resource.""")
@cli_util.option('--infrastructure-id', required=True,
                 help=u"""An OCID for a Compute Cloud@Customer Infrastructure.""")
@cli_util.option('--upgrade-schedule-id', required=False,
                 help=u"""Schedule used for upgrades. If no schedule is associated with the infrastructure, it can be updated at any time.""")
@json_skeleton_utils.get_cli_json_input_option({})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'compute_cloud_at_customer', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'compute_cloud_at_customer', 'class': 'dict(str, string)'}})
@cli_util.wrap_exceptions
def update_ccc_infrastructure(ctx, **kwargs):
    if 'infrastructure_id' in kwargs:
        kwargs['ccc_infrastructure_id'] = kwargs['infrastructure_id']
        kwargs.pop('infrastructure_id')
    if 'upgrade_schedule_id' in kwargs:
        kwargs['ccc_upgrade_schedule_id'] = kwargs['upgrade_schedule_id']
        kwargs.pop('upgrade_schedule_id')
    ctx.invoke(computecloudatcustomer_cli.update_ccc_infrastructure, **kwargs)


@cli_util.copy_params_from_generated_command(computecloudatcustomer_cli.get_ccc_infrastructure,
                                             params_to_exclude=['ccc_infrastructure_id'])
@computecloudatcustomer_cli.ccc_infrastructure_group.command(
    name=cli_util.override('get_ccc_infrastructure.command_name', 'get'),
    help="""Gets a Compute Cloud@Customer infrastructure.""")
@cli_util.option('--infrastructure-id', required=True,
                 help=u"""An OCID for a Compute Cloud@Customer Infrastructure.""")
@json_skeleton_utils.get_cli_json_input_option({})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_ccc_infrastructure(ctx, **kwargs):
    if 'infrastructure_id' in kwargs:
        kwargs['ccc_infrastructure_id'] = kwargs['infrastructure_id']
        kwargs.pop('infrastructure_id')
    ctx.invoke(computecloudatcustomer_cli.get_ccc_infrastructure, **kwargs)


@cli_util.copy_params_from_generated_command(computecloudatcustomer_cli.delete_ccc_infrastructure,
                                             params_to_exclude=['ccc_infrastructure_id'])
@computecloudatcustomer_cli.ccc_infrastructure_group.command(
    name=cli_util.override('delete_ccc_infrastructure.command_name', 'delete'),
    help="""Deletes a Compute Cloud@Customer infrastructure resource specified by the resource OCID.""")
@cli_util.option('--infrastructure-id', required=True,
                 help=u"""An OCID for a Compute Cloud@Customer Infrastructure.""")
@json_skeleton_utils.get_cli_json_input_option({})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_ccc_infrastructure(ctx, **kwargs):
    if 'infrastructure_id' in kwargs:
        kwargs['ccc_infrastructure_id'] = kwargs['infrastructure_id']
        kwargs.pop('infrastructure_id')
    ctx.invoke(computecloudatcustomer_cli.delete_ccc_infrastructure, **kwargs)


@cli_util.copy_params_from_generated_command(computecloudatcustomer_cli.change_ccc_infrastructure_compartment,
                                             params_to_exclude=['ccc_infrastructure_id'])
@computecloudatcustomer_cli.ccc_infrastructure_group.command(
    name=cli_util.override('change_ccc_infrastructure_compartment.command_name', 'change-compartment'),
    help="""Moves a Compute Cloud@Customer infrastructure resource from one compartment to another.""")
@cli_util.option('--infrastructure-id', required=True,
                 help=u"""An OCID for a Compute Cloud@Customer Infrastructure.""")
@json_skeleton_utils.get_cli_json_input_option({})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_ccc_infrastructure_compartment(ctx, **kwargs):
    if 'infrastructure_id' in kwargs:
        kwargs['ccc_infrastructure_id'] = kwargs['infrastructure_id']
        kwargs.pop('infrastructure_id')
    ctx.invoke(computecloudatcustomer_cli.change_ccc_infrastructure_compartment, **kwargs)


@cli_util.copy_params_from_generated_command(computecloudatcustomer_cli.list_ccc_infrastructures,
                                             params_to_exclude=['ccc_infrastructure_id'])
@computecloudatcustomer_cli.ccc_infrastructure_group.command(
    name=cli_util.override('list_ccc_infrastructure.command_name', 'list'),
    help="""Returns a list of Compute Cloud@Customer infrastructures.""")
@cli_util.option('--infrastructure-id', required=False,
                 help=u"""An OCID for a Compute Cloud@Customer Infrastructure.""")
@json_skeleton_utils.get_cli_json_input_option({})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'compute_cloud_at_customer', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'compute_cloud_at_customer', 'class': 'dict(str, string)'}})
@cli_util.wrap_exceptions
def list_ccc_infrastructure(ctx, **kwargs):
    if 'infrastructure_id' in kwargs:
        kwargs['ccc_infrastructure_id'] = kwargs['infrastructure_id']
        kwargs.pop('infrastructure_id')
    ctx.invoke(computecloudatcustomer_cli.list_ccc_infrastructures, **kwargs)


# Update the parameters to remove the prefix ccc- (duplicated information)
@cli_util.copy_params_from_generated_command(computecloudatcustomer_cli.update_ccc_upgrade_schedule,
                                             params_to_exclude=['ccc_upgrade_schedule_id'])
@computecloudatcustomer_cli.ccc_upgrade_schedule_group.command(
    name=cli_util.override('update_ccc_upgrade_schedule.command_name', 'update'),
    help="""Updates the Compute Cloud@Customer upgrade schedule.""")
@cli_util.option('--upgrade-schedule-id', required=True,
                 help=u"""Compute Cloud@Customer upgrade schedule OCID.""")
@json_skeleton_utils.get_cli_json_input_option({})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler({'events': {'module': 'compute_cloud_at_customer', 'class': 'list[CreateCccScheduleEvent]'}, 'freeform-tags': {'module': 'compute_cloud_at_customer', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'compute_cloud_at_customer', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_ccc_upgrade_schedule(ctx, **kwargs):
    if 'upgrade_schedule_id' in kwargs:
        kwargs['ccc_upgrade_schedule_id'] = kwargs['upgrade_schedule_id']
        kwargs.pop('upgrade_schedule_id')
    ctx.invoke(computecloudatcustomer_cli.update_ccc_upgrade_schedule, **kwargs)


@cli_util.copy_params_from_generated_command(computecloudatcustomer_cli.get_ccc_upgrade_schedule,
                                             params_to_exclude=['ccc_upgrade_schedule_id'])
@computecloudatcustomer_cli.ccc_upgrade_schedule_group.command(
    name=cli_util.override('get_ccc_upgrade_schedule.command_name', 'get'),
    help="""Gets a Compute Cloud@Customer upgrade schedule by the specified OCID.""")
@cli_util.option('--upgrade-schedule-id', required=True,
                 help=u"""Compute Cloud@Customer upgrade schedule OCID.""")
@json_skeleton_utils.get_cli_json_input_option({})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_ccc_upgrade_schedule(ctx, **kwargs):
    if 'upgrade_schedule_id' in kwargs:
        kwargs['ccc_upgrade_schedule_id'] = kwargs['upgrade_schedule_id']
        kwargs.pop('upgrade_schedule_id')
    ctx.invoke(computecloudatcustomer_cli.get_ccc_upgrade_schedule, **kwargs)


@cli_util.copy_params_from_generated_command(computecloudatcustomer_cli.list_ccc_upgrade_schedules,
                                             params_to_exclude=['ccc_upgrade_schedule_id'])
@computecloudatcustomer_cli.ccc_upgrade_schedule_group.command(
    name=cli_util.override('list_ccc_upgrade_schedules.command_name', 'list'),
    help="""Returns a list of Compute Cloud@Customer upgrade schedules.""")
@cli_util.option('--upgrade-schedule-id', required=False,
                 help=u"""Compute Cloud@Customer upgrade schedule OCID.""")
@json_skeleton_utils.get_cli_json_input_option({})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def list_ccc_upgrade_schedule(ctx, **kwargs):
    if 'upgrade_schedule_id' in kwargs:
        kwargs['ccc_upgrade_schedule_id'] = kwargs['upgrade_schedule_id']
        kwargs.pop('upgrade_schedule_id')
    ctx.invoke(computecloudatcustomer_cli.list_ccc_upgrade_schedules, **kwargs)


@cli_util.copy_params_from_generated_command(computecloudatcustomer_cli.delete_ccc_upgrade_schedule,
                                             params_to_exclude=['ccc_upgrade_schedule_id'])
@computecloudatcustomer_cli.ccc_upgrade_schedule_group.command(
    name=cli_util.override('delete_ccc_upgrade_schedule.command_name', 'delete'),
    help="""Deletes a Compute Cloud@Customer upgrade schedule by the specified OCID""")
@cli_util.option('--upgrade-schedule-id', required=True,
                 help=u"""Compute Cloud@Customer upgrade schedule OCID.""")
@json_skeleton_utils.get_cli_json_input_option({})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_ccc_upgrade_schedule(ctx, **kwargs):
    if 'upgrade_schedule_id' in kwargs:
        kwargs['ccc_upgrade_schedule_id'] = kwargs['upgrade_schedule_id']
        kwargs.pop('upgrade_schedule_id')
    ctx.invoke(computecloudatcustomer_cli.delete_ccc_upgrade_schedule, **kwargs)


@cli_util.copy_params_from_generated_command(computecloudatcustomer_cli.change_ccc_upgrade_schedule_compartment,
                                             params_to_exclude=['ccc_upgrade_schedule_id'])
@computecloudatcustomer_cli.ccc_upgrade_schedule_group.command(
    name=cli_util.override('change_ccc_upgrade_schedule_compartment.command_name', 'change-compartment'),
    help="""Moves a Compute Cloud@Customer upgrade schedule from one compartment to another using the specified OCID.""")
@cli_util.option('--upgrade-schedule-id', required=True,
                 help=u"""Compute Cloud@Customer upgrade schedule OCID.""")
@json_skeleton_utils.get_cli_json_input_option({})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_ccc_upgrade_schedule_compartment(ctx, **kwargs):
    if 'upgrade_schedule_id' in kwargs:
        kwargs['ccc_upgrade_schedule_id'] = kwargs['upgrade_schedule_id']
        kwargs.pop('upgrade_schedule_id')
    ctx.invoke(computecloudatcustomer_cli.change_ccc_upgrade_schedule_compartment, **kwargs)
