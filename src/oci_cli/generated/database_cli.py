# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from ..cli_root import cli
from .. import cli_constants  # noqa: F401
from .. import cli_util
from .. import json_skeleton_utils
from .. import custom_types  # noqa: F401
from ..aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('db_root_group.command_name', 'db'), cls=CommandGroupWithAlias, help=cli_util.override('db_root_group.help', """The API for the Database Service."""), short_help=cli_util.override('db_root_group.short_help', """Database Service API"""))
@cli_util.help_option_group
def db_root_group():
    pass


@click.command(cli_util.override('autonomous_data_warehouse_backup_group.command_name', 'autonomous-data-warehouse-backup'), cls=CommandGroupWithAlias, help="""An Autonomous Data Warehouse backup. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def autonomous_data_warehouse_backup_group():
    pass


@click.command(cli_util.override('autonomous_data_warehouse_group.command_name', 'autonomous-data-warehouse'), cls=CommandGroupWithAlias, help="""An Oracle Autonomous Data Warehouse.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def autonomous_data_warehouse_group():
    pass


@click.command(cli_util.override('backup_group.command_name', 'backup'), cls=CommandGroupWithAlias, help="""A database backup. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def backup_group():
    pass


@click.command(cli_util.override('db_system_group.command_name', 'db-system'), cls=CommandGroupWithAlias, help="""The Database Service supports several types of DB systems, ranging in size, price, and performance. For details about each type of system, see:

- [Exadata DB Systems] - [Bare Metal and Virtual Machine DB Systems]

To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see [Getting Started with Policies].

For information about access control and compartments, see [Overview of the Identity Service].

For information about availability domains, see [Regions and Availability Domains].

To get a list of availability domains, use the `ListAvailabilityDomains` operation in the Identity Service API.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def db_system_group():
    pass


@click.command(cli_util.override('autonomous_database_group.command_name', 'autonomous-database'), cls=CommandGroupWithAlias, help="""An Oracle Autonomous Database.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def autonomous_database_group():
    pass


@click.command(cli_util.override('patch_group.command_name', 'patch'), cls=CommandGroupWithAlias, help="""A Patch for a DB system or DB Home.

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def patch_group():
    pass


@click.command(cli_util.override('db_version_group.command_name', 'db-version'), cls=CommandGroupWithAlias, help="""The Oracle database software version.

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def db_version_group():
    pass


@click.command(cli_util.override('database_group.command_name', 'database'), cls=CommandGroupWithAlias, help="""An Oracle database on a bare metal or virtual machine DB system. For more information, see [Bare Metal and Virtual Machine DB Systems].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def database_group():
    pass


@click.command(cli_util.override('patch_history_entry_group.command_name', 'patch-history-entry'), cls=CommandGroupWithAlias, help="""The record of a patch action on a specified target.""")
@cli_util.help_option_group
def patch_history_entry_group():
    pass


@click.command(cli_util.override('db_system_shape_group.command_name', 'db-system-shape'), cls=CommandGroupWithAlias, help="""The shape of the DB system. The shape determines resources to allocate to the DB system - CPU cores and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes. For a description of shapes, see [DB System Launch Options]. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def db_system_shape_group():
    pass


@click.command(cli_util.override('data_guard_association_group.command_name', 'data-guard-association'), cls=CommandGroupWithAlias, help="""The properties that define a Data Guard association.

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

For information about endpoints and signing API requests, see [About the API]. For information about available SDKs and tools, see [SDKS and Other Tools].""")
@cli_util.help_option_group
def data_guard_association_group():
    pass


@click.command(cli_util.override('autonomous_database_backup_group.command_name', 'autonomous-database-backup'), cls=CommandGroupWithAlias, help="""An Autonomous Database backup. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def autonomous_database_backup_group():
    pass


@click.command(cli_util.override('db_home_group.command_name', 'db-home'), cls=CommandGroupWithAlias, help="""A directory where Oracle Database software is installed. A bare metal DB system can have multiple database homes and each database home can run a different supported version of Oracle Database. A virtual machine DB system can have only one database home. For more information, see [Bare Metal and Virtual Machine DB Systems].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def db_home_group():
    pass


@click.command(cli_util.override('db_node_group.command_name', 'db-node'), cls=CommandGroupWithAlias, help="""A server where Oracle Database software is running.

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def db_node_group():
    pass


@click.command(cli_util.override('external_backup_job_group.command_name', 'external-backup-job'), cls=CommandGroupWithAlias, help="""Provides all the details that apply to an external backup job.""")
@cli_util.help_option_group
def external_backup_job_group():
    pass


db_root_group.add_command(autonomous_data_warehouse_backup_group)
db_root_group.add_command(autonomous_data_warehouse_group)
db_root_group.add_command(backup_group)
db_root_group.add_command(db_system_group)
db_root_group.add_command(autonomous_database_group)
db_root_group.add_command(patch_group)
db_root_group.add_command(db_version_group)
db_root_group.add_command(database_group)
db_root_group.add_command(patch_history_entry_group)
db_root_group.add_command(db_system_shape_group)
db_root_group.add_command(data_guard_association_group)
db_root_group.add_command(autonomous_database_backup_group)
db_root_group.add_command(db_home_group)
db_root_group.add_command(db_node_group)
db_root_group.add_command(external_backup_job_group)


@external_backup_job_group.command(name=cli_util.override('complete_external_backup_job.command_name', 'complete'), help="""Changes the status of the standalone backup resource to `ACTIVE` after the backup is created from the on-premises database and placed in Oracle Cloud Infrastructure Object Storage.

**Note:** This API is used by an Oracle Cloud Infrastructure Python script that is packaged with the Oracle Cloud Infrastructure CLI. Oracle recommends that you use the script instead using the API directly. See [Migrating an On-Premises Database to Oracle Cloud Infrastructure by Creating a Backup in the Cloud] for more information.""")
@cli_util.option('--backup-id', required=True, help="""The backup [OCID].""")
@cli_util.option('--cf-backup-handle', help="""The handle of the control file backup.""")
@cli_util.option('--data-size', type=click.INT, help="""The size of the data in the database, in megabytes.""")
@cli_util.option('--redo-size', type=click.INT, help="""The size of the redo in the database, in megabytes.""")
@cli_util.option('--spf-backup-handle', help="""The handle of the spfile backup.""")
@cli_util.option('--sql-patches', type=custom_types.CLI_COMPLEX_TYPE, help="""The list of SQL patches that need to be applied to the backup during the restore.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--tde-wallet-path', help="""If the database being backed up is TDE enabled, this will be the path to the associated TDE wallet in Object Storage.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'sql-patches': {'module': 'database', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'sql-patches': {'module': 'database', 'class': 'list[string]'}}, output_type={'module': 'database', 'class': 'ExternalBackupJob'})
@cli_util.wrap_exceptions
def complete_external_backup_job(ctx, from_json, backup_id, cf_backup_handle, data_size, redo_size, spf_backup_handle, sql_patches, tde_wallet_path, if_match):

    if isinstance(backup_id, six.string_types) and len(backup_id.strip()) == 0:
        raise click.UsageError('Parameter --backup-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if cf_backup_handle is not None:
        details['cfBackupHandle'] = cf_backup_handle

    if data_size is not None:
        details['dataSize'] = data_size

    if redo_size is not None:
        details['redoSize'] = redo_size

    if spf_backup_handle is not None:
        details['spfBackupHandle'] = spf_backup_handle

    if sql_patches is not None:
        details['sqlPatches'] = cli_util.parse_json_parameter("sql_patches", sql_patches)

    if tde_wallet_path is not None:
        details['tdeWalletPath'] = tde_wallet_path

    client = cli_util.build_client('database', ctx)
    result = client.complete_external_backup_job(
        backup_id=backup_id,
        complete_external_backup_job_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@autonomous_data_warehouse_group.command(name=cli_util.override('create_autonomous_data_warehouse.command_name', 'create'), help="""Creates a new Autonomous Data Warehouse.""")
@cli_util.option('--admin-password', required=True, help="""A strong password for Admin. The password must be between 12 and 60 characters long, and must contain at least 1 uppercase, 1 lowercase and 2 numeric characters. It cannot contain the double quote symbol (\"). It must be different than the last 4 passwords.""")
@cli_util.option('--compartment-id', required=True, help="""The [OCID] of the compartment of the Autonomous Data Warehouse.""")
@cli_util.option('--cpu-core-count', required=True, type=click.INT, help="""The number of CPU Cores to be made available to the database.""")
@cli_util.option('--data-storage-size-in-tbs', required=True, type=click.INT, help="""Size, in terabytes, of the data volume that will be created and attached to the database. This storage can later be scaled up if needed.""")
@cli_util.option('--db-name', required=True, help="""The database name. The name must begin with an alphabetic character and can contain a maximum of 14 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""The user-friendly name for the Autonomous Data Warehouse. The name does not have to be unique.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--license-model', type=custom_types.CliCaseInsensitiveChoice(["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]), help="""The Oracle license model that applies to the Oracle Autonomous Data Warehouse. The default is BRING_YOUR_OWN_LICENSE.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}}, output_type={'module': 'database', 'class': 'AutonomousDataWarehouse'})
@cli_util.wrap_exceptions
def create_autonomous_data_warehouse(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, admin_password, compartment_id, cpu_core_count, data_storage_size_in_tbs, db_name, defined_tags, display_name, freeform_tags, license_model):
    kwargs = {}

    details = {}
    details['adminPassword'] = admin_password
    details['compartmentId'] = compartment_id
    details['cpuCoreCount'] = cpu_core_count
    details['dataStorageSizeInTBs'] = data_storage_size_in_tbs
    details['dbName'] = db_name

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if license_model is not None:
        details['licenseModel'] = license_model

    client = cli_util.build_client('database', ctx)
    result = client.create_autonomous_data_warehouse(
        create_autonomous_data_warehouse_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_data_warehouse') and callable(getattr(client, 'get_autonomous_data_warehouse')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_data_warehouse(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_data_warehouse_backup_group.command(name=cli_util.override('create_autonomous_data_warehouse_backup.command_name', 'create'), help="""Creates a new Autonomous Data Warehouse backup for the specified database based on the provided request parameters.""")
@cli_util.option('--autonomous-data-warehouse-id', required=True, help="""The [OCID] of the Autonomous Data Warehouse backup.""")
@cli_util.option('--display-name', required=True, help="""The user-friendly name for the backup. The name does not have to be unique.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'AutonomousDataWarehouseBackup'})
@cli_util.wrap_exceptions
def create_autonomous_data_warehouse_backup(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, autonomous_data_warehouse_id, display_name):
    kwargs = {}

    details = {}
    details['autonomousDataWarehouseId'] = autonomous_data_warehouse_id
    details['displayName'] = display_name

    client = cli_util.build_client('database', ctx)
    result = client.create_autonomous_data_warehouse_backup(
        create_autonomous_data_warehouse_backup_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_data_warehouse_backup') and callable(getattr(client, 'get_autonomous_data_warehouse_backup')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_data_warehouse_backup(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_database_group.command(name=cli_util.override('create_autonomous_database.command_name', 'create'), help="""Creates a new Autonomous Database.""")
@cli_util.option('--admin-password', required=True, help="""A strong password for Admin. The password must be between 12 and 60 characters long, and must contain at least 1 uppercase, 1 lowercase and 2 numeric characters. It cannot contain the double quote symbol (\"). It must be different than the last 4 passwords.""")
@cli_util.option('--compartment-id', required=True, help="""The [OCID] of the compartment of the autonomous database.""")
@cli_util.option('--cpu-core-count', required=True, type=click.INT, help="""The number of CPU Cores to be made available to the database.""")
@cli_util.option('--data-storage-size-in-tbs', required=True, type=click.INT, help="""The size, in terabytes, of the data volume that will be created and attached to the database. This storage can later be scaled up if needed.""")
@cli_util.option('--db-name', required=True, help="""The database name. The name must begin with an alphabetic character and can contain a maximum of 14 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""The user-friendly name for the Autonomous Database. The name does not have to be unique.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--license-model', type=custom_types.CliCaseInsensitiveChoice(["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]), help="""The Oracle license model that applies to the Oracle Autonomous Database. The default is BRING_YOUR_OWN_LICENSE.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "RESTORE_FAILED", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}}, output_type={'module': 'database', 'class': 'AutonomousDatabase'})
@cli_util.wrap_exceptions
def create_autonomous_database(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, admin_password, compartment_id, cpu_core_count, data_storage_size_in_tbs, db_name, defined_tags, display_name, freeform_tags, license_model):
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['adminPassword'] = admin_password
    details['compartmentId'] = compartment_id
    details['cpuCoreCount'] = cpu_core_count
    details['dataStorageSizeInTBs'] = data_storage_size_in_tbs
    details['dbName'] = db_name

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if license_model is not None:
        details['licenseModel'] = license_model

    client = cli_util.build_client('database', ctx)
    result = client.create_autonomous_database(
        create_autonomous_database_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_database') and callable(getattr(client, 'get_autonomous_database')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_database(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_database_backup_group.command(name=cli_util.override('create_autonomous_database_backup.command_name', 'create'), help="""Creates a new Autonomous Database backup for the specified database based on the provided request parameters.""")
@cli_util.option('--autonomous-database-id', required=True, help="""The [OCID] of the Autonomous Database backup.""")
@cli_util.option('--display-name', required=True, help="""The user-friendly name for the backup. The name does not have to be unique.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'AutonomousDatabaseBackup'})
@cli_util.wrap_exceptions
def create_autonomous_database_backup(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, autonomous_database_id, display_name):
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['autonomousDatabaseId'] = autonomous_database_id
    details['displayName'] = display_name

    client = cli_util.build_client('database', ctx)
    result = client.create_autonomous_database_backup(
        create_autonomous_database_backup_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_database_backup') and callable(getattr(client, 'get_autonomous_database_backup')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_database_backup(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@backup_group.command(name=cli_util.override('create_backup.command_name', 'create'), help="""Creates a new backup in the specified database based on the request parameters you provide. If you previously used RMAN or dbcli to configure backups and then you switch to using the Console or the API for backups, a new backup configuration is created and associated with your database. This means that you can no longer rely on your previously configured unmanaged backups to work.""")
@cli_util.option('--database-id', required=True, help="""The [OCID] of the database.""")
@cli_util.option('--display-name', required=True, help="""The user-friendly name for the backup. The name does not have to be unique.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "RESTORING"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'Backup'})
@cli_util.wrap_exceptions
def create_backup(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_id, display_name):
    kwargs = {}

    details = {}
    details['databaseId'] = database_id
    details['displayName'] = display_name

    client = cli_util.build_client('database', ctx)
    result = client.create_backup(
        create_backup_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_backup') and callable(getattr(client, 'get_backup')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_backup(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@data_guard_association_group.command(name=cli_util.override('create_data_guard_association.command_name', 'create'), help="""Creates a new Data Guard association.  A Data Guard association represents the replication relationship between the specified database and a peer database. For more information, see [Using Oracle Data Guard].

All Oracle Cloud Infrastructure resources, including Data Guard associations, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. For more information, see [Resource Identifiers].""")
@cli_util.option('--database-id', required=True, help="""The database [OCID].""")
@cli_util.option('--creation-type', required=True, help="""Specifies where to create the associated database. \"ExistingDbSystem\" is the only supported `creationType` value.""")
@cli_util.option('--database-admin-password', required=True, help="""A strong password for the `SYS`, `SYSTEM`, and `PDB Admin` users to apply during standby creation.

The password must contain no fewer than nine characters and include:

* At least two uppercase characters.

* At least two lowercase characters.

* At least two numeric characters.

* At least two special characters. Valid special characters include \"_\", \"#\", and \"-\" only.

**The password MUST be the same as the primary admin password.**""")
@cli_util.option('--protection-mode', required=True, type=custom_types.CliCaseInsensitiveChoice(["MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE", "MAXIMUM_PROTECTION"]), help="""The protection mode to set up between the primary and standby databases. For more information, see [Oracle Data Guard Protection Modes] in the Oracle Data Guard documentation.

**IMPORTANT** - The only protection mode currently supported by the Database Service is MAXIMUM_PERFORMANCE.""")
@cli_util.option('--transport-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["SYNC", "ASYNC", "FASTSYNC"]), help="""The redo transport type to use for this Data Guard association.  Valid values depend on the specified `protectionMode`:

* MAXIMUM_AVAILABILITY - SYNC or FASTSYNC * MAXIMUM_PERFORMANCE - ASYNC * MAXIMUM_PROTECTION - SYNC

For more information, see [Redo Transport Services] in the Oracle Data Guard documentation.

**IMPORTANT** - The only transport type currently supported by the Database Service is ASYNC.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DataGuardAssociation'})
@cli_util.wrap_exceptions
def create_data_guard_association(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_id, creation_type, database_admin_password, protection_mode, transport_type):

    if isinstance(database_id, six.string_types) and len(database_id.strip()) == 0:
        raise click.UsageError('Parameter --database-id cannot be whitespace or empty string')
    kwargs = {}

    details = {}
    details['creationType'] = creation_type
    details['databaseAdminPassword'] = database_admin_password
    details['protectionMode'] = protection_mode
    details['transportType'] = transport_type

    client = cli_util.build_client('database', ctx)
    result = client.create_data_guard_association(
        database_id=database_id,
        create_data_guard_association_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_data_guard_association') and callable(getattr(client, 'get_data_guard_association')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_guard_association(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@data_guard_association_group.command(name=cli_util.override('create_data_guard_association_create_data_guard_association_to_existing_db_system_details.command_name', 'create-data-guard-association-create-data-guard-association-to-existing-db-system-details'), help="""Creates a new Data Guard association.  A Data Guard association represents the replication relationship between the specified database and a peer database. For more information, see [Using Oracle Data Guard].

All Oracle Cloud Infrastructure resources, including Data Guard associations, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. For more information, see [Resource Identifiers].""")
@cli_util.option('--database-id', required=True, help="""The database [OCID].""")
@cli_util.option('--database-admin-password', required=True, help="""A strong password for the `SYS`, `SYSTEM`, and `PDB Admin` users to apply during standby creation.

The password must contain no fewer than nine characters and include:

* At least two uppercase characters.

* At least two lowercase characters.

* At least two numeric characters.

* At least two special characters. Valid special characters include \"_\", \"#\", and \"-\" only.

**The password MUST be the same as the primary admin password.**""")
@cli_util.option('--protection-mode', required=True, type=custom_types.CliCaseInsensitiveChoice(["MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE", "MAXIMUM_PROTECTION"]), help="""The protection mode to set up between the primary and standby databases. For more information, see [Oracle Data Guard Protection Modes] in the Oracle Data Guard documentation.

**IMPORTANT** - The only protection mode currently supported by the Database Service is MAXIMUM_PERFORMANCE.""")
@cli_util.option('--transport-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["SYNC", "ASYNC", "FASTSYNC"]), help="""The redo transport type to use for this Data Guard association.  Valid values depend on the specified `protectionMode`:

* MAXIMUM_AVAILABILITY - SYNC or FASTSYNC * MAXIMUM_PERFORMANCE - ASYNC * MAXIMUM_PROTECTION - SYNC

For more information, see [Redo Transport Services] in the Oracle Data Guard documentation.

**IMPORTANT** - The only transport type currently supported by the Database Service is ASYNC.""")
@cli_util.option('--peer-db-system-id', help="""The [OCID] of the DB system to create the standby database on.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DataGuardAssociation'})
@cli_util.wrap_exceptions
def create_data_guard_association_create_data_guard_association_to_existing_db_system_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_id, database_admin_password, protection_mode, transport_type, peer_db_system_id):

    if isinstance(database_id, six.string_types) and len(database_id.strip()) == 0:
        raise click.UsageError('Parameter --database-id cannot be whitespace or empty string')
    kwargs = {}

    details = {}
    details['databaseAdminPassword'] = database_admin_password
    details['protectionMode'] = protection_mode
    details['transportType'] = transport_type

    if peer_db_system_id is not None:
        details['peerDbSystemId'] = peer_db_system_id

    details['creationType'] = 'ExistingDbSystem'

    client = cli_util.build_client('database', ctx)
    result = client.create_data_guard_association(
        database_id=database_id,
        create_data_guard_association_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_data_guard_association') and callable(getattr(client, 'get_data_guard_association')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_guard_association(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_home_group.command(name=cli_util.override('create_db_home.command_name', 'create'), help="""Creates a new database home in the specified DB system based on the request parameters you provide.""")
@cli_util.option('--db-system-id', required=True, help="""The [OCID] of the DB system.""")
@cli_util.option('--display-name', help="""The user-provided name of the database home.""")
@cli_util.option('--source', type=custom_types.CliCaseInsensitiveChoice(["NONE", "DB_BACKUP"]), help="""The source of database: NONE for creating a new database. DB_BACKUP for creating a new database by restoring from a database backup.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DbHome'})
@cli_util.wrap_exceptions
def create_db_home(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, db_system_id, display_name, source):
    kwargs = {}

    details = {}
    details['dbSystemId'] = db_system_id

    if display_name is not None:
        details['displayName'] = display_name

    if source is not None:
        details['source'] = source

    client = cli_util.build_client('database', ctx)
    result = client.create_db_home(
        create_db_home_with_db_system_id_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_db_home') and callable(getattr(client, 'get_db_home')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_db_home(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_home_group.command(name=cli_util.override('create_db_home_create_db_home_with_db_system_id_from_backup_details.command_name', 'create-db-home-create-db-home-with-db-system-id-from-backup-details'), help="""Creates a new database home in the specified DB system based on the request parameters you provide.""")
@cli_util.option('--db-system-id', required=True, help="""The [OCID] of the DB system.""")
@cli_util.option('--database', required=True, type=custom_types.CLI_COMPLEX_TYPE, help="""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""The user-provided name of the database home.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'database': {'module': 'database', 'class': 'CreateDatabaseFromBackupDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database': {'module': 'database', 'class': 'CreateDatabaseFromBackupDetails'}}, output_type={'module': 'database', 'class': 'DbHome'})
@cli_util.wrap_exceptions
def create_db_home_create_db_home_with_db_system_id_from_backup_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, db_system_id, database, display_name):
    kwargs = {}

    details = {}
    details['dbSystemId'] = db_system_id
    details['database'] = cli_util.parse_json_parameter("database", database)

    if display_name is not None:
        details['displayName'] = display_name

    details['source'] = 'DB_BACKUP'

    client = cli_util.build_client('database', ctx)
    result = client.create_db_home(
        create_db_home_with_db_system_id_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_db_home') and callable(getattr(client, 'get_db_home')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_db_home(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_home_group.command(name=cli_util.override('create_db_home_create_db_home_with_db_system_id_details.command_name', 'create-db-home-create-db-home-with-db-system-id-details'), help="""Creates a new database home in the specified DB system based on the request parameters you provide.""")
@cli_util.option('--db-system-id', required=True, help="""The [OCID] of the DB system.""")
@cli_util.option('--database', required=True, type=custom_types.CLI_COMPLEX_TYPE, help="""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--db-version', required=True, help="""A valid Oracle Database version. To get a list of supported versions, use the [ListDbVersions] operation.""")
@cli_util.option('--display-name', help="""The user-provided name of the database home.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'database': {'module': 'database', 'class': 'CreateDatabaseDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database': {'module': 'database', 'class': 'CreateDatabaseDetails'}}, output_type={'module': 'database', 'class': 'DbHome'})
@cli_util.wrap_exceptions
def create_db_home_create_db_home_with_db_system_id_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, db_system_id, database, db_version, display_name):
    kwargs = {}

    details = {}
    details['dbSystemId'] = db_system_id
    details['database'] = cli_util.parse_json_parameter("database", database)
    details['dbVersion'] = db_version

    if display_name is not None:
        details['displayName'] = display_name

    details['source'] = 'NONE'

    client = cli_util.build_client('database', ctx)
    result = client.create_db_home(
        create_db_home_with_db_system_id_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_db_home') and callable(getattr(client, 'get_db_home')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_db_home(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@external_backup_job_group.command(name=cli_util.override('create_external_backup_job.command_name', 'create'), help="""Creates a new backup resource and returns the information the caller needs to back up an on-premises Oracle Database to Oracle Cloud Infrastructure.

**Note:** This API is used by an Oracle Cloud Infrastructure Python script that is packaged with the Oracle Cloud Infrastructure CLI. Oracle recommends that you use the script instead using the API directly. See [Migrating an On-Premises Database to Oracle Cloud Infrastructure by Creating a Backup in the Cloud] for more information.""")
@cli_util.option('--availability-domain', required=True, help="""The targeted availability domain for the backup.""")
@cli_util.option('--character-set', required=True, help="""The character set for the database.""")
@cli_util.option('--compartment-id', required=True, help="""The [OCID] of the compartment where this backup should be created.""")
@cli_util.option('--database-edition', required=True, type=custom_types.CliCaseInsensitiveChoice(["STANDARD_EDITION", "ENTERPRISE_EDITION", "ENTERPRISE_EDITION_HIGH_PERFORMANCE", "ENTERPRISE_EDITION_EXTREME_PERFORMANCE"]), help="""The Oracle Database edition to use for creating a database from this standalone backup. Note that 2-node RAC DB systems require Enterprise Edition - Extreme Performance.""")
@cli_util.option('--database-mode', required=True, type=custom_types.CliCaseInsensitiveChoice(["SI", "RAC"]), help="""The mode (single instance or RAC) of the database being backed up.""")
@cli_util.option('--db-name', required=True, help="""The name of the database from which the backup is being taken.""")
@cli_util.option('--db-version', required=True, help="""A valid Oracle Database version.""")
@cli_util.option('--display-name', required=True, help="""A user-friendly name for the backup. This name does not have to be unique.""")
@cli_util.option('--external-database-identifier', required=True, type=click.INT, help="""The `DBID` of the Oracle Database being backed up.""")
@cli_util.option('--ncharacter-set', required=True, help="""The national character set for the database.""")
@cli_util.option('--db-unique-name', help="""The `DB_UNIQUE_NAME` of the Oracle Database being backed up.""")
@cli_util.option('--pdb-name', help="""The pluggable database name.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'ExternalBackupJob'})
@cli_util.wrap_exceptions
def create_external_backup_job(ctx, from_json, availability_domain, character_set, compartment_id, database_edition, database_mode, db_name, db_version, display_name, external_database_identifier, ncharacter_set, db_unique_name, pdb_name):
    kwargs = {}

    details = {}
    details['availabilityDomain'] = availability_domain
    details['characterSet'] = character_set
    details['compartmentId'] = compartment_id
    details['databaseEdition'] = database_edition
    details['databaseMode'] = database_mode
    details['dbName'] = db_name
    details['dbVersion'] = db_version
    details['displayName'] = display_name
    details['externalDatabaseIdentifier'] = external_database_identifier
    details['ncharacterSet'] = ncharacter_set

    if db_unique_name is not None:
        details['dbUniqueName'] = db_unique_name

    if pdb_name is not None:
        details['pdbName'] = pdb_name

    client = cli_util.build_client('database', ctx)
    result = client.create_external_backup_job(
        create_external_backup_job_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@db_node_group.command(name=cli_util.override('db_node_action.command_name', 'db-node-action'), help="""Performs an action, such as one of the power actions (start, stop, softreset, or reset), on the specified DB Node.

**start** - power on

**stop** - power off

**softreset** - ACPI shutdown and power on

**reset** - power off and power on

Note that the **stop** state has no effect on the resources you consume. Billing continues for DB Nodes that you stop, and related resources continue to apply against any relevant quotas. You must terminate the DB system ([TerminateDbSystem]) to remove its resources from billing and quotas.""")
@cli_util.option('--db-node-id', required=True, help="""The database node [OCID].""")
@cli_util.option('--action', required=True, help="""The action to perform on the DB Node. Allowed values are: STOP, START, SOFTRESET, RESET""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "FAILED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DbNode'})
@cli_util.wrap_exceptions
def db_node_action(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, db_node_id, action, if_match):

    if isinstance(db_node_id, six.string_types) and len(db_node_id.strip()) == 0:
        raise click.UsageError('Parameter --db-node-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('database', ctx)
    result = client.db_node_action(
        db_node_id=db_node_id,
        action=action,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_db_node') and callable(getattr(client, 'get_db_node')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_db_node(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_data_warehouse_group.command(name=cli_util.override('delete_autonomous_data_warehouse.command_name', 'delete'), help="""Deletes the specified Autonomous Data Warehouse.""")
@cli_util.option('--autonomous-data-warehouse-id', required=True, help="""The database [OCID].""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_autonomous_data_warehouse(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, autonomous_data_warehouse_id, if_match):

    if isinstance(autonomous_data_warehouse_id, six.string_types) and len(autonomous_data_warehouse_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-data-warehouse-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('database', ctx)
    result = client.delete_autonomous_data_warehouse(
        autonomous_data_warehouse_id=autonomous_data_warehouse_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_data_warehouse') and callable(getattr(client, 'get_autonomous_data_warehouse')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_autonomous_data_warehouse(autonomous_data_warehouse_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_database_group.command(name=cli_util.override('delete_autonomous_database.command_name', 'delete'), help="""Deletes the specified Autonomous Database.""")
@cli_util.option('--autonomous-database-id', required=True, help="""The database [OCID].""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "RESTORE_FAILED", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_autonomous_database(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, autonomous_database_id, if_match):

    if isinstance(autonomous_database_id, six.string_types) and len(autonomous_database_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-database-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    result = client.delete_autonomous_database(
        autonomous_database_id=autonomous_database_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_database') and callable(getattr(client, 'get_autonomous_database')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_autonomous_database(autonomous_database_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@backup_group.command(name=cli_util.override('delete_backup.command_name', 'delete'), help="""Deletes a full backup. You cannot delete automatic backups using this API.""")
@cli_util.option('--backup-id', required=True, help="""The backup [OCID].""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "RESTORING"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_backup(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, backup_id, if_match):

    if isinstance(backup_id, six.string_types) and len(backup_id.strip()) == 0:
        raise click.UsageError('Parameter --backup-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('database', ctx)
    result = client.delete_backup(
        backup_id=backup_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_backup') and callable(getattr(client, 'get_backup')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_backup(backup_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_home_group.command(name=cli_util.override('delete_db_home.command_name', 'delete'), help="""Deletes a DB Home. The DB Home and its database data are local to the DB system and will be lost when it is deleted. Oracle recommends that you back up any data in the DB system prior to deleting it.""")
@cli_util.option('--db-home-id', required=True, help="""The database home [OCID].""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--perform-final-backup', type=click.BOOL, help="""Whether to perform a final backup of the database or not. Default is false. If you previously used RMAN or dbcli to configure backups and then you switch to using the Console or the API for backups, a new backup configuration is created and associated with your database. This means that you can no longer rely on your previously configured unmanaged backups to work.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_db_home(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, db_home_id, if_match, perform_final_backup):

    if isinstance(db_home_id, six.string_types) and len(db_home_id.strip()) == 0:
        raise click.UsageError('Parameter --db-home-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if perform_final_backup is not None:
        kwargs['perform_final_backup'] = perform_final_backup
    client = cli_util.build_client('database', ctx)
    result = client.delete_db_home(
        db_home_id=db_home_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_db_home') and callable(getattr(client, 'get_db_home')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_db_home(db_home_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@data_guard_association_group.command(name=cli_util.override('failover_data_guard_association.command_name', 'failover'), help="""Performs a failover to transition the standby database identified by the `databaseId` parameter into the specified Data Guard association's primary role after the existing primary database fails or becomes unreachable.

A failover might result in data loss depending on the protection mode in effect at the time of the primary database failure.""")
@cli_util.option('--database-id', required=True, help="""The database [OCID].""")
@cli_util.option('--data-guard-association-id', required=True, help="""The Data Guard association's [OCID].""")
@cli_util.option('--database-admin-password', required=True, help="""The DB system administrator password.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DataGuardAssociation'})
@cli_util.wrap_exceptions
def failover_data_guard_association(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_id, data_guard_association_id, database_admin_password, if_match):

    if isinstance(database_id, six.string_types) and len(database_id.strip()) == 0:
        raise click.UsageError('Parameter --database-id cannot be whitespace or empty string')

    if isinstance(data_guard_association_id, six.string_types) and len(data_guard_association_id.strip()) == 0:
        raise click.UsageError('Parameter --data-guard-association-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}
    details['databaseAdminPassword'] = database_admin_password

    client = cli_util.build_client('database', ctx)
    result = client.failover_data_guard_association(
        database_id=database_id,
        data_guard_association_id=data_guard_association_id,
        failover_data_guard_association_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_data_guard_association') and callable(getattr(client, 'get_data_guard_association')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_guard_association(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_data_warehouse_group.command(name=cli_util.override('generate_autonomous_data_warehouse_wallet.command_name', 'generate-autonomous-data-warehouse-wallet'), help="""Creates and downloads a wallet for the specified Autonomous Data Warehouse.""")
@cli_util.option('--autonomous-data-warehouse-id', required=True, help="""The database [OCID].""")
@cli_util.option('--password', required=True, help="""The password to encrypt the keys inside the wallet.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def generate_autonomous_data_warehouse_wallet(ctx, from_json, file, autonomous_data_warehouse_id, password):

    if isinstance(autonomous_data_warehouse_id, six.string_types) and len(autonomous_data_warehouse_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-data-warehouse-id cannot be whitespace or empty string')
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['password'] = password

    client = cli_util.build_client('database', ctx)
    result = client.generate_autonomous_data_warehouse_wallet(
        autonomous_data_warehouse_id=autonomous_data_warehouse_id,
        generate_autonomous_data_warehouse_wallet_details=details,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@autonomous_database_group.command(name=cli_util.override('generate_autonomous_database_wallet.command_name', 'generate-autonomous-database-wallet'), help="""Creates and downloads a wallet for the specified Autonomous Transaction Processing database.""")
@cli_util.option('--autonomous-database-id', required=True, help="""The database [OCID].""")
@cli_util.option('--password', required=True, help="""The password to encrypt the keys inside the wallet.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def generate_autonomous_database_wallet(ctx, from_json, file, autonomous_database_id, password):

    if isinstance(autonomous_database_id, six.string_types) and len(autonomous_database_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-database-id cannot be whitespace or empty string')
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['password'] = password

    client = cli_util.build_client('database', ctx)
    result = client.generate_autonomous_database_wallet(
        autonomous_database_id=autonomous_database_id,
        generate_autonomous_database_wallet_details=details,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@autonomous_data_warehouse_group.command(name=cli_util.override('get_autonomous_data_warehouse.command_name', 'get'), help="""Gets the details of the specified Autonomous Data Warehouse.""")
@cli_util.option('--autonomous-data-warehouse-id', required=True, help="""The database [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'AutonomousDataWarehouse'})
@cli_util.wrap_exceptions
def get_autonomous_data_warehouse(ctx, from_json, autonomous_data_warehouse_id):

    if isinstance(autonomous_data_warehouse_id, six.string_types) and len(autonomous_data_warehouse_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-data-warehouse-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_autonomous_data_warehouse(
        autonomous_data_warehouse_id=autonomous_data_warehouse_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@autonomous_data_warehouse_backup_group.command(name=cli_util.override('get_autonomous_data_warehouse_backup.command_name', 'get'), help="""Gets information about the specified Autonomous Data Warehouse backup.""")
@cli_util.option('--autonomous-data-warehouse-backup-id', required=True, help="""The [OCID] of the Autonomous Data Warehouse backup.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'AutonomousDataWarehouseBackup'})
@cli_util.wrap_exceptions
def get_autonomous_data_warehouse_backup(ctx, from_json, autonomous_data_warehouse_backup_id):

    if isinstance(autonomous_data_warehouse_backup_id, six.string_types) and len(autonomous_data_warehouse_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-data-warehouse-backup-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_autonomous_data_warehouse_backup(
        autonomous_data_warehouse_backup_id=autonomous_data_warehouse_backup_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@autonomous_database_group.command(name=cli_util.override('get_autonomous_database.command_name', 'get'), help="""Gets the details of the specified Autonomous Database.""")
@cli_util.option('--autonomous-database-id', required=True, help="""The database [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'AutonomousDatabase'})
@cli_util.wrap_exceptions
def get_autonomous_database(ctx, from_json, autonomous_database_id):

    if isinstance(autonomous_database_id, six.string_types) and len(autonomous_database_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-database-id cannot be whitespace or empty string')
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    result = client.get_autonomous_database(
        autonomous_database_id=autonomous_database_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@autonomous_database_backup_group.command(name=cli_util.override('get_autonomous_database_backup.command_name', 'get'), help="""Gets information about the specified Autonomous Database backup.""")
@cli_util.option('--autonomous-database-backup-id', required=True, help="""The [OCID] of the Autonomous Database backup.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'AutonomousDatabaseBackup'})
@cli_util.wrap_exceptions
def get_autonomous_database_backup(ctx, from_json, autonomous_database_backup_id):

    if isinstance(autonomous_database_backup_id, six.string_types) and len(autonomous_database_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-database-backup-id cannot be whitespace or empty string')
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    result = client.get_autonomous_database_backup(
        autonomous_database_backup_id=autonomous_database_backup_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@backup_group.command(name=cli_util.override('get_backup.command_name', 'get'), help="""Gets information about the specified backup.""")
@cli_util.option('--backup-id', required=True, help="""The backup [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'Backup'})
@cli_util.wrap_exceptions
def get_backup(ctx, from_json, backup_id):

    if isinstance(backup_id, six.string_types) and len(backup_id.strip()) == 0:
        raise click.UsageError('Parameter --backup-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_backup(
        backup_id=backup_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_guard_association_group.command(name=cli_util.override('get_data_guard_association.command_name', 'get'), help="""Gets the specified Data Guard association's configuration information.""")
@cli_util.option('--database-id', required=True, help="""The database [OCID].""")
@cli_util.option('--data-guard-association-id', required=True, help="""The Data Guard association's [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DataGuardAssociation'})
@cli_util.wrap_exceptions
def get_data_guard_association(ctx, from_json, database_id, data_guard_association_id):

    if isinstance(database_id, six.string_types) and len(database_id.strip()) == 0:
        raise click.UsageError('Parameter --database-id cannot be whitespace or empty string')

    if isinstance(data_guard_association_id, six.string_types) and len(data_guard_association_id.strip()) == 0:
        raise click.UsageError('Parameter --data-guard-association-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_data_guard_association(
        database_id=database_id,
        data_guard_association_id=data_guard_association_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_group.command(name=cli_util.override('get_database.command_name', 'get'), help="""Gets information about a specific database.""")
@cli_util.option('--database-id', required=True, help="""The database [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'Database'})
@cli_util.wrap_exceptions
def get_database(ctx, from_json, database_id):

    if isinstance(database_id, six.string_types) and len(database_id.strip()) == 0:
        raise click.UsageError('Parameter --database-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_database(
        database_id=database_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@db_home_group.command(name=cli_util.override('get_db_home.command_name', 'get'), help="""Gets information about the specified database home.""")
@cli_util.option('--db-home-id', required=True, help="""The database home [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DbHome'})
@cli_util.wrap_exceptions
def get_db_home(ctx, from_json, db_home_id):

    if isinstance(db_home_id, six.string_types) and len(db_home_id.strip()) == 0:
        raise click.UsageError('Parameter --db-home-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_db_home(
        db_home_id=db_home_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@patch_group.command(name=cli_util.override('get_db_home_patch.command_name', 'get-db-home'), help="""Gets information about a specified patch package.""")
@cli_util.option('--db-home-id', required=True, help="""The database home [OCID].""")
@cli_util.option('--patch-id', required=True, help="""The [OCID] of the patch.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'Patch'})
@cli_util.wrap_exceptions
def get_db_home_patch(ctx, from_json, db_home_id, patch_id):

    if isinstance(db_home_id, six.string_types) and len(db_home_id.strip()) == 0:
        raise click.UsageError('Parameter --db-home-id cannot be whitespace or empty string')

    if isinstance(patch_id, six.string_types) and len(patch_id.strip()) == 0:
        raise click.UsageError('Parameter --patch-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_db_home_patch(
        db_home_id=db_home_id,
        patch_id=patch_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@patch_history_entry_group.command(name=cli_util.override('get_db_home_patch_history_entry.command_name', 'get-db-home'), help="""Gets the patch history details for the specified patchHistoryEntryId""")
@cli_util.option('--db-home-id', required=True, help="""The database home [OCID].""")
@cli_util.option('--patch-history-entry-id', required=True, help="""The [OCID] of the patch history entry.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'PatchHistoryEntry'})
@cli_util.wrap_exceptions
def get_db_home_patch_history_entry(ctx, from_json, db_home_id, patch_history_entry_id):

    if isinstance(db_home_id, six.string_types) and len(db_home_id.strip()) == 0:
        raise click.UsageError('Parameter --db-home-id cannot be whitespace or empty string')

    if isinstance(patch_history_entry_id, six.string_types) and len(patch_history_entry_id.strip()) == 0:
        raise click.UsageError('Parameter --patch-history-entry-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_db_home_patch_history_entry(
        db_home_id=db_home_id,
        patch_history_entry_id=patch_history_entry_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@db_node_group.command(name=cli_util.override('get_db_node.command_name', 'get'), help="""Gets information about the specified database node.""")
@cli_util.option('--db-node-id', required=True, help="""The database node [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DbNode'})
@cli_util.wrap_exceptions
def get_db_node(ctx, from_json, db_node_id):

    if isinstance(db_node_id, six.string_types) and len(db_node_id.strip()) == 0:
        raise click.UsageError('Parameter --db-node-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_db_node(
        db_node_id=db_node_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@db_system_group.command(name=cli_util.override('get_db_system.command_name', 'get'), help="""Gets information about the specified DB system.""")
@cli_util.option('--db-system-id', required=True, help="""The DB system [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def get_db_system(ctx, from_json, db_system_id):

    if isinstance(db_system_id, six.string_types) and len(db_system_id.strip()) == 0:
        raise click.UsageError('Parameter --db-system-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_db_system(
        db_system_id=db_system_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@patch_group.command(name=cli_util.override('get_db_system_patch.command_name', 'get-db-system'), help="""Gets information about a specified patch package.""")
@cli_util.option('--db-system-id', required=True, help="""The DB system [OCID].""")
@cli_util.option('--patch-id', required=True, help="""The [OCID] of the patch.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'Patch'})
@cli_util.wrap_exceptions
def get_db_system_patch(ctx, from_json, db_system_id, patch_id):

    if isinstance(db_system_id, six.string_types) and len(db_system_id.strip()) == 0:
        raise click.UsageError('Parameter --db-system-id cannot be whitespace or empty string')

    if isinstance(patch_id, six.string_types) and len(patch_id.strip()) == 0:
        raise click.UsageError('Parameter --patch-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_db_system_patch(
        db_system_id=db_system_id,
        patch_id=patch_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@patch_history_entry_group.command(name=cli_util.override('get_db_system_patch_history_entry.command_name', 'get-db-system'), help="""Gets the patch history details for the specified patchHistoryEntryId.""")
@cli_util.option('--db-system-id', required=True, help="""The DB system [OCID].""")
@cli_util.option('--patch-history-entry-id', required=True, help="""The [OCID] of the patch history entry.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'PatchHistoryEntry'})
@cli_util.wrap_exceptions
def get_db_system_patch_history_entry(ctx, from_json, db_system_id, patch_history_entry_id):

    if isinstance(db_system_id, six.string_types) and len(db_system_id.strip()) == 0:
        raise click.UsageError('Parameter --db-system-id cannot be whitespace or empty string')

    if isinstance(patch_history_entry_id, six.string_types) and len(patch_history_entry_id.strip()) == 0:
        raise click.UsageError('Parameter --patch-history-entry-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_db_system_patch_history_entry(
        db_system_id=db_system_id,
        patch_history_entry_id=patch_history_entry_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@external_backup_job_group.command(name=cli_util.override('get_external_backup_job.command_name', 'get'), help="""Gets information about the specified external backup job.

**Note:** This API is used by an Oracle Cloud Infrastructure Python script that is packaged with the Oracle Cloud Infrastructure CLI. Oracle recommends that you use the script instead using the API directly. See [Migrating an On-Premises Database to Oracle Cloud Infrastructure by Creating a Backup in the Cloud] for more information.""")
@cli_util.option('--backup-id', required=True, help="""The backup [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'ExternalBackupJob'})
@cli_util.wrap_exceptions
def get_external_backup_job(ctx, from_json, backup_id):

    if isinstance(backup_id, six.string_types) and len(backup_id.strip()) == 0:
        raise click.UsageError('Parameter --backup-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_external_backup_job(
        backup_id=backup_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@db_system_group.command(name=cli_util.override('launch_db_system.command_name', 'launch'), help="""Launches a new DB system in the specified compartment and availability domain. The Oracle Database edition that you specify applies to all the databases on that DB system. The selected edition cannot be changed.

An initial database is created on the DB system based on the request parameters you provide and some default options. For more information, see [Default Options for the Initial Database].""")
@cli_util.option('--availability-domain', required=True, help="""The availability domain where the DB system is located.""")
@cli_util.option('--compartment-id', required=True, help="""The [OCID] of the compartment the DB system  belongs in.""")
@cli_util.option('--cpu-core-count', required=True, type=click.INT, help="""The number of CPU cores to enable for a bare metal or Exadata DB system. The valid values depend on the specified shape:

- BM.DenseIO1.36 - Specify a multiple of 2, from 2 to 36. - BM.DenseIO2.52 - Specify a multiple of 2, from 2 to 52. - Exadata.Quarter1.84 - Specify a multiple of 2, from 22 to 84. - Exadata.Half1.168 - Specify a multiple of 4, from 44 to 168. - Exadata.Full1.336 - Specify a multiple of 8, from 88 to 336. - Exadata.Quarter2.92 - Specify a multiple of 2, from 0 to 92. - Exadata.Half2.184 - Specify a multiple of 4, from 0 to 184. - Exadata.Full2.368 - Specify a multiple of 8, from 0 to 368.

This parameter is not used for virtual machine DB systems because virtual machine DB systems have a set number of cores for each shape. For information about the number of cores for a virtual machine DB system shape, see [Virtual Machine DB Systems]""")
@cli_util.option('--hostname', required=True, help="""The hostname for the DB system. The hostname must begin with an alphabetic character and can contain a maximum of 30 alphanumeric characters, including hyphens (-).

The maximum length of the combined hostname and domain is 63 characters.

**Note:** The hostname must be unique within the subnet. If it is not unique, the DB system will fail to provision.""")
@cli_util.option('--shape', required=True, help="""The shape of the DB system. The shape determines resources allocated to the DB system. - For virtual machine shapes, the number of CPU cores and memory - For bare metal and Exadata shapes, the number of CPU cores, memory, and storage

To get a list of shapes, use the [ListDbSystemShapes] operation.""")
@cli_util.option('--ssh-public-keys', required=True, type=custom_types.CLI_COMPLEX_TYPE, help="""The public key portion of the key pair to use for SSH access to the DB system. Multiple public keys can be provided. The length of the combined keys cannot exceed 10,000 characters.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--subnet-id', required=True, help="""The [OCID] of the subnet the DB system is associated with.

**Subnet Restrictions:** - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28. - For Exadata and virtual machine 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.128.0/20.

These subnets are used by the Oracle Clusterware private interconnect on the database instance. Specifying an overlapping subnet will cause the private interconnect to malfunction. This restriction applies to both the client subnet and the backup subnet.""")
@cli_util.option('--backup-subnet-id', help="""The [OCID] of the backup network subnet the DB system is associated with. Applicable only to Exadata DB systems.

**Subnet Restrictions:** See the subnet restrictions information for **subnetId**.""")
@cli_util.option('--cluster-name', help="""The cluster name for Exadata and 2-node RAC virtual machine DB systems. The cluster name must begin with an an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.""")
@cli_util.option('--data-storage-percentage', type=click.INT, help="""The percentage assigned to DATA storage (user data and database files). The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Specify 80 or 40. The default is 80 percent assigned to DATA storage. Not applicable for virtual machine DB systems.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""The user-friendly name for the DB system. The name does not have to be unique.""")
@cli_util.option('--domain', help="""A domain name used for the DB system. If the Oracle-provided Internet and VCN Resolver is enabled for the specified subnet, the domain name for the subnet is used (do not provide one). Otherwise, provide a valid DNS domain name. Hyphens (-) are not permitted.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--initial-data-storage-size-in-gb', type=click.INT, help="""Size (in GB) of the initial data volume that will be created and attached to a virtual machine DB system. You can scale up storage after provisioning, as needed. Note that the total storage size attached will be more than the amount you specify to allow for REDO/RECO space and software volume.""")
@cli_util.option('--node-count', type=click.INT, help="""The number of nodes to launch for a 2-node RAC virtual machine DB system.""")
@cli_util.option('--source', type=custom_types.CliCaseInsensitiveChoice(["NONE", "DB_BACKUP"]), help="""The source of the database:   NONE for creating a new database. DB_BACKUP for creating a new database by restoring from a backup. The default is NONE.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}}, output_type={'module': 'database', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def launch_db_system(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, compartment_id, cpu_core_count, hostname, shape, ssh_public_keys, subnet_id, backup_subnet_id, cluster_name, data_storage_percentage, defined_tags, display_name, domain, freeform_tags, initial_data_storage_size_in_gb, node_count, source):
    kwargs = {}

    details = {}
    details['availabilityDomain'] = availability_domain
    details['compartmentId'] = compartment_id
    details['cpuCoreCount'] = cpu_core_count
    details['hostname'] = hostname
    details['shape'] = shape
    details['sshPublicKeys'] = cli_util.parse_json_parameter("ssh_public_keys", ssh_public_keys)
    details['subnetId'] = subnet_id

    if backup_subnet_id is not None:
        details['backupSubnetId'] = backup_subnet_id

    if cluster_name is not None:
        details['clusterName'] = cluster_name

    if data_storage_percentage is not None:
        details['dataStoragePercentage'] = data_storage_percentage

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if domain is not None:
        details['domain'] = domain

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if initial_data_storage_size_in_gb is not None:
        details['initialDataStorageSizeInGB'] = initial_data_storage_size_in_gb

    if node_count is not None:
        details['nodeCount'] = node_count

    if source is not None:
        details['source'] = source

    client = cli_util.build_client('database', ctx)
    result = client.launch_db_system(
        launch_db_system_details=details,
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

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_db_system(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_system_group.command(name=cli_util.override('launch_db_system_launch_db_system_details.command_name', 'launch-db-system-launch-db-system-details'), help="""Launches a new DB system in the specified compartment and availability domain. The Oracle Database edition that you specify applies to all the databases on that DB system. The selected edition cannot be changed.

An initial database is created on the DB system based on the request parameters you provide and some default options. For more information, see [Default Options for the Initial Database].""")
@cli_util.option('--availability-domain', required=True, help="""The availability domain where the DB system is located.""")
@cli_util.option('--compartment-id', required=True, help="""The [OCID] of the compartment the DB system  belongs in.""")
@cli_util.option('--cpu-core-count', required=True, type=click.INT, help="""The number of CPU cores to enable for a bare metal or Exadata DB system. The valid values depend on the specified shape:

- BM.DenseIO1.36 - Specify a multiple of 2, from 2 to 36. - BM.DenseIO2.52 - Specify a multiple of 2, from 2 to 52. - Exadata.Quarter1.84 - Specify a multiple of 2, from 22 to 84. - Exadata.Half1.168 - Specify a multiple of 4, from 44 to 168. - Exadata.Full1.336 - Specify a multiple of 8, from 88 to 336. - Exadata.Quarter2.92 - Specify a multiple of 2, from 0 to 92. - Exadata.Half2.184 - Specify a multiple of 4, from 0 to 184. - Exadata.Full2.368 - Specify a multiple of 8, from 0 to 368.

This parameter is not used for virtual machine DB systems because virtual machine DB systems have a set number of cores for each shape. For information about the number of cores for a virtual machine DB system shape, see [Virtual Machine DB Systems]""")
@cli_util.option('--hostname', required=True, help="""The hostname for the DB system. The hostname must begin with an alphabetic character and can contain a maximum of 30 alphanumeric characters, including hyphens (-).

The maximum length of the combined hostname and domain is 63 characters.

**Note:** The hostname must be unique within the subnet. If it is not unique, the DB system will fail to provision.""")
@cli_util.option('--shape', required=True, help="""The shape of the DB system. The shape determines resources allocated to the DB system. - For virtual machine shapes, the number of CPU cores and memory - For bare metal and Exadata shapes, the number of CPU cores, memory, and storage

To get a list of shapes, use the [ListDbSystemShapes] operation.""")
@cli_util.option('--ssh-public-keys', required=True, type=custom_types.CLI_COMPLEX_TYPE, help="""The public key portion of the key pair to use for SSH access to the DB system. Multiple public keys can be provided. The length of the combined keys cannot exceed 10,000 characters.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--subnet-id', required=True, help="""The [OCID] of the subnet the DB system is associated with.

**Subnet Restrictions:** - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28. - For Exadata and virtual machine 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.128.0/20.

These subnets are used by the Oracle Clusterware private interconnect on the database instance. Specifying an overlapping subnet will cause the private interconnect to malfunction. This restriction applies to both the client subnet and the backup subnet.""")
@cli_util.option('--database-edition', required=True, type=custom_types.CliCaseInsensitiveChoice(["STANDARD_EDITION", "ENTERPRISE_EDITION", "ENTERPRISE_EDITION_HIGH_PERFORMANCE", "ENTERPRISE_EDITION_EXTREME_PERFORMANCE"]), help="""The Oracle Database Edition that applies to all the databases on the DB system. Exadata DB systems and 2-node RAC DB systems require ENTERPRISE_EDITION_EXTREME_PERFORMANCE.""")
@cli_util.option('--db-home', required=True, type=custom_types.CLI_COMPLEX_TYPE, help="""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--backup-subnet-id', help="""The [OCID] of the backup network subnet the DB system is associated with. Applicable only to Exadata DB systems.

**Subnet Restrictions:** See the subnet restrictions information for **subnetId**.""")
@cli_util.option('--cluster-name', help="""The cluster name for Exadata and 2-node RAC virtual machine DB systems. The cluster name must begin with an an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.""")
@cli_util.option('--data-storage-percentage', type=click.INT, help="""The percentage assigned to DATA storage (user data and database files). The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Specify 80 or 40. The default is 80 percent assigned to DATA storage. Not applicable for virtual machine DB systems.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""The user-friendly name for the DB system. The name does not have to be unique.""")
@cli_util.option('--domain', help="""A domain name used for the DB system. If the Oracle-provided Internet and VCN Resolver is enabled for the specified subnet, the domain name for the subnet is used (do not provide one). Otherwise, provide a valid DNS domain name. Hyphens (-) are not permitted.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--initial-data-storage-size-in-gb', type=click.INT, help="""Size (in GB) of the initial data volume that will be created and attached to a virtual machine DB system. You can scale up storage after provisioning, as needed. Note that the total storage size attached will be more than the amount you specify to allow for REDO/RECO space and software volume.""")
@cli_util.option('--node-count', type=click.INT, help="""The number of nodes to launch for a 2-node RAC virtual machine DB system.""")
@cli_util.option('--disk-redundancy', type=custom_types.CliCaseInsensitiveChoice(["HIGH", "NORMAL"]), help="""The type of redundancy configured for the DB system. Normal is 2-way redundancy, recommended for test and development systems. High is 3-way redundancy, recommended for production systems.""")
@cli_util.option('--license-model', type=custom_types.CliCaseInsensitiveChoice(["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]), help="""The Oracle license model that applies to all the databases on the DB system. The default is LICENSE_INCLUDED.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}, 'db-home': {'module': 'database', 'class': 'CreateDbHomeDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}, 'db-home': {'module': 'database', 'class': 'CreateDbHomeDetails'}}, output_type={'module': 'database', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def launch_db_system_launch_db_system_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, compartment_id, cpu_core_count, hostname, shape, ssh_public_keys, subnet_id, database_edition, db_home, backup_subnet_id, cluster_name, data_storage_percentage, defined_tags, display_name, domain, freeform_tags, initial_data_storage_size_in_gb, node_count, disk_redundancy, license_model):
    kwargs = {}

    details = {}
    details['availabilityDomain'] = availability_domain
    details['compartmentId'] = compartment_id
    details['cpuCoreCount'] = cpu_core_count
    details['hostname'] = hostname
    details['shape'] = shape
    details['sshPublicKeys'] = cli_util.parse_json_parameter("ssh_public_keys", ssh_public_keys)
    details['subnetId'] = subnet_id
    details['databaseEdition'] = database_edition
    details['dbHome'] = cli_util.parse_json_parameter("db_home", db_home)

    if backup_subnet_id is not None:
        details['backupSubnetId'] = backup_subnet_id

    if cluster_name is not None:
        details['clusterName'] = cluster_name

    if data_storage_percentage is not None:
        details['dataStoragePercentage'] = data_storage_percentage

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if domain is not None:
        details['domain'] = domain

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if initial_data_storage_size_in_gb is not None:
        details['initialDataStorageSizeInGB'] = initial_data_storage_size_in_gb

    if node_count is not None:
        details['nodeCount'] = node_count

    if disk_redundancy is not None:
        details['diskRedundancy'] = disk_redundancy

    if license_model is not None:
        details['licenseModel'] = license_model

    details['source'] = 'NONE'

    client = cli_util.build_client('database', ctx)
    result = client.launch_db_system(
        launch_db_system_details=details,
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

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_db_system(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_system_group.command(name=cli_util.override('launch_db_system_launch_db_system_from_backup_details.command_name', 'launch-db-system-launch-db-system-from-backup-details'), help="""Launches a new DB system in the specified compartment and availability domain. The Oracle Database edition that you specify applies to all the databases on that DB system. The selected edition cannot be changed.

An initial database is created on the DB system based on the request parameters you provide and some default options. For more information, see [Default Options for the Initial Database].""")
@cli_util.option('--availability-domain', required=True, help="""The availability domain where the DB system is located.""")
@cli_util.option('--compartment-id', required=True, help="""The [OCID] of the compartment the DB system  belongs in.""")
@cli_util.option('--cpu-core-count', required=True, type=click.INT, help="""The number of CPU cores to enable for a bare metal or Exadata DB system. The valid values depend on the specified shape:

- BM.DenseIO1.36 - Specify a multiple of 2, from 2 to 36. - BM.DenseIO2.52 - Specify a multiple of 2, from 2 to 52. - Exadata.Quarter1.84 - Specify a multiple of 2, from 22 to 84. - Exadata.Half1.168 - Specify a multiple of 4, from 44 to 168. - Exadata.Full1.336 - Specify a multiple of 8, from 88 to 336. - Exadata.Quarter2.92 - Specify a multiple of 2, from 0 to 92. - Exadata.Half2.184 - Specify a multiple of 4, from 0 to 184. - Exadata.Full2.368 - Specify a multiple of 8, from 0 to 368.

This parameter is not used for virtual machine DB systems because virtual machine DB systems have a set number of cores for each shape. For information about the number of cores for a virtual machine DB system shape, see [Virtual Machine DB Systems]""")
@cli_util.option('--hostname', required=True, help="""The hostname for the DB system. The hostname must begin with an alphabetic character and can contain a maximum of 30 alphanumeric characters, including hyphens (-).

The maximum length of the combined hostname and domain is 63 characters.

**Note:** The hostname must be unique within the subnet. If it is not unique, the DB system will fail to provision.""")
@cli_util.option('--shape', required=True, help="""The shape of the DB system. The shape determines resources allocated to the DB system. - For virtual machine shapes, the number of CPU cores and memory - For bare metal and Exadata shapes, the number of CPU cores, memory, and storage

To get a list of shapes, use the [ListDbSystemShapes] operation.""")
@cli_util.option('--ssh-public-keys', required=True, type=custom_types.CLI_COMPLEX_TYPE, help="""The public key portion of the key pair to use for SSH access to the DB system. Multiple public keys can be provided. The length of the combined keys cannot exceed 10,000 characters.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--subnet-id', required=True, help="""The [OCID] of the subnet the DB system is associated with.

**Subnet Restrictions:** - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28. - For Exadata and virtual machine 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.128.0/20.

These subnets are used by the Oracle Clusterware private interconnect on the database instance. Specifying an overlapping subnet will cause the private interconnect to malfunction. This restriction applies to both the client subnet and the backup subnet.""")
@cli_util.option('--database-edition', required=True, type=custom_types.CliCaseInsensitiveChoice(["STANDARD_EDITION", "ENTERPRISE_EDITION", "ENTERPRISE_EDITION_HIGH_PERFORMANCE", "ENTERPRISE_EDITION_EXTREME_PERFORMANCE"]), help="""The Oracle Database Edition that applies to all the databases on the DB system. Exadata DB systems and 2-node RAC DB systems require ENTERPRISE_EDITION_EXTREME_PERFORMANCE.""")
@cli_util.option('--db-home', required=True, type=custom_types.CLI_COMPLEX_TYPE, help="""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--backup-subnet-id', help="""The [OCID] of the backup network subnet the DB system is associated with. Applicable only to Exadata DB systems.

**Subnet Restrictions:** See the subnet restrictions information for **subnetId**.""")
@cli_util.option('--cluster-name', help="""The cluster name for Exadata and 2-node RAC virtual machine DB systems. The cluster name must begin with an an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.""")
@cli_util.option('--data-storage-percentage', type=click.INT, help="""The percentage assigned to DATA storage (user data and database files). The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Specify 80 or 40. The default is 80 percent assigned to DATA storage. Not applicable for virtual machine DB systems.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""The user-friendly name for the DB system. The name does not have to be unique.""")
@cli_util.option('--domain', help="""A domain name used for the DB system. If the Oracle-provided Internet and VCN Resolver is enabled for the specified subnet, the domain name for the subnet is used (do not provide one). Otherwise, provide a valid DNS domain name. Hyphens (-) are not permitted.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--initial-data-storage-size-in-gb', type=click.INT, help="""Size (in GB) of the initial data volume that will be created and attached to a virtual machine DB system. You can scale up storage after provisioning, as needed. Note that the total storage size attached will be more than the amount you specify to allow for REDO/RECO space and software volume.""")
@cli_util.option('--node-count', type=click.INT, help="""The number of nodes to launch for a 2-node RAC virtual machine DB system.""")
@cli_util.option('--disk-redundancy', type=custom_types.CliCaseInsensitiveChoice(["HIGH", "NORMAL"]), help="""The type of redundancy configured for the DB system. NORMAL 2-way redundancy, recommended for test and development systems. HIGH is 3-way redundancy, recommended for production systems.""")
@cli_util.option('--license-model', type=custom_types.CliCaseInsensitiveChoice(["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]), help="""The Oracle license model that applies to all the databases on the DB system. The default is LICENSE_INCLUDED.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}, 'db-home': {'module': 'database', 'class': 'CreateDbHomeFromBackupDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}, 'db-home': {'module': 'database', 'class': 'CreateDbHomeFromBackupDetails'}}, output_type={'module': 'database', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def launch_db_system_launch_db_system_from_backup_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, compartment_id, cpu_core_count, hostname, shape, ssh_public_keys, subnet_id, database_edition, db_home, backup_subnet_id, cluster_name, data_storage_percentage, defined_tags, display_name, domain, freeform_tags, initial_data_storage_size_in_gb, node_count, disk_redundancy, license_model):
    kwargs = {}

    details = {}
    details['availabilityDomain'] = availability_domain
    details['compartmentId'] = compartment_id
    details['cpuCoreCount'] = cpu_core_count
    details['hostname'] = hostname
    details['shape'] = shape
    details['sshPublicKeys'] = cli_util.parse_json_parameter("ssh_public_keys", ssh_public_keys)
    details['subnetId'] = subnet_id
    details['databaseEdition'] = database_edition
    details['dbHome'] = cli_util.parse_json_parameter("db_home", db_home)

    if backup_subnet_id is not None:
        details['backupSubnetId'] = backup_subnet_id

    if cluster_name is not None:
        details['clusterName'] = cluster_name

    if data_storage_percentage is not None:
        details['dataStoragePercentage'] = data_storage_percentage

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if domain is not None:
        details['domain'] = domain

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if initial_data_storage_size_in_gb is not None:
        details['initialDataStorageSizeInGB'] = initial_data_storage_size_in_gb

    if node_count is not None:
        details['nodeCount'] = node_count

    if disk_redundancy is not None:
        details['diskRedundancy'] = disk_redundancy

    if license_model is not None:
        details['licenseModel'] = license_model

    details['source'] = 'DB_BACKUP'

    client = cli_util.build_client('database', ctx)
    result = client.launch_db_system(
        launch_db_system_details=details,
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

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_db_system(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_data_warehouse_backup_group.command(name=cli_util.override('list_autonomous_data_warehouse_backups.command_name', 'list'), help="""Gets a list of Autonomous Data Warehouse backups based on either the `autonomousDataWarehouseId` or `compartmentId` specified as a query parameter.""")
@cli_util.option('--autonomous-data-warehouse-id', help="""The database [OCID].""")
@cli_util.option('--compartment-id', help="""The compartment [OCID].""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return per page.""")
@cli_util.option('--page', help="""The pagination token to continue listing from.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help="""A filter to return only resources that match the given lifecycle state exactly.""")
@cli_util.option('--display-name', help="""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[AutonomousDataWarehouseBackupSummary]'})
@cli_util.wrap_exceptions
def list_autonomous_data_warehouse_backups(ctx, from_json, all_pages, page_size, autonomous_data_warehouse_id, compartment_id, limit, page, sort_by, sort_order, lifecycle_state, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if autonomous_data_warehouse_id is not None:
        kwargs['autonomous_data_warehouse_id'] = autonomous_data_warehouse_id
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_autonomous_data_warehouse_backups,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_autonomous_data_warehouse_backups,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_autonomous_data_warehouse_backups(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@autonomous_data_warehouse_group.command(name=cli_util.override('list_autonomous_data_warehouses.command_name', 'list'), help="""Gets a list of Autonomous Data Warehouses.""")
@cli_util.option('--compartment-id', required=True, help="""The compartment [OCID].""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return per page.""")
@cli_util.option('--page', help="""The pagination token to continue listing from.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION"]), help="""A filter to return only resources that match the given lifecycle state exactly.""")
@cli_util.option('--display-name', help="""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[AutonomousDataWarehouseSummary]'})
@cli_util.wrap_exceptions
def list_autonomous_data_warehouses(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_by, sort_order, lifecycle_state, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_autonomous_data_warehouses,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_autonomous_data_warehouses,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_autonomous_data_warehouses(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@autonomous_database_backup_group.command(name=cli_util.override('list_autonomous_database_backups.command_name', 'list'), help="""Gets a list of Autonomous Database backups based on either the `autonomousDatabaseId` or `compartmentId` specified as a query parameter.""")
@cli_util.option('--autonomous-database-id', help="""The database [OCID].""")
@cli_util.option('--compartment-id', help="""The compartment [OCID].""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return per page.""")
@cli_util.option('--page', help="""The pagination token to continue listing from.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help="""A filter to return only resources that match the given lifecycle state exactly.""")
@cli_util.option('--display-name', help="""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[AutonomousDatabaseBackupSummary]'})
@cli_util.wrap_exceptions
def list_autonomous_database_backups(ctx, from_json, all_pages, page_size, autonomous_database_id, compartment_id, limit, page, sort_by, sort_order, lifecycle_state, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if autonomous_database_id is not None:
        kwargs['autonomous_database_id'] = autonomous_database_id
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_autonomous_database_backups,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_autonomous_database_backups,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_autonomous_database_backups(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@autonomous_database_group.command(name=cli_util.override('list_autonomous_databases.command_name', 'list'), help="""Gets a list of Autonomous Databases.""")
@cli_util.option('--compartment-id', required=True, help="""The compartment [OCID].""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return per page.""")
@cli_util.option('--page', help="""The pagination token to continue listing from.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "RESTORE_FAILED", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION"]), help="""A filter to return only resources that match the given lifecycle state exactly.""")
@cli_util.option('--display-name', help="""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[AutonomousDatabaseSummary]'})
@cli_util.wrap_exceptions
def list_autonomous_databases(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_by, sort_order, lifecycle_state, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_autonomous_databases,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_autonomous_databases,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_autonomous_databases(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@backup_group.command(name=cli_util.override('list_backups.command_name', 'list'), help="""Gets a list of backups based on the databaseId or compartmentId specified. Either one of the query parameters must be provided.""")
@cli_util.option('--database-id', help="""The [OCID] of the database.""")
@cli_util.option('--compartment-id', help="""The compartment [OCID].""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return per page.""")
@cli_util.option('--page', help="""The pagination token to continue listing from.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[BackupSummary]'})
@cli_util.wrap_exceptions
def list_backups(ctx, from_json, all_pages, page_size, database_id, compartment_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if database_id is not None:
        kwargs['database_id'] = database_id
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_backups,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_backups,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_backups(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@data_guard_association_group.command(name=cli_util.override('list_data_guard_associations.command_name', 'list'), help="""Lists all Data Guard associations for the specified database.""")
@cli_util.option('--database-id', required=True, help="""The database [OCID].""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return per page.""")
@cli_util.option('--page', help="""The pagination token to continue listing from.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[DataGuardAssociationSummary]'})
@cli_util.wrap_exceptions
def list_data_guard_associations(ctx, from_json, all_pages, page_size, database_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(database_id, six.string_types) and len(database_id.strip()) == 0:
        raise click.UsageError('Parameter --database-id cannot be whitespace or empty string')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_data_guard_associations,
            database_id=database_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_data_guard_associations,
            limit,
            page_size,
            database_id=database_id,
            **kwargs
        )
    else:
        result = client.list_data_guard_associations(
            database_id=database_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@database_group.command(name=cli_util.override('list_databases.command_name', 'list'), help="""Gets a list of the databases in the specified database home.""")
@cli_util.option('--compartment-id', required=True, help="""The compartment [OCID].""")
@cli_util.option('--db-home-id', required=True, help="""A database home [OCID].""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return per page.""")
@cli_util.option('--page', help="""The pagination token to continue listing from.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["DBNAME", "TIMECREATED"]), help="""The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DBNAME is ascending. The DBNAME sort order is case sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "BACKUP_IN_PROGRESS", "TERMINATING", "TERMINATED", "RESTORE_FAILED", "FAILED"]), help="""A filter to return only resources that match the given lifecycle state exactly.""")
@cli_util.option('--db-name', help="""A filter to return only resources that match the entire database name given. The match is not case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[DatabaseSummary]'})
@cli_util.wrap_exceptions
def list_databases(ctx, from_json, all_pages, page_size, compartment_id, db_home_id, limit, page, sort_by, sort_order, lifecycle_state, db_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if db_name is not None:
        kwargs['db_name'] = db_name
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_databases,
            compartment_id=compartment_id,
            db_home_id=db_home_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_databases,
            limit,
            page_size,
            compartment_id=compartment_id,
            db_home_id=db_home_id,
            **kwargs
        )
    else:
        result = client.list_databases(
            compartment_id=compartment_id,
            db_home_id=db_home_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@patch_history_entry_group.command(name=cli_util.override('list_db_home_patch_history_entries.command_name', 'list-db-home'), help="""Gets history of the actions taken for patches for the specified database home.""")
@cli_util.option('--db-home-id', required=True, help="""The database home [OCID].""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return per page.""")
@cli_util.option('--page', help="""The pagination token to continue listing from.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[PatchHistoryEntrySummary]'})
@cli_util.wrap_exceptions
def list_db_home_patch_history_entries(ctx, from_json, all_pages, page_size, db_home_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(db_home_id, six.string_types) and len(db_home_id.strip()) == 0:
        raise click.UsageError('Parameter --db-home-id cannot be whitespace or empty string')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_db_home_patch_history_entries,
            db_home_id=db_home_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_db_home_patch_history_entries,
            limit,
            page_size,
            db_home_id=db_home_id,
            **kwargs
        )
    else:
        result = client.list_db_home_patch_history_entries(
            db_home_id=db_home_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@patch_group.command(name=cli_util.override('list_db_home_patches.command_name', 'list-db-home'), help="""Lists patches applicable to the requested database home.""")
@cli_util.option('--db-home-id', required=True, help="""The database home [OCID].""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return per page.""")
@cli_util.option('--page', help="""The pagination token to continue listing from.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[PatchSummary]'})
@cli_util.wrap_exceptions
def list_db_home_patches(ctx, from_json, all_pages, page_size, db_home_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(db_home_id, six.string_types) and len(db_home_id.strip()) == 0:
        raise click.UsageError('Parameter --db-home-id cannot be whitespace or empty string')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_db_home_patches,
            db_home_id=db_home_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_db_home_patches,
            limit,
            page_size,
            db_home_id=db_home_id,
            **kwargs
        )
    else:
        result = client.list_db_home_patches(
            db_home_id=db_home_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@db_home_group.command(name=cli_util.override('list_db_homes.command_name', 'list'), help="""Gets a list of database homes in the specified DB system and compartment. A database home is a directory where Oracle database software is installed.""")
@cli_util.option('--compartment-id', required=True, help="""The compartment [OCID].""")
@cli_util.option('--db-system-id', required=True, help="""The [OCID] of the DB system.""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return per page.""")
@cli_util.option('--page', help="""The pagination token to continue listing from.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), help="""A filter to return only resources that match the given lifecycle state exactly.""")
@cli_util.option('--display-name', help="""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[DbHomeSummary]'})
@cli_util.wrap_exceptions
def list_db_homes(ctx, from_json, all_pages, page_size, compartment_id, db_system_id, limit, page, sort_by, sort_order, lifecycle_state, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_db_homes,
            compartment_id=compartment_id,
            db_system_id=db_system_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_db_homes,
            limit,
            page_size,
            compartment_id=compartment_id,
            db_system_id=db_system_id,
            **kwargs
        )
    else:
        result = client.list_db_homes(
            compartment_id=compartment_id,
            db_system_id=db_system_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@db_node_group.command(name=cli_util.override('list_db_nodes.command_name', 'list'), help="""Gets a list of database nodes in the specified DB system and compartment. A database node is a server running database software.""")
@cli_util.option('--compartment-id', required=True, help="""The compartment [OCID].""")
@cli_util.option('--db-system-id', required=True, help="""The [OCID] of the DB system.""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return per page.""")
@cli_util.option('--page', help="""The pagination token to continue listing from.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED"]), help="""Sort by TIMECREATED.  Default order for TIMECREATED is descending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "FAILED"]), help="""A filter to return only resources that match the given lifecycle state exactly.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[DbNodeSummary]'})
@cli_util.wrap_exceptions
def list_db_nodes(ctx, from_json, all_pages, page_size, compartment_id, db_system_id, limit, page, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_db_nodes,
            compartment_id=compartment_id,
            db_system_id=db_system_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_db_nodes,
            limit,
            page_size,
            compartment_id=compartment_id,
            db_system_id=db_system_id,
            **kwargs
        )
    else:
        result = client.list_db_nodes(
            compartment_id=compartment_id,
            db_system_id=db_system_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@patch_history_entry_group.command(name=cli_util.override('list_db_system_patch_history_entries.command_name', 'list-db-system'), help="""Gets the history of the patch actions performed on the specified DB system.""")
@cli_util.option('--db-system-id', required=True, help="""The DB system [OCID].""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return per page.""")
@cli_util.option('--page', help="""The pagination token to continue listing from.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[PatchHistoryEntrySummary]'})
@cli_util.wrap_exceptions
def list_db_system_patch_history_entries(ctx, from_json, all_pages, page_size, db_system_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(db_system_id, six.string_types) and len(db_system_id.strip()) == 0:
        raise click.UsageError('Parameter --db-system-id cannot be whitespace or empty string')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_db_system_patch_history_entries,
            db_system_id=db_system_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_db_system_patch_history_entries,
            limit,
            page_size,
            db_system_id=db_system_id,
            **kwargs
        )
    else:
        result = client.list_db_system_patch_history_entries(
            db_system_id=db_system_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@patch_group.command(name=cli_util.override('list_db_system_patches.command_name', 'list-db-system'), help="""Lists the patches applicable to the requested DB system.""")
@cli_util.option('--db-system-id', required=True, help="""The DB system [OCID].""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return per page.""")
@cli_util.option('--page', help="""The pagination token to continue listing from.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[PatchSummary]'})
@cli_util.wrap_exceptions
def list_db_system_patches(ctx, from_json, all_pages, page_size, db_system_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(db_system_id, six.string_types) and len(db_system_id.strip()) == 0:
        raise click.UsageError('Parameter --db-system-id cannot be whitespace or empty string')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_db_system_patches,
            db_system_id=db_system_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_db_system_patches,
            limit,
            page_size,
            db_system_id=db_system_id,
            **kwargs
        )
    else:
        result = client.list_db_system_patches(
            db_system_id=db_system_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@db_system_shape_group.command(name=cli_util.override('list_db_system_shapes.command_name', 'list'), help="""Gets a list of the shapes that can be used to launch a new DB system. The shape determines resources to allocate to the DB system - CPU cores and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes.""")
@cli_util.option('--availability-domain', required=True, help="""The name of the Availability Domain.""")
@cli_util.option('--compartment-id', required=True, help="""The compartment [OCID].""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return per page.""")
@cli_util.option('--page', help="""The pagination token to continue listing from.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[DbSystemShapeSummary]'})
@cli_util.wrap_exceptions
def list_db_system_shapes(ctx, from_json, all_pages, page_size, availability_domain, compartment_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_db_system_shapes,
            availability_domain=availability_domain,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_db_system_shapes,
            limit,
            page_size,
            availability_domain=availability_domain,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_db_system_shapes(
            availability_domain=availability_domain,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@db_system_group.command(name=cli_util.override('list_db_systems.command_name', 'list'), help="""Gets a list of the DB systems in the specified compartment. You can specify a backupId to list only the DB systems that support creating a database using this backup in this compartment.""")
@cli_util.option('--compartment-id', required=True, help="""The compartment [OCID].""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return per page.""")
@cli_util.option('--page', help="""The pagination token to continue listing from.""")
@cli_util.option('--backup-id', help="""The [OCID] of the backup. Specify a backupId to list only the DB systems that support creating a database using this backup in this compartment.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), help="""A filter to return only resources that match the given lifecycle state exactly.""")
@cli_util.option('--availability-domain', help="""A filter to return only resources that match the given availability domain exactly.""")
@cli_util.option('--display-name', help="""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[DbSystemSummary]'})
@cli_util.wrap_exceptions
def list_db_systems(ctx, from_json, all_pages, page_size, compartment_id, limit, page, backup_id, sort_by, sort_order, lifecycle_state, availability_domain, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    if sort_by and not availability_domain and not all_pages:
        raise click.UsageError('You must provide an --availability-domain when doing a --sort-by, unless you specify the --all parameter')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if backup_id is not None:
        kwargs['backup_id'] = backup_id
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if availability_domain is not None:
        kwargs['availability_domain'] = availability_domain
    if display_name is not None:
        kwargs['display_name'] = display_name
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_db_systems,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_db_systems,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_db_systems(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@db_version_group.command(name=cli_util.override('list_db_versions.command_name', 'list'), help="""Gets a list of supported Oracle database versions.""")
@cli_util.option('--compartment-id', required=True, help="""The compartment [OCID].""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return per page.""")
@cli_util.option('--page', help="""The pagination token to continue listing from.""")
@cli_util.option('--db-system-shape', help="""If provided, filters the results to the set of database versions which are supported for the given shape.""")
@cli_util.option('--db-system-id', help="""The DB system [OCID]. If provided, filters the results to the set of database versions which are supported for the DB system.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[DbVersionSummary]'})
@cli_util.wrap_exceptions
def list_db_versions(ctx, from_json, all_pages, page_size, compartment_id, limit, page, db_system_shape, db_system_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if db_system_shape is not None:
        kwargs['db_system_shape'] = db_system_shape
    if db_system_id is not None:
        kwargs['db_system_id'] = db_system_id
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_db_versions,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_db_versions,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_db_versions(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@data_guard_association_group.command(name=cli_util.override('reinstate_data_guard_association.command_name', 'reinstate'), help="""Reinstates the database identified by the `databaseId` parameter into the standby role in a Data Guard association.""")
@cli_util.option('--database-id', required=True, help="""The database [OCID].""")
@cli_util.option('--data-guard-association-id', required=True, help="""The Data Guard association's [OCID].""")
@cli_util.option('--database-admin-password', required=True, help="""The DB system administrator password.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DataGuardAssociation'})
@cli_util.wrap_exceptions
def reinstate_data_guard_association(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_id, data_guard_association_id, database_admin_password, if_match):

    if isinstance(database_id, six.string_types) and len(database_id.strip()) == 0:
        raise click.UsageError('Parameter --database-id cannot be whitespace or empty string')

    if isinstance(data_guard_association_id, six.string_types) and len(data_guard_association_id.strip()) == 0:
        raise click.UsageError('Parameter --data-guard-association-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}
    details['databaseAdminPassword'] = database_admin_password

    client = cli_util.build_client('database', ctx)
    result = client.reinstate_data_guard_association(
        database_id=database_id,
        data_guard_association_id=data_guard_association_id,
        reinstate_data_guard_association_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_data_guard_association') and callable(getattr(client, 'get_data_guard_association')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_guard_association(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_data_warehouse_group.command(name=cli_util.override('restore_autonomous_data_warehouse.command_name', 'restore'), help="""Restores an Autonomous Data Warehouse based on the provided request parameters.""")
@cli_util.option('--autonomous-data-warehouse-id', required=True, help="""The database [OCID].""")
@cli_util.option('--timestamp', required=True, type=custom_types.CLI_DATETIME, help="""The time to restore the database to.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'AutonomousDataWarehouse'})
@cli_util.wrap_exceptions
def restore_autonomous_data_warehouse(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, autonomous_data_warehouse_id, timestamp, if_match):

    if isinstance(autonomous_data_warehouse_id, six.string_types) and len(autonomous_data_warehouse_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-data-warehouse-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}
    details['timestamp'] = timestamp

    client = cli_util.build_client('database', ctx)
    result = client.restore_autonomous_data_warehouse(
        autonomous_data_warehouse_id=autonomous_data_warehouse_id,
        restore_autonomous_data_warehouse_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_data_warehouse') and callable(getattr(client, 'get_autonomous_data_warehouse')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_data_warehouse(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_database_group.command(name=cli_util.override('restore_autonomous_database.command_name', 'restore'), help="""Restores an Autonomous Database based on the provided request parameters.""")
@cli_util.option('--autonomous-database-id', required=True, help="""The database [OCID].""")
@cli_util.option('--timestamp', required=True, type=custom_types.CLI_DATETIME, help="""The time to restore the database to.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "RESTORE_FAILED", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'AutonomousDatabase'})
@cli_util.wrap_exceptions
def restore_autonomous_database(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, autonomous_database_id, timestamp, if_match):

    if isinstance(autonomous_database_id, six.string_types) and len(autonomous_database_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-database-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}
    details['timestamp'] = timestamp

    client = cli_util.build_client('database', ctx)
    result = client.restore_autonomous_database(
        autonomous_database_id=autonomous_database_id,
        restore_autonomous_database_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_database') and callable(getattr(client, 'get_autonomous_database')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_database(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@database_group.command(name=cli_util.override('restore_database.command_name', 'restore'), help="""Restore a Database based on the request parameters you provide.""")
@cli_util.option('--database-id', required=True, help="""The database [OCID].""")
@cli_util.option('--database-scn', help="""Restores using the backup with the System Change Number (SCN) specified.""")
@cli_util.option('--latest', type=click.BOOL, help="""Restores to the last known good state with the least possible data loss.""")
@cli_util.option('--timestamp', type=custom_types.CLI_DATETIME, help="""Restores to the timestamp specified.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "BACKUP_IN_PROGRESS", "TERMINATING", "TERMINATED", "RESTORE_FAILED", "FAILED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'Database'})
@cli_util.wrap_exceptions
def restore_database(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_id, database_scn, latest, timestamp, if_match):

    if isinstance(database_id, six.string_types) and len(database_id.strip()) == 0:
        raise click.UsageError('Parameter --database-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if database_scn is not None:
        details['databaseSCN'] = database_scn

    if latest is not None:
        details['latest'] = latest

    if timestamp is not None:
        details['timestamp'] = timestamp

    client = cli_util.build_client('database', ctx)
    result = client.restore_database(
        database_id=database_id,
        restore_database_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_database') and callable(getattr(client, 'get_database')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_database(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_data_warehouse_group.command(name=cli_util.override('start_autonomous_data_warehouse.command_name', 'start'), help="""Starts the specified autonomous Data Warehouse.""")
@cli_util.option('--autonomous-data-warehouse-id', required=True, help="""The database [OCID].""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'AutonomousDataWarehouse'})
@cli_util.wrap_exceptions
def start_autonomous_data_warehouse(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, autonomous_data_warehouse_id, if_match):

    if isinstance(autonomous_data_warehouse_id, six.string_types) and len(autonomous_data_warehouse_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-data-warehouse-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('database', ctx)
    result = client.start_autonomous_data_warehouse(
        autonomous_data_warehouse_id=autonomous_data_warehouse_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_data_warehouse') and callable(getattr(client, 'get_autonomous_data_warehouse')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_data_warehouse(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_database_group.command(name=cli_util.override('start_autonomous_database.command_name', 'start'), help="""Starts the specified Autonomous Database.""")
@cli_util.option('--autonomous-database-id', required=True, help="""The database [OCID].""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "RESTORE_FAILED", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'AutonomousDatabase'})
@cli_util.wrap_exceptions
def start_autonomous_database(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, autonomous_database_id, if_match):

    if isinstance(autonomous_database_id, six.string_types) and len(autonomous_database_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-database-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('database', ctx)
    result = client.start_autonomous_database(
        autonomous_database_id=autonomous_database_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_database') and callable(getattr(client, 'get_autonomous_database')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_database(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_data_warehouse_group.command(name=cli_util.override('stop_autonomous_data_warehouse.command_name', 'stop'), help="""Stops the specified Autonomous Data Warehouse.""")
@cli_util.option('--autonomous-data-warehouse-id', required=True, help="""The database [OCID].""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'AutonomousDataWarehouse'})
@cli_util.wrap_exceptions
def stop_autonomous_data_warehouse(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, autonomous_data_warehouse_id, if_match):

    if isinstance(autonomous_data_warehouse_id, six.string_types) and len(autonomous_data_warehouse_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-data-warehouse-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('database', ctx)
    result = client.stop_autonomous_data_warehouse(
        autonomous_data_warehouse_id=autonomous_data_warehouse_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_data_warehouse') and callable(getattr(client, 'get_autonomous_data_warehouse')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_data_warehouse(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_database_group.command(name=cli_util.override('stop_autonomous_database.command_name', 'stop'), help="""Stops the specified Autonomous Database.""")
@cli_util.option('--autonomous-database-id', required=True, help="""The database [OCID].""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "RESTORE_FAILED", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'AutonomousDatabase'})
@cli_util.wrap_exceptions
def stop_autonomous_database(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, autonomous_database_id, if_match):

    if isinstance(autonomous_database_id, six.string_types) and len(autonomous_database_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-database-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    result = client.stop_autonomous_database(
        autonomous_database_id=autonomous_database_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_database') and callable(getattr(client, 'get_autonomous_database')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_database(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@data_guard_association_group.command(name=cli_util.override('switchover_data_guard_association.command_name', 'switchover'), help="""Performs a switchover to transition the primary database of a Data Guard association into a standby role. The standby database associated with the `dataGuardAssociationId` assumes the primary database role.

A switchover guarantees no data loss.""")
@cli_util.option('--database-id', required=True, help="""The database [OCID].""")
@cli_util.option('--data-guard-association-id', required=True, help="""The Data Guard association's [OCID].""")
@cli_util.option('--database-admin-password', required=True, help="""The DB system administrator password.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DataGuardAssociation'})
@cli_util.wrap_exceptions
def switchover_data_guard_association(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_id, data_guard_association_id, database_admin_password, if_match):

    if isinstance(database_id, six.string_types) and len(database_id.strip()) == 0:
        raise click.UsageError('Parameter --database-id cannot be whitespace or empty string')

    if isinstance(data_guard_association_id, six.string_types) and len(data_guard_association_id.strip()) == 0:
        raise click.UsageError('Parameter --data-guard-association-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}
    details['databaseAdminPassword'] = database_admin_password

    client = cli_util.build_client('database', ctx)
    result = client.switchover_data_guard_association(
        database_id=database_id,
        data_guard_association_id=data_guard_association_id,
        switchover_data_guard_association_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_data_guard_association') and callable(getattr(client, 'get_data_guard_association')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_guard_association(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_system_group.command(name=cli_util.override('terminate_db_system.command_name', 'terminate'), help="""Terminates a DB system and permanently deletes it and any databases running on it, and any storage volumes attached to it. The database data is local to the DB system and will be lost when the system is terminated. Oracle recommends that you back up any data in the DB system prior to terminating it.""")
@cli_util.option('--db-system-id', required=True, help="""The DB system [OCID].""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def terminate_db_system(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, db_system_id, if_match):

    if isinstance(db_system_id, six.string_types) and len(db_system_id.strip()) == 0:
        raise click.UsageError('Parameter --db-system-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('database', ctx)
    result = client.terminate_db_system(
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

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_db_system(db_system_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_data_warehouse_group.command(name=cli_util.override('update_autonomous_data_warehouse.command_name', 'update'), help="""Updates the specified Autonomous Data Warehouse with a new CPU core count and size.""")
@cli_util.option('--autonomous-data-warehouse-id', required=True, help="""The database [OCID].""")
@cli_util.option('--admin-password', help="""A strong password for Admin. The password must be between 12 and 60 characters long, and must contain at least 1 uppercase, 1 lowercase and 2 numeric characters. It cannot contain the double quote symbol (\"). It must be different than the last 4 passwords.""")
@cli_util.option('--cpu-core-count', type=click.INT, help="""The number of CPU cores to be made available to the database.""")
@cli_util.option('--data-storage-size-in-tbs', type=click.INT, help="""Size, in terabytes, of the data volume that will be attached to the database.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""The user-friendly name for the Autonomous Data Warehouse. The name does not have to be unique.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}}, output_type={'module': 'database', 'class': 'AutonomousDataWarehouse'})
@cli_util.wrap_exceptions
def update_autonomous_data_warehouse(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, autonomous_data_warehouse_id, admin_password, cpu_core_count, data_storage_size_in_tbs, defined_tags, display_name, freeform_tags, if_match):

    if isinstance(autonomous_data_warehouse_id, six.string_types) and len(autonomous_data_warehouse_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-data-warehouse-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if admin_password is not None:
        details['adminPassword'] = admin_password

    if cpu_core_count is not None:
        details['cpuCoreCount'] = cpu_core_count

    if data_storage_size_in_tbs is not None:
        details['dataStorageSizeInTBs'] = data_storage_size_in_tbs

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('database', ctx)
    result = client.update_autonomous_data_warehouse(
        autonomous_data_warehouse_id=autonomous_data_warehouse_id,
        update_autonomous_data_warehouse_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_data_warehouse') and callable(getattr(client, 'get_autonomous_data_warehouse')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_data_warehouse(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_database_group.command(name=cli_util.override('update_autonomous_database.command_name', 'update'), help="""Updates the specified Autonomous Database with a new CPU core count and size.""")
@cli_util.option('--autonomous-database-id', required=True, help="""The database [OCID].""")
@cli_util.option('--admin-password', help="""A strong password for Admin. The password must be between 12 and 60 characters long, and must contain at least 1 uppercase, 1 lowercase and 2 numeric characters. It cannot contain the double quote symbol (\"). It must be different than the last 4 passwords.""")
@cli_util.option('--cpu-core-count', type=click.INT, help="""The number of CPU cores to be made available to the database.""")
@cli_util.option('--data-storage-size-in-tbs', type=click.INT, help="""The size, in terabytes, of the data volume that will be attached to the database.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""The user-friendly name for the Autonomous Database. The name does not have to be unique.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "RESTORE_FAILED", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}}, output_type={'module': 'database', 'class': 'AutonomousDatabase'})
@cli_util.wrap_exceptions
def update_autonomous_database(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, autonomous_database_id, admin_password, cpu_core_count, data_storage_size_in_tbs, defined_tags, display_name, freeform_tags, if_match):

    if isinstance(autonomous_database_id, six.string_types) and len(autonomous_database_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-database-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}

    if admin_password is not None:
        details['adminPassword'] = admin_password

    if cpu_core_count is not None:
        details['cpuCoreCount'] = cpu_core_count

    if data_storage_size_in_tbs is not None:
        details['dataStorageSizeInTBs'] = data_storage_size_in_tbs

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('database', ctx)
    result = client.update_autonomous_database(
        autonomous_database_id=autonomous_database_id,
        update_autonomous_database_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_database') and callable(getattr(client, 'get_autonomous_database')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_database(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@database_group.command(name=cli_util.override('update_database.command_name', 'update'), help="""Update a Database based on the request parameters you provide.""")
@cli_util.option('--database-id', required=True, help="""The database [OCID].""")
@cli_util.option('--db-backup-config', type=custom_types.CLI_COMPLEX_TYPE, help="""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "BACKUP_IN_PROGRESS", "TERMINATING", "TERMINATED", "RESTORE_FAILED", "FAILED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'db-backup-config': {'module': 'database', 'class': 'DbBackupConfig'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'db-backup-config': {'module': 'database', 'class': 'DbBackupConfig'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}}, output_type={'module': 'database', 'class': 'Database'})
@cli_util.wrap_exceptions
def update_database(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, database_id, db_backup_config, defined_tags, freeform_tags, if_match):

    if isinstance(database_id, six.string_types) and len(database_id.strip()) == 0:
        raise click.UsageError('Parameter --database-id cannot be whitespace or empty string')
    if not force:
        if db_backup_config or defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to db-backup-config and defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if db_backup_config is not None:
        details['dbBackupConfig'] = cli_util.parse_json_parameter("db_backup_config", db_backup_config)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('database', ctx)
    result = client.update_database(
        database_id=database_id,
        update_database_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_database') and callable(getattr(client, 'get_database')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_database(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_home_group.command(name=cli_util.override('update_db_home.command_name', 'update'), help="""Patches the specified dbHome.""")
@cli_util.option('--db-home-id', required=True, help="""The database home [OCID].""")
@cli_util.option('--db-version', type=custom_types.CLI_COMPLEX_TYPE, help="""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'db-version': {'module': 'database', 'class': 'PatchDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'db-version': {'module': 'database', 'class': 'PatchDetails'}}, output_type={'module': 'database', 'class': 'DbHome'})
@cli_util.wrap_exceptions
def update_db_home(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, db_home_id, db_version, if_match):

    if isinstance(db_home_id, six.string_types) and len(db_home_id.strip()) == 0:
        raise click.UsageError('Parameter --db-home-id cannot be whitespace or empty string')
    if not force:
        if db_version:
            if not click.confirm("WARNING: Updates to db-version will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if db_version is not None:
        details['dbVersion'] = cli_util.parse_json_parameter("db_version", db_version)

    client = cli_util.build_client('database', ctx)
    result = client.update_db_home(
        db_home_id=db_home_id,
        update_db_home_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_db_home') and callable(getattr(client, 'get_db_home')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_db_home(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_system_group.command(name=cli_util.override('update_db_system.command_name', 'update'), help="""Updates the properties of a DB system, such as the CPU core count.""")
@cli_util.option('--db-system-id', required=True, help="""The DB system [OCID].""")
@cli_util.option('--cpu-core-count', type=click.INT, help="""The new number of CPU cores to set for the DB system. Not applicable for virtual machine DB systems.""")
@cli_util.option('--data-storage-size-in-gbs', type=click.INT, help="""The size, in gigabytes, to scale the attached storage up to for this virtual machine DB system. This value must be greater than current storage size. Note that the resulting total storage size attached will be greater than the amount requested to allow for REDO/RECO space and software volume. Applies only to virtual machine DB systems.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ssh-public-keys', type=custom_types.CLI_COMPLEX_TYPE, help="""The public key portion of the key pair to use for SSH access to the DB system. Multiple public keys can be provided. The length of the combined keys cannot exceed 10,000 characters.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--version', type=custom_types.CLI_COMPLEX_TYPE, help="""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}, 'version': {'module': 'database', 'class': 'PatchDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}, 'version': {'module': 'database', 'class': 'PatchDetails'}}, output_type={'module': 'database', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def update_db_system(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, db_system_id, cpu_core_count, data_storage_size_in_gbs, defined_tags, freeform_tags, ssh_public_keys, version, if_match):

    if isinstance(db_system_id, six.string_types) and len(db_system_id.strip()) == 0:
        raise click.UsageError('Parameter --db-system-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags or ssh_public_keys or version:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags and ssh-public-keys and version will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if cpu_core_count is not None:
        details['cpuCoreCount'] = cpu_core_count

    if data_storage_size_in_gbs is not None:
        details['dataStorageSizeInGBs'] = data_storage_size_in_gbs

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if ssh_public_keys is not None:
        details['sshPublicKeys'] = cli_util.parse_json_parameter("ssh_public_keys", ssh_public_keys)

    if version is not None:
        details['version'] = cli_util.parse_json_parameter("version", version)

    client = cli_util.build_client('database', ctx)
    result = client.update_db_system(
        db_system_id=db_system_id,
        update_db_system_details=details,
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

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_db_system(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
