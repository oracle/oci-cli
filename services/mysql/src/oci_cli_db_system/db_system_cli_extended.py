# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from services.mysql.src.oci_cli_db_system.generated import dbsystem_cli
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types
import click
import six
import oci.waiter
import sys
import json

# rename  oci mysql db-system create-db-system-create-db-system-source-from-backup-details -> oci mysql db-system clone
cli_util.rename_command(dbsystem_cli, dbsystem_cli.db_system_group, dbsystem_cli.create_db_system_create_db_system_source_from_backup_details, "clone")

# rename  oci mysql db-system create-db-system-create-db-system-source-import-from-url-details -> oci mysql db-system import
cli_util.rename_command(dbsystem_cli, dbsystem_cli.db_system_group, dbsystem_cli.create_db_system_create_db_system_source_import_from_url_details, "import")

# oci mysql db-system db-system -> oci mysql db-system system
dbsystem_cli.db_system_root_group.commands.pop(dbsystem_cli.db_system_group.name)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.create_db_system)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.create_db_system_create_db_system_source_from_backup_details)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.create_db_system_create_db_system_source_import_from_url_details)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.delete_db_system)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.get_db_system)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.list_db_systems)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.restart_db_system)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.start_db_system)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.stop_db_system)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.update_db_system)

# oci mysql db-system heat-wave-cluster -> oci mysql db-system heatwave-cluster
cli_util.rename_command(dbsystem_cli, dbsystem_cli.db_system_root_group, dbsystem_cli.heat_wave_cluster_group, "heatwave-cluster")


# oci mysql db-system heat-wave-cluster-memory-estimate -> oci mysql db-system heatwave-cluster-memory-estimate
cli_util.rename_command(dbsystem_cli, dbsystem_cli.db_system_root_group, dbsystem_cli.heat_wave_cluster_memory_estimate_group, "heatwave-cluster-memory-estimate")


@cli_util.copy_params_from_generated_command(dbsystem_cli.list_db_systems, params_to_exclude=['is_heat_wave_cluster_attached'])
@dbsystem_cli.db_system_root_group.command(name=dbsystem_cli.list_db_systems.name, help=dbsystem_cli.list_db_systems.help)
@cli_util.option('--is-heatwave-cluster-attached', type=click.BOOL, help=u"""If true, return only DB Systems with a HeatWave cluster attached, if false return only DB Systems with no HeatWave cluster attached. If not present, return all DB Systems.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'mysql', 'class': 'list[DbSystemSummary]'})
@cli_util.wrap_exceptions
def list_db_systems_extended(ctx, **kwargs):
    if 'is_heatwave_cluster_attached' in kwargs:
        kwargs['is_heat_wave_cluster_attached'] = kwargs['is_heatwave_cluster_attached']
        kwargs.pop('is_heatwave_cluster_attached')

    ctx.invoke(dbsystem_cli.list_db_systems, **kwargs)


@cli_util.copy_params_from_generated_command(dbsystem_cli.start_db_system, params_to_exclude=['wait_for_state'])
@dbsystem_cli.db_system_root_group.command(name=dbsystem_cli.start_db_system.name, help=dbsystem_cli.start_db_system.help)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def start_db_system_extended(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, db_system_id, if_match, **kwargs):
    if isinstance(db_system_id, six.string_types) and len(db_system_id.strip()) == 0:
        raise click.UsageError('Parameter --db-system-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('mysql', 'db_system', ctx)
    result = client.start_db_system(
        db_system_id=db_system_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_db_system') and callable(getattr(client, 'get_db_system')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo(
                    'Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state),
                    file=sys.stderr)
                result = oci.wait_until(client, client.get_db_system(db_system_id), 'lifecycle_state', wait_for_state,
                                        **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo(
                    'Failed to wait until the work request entered the specified state. Outputting last known resource state',
                    file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo(
                    'Encountered error while waiting for work request to enter the specified state. Outputting last known resource state',
                    file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@cli_util.copy_params_from_generated_command(dbsystem_cli.stop_db_system, params_to_exclude=['wait_for_state'])
@dbsystem_cli.db_system_root_group.command(name=dbsystem_cli.stop_db_system.name, help=dbsystem_cli.stop_db_system.help)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def stop_db_system_extended(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, db_system_id, shutdown_type, if_match, **kwargs):
    if isinstance(db_system_id, six.string_types) and len(db_system_id.strip()) == 0:
        raise click.UsageError('Parameter --db-system-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['shutdownType'] = shutdown_type

    client = cli_util.build_client('mysql', 'db_system', ctx)
    result = client.stop_db_system(
        db_system_id=db_system_id,
        stop_db_system_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_db_system') and callable(getattr(client, 'get_db_system')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_db_system(db_system_id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@cli_util.copy_params_from_generated_command(dbsystem_cli.create_db_system, params_to_exclude=['data_storage'])
@dbsystem_cli.db_system_root_group.command(name=dbsystem_cli.create_db_system.name, help=dbsystem_cli.create_db_system.help)
@cli_util.option('--is-auto-expand-storage-enabled', type=click.BOOL, help="""Checks whether Automatic Storage Expansion should be enabled for the dbsystem.""")
@cli_util.option('--max-storage-size-in-gbs', type=click.INT, help="""Sets the maximum storage size a db system can automatically be expanded to.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backup-policy': {'module': 'mysql', 'class': 'CreateBackupPolicyDetails'}, 'source': {'module': 'mysql', 'class': 'CreateDbSystemSourceDetails'}, 'maintenance': {'module': 'mysql', 'class': 'CreateMaintenanceDetails'}, 'freeform-tags': {'module': 'mysql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'mysql', 'class': 'dict(str, dict(str, object))'}, 'deletion-policy': {'module': 'mysql', 'class': 'CreateDeletionPolicyDetails'}, 'secure-connections': {'module': 'mysql', 'class': 'SecureConnectionDetails'}, 'customer-contacts': {'module': 'mysql', 'class': 'list[CustomerContact]'}, 'read-endpoint': {'module': 'mysql', 'class': 'CreateReadEndpointDetails'}}, output_type={'module': 'mysql', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def create_db_system_extended(ctx, **kwargs):
    data_storage = {}
    if 'is_auto_expand_storage_enabled' in kwargs and kwargs['is_auto_expand_storage_enabled'] is not None:
        data_storage['isAutoExpandStorageEnabled'] = kwargs['is_auto_expand_storage_enabled']
    kwargs.pop('is_auto_expand_storage_enabled')

    if 'max_storage_size_in_gbs' in kwargs and kwargs['max_storage_size_in_gbs'] is not None:
        data_storage['maxStorageSizeInGBs'] = kwargs['max_storage_size_in_gbs']
    kwargs.pop('max_storage_size_in_gbs')

    if len(data_storage) > 0:
        kwargs['data_storage'] = json.dumps(data_storage)

    ctx.invoke(dbsystem_cli.create_db_system, **kwargs)


@cli_util.copy_params_from_generated_command(dbsystem_cli.update_db_system, params_to_exclude=['data_storage'])
@dbsystem_cli.db_system_root_group.command(name=dbsystem_cli.update_db_system.name, help=dbsystem_cli.update_db_system.help)
@cli_util.option('--is-auto-expand-storage-enabled', type=click.BOOL, help="""Checks whether Automatic Storage Expansion should be enabled for the dbsystem.""")
@cli_util.option('--max-storage-size-in-gbs', type=click.INT, help="""Sets the maximum storage size a db system can automatically be expanded to.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backup-policy': {'module': 'mysql', 'class': 'UpdateBackupPolicyDetails'}, 'maintenance': {'module': 'mysql', 'class': 'UpdateMaintenanceDetails'}, 'freeform-tags': {'module': 'mysql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'mysql', 'class': 'dict(str, dict(str, object))'}, 'deletion-policy': {'module': 'mysql', 'class': 'UpdateDeletionPolicyDetails'}, 'secure-connections': {'module': 'mysql', 'class': 'SecureConnectionDetails'}, 'customer-contacts': {'module': 'mysql', 'class': 'list[CustomerContact]'}, 'read-endpoint': {'module': 'mysql', 'class': 'UpdateReadEndpointDetails'}})
@cli_util.wrap_exceptions
def update_db_system_extended(ctx, **kwargs):
    data_storage = {}
    if 'is_auto_expand_storage_enabled' in kwargs and kwargs['is_auto_expand_storage_enabled'] is not None:
        data_storage['isAutoExpandStorageEnabled'] = kwargs['is_auto_expand_storage_enabled']
    kwargs.pop('is_auto_expand_storage_enabled')

    if 'max_storage_size_in_gbs' in kwargs and kwargs['max_storage_size_in_gbs'] is not None:
        data_storage['maxStorageSizeInGBs'] = kwargs['max_storage_size_in_gbs']
    kwargs.pop('max_storage_size_in_gbs')

    if len(data_storage) > 0:
        kwargs['data_storage'] = json.dumps(data_storage)

    ctx.invoke(dbsystem_cli.update_db_system, **kwargs)


# clone
@cli_util.copy_params_from_generated_command(dbsystem_cli.create_db_system_create_db_system_source_from_backup_details, params_to_exclude=['data_storage'])
@dbsystem_cli.db_system_root_group.command(name="clone", help=dbsystem_cli.create_db_system_create_db_system_source_from_backup_details.help)
@cli_util.option('--is-auto-expand-storage-enabled', type=click.BOOL, help="""Checks whether Automatic Storage Expansion should be enabled for the dbsystem.""")
@cli_util.option('--max-storage-size-in-gbs', type=click.INT, help="""Sets the maximum storage size a db system can automatically be expanded to.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backup-policy': {'module': 'mysql', 'class': 'CreateBackupPolicyDetails'}, 'maintenance': {'module': 'mysql', 'class': 'CreateMaintenanceDetails'}, 'freeform-tags': {'module': 'mysql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'mysql', 'class': 'dict(str, dict(str, object))'}, 'deletion-policy': {'module': 'mysql', 'class': 'CreateDeletionPolicyDetails'}, 'secure-connections': {'module': 'mysql', 'class': 'SecureConnectionDetails'}, 'customer-contacts': {'module': 'mysql', 'class': 'list[CustomerContact]'}, 'read-endpoint': {'module': 'mysql', 'class': 'CreateReadEndpointDetails'}})
@cli_util.wrap_exceptions
def clone_db_system_extended(ctx, **kwargs):
    data_storage = {}
    if 'is_auto_expand_storage_enabled' in kwargs and kwargs['is_auto_expand_storage_enabled'] is not None:
        data_storage['isAutoExpandStorageEnabled'] = kwargs['is_auto_expand_storage_enabled']
    kwargs.pop('is_auto_expand_storage_enabled')

    if 'max_storage_size_in_gbs' in kwargs and kwargs['max_storage_size_in_gbs'] is not None:
        data_storage['maxStorageSizeInGBs'] = kwargs['max_storage_size_in_gbs']
    kwargs.pop('max_storage_size_in_gbs')

    if len(data_storage) > 0:
        kwargs['data_storage'] = json.dumps(data_storage)

    ctx.invoke(dbsystem_cli.create_db_system_create_db_system_source_from_backup_details, **kwargs)


# import
# rename --source-source-url argument
@cli_util.copy_params_from_generated_command(dbsystem_cli.create_db_system_create_db_system_source_import_from_url_details, params_to_exclude=['data_storage', 'source_source_url'])
@dbsystem_cli.db_system_root_group.command(name="import", help=dbsystem_cli.create_db_system_create_db_system_source_import_from_url_details.help)
@cli_util.option('--source-url', required=True, help="""The Pre-Authenticated Request (PAR) URL of the file you want to import from Object Storage.""")
@cli_util.option('--is-auto-expand-storage-enabled', type=click.BOOL, help="""Checks whether Automatic Storage Expansion should be enabled for the dbsystem.""")
@cli_util.option('--max-storage-size-in-gbs', type=click.INT, help="""Sets the maximum storage size a db system can automatically be expanded to.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backup-policy': {'module': 'mysql', 'class': 'CreateBackupPolicyDetails'}, 'maintenance': {'module': 'mysql', 'class': 'CreateMaintenanceDetails'}, 'freeform-tags': {'module': 'mysql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'mysql', 'class': 'dict(str, dict(str, object))'}, 'deletion-policy': {'module': 'mysql', 'class': 'CreateDeletionPolicyDetails'}, 'secure-connections': {'module': 'mysql', 'class': 'SecureConnectionDetails'}, 'customer-contacts': {'module': 'mysql', 'class': 'list[CustomerContact]'}, 'read-endpoint': {'module': 'mysql', 'class': 'CreateReadEndpointDetails'}}, output_type={'module': 'mysql', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def import_extended(ctx, **kwargs):
    data_storage = {}
    if 'is_auto_expand_storage_enabled' in kwargs and kwargs['is_auto_expand_storage_enabled'] is not None:
        data_storage['isAutoExpandStorageEnabled'] = kwargs['is_auto_expand_storage_enabled']
    kwargs.pop('is_auto_expand_storage_enabled')

    if 'max_storage_size_in_gbs' in kwargs:
        data_storage['maxStorageSizeInGBs'] = kwargs['max_storage_size_in_gbs']
    kwargs.pop('max_storage_size_in_gbs')

    if len(data_storage) > 0:
        kwargs['data_storage'] = json.dumps(data_storage)

    if 'source_url' in kwargs:
        kwargs['source_source_url'] = kwargs['source_url']
        kwargs.pop('source_url')

    ctx.invoke(dbsystem_cli.create_db_system_create_db_system_source_import_from_url_details, **kwargs)
