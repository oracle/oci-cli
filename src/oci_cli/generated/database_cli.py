# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from ..cli_root import cli
from .. import cli_util
from .. import json_skeleton_utils
from .. import retry_utils  # noqa: F401
from .. import custom_types  # noqa: F401
from ..aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('db_group.command_name', 'db'), cls=CommandGroupWithAlias, help=cli_util.override('db_group.help', """The API for the Database Service."""))
@cli_util.help_option_group
def db_group():
    pass


@click.command(cli_util.override('patch_group.command_name', 'patch'), cls=CommandGroupWithAlias, help="""A Patch for a DB System or DB Home.

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access,
see [Getting Started with Policies].""")
@cli_util.help_option_group
def patch_group():
    pass


@click.command(cli_util.override('db_version_group.command_name', 'db-version'), cls=CommandGroupWithAlias, help="""The Oracle database software version.

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def db_version_group():
    pass


@click.command(cli_util.override('backup_group.command_name', 'backup'), cls=CommandGroupWithAlias, help="""A database backup
To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def backup_group():
    pass


@click.command(cli_util.override('database_group.command_name', 'database'), cls=CommandGroupWithAlias, help="""An Oracle database on a DB System. For more information, see [Managing Oracle Databases].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def database_group():
    pass


@click.command(cli_util.override('patch_history_entry_group.command_name', 'patch-history-entry'), cls=CommandGroupWithAlias, help="""The record of a patch action on a specified target.""")
@cli_util.help_option_group
def patch_history_entry_group():
    pass


@click.command(cli_util.override('db_system_shape_group.command_name', 'db-system-shape'), cls=CommandGroupWithAlias, help="""The shape of the DB System. The shape determines resources to allocate to the DB system - CPU cores and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes.
For a description of shapes, see [DB System Launch Options].
To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator.
If you're an administrator who needs to write policies to give users access,
see [Getting Started with Policies].""")
@cli_util.help_option_group
def db_system_shape_group():
    pass


@click.command(cli_util.override('data_guard_association_group.command_name', 'data-guard-association'), cls=CommandGroupWithAlias, help="""The properties that define a Data Guard association.

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an
administrator. If you're an administrator who needs to write policies to give users access, see
[Getting Started with Policies].

For information about endpoints and signing API requests, see
[About the API]. For information about available SDKs and tools, see
[SDKS and Other Tools].""")
@cli_util.help_option_group
def data_guard_association_group():
    pass


@click.command(cli_util.override('db_home_group.command_name', 'db-home'), cls=CommandGroupWithAlias, help="""A directory where Oracle database software is installed. Each DB System can have multiple database homes,
and each database home can have multiple databases within it. All the databases within a single database home
must be the same database version, but different database homes can run different versions. For more information,
see [Managing Oracle Databases].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an
administrator. If you're an administrator who needs to write policies to give users access,
see [Getting Started with Policies].""")
@cli_util.help_option_group
def db_home_group():
    pass


@click.command(cli_util.override('db_system_group.command_name', 'db-system'), cls=CommandGroupWithAlias, help="""The Database Service supports several types of DB Systems, ranging in size, price, and performance. For details about each type of system, see:

- [Exadata DB Systems]
- [Bare Metal or VM DB Systems]

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

For information about access control and compartments, see
[Overview of the Identity Service].

For information about Availability Domains, see
[Regions and Availability Domains].

To get a list of Availability Domains, use the `ListAvailabilityDomains` operation
in the Identity Service API.""")
@cli_util.help_option_group
def db_system_group():
    pass


@click.command(cli_util.override('db_node_group.command_name', 'db-node'), cls=CommandGroupWithAlias, help="""A server where Oracle database software is running.

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def db_node_group():
    pass


@backup_group.command(name=cli_util.override('create_backup.command_name', 'create'), help="""Creates a new backup in the specified database based on the request parameters you provide. If you previously used RMAN or dbcli to configure backups and then you switch to using the Console or the API for backups, a new backup configuration is created and associated with your database. This means that you can no longer rely on your previously configured unmanaged backups to work.""")
@click.option('--database-id', callback=cli_util.handle_required_param, help="""The OCID of the database. [required]""")
@click.option('--display-name', callback=cli_util.handle_required_param, help="""The user-friendly name for the backup. It does not have to be unique. [required]""")
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "RESTORING"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
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
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_backup, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@data_guard_association_group.command(name=cli_util.override('create_data_guard_association.command_name', 'create'), help="""Creates a new Data Guard association.  A Data Guard association represents the replication relationship between the specified database and a peer database. For more information, see [Using Oracle Data Guard].

All Oracle Cloud Infrastructure resources, including Data Guard associations, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. Fore more information, see [Resource Identifiers].""")
@click.option('--database-id', callback=cli_util.handle_required_param, help="""The database [OCID]. [required]""")
@click.option('--creation-type', callback=cli_util.handle_required_param, help="""Specifies where to create the associated database. \"ExistingDbSystem\" is the only supported `creationType` value. [required]""")
@click.option('--database-admin-password', callback=cli_util.handle_required_param, help="""A strong password for the `SYS`, `SYSTEM`, and `PDB Admin` users to apply during standby creation.

The password must contain no fewer than nine characters and include:

* At least two uppercase characters.

* At least two lowercase characters.

* At least two numeric characters.

* At least two special characters. Valid special characters include \"_\", \"#\", and \"-\" only.

**The password MUST be the same as the primary admin password.** [required]""")
@click.option('--protection-mode', callback=cli_util.handle_required_param, type=custom_types.CliCaseInsensitiveChoice(["MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE", "MAXIMUM_PROTECTION"]), help="""The protection mode to set up between the primary and standby databases. For more information, see [Oracle Data Guard Protection Modes] in the Oracle Data Guard documentation.

**IMPORTANT** - The only protection mode currently supported by the Database Service is MAXIMUM_PERFORMANCE. [required]""")
@click.option('--transport-type', callback=cli_util.handle_required_param, type=custom_types.CliCaseInsensitiveChoice(["SYNC", "ASYNC", "FASTSYNC"]), help="""The redo transport type to use for this Data Guard association.  Valid values depend on the specified `protectionMode`:

* MAXIMUM_AVAILABILITY - SYNC or FASTSYNC * MAXIMUM_PERFORMANCE - ASYNC * MAXIMUM_PROTECTION - SYNC

For more information, see [Redo Transport Services] in the Oracle Data Guard documentation.

**IMPORTANT** - The only transport type currently supported by the Database Service is ASYNC. [required]""")
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
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
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_data_guard_association, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_home_group.command(name=cli_util.override('create_db_home.command_name', 'create'), help="""Creates a new DB Home in the specified DB System based on the request parameters you provide.""")
@click.option('--db-system-id', callback=cli_util.handle_required_param, help="""The OCID of the DB System. [required]""")
@click.option('--display-name', callback=cli_util.handle_optional_param, help="""The user-provided name of the database home.""")
@click.option('--source', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["NONE", "DB_BACKUP"]), help="""Source of database:   NONE for creating a new database   DB_BACKUP for creating a new database by restoring a backup""")
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
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
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_db_home, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_node_group.command(name=cli_util.override('db_node_action.command_name', 'db-node-action'), help="""Performs an action, such as one of the power actions (start, stop, softreset, or reset), on the specified DB Node.

**start** - power on

**stop** - power off

**softreset** - ACPI shutdown and power on

**reset** - power off and power on

Note that the **stop** state has no effect on the resources you consume. Billing continues for DB Nodes that you stop, and related resources continue to apply against any relevant quotas. You must terminate the DB System ([TerminateDbSystem]) to remove its resources from billing and quotas.""")
@click.option('--db-node-id', callback=cli_util.handle_required_param, help="""The database node [OCID]. [required]""")
@click.option('--action', callback=cli_util.handle_required_param, help="""The action to perform on the DB Node. Allowed values are: STOP, START, SOFTRESET, RESET [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "FAILED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
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
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_db_node, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@backup_group.command(name=cli_util.override('delete_backup.command_name', 'delete'), help="""Deletes a full backup. You cannot delete automatic backups using this API.""")
@click.option('--backup-id', callback=cli_util.handle_required_param, help="""The backup OCID. [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "RESTORING"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
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
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_backup, backup_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_home_group.command(name=cli_util.override('delete_db_home.command_name', 'delete'), help="""Deletes a DB Home. The DB Home and its database data are local to the DB System and will be lost when it is deleted. Oracle recommends that you back up any data in the DB System prior to deleting it.""")
@click.option('--db-home-id', callback=cli_util.handle_required_param, help="""The database home [OCID]. [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--perform-final-backup', callback=cli_util.handle_optional_param, type=click.BOOL, help="""Whether to perform a final backup of the database or not. Default is false. If you previously used RMAN or dbcli to configure backups and then you switch to using the Console or the API for backups, a new backup configuration is created and associated with your database. This means that you can no longer rely on your previously configured unmanaged backups to work.""")
@cli_util.confirm_delete_option
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
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
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_db_home, db_home_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@data_guard_association_group.command(name=cli_util.override('failover_data_guard_association.command_name', 'failover'), help="""Performs a failover to transition the standby database identified by the `databaseId` parameter into the specified Data Guard association's primary role after the existing primary database fails or becomes unreachable.

A failover might result in data loss depending on the protection mode in effect at the time of the primary database failure.""")
@click.option('--database-id', callback=cli_util.handle_required_param, help="""The database [OCID]. [required]""")
@click.option('--data-guard-association-id', callback=cli_util.handle_required_param, help="""The Data Guard association's [OCID]. [required]""")
@click.option('--database-admin-password', callback=cli_util.handle_required_param, help="""The DB System administrator password. [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DataGuardAssociation'})
@cli_util.wrap_exceptions
def failover_data_guard_association(ctx, from_json, database_id, data_guard_association_id, database_admin_password, if_match):

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
    cli_util.render_response(result, ctx)


@backup_group.command(name=cli_util.override('get_backup.command_name', 'get'), help="""Gets information about the specified backup.""")
@click.option('--backup-id', callback=cli_util.handle_required_param, help="""The backup OCID. [required]""")
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
@click.option('--database-id', callback=cli_util.handle_required_param, help="""The database [OCID]. [required]""")
@click.option('--data-guard-association-id', callback=cli_util.handle_required_param, help="""The Data Guard association's [OCID]. [required]""")
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
@click.option('--database-id', callback=cli_util.handle_required_param, help="""The database [OCID]. [required]""")
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
@click.option('--db-home-id', callback=cli_util.handle_required_param, help="""The database home [OCID]. [required]""")
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
@click.option('--db-home-id', callback=cli_util.handle_required_param, help="""The database home [OCID]. [required]""")
@click.option('--patch-id', callback=cli_util.handle_required_param, help="""The OCID of the patch. [required]""")
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
@click.option('--db-home-id', callback=cli_util.handle_required_param, help="""The database home [OCID]. [required]""")
@click.option('--patch-history-entry-id', callback=cli_util.handle_required_param, help="""The OCID of the patch history entry. [required]""")
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
@click.option('--db-node-id', callback=cli_util.handle_required_param, help="""The database node [OCID]. [required]""")
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


@db_system_group.command(name=cli_util.override('get_db_system.command_name', 'get'), help="""Gets information about the specified DB System.""")
@click.option('--db-system-id', callback=cli_util.handle_required_param, help="""The DB System [OCID]. [required]""")
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
@click.option('--db-system-id', callback=cli_util.handle_required_param, help="""The DB System [OCID]. [required]""")
@click.option('--patch-id', callback=cli_util.handle_required_param, help="""The OCID of the patch. [required]""")
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
@click.option('--db-system-id', callback=cli_util.handle_required_param, help="""The DB System [OCID]. [required]""")
@click.option('--patch-history-entry-id', callback=cli_util.handle_required_param, help="""The OCID of the patch history entry. [required]""")
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


@db_system_group.command(name=cli_util.override('launch_db_system.command_name', 'launch'), help="""Launches a new DB System in the specified compartment and Availability Domain. You'll specify a single Oracle Database Edition that applies to all the databases on that DB System. The selected edition cannot be changed.

An initial database is created on the DB System based on the request parameters you provide and some default options. For more information, see [Default Options for the Initial Database].

The DB System will include a command line interface (CLI) that you can use to create additional databases and manage existing databases. For more information, see the [Oracle Database CLI Reference].""")
@click.option('--availability-domain', callback=cli_util.handle_required_param, help="""The Availability Domain where the DB System is located. [required]""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The Oracle Cloud ID (OCID) of the compartment the DB System  belongs in. [required]""")
@click.option('--cpu-core-count', callback=cli_util.handle_required_param, type=click.INT, help="""The number of CPU cores to enable. The valid values depend on the specified shape:

- BM.DenseIO1.36 and BM.HighIO1.36 - Specify a multiple of 2, from 2 to 36. - BM.RACLocalStorage1.72 - Specify a multiple of 4, from 4 to 72. - Exadata.Quarter1.84 - Specify a multiple of 2, from 22 to 84. - Exadata.Half1.168 - Specify a multiple of 4, from 44 to 168. - Exadata.Full1.336 - Specify a multiple of 8, from 88 to 336.

For VM DB systems, the core count is inferred from the specific VM shape chosen, so this parameter is not used. [required]""")
@click.option('--database-edition', callback=cli_util.handle_required_param, type=custom_types.CliCaseInsensitiveChoice(["STANDARD_EDITION", "ENTERPRISE_EDITION", "ENTERPRISE_EDITION_EXTREME_PERFORMANCE", "ENTERPRISE_EDITION_HIGH_PERFORMANCE"]), help="""The Oracle Database Edition that applies to all the databases on the DB System.

Exadata DB Systems and 2-node RAC DB Systems require ENTERPRISE_EDITION_EXTREME_PERFORMANCE. [required]""")
@click.option('--db-home', callback=cli_util.handle_required_param, type=custom_types.CLI_COMPLEX_TYPE, help=""" [required]""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--hostname', callback=cli_util.handle_required_param, help="""The host name for the DB System. The host name must begin with an alphabetic character and can contain a maximum of 30 alphanumeric characters, including hyphens (-).

The maximum length of the combined hostname and domain is 63 characters.

**Note:** The hostname must be unique within the subnet. If it is not unique, the DB System will fail to provision. [required]""")
@click.option('--shape', callback=cli_util.handle_required_param, help="""The shape of the DB System. The shape determines resources allocated to the DB System - CPU cores and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes. To get a list of shapes, use the [ListDbSystemShapes] operation. [required]""")
@click.option('--ssh-public-keys', callback=cli_util.handle_required_param, type=custom_types.CLI_COMPLEX_TYPE, help="""The public key portion of the key pair to use for SSH access to the DB System. Multiple public keys can be provided. The length of the combined keys cannot exceed 10,000 characters. [required]""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--subnet-id', callback=cli_util.handle_required_param, help="""The OCID of the subnet the DB System is associated with.

**Subnet Restrictions:** - For single node and 2-node (RAC) DB Systems, do not use a subnet that overlaps with 192.168.16.16/28 - For Exadata and VM-based RAC DB Systems, do not use a subnet that overlaps with 192.168.128.0/20

These subnets are used by the Oracle Clusterware private interconnect on the database instance. Specifying an overlapping subnet will cause the private interconnect to malfunction. This restriction applies to both the client subnet and backup subnet. [required]""")
@click.option('--backup-subnet-id', callback=cli_util.handle_optional_param, help="""The OCID of the backup network subnet the DB System is associated with. Applicable only to Exadata.

**Subnet Restrictions:** See above subnetId's **Subnet Restriction**.""")
@click.option('--cluster-name', callback=cli_util.handle_optional_param, help="""Cluster name for Exadata and 2-node RAC DB Systems. The cluster name must begin with an an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.""")
@click.option('--data-storage-percentage', callback=cli_util.handle_optional_param, type=click.INT, help="""The percentage assigned to DATA storage (user data and database files). The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Specify 80 or 40. The default is 80 percent assigned to DATA storage. This is not applicable for VM based DB systems.""")
@click.option('--disk-redundancy', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["HIGH", "NORMAL"]), help="""The type of redundancy configured for the DB System. Normal is 2-way redundancy, recommended for test and development systems. High is 3-way redundancy, recommended for production systems.""")
@click.option('--display-name', callback=cli_util.handle_optional_param, help="""The user-friendly name for the DB System. It does not have to be unique.""")
@click.option('--domain', callback=cli_util.handle_optional_param, help="""A domain name used for the DB System. If the Oracle-provided Internet and VCN Resolver is enabled for the specified subnet, the domain name for the subnet is used (don't provide one). Otherwise, provide a valid DNS domain name. Hyphens (-) are not permitted.""")
@click.option('--initial-data-storage-size-in-gb', callback=cli_util.handle_optional_param, type=click.INT, help="""Size, in GBs, of the initial data volume that will be created and attached to VM-shape based DB system. This storage can later be scaled up if needed. Note that the total storage size attached will be more than what is requested, to account for REDO/RECO space and software volume.""")
@click.option('--license-model', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]), help="""The Oracle license model that applies to all the databases on the DB System. The default is LICENSE_INCLUDED.""")
@click.option('--node-count', callback=cli_util.handle_optional_param, type=click.INT, help="""Number of nodes to launch for a VM-shape based RAC DB system.""")
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'db-home': {'module': 'database', 'class': 'CreateDbHomeDetails'}, 'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'db-home': {'module': 'database', 'class': 'CreateDbHomeDetails'}, 'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}}, output_type={'module': 'database', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def launch_db_system(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, compartment_id, cpu_core_count, database_edition, db_home, hostname, shape, ssh_public_keys, subnet_id, backup_subnet_id, cluster_name, data_storage_percentage, disk_redundancy, display_name, domain, initial_data_storage_size_in_gb, license_model, node_count):
    kwargs = {}

    details = {}
    details['availabilityDomain'] = availability_domain
    details['compartmentId'] = compartment_id
    details['cpuCoreCount'] = cpu_core_count
    details['databaseEdition'] = database_edition
    details['dbHome'] = cli_util.parse_json_parameter("db_home", db_home)
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

    if disk_redundancy is not None:
        details['diskRedundancy'] = disk_redundancy

    if display_name is not None:
        details['displayName'] = display_name

    if domain is not None:
        details['domain'] = domain

    if initial_data_storage_size_in_gb is not None:
        details['initialDataStorageSizeInGB'] = initial_data_storage_size_in_gb

    if license_model is not None:
        details['licenseModel'] = license_model

    if node_count is not None:
        details['nodeCount'] = node_count

    client = cli_util.build_client('database', ctx)
    result = client.launch_db_system(
        launch_db_system_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_db_system') and callable(getattr(client, 'get_db_system')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_db_system, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@backup_group.command(name=cli_util.override('list_backups.command_name', 'list'), help="""Gets a list of backups based on the databaseId or compartmentId specified. Either one of the query parameters must be provided.""")
@click.option('--database-id', callback=cli_util.handle_optional_param, help="""The OCID of the database.""")
@click.option('--compartment-id', callback=cli_util.handle_optional_param, help="""The compartment OCID.""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return.""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The pagination token to continue listing from.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
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

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_backups,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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
@click.option('--database-id', callback=cli_util.handle_required_param, help="""The database [OCID]. [required]""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return.""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The pagination token to continue listing from.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
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

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_data_guard_associations,
            database_id=database_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The compartment [OCID]. [required]""")
@click.option('--db-home-id', callback=cli_util.handle_required_param, help="""A database home [OCID]. [required]""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return.""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The pagination token to continue listing from.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[DatabaseSummary]'})
@cli_util.wrap_exceptions
def list_databases(ctx, from_json, all_pages, page_size, compartment_id, db_home_id, limit, page):

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

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_databases,
            compartment_id=compartment_id,
            db_home_id=db_home_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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
@click.option('--db-home-id', callback=cli_util.handle_required_param, help="""The database home [OCID]. [required]""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return.""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The pagination token to continue listing from.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
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

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_db_home_patch_history_entries,
            db_home_id=db_home_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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
@click.option('--db-home-id', callback=cli_util.handle_required_param, help="""The database home [OCID]. [required]""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return.""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The pagination token to continue listing from.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
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

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_db_home_patches,
            db_home_id=db_home_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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


@db_home_group.command(name=cli_util.override('list_db_homes.command_name', 'list'), help="""Gets a list of database homes in the specified DB System and compartment. A database home is a directory where Oracle database software is installed.""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The compartment [OCID]. [required]""")
@click.option('--db-system-id', callback=cli_util.handle_required_param, help="""The [OCID] of the DB System. [required]""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return.""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The pagination token to continue listing from.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[DbHomeSummary]'})
@cli_util.wrap_exceptions
def list_db_homes(ctx, from_json, all_pages, page_size, compartment_id, db_system_id, limit, page):

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

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_db_homes,
            compartment_id=compartment_id,
            db_system_id=db_system_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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


@db_node_group.command(name=cli_util.override('list_db_nodes.command_name', 'list'), help="""Gets a list of database nodes in the specified DB System and compartment. A database node is a server running database software.""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The compartment [OCID]. [required]""")
@click.option('--db-system-id', callback=cli_util.handle_required_param, help="""The [OCID] of the DB System. [required]""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return.""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The pagination token to continue listing from.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[DbNodeSummary]'})
@cli_util.wrap_exceptions
def list_db_nodes(ctx, from_json, all_pages, page_size, compartment_id, db_system_id, limit, page):

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

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_db_nodes,
            compartment_id=compartment_id,
            db_system_id=db_system_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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


@patch_history_entry_group.command(name=cli_util.override('list_db_system_patch_history_entries.command_name', 'list-db-system'), help="""Gets the history of the patch actions performed on the specified DB System.""")
@click.option('--db-system-id', callback=cli_util.handle_required_param, help="""The DB System [OCID]. [required]""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return.""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The pagination token to continue listing from.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
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

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_db_system_patch_history_entries,
            db_system_id=db_system_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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


@patch_group.command(name=cli_util.override('list_db_system_patches.command_name', 'list-db-system'), help="""Lists the patches applicable to the requested DB System.""")
@click.option('--db-system-id', callback=cli_util.handle_required_param, help="""The DB System [OCID]. [required]""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return.""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The pagination token to continue listing from.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
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

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_db_system_patches,
            db_system_id=db_system_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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


@db_system_shape_group.command(name=cli_util.override('list_db_system_shapes.command_name', 'list'), help="""Gets a list of the shapes that can be used to launch a new DB System. The shape determines resources to allocate to the DB system - CPU cores and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes.""")
@click.option('--availability-domain', callback=cli_util.handle_required_param, help="""The name of the Availability Domain. [required]""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The compartment [OCID]. [required]""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return.""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The pagination token to continue listing from.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
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

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_db_system_shapes,
            availability_domain=availability_domain,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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


@db_system_group.command(name=cli_util.override('list_db_systems.command_name', 'list'), help="""Gets a list of the DB Systems in the specified compartment.""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The compartment [OCID]. [required]""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return.""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The pagination token to continue listing from.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[DbSystemSummary]'})
@cli_util.wrap_exceptions
def list_db_systems(ctx, from_json, all_pages, page_size, compartment_id, limit, page):

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

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_db_systems,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The compartment [OCID]. [required]""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return.""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The pagination token to continue listing from.""")
@click.option('--db-system-shape', callback=cli_util.handle_optional_param, help="""If provided, filters the results to the set of database versions which are supported for the given shape.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[DbVersionSummary]'})
@cli_util.wrap_exceptions
def list_db_versions(ctx, from_json, all_pages, page_size, compartment_id, limit, page, db_system_shape):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if db_system_shape is not None:
        kwargs['db_system_shape'] = db_system_shape
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_db_versions,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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
@click.option('--database-id', callback=cli_util.handle_required_param, help="""The database [OCID]. [required]""")
@click.option('--data-guard-association-id', callback=cli_util.handle_required_param, help="""The Data Guard association's [OCID]. [required]""")
@click.option('--database-admin-password', callback=cli_util.handle_required_param, help="""The DB System administrator password. [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DataGuardAssociation'})
@cli_util.wrap_exceptions
def reinstate_data_guard_association(ctx, from_json, database_id, data_guard_association_id, database_admin_password, if_match):

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
    cli_util.render_response(result, ctx)


@database_group.command(name=cli_util.override('restore_database.command_name', 'restore'), help="""Restore a Database based on the request parameters you provide.""")
@click.option('--database-id', callback=cli_util.handle_required_param, help="""The database [OCID]. [required]""")
@click.option('--database-scn', callback=cli_util.handle_optional_param, help="""Restores using the backup with the System Change Number (SCN) specified.""")
@click.option('--latest', callback=cli_util.handle_optional_param, type=click.BOOL, help="""Restores to the last known good state with the least possible data loss.""")
@click.option('--timestamp', callback=cli_util.handle_optional_param, type=custom_types.CLI_DATETIME, help="""Restores to the timestamp specified.""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'Database'})
@cli_util.wrap_exceptions
def restore_database(ctx, from_json, database_id, database_scn, latest, timestamp, if_match):

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
    cli_util.render_response(result, ctx)


@data_guard_association_group.command(name=cli_util.override('switchover_data_guard_association.command_name', 'switchover'), help="""Performs a switchover to transition the primary database of a Data Guard association into a standby role. The standby database associated with the `dataGuardAssociationId` assumes the primary database role.

A switchover guarantees no data loss.""")
@click.option('--database-id', callback=cli_util.handle_required_param, help="""The database [OCID]. [required]""")
@click.option('--data-guard-association-id', callback=cli_util.handle_required_param, help="""The Data Guard association's [OCID]. [required]""")
@click.option('--database-admin-password', callback=cli_util.handle_required_param, help="""The DB System administrator password. [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DataGuardAssociation'})
@cli_util.wrap_exceptions
def switchover_data_guard_association(ctx, from_json, database_id, data_guard_association_id, database_admin_password, if_match):

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
    cli_util.render_response(result, ctx)


@db_system_group.command(name=cli_util.override('terminate_db_system.command_name', 'terminate'), help="""Terminates a DB System and permanently deletes it and any databases running on it, and any storage volumes attached to it. The database data is local to the DB System and will be lost when the system is terminated. Oracle recommends that you back up any data in the DB System prior to terminating it.""")
@click.option('--db-system-id', callback=cli_util.handle_required_param, help="""The DB System [OCID]. [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
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
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_db_system, db_system_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@database_group.command(name=cli_util.override('update_database.command_name', 'update'), help="""Update a Database based on the request parameters you provide.""")
@click.option('--database-id', callback=cli_util.handle_required_param, help="""The database [OCID]. [required]""")
@click.option('--db-backup-config', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--force', callback=cli_util.handle_optional_param, help="""Perform update without prompting for confirmation.""", is_flag=True)
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "BACKUP_IN_PROGRESS", "TERMINATING", "TERMINATED", "RESTORE_FAILED", "FAILED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'db-backup-config': {'module': 'database', 'class': 'DbBackupConfig'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'db-backup-config': {'module': 'database', 'class': 'DbBackupConfig'}}, output_type={'module': 'database', 'class': 'Database'})
@cli_util.wrap_exceptions
def update_database(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, database_id, db_backup_config, if_match):

    if isinstance(database_id, six.string_types) and len(database_id.strip()) == 0:
        raise click.UsageError('Parameter --database-id cannot be whitespace or empty string')
    if not force:
        if db_backup_config:
            if not click.confirm("WARNING: Updates to db-backup-config will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if db_backup_config is not None:
        details['dbBackupConfig'] = cli_util.parse_json_parameter("db_backup_config", db_backup_config)

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
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_database, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_home_group.command(name=cli_util.override('update_db_home.command_name', 'update'), help="""Patches the specified dbHome.""")
@click.option('--db-home-id', callback=cli_util.handle_required_param, help="""The database home [OCID]. [required]""")
@click.option('--db-version', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--force', callback=cli_util.handle_optional_param, help="""Perform update without prompting for confirmation.""", is_flag=True)
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
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
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_db_home, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_system_group.command(name=cli_util.override('update_db_system.command_name', 'update'), help="""Updates the properties of a DB System, such as the CPU core count.""")
@click.option('--db-system-id', callback=cli_util.handle_required_param, help="""The DB System [OCID]. [required]""")
@click.option('--cpu-core-count', callback=cli_util.handle_optional_param, type=click.INT, help="""The number of CPU Cores to be set on the DB System. Applicable only for non-VM based DB systems.""")
@click.option('--data-storage-size-in-gbs', callback=cli_util.handle_optional_param, type=click.INT, help="""Size, in GBs, to which the currently attached storage needs to be scaled up to for VM based DB system. This must be greater than current storage size. Note that the total storage size attached will be more than what is requested, to account for REDO/RECO space and software volume.""")
@click.option('--ssh-public-keys', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""The public key portion of the key pair to use for SSH access to the DB System. Multiple public keys can be provided. The length of the combined keys cannot exceed 10,000 characters.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--version', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--force', callback=cli_util.handle_optional_param, help="""Perform update without prompting for confirmation.""", is_flag=True)
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}, 'version': {'module': 'database', 'class': 'PatchDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}, 'version': {'module': 'database', 'class': 'PatchDetails'}}, output_type={'module': 'database', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def update_db_system(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, db_system_id, cpu_core_count, data_storage_size_in_gbs, ssh_public_keys, version, if_match):

    if isinstance(db_system_id, six.string_types) and len(db_system_id.strip()) == 0:
        raise click.UsageError('Parameter --db-system-id cannot be whitespace or empty string')
    if not force:
        if ssh_public_keys or version:
            if not click.confirm("WARNING: Updates to ssh-public-keys and version will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if cpu_core_count is not None:
        details['cpuCoreCount'] = cpu_core_count

    if data_storage_size_in_gbs is not None:
        details['dataStorageSizeInGBs'] = data_storage_size_in_gbs

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
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_db_system, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
