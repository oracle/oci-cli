# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
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


@cli.command(cli_util.override('goldengate.goldengate_root_group.command_name', 'goldengate'), cls=CommandGroupWithAlias, help=cli_util.override('goldengate.goldengate_root_group.help', """Use the Oracle Cloud Infrastructure GoldenGate APIs to perform data replication operations."""), short_help=cli_util.override('goldengate.goldengate_root_group.short_help', """GoldenGate API"""))
@cli_util.help_option_group
def goldengate_root_group():
    pass


@click.command(cli_util.override('goldengate.deployment_backup_group.command_name', 'deployment-backup'), cls=CommandGroupWithAlias, help="""A backup of the current state of the GoldenGate deployment. Can be used to restore a deployment, or create a new deployment with that state as the starting deployment state.""")
@cli_util.help_option_group
def deployment_backup_group():
    pass


@click.command(cli_util.override('goldengate.trail_file_summary_group.command_name', 'trail-file-summary'), cls=CommandGroupWithAlias, help="""Summary of the TrailFiles.""")
@cli_util.help_option_group
def trail_file_summary_group():
    pass


@click.command(cli_util.override('goldengate.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""A log message from the execution of a work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('goldengate.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""The API operations that create and configure GoldenGate resources do not take effect immediately. In these cases, the operation spawns an asynchronous workflow to fulfill the request. Work requests provide visibility into the status of these in-progress, long-running asynchronous workflows.""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('goldengate.message_summary_group.command_name', 'message-summary'), cls=CommandGroupWithAlias, help="""Deployment message Summary.""")
@cli_util.help_option_group
def message_summary_group():
    pass


@click.command(cli_util.override('goldengate.database_registration_group.command_name', 'database-registration'), cls=CommandGroupWithAlias, help="""Represents the metadata description of a database used by deployments in the same compartment.""")
@cli_util.help_option_group
def database_registration_group():
    pass


@click.command(cli_util.override('goldengate.deployment_upgrade_group.command_name', 'deployment-upgrade'), cls=CommandGroupWithAlias, help="""A container for your OCI GoldenGate Upgrade information.""")
@cli_util.help_option_group
def deployment_upgrade_group():
    pass


@click.command(cli_util.override('goldengate.deployment_type_collection_group.command_name', 'deployment-type-collection'), cls=CommandGroupWithAlias, help="""The list of DeploymentTypeDescriptor objects.""")
@cli_util.help_option_group
def deployment_type_collection_group():
    pass


@click.command(cli_util.override('goldengate.connection_assignment_group.command_name', 'connection-assignment'), cls=CommandGroupWithAlias, help="""Represents the metadata description of a connection assignment. Before you can use a connection as a GoldenGate source or target, you must assign it to a deployment.""")
@cli_util.help_option_group
def connection_assignment_group():
    pass


@click.command(cli_util.override('goldengate.trail_sequence_summary_group.command_name', 'trail-sequence-summary'), cls=CommandGroupWithAlias, help="""Summary of the TrailSequences.""")
@cli_util.help_option_group
def trail_sequence_summary_group():
    pass


@click.command(cli_util.override('goldengate.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('goldengate.connection_group.command_name', 'connection'), cls=CommandGroupWithAlias, help="""Represents the metadata description of a connection used by deployments in the same compartment.""")
@cli_util.help_option_group
def connection_group():
    pass


@click.command(cli_util.override('goldengate.deployment_group.command_name', 'deployment'), cls=CommandGroupWithAlias, help="""A container for your OCI GoldenGate resources, such as the OCI GoldenGate deployment console.""")
@cli_util.help_option_group
def deployment_group():
    pass


goldengate_root_group.add_command(deployment_backup_group)
goldengate_root_group.add_command(trail_file_summary_group)
goldengate_root_group.add_command(work_request_log_entry_group)
goldengate_root_group.add_command(work_request_group)
goldengate_root_group.add_command(message_summary_group)
goldengate_root_group.add_command(database_registration_group)
goldengate_root_group.add_command(deployment_upgrade_group)
goldengate_root_group.add_command(deployment_type_collection_group)
goldengate_root_group.add_command(connection_assignment_group)
goldengate_root_group.add_command(trail_sequence_summary_group)
goldengate_root_group.add_command(work_request_error_group)
goldengate_root_group.add_command(connection_group)
goldengate_root_group.add_command(deployment_group)


@deployment_backup_group.command(name=cli_util.override('goldengate.cancel_deployment_backup.command_name', 'cancel'), help=u"""Cancels a Deployment Backup creation process. \n[Command Reference](cancelDeploymentBackup)""")
@cli_util.option('--deployment-backup-id', required=True, help=u"""A unique DeploymentBackup identifier.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["DEFAULT"]), help=u"""The type of a deployment backup cancel""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_deployment_backup(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deployment_backup_id, type, if_match):

    if isinstance(deployment_backup_id, six.string_types) and len(deployment_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --deployment-backup-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['type'] = type

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.cancel_deployment_backup(
        deployment_backup_id=deployment_backup_id,
        cancel_deployment_backup_details=_details,
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


@deployment_backup_group.command(name=cli_util.override('goldengate.cancel_deployment_backup_default_cancel_deployment_backup_details.command_name', 'cancel-deployment-backup-default-cancel-deployment-backup-details'), help=u"""Cancels a Deployment Backup creation process. \n[Command Reference](cancelDeploymentBackup)""")
@cli_util.option('--deployment-backup-id', required=True, help=u"""A unique DeploymentBackup identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_deployment_backup_default_cancel_deployment_backup_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deployment_backup_id, if_match):

    if isinstance(deployment_backup_id, six.string_types) and len(deployment_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --deployment-backup-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    _details['type'] = 'DEFAULT'

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.cancel_deployment_backup(
        deployment_backup_id=deployment_backup_id,
        cancel_deployment_backup_details=_details,
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


@connection_group.command(name=cli_util.override('goldengate.change_connection_compartment.command_name', 'change-compartment'), help=u"""Moves the Connection into a different compartment within the same tenancy. When provided, If-Match is checked against ETag values of the resource.  For information about moving resources between compartments, see [Moving Resources Between Compartments]. \n[Command Reference](changeConnectionCompartment)""")
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of a Connection.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment being referenced.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_connection_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, connection_id, compartment_id, if_match):

    if isinstance(connection_id, six.string_types) and len(connection_id.strip()) == 0:
        raise click.UsageError('Parameter --connection-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.change_connection_compartment(
        connection_id=connection_id,
        change_connection_compartment_details=_details,
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


@database_registration_group.command(name=cli_util.override('goldengate.change_database_registration_compartment.command_name', 'change-compartment'), help=u"""Note: Deprecated. Use the new resource model APIs instead. Moves the DatabaseRegistration into a different compartment within the same tenancy. When provided, If-Match is checked against ETag values of the resource.  For information about moving resources between compartments, see [Moving Resources Between Compartments]. \n[Command Reference](changeDatabaseRegistrationCompartment)""")
@cli_util.option('--database-registration-id', required=True, help=u"""A unique DatabaseRegistration identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment being referenced.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_database_registration_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_registration_id, compartment_id, if_match):

    if isinstance(database_registration_id, six.string_types) and len(database_registration_id.strip()) == 0:
        raise click.UsageError('Parameter --database-registration-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.change_database_registration_compartment(
        database_registration_id=database_registration_id,
        change_database_registration_compartment_details=_details,
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


@deployment_backup_group.command(name=cli_util.override('goldengate.change_deployment_backup_compartment.command_name', 'change-compartment'), help=u"""Moves a DeploymentBackup into a different compartment within the same tenancy.  When provided, If-Match is checked against ETag values of the resource.  For information about moving resources between compartments, see [Moving Resources Between Compartments]. \n[Command Reference](changeDeploymentBackupCompartment)""")
@cli_util.option('--deployment-backup-id', required=True, help=u"""A unique DeploymentBackup identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment being referenced.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_deployment_backup_compartment(ctx, from_json, deployment_backup_id, compartment_id, if_match):

    if isinstance(deployment_backup_id, six.string_types) and len(deployment_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --deployment-backup-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.change_deployment_backup_compartment(
        deployment_backup_id=deployment_backup_id,
        change_deployment_backup_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@deployment_group.command(name=cli_util.override('goldengate.change_deployment_compartment.command_name', 'change-compartment'), help=u"""Moves the Deployment into a different compartment within the same tenancy.  When provided, If-Match is checked against ETag values of the resource.  For information about moving resources between compartments, see [Moving Resources Between Compartments]. \n[Command Reference](changeDeploymentCompartment)""")
@cli_util.option('--deployment-id', required=True, help=u"""A unique Deployment identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment being referenced.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_deployment_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deployment_id, compartment_id, if_match):

    if isinstance(deployment_id, six.string_types) and len(deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --deployment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.change_deployment_compartment(
        deployment_id=deployment_id,
        change_deployment_compartment_details=_details,
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


@connection_group.command(name=cli_util.override('goldengate.create_connection.command_name', 'create'), help=u"""Creates a new Connection. \n[Command Reference](createConnection)""")
@cli_util.option('--connection-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["GOLDENGATE", "KAFKA", "MYSQL", "OCI_OBJECT_STORAGE", "ORACLE"]), help=u"""The connection type.""")
@cli_util.option('--display-name', required=True, help=u"""An object's Display Name.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment being referenced.""")
@cli_util.option('--description', help=u"""Metadata about this specific object.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.

Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Tags defined for this resource. Each key is predefined and scoped to a namespace.

Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vault-id', help=u"""The [OCID] of the customer vault being referenced. If provided, this will reference a vault which the customer will be required to ensure the policies are established to permit the GoldenGate Service to manage secrets contained within this vault.""")
@cli_util.option('--key-id', help=u"""The [OCID] of the customer \"Master\" key being referenced. If provided, this will reference a key which the customer will be required to ensure the policies are established to permit the GoldenGate Service to utilize this key to manage secrets.""")
@cli_util.option('--subnet-id', help=u"""The [OCID] of the subnet being referenced.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}}, output_type={'module': 'golden_gate', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, connection_type, display_name, compartment_id, description, freeform_tags, defined_tags, vault_id, key_id, subnet_id, nsg_ids):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['connectionType'] = connection_type
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if vault_id is not None:
        _details['vaultId'] = vault_id

    if key_id is not None:
        _details['keyId'] = key_id

    if subnet_id is not None:
        _details['subnetId'] = subnet_id

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
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


@connection_group.command(name=cli_util.override('goldengate.create_connection_create_mysql_connection_details.command_name', 'create-connection-create-mysql-connection-details'), help=u"""Creates a new Connection. \n[Command Reference](createConnection)""")
@cli_util.option('--display-name', required=True, help=u"""An object's Display Name.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment being referenced.""")
@cli_util.option('--technology-type', required=True, help=u"""The MySQL technology type.""")
@cli_util.option('--username', required=True, help=u"""The username Oracle GoldenGate uses to connect the associated RDBMS.  This username must already exist and be available for use by the database.  It must conform to the security requirements implemented by the database including length, case sensitivity, and so on.""")
@cli_util.option('--password', required=True, help=u"""The password Oracle GoldenGate uses to connect the associated RDBMS.  It must conform to the specific security requirements implemented by the database including length, case sensitivity, and so on.""")
@cli_util.option('--database-name', required=True, help=u"""The name of the database.""")
@cli_util.option('--security-protocol', required=True, help=u"""Security Type for MySQL.""")
@cli_util.option('--description', help=u"""Metadata about this specific object.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.

Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Tags defined for this resource. Each key is predefined and scoped to a namespace.

Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vault-id', help=u"""The [OCID] of the customer vault being referenced. If provided, this will reference a vault which the customer will be required to ensure the policies are established to permit the GoldenGate Service to manage secrets contained within this vault.""")
@cli_util.option('--key-id', help=u"""The [OCID] of the customer \"Master\" key being referenced. If provided, this will reference a key which the customer will be required to ensure the policies are established to permit the GoldenGate Service to utilize this key to manage secrets.""")
@cli_util.option('--subnet-id', help=u"""The [OCID] of the subnet being referenced.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--host', help=u"""The name or address of a host.""")
@cli_util.option('--port', type=click.INT, help=u"""The port of an endpoint usually specified for a connection.""")
@cli_util.option('--ssl-mode', help=u"""SSL modes for MySQL.""")
@cli_util.option('--ssl-ca', help=u"""Database Certificate - The base64 encoded content of mysql.pem file containing the server public key (for 1 and 2-way SSL).""")
@cli_util.option('--ssl-crl', help=u"""Certificates revoked by certificate authorities (CA). Server certificate must not be on this list (for 1 and 2-way SSL). Note: This is an optional and that too only applicable if TLS/MTLS option is selected.""")
@cli_util.option('--ssl-cert', help=u"""Client Certificate - The base64 encoded content of client-cert.pem file containing the client public key (for 2-way SSL).""")
@cli_util.option('--ssl-key', help=u"""Client Key - The client-key.pem containing the client private key (for 2-way SSL).""")
@cli_util.option('--private-ip', help=u"""The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.""")
@cli_util.option('--additional-attributes', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of name-value pair attribute entries. Used as additional parameters in connection string.

This option is a JSON list with items of type NameValuePair.  For documentation on NameValuePair please see our API reference: https://docs.cloud.oracle.com/api/#/en/goldengate/20200407/datatypes/NameValuePair.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--db-system-id', help=u"""The [OCID] of the database system being referenced.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}, 'additional-attributes': {'module': 'golden_gate', 'class': 'list[NameValuePair]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}, 'additional-attributes': {'module': 'golden_gate', 'class': 'list[NameValuePair]'}}, output_type={'module': 'golden_gate', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection_create_mysql_connection_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, technology_type, username, password, database_name, security_protocol, description, freeform_tags, defined_tags, vault_id, key_id, subnet_id, nsg_ids, host, port, ssl_mode, ssl_ca, ssl_crl, ssl_cert, ssl_key, private_ip, additional_attributes, db_system_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['technologyType'] = technology_type
    _details['username'] = username
    _details['password'] = password
    _details['databaseName'] = database_name
    _details['securityProtocol'] = security_protocol

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if vault_id is not None:
        _details['vaultId'] = vault_id

    if key_id is not None:
        _details['keyId'] = key_id

    if subnet_id is not None:
        _details['subnetId'] = subnet_id

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if host is not None:
        _details['host'] = host

    if port is not None:
        _details['port'] = port

    if ssl_mode is not None:
        _details['sslMode'] = ssl_mode

    if ssl_ca is not None:
        _details['sslCa'] = ssl_ca

    if ssl_crl is not None:
        _details['sslCrl'] = ssl_crl

    if ssl_cert is not None:
        _details['sslCert'] = ssl_cert

    if ssl_key is not None:
        _details['sslKey'] = ssl_key

    if private_ip is not None:
        _details['privateIp'] = private_ip

    if additional_attributes is not None:
        _details['additionalAttributes'] = cli_util.parse_json_parameter("additional_attributes", additional_attributes)

    if db_system_id is not None:
        _details['dbSystemId'] = db_system_id

    _details['connectionType'] = 'MYSQL'

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
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


@connection_group.command(name=cli_util.override('goldengate.create_connection_create_oci_object_storage_connection_details.command_name', 'create-connection-create-oci-object-storage-connection-details'), help=u"""Creates a new Connection. \n[Command Reference](createConnection)""")
@cli_util.option('--display-name', required=True, help=u"""An object's Display Name.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment being referenced.""")
@cli_util.option('--technology-type', required=True, help=u"""The OCI Object Storage technology type.""")
@cli_util.option('--private-key-file', required=True, help=u"""The base64 encoded content of the private key file (PEM file) corresponding to the API key of the fingerprint. See documentation: https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm""")
@cli_util.option('--public-key-fingerprint', required=True, help=u"""The fingerprint of the API Key of the user specified by the userId. See documentation: https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm""")
@cli_util.option('--description', help=u"""Metadata about this specific object.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.

Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Tags defined for this resource. Each key is predefined and scoped to a namespace.

Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vault-id', help=u"""The [OCID] of the customer vault being referenced. If provided, this will reference a vault which the customer will be required to ensure the policies are established to permit the GoldenGate Service to manage secrets contained within this vault.""")
@cli_util.option('--key-id', help=u"""The [OCID] of the customer \"Master\" key being referenced. If provided, this will reference a key which the customer will be required to ensure the policies are established to permit the GoldenGate Service to utilize this key to manage secrets.""")
@cli_util.option('--subnet-id', help=u"""The [OCID] of the subnet being referenced.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--tenancy-id', help=u"""The [OCID] of the related OCI tenancy.""")
@cli_util.option('--region-parameterconflict', help=u"""The name of the region. e.g.: us-ashburn-1""")
@cli_util.option('--user-id', help=u"""The [OCID] of the OCI user who will access the Object Storage. The user must have write access to the bucket they want to connect to.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}}, output_type={'module': 'golden_gate', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection_create_oci_object_storage_connection_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, technology_type, private_key_file, public_key_fingerprint, description, freeform_tags, defined_tags, vault_id, key_id, subnet_id, nsg_ids, tenancy_id, region_parameterconflict, user_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['technologyType'] = technology_type
    _details['privateKeyFile'] = private_key_file
    _details['publicKeyFingerprint'] = public_key_fingerprint

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if vault_id is not None:
        _details['vaultId'] = vault_id

    if key_id is not None:
        _details['keyId'] = key_id

    if subnet_id is not None:
        _details['subnetId'] = subnet_id

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if tenancy_id is not None:
        _details['tenancyId'] = tenancy_id

    if region_parameterconflict is not None:
        _details['region'] = region_parameterconflict

    if user_id is not None:
        _details['userId'] = user_id

    _details['connectionType'] = 'OCI_OBJECT_STORAGE'

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
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


@connection_group.command(name=cli_util.override('goldengate.create_connection_create_kafka_connection_details.command_name', 'create-connection-create-kafka-connection-details'), help=u"""Creates a new Connection. \n[Command Reference](createConnection)""")
@cli_util.option('--display-name', required=True, help=u"""An object's Display Name.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment being referenced.""")
@cli_util.option('--technology-type', required=True, help=u"""The Kafka technology type.""")
@cli_util.option('--description', help=u"""Metadata about this specific object.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.

Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Tags defined for this resource. Each key is predefined and scoped to a namespace.

Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vault-id', help=u"""The [OCID] of the customer vault being referenced. If provided, this will reference a vault which the customer will be required to ensure the policies are established to permit the GoldenGate Service to manage secrets contained within this vault.""")
@cli_util.option('--key-id', help=u"""The [OCID] of the customer \"Master\" key being referenced. If provided, this will reference a key which the customer will be required to ensure the policies are established to permit the GoldenGate Service to utilize this key to manage secrets.""")
@cli_util.option('--subnet-id', help=u"""The [OCID] of the subnet being referenced.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--stream-pool-id', help=u"""The [OCID] of the stream pool being referenced.""")
@cli_util.option('--bootstrap-servers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Kafka bootstrap. Equivalent of bootstrap.servers configuration property in Kafka: list of KafkaBootstrapServer objects specified by host/port. Used for establishing the initial connection to the Kafka cluster. Example: `\"server1.example.com:9092,server2.example.com:9092\"`

This option is a JSON list with items of type KafkaBootstrapServer.  For documentation on KafkaBootstrapServer please see our API reference: https://docs.cloud.oracle.com/api/#/en/goldengate/20200407/datatypes/KafkaBootstrapServer.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--security-protocol', help=u"""Security Type for Kafka.""")
@cli_util.option('--username', help=u"""The username Oracle GoldenGate uses to connect the associated RDBMS.  This username must already exist and be available for use by the database.  It must conform to the security requirements implemented by the database including length, case sensitivity, and so on.""")
@cli_util.option('--password', help=u"""The password Oracle GoldenGate uses to connect the associated RDBMS.  It must conform to the specific security requirements implemented by the database including length, case sensitivity, and so on.""")
@cli_util.option('--trust-store', help=u"""The base64 encoded content of the TrustStore file.""")
@cli_util.option('--trust-store-password', help=u"""The TrustStore password.""")
@cli_util.option('--key-store', help=u"""The base64 encoded content of the KeyStore file.""")
@cli_util.option('--key-store-password', help=u"""The KeyStore password.""")
@cli_util.option('--ssl-key-password', help=u"""The password for the cert inside of of the KeyStore. In case it differs from the KeyStore password, it should be provided.""")
@cli_util.option('--consumer-properties', help=u"""The base64 encoded content of the consumer.properties file.""")
@cli_util.option('--producer-properties', help=u"""The base64 encoded content of the producer.properties file.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}, 'bootstrap-servers': {'module': 'golden_gate', 'class': 'list[KafkaBootstrapServer]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}, 'bootstrap-servers': {'module': 'golden_gate', 'class': 'list[KafkaBootstrapServer]'}}, output_type={'module': 'golden_gate', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection_create_kafka_connection_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, technology_type, description, freeform_tags, defined_tags, vault_id, key_id, subnet_id, nsg_ids, stream_pool_id, bootstrap_servers, security_protocol, username, password, trust_store, trust_store_password, key_store, key_store_password, ssl_key_password, consumer_properties, producer_properties):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['technologyType'] = technology_type

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if vault_id is not None:
        _details['vaultId'] = vault_id

    if key_id is not None:
        _details['keyId'] = key_id

    if subnet_id is not None:
        _details['subnetId'] = subnet_id

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if stream_pool_id is not None:
        _details['streamPoolId'] = stream_pool_id

    if bootstrap_servers is not None:
        _details['bootstrapServers'] = cli_util.parse_json_parameter("bootstrap_servers", bootstrap_servers)

    if security_protocol is not None:
        _details['securityProtocol'] = security_protocol

    if username is not None:
        _details['username'] = username

    if password is not None:
        _details['password'] = password

    if trust_store is not None:
        _details['trustStore'] = trust_store

    if trust_store_password is not None:
        _details['trustStorePassword'] = trust_store_password

    if key_store is not None:
        _details['keyStore'] = key_store

    if key_store_password is not None:
        _details['keyStorePassword'] = key_store_password

    if ssl_key_password is not None:
        _details['sslKeyPassword'] = ssl_key_password

    if consumer_properties is not None:
        _details['consumerProperties'] = consumer_properties

    if producer_properties is not None:
        _details['producerProperties'] = producer_properties

    _details['connectionType'] = 'KAFKA'

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
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


@connection_group.command(name=cli_util.override('goldengate.create_connection_create_oracle_connection_details.command_name', 'create-connection-create-oracle-connection-details'), help=u"""Creates a new Connection. \n[Command Reference](createConnection)""")
@cli_util.option('--display-name', required=True, help=u"""An object's Display Name.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment being referenced.""")
@cli_util.option('--technology-type', required=True, help=u"""The Oracle technology type.""")
@cli_util.option('--username', required=True, help=u"""The username Oracle GoldenGate uses to connect the associated RDBMS.  This username must already exist and be available for use by the database.  It must conform to the security requirements implemented by the database including length, case sensitivity, and so on.""")
@cli_util.option('--password', required=True, help=u"""The password Oracle GoldenGate uses to connect the associated RDBMS.  It must conform to the specific security requirements implemented by the database including length, case sensitivity, and so on.""")
@cli_util.option('--description', help=u"""Metadata about this specific object.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.

Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Tags defined for this resource. Each key is predefined and scoped to a namespace.

Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vault-id', help=u"""The [OCID] of the customer vault being referenced. If provided, this will reference a vault which the customer will be required to ensure the policies are established to permit the GoldenGate Service to manage secrets contained within this vault.""")
@cli_util.option('--key-id', help=u"""The [OCID] of the customer \"Master\" key being referenced. If provided, this will reference a key which the customer will be required to ensure the policies are established to permit the GoldenGate Service to utilize this key to manage secrets.""")
@cli_util.option('--subnet-id', help=u"""The [OCID] of the subnet being referenced.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-string', help=u"""Connect descriptor or Easy Connect Naming method that Oracle GoldenGate uses to connect to a database.""")
@cli_util.option('--wallet', help=u"""The wallet contents Oracle GoldenGate uses to make connections to a database.  This attribute is expected to be base64 encoded.""")
@cli_util.option('--session-mode', help=u"""The mode of the database connection session to be established by the data client. 'REDIRECT' - for a RAC database, 'DIRECT' - for a non-RAC database. Connection to a RAC database involves a redirection received from the SCAN listeners to the database node to connect to. By default the mode would be DIRECT.""")
@cli_util.option('--private-ip', help=u"""The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.""")
@cli_util.option('--database-id', help=u"""The [OCID] of the database being referenced.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}}, output_type={'module': 'golden_gate', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection_create_oracle_connection_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, technology_type, username, password, description, freeform_tags, defined_tags, vault_id, key_id, subnet_id, nsg_ids, connection_string, wallet, session_mode, private_ip, database_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['technologyType'] = technology_type
    _details['username'] = username
    _details['password'] = password

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if vault_id is not None:
        _details['vaultId'] = vault_id

    if key_id is not None:
        _details['keyId'] = key_id

    if subnet_id is not None:
        _details['subnetId'] = subnet_id

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if connection_string is not None:
        _details['connectionString'] = connection_string

    if wallet is not None:
        _details['wallet'] = wallet

    if session_mode is not None:
        _details['sessionMode'] = session_mode

    if private_ip is not None:
        _details['privateIp'] = private_ip

    if database_id is not None:
        _details['databaseId'] = database_id

    _details['connectionType'] = 'ORACLE'

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
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


@connection_group.command(name=cli_util.override('goldengate.create_connection_create_golden_gate_connection_details.command_name', 'create-connection-create-golden-gate-connection-details'), help=u"""Creates a new Connection. \n[Command Reference](createConnection)""")
@cli_util.option('--display-name', required=True, help=u"""An object's Display Name.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment being referenced.""")
@cli_util.option('--technology-type', required=True, help=u"""The GoldenGate technology type.""")
@cli_util.option('--description', help=u"""Metadata about this specific object.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.

Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Tags defined for this resource. Each key is predefined and scoped to a namespace.

Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vault-id', help=u"""The [OCID] of the customer vault being referenced. If provided, this will reference a vault which the customer will be required to ensure the policies are established to permit the GoldenGate Service to manage secrets contained within this vault.""")
@cli_util.option('--key-id', help=u"""The [OCID] of the customer \"Master\" key being referenced. If provided, this will reference a key which the customer will be required to ensure the policies are established to permit the GoldenGate Service to utilize this key to manage secrets.""")
@cli_util.option('--subnet-id', help=u"""The [OCID] of the subnet being referenced.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--deployment-id', help=u"""The [OCID] of the deployment being referenced.""")
@cli_util.option('--host', help=u"""The name or address of a host.""")
@cli_util.option('--port', type=click.INT, help=u"""The port of an endpoint usually specified for a connection.""")
@cli_util.option('--private-ip', help=u"""The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}}, output_type={'module': 'golden_gate', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection_create_golden_gate_connection_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, technology_type, description, freeform_tags, defined_tags, vault_id, key_id, subnet_id, nsg_ids, deployment_id, host, port, private_ip):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['technologyType'] = technology_type

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if vault_id is not None:
        _details['vaultId'] = vault_id

    if key_id is not None:
        _details['keyId'] = key_id

    if subnet_id is not None:
        _details['subnetId'] = subnet_id

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if deployment_id is not None:
        _details['deploymentId'] = deployment_id

    if host is not None:
        _details['host'] = host

    if port is not None:
        _details['port'] = port

    if private_ip is not None:
        _details['privateIp'] = private_ip

    _details['connectionType'] = 'GOLDENGATE'

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
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


@connection_assignment_group.command(name=cli_util.override('goldengate.create_connection_assignment.command_name', 'create'), help=u"""Creates a new Connection Assignment. \n[Command Reference](createConnectionAssignment)""")
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of the connection being referenced.""")
@cli_util.option('--deployment-id', required=True, help=u"""The [OCID] of the deployment being referenced.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'golden_gate', 'class': 'ConnectionAssignment'})
@cli_util.wrap_exceptions
def create_connection_assignment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, connection_id, deployment_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['connectionId'] = connection_id
    _details['deploymentId'] = deployment_id

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.create_connection_assignment(
        create_connection_assignment_details=_details,
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


@database_registration_group.command(name=cli_util.override('goldengate.create_database_registration.command_name', 'create'), help=u"""Note: Deprecated. Use the new resource model APIs instead. Creates a new DatabaseRegistration. \n[Command Reference](createDatabaseRegistration)""")
@cli_util.option('--display-name', required=True, help=u"""An object's Display Name.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment being referenced.""")
@cli_util.option('--fqdn', required=True, help=u"""A three-label Fully Qualified Domain Name (FQDN) for a resource.""")
@cli_util.option('--username', required=True, help=u"""The username Oracle GoldenGate uses to connect the associated RDBMS.  This username must already exist and be available for use by the database.  It must conform to the security requirements implemented by the database including length, case sensitivity, and so on.""")
@cli_util.option('--password', required=True, help=u"""The password Oracle GoldenGate uses to connect the associated RDBMS.  It must conform to the specific security requirements implemented by the database including length, case sensitivity, and so on.""")
@cli_util.option('--alias-name', required=True, help=u"""Credential store alias.""")
@cli_util.option('--description', help=u"""Metadata about this specific object.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.

Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Tags defined for this resource. Each key is predefined and scoped to a namespace.

Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ip-address', help=u"""The private IP address in the customer's VCN of the customer's endpoint, typically a database.""")
@cli_util.option('--subnet-id', help=u"""The [OCID] of the subnet being referenced.""")
@cli_util.option('--database-id', help=u"""The [OCID] of the database being referenced.""")
@cli_util.option('--connection-string', help=u"""Connect descriptor or Easy Connect Naming method that Oracle GoldenGate uses to connect to a database.""")
@cli_util.option('--session-mode', type=custom_types.CliCaseInsensitiveChoice(["DIRECT", "REDIRECT"]), help=u"""The mode of the database connection session to be established by the data client. 'REDIRECT' - for a RAC database, 'DIRECT' - for a non-RAC database. Connection to a RAC database involves a redirection received from the SCAN listeners to the database node to connect to. By default the mode would be DIRECT.""")
@cli_util.option('--wallet', help=u"""The wallet contents Oracle GoldenGate uses to make connections to a database.  This attribute is expected to be base64 encoded.""")
@cli_util.option('--vault-id', help=u"""The [OCID] of the customer vault being referenced. If provided, this will reference a vault which the customer will be required to ensure the policies are established to permit the GoldenGate Service to manage secrets contained within this vault.""")
@cli_util.option('--key-id', help=u"""The [OCID] of the customer \"Master\" key being referenced. If provided, this will reference a key which the customer will be required to ensure the policies are established to permit the GoldenGate Service to utilize this key to manage secrets.""")
@cli_util.option('--secret-compartment-id', help=u"""The [OCID] of the compartment where the the GGS Secret will be created. If provided, this will reference a key which the customer will be required to ensure the policies are established to permit the GoldenGate Service to utilize this Compartment in which to create a Secret.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'golden_gate', 'class': 'DatabaseRegistration'})
@cli_util.wrap_exceptions
def create_database_registration(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, fqdn, username, password, alias_name, description, freeform_tags, defined_tags, ip_address, subnet_id, database_id, connection_string, session_mode, wallet, vault_id, key_id, secret_compartment_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['fqdn'] = fqdn
    _details['username'] = username
    _details['password'] = password
    _details['aliasName'] = alias_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if ip_address is not None:
        _details['ipAddress'] = ip_address

    if subnet_id is not None:
        _details['subnetId'] = subnet_id

    if database_id is not None:
        _details['databaseId'] = database_id

    if connection_string is not None:
        _details['connectionString'] = connection_string

    if session_mode is not None:
        _details['sessionMode'] = session_mode

    if wallet is not None:
        _details['wallet'] = wallet

    if vault_id is not None:
        _details['vaultId'] = vault_id

    if key_id is not None:
        _details['keyId'] = key_id

    if secret_compartment_id is not None:
        _details['secretCompartmentId'] = secret_compartment_id

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.create_database_registration(
        create_database_registration_details=_details,
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


@deployment_group.command(name=cli_util.override('goldengate.create_deployment.command_name', 'create'), help=u"""Creates a new Deployment. \n[Command Reference](createDeployment)""")
@cli_util.option('--display-name', required=True, help=u"""An object's Display Name.""")
@cli_util.option('--license-model', required=True, type=custom_types.CliCaseInsensitiveChoice(["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]), help=u"""The Oracle license model that applies to a Deployment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment being referenced.""")
@cli_util.option('--subnet-id', required=True, help=u"""The [OCID] of the subnet being referenced.""")
@cli_util.option('--cpu-core-count', required=True, type=click.INT, help=u"""The Minimum number of OCPUs to be made available for this Deployment.""")
@cli_util.option('--is-auto-scaling-enabled', required=True, type=click.BOOL, help=u"""Indicates if auto scaling is enabled for the Deployment's CPU core count.""")
@cli_util.option('--deployment-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["OGG", "DATABASE_ORACLE", "BIGDATA", "DATABASE_MYSQL"]), help=u"""The type of deployment, the value determines the exact 'type' of service executed in the Deployment. NOTE: Use of the value 'OGG' is maintained for backward compatibility purposes.  Its use is discouraged       in favor of the equivalent 'DATABASE_ORACLE' value.""")
@cli_util.option('--description', help=u"""Metadata about this specific object.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.

Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Tags defined for this resource. Each key is predefined and scoped to a namespace.

Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--deployment-backup-id', help=u"""The [OCID] of the backup being referenced.""")
@cli_util.option('--fqdn', help=u"""A three-label Fully Qualified Domain Name (FQDN) for a resource.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-public', type=click.BOOL, help=u"""True if this object is publicly available.""")
@cli_util.option('--ogg-data', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}, 'ogg-data': {'module': 'golden_gate', 'class': 'CreateOggDeploymentDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}, 'ogg-data': {'module': 'golden_gate', 'class': 'CreateOggDeploymentDetails'}}, output_type={'module': 'golden_gate', 'class': 'Deployment'})
@cli_util.wrap_exceptions
def create_deployment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, license_model, compartment_id, subnet_id, cpu_core_count, is_auto_scaling_enabled, deployment_type, description, freeform_tags, defined_tags, deployment_backup_id, fqdn, nsg_ids, is_public, ogg_data):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['licenseModel'] = license_model
    _details['compartmentId'] = compartment_id
    _details['subnetId'] = subnet_id
    _details['cpuCoreCount'] = cpu_core_count
    _details['isAutoScalingEnabled'] = is_auto_scaling_enabled
    _details['deploymentType'] = deployment_type

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if deployment_backup_id is not None:
        _details['deploymentBackupId'] = deployment_backup_id

    if fqdn is not None:
        _details['fqdn'] = fqdn

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if is_public is not None:
        _details['isPublic'] = is_public

    if ogg_data is not None:
        _details['oggData'] = cli_util.parse_json_parameter("ogg_data", ogg_data)

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.create_deployment(
        create_deployment_details=_details,
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


@deployment_backup_group.command(name=cli_util.override('goldengate.create_deployment_backup.command_name', 'create'), help=u"""Creates a new DeploymentBackup. \n[Command Reference](createDeploymentBackup)""")
@cli_util.option('--display-name', required=True, help=u"""An object's Display Name.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment being referenced.""")
@cli_util.option('--deployment-id', required=True, help=u"""The [OCID] of the deployment being referenced.""")
@cli_util.option('--namespace-name', required=True, help=u"""Name of namespace that serves as a container for all of your buckets""")
@cli_util.option('--bucket-name', required=True, help=u"""Name of the bucket where the object is to be uploaded in the object storage""")
@cli_util.option('--object-name', required=True, help=u"""Name of the object to be uploaded to object storage""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.

Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Tags defined for this resource. Each key is predefined and scoped to a namespace.

Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_deployment_backup(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, deployment_id, namespace_name, bucket_name, object_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['deploymentId'] = deployment_id
    _details['namespaceName'] = namespace_name
    _details['bucketName'] = bucket_name
    _details['objectName'] = object_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.create_deployment_backup(
        create_deployment_backup_details=_details,
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


@connection_group.command(name=cli_util.override('goldengate.delete_connection.command_name', 'delete'), help=u"""Deletes a Connection. \n[Command Reference](deleteConnection)""")
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of a Connection.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
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
    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
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


@connection_assignment_group.command(name=cli_util.override('goldengate.delete_connection_assignment.command_name', 'delete'), help=u"""Deletes a Connection Assignment. \n[Command Reference](deleteConnectionAssignment)""")
@cli_util.option('--connection-assignment-id', required=True, help=u"""The [OCID] of the Connection Assignment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_connection_assignment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, connection_assignment_id, if_match):

    if isinstance(connection_assignment_id, six.string_types) and len(connection_assignment_id.strip()) == 0:
        raise click.UsageError('Parameter --connection-assignment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.delete_connection_assignment(
        connection_assignment_id=connection_assignment_id,
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


@database_registration_group.command(name=cli_util.override('goldengate.delete_database_registration.command_name', 'delete'), help=u"""Note: Deprecated. Use the new resource model APIs instead. Deletes a DatabaseRegistration. \n[Command Reference](deleteDatabaseRegistration)""")
@cli_util.option('--database-registration-id', required=True, help=u"""A unique DatabaseRegistration identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_database_registration(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_registration_id, if_match):

    if isinstance(database_registration_id, six.string_types) and len(database_registration_id.strip()) == 0:
        raise click.UsageError('Parameter --database-registration-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.delete_database_registration(
        database_registration_id=database_registration_id,
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


@deployment_group.command(name=cli_util.override('goldengate.delete_deployment.command_name', 'delete'), help=u"""Deletes the Deployment. \n[Command Reference](deleteDeployment)""")
@cli_util.option('--deployment-id', required=True, help=u"""A unique Deployment identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_deployment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deployment_id, if_match):

    if isinstance(deployment_id, six.string_types) and len(deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --deployment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.delete_deployment(
        deployment_id=deployment_id,
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


@deployment_backup_group.command(name=cli_util.override('goldengate.delete_deployment_backup.command_name', 'delete'), help=u"""Deletes a DeploymentBackup. \n[Command Reference](deleteDeploymentBackup)""")
@cli_util.option('--deployment-backup-id', required=True, help=u"""A unique DeploymentBackup identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_deployment_backup(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deployment_backup_id, if_match):

    if isinstance(deployment_backup_id, six.string_types) and len(deployment_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --deployment-backup-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.delete_deployment_backup(
        deployment_backup_id=deployment_backup_id,
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


@connection_group.command(name=cli_util.override('goldengate.get_connection.command_name', 'get'), help=u"""Retrieves a Connection. \n[Command Reference](getConnection)""")
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of a Connection.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'golden_gate', 'class': 'Connection'})
@cli_util.wrap_exceptions
def get_connection(ctx, from_json, connection_id):

    if isinstance(connection_id, six.string_types) and len(connection_id.strip()) == 0:
        raise click.UsageError('Parameter --connection-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.get_connection(
        connection_id=connection_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_assignment_group.command(name=cli_util.override('goldengate.get_connection_assignment.command_name', 'get'), help=u"""Retrieves a Connection Assignment. \n[Command Reference](getConnectionAssignment)""")
@cli_util.option('--connection-assignment-id', required=True, help=u"""The [OCID] of the Connection Assignment.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'golden_gate', 'class': 'ConnectionAssignment'})
@cli_util.wrap_exceptions
def get_connection_assignment(ctx, from_json, connection_assignment_id):

    if isinstance(connection_assignment_id, six.string_types) and len(connection_assignment_id.strip()) == 0:
        raise click.UsageError('Parameter --connection-assignment-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.get_connection_assignment(
        connection_assignment_id=connection_assignment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_registration_group.command(name=cli_util.override('goldengate.get_database_registration.command_name', 'get'), help=u"""Note: Deprecated. Use the new resource model APIs instead. Retrieves a DatabaseRegistration. \n[Command Reference](getDatabaseRegistration)""")
@cli_util.option('--database-registration-id', required=True, help=u"""A unique DatabaseRegistration identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'golden_gate', 'class': 'DatabaseRegistration'})
@cli_util.wrap_exceptions
def get_database_registration(ctx, from_json, database_registration_id):

    if isinstance(database_registration_id, six.string_types) and len(database_registration_id.strip()) == 0:
        raise click.UsageError('Parameter --database-registration-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.get_database_registration(
        database_registration_id=database_registration_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@deployment_group.command(name=cli_util.override('goldengate.get_deployment.command_name', 'get'), help=u"""Retrieves a deployment. \n[Command Reference](getDeployment)""")
@cli_util.option('--deployment-id', required=True, help=u"""A unique Deployment identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'golden_gate', 'class': 'Deployment'})
@cli_util.wrap_exceptions
def get_deployment(ctx, from_json, deployment_id):

    if isinstance(deployment_id, six.string_types) and len(deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --deployment-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.get_deployment(
        deployment_id=deployment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@deployment_backup_group.command(name=cli_util.override('goldengate.get_deployment_backup.command_name', 'get'), help=u"""Retrieves a DeploymentBackup. \n[Command Reference](getDeploymentBackup)""")
@cli_util.option('--deployment-backup-id', required=True, help=u"""A unique DeploymentBackup identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'golden_gate', 'class': 'DeploymentBackup'})
@cli_util.wrap_exceptions
def get_deployment_backup(ctx, from_json, deployment_backup_id):

    if isinstance(deployment_backup_id, six.string_types) and len(deployment_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --deployment-backup-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.get_deployment_backup(
        deployment_backup_id=deployment_backup_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@deployment_upgrade_group.command(name=cli_util.override('goldengate.get_deployment_upgrade.command_name', 'get'), help=u"""Retrieves a deployment upgrade. \n[Command Reference](getDeploymentUpgrade)""")
@cli_util.option('--deployment-upgrade-id', required=True, help=u"""A unique Deployment Upgrade identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'golden_gate', 'class': 'DeploymentUpgrade'})
@cli_util.wrap_exceptions
def get_deployment_upgrade(ctx, from_json, deployment_upgrade_id):

    if isinstance(deployment_upgrade_id, six.string_types) and len(deployment_upgrade_id.strip()) == 0:
        raise click.UsageError('Parameter --deployment-upgrade-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.get_deployment_upgrade(
        deployment_upgrade_id=deployment_upgrade_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('goldengate.get_work_request.command_name', 'get'), help=u"""Retrieve the WorkRequest identified by the given OCID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'golden_gate', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_assignment_group.command(name=cli_util.override('goldengate.list_connection_assignments.command_name', 'list'), help=u"""Lists the Connection Assignments in the compartment. \n[Command Reference](listConnectionAssignments)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which to list resources.""")
@cli_util.option('--deployment-id', help=u"""The [OCID] of the deployment in which to list resources.""")
@cli_util.option('--connection-id', help=u"""The [OCID] of the connection.""")
@cli_util.option('--name', help=u"""The name of the connection in the assignment (aliasName).""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING"]), help=u"""A filter to return only connection assignments having the 'lifecycleState' given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order can be provided. Default order for 'timeCreated' is descending.  Default order for 'displayName' is ascending. If no value is specified timeCreated is the default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'golden_gate', 'class': 'ConnectionAssignmentCollection'})
@cli_util.wrap_exceptions
def list_connection_assignments(ctx, from_json, all_pages, page_size, compartment_id, deployment_id, connection_id, name, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if deployment_id is not None:
        kwargs['deployment_id'] = deployment_id
    if connection_id is not None:
        kwargs['connection_id'] = connection_id
    if name is not None:
        kwargs['name'] = name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_connection_assignments,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_connection_assignments,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_connection_assignments(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@connection_group.command(name=cli_util.override('goldengate.list_connections.command_name', 'list'), help=u"""Lists the Connections in the compartment. \n[Command Reference](listConnections)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which to list resources.""")
@cli_util.option('--technology-type', type=custom_types.CliCaseInsensitiveChoice(["OCI_AUTONOMOUS_DATABASE", "OCI_MYSQL", "OCI_OBJECT_STORAGE", "OCI_STREAMING", "ORACLE_DATABASE", "ORACLE_EXADATA", "AMAZON_RDS_ORACLE", "AMAZON_AURORA_MYSQL", "AMAZON_RDS_MARIADB", "AMAZON_RDS_MYSQL", "APACHE_KAFKA", "AZURE_MYSQL", "GOLDENGATE", "GOOGLE_CLOUD_SQL_MYSQL", "MARIADB", "MYSQL_SERVER"]), multiple=True, help=u"""The array of technology types.""")
@cli_util.option('--connection-type', type=custom_types.CliCaseInsensitiveChoice(["GOLDENGATE", "KAFKA", "MYSQL", "OCI_OBJECT_STORAGE", "ORACLE"]), multiple=True, help=u"""The array of connection types.""")
@cli_util.option('--assigned-deployment-id', help=u"""The OCID of the deployment which for the connection must be assigned.""")
@cli_util.option('--assignable-deployment-id', help=u"""Filters for compatible connections which can be, but currently not assigned to the deployment specified by its id.""")
@cli_util.option('--assignable-deployment-type', type=custom_types.CliCaseInsensitiveChoice(["OGG", "DATABASE_ORACLE", "BIGDATA", "DATABASE_MYSQL"]), help=u"""Filters for connections which can be assigned to the latest version of the specified deployment type.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only connections having the 'lifecycleState' given.""")
@cli_util.option('--display-name', help=u"""A filter to return only the resources that match the entire 'displayName' given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order can be provided. Default order for 'timeCreated' is descending.  Default order for 'displayName' is ascending. If no value is specified timeCreated is the default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'golden_gate', 'class': 'ConnectionCollection'})
@cli_util.wrap_exceptions
def list_connections(ctx, from_json, all_pages, page_size, compartment_id, technology_type, connection_type, assigned_deployment_id, assignable_deployment_id, assignable_deployment_type, lifecycle_state, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if technology_type is not None and len(technology_type) > 0:
        kwargs['technology_type'] = technology_type
    if connection_type is not None and len(connection_type) > 0:
        kwargs['connection_type'] = connection_type
    if assigned_deployment_id is not None:
        kwargs['assigned_deployment_id'] = assigned_deployment_id
    if assignable_deployment_id is not None:
        kwargs['assignable_deployment_id'] = assignable_deployment_id
    if assignable_deployment_type is not None:
        kwargs['assignable_deployment_type'] = assignable_deployment_type
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
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


@database_registration_group.command(name=cli_util.override('goldengate.list_database_registrations.command_name', 'list'), help=u"""Note: Deprecated. Use the new resource model APIs instead. Lists the DatabaseRegistrations in the compartment. \n[Command Reference](listDatabaseRegistrations)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which to list resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", "IN_PROGRESS", "CANCELING", "CANCELED", "SUCCEEDED"]), help=u"""A filter to return only the resources that match the 'lifecycleState' given.""")
@cli_util.option('--display-name', help=u"""A filter to return only the resources that match the entire 'displayName' given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order can be provided. Default order for 'timeCreated' is descending.  Default order for 'displayName' is ascending. If no value is specified timeCreated is the default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'golden_gate', 'class': 'DatabaseRegistrationCollection'})
@cli_util.wrap_exceptions
def list_database_registrations(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_database_registrations,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_database_registrations,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_database_registrations(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@deployment_backup_group.command(name=cli_util.override('goldengate.list_deployment_backups.command_name', 'list'), help=u"""Lists the Backups in a compartment. \n[Command Reference](listDeploymentBackups)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which to list resources.""")
@cli_util.option('--deployment-id', help=u"""The [OCID] of the deployment in which to list resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", "IN_PROGRESS", "CANCELING", "CANCELED", "SUCCEEDED"]), help=u"""A filter to return only the resources that match the 'lifecycleState' given.""")
@cli_util.option('--display-name', help=u"""A filter to return only the resources that match the entire 'displayName' given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order can be provided. Default order for 'timeCreated' is descending.  Default order for 'displayName' is ascending. If no value is specified timeCreated is the default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'golden_gate', 'class': 'DeploymentBackupCollection'})
@cli_util.wrap_exceptions
def list_deployment_backups(ctx, from_json, all_pages, page_size, compartment_id, deployment_id, lifecycle_state, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if deployment_id is not None:
        kwargs['deployment_id'] = deployment_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_deployment_backups,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_deployment_backups,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_deployment_backups(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@deployment_type_collection_group.command(name=cli_util.override('goldengate.list_deployment_types.command_name', 'list-deployment-types'), help=u"""Returns an array of DeploymentTypeDescriptor \n[Command Reference](listDeploymentTypes)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only the resources that match the entire 'displayName' given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order can be provided. Default order for 'timeCreated' is descending.  Default order for 'displayName' is ascending. If no value is specified timeCreated is the default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'golden_gate', 'class': 'DeploymentTypeCollection'})
@cli_util.wrap_exceptions
def list_deployment_types(ctx, from_json, all_pages, page_size, compartment_id, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_deployment_types,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_deployment_types,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_deployment_types(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@deployment_upgrade_group.command(name=cli_util.override('goldengate.list_deployment_upgrades.command_name', 'list'), help=u"""Lists the Deployment Upgrades in a compartment. \n[Command Reference](listDeploymentUpgrades)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which to list resources.""")
@cli_util.option('--deployment-id', help=u"""The [OCID] of the deployment in which to list resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", "IN_PROGRESS", "CANCELING", "CANCELED", "SUCCEEDED"]), help=u"""A filter to return only the resources that match the 'lifecycleState' given.""")
@cli_util.option('--display-name', help=u"""A filter to return only the resources that match the entire 'displayName' given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order can be provided. Default order for 'timeCreated' is descending.  Default order for 'displayName' is ascending. If no value is specified timeCreated is the default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'golden_gate', 'class': 'DeploymentUpgradeCollection'})
@cli_util.wrap_exceptions
def list_deployment_upgrades(ctx, from_json, all_pages, page_size, compartment_id, deployment_id, lifecycle_state, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if deployment_id is not None:
        kwargs['deployment_id'] = deployment_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_deployment_upgrades,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_deployment_upgrades,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_deployment_upgrades(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@deployment_group.command(name=cli_util.override('goldengate.list_deployments.command_name', 'list'), help=u"""Lists the Deployments in a compartment. \n[Command Reference](listDeployments)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which to list resources.""")
@cli_util.option('--supported-connection-type', type=custom_types.CliCaseInsensitiveChoice(["GOLDENGATE", "KAFKA", "MYSQL", "OCI_OBJECT_STORAGE", "ORACLE"]), help=u"""The connection type which the deployment must support.""")
@cli_util.option('--assigned-connection-id', help=u"""The OCID of the connection which for the deployment must be assigned.""")
@cli_util.option('--assignable-connection-id', help=u"""Filters for compatible deployments which can be, but currently not assigned to the connection specified by its id.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", "IN_PROGRESS", "CANCELING", "CANCELED", "SUCCEEDED"]), help=u"""A filter to return only the resources that match the 'lifecycleState' given.""")
@cli_util.option('--lifecycle-sub-state', type=custom_types.CliCaseInsensitiveChoice(["RECOVERING", "STARTING", "STOPPING", "MOVING", "UPGRADING", "RESTORING", "BACKUP_IN_PROGRESS"]), help=u"""A filter to return only the resources that match the 'lifecycleSubState' given.""")
@cli_util.option('--display-name', help=u"""A filter to return only the resources that match the entire 'displayName' given.""")
@cli_util.option('--fqdn', help=u"""A filter to return only the resources that match the 'fqdn' given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order can be provided. Default order for 'timeCreated' is descending.  Default order for 'displayName' is ascending. If no value is specified timeCreated is the default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'golden_gate', 'class': 'DeploymentCollection'})
@cli_util.wrap_exceptions
def list_deployments(ctx, from_json, all_pages, page_size, compartment_id, supported_connection_type, assigned_connection_id, assignable_connection_id, lifecycle_state, lifecycle_sub_state, display_name, fqdn, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if supported_connection_type is not None:
        kwargs['supported_connection_type'] = supported_connection_type
    if assigned_connection_id is not None:
        kwargs['assigned_connection_id'] = assigned_connection_id
    if assignable_connection_id is not None:
        kwargs['assignable_connection_id'] = assignable_connection_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if lifecycle_sub_state is not None:
        kwargs['lifecycle_sub_state'] = lifecycle_sub_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if fqdn is not None:
        kwargs['fqdn'] = fqdn
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_deployments,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_deployments,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_deployments(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@message_summary_group.command(name=cli_util.override('goldengate.list_messages.command_name', 'list-messages'), help=u"""Lists the DeploymentMessages for a deployment. The sorting order is not important. By default first will be Upgrade message, next Exception message and then Storage Utilization message. \n[Command Reference](listMessages)""")
@cli_util.option('--deployment-id', required=True, help=u"""A unique Deployment identifier.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'golden_gate', 'class': 'DeploymentMessageCollection'})
@cli_util.wrap_exceptions
def list_messages(ctx, from_json, all_pages, page_size, deployment_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_messages,
            deployment_id=deployment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_messages,
            limit,
            page_size,
            deployment_id=deployment_id,
            **kwargs
        )
    else:
        result = client.list_messages(
            deployment_id=deployment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@trail_file_summary_group.command(name=cli_util.override('goldengate.list_trail_files.command_name', 'list-trail-files'), help=u"""Lists the TrailFiles for a deployment. \n[Command Reference](listTrailFiles)""")
@cli_util.option('--deployment-id', required=True, help=u"""A unique Deployment identifier.""")
@cli_util.option('--display-name', help=u"""A filter to return only the resources that match the entire 'displayName' given.""")
@cli_util.option('--trail-file-id', help=u"""A Trail File identifier""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeLastUpdated", "displayName"]), help=u"""The field to sort by. Only one sort order can be provided. Default order for 'timeLastUpdated' is descending.  Default order for 'displayName' is ascending. If no value is specified displayName is the default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'golden_gate', 'class': 'TrailFileCollection'})
@cli_util.wrap_exceptions
def list_trail_files(ctx, from_json, all_pages, page_size, deployment_id, display_name, trail_file_id, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if trail_file_id is not None:
        kwargs['trail_file_id'] = trail_file_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_trail_files,
            deployment_id=deployment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_trail_files,
            limit,
            page_size,
            deployment_id=deployment_id,
            **kwargs
        )
    else:
        result = client.list_trail_files(
            deployment_id=deployment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@trail_sequence_summary_group.command(name=cli_util.override('goldengate.list_trail_sequences.command_name', 'list-trail-sequences'), help=u"""Lists the Trail Sequences for a TrailFile in a given deployment. \n[Command Reference](listTrailSequences)""")
@cli_util.option('--deployment-id', required=True, help=u"""A unique Deployment identifier.""")
@cli_util.option('--trail-file-id', required=True, help=u"""A Trail File identifier""")
@cli_util.option('--trail-sequence-id', help=u"""A Trail Sequence identifier""")
@cli_util.option('--display-name', help=u"""A filter to return only the resources that match the entire 'displayName' given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeLastUpdated", "displayName"]), help=u"""The field to sort by. Only one sort order can be provided. Default order for 'timeLastUpdated' is descending.  Default order for 'displayName' is ascending. If no value is specified displayName is the default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'golden_gate', 'class': 'TrailSequenceCollection'})
@cli_util.wrap_exceptions
def list_trail_sequences(ctx, from_json, all_pages, page_size, deployment_id, trail_file_id, trail_sequence_id, display_name, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if trail_sequence_id is not None:
        kwargs['trail_sequence_id'] = trail_sequence_id
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
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_trail_sequences,
            deployment_id=deployment_id,
            trail_file_id=trail_file_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_trail_sequences,
            limit,
            page_size,
            deployment_id=deployment_id,
            trail_file_id=trail_file_id,
            **kwargs
        )
    else:
        result = client.list_trail_sequences(
            deployment_id=deployment_id,
            trail_file_id=trail_file_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('goldengate.list_work_request_errors.command_name', 'list'), help=u"""Lists work request errors. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the asynchronous request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'golden_gate', 'class': 'list[WorkRequestError]'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
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


@work_request_log_entry_group.command(name=cli_util.override('goldengate.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Lists work request logs. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the asynchronous request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'golden_gate', 'class': 'list[WorkRequestLogEntry]'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
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


@work_request_group.command(name=cli_util.override('goldengate.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in the compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which to list resources.""")
@cli_util.option('--resource-id', help=u"""The [OCID] of the resource in which to list resources.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'golden_gate', 'class': 'list[WorkRequest]'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, resource_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if resource_id is not None:
        kwargs['resource_id'] = resource_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
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


@deployment_backup_group.command(name=cli_util.override('goldengate.restore_deployment.command_name', 'restore-deployment'), help=u"""Restores a Deployment from a Deployment Backup created from the same Deployment. \n[Command Reference](restoreDeployment)""")
@cli_util.option('--deployment-backup-id', required=True, help=u"""A unique DeploymentBackup identifier.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["DEFAULT"]), help=u"""The type of a deployment restore""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def restore_deployment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deployment_backup_id, type, if_match):

    if isinstance(deployment_backup_id, six.string_types) and len(deployment_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --deployment-backup-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['type'] = type

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.restore_deployment(
        deployment_backup_id=deployment_backup_id,
        restore_deployment_details=_details,
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


@deployment_backup_group.command(name=cli_util.override('goldengate.restore_deployment_default_restore_deployment_details.command_name', 'restore-deployment-default-restore-deployment-details'), help=u"""Restores a Deployment from a Deployment Backup created from the same Deployment. \n[Command Reference](restoreDeployment)""")
@cli_util.option('--deployment-backup-id', required=True, help=u"""A unique DeploymentBackup identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def restore_deployment_default_restore_deployment_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deployment_backup_id, if_match):

    if isinstance(deployment_backup_id, six.string_types) and len(deployment_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --deployment-backup-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    _details['type'] = 'DEFAULT'

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.restore_deployment(
        deployment_backup_id=deployment_backup_id,
        restore_deployment_details=_details,
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


@deployment_group.command(name=cli_util.override('goldengate.start_deployment.command_name', 'start'), help=u"""Starts a Deployment. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](startDeployment)""")
@cli_util.option('--deployment-id', required=True, help=u"""A unique Deployment identifier.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["DEFAULT"]), help=u"""The type of a deployment start""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def start_deployment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deployment_id, type, if_match):

    if isinstance(deployment_id, six.string_types) and len(deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --deployment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['type'] = type

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.start_deployment(
        deployment_id=deployment_id,
        start_deployment_details=_details,
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


@deployment_group.command(name=cli_util.override('goldengate.start_deployment_default_start_deployment_details.command_name', 'start-deployment-default-start-deployment-details'), help=u"""Starts a Deployment. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](startDeployment)""")
@cli_util.option('--deployment-id', required=True, help=u"""A unique Deployment identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def start_deployment_default_start_deployment_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deployment_id, if_match):

    if isinstance(deployment_id, six.string_types) and len(deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --deployment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    _details['type'] = 'DEFAULT'

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.start_deployment(
        deployment_id=deployment_id,
        start_deployment_details=_details,
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


@deployment_group.command(name=cli_util.override('goldengate.stop_deployment.command_name', 'stop'), help=u"""Stops a Deployment. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](stopDeployment)""")
@cli_util.option('--deployment-id', required=True, help=u"""A unique Deployment identifier.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["DEFAULT"]), help=u"""The type of a deployment stop""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def stop_deployment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deployment_id, type, if_match):

    if isinstance(deployment_id, six.string_types) and len(deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --deployment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['type'] = type

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.stop_deployment(
        deployment_id=deployment_id,
        stop_deployment_details=_details,
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


@deployment_group.command(name=cli_util.override('goldengate.stop_deployment_default_stop_deployment_details.command_name', 'stop-deployment-default-stop-deployment-details'), help=u"""Stops a Deployment. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](stopDeployment)""")
@cli_util.option('--deployment-id', required=True, help=u"""A unique Deployment identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def stop_deployment_default_stop_deployment_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deployment_id, if_match):

    if isinstance(deployment_id, six.string_types) and len(deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --deployment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    _details['type'] = 'DEFAULT'

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.stop_deployment(
        deployment_id=deployment_id,
        stop_deployment_details=_details,
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


@connection_group.command(name=cli_util.override('goldengate.update_connection.command_name', 'update'), help=u"""Updates the Connection. \n[Command Reference](updateConnection)""")
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of a Connection.""")
@cli_util.option('--connection-type', type=custom_types.CliCaseInsensitiveChoice(["GOLDENGATE", "KAFKA", "MYSQL", "OCI_OBJECT_STORAGE", "ORACLE"]), help=u"""The connection type.""")
@cli_util.option('--display-name', help=u"""An object's Display Name.""")
@cli_util.option('--description', help=u"""Metadata about this specific object.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.

Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Tags defined for this resource. Each key is predefined and scoped to a namespace.

Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vault-id', help=u"""The [OCID] of the customer vault being referenced. If provided, this will reference a vault which the customer will be required to ensure the policies are established to permit the GoldenGate Service to manage secrets contained within this vault.""")
@cli_util.option('--key-id', help=u"""The [OCID] of the customer \"Master\" key being referenced. If provided, this will reference a key which the customer will be required to ensure the policies are established to permit the GoldenGate Service to utilize this key to manage secrets.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_connection(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, connection_id, connection_type, display_name, description, freeform_tags, defined_tags, vault_id, key_id, nsg_ids, if_match):

    if isinstance(connection_id, six.string_types) and len(connection_id.strip()) == 0:
        raise click.UsageError('Parameter --connection-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or nsg_ids:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and nsg-ids will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if connection_type is not None:
        _details['connectionType'] = connection_type

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if vault_id is not None:
        _details['vaultId'] = vault_id

    if key_id is not None:
        _details['keyId'] = key_id

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
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


@connection_group.command(name=cli_util.override('goldengate.update_connection_update_oracle_connection_details.command_name', 'update-connection-update-oracle-connection-details'), help=u"""Updates the Connection. \n[Command Reference](updateConnection)""")
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of a Connection.""")
@cli_util.option('--display-name', help=u"""An object's Display Name.""")
@cli_util.option('--description', help=u"""Metadata about this specific object.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.

Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Tags defined for this resource. Each key is predefined and scoped to a namespace.

Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vault-id', help=u"""The [OCID] of the customer vault being referenced. If provided, this will reference a vault which the customer will be required to ensure the policies are established to permit the GoldenGate Service to manage secrets contained within this vault.""")
@cli_util.option('--key-id', help=u"""The [OCID] of the customer \"Master\" key being referenced. If provided, this will reference a key which the customer will be required to ensure the policies are established to permit the GoldenGate Service to utilize this key to manage secrets.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--username', help=u"""The username Oracle GoldenGate uses to connect the associated RDBMS.  This username must already exist and be available for use by the database.  It must conform to the security requirements implemented by the database including length, case sensitivity, and so on.""")
@cli_util.option('--password', help=u"""The password Oracle GoldenGate uses to connect the associated RDBMS.  It must conform to the specific security requirements implemented by the database including length, case sensitivity, and so on.""")
@cli_util.option('--connection-string', help=u"""Connect descriptor or Easy Connect Naming method that Oracle GoldenGate uses to connect to a database.""")
@cli_util.option('--wallet', help=u"""The wallet contents Oracle GoldenGate uses to make connections to a database.  This attribute is expected to be base64 encoded.""")
@cli_util.option('--session-mode', help=u"""The mode of the database connection session to be established by the data client. 'REDIRECT' - for a RAC database, 'DIRECT' - for a non-RAC database. Connection to a RAC database involves a redirection received from the SCAN listeners to the database node to connect to. By default the mode would be DIRECT.""")
@cli_util.option('--private-ip', help=u"""The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.""")
@cli_util.option('--database-id', help=u"""The [OCID] of the database being referenced.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_connection_update_oracle_connection_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, connection_id, display_name, description, freeform_tags, defined_tags, vault_id, key_id, nsg_ids, username, password, connection_string, wallet, session_mode, private_ip, database_id, if_match):

    if isinstance(connection_id, six.string_types) and len(connection_id.strip()) == 0:
        raise click.UsageError('Parameter --connection-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or nsg_ids:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and nsg-ids will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if vault_id is not None:
        _details['vaultId'] = vault_id

    if key_id is not None:
        _details['keyId'] = key_id

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if username is not None:
        _details['username'] = username

    if password is not None:
        _details['password'] = password

    if connection_string is not None:
        _details['connectionString'] = connection_string

    if wallet is not None:
        _details['wallet'] = wallet

    if session_mode is not None:
        _details['sessionMode'] = session_mode

    if private_ip is not None:
        _details['privateIp'] = private_ip

    if database_id is not None:
        _details['databaseId'] = database_id

    _details['connectionType'] = 'ORACLE'

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
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


@connection_group.command(name=cli_util.override('goldengate.update_connection_update_oci_object_storage_connection_details.command_name', 'update-connection-update-oci-object-storage-connection-details'), help=u"""Updates the Connection. \n[Command Reference](updateConnection)""")
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of a Connection.""")
@cli_util.option('--display-name', help=u"""An object's Display Name.""")
@cli_util.option('--description', help=u"""Metadata about this specific object.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.

Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Tags defined for this resource. Each key is predefined and scoped to a namespace.

Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vault-id', help=u"""The [OCID] of the customer vault being referenced. If provided, this will reference a vault which the customer will be required to ensure the policies are established to permit the GoldenGate Service to manage secrets contained within this vault.""")
@cli_util.option('--key-id', help=u"""The [OCID] of the customer \"Master\" key being referenced. If provided, this will reference a key which the customer will be required to ensure the policies are established to permit the GoldenGate Service to utilize this key to manage secrets.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--tenancy-id', help=u"""The [OCID] of the related OCI tenancy.""")
@cli_util.option('--region-parameterconflict', help=u"""The name of the region. e.g.: us-ashburn-1""")
@cli_util.option('--user-id', help=u"""The [OCID] of the OCI user who will access the Object Storage. The user must have write access to the bucket they want to connect to.""")
@cli_util.option('--private-key-file', help=u"""The base64 encoded content of the private key file (PEM file) corresponding to the API key of the fingerprint. See documentation: https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm""")
@cli_util.option('--public-key-fingerprint', help=u"""The fingerprint of the API Key of the user specified by the userId. See documentation: https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_connection_update_oci_object_storage_connection_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, connection_id, display_name, description, freeform_tags, defined_tags, vault_id, key_id, nsg_ids, tenancy_id, region_parameterconflict, user_id, private_key_file, public_key_fingerprint, if_match):

    if isinstance(connection_id, six.string_types) and len(connection_id.strip()) == 0:
        raise click.UsageError('Parameter --connection-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or nsg_ids:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and nsg-ids will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if vault_id is not None:
        _details['vaultId'] = vault_id

    if key_id is not None:
        _details['keyId'] = key_id

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if tenancy_id is not None:
        _details['tenancyId'] = tenancy_id

    if region_parameterconflict is not None:
        _details['region'] = region_parameterconflict

    if user_id is not None:
        _details['userId'] = user_id

    if private_key_file is not None:
        _details['privateKeyFile'] = private_key_file

    if public_key_fingerprint is not None:
        _details['publicKeyFingerprint'] = public_key_fingerprint

    _details['connectionType'] = 'OCI_OBJECT_STORAGE'

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
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


@connection_group.command(name=cli_util.override('goldengate.update_connection_update_mysql_connection_details.command_name', 'update-connection-update-mysql-connection-details'), help=u"""Updates the Connection. \n[Command Reference](updateConnection)""")
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of a Connection.""")
@cli_util.option('--display-name', help=u"""An object's Display Name.""")
@cli_util.option('--description', help=u"""Metadata about this specific object.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.

Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Tags defined for this resource. Each key is predefined and scoped to a namespace.

Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vault-id', help=u"""The [OCID] of the customer vault being referenced. If provided, this will reference a vault which the customer will be required to ensure the policies are established to permit the GoldenGate Service to manage secrets contained within this vault.""")
@cli_util.option('--key-id', help=u"""The [OCID] of the customer \"Master\" key being referenced. If provided, this will reference a key which the customer will be required to ensure the policies are established to permit the GoldenGate Service to utilize this key to manage secrets.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--username', help=u"""The username Oracle GoldenGate uses to connect the associated RDBMS.  This username must already exist and be available for use by the database.  It must conform to the security requirements implemented by the database including length, case sensitivity, and so on.""")
@cli_util.option('--password', help=u"""The password Oracle GoldenGate uses to connect the associated RDBMS.  It must conform to the specific security requirements implemented by the database including length, case sensitivity, and so on.""")
@cli_util.option('--host', help=u"""The name or address of a host.""")
@cli_util.option('--port', type=click.INT, help=u"""The port of an endpoint usually specified for a connection.""")
@cli_util.option('--database-name', help=u"""The name of the database.""")
@cli_util.option('--security-protocol', help=u"""Security Type for MySQL.""")
@cli_util.option('--ssl-mode', help=u"""SSL modes for MySQL.""")
@cli_util.option('--ssl-ca', help=u"""Database Certificate - The base64 encoded content of mysql.pem file containing the server public key (for 1 and 2-way SSL).""")
@cli_util.option('--ssl-crl', help=u"""Certificates revoked by certificate authorities (CA). Server certificate must not be on this list (for 1 and 2-way SSL). Note: This is an optional and that too only applicable if TLS/MTLS option is selected.""")
@cli_util.option('--ssl-cert', help=u"""Client Certificate - The base64 encoded content of client-cert.pem file containing the client public key (for 2-way SSL).""")
@cli_util.option('--ssl-key', help=u"""Client Key - The client-key.pem containing the client private key (for 2-way SSL).""")
@cli_util.option('--private-ip', help=u"""The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.""")
@cli_util.option('--additional-attributes', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of name-value pair attribute entries. Used as additional parameters in connection string.

This option is a JSON list with items of type NameValuePair.  For documentation on NameValuePair please see our API reference: https://docs.cloud.oracle.com/api/#/en/goldengate/20200407/datatypes/NameValuePair.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--db-system-id', help=u"""The [OCID] of the database system being referenced.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}, 'additional-attributes': {'module': 'golden_gate', 'class': 'list[NameValuePair]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}, 'additional-attributes': {'module': 'golden_gate', 'class': 'list[NameValuePair]'}})
@cli_util.wrap_exceptions
def update_connection_update_mysql_connection_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, connection_id, display_name, description, freeform_tags, defined_tags, vault_id, key_id, nsg_ids, username, password, host, port, database_name, security_protocol, ssl_mode, ssl_ca, ssl_crl, ssl_cert, ssl_key, private_ip, additional_attributes, db_system_id, if_match):

    if isinstance(connection_id, six.string_types) and len(connection_id.strip()) == 0:
        raise click.UsageError('Parameter --connection-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or nsg_ids or additional_attributes:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and nsg-ids and additional-attributes will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if vault_id is not None:
        _details['vaultId'] = vault_id

    if key_id is not None:
        _details['keyId'] = key_id

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if username is not None:
        _details['username'] = username

    if password is not None:
        _details['password'] = password

    if host is not None:
        _details['host'] = host

    if port is not None:
        _details['port'] = port

    if database_name is not None:
        _details['databaseName'] = database_name

    if security_protocol is not None:
        _details['securityProtocol'] = security_protocol

    if ssl_mode is not None:
        _details['sslMode'] = ssl_mode

    if ssl_ca is not None:
        _details['sslCa'] = ssl_ca

    if ssl_crl is not None:
        _details['sslCrl'] = ssl_crl

    if ssl_cert is not None:
        _details['sslCert'] = ssl_cert

    if ssl_key is not None:
        _details['sslKey'] = ssl_key

    if private_ip is not None:
        _details['privateIp'] = private_ip

    if additional_attributes is not None:
        _details['additionalAttributes'] = cli_util.parse_json_parameter("additional_attributes", additional_attributes)

    if db_system_id is not None:
        _details['dbSystemId'] = db_system_id

    _details['connectionType'] = 'MYSQL'

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
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


@connection_group.command(name=cli_util.override('goldengate.update_connection_update_kafka_connection_details.command_name', 'update-connection-update-kafka-connection-details'), help=u"""Updates the Connection. \n[Command Reference](updateConnection)""")
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of a Connection.""")
@cli_util.option('--display-name', help=u"""An object's Display Name.""")
@cli_util.option('--description', help=u"""Metadata about this specific object.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.

Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Tags defined for this resource. Each key is predefined and scoped to a namespace.

Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vault-id', help=u"""The [OCID] of the customer vault being referenced. If provided, this will reference a vault which the customer will be required to ensure the policies are established to permit the GoldenGate Service to manage secrets contained within this vault.""")
@cli_util.option('--key-id', help=u"""The [OCID] of the customer \"Master\" key being referenced. If provided, this will reference a key which the customer will be required to ensure the policies are established to permit the GoldenGate Service to utilize this key to manage secrets.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--stream-pool-id', help=u"""The [OCID] of the stream pool being referenced.""")
@cli_util.option('--bootstrap-servers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Kafka bootstrap. Equivalent of bootstrap.servers configuration property in Kafka: list of KafkaBootstrapServer objects specified by host/port. Used for establishing the initial connection to the Kafka cluster. Example: `\"server1.example.com:9092,server2.example.com:9092\"`

This option is a JSON list with items of type KafkaBootstrapServer.  For documentation on KafkaBootstrapServer please see our API reference: https://docs.cloud.oracle.com/api/#/en/goldengate/20200407/datatypes/KafkaBootstrapServer.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--security-protocol', help=u"""Security Type for Kafka.""")
@cli_util.option('--username', help=u"""The username Oracle GoldenGate uses to connect the associated RDBMS.  This username must already exist and be available for use by the database.  It must conform to the security requirements implemented by the database including length, case sensitivity, and so on.""")
@cli_util.option('--password', help=u"""The password Oracle GoldenGate uses to connect the associated RDBMS.  It must conform to the specific security requirements implemented by the database including length, case sensitivity, and so on.""")
@cli_util.option('--trust-store', help=u"""The base64 encoded content of the TrustStore file.""")
@cli_util.option('--trust-store-password', help=u"""The TrustStore password.""")
@cli_util.option('--key-store', help=u"""The base64 encoded content of the KeyStore file.""")
@cli_util.option('--key-store-password', help=u"""The KeyStore password.""")
@cli_util.option('--ssl-key-password', help=u"""The password for the cert inside of of the KeyStore. In case it differs from the KeyStore password, it should be provided.""")
@cli_util.option('--consumer-properties', help=u"""The base64 encoded content of the consumer.properties file.""")
@cli_util.option('--producer-properties', help=u"""The base64 encoded content of the producer.properties file.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}, 'bootstrap-servers': {'module': 'golden_gate', 'class': 'list[KafkaBootstrapServer]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}, 'bootstrap-servers': {'module': 'golden_gate', 'class': 'list[KafkaBootstrapServer]'}})
@cli_util.wrap_exceptions
def update_connection_update_kafka_connection_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, connection_id, display_name, description, freeform_tags, defined_tags, vault_id, key_id, nsg_ids, stream_pool_id, bootstrap_servers, security_protocol, username, password, trust_store, trust_store_password, key_store, key_store_password, ssl_key_password, consumer_properties, producer_properties, if_match):

    if isinstance(connection_id, six.string_types) and len(connection_id.strip()) == 0:
        raise click.UsageError('Parameter --connection-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or nsg_ids or bootstrap_servers:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and nsg-ids and bootstrap-servers will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if vault_id is not None:
        _details['vaultId'] = vault_id

    if key_id is not None:
        _details['keyId'] = key_id

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if stream_pool_id is not None:
        _details['streamPoolId'] = stream_pool_id

    if bootstrap_servers is not None:
        _details['bootstrapServers'] = cli_util.parse_json_parameter("bootstrap_servers", bootstrap_servers)

    if security_protocol is not None:
        _details['securityProtocol'] = security_protocol

    if username is not None:
        _details['username'] = username

    if password is not None:
        _details['password'] = password

    if trust_store is not None:
        _details['trustStore'] = trust_store

    if trust_store_password is not None:
        _details['trustStorePassword'] = trust_store_password

    if key_store is not None:
        _details['keyStore'] = key_store

    if key_store_password is not None:
        _details['keyStorePassword'] = key_store_password

    if ssl_key_password is not None:
        _details['sslKeyPassword'] = ssl_key_password

    if consumer_properties is not None:
        _details['consumerProperties'] = consumer_properties

    if producer_properties is not None:
        _details['producerProperties'] = producer_properties

    _details['connectionType'] = 'KAFKA'

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
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


@connection_group.command(name=cli_util.override('goldengate.update_connection_update_golden_gate_connection_details.command_name', 'update-connection-update-golden-gate-connection-details'), help=u"""Updates the Connection. \n[Command Reference](updateConnection)""")
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of a Connection.""")
@cli_util.option('--display-name', help=u"""An object's Display Name.""")
@cli_util.option('--description', help=u"""Metadata about this specific object.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.

Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Tags defined for this resource. Each key is predefined and scoped to a namespace.

Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vault-id', help=u"""The [OCID] of the customer vault being referenced. If provided, this will reference a vault which the customer will be required to ensure the policies are established to permit the GoldenGate Service to manage secrets contained within this vault.""")
@cli_util.option('--key-id', help=u"""The [OCID] of the customer \"Master\" key being referenced. If provided, this will reference a key which the customer will be required to ensure the policies are established to permit the GoldenGate Service to utilize this key to manage secrets.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--deployment-id', help=u"""The [OCID] of the deployment being referenced.""")
@cli_util.option('--host', help=u"""The name or address of a host.""")
@cli_util.option('--port', type=click.INT, help=u"""The port of an endpoint usually specified for a connection.""")
@cli_util.option('--private-ip', help=u"""The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_connection_update_golden_gate_connection_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, connection_id, display_name, description, freeform_tags, defined_tags, vault_id, key_id, nsg_ids, deployment_id, host, port, private_ip, if_match):

    if isinstance(connection_id, six.string_types) and len(connection_id.strip()) == 0:
        raise click.UsageError('Parameter --connection-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or nsg_ids:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and nsg-ids will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if vault_id is not None:
        _details['vaultId'] = vault_id

    if key_id is not None:
        _details['keyId'] = key_id

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if deployment_id is not None:
        _details['deploymentId'] = deployment_id

    if host is not None:
        _details['host'] = host

    if port is not None:
        _details['port'] = port

    if private_ip is not None:
        _details['privateIp'] = private_ip

    _details['connectionType'] = 'GOLDENGATE'

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
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


@database_registration_group.command(name=cli_util.override('goldengate.update_database_registration.command_name', 'update'), help=u"""Note: Deprecated. Use the new resource model APIs instead. Updates the DatabaseRegistration. \n[Command Reference](updateDatabaseRegistration)""")
@cli_util.option('--database-registration-id', required=True, help=u"""A unique DatabaseRegistration identifier.""")
@cli_util.option('--display-name', help=u"""An object's Display Name.""")
@cli_util.option('--description', help=u"""Metadata about this specific object.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.

Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Tags defined for this resource. Each key is predefined and scoped to a namespace.

Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--fqdn', help=u"""A three-label Fully Qualified Domain Name (FQDN) for a resource.""")
@cli_util.option('--username', help=u"""The username Oracle GoldenGate uses to connect the associated RDBMS.  This username must already exist and be available for use by the database.  It must conform to the security requirements implemented by the database including length, case sensitivity, and so on.""")
@cli_util.option('--password', help=u"""The password Oracle GoldenGate uses to connect the associated RDBMS.  It must conform to the specific security requirements implemented by the database including length, case sensitivity, and so on.""")
@cli_util.option('--connection-string', help=u"""Connect descriptor or Easy Connect Naming method that Oracle GoldenGate uses to connect to a database.""")
@cli_util.option('--session-mode', type=custom_types.CliCaseInsensitiveChoice(["DIRECT", "REDIRECT"]), help=u"""The mode of the database connection session to be established by the data client. 'REDIRECT' - for a RAC database, 'DIRECT' - for a non-RAC database. Connection to a RAC database involves a redirection received from the SCAN listeners to the database node to connect to. By default the mode would be DIRECT.""")
@cli_util.option('--wallet', help=u"""The wallet contents Oracle GoldenGate uses to make connections to a database.  This attribute is expected to be base64 encoded.""")
@cli_util.option('--alias-name', help=u"""Credential store alias.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_database_registration(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, database_registration_id, display_name, description, freeform_tags, defined_tags, fqdn, username, password, connection_string, session_mode, wallet, alias_name, if_match):

    if isinstance(database_registration_id, six.string_types) and len(database_registration_id.strip()) == 0:
        raise click.UsageError('Parameter --database-registration-id cannot be whitespace or empty string')
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

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if fqdn is not None:
        _details['fqdn'] = fqdn

    if username is not None:
        _details['username'] = username

    if password is not None:
        _details['password'] = password

    if connection_string is not None:
        _details['connectionString'] = connection_string

    if session_mode is not None:
        _details['sessionMode'] = session_mode

    if wallet is not None:
        _details['wallet'] = wallet

    if alias_name is not None:
        _details['aliasName'] = alias_name

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.update_database_registration(
        database_registration_id=database_registration_id,
        update_database_registration_details=_details,
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


@deployment_group.command(name=cli_util.override('goldengate.update_deployment.command_name', 'update'), help=u"""Modifies a Deployment. \n[Command Reference](updateDeployment)""")
@cli_util.option('--deployment-id', required=True, help=u"""A unique Deployment identifier.""")
@cli_util.option('--display-name', help=u"""An object's Display Name.""")
@cli_util.option('--license-model', type=custom_types.CliCaseInsensitiveChoice(["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]), help=u"""The Oracle license model that applies to a Deployment.""")
@cli_util.option('--description', help=u"""Metadata about this specific object.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.

Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Tags defined for this resource. Each key is predefined and scoped to a namespace.

Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--subnet-id', help=u"""The [OCID] of the subnet being referenced.""")
@cli_util.option('--is-public', type=click.BOOL, help=u"""True if this object is publicly available.""")
@cli_util.option('--fqdn', help=u"""A three-label Fully Qualified Domain Name (FQDN) for a resource.""")
@cli_util.option('--cpu-core-count', type=click.INT, help=u"""The Minimum number of OCPUs to be made available for this Deployment.""")
@cli_util.option('--is-auto-scaling-enabled', type=click.BOOL, help=u"""Indicates if auto scaling is enabled for the Deployment's CPU core count.""")
@cli_util.option('--ogg-data', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}, 'ogg-data': {'module': 'golden_gate', 'class': 'UpdateOggDeploymentDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}, 'ogg-data': {'module': 'golden_gate', 'class': 'UpdateOggDeploymentDetails'}})
@cli_util.wrap_exceptions
def update_deployment(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deployment_id, display_name, license_model, description, freeform_tags, defined_tags, nsg_ids, subnet_id, is_public, fqdn, cpu_core_count, is_auto_scaling_enabled, ogg_data, if_match):

    if isinstance(deployment_id, six.string_types) and len(deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --deployment-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or nsg_ids or ogg_data:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and nsg-ids and ogg-data will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if license_model is not None:
        _details['licenseModel'] = license_model

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if subnet_id is not None:
        _details['subnetId'] = subnet_id

    if is_public is not None:
        _details['isPublic'] = is_public

    if fqdn is not None:
        _details['fqdn'] = fqdn

    if cpu_core_count is not None:
        _details['cpuCoreCount'] = cpu_core_count

    if is_auto_scaling_enabled is not None:
        _details['isAutoScalingEnabled'] = is_auto_scaling_enabled

    if ogg_data is not None:
        _details['oggData'] = cli_util.parse_json_parameter("ogg_data", ogg_data)

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.update_deployment(
        deployment_id=deployment_id,
        update_deployment_details=_details,
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


@deployment_backup_group.command(name=cli_util.override('goldengate.update_deployment_backup.command_name', 'update'), help=u"""Modifies a Deployment Backup. \n[Command Reference](updateDeploymentBackup)""")
@cli_util.option('--deployment-backup-id', required=True, help=u"""A unique DeploymentBackup identifier.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.

Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Tags defined for this resource. Each key is predefined and scoped to a namespace.

Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", "IN_PROGRESS", "CANCELING", "CANCELED", "SUCCEEDED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'golden_gate', 'class': 'DeploymentBackup'})
@cli_util.wrap_exceptions
def update_deployment_backup(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deployment_backup_id, freeform_tags, defined_tags, if_match):

    if isinstance(deployment_backup_id, six.string_types) and len(deployment_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --deployment-backup-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.update_deployment_backup(
        deployment_backup_id=deployment_backup_id,
        update_deployment_backup_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_deployment_backup') and callable(getattr(client, 'get_deployment_backup')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_deployment_backup(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@deployment_group.command(name=cli_util.override('goldengate.upgrade_deployment.command_name', 'upgrade'), help=u"""Upgrade a Deployment. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](upgradeDeployment)""")
@cli_util.option('--deployment-id', required=True, help=u"""A unique Deployment identifier.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["CURRENT_RELEASE"]), help=u"""The type of a deployment upgrade""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def upgrade_deployment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deployment_id, type, if_match):

    if isinstance(deployment_id, six.string_types) and len(deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --deployment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['type'] = type

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.upgrade_deployment(
        deployment_id=deployment_id,
        upgrade_deployment_details=_details,
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


@deployment_group.command(name=cli_util.override('goldengate.upgrade_deployment_upgrade_deployment_current_release_details.command_name', 'upgrade-deployment-upgrade-deployment-current-release-details'), help=u"""Upgrade a Deployment. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](upgradeDeployment)""")
@cli_util.option('--deployment-id', required=True, help=u"""A unique Deployment identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def upgrade_deployment_upgrade_deployment_current_release_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deployment_id, if_match):

    if isinstance(deployment_id, six.string_types) and len(deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --deployment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    _details['type'] = 'CURRENT_RELEASE'

    client = cli_util.build_client('golden_gate', 'golden_gate', ctx)
    result = client.upgrade_deployment(
        deployment_id=deployment_id,
        upgrade_deployment_details=_details,
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
