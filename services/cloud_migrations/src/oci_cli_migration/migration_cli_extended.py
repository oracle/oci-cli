# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
import click  # noqa: F401
import json  # noqa: F401
from services.cloud_migrations.src.oci_cli_migration.generated import migration_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401

cli_util.rename_command(migration_cli, migration_cli.migration_asset_group, migration_cli.list_migration_assets, "list")

# oci cloud-migrations migration-asset-collection list-migration-assets -> oci cloud-migrations migration-asset-collection list
migration_cli.cloud_migrations_root_group.commands.pop(
    migration_cli.migration_asset_collection_group.name)
migration_cli.migration_asset_group.add_command(migration_cli.list_migration_assets)
cli_util.rename_command(migration_cli, migration_cli.migration_asset_group, migration_cli.start_asset_replication,
                        "start_replication")

# oci cloud-migrations migration-collection list-migrations -> oci cloud-migrations migration-collection list
migration_cli.cloud_migrations_root_group.commands.pop(migration_cli.migration_collection_group.name)
migration_cli.migration_group.add_command(migration_cli.list_migrations)
cli_util.rename_command(migration_cli, migration_cli.migration_group, migration_cli.list_migrations, "list")

# oci cloud-migrations migration-plan-collection list-migration-plans -> oci cloud-migrations migration-plan-collection list
migration_cli.cloud_migrations_root_group.commands.pop(migration_cli.migration_plan_collection_group.name)
migration_cli.migration_plan_group.add_command(migration_cli.list_migration_plans)
cli_util.rename_command(migration_cli, migration_cli.migration_plan_group, migration_cli.list_migration_plans, "list")

# oci cloud-migrations replication-schedule-collection list-replication-schedules ->
# oci cloud-migrations replication-schedule-collection list
migration_cli.cloud_migrations_root_group.commands.pop(
    migration_cli.replication_schedule_collection_group.name)
migration_cli.replication_schedule_group.add_command(migration_cli.list_replication_schedules)
cli_util.rename_command(migration_cli, migration_cli.replication_schedule_group,
                        migration_cli.list_replication_schedules,
                        "list")

# oci cloud-migrations target-asset create-target-asset-create-vm-target-asset-details ->
# oci cloud-migrations target-asset create-vm
cli_util.rename_command(migration_cli, migration_cli.target_asset_group,
                        migration_cli.create_target_asset_create_vm_target_asset_details, "create-vm")

# oci cloud-migrations target-asset update-target-asset-update-vm-target-asset-details ->
# oci cloud-migrations target-asset update-vm
cli_util.rename_command(migration_cli, migration_cli.target_asset_group,
                        migration_cli.update_target_asset_update_vm_target_asset_details, "update-vm")

# oci cloud-migrations target-asset-collection list-target-assets -> oci cloud-migrations target-asset-collection list
migration_cli.cloud_migrations_root_group.commands.pop(migration_cli.target_asset_collection_group.name)
migration_cli.target_asset_group.add_command(migration_cli.list_target_assets)
cli_util.rename_command(migration_cli, migration_cli.target_asset_group, migration_cli.list_target_assets, "list")

# oci cloud-migrations work-request-log-entry list-work-request-logs -> oci cloud-migrations work-request-log-entry list
cli_util.rename_command(migration_cli, migration_cli.work_request_log_entry_group, migration_cli.list_work_request_logs,
                        "list")

# oci cloud-migrations available-shapes-collection list-available-shapes ->
# oci cloud-migrations available-shapes-collection list
cli_util.rename_command(migration_cli, migration_cli.available_shapes_collection_group,
                        migration_cli.list_available_shapes, "list")
cli_util.rename_command(migration_cli, migration_cli.cloud_migrations_root_group,
                        migration_cli.available_shapes_collection_group, "available_shapes")

# Consolidate the polymorphic CLI commands for create and update
migration_cli.target_asset_group.commands.pop(migration_cli.create_target_asset.name)
migration_cli.target_asset_group.commands.pop(migration_cli.create_target_asset_create_vm_target_asset_details.name)
migration_cli.target_asset_group.commands.pop(migration_cli.update_target_asset.name)
migration_cli.target_asset_group.commands.pop(migration_cli.update_target_asset_update_vm_target_asset_details.name)


@cli_util.copy_params_from_generated_command(migration_cli.create_target_asset, params_to_exclude=[''])
@migration_cli.target_asset_group.command(
    name=cli_util.override('cloud_migrations.create_target_asset.command_name', 'create'),
    help=u"""Creates a target asset. \n[Command Reference](createTargetAsset)""")
@cli_util.option('--preferred-shape-type', required=True, help=u"""Preferred VM shape type that you provide.""")
@cli_util.option('--user-spec', required=True, type=custom_types.CLI_COMPLEX_TYPE,
                 help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--block-volumes-performance', type=click.INT, help=u"""Performance of the block volumes.""")
@cli_util.option('--ms-license', help=u"""Microsoft license for the VM configuration.""")
@json_skeleton_utils.get_cli_json_input_option({'user-spec': {'module': 'cloud_migrations', 'class': 'LaunchInstanceDetails'}})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'user-spec': {'module': 'cloud_migrations', 'class': 'LaunchInstanceDetails'}}, output_type={'module': 'cloud_migrations', 'class': 'TargetAsset'})
@cli_util.wrap_exceptions
def create_target_asset(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, migration_plan_id,
                        type, is_excluded_from_execution, preferred_shape_type, user_spec, block_volumes_performance,
                        ms_license):
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['migrationPlanId'] = migration_plan_id
    _details['type'] = type
    _details['isExcludedFromExecution'] = is_excluded_from_execution
    _details['preferredShapeType'] = preferred_shape_type
    _details['userSpec'] = cli_util.parse_json_parameter("user_spec", user_spec)

    if block_volumes_performance is not None:
        _details['blockVolumesPerformance'] = block_volumes_performance

    if ms_license is not None:
        _details['msLicense'] = ms_license

    client = cli_util.build_client('cloud_migrations', 'migration', ctx)
    result = client.create_target_asset(
        create_target_asset_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo(
                    'Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state),
                    file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']),
                                        'status', wait_for_state, **wait_period_kwargs)
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


@cli_util.copy_params_from_generated_command(migration_cli.update_target_asset, params_to_exclude=[''])
@migration_cli.target_asset_group.command(
    name=cli_util.override('cloud_migrations.update_target_asset.command_name', 'update'),
    help=u"""Updates the target asset. \n[Command Reference](updateTargetAsset)""")
@cli_util.option('--preferred-shape-type', help=u"""Preferred VM shape type that you provided.""")
@cli_util.option('--block-volumes-performance', type=click.INT, help=u"""Performance of the block volumes.""")
@cli_util.option('--ms-license', help=u"""Microsoft license for VM configuration.""")
@cli_util.option('--user-spec', type=custom_types.CLI_COMPLEX_TYPE,
                 help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'user-spec': {'module': 'cloud_migrations', 'class': 'LaunchInstanceDetails'}})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'user-spec': {'module': 'cloud_migrations', 'class': 'LaunchInstanceDetails'}})
@cli_util.wrap_exceptions
def update_target_asset(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, target_asset_id,
                        type, is_excluded_from_execution, if_match, preferred_shape_type, block_volumes_performance,
                        ms_license, user_spec):
    if isinstance(target_asset_id, six.string_types) and len(target_asset_id.strip()) == 0:
        raise click.UsageError('Parameter --target-asset-id cannot be whitespace or empty string')

    if not force:
        if user_spec:
            if not click.confirm(
                    "WARNING: Updates to user-spec will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['type'] = type

    if is_excluded_from_execution is not None:
        _details['isExcludedFromExecution'] = is_excluded_from_execution

    if preferred_shape_type is not None:
        _details['preferredShapeType'] = preferred_shape_type

    if block_volumes_performance is not None:
        _details['blockVolumesPerformance'] = block_volumes_performance

    if ms_license is not None:
        _details['msLicense'] = ms_license

    if user_spec is not None:
        _details['userSpec'] = cli_util.parse_json_parameter("user_spec", user_spec)

    client = cli_util.build_client('cloud_migrations', 'migration', ctx)
    result = client.update_target_asset(
        target_asset_id=target_asset_id,
        update_target_asset_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo(
                    'Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state),
                    file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']),
                                        'status', wait_for_state, **wait_period_kwargs)
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
