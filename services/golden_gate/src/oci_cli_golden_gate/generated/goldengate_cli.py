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


@click.command(cli_util.override('goldengate.database_registration_group.command_name', 'database-registration'), cls=CommandGroupWithAlias, help="""Represents the metadata description of a database used by deployments in the same compartment.""")
@cli_util.help_option_group
def database_registration_group():
    pass


@click.command(cli_util.override('goldengate.deployment_upgrade_group.command_name', 'deployment-upgrade'), cls=CommandGroupWithAlias, help="""A container for your OCI GoldenGate Upgrade information.""")
@cli_util.help_option_group
def deployment_upgrade_group():
    pass


@click.command(cli_util.override('goldengate.deployment_backup_group.command_name', 'deployment-backup'), cls=CommandGroupWithAlias, help="""A backup of the current state of the GoldenGate deployment. Can be used to restore a deployment, or create a new deployment with that state as the starting deployment state.""")
@cli_util.help_option_group
def deployment_backup_group():
    pass


@click.command(cli_util.override('goldengate.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('goldengate.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""A log message from the execution of a work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('goldengate.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""The API operations that create and configure GoldenGate resources do not take effect immediately. In these cases, the operation spawns an asynchronous workflow to fulfill teh request. Work requests provide visibility into the status of these in-progress, long-running asynchronous workflows.""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('goldengate.deployment_group.command_name', 'deployment'), cls=CommandGroupWithAlias, help="""A container for your OCI GoldenGate resources, such as the OCI GoldenGate deployment console.""")
@cli_util.help_option_group
def deployment_group():
    pass


goldengate_root_group.add_command(database_registration_group)
goldengate_root_group.add_command(deployment_upgrade_group)
goldengate_root_group.add_command(deployment_backup_group)
goldengate_root_group.add_command(work_request_error_group)
goldengate_root_group.add_command(work_request_log_entry_group)
goldengate_root_group.add_command(work_request_group)
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


@database_registration_group.command(name=cli_util.override('goldengate.change_database_registration_compartment.command_name', 'change-compartment'), help=u"""Moves the DatabaseRegistration into a different compartment within the same tenancy. When provided, If-Match is checked against ETag values of the resource.  For information about moving resources between compartments, see [Moving Resources Between Compartments]. \n[Command Reference](changeDatabaseRegistrationCompartment)""")
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


@database_registration_group.command(name=cli_util.override('goldengate.create_database_registration.command_name', 'create'), help=u"""Creates a new DatabaseRegistration. \n[Command Reference](createDatabaseRegistration)""")
@cli_util.option('--display-name', required=True, help=u"""An object's Display Name.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment being referenced.""")
@cli_util.option('--fqdn', required=True, help=u"""A three-label Fully Qualified Domain Name (FQDN) for a resource.""")
@cli_util.option('--username', required=True, help=u"""The username Oracle GoldenGate uses to connect the associated RDBMS.  This username must already exist and be available for use by the database.  It must conform to the security requirements implemented by the database including length, case sensitivity, and so on.""")
@cli_util.option('--password', required=True, help=u"""The password Oracle GoldenGate uses to connect the associated RDBMS.  It must conform to the specific security requirements implemented by the database including length, case sensitivity, and so on.""")
@cli_util.option('--alias-name', required=True, help=u"""Credential store alias.""")
@cli_util.option('--description', help=u"""Metadata about this specific object.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Tags defined for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ip-address', help=u"""The private IP address in the customer's VCN of the customer's endpoint, typically a database.""")
@cli_util.option('--subnet-id', help=u"""The [OCID] of the subnet being referenced.""")
@cli_util.option('--database-id', help=u"""The [OCID] of the database being referenced.""")
@cli_util.option('--connection-string', help=u"""Connect descriptor or Easy Connect Naming method that Oracle GoldenGate uses to connect to a database.""")
@cli_util.option('--session-mode', type=custom_types.CliCaseInsensitiveChoice(["DIRECT", "REDIRECT"]), help=u"""The mode of the database connection session to be established by the data client. REDIRECT - for a RAC database, DIRECT - for a non-RAC database. Connection to a RAC database involves a redirection received from the SCAN listeners to the database node to connect to. By default the mode would be DIRECT.""")
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
@cli_util.option('--deployment-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["OGG"]), help=u"""The deployment type.""")
@cli_util.option('--description', help=u"""Metadata about this specific object.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Tags defined for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--deployment-backup-id', help=u"""The [OCID] of the backup being referenced.""")
@cli_util.option('--fqdn', help=u"""A three-label Fully Qualified Domain Name (FQDN) for a resource.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of [Network Security Group] OCIDs used to define network access for a deployment.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
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
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Tags defined for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
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


@database_registration_group.command(name=cli_util.override('goldengate.delete_database_registration.command_name', 'delete'), help=u"""Deletes a DatabaseRegistration. \n[Command Reference](deleteDatabaseRegistration)""")
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


@database_registration_group.command(name=cli_util.override('goldengate.get_database_registration.command_name', 'get'), help=u"""Retrieves a DatabaseRegistration. \n[Command Reference](getDatabaseRegistration)""")
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
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
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


@database_registration_group.command(name=cli_util.override('goldengate.list_database_registrations.command_name', 'list'), help=u"""Lists the DatabaseRegistrations in the compartment. \n[Command Reference](listDatabaseRegistrations)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
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
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--deployment-id', help=u"""The ID of the deployment in which to list resources.""")
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


@deployment_upgrade_group.command(name=cli_util.override('goldengate.list_deployment_upgrades.command_name', 'list'), help=u"""Lists the Deployment Upgrades in a compartment. \n[Command Reference](listDeploymentUpgrades)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--deployment-id', help=u"""The ID of the deployment in which to list resources.""")
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
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
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
def list_deployments(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, lifecycle_sub_state, display_name, fqdn, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
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


@work_request_error_group.command(name=cli_util.override('goldengate.list_work_request_errors.command_name', 'list'), help=u"""Lists work request errors. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
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
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
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
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--resource-id', help=u"""The ID of the resource in which to list resources.""")
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


@database_registration_group.command(name=cli_util.override('goldengate.update_database_registration.command_name', 'update'), help=u"""Updates the DatabaseRegistration. \n[Command Reference](updateDatabaseRegistration)""")
@cli_util.option('--database-registration-id', required=True, help=u"""A unique DatabaseRegistration identifier.""")
@cli_util.option('--display-name', help=u"""An object's Display Name.""")
@cli_util.option('--description', help=u"""Metadata about this specific object.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Tags defined for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--fqdn', help=u"""A three-label Fully Qualified Domain Name (FQDN) for a resource.""")
@cli_util.option('--username', help=u"""The username Oracle GoldenGate uses to connect the associated RDBMS.  This username must already exist and be available for use by the database.  It must conform to the security requirements implemented by the database including length, case sensitivity, and so on.""")
@cli_util.option('--password', help=u"""The password Oracle GoldenGate uses to connect the associated RDBMS.  It must conform to the specific security requirements implemented by the database including length, case sensitivity, and so on.""")
@cli_util.option('--connection-string', help=u"""Connect descriptor or Easy Connect Naming method that Oracle GoldenGate uses to connect to a database.""")
@cli_util.option('--session-mode', type=custom_types.CliCaseInsensitiveChoice(["DIRECT", "REDIRECT"]), help=u"""The mode of the database connection session to be established by the data client. REDIRECT - for a RAC database, DIRECT - for a non-RAC database. Connection to a RAC database involves a redirection received from the SCAN listeners to the database node to connect to. By default the mode would be DIRECT.""")
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
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Tags defined for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of [Network Security Group] OCIDs used to define network access for a deployment.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
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
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Tags defined for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
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
