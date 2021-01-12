# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci_cli import cli_util
from services.bds.src.oci_cli_bds.generated import bds_cli
from oci_cli import custom_types  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
import click
from oci_cli.aliasing import CommandGroupWithAlias


# oci bds work-request-log-entry list-work-request-logs -> oci bds work-request-log-entry list
cli_util.rename_command(bds_cli, bds_cli.work_request_log_entry_group, bds_cli.list_work_request_logs, 'list')


# oci bds bds-instance -> oci bds instance
cli_util.rename_command(bds_cli, bds_cli.bds_root_group, bds_cli.bds_instance_group, "instance")


# oci bds bds-instance add  -> oci bds instance worker-nodes add
@click.command('worker-nodes', cls=CommandGroupWithAlias, help=bds_cli.add_worker_nodes.help)
@cli_util.help_option_group
def bds_worker_nodes_group():
    pass


bds_cli.bds_instance_group.commands.pop(bds_cli.add_worker_nodes.name)
bds_cli.bds_instance_group.add_command(bds_worker_nodes_group)
bds_worker_nodes_group.add_command(bds_cli.add_worker_nodes)


# Add command: oci bds block-storage add
@click.command('block-storage', cls=CommandGroupWithAlias, help=bds_cli.add_block_storage.help)
@cli_util.help_option_group
def bds_block_storage_group():
    pass


bds_cli.bds_root_group.add_command(bds_block_storage_group)
bds_block_storage_group.add_command(bds_cli.add_block_storage)


# Add commands: oci bds cloudsql add | remove
@click.command('cloudsql', cls=CommandGroupWithAlias, help=bds_cli.add_cloud_sql.help)
@cli_util.help_option_group
def bds_cloud_sql_group():
    pass


bds_cli.bds_root_group.add_command(bds_cloud_sql_group)
bds_cloud_sql_group.add_command(bds_cli.add_cloud_sql)
bds_cloud_sql_group.add_command(bds_cli.remove_cloud_sql)


# Add command: oci bds auto-scaling-config create | delete | get | edit | list
@click.command('auto-scale-config', cls=CommandGroupWithAlias, help=bds_cli.add_auto_scaling_configuration.help)
@cli_util.help_option_group
def bds_auto_scaling_group():
    pass


bds_cli.bds_root_group.add_command(bds_auto_scaling_group)
bds_auto_scaling_group.add_command(bds_cli.add_auto_scaling_configuration)
cli_util.rename_command(bds_cli, bds_auto_scaling_group, bds_cli.add_auto_scaling_configuration, "create")
bds_auto_scaling_group.add_command(bds_cli.remove_auto_scaling_configuration)
cli_util.rename_command(bds_cli, bds_auto_scaling_group, bds_cli.remove_auto_scaling_configuration, "delete")
bds_cli.bds_instance_group.commands.pop(bds_cli.get_auto_scaling_configuration.name)
bds_auto_scaling_group.add_command(bds_cli.get_auto_scaling_configuration)
cli_util.rename_command(bds_cli, bds_auto_scaling_group, bds_cli.get_auto_scaling_configuration, "get")
bds_cli.bds_instance_group.commands.pop(bds_cli.update_auto_scaling_configuration.name)
bds_auto_scaling_group.add_command(bds_cli.update_auto_scaling_configuration)
cli_util.rename_command(bds_cli, bds_auto_scaling_group, bds_cli.update_auto_scaling_configuration, "edit")
bds_cli.bds_instance_group.commands.pop(bds_cli.list_auto_scaling_configurations.name)
bds_auto_scaling_group.add_command(bds_cli.list_auto_scaling_configurations)
cli_util.rename_command(bds_cli, bds_auto_scaling_group, bds_cli.list_auto_scaling_configurations, "list")
