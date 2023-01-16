# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('database_migration.database_migration_root_group.command_name', 'database-migration'), cls=CommandGroupWithAlias, help=cli_util.override('database_migration.database_migration_root_group.help', """Use the Oracle Cloud Infrastructure Database Migration APIs to perform database migration operations."""), short_help=cli_util.override('database_migration.database_migration_root_group.short_help', """Database Migration API"""))
@cli_util.help_option_group
def database_migration_root_group():
    pass


@click.command(cli_util.override('database_migration.agent_group.command_name', 'agent'), cls=CommandGroupWithAlias, help="""ODMS Agent Details""")
@cli_util.help_option_group
def agent_group():
    pass


@click.command(cli_util.override('database_migration.work_request_summary_group.command_name', 'work-request-summary'), cls=CommandGroupWithAlias, help="""A summary of the status of a work request.""")
@cli_util.help_option_group
def work_request_summary_group():
    pass


@click.command(cli_util.override('database_migration.migration_object_collection_group.command_name', 'migration-object-collection'), cls=CommandGroupWithAlias, help="""Database objects to migrate.""")
@cli_util.help_option_group
def migration_object_collection_group():
    pass


@click.command(cli_util.override('database_migration.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""A log message from executing an operation that is tracked by a work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('database_migration.excluded_object_summary_group.command_name', 'excluded-object-summary'), cls=CommandGroupWithAlias, help="""Excluded object summary line.""")
@cli_util.help_option_group
def excluded_object_summary_group():
    pass


@click.command(cli_util.override('database_migration.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""An asynchronous work request.""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('database_migration.agent_summary_group.command_name', 'agent-summary'), cls=CommandGroupWithAlias, help="""ODMS Agent Details""")
@cli_util.help_option_group
def agent_summary_group():
    pass


@click.command(cli_util.override('database_migration.migration_summary_group.command_name', 'migration-summary'), cls=CommandGroupWithAlias, help="""Migration resource""")
@cli_util.help_option_group
def migration_summary_group():
    pass


@click.command(cli_util.override('database_migration.agent_image_summary_group.command_name', 'agent-image-summary'), cls=CommandGroupWithAlias, help="""Available ODMS Agent Images.""")
@cli_util.help_option_group
def agent_image_summary_group():
    pass


@click.command(cli_util.override('database_migration.connection_summary_group.command_name', 'connection-summary'), cls=CommandGroupWithAlias, help="""Database Connection Summary.""")
@cli_util.help_option_group
def connection_summary_group():
    pass


@click.command(cli_util.override('database_migration.job_summary_group.command_name', 'job-summary'), cls=CommandGroupWithAlias, help="""Job description""")
@cli_util.help_option_group
def job_summary_group():
    pass


@click.command(cli_util.override('database_migration.migration_object_type_summary_group.command_name', 'migration-object-type-summary'), cls=CommandGroupWithAlias, help="""Migration Object Type""")
@cli_util.help_option_group
def migration_object_type_summary_group():
    pass


@click.command(cli_util.override('database_migration.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing an operation that is tracked by a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('database_migration.migration_group.command_name', 'migration'), cls=CommandGroupWithAlias, help="""Migration resource""")
@cli_util.help_option_group
def migration_group():
    pass


@click.command(cli_util.override('database_migration.connection_group.command_name', 'connection'), cls=CommandGroupWithAlias, help="""Database Connection resource used for migrations.""")
@cli_util.help_option_group
def connection_group():
    pass


@click.command(cli_util.override('database_migration.job_group.command_name', 'job'), cls=CommandGroupWithAlias, help="""Results of a Database Connection search. Contains DatabaseConnectionSummary items.""")
@cli_util.help_option_group
def job_group():
    pass


@click.command(cli_util.override('database_migration.job_output_summary_group.command_name', 'job-output-summary'), cls=CommandGroupWithAlias, help="""Job output summary line.""")
@cli_util.help_option_group
def job_output_summary_group():
    pass


database_migration_root_group.add_command(agent_group)
database_migration_root_group.add_command(work_request_summary_group)
database_migration_root_group.add_command(migration_object_collection_group)
database_migration_root_group.add_command(work_request_log_entry_group)
database_migration_root_group.add_command(excluded_object_summary_group)
database_migration_root_group.add_command(work_request_group)
database_migration_root_group.add_command(agent_summary_group)
database_migration_root_group.add_command(migration_summary_group)
database_migration_root_group.add_command(agent_image_summary_group)
database_migration_root_group.add_command(connection_summary_group)
database_migration_root_group.add_command(job_summary_group)
database_migration_root_group.add_command(migration_object_type_summary_group)
database_migration_root_group.add_command(work_request_error_group)
database_migration_root_group.add_command(migration_group)
database_migration_root_group.add_command(connection_group)
database_migration_root_group.add_command(job_group)
database_migration_root_group.add_command(job_output_summary_group)


@job_group.command(name=cli_util.override('database_migration.abort_job.command_name', 'abort'), help=u"""Aborts a Migration Job (either Evaluation or Migration). \n[Command Reference](abortJob)""")
@cli_util.option('--job-id', required=True, help=u"""The OCID of the job""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "UNKNOWN", "TERMINATED", "FAILED", "SUCCEEDED", "WAITING", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_migration', 'class': 'Job'})
@cli_util.wrap_exceptions
def abort_job(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, job_id, if_match):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    result = client.abort_job(
        job_id=job_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@migration_group.command(name=cli_util.override('database_migration.add_migration_objects.command_name', 'add'), help=u"""Add excluded/included object to the list. \n[Command Reference](addMigrationObjects)""")
@cli_util.option('--migration-id', required=True, help=u"""The OCID of the migration""")
@cli_util.option('--items', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Database objects to exclude/include from migration""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'database_migration', 'class': 'list[MigrationObjectSummary]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'database_migration', 'class': 'list[MigrationObjectSummary]'}})
@cli_util.wrap_exceptions
def add_migration_objects(ctx, from_json, migration_id, items, if_match):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    result = client.add_migration_objects(
        migration_id=migration_id,
        add_migration_objects_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@agent_group.command(name=cli_util.override('database_migration.change_agent_compartment.command_name', 'change-compartment'), help=u"""Used to configure an ODMS Agent Compartment ID. \n[Command Reference](changeAgentCompartment)""")
@cli_util.option('--agent-id', required=True, help=u"""The OCID of the agent""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to move the resource to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_agent_compartment(ctx, from_json, agent_id, compartment_id, if_match):

    if isinstance(agent_id, six.string_types) and len(agent_id.strip()) == 0:
        raise click.UsageError('Parameter --agent-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    result = client.change_agent_compartment(
        agent_id=agent_id,
        change_agent_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_group.command(name=cli_util.override('database_migration.change_connection_compartment.command_name', 'change-compartment'), help=u"""Used to change the Database Connection compartment. \n[Command Reference](changeConnectionCompartment)""")
@cli_util.option('--connection-id', required=True, help=u"""The OCID of the database connection""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to move the resource to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_connection_compartment(ctx, from_json, connection_id, compartment_id, if_match):

    if isinstance(connection_id, six.string_types) and len(connection_id.strip()) == 0:
        raise click.UsageError('Parameter --connection-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    result = client.change_connection_compartment(
        connection_id=connection_id,
        change_connection_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@migration_group.command(name=cli_util.override('database_migration.change_migration_compartment.command_name', 'change-compartment'), help=u"""Used to change the Migration compartment. \n[Command Reference](changeMigrationCompartment)""")
@cli_util.option('--migration-id', required=True, help=u"""The OCID of the migration""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to move the resource to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_migration_compartment(ctx, from_json, migration_id, compartment_id, if_match):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    result = client.change_migration_compartment(
        migration_id=migration_id,
        change_migration_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@migration_group.command(name=cli_util.override('database_migration.clone_migration.command_name', 'clone'), help=u"""Clone a configuration from an existing Migration. \n[Command Reference](cloneMigration)""")
@cli_util.option('--migration-id', required=True, help=u"""The OCID of the migration""")
@cli_util.option('--source-database-connection-id', required=True, help=u"""The OCID of the Source Database Connection.""")
@cli_util.option('--target-database-connection-id', required=True, help=u"""The OCID of the Target Database Connection.""")
@cli_util.option('--display-name', help=u"""Migration Display Name""")
@cli_util.option('--compartment-id', help=u"""OCID of the compartment""")
@cli_util.option('--agent-id', help=u"""The OCID of the registered on-premises ODMS Agent. Only valid for Offline Logical Migrations.""")
@cli_util.option('--source-container-database-connection-id', help=u"""The OCID of the Source Container Database Connection. Only used for Online migrations. Only Connections of type Non-Autonomous can be used as source container databases.""")
@cli_util.option('--exclude-objects', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Database objects to exclude from migration, cannot be specified alongside 'includeObjects'

This option is a JSON list with items of type DatabaseObject.  For documentation on DatabaseObject please see our API reference: https://docs.cloud.oracle.com/api/#/en/databasemigration/20210929/datatypes/DatabaseObject.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--include-objects', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Database objects to include from migration, cannot be specified alongside 'excludeObjects'

This option is a JSON list with items of type DatabaseObject.  For documentation on DatabaseObject please see our API reference: https://docs.cloud.oracle.com/api/#/en/databasemigration/20210929/datatypes/DatabaseObject.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vault-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'exclude-objects': {'module': 'database_migration', 'class': 'list[DatabaseObject]'}, 'include-objects': {'module': 'database_migration', 'class': 'list[DatabaseObject]'}, 'vault-details': {'module': 'database_migration', 'class': 'CreateVaultDetails'}, 'freeform-tags': {'module': 'database_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'exclude-objects': {'module': 'database_migration', 'class': 'list[DatabaseObject]'}, 'include-objects': {'module': 'database_migration', 'class': 'list[DatabaseObject]'}, 'vault-details': {'module': 'database_migration', 'class': 'CreateVaultDetails'}, 'freeform-tags': {'module': 'database_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database_migration', 'class': 'Migration'})
@cli_util.wrap_exceptions
def clone_migration(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, migration_id, source_database_connection_id, target_database_connection_id, display_name, compartment_id, agent_id, source_container_database_connection_id, exclude_objects, include_objects, vault_details, freeform_tags, defined_tags, if_match):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['sourceDatabaseConnectionId'] = source_database_connection_id
    _details['targetDatabaseConnectionId'] = target_database_connection_id

    if display_name is not None:
        _details['displayName'] = display_name

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if agent_id is not None:
        _details['agentId'] = agent_id

    if source_container_database_connection_id is not None:
        _details['sourceContainerDatabaseConnectionId'] = source_container_database_connection_id

    if exclude_objects is not None:
        _details['excludeObjects'] = cli_util.parse_json_parameter("exclude_objects", exclude_objects)

    if include_objects is not None:
        _details['includeObjects'] = cli_util.parse_json_parameter("include_objects", include_objects)

    if vault_details is not None:
        _details['vaultDetails'] = cli_util.parse_json_parameter("vault_details", vault_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    result = client.clone_migration(
        migration_id=migration_id,
        clone_migration_details=_details,
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

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
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


@connection_group.command(name=cli_util.override('database_migration.create_connection.command_name', 'create'), help=u"""Create a Database Connection resource that contains the details to connect to either a Source or Target Database in the migration. \n[Command Reference](createConnection)""")
@cli_util.option('--compartment-id', required=True, help=u"""OCID of the compartment""")
@cli_util.option('--database-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["MANUAL", "AUTONOMOUS", "USER_MANAGED_OCI"]), help=u"""Database connection type.""")
@cli_util.option('--admin-credentials', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vault-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Database Connection display name identifier.""")
@cli_util.option('--manual-database-sub-type', type=custom_types.CliCaseInsensitiveChoice(["ORACLE", "RDS_ORACLE"]), help=u"""Database manual connection subtype. This value can only be specified for manual connections.""")
@cli_util.option('--database-id', help=u"""The OCID of the cloud database. Required if the database connection type is Autonomous.""")
@cli_util.option('--connect-descriptor', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--certificate-tdn', help=u"""This name is the distinguished name used while creating the certificate on target database. Requires a TLS wallet to be specified. Not required for source container database connections.""")
@cli_util.option('--tls-wallet', help=u"""cwallet.sso containing containing the TCPS/SSL certificate; base64 encoded String. Not required for source container database connections.""")
@cli_util.option('--tls-keystore', help=u"""keystore.jks file contents; base64 encoded String. Requires a TLS wallet to be specified. Not required for source container database connections.""")
@cli_util.option('--ssh-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--private-endpoint', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of Network Security Group OCIDs used to define network access for Connections.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'connect-descriptor': {'module': 'database_migration', 'class': 'CreateConnectDescriptor'}, 'ssh-details': {'module': 'database_migration', 'class': 'CreateSshDetails'}, 'admin-credentials': {'module': 'database_migration', 'class': 'CreateAdminCredentials'}, 'private-endpoint': {'module': 'database_migration', 'class': 'CreatePrivateEndpoint'}, 'vault-details': {'module': 'database_migration', 'class': 'CreateVaultDetails'}, 'freeform-tags': {'module': 'database_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database_migration', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'database_migration', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'connect-descriptor': {'module': 'database_migration', 'class': 'CreateConnectDescriptor'}, 'ssh-details': {'module': 'database_migration', 'class': 'CreateSshDetails'}, 'admin-credentials': {'module': 'database_migration', 'class': 'CreateAdminCredentials'}, 'private-endpoint': {'module': 'database_migration', 'class': 'CreatePrivateEndpoint'}, 'vault-details': {'module': 'database_migration', 'class': 'CreateVaultDetails'}, 'freeform-tags': {'module': 'database_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database_migration', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'database_migration', 'class': 'list[string]'}}, output_type={'module': 'database_migration', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, database_type, admin_credentials, vault_details, display_name, manual_database_sub_type, database_id, connect_descriptor, certificate_tdn, tls_wallet, tls_keystore, ssh_details, private_endpoint, freeform_tags, defined_tags, nsg_ids):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['databaseType'] = database_type
    _details['adminCredentials'] = cli_util.parse_json_parameter("admin_credentials", admin_credentials)
    _details['vaultDetails'] = cli_util.parse_json_parameter("vault_details", vault_details)

    if display_name is not None:
        _details['displayName'] = display_name

    if manual_database_sub_type is not None:
        _details['manualDatabaseSubType'] = manual_database_sub_type

    if database_id is not None:
        _details['databaseId'] = database_id

    if connect_descriptor is not None:
        _details['connectDescriptor'] = cli_util.parse_json_parameter("connect_descriptor", connect_descriptor)

    if certificate_tdn is not None:
        _details['certificateTdn'] = certificate_tdn

    if tls_wallet is not None:
        _details['tlsWallet'] = tls_wallet

    if tls_keystore is not None:
        _details['tlsKeystore'] = tls_keystore

    if ssh_details is not None:
        _details['sshDetails'] = cli_util.parse_json_parameter("ssh_details", ssh_details)

    if private_endpoint is not None:
        _details['privateEndpoint'] = cli_util.parse_json_parameter("private_endpoint", private_endpoint)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    result = client.create_connection(
        create_connection_details=_details,
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

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
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


@migration_group.command(name=cli_util.override('database_migration.create_migration.command_name', 'create'), help=u"""Create a Migration resource that contains all the details to perform the database migration operation, such as source and destination database details, credentials, etc. \n[Command Reference](createMigration)""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["ONLINE", "OFFLINE"]), help=u"""Migration type.""")
@cli_util.option('--compartment-id', required=True, help=u"""OCID of the compartment""")
@cli_util.option('--source-database-connection-id', required=True, help=u"""The OCID of the Source Database Connection.""")
@cli_util.option('--target-database-connection-id', required=True, help=u"""The OCID of the Target Database Connection.""")
@cli_util.option('--display-name', help=u"""Migration Display Name""")
@cli_util.option('--agent-id', help=u"""The OCID of the registered ODMS Agent. Only valid for Offline Logical Migrations.""")
@cli_util.option('--source-container-database-connection-id', help=u"""The OCID of the Source Container Database Connection. Only used for Online migrations. Only Connections of type Non-Autonomous can be used as source container databases.""")
@cli_util.option('--data-transfer-medium-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--dump-transfer-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--datapump-settings', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--advisor-settings', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--exclude-objects', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Database objects to exclude from migration, cannot be specified alongside 'includeObjects'

This option is a JSON list with items of type DatabaseObject.  For documentation on DatabaseObject please see our API reference: https://docs.cloud.oracle.com/api/#/en/databasemigration/20210929/datatypes/DatabaseObject.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--include-objects', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Database objects to include from migration, cannot be specified alongside 'excludeObjects'

This option is a JSON list with items of type DatabaseObject.  For documentation on DatabaseObject please see our API reference: https://docs.cloud.oracle.com/api/#/en/databasemigration/20210929/datatypes/DatabaseObject.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--golden-gate-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vault-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'data-transfer-medium-details': {'module': 'database_migration', 'class': 'CreateDataTransferMediumDetails'}, 'dump-transfer-details': {'module': 'database_migration', 'class': 'CreateDumpTransferDetails'}, 'datapump-settings': {'module': 'database_migration', 'class': 'CreateDataPumpSettings'}, 'advisor-settings': {'module': 'database_migration', 'class': 'CreateAdvisorSettings'}, 'exclude-objects': {'module': 'database_migration', 'class': 'list[DatabaseObject]'}, 'include-objects': {'module': 'database_migration', 'class': 'list[DatabaseObject]'}, 'golden-gate-details': {'module': 'database_migration', 'class': 'CreateGoldenGateDetails'}, 'vault-details': {'module': 'database_migration', 'class': 'CreateVaultDetails'}, 'freeform-tags': {'module': 'database_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'data-transfer-medium-details': {'module': 'database_migration', 'class': 'CreateDataTransferMediumDetails'}, 'dump-transfer-details': {'module': 'database_migration', 'class': 'CreateDumpTransferDetails'}, 'datapump-settings': {'module': 'database_migration', 'class': 'CreateDataPumpSettings'}, 'advisor-settings': {'module': 'database_migration', 'class': 'CreateAdvisorSettings'}, 'exclude-objects': {'module': 'database_migration', 'class': 'list[DatabaseObject]'}, 'include-objects': {'module': 'database_migration', 'class': 'list[DatabaseObject]'}, 'golden-gate-details': {'module': 'database_migration', 'class': 'CreateGoldenGateDetails'}, 'vault-details': {'module': 'database_migration', 'class': 'CreateVaultDetails'}, 'freeform-tags': {'module': 'database_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database_migration', 'class': 'Migration'})
@cli_util.wrap_exceptions
def create_migration(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, type, compartment_id, source_database_connection_id, target_database_connection_id, display_name, agent_id, source_container_database_connection_id, data_transfer_medium_details, dump_transfer_details, datapump_settings, advisor_settings, exclude_objects, include_objects, golden_gate_details, vault_details, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['type'] = type
    _details['compartmentId'] = compartment_id
    _details['sourceDatabaseConnectionId'] = source_database_connection_id
    _details['targetDatabaseConnectionId'] = target_database_connection_id

    if display_name is not None:
        _details['displayName'] = display_name

    if agent_id is not None:
        _details['agentId'] = agent_id

    if source_container_database_connection_id is not None:
        _details['sourceContainerDatabaseConnectionId'] = source_container_database_connection_id

    if data_transfer_medium_details is not None:
        _details['dataTransferMediumDetails'] = cli_util.parse_json_parameter("data_transfer_medium_details", data_transfer_medium_details)

    if dump_transfer_details is not None:
        _details['dumpTransferDetails'] = cli_util.parse_json_parameter("dump_transfer_details", dump_transfer_details)

    if datapump_settings is not None:
        _details['datapumpSettings'] = cli_util.parse_json_parameter("datapump_settings", datapump_settings)

    if advisor_settings is not None:
        _details['advisorSettings'] = cli_util.parse_json_parameter("advisor_settings", advisor_settings)

    if exclude_objects is not None:
        _details['excludeObjects'] = cli_util.parse_json_parameter("exclude_objects", exclude_objects)

    if include_objects is not None:
        _details['includeObjects'] = cli_util.parse_json_parameter("include_objects", include_objects)

    if golden_gate_details is not None:
        _details['goldenGateDetails'] = cli_util.parse_json_parameter("golden_gate_details", golden_gate_details)

    if vault_details is not None:
        _details['vaultDetails'] = cli_util.parse_json_parameter("vault_details", vault_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    result = client.create_migration(
        create_migration_details=_details,
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

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
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


@agent_group.command(name=cli_util.override('database_migration.delete_agent.command_name', 'delete'), help=u"""Delete the ODMS Agent represented by the specified ODMS Agent ID. \n[Command Reference](deleteAgent)""")
@cli_util.option('--agent-id', required=True, help=u"""The OCID of the agent""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_agent(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, agent_id, if_match):

    if isinstance(agent_id, six.string_types) and len(agent_id.strip()) == 0:
        raise click.UsageError('Parameter --agent-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    result = client.delete_agent(
        agent_id=agent_id,
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

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@connection_group.command(name=cli_util.override('database_migration.delete_connection.command_name', 'delete'), help=u"""Deletes the Database Connection represented by the specified connection ID. \n[Command Reference](deleteConnection)""")
@cli_util.option('--connection-id', required=True, help=u"""The OCID of the database connection""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_connection(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, connection_id, if_match):

    if isinstance(connection_id, six.string_types) and len(connection_id.strip()) == 0:
        raise click.UsageError('Parameter --connection-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    result = client.delete_connection(
        connection_id=connection_id,
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

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('database_migration.delete_job.command_name', 'delete'), help=u"""Deletes the migration job represented by the given job ID. \n[Command Reference](deleteJob)""")
@cli_util.option('--job-id', required=True, help=u"""The OCID of the job""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "UNKNOWN", "TERMINATED", "FAILED", "SUCCEEDED", "WAITING", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_job(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, job_id, if_match):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    result = client.delete_job(
        job_id=job_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_job(job_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@migration_group.command(name=cli_util.override('database_migration.delete_migration.command_name', 'delete'), help=u"""Deletes the Migration represented by the specified migration ID. \n[Command Reference](deleteMigration)""")
@cli_util.option('--migration-id', required=True, help=u"""The OCID of the migration""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_migration(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, migration_id, if_match):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    result = client.delete_migration(
        migration_id=migration_id,
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

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('database_migration.evaluate_migration.command_name', 'evaluate-migration'), help=u"""Start Validate Migration job. \n[Command Reference](evaluateMigration)""")
@cli_util.option('--migration-id', required=True, help=u"""The OCID of the migration""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_migration', 'class': 'Job'})
@cli_util.wrap_exceptions
def evaluate_migration(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, migration_id, if_match):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    result = client.evaluate_migration(
        migration_id=migration_id,
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

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
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


@job_group.command(name=cli_util.override('database_migration.get_advisor_report.command_name', 'get-advisor-report'), help=u"""Get the Pre-Migration Advisor report details \n[Command Reference](getAdvisorReport)""")
@cli_util.option('--job-id', required=True, help=u"""The OCID of the job""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_migration', 'class': 'AdvisorReport'})
@cli_util.wrap_exceptions
def get_advisor_report(ctx, from_json, job_id):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    result = client.get_advisor_report(
        job_id=job_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@agent_group.command(name=cli_util.override('database_migration.get_agent.command_name', 'get'), help=u"""Display the ODMS Agent configuration. \n[Command Reference](getAgent)""")
@cli_util.option('--agent-id', required=True, help=u"""The OCID of the agent""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_migration', 'class': 'Agent'})
@cli_util.wrap_exceptions
def get_agent(ctx, from_json, agent_id):

    if isinstance(agent_id, six.string_types) and len(agent_id.strip()) == 0:
        raise click.UsageError('Parameter --agent-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    result = client.get_agent(
        agent_id=agent_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_group.command(name=cli_util.override('database_migration.get_connection.command_name', 'get'), help=u"""Display Database Connection details. \n[Command Reference](getConnection)""")
@cli_util.option('--connection-id', required=True, help=u"""The OCID of the database connection""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_migration', 'class': 'Connection'})
@cli_util.wrap_exceptions
def get_connection(ctx, from_json, connection_id):

    if isinstance(connection_id, six.string_types) and len(connection_id.strip()) == 0:
        raise click.UsageError('Parameter --connection-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    result = client.get_connection(
        connection_id=connection_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('database_migration.get_job.command_name', 'get'), help=u"""Get a migration job. \n[Command Reference](getJob)""")
@cli_util.option('--job-id', required=True, help=u"""The OCID of the job""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_migration', 'class': 'Job'})
@cli_util.wrap_exceptions
def get_job(ctx, from_json, job_id):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    result = client.get_job(
        job_id=job_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('database_migration.get_job_output_content.command_name', 'get-job-output-content'), help=u"""Get the migration Job Output content as a String. \n[Command Reference](getJobOutputContent)""")
@cli_util.option('--job-id', required=True, help=u"""The OCID of the job""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_job_output_content(ctx, from_json, file, job_id):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    result = client.get_job_output_content(
        job_id=job_id,
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


@migration_group.command(name=cli_util.override('database_migration.get_migration.command_name', 'get'), help=u"""Display Migration details. \n[Command Reference](getMigration)""")
@cli_util.option('--migration-id', required=True, help=u"""The OCID of the migration""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_migration', 'class': 'Migration'})
@cli_util.wrap_exceptions
def get_migration(ctx, from_json, migration_id, if_match):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    result = client.get_migration(
        migration_id=migration_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('database_migration.get_work_request.command_name', 'get'), help=u"""Gets the details of a work request. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_migration', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@agent_image_summary_group.command(name=cli_util.override('database_migration.list_agent_images.command_name', 'list-agent-images'), help=u"""Get details of the ODMS Agent Images available to install on-premises. \n[Command Reference](listAgentImages)""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_migration', 'class': 'AgentImageCollection'})
@cli_util.wrap_exceptions
def list_agent_images(ctx, from_json, all_pages, page_size, limit, page, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_agent_images,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_agent_images,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_agent_images(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@agent_summary_group.command(name=cli_util.override('database_migration.list_agents.command_name', 'list-agents'), help=u"""Display the name of all the existing ODMS Agents in the server. \n[Command Reference](listAgents)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The current state of the Database Migration Deployment.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_migration', 'class': 'AgentCollection'})
@cli_util.wrap_exceptions
def list_agents(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_by, sort_order, display_name, lifecycle_state):

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
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_agents,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_agents,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_agents(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@connection_summary_group.command(name=cli_util.override('database_migration.list_connections.command_name', 'list-connections'), help=u"""List all Database Connections. \n[Command Reference](listConnections)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The current state of the Database Migration Deployment.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_migration', 'class': 'ConnectionCollection'})
@cli_util.wrap_exceptions
def list_connections(ctx, from_json, all_pages, page_size, compartment_id, display_name, limit, page, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
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
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_connections,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_connections,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_connections(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@excluded_object_summary_group.command(name=cli_util.override('database_migration.list_excluded_objects.command_name', 'list-excluded-objects'), help=u"""List the excluded database objects. \n[Command Reference](listExcludedObjects)""")
@cli_util.option('--job-id', required=True, help=u"""The OCID of the job""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["type", "reasonCategory"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for reasonCategory is ascending. If no value is specified reasonCategory is default.""")
@cli_util.option('--type', help=u"""Excluded object type.""")
@cli_util.option('--owner', help=u"""Excluded object owner""")
@cli_util.option('--object', help=u"""Excluded object name""")
@cli_util.option('--owner-contains', help=u"""Excluded object owner which contains provided value.""")
@cli_util.option('--object-contains', help=u"""Excluded object name which contains provided value.""")
@cli_util.option('--reason-category', type=custom_types.CliCaseInsensitiveChoice(["ORACLE_MAINTAINED", "GG_UNSUPPORTED", "USER_EXCLUDED", "MANDATORY_EXCLUDED", "USER_EXCLUDED_TYPE"]), help=u"""Reason category for the excluded object""")
@cli_util.option('--source-rule', help=u"""Exclude object rule that matches the excluded object, if applicable.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_migration', 'class': 'ExcludedObjectSummaryCollection'})
@cli_util.wrap_exceptions
def list_excluded_objects(ctx, from_json, all_pages, page_size, job_id, limit, page, sort_order, sort_by, type, owner, object, owner_contains, object_contains, reason_category, source_rule):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if type is not None:
        kwargs['type'] = type
    if owner is not None:
        kwargs['owner'] = owner
    if object is not None:
        kwargs['object'] = object
    if owner_contains is not None:
        kwargs['owner_contains'] = owner_contains
    if object_contains is not None:
        kwargs['object_contains'] = object_contains
    if reason_category is not None:
        kwargs['reason_category'] = reason_category
    if source_rule is not None:
        kwargs['source_rule'] = source_rule
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_excluded_objects,
            job_id=job_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_excluded_objects,
            limit,
            page_size,
            job_id=job_id,
            **kwargs
        )
    else:
        result = client.list_excluded_objects(
            job_id=job_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@job_output_summary_group.command(name=cli_util.override('database_migration.list_job_outputs.command_name', 'list-job-outputs'), help=u"""List the Job Outputs \n[Command Reference](listJobOutputs)""")
@cli_util.option('--job-id', required=True, help=u"""The OCID of the job""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_migration', 'class': 'JobOutputSummaryCollection'})
@cli_util.wrap_exceptions
def list_job_outputs(ctx, from_json, all_pages, page_size, job_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_job_outputs,
            job_id=job_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_job_outputs,
            limit,
            page_size,
            job_id=job_id,
            **kwargs
        )
    else:
        result = client.list_job_outputs(
            job_id=job_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@job_summary_group.command(name=cli_util.override('database_migration.list_jobs.command_name', 'list-jobs'), help=u"""List all the names of the Migration jobs associated to the specified migration site. \n[Command Reference](listJobs)""")
@cli_util.option('--migration-id', required=True, help=u"""The ID of the migration in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "UNKNOWN", "TERMINATED", "FAILED", "SUCCEEDED", "WAITING", "CANCELING", "CANCELED"]), help=u"""The lifecycle state of the Migration Job.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_migration', 'class': 'JobCollection'})
@cli_util.wrap_exceptions
def list_jobs(ctx, from_json, all_pages, page_size, migration_id, display_name, limit, page, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
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
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_jobs,
            migration_id=migration_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_jobs,
            limit,
            page_size,
            migration_id=migration_id,
            **kwargs
        )
    else:
        result = client.list_jobs(
            migration_id=migration_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@migration_object_type_summary_group.command(name=cli_util.override('database_migration.list_migration_object_types.command_name', 'list-migration-object-types'), help=u"""Display sample object types to exclude or include for a Migration. \n[Command Reference](listMigrationObjectTypes)""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["name"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for name is custom based on it's usage frequency. If no value is specified name is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_migration', 'class': 'MigrationObjectTypeSummaryCollection'})
@cli_util.wrap_exceptions
def list_migration_object_types(ctx, from_json, all_pages, page_size, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_migration_object_types,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_migration_object_types,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_migration_object_types(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@migration_object_collection_group.command(name=cli_util.override('database_migration.list_migration_objects.command_name', 'list-migration-objects'), help=u"""Display excluded/included objects. \n[Command Reference](listMigrationObjects)""")
@cli_util.option('--migration-id', required=True, help=u"""The OCID of the migration""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_migration', 'class': 'MigrationObjectCollection'})
@cli_util.wrap_exceptions
def list_migration_objects(ctx, from_json, all_pages, page_size, migration_id, if_match, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_migration_objects,
            migration_id=migration_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_migration_objects,
            limit,
            page_size,
            migration_id=migration_id,
            **kwargs
        )
    else:
        result = client.list_migration_objects(
            migration_id=migration_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@migration_summary_group.command(name=cli_util.override('database_migration.list_migrations.command_name', 'list-migrations'), help=u"""List all Migrations. \n[Command Reference](listMigrations)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "IN_PROGRESS", "ACCEPTED", "SUCCEEDED", "CANCELED", "WAITING", "NEEDS_ATTENTION", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The lifecycle state of the Migration.""")
@cli_util.option('--lifecycle-details', type=custom_types.CliCaseInsensitiveChoice(["READY", "ABORTING", "VALIDATING", "VALIDATED", "WAITING", "MIGRATING", "DONE"]), help=u"""The lifecycle detailed status of the Migration.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_migration', 'class': 'MigrationCollection'})
@cli_util.wrap_exceptions
def list_migrations(ctx, from_json, all_pages, page_size, compartment_id, display_name, limit, page, sort_by, sort_order, lifecycle_state, lifecycle_details):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
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
    if lifecycle_details is not None:
        kwargs['lifecycle_details'] = lifecycle_details
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_migrations,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_migrations,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_migrations(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('database_migration.list_work_request_errors.command_name', 'list'), help=u"""Gets the errors for a work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timestamp"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timestamp is descending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_migration', 'class': 'WorkRequestErrorCollection'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_errors,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_errors,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_errors(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_log_entry_group.command(name=cli_util.override('database_migration.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Gets the logs for a work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timestamp"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timestamp is descending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_migration', 'class': 'WorkRequestLogEntryCollection'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_logs,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_logs,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_logs(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_summary_group.command(name=cli_util.override('database_migration.list_work_requests.command_name', 'list-work-requests'), help=u"""Lists the work requests in a compartment or for a specified resource. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--resource-id', help=u"""The [OCID] of the resource.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help=u"""A filter to return only resources their lifecycleState matches the given OperationStatus.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_migration', 'class': 'WorkRequestCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, resource_id, status, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if resource_id is not None:
        kwargs['resource_id'] = resource_id
    if status is not None:
        kwargs['status'] = status
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@migration_group.command(name=cli_util.override('database_migration.remove_migration_objects.command_name', 'remove'), help=u"""Remove excluded/included objects. \n[Command Reference](removeMigrationObjects)""")
@cli_util.option('--migration-id', required=True, help=u"""The OCID of the migration""")
@cli_util.option('--items', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Database objects to exclude/include from migration""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'database_migration', 'class': 'list[MigrationObjectSummary]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'database_migration', 'class': 'list[MigrationObjectSummary]'}})
@cli_util.wrap_exceptions
def remove_migration_objects(ctx, from_json, migration_id, items, if_match):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    result = client.remove_migration_objects(
        migration_id=migration_id,
        remove_migration_objects_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('database_migration.resume_job.command_name', 'resume'), help=u"""Resume a migration Job. \n[Command Reference](resumeJob)""")
@cli_util.option('--job-id', required=True, help=u"""The OCID of the job""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-after', type=custom_types.CliCaseInsensitiveChoice(["ODMS_VALIDATE_TGT", "ODMS_VALIDATE_SRC", "ODMS_VALIDATE_PREMIGRATION_ADVISOR", "ODMS_VALIDATE_GG_HUB", "ODMS_VALIDATE_DATAPUMP_SETTINGS", "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC", "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT", "ODMS_VALIDATE_DATAPUMP_SRC", "ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC", "ODMS_VALIDATE", "ODMS_PREPARE", "ODMS_INITIAL_LOAD_EXPORT", "ODMS_DATA_UPLOAD", "ODMS_INITIAL_LOAD_IMPORT", "ODMS_POST_INITIAL_LOAD", "ODMS_PREPARE_REPLICATION_TARGET", "ODMS_MONITOR_REPLICATION_LAG", "ODMS_SWITCHOVER", "ODMS_CLEANUP"]), help=u"""Name of a migration phase. The Job will wait after executing this phase until Resume Job endpoint is called again.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "UNKNOWN", "TERMINATED", "FAILED", "SUCCEEDED", "WAITING", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_migration', 'class': 'Job'})
@cli_util.wrap_exceptions
def resume_job(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, job_id, if_match, wait_after):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if wait_after is not None:
        _details['waitAfter'] = wait_after

    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    result = client.resume_job(
        job_id=job_id,
        resume_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@migration_group.command(name=cli_util.override('database_migration.retrieve_supported_phases.command_name', 'retrieve-supported-phases'), help=u"""Display Migration Phases for a specified migration. \n[Command Reference](retrieveSupportedPhases)""")
@cli_util.option('--migration-id', required=True, help=u"""The OCID of the migration""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_migration', 'class': 'MigrationPhaseCollection'})
@cli_util.wrap_exceptions
def retrieve_supported_phases(ctx, from_json, migration_id):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    result = client.retrieve_supported_phases(
        migration_id=migration_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('database_migration.start_migration.command_name', 'start-migration'), help=u"""Start Migration job. \n[Command Reference](startMigration)""")
@cli_util.option('--migration-id', required=True, help=u"""The OCID of the migration""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-after', type=custom_types.CliCaseInsensitiveChoice(["ODMS_VALIDATE_TGT", "ODMS_VALIDATE_SRC", "ODMS_VALIDATE_PREMIGRATION_ADVISOR", "ODMS_VALIDATE_GG_HUB", "ODMS_VALIDATE_DATAPUMP_SETTINGS", "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC", "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT", "ODMS_VALIDATE_DATAPUMP_SRC", "ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC", "ODMS_VALIDATE", "ODMS_PREPARE", "ODMS_INITIAL_LOAD_EXPORT", "ODMS_DATA_UPLOAD", "ODMS_INITIAL_LOAD_IMPORT", "ODMS_POST_INITIAL_LOAD", "ODMS_PREPARE_REPLICATION_TARGET", "ODMS_MONITOR_REPLICATION_LAG", "ODMS_SWITCHOVER", "ODMS_CLEANUP"]), help=u"""Name of a migration phase. The Job will wait after executing this phase until the Resume Job endpoint is called.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_migration', 'class': 'Job'})
@cli_util.wrap_exceptions
def start_migration(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, migration_id, if_match, wait_after):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if wait_after is not None:
        _details['waitAfter'] = wait_after

    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    result = client.start_migration(
        migration_id=migration_id,
        start_migration_details=_details,
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

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
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


@agent_group.command(name=cli_util.override('database_migration.update_agent.command_name', 'update'), help=u"""Modifies the ODMS Agent represented by the given ODMS Agent ID. \n[Command Reference](updateAgent)""")
@cli_util.option('--agent-id', required=True, help=u"""The OCID of the agent""")
@cli_util.option('--display-name', help=u"""ODMS Agent name""")
@cli_util.option('--stream-id', help=u"""The OCID of the Stream""")
@cli_util.option('--public-key', help=u"""ODMS Agent public key.""")
@cli_util.option('--version-parameterconflict', help=u"""ODMS Agent version""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'database_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'database_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database_migration', 'class': 'Agent'})
@cli_util.wrap_exceptions
def update_agent(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, agent_id, display_name, stream_id, public_key, version_parameterconflict, freeform_tags, defined_tags, if_match):

    if isinstance(agent_id, six.string_types) and len(agent_id.strip()) == 0:
        raise click.UsageError('Parameter --agent-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if stream_id is not None:
        _details['streamId'] = stream_id

    if public_key is not None:
        _details['publicKey'] = public_key

    if version_parameterconflict is not None:
        _details['version'] = version_parameterconflict

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    result = client.update_agent(
        agent_id=agent_id,
        update_agent_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_agent') and callable(getattr(client, 'get_agent')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_agent(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@connection_group.command(name=cli_util.override('database_migration.update_connection.command_name', 'update'), help=u"""Update Database Connection resource details. \n[Command Reference](updateConnection)""")
@cli_util.option('--connection-id', required=True, help=u"""The OCID of the database connection""")
@cli_util.option('--display-name', help=u"""Database Connection display name identifier.""")
@cli_util.option('--database-id', help=u"""The OCID of the cloud database.""")
@cli_util.option('--connect-descriptor', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--certificate-tdn', help=u"""This name is the distinguished name used while creating the certificate on target database. Not required for source container database connections.""")
@cli_util.option('--tls-wallet', help=u"""cwallet.sso containing containing the TCPS/SSL certificate; base64 encoded String. Not required for source container database connections.""")
@cli_util.option('--tls-keystore', help=u"""keystore.jks file contents; base64 encoded String. Not required for source container database connections.""")
@cli_util.option('--ssh-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--admin-credentials', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--private-endpoint', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vault-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of Network Security Group OCIDs used to define network access for Connections.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'connect-descriptor': {'module': 'database_migration', 'class': 'UpdateConnectDescriptor'}, 'ssh-details': {'module': 'database_migration', 'class': 'UpdateSshDetails'}, 'admin-credentials': {'module': 'database_migration', 'class': 'UpdateAdminCredentials'}, 'private-endpoint': {'module': 'database_migration', 'class': 'UpdatePrivateEndpoint'}, 'vault-details': {'module': 'database_migration', 'class': 'UpdateVaultDetails'}, 'freeform-tags': {'module': 'database_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database_migration', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'database_migration', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'connect-descriptor': {'module': 'database_migration', 'class': 'UpdateConnectDescriptor'}, 'ssh-details': {'module': 'database_migration', 'class': 'UpdateSshDetails'}, 'admin-credentials': {'module': 'database_migration', 'class': 'UpdateAdminCredentials'}, 'private-endpoint': {'module': 'database_migration', 'class': 'UpdatePrivateEndpoint'}, 'vault-details': {'module': 'database_migration', 'class': 'UpdateVaultDetails'}, 'freeform-tags': {'module': 'database_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database_migration', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'database_migration', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_connection(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, connection_id, display_name, database_id, connect_descriptor, certificate_tdn, tls_wallet, tls_keystore, ssh_details, admin_credentials, private_endpoint, vault_details, freeform_tags, defined_tags, nsg_ids, if_match):

    if isinstance(connection_id, six.string_types) and len(connection_id.strip()) == 0:
        raise click.UsageError('Parameter --connection-id cannot be whitespace or empty string')
    if not force:
        if connect_descriptor or ssh_details or admin_credentials or private_endpoint or vault_details or freeform_tags or defined_tags or nsg_ids:
            if not click.confirm("WARNING: Updates to connect-descriptor and ssh-details and admin-credentials and private-endpoint and vault-details and freeform-tags and defined-tags and nsg-ids will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if database_id is not None:
        _details['databaseId'] = database_id

    if connect_descriptor is not None:
        _details['connectDescriptor'] = cli_util.parse_json_parameter("connect_descriptor", connect_descriptor)

    if certificate_tdn is not None:
        _details['certificateTdn'] = certificate_tdn

    if tls_wallet is not None:
        _details['tlsWallet'] = tls_wallet

    if tls_keystore is not None:
        _details['tlsKeystore'] = tls_keystore

    if ssh_details is not None:
        _details['sshDetails'] = cli_util.parse_json_parameter("ssh_details", ssh_details)

    if admin_credentials is not None:
        _details['adminCredentials'] = cli_util.parse_json_parameter("admin_credentials", admin_credentials)

    if private_endpoint is not None:
        _details['privateEndpoint'] = cli_util.parse_json_parameter("private_endpoint", private_endpoint)

    if vault_details is not None:
        _details['vaultDetails'] = cli_util.parse_json_parameter("vault_details", vault_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    result = client.update_connection(
        connection_id=connection_id,
        update_connection_details=_details,
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

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
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


@job_group.command(name=cli_util.override('database_migration.update_job.command_name', 'update'), help=u"""Update Migration Job resource details. \n[Command Reference](updateJob)""")
@cli_util.option('--job-id', required=True, help=u"""The OCID of the job""")
@cli_util.option('--display-name', help=u"""Name of the job.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "UNKNOWN", "TERMINATED", "FAILED", "SUCCEEDED", "WAITING", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'database_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'database_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database_migration', 'class': 'Job'})
@cli_util.wrap_exceptions
def update_job(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, job_id, display_name, freeform_tags, defined_tags, if_match):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    result = client.update_job(
        job_id=job_id,
        update_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@migration_group.command(name=cli_util.override('database_migration.update_migration.command_name', 'update'), help=u"""Update Migration resource details. \n[Command Reference](updateMigration)""")
@cli_util.option('--migration-id', required=True, help=u"""The OCID of the migration""")
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["ONLINE", "OFFLINE"]), help=u"""Migration type.""")
@cli_util.option('--display-name', help=u"""Migration Display Name""")
@cli_util.option('--agent-id', help=u"""The OCID of the registered ODMS Agent.""")
@cli_util.option('--source-database-connection-id', help=u"""The OCID of the Source Database Connection.""")
@cli_util.option('--source-container-database-connection-id', help=u"""The OCID of the Source Container Database Connection. Only used for Online migrations. Only Connections of type Non-Autonomous can be used as source container databases. An empty value would remove the stored Connection ID.""")
@cli_util.option('--target-database-connection-id', help=u"""The OCID of the Target Database Connection.""")
@cli_util.option('--data-transfer-medium-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--dump-transfer-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--datapump-settings', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--advisor-settings', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--exclude-objects', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Database objects to exclude from migration, cannot be specified alongside 'includeObjects'. If specified, the list will be replaced entirely. Empty list will remove stored excludeObjects details.

This option is a JSON list with items of type DatabaseObject.  For documentation on DatabaseObject please see our API reference: https://docs.cloud.oracle.com/api/#/en/databasemigration/20210929/datatypes/DatabaseObject.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--include-objects', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Database objects to include from migration, cannot be specified alongside 'excludeObjects'. If specified, the list will be replaced entirely. Empty list will remove stored includeObjects details.

This option is a JSON list with items of type DatabaseObject.  For documentation on DatabaseObject please see our API reference: https://docs.cloud.oracle.com/api/#/en/databasemigration/20210929/datatypes/DatabaseObject.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--golden-gate-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vault-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'data-transfer-medium-details': {'module': 'database_migration', 'class': 'UpdateDataTransferMediumDetails'}, 'dump-transfer-details': {'module': 'database_migration', 'class': 'UpdateDumpTransferDetails'}, 'datapump-settings': {'module': 'database_migration', 'class': 'UpdateDataPumpSettings'}, 'advisor-settings': {'module': 'database_migration', 'class': 'UpdateAdvisorSettings'}, 'exclude-objects': {'module': 'database_migration', 'class': 'list[DatabaseObject]'}, 'include-objects': {'module': 'database_migration', 'class': 'list[DatabaseObject]'}, 'golden-gate-details': {'module': 'database_migration', 'class': 'UpdateGoldenGateDetails'}, 'vault-details': {'module': 'database_migration', 'class': 'UpdateVaultDetails'}, 'freeform-tags': {'module': 'database_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'data-transfer-medium-details': {'module': 'database_migration', 'class': 'UpdateDataTransferMediumDetails'}, 'dump-transfer-details': {'module': 'database_migration', 'class': 'UpdateDumpTransferDetails'}, 'datapump-settings': {'module': 'database_migration', 'class': 'UpdateDataPumpSettings'}, 'advisor-settings': {'module': 'database_migration', 'class': 'UpdateAdvisorSettings'}, 'exclude-objects': {'module': 'database_migration', 'class': 'list[DatabaseObject]'}, 'include-objects': {'module': 'database_migration', 'class': 'list[DatabaseObject]'}, 'golden-gate-details': {'module': 'database_migration', 'class': 'UpdateGoldenGateDetails'}, 'vault-details': {'module': 'database_migration', 'class': 'UpdateVaultDetails'}, 'freeform-tags': {'module': 'database_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_migration(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, migration_id, type, display_name, agent_id, source_database_connection_id, source_container_database_connection_id, target_database_connection_id, data_transfer_medium_details, dump_transfer_details, datapump_settings, advisor_settings, exclude_objects, include_objects, golden_gate_details, vault_details, freeform_tags, defined_tags, if_match):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')
    if not force:
        if data_transfer_medium_details or dump_transfer_details or datapump_settings or advisor_settings or exclude_objects or include_objects or golden_gate_details or vault_details or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to data-transfer-medium-details and dump-transfer-details and datapump-settings and advisor-settings and exclude-objects and include-objects and golden-gate-details and vault-details and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if type is not None:
        _details['type'] = type

    if display_name is not None:
        _details['displayName'] = display_name

    if agent_id is not None:
        _details['agentId'] = agent_id

    if source_database_connection_id is not None:
        _details['sourceDatabaseConnectionId'] = source_database_connection_id

    if source_container_database_connection_id is not None:
        _details['sourceContainerDatabaseConnectionId'] = source_container_database_connection_id

    if target_database_connection_id is not None:
        _details['targetDatabaseConnectionId'] = target_database_connection_id

    if data_transfer_medium_details is not None:
        _details['dataTransferMediumDetails'] = cli_util.parse_json_parameter("data_transfer_medium_details", data_transfer_medium_details)

    if dump_transfer_details is not None:
        _details['dumpTransferDetails'] = cli_util.parse_json_parameter("dump_transfer_details", dump_transfer_details)

    if datapump_settings is not None:
        _details['datapumpSettings'] = cli_util.parse_json_parameter("datapump_settings", datapump_settings)

    if advisor_settings is not None:
        _details['advisorSettings'] = cli_util.parse_json_parameter("advisor_settings", advisor_settings)

    if exclude_objects is not None:
        _details['excludeObjects'] = cli_util.parse_json_parameter("exclude_objects", exclude_objects)

    if include_objects is not None:
        _details['includeObjects'] = cli_util.parse_json_parameter("include_objects", include_objects)

    if golden_gate_details is not None:
        _details['goldenGateDetails'] = cli_util.parse_json_parameter("golden_gate_details", golden_gate_details)

    if vault_details is not None:
        _details['vaultDetails'] = cli_util.parse_json_parameter("vault_details", vault_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('database_migration', 'database_migration', ctx)
    result = client.update_migration(
        migration_id=migration_id,
        update_migration_details=_details,
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

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
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
