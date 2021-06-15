# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from services.data_safe.src.oci_cli_data_safe.generated import datasafe_cli

# 1 :
# From: oci data-safe data-safe-configuration get --compartment-id | -c, -? | -h | --help
# To: oci data-safe configuration get --compartment-id | -c, -? | -h | --help

cli_util.rename_command(datasafe_cli, datasafe_cli.data_safe_root_group, datasafe_cli.data_safe_configuration_group, "configuration")


# 2:
# From: oci data-safe data-safe-private-endpoint change-compartment --data-safe-private-endpoint-id, --compartment-id | -c, -? | -h | --help
# To: oci data-safe private-endpoint change-compartment --private-endpoint-id, --compartment-id | -c, -? | -h | --help
# Step 1: Rename data-safe-private-endpoint to  private-endpoint. This applies for all the commands
cli_util.rename_command(datasafe_cli, datasafe_cli.data_safe_root_group, datasafe_cli.data_safe_private_endpoint_group, "private-endpoint")


# Step 2: Change --data-safe-private-endpoint-id to --private-endpoint-id
@cli_util.copy_params_from_generated_command(datasafe_cli.change_data_safe_private_endpoint_compartment, params_to_exclude=['data_safe_private_endpoint_id'])
@datasafe_cli.data_safe_private_endpoint_group.command(name='change-compartment', help=datasafe_cli.change_data_safe_private_endpoint_compartment.help)
@cli_util.option('--private-endpoint-id', required=True, help=u"""unique data safe private endpoint identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_data_safe_private_endpoint_compartment_extended(ctx, **kwargs):
    if 'private_endpoint_id' in kwargs:
        kwargs['data_safe_private_endpoint_id'] = kwargs['private_endpoint_id']
        kwargs.pop('private_endpoint_id')
    ctx.invoke(datasafe_cli.change_data_safe_private_endpoint_compartment, **kwargs)

# 3:
# From: oci data-safe data-safe-private-endpoint delete --data-safe-private-endpoint-id, --force, -? | -h | --help
# To: oci data-safe private-endpoint delete --private-endpoint-id, --force, -? | -h | --help
# cli_util.rename_command(datasafe_cli, datasafe_cli.data_safe_root_group, datasafe_cli.data_safe_private_endpoint_group, "private-endpoint")


# Step 2:
@cli_util.copy_params_from_generated_command(datasafe_cli.delete_data_safe_private_endpoint, params_to_exclude=['data_safe_private_endpoint_id'])
@datasafe_cli.data_safe_private_endpoint_group.command(name='delete', help=datasafe_cli.delete_data_safe_private_endpoint.help)
@cli_util.option('--private-endpoint-id', required=True, help=u"""unique data safe private endpoint identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_data_safe_private_endpoint_extended(ctx, **kwargs):
    if 'private_endpoint_id' in kwargs:
        kwargs['data_safe_private_endpoint_id'] = kwargs['private_endpoint_id']
        kwargs.pop('private_endpoint_id')
    ctx.invoke(datasafe_cli.delete_data_safe_private_endpoint, **kwargs)

# 4
# From: oci data-safe data-safe-private-endpoint get --data-safe-private-endpoint-id, -? | -h | --help
# To: oci data-safe private-endpoint get --private-endpoint-id, -? | -h | --help
# Step 2:


@cli_util.copy_params_from_generated_command(datasafe_cli.get_data_safe_private_endpoint, params_to_exclude=['data_safe_private_endpoint_id'])
@datasafe_cli.data_safe_private_endpoint_group.command(name='get', help=datasafe_cli.get_data_safe_private_endpoint.help)
@cli_util.option('--private-endpoint-id', required=True, help=u"""unique data safe private endpoint identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_safe', 'class': 'DataSafePrivateEndpoint'})
@cli_util.wrap_exceptions
def get_data_safe_private_endpoint_extended(ctx, **kwargs):
    if 'private_endpoint_id' in kwargs:
        kwargs['data_safe_private_endpoint_id'] = kwargs['private_endpoint_id']
        kwargs.pop('private_endpoint_id')

    ctx.invoke(datasafe_cli.get_data_safe_private_endpoint, **kwargs)

# 5 :
# From: oci data-safe data-safe-private-endpoint update --data-safe-private-endpoint-id, --display-name, --defined-tags, --description, --force, --freeform-tags, -? | -h | --help, --nsg-ids
# To: oci data-safe private-endpoint update --private-endpoint-id, --display-name, --defined-tags, --description, --force, --freeform-tags, -? | -h | --help, --nsg-ids
# Step 2;


@cli_util.copy_params_from_generated_command(datasafe_cli.update_data_safe_private_endpoint, params_to_exclude=['data_safe_private_endpoint_id'])
@datasafe_cli.data_safe_private_endpoint_group.command(name='update', help=datasafe_cli.update_data_safe_private_endpoint.help)
@cli_util.option('--private-endpoint-id', required=True, help=u"""unique data safe private endpoint identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'nsg-ids': {'module': 'data_safe', 'class': 'list[string]'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_data_safe_private_endpoint_extended(ctx, **kwargs):
    if 'private_endpoint_id' in kwargs:
        kwargs['data_safe_private_endpoint_id'] = kwargs['private_endpoint_id']
        kwargs.pop('private_endpoint_id')
    ctx.invoke(datasafe_cli.update_data_safe_private_endpoint, **kwargs)


# 6 :
# From:
# oci data-safe enable-data-safe-configuration-details enable-data-safe-configuration --compartment-id | -c, --defined-tags, --force, --freeform-tags, -? | -h | --help, --is-enabled
# To: oci data-safe service enable --compartment-id | -c, --defined-tags, --force, --freeform-tags, -? | -h | --help, --is-enabled


cli_util.rename_command(datasafe_cli, datasafe_cli.data_safe_root_group, datasafe_cli.data_safe_configuration_group, "service")

cli_util.rename_command(datasafe_cli, datasafe_cli.data_safe_configuration_group, datasafe_cli.enable_data_safe_configuration, "enable")


# 7:
# From:  oci data-safe work-request-log-entry list-work-request-logs --work-request-id, --all, -? | -h | --help
# To: oci data-safe work-request-log-entry list --work-request-id, --all, -? | -h | --help
cli_util.rename_command(datasafe_cli, datasafe_cli.work_request_log_entry_group, datasafe_cli.list_work_request_logs, "list")


# Remove create-target-database-autonomous-database-details from oci data-safe target-database
datasafe_cli.target_database_group.commands.pop(datasafe_cli.create_target_database_autonomous_database_details.name)


# Remove create-target-database-database-cloud-service-details from oci data-safe target-database
datasafe_cli.target_database_group.commands.pop(datasafe_cli.create_target_database_database_cloud_service_details.name)


# Remove create-target-database-installed-database-details from oci data-safe target-database
datasafe_cli.target_database_group.commands.pop(datasafe_cli.create_target_database_installed_database_details.name)


# Remove create-target-database-on-premise-connector from oci data-safe target-database
datasafe_cli.target_database_group.commands.pop(datasafe_cli.create_target_database_on_premise_connector.name)


# Remove create-target-database-private-endpoint from oci data-safe target-database
datasafe_cli.target_database_group.commands.pop(datasafe_cli.create_target_database_private_endpoint.name)


# Remove update-target-database-autonomous-database-details from oci data-safe target-database
datasafe_cli.target_database_group.commands.pop(datasafe_cli.update_target_database_autonomous_database_details.name)


# Remove update-target-database-database-cloud-service-details from oci data-safe target-database
datasafe_cli.target_database_group.commands.pop(datasafe_cli.update_target_database_database_cloud_service_details.name)


# Remove update-target-database-installed-database-details from oci data-safe target-database
datasafe_cli.target_database_group.commands.pop(datasafe_cli.update_target_database_installed_database_details.name)


# Remove update-target-database-on-premise-connector from oci data-safe target-database
datasafe_cli.target_database_group.commands.pop(datasafe_cli.update_target_database_on_premise_connector.name)


# Remove update-target-database-private-endpoint from oci data-safe target-database
datasafe_cli.target_database_group.commands.pop(datasafe_cli.update_target_database_private_endpoint.name)
