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


@cli.command(cli_util.override('recovery.recovery_root_group.command_name', 'recovery'), cls=CommandGroupWithAlias, help=cli_util.override('recovery.recovery_root_group.help', """Use Oracle Database Autonomous Recovery Service API to manage Protected Databases."""), short_help=cli_util.override('recovery.recovery_root_group.short_help', """Oracle Database Autonomous Recovery Service API"""))
@cli_util.help_option_group
def recovery_root_group():
    pass


@click.command(cli_util.override('recovery.protection_policy_group.command_name', 'protection-policy'), cls=CommandGroupWithAlias, help="""The details of a protection policy.A policy defines the exact number of days to retain protected database backups created by Recovery Service. Each protected database must be associated with one protection policy. You can use Oracle-defined protection policies or create custom policies to suit your internal backup storage regulation demands.""")
@cli_util.help_option_group
def protection_policy_group():
    pass


@click.command(cli_util.override('recovery.work_request_error_collection_group.command_name', 'work-request-error-collection'), cls=CommandGroupWithAlias, help="""Results of a workRequestError search. Contains both WorkRequestError items and other information, such as metadata.""")
@cli_util.help_option_group
def work_request_error_collection_group():
    pass


@click.command(cli_util.override('recovery.work_request_summary_collection_group.command_name', 'work-request-summary-collection'), cls=CommandGroupWithAlias, help="""Results of a workRequest search. Contains both WorkRequest items and other information, such as metadata.""")
@cli_util.help_option_group
def work_request_summary_collection_group():
    pass


@click.command(cli_util.override('recovery.recovery_service_subnet_group.command_name', 'recovery-service-subnet'), cls=CommandGroupWithAlias, help="""The details of a recovery service subnet. Recovery service subnets allows Recovery Service to access protected databases in each VCN. Each recovery service subnet uses a single private endpoint on a subnet of your choice within a VCN. The private endpoint need not be on the same subnet as the Oracle Cloud Database, although, it must be on a subnet that can communicate with the Oracle Cloud Database.""")
@cli_util.help_option_group
def recovery_service_subnet_group():
    pass


@click.command(cli_util.override('recovery.protection_policy_collection_group.command_name', 'protection-policy-collection'), cls=CommandGroupWithAlias, help="""Results of a Protection Policy search. Contains both Protection Policy Summary items and other information, such as metadata.""")
@cli_util.help_option_group
def protection_policy_collection_group():
    pass


@click.command(cli_util.override('recovery.protected_database_group.command_name', 'protected-database'), cls=CommandGroupWithAlias, help="""A protected database is an Oracle Cloud Database whose backups are managed by Oracle Database Autonomous Recovery Service. Each protected database requires a recovery service subnet and a protection policy to use Recovery Service as the backup destination for centralized backup and recovery""")
@cli_util.help_option_group
def protected_database_group():
    pass


@click.command(cli_util.override('recovery.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""A description of workrequest status""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('recovery.protected_database_collection_group.command_name', 'protected-database-collection'), cls=CommandGroupWithAlias, help="""Results of a protected database search operation. The results contain protected database summary and metadata information.""")
@cli_util.help_option_group
def protected_database_collection_group():
    pass


@click.command(cli_util.override('recovery.recovery_service_subnet_collection_group.command_name', 'recovery-service-subnet-collection'), cls=CommandGroupWithAlias, help="""Results of a recovery service subnet search operation. The results contain recovery service subnet summary and metadata information.""")
@cli_util.help_option_group
def recovery_service_subnet_collection_group():
    pass


@click.command(cli_util.override('recovery.work_request_log_entry_collection_group.command_name', 'work-request-log-entry-collection'), cls=CommandGroupWithAlias, help="""Results of a workRequestLog search. Contains both workRequestLog items and other information, such as metadata.""")
@cli_util.help_option_group
def work_request_log_entry_collection_group():
    pass


recovery_root_group.add_command(protection_policy_group)
recovery_root_group.add_command(work_request_error_collection_group)
recovery_root_group.add_command(work_request_summary_collection_group)
recovery_root_group.add_command(recovery_service_subnet_group)
recovery_root_group.add_command(protection_policy_collection_group)
recovery_root_group.add_command(protected_database_group)
recovery_root_group.add_command(work_request_group)
recovery_root_group.add_command(protected_database_collection_group)
recovery_root_group.add_command(recovery_service_subnet_collection_group)
recovery_root_group.add_command(work_request_log_entry_collection_group)


@protected_database_group.command(name=cli_util.override('recovery.change_protected_database_compartment.command_name', 'change-compartment'), help=u"""Moves a protected database resource from the existing compartment to the specified compartment. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeProtectedDatabaseCompartment)""")
@cli_util.option('--protected-database-id', required=True, help=u"""The protected database OCID.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the protected database should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_protected_database_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, protected_database_id, compartment_id, if_match):

    if isinstance(protected_database_id, six.string_types) and len(protected_database_id.strip()) == 0:
        raise click.UsageError('Parameter --protected-database-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('recovery', 'database_recovery', ctx)
    result = client.change_protected_database_compartment(
        protected_database_id=protected_database_id,
        change_protected_database_compartment_details=_details,
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


@protection_policy_group.command(name=cli_util.override('recovery.change_protection_policy_compartment.command_name', 'change-compartment'), help=u"""Moves a protection policy resource from the existing compartment to the specified compartment. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeProtectionPolicyCompartment)""")
@cli_util.option('--protection-policy-id', required=True, help=u"""The protection policy OCID.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the Protection Policy should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_protection_policy_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, protection_policy_id, compartment_id, if_match):

    if isinstance(protection_policy_id, six.string_types) and len(protection_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --protection-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('recovery', 'database_recovery', ctx)
    result = client.change_protection_policy_compartment(
        protection_policy_id=protection_policy_id,
        change_protection_policy_compartment_details=_details,
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


@recovery_service_subnet_group.command(name=cli_util.override('recovery.change_recovery_service_subnet_compartment.command_name', 'change-compartment'), help=u"""Moves a recovery service subnet resource from the existing compartment to the specified compartment. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeRecoveryServiceSubnetCompartment)""")
@cli_util.option('--recovery-service-subnet-id', required=True, help=u"""The recovery service subnet OCID.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the Recovery Service subnet should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_recovery_service_subnet_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, recovery_service_subnet_id, compartment_id, if_match):

    if isinstance(recovery_service_subnet_id, six.string_types) and len(recovery_service_subnet_id.strip()) == 0:
        raise click.UsageError('Parameter --recovery-service-subnet-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('recovery', 'database_recovery', ctx)
    result = client.change_recovery_service_subnet_compartment(
        recovery_service_subnet_id=recovery_service_subnet_id,
        change_recovery_service_subnet_compartment_details=_details,
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


@protected_database_group.command(name=cli_util.override('recovery.create_protected_database.command_name', 'create'), help=u"""Creates a new Protected Database. \n[Command Reference](createProtectedDatabase)""")
@cli_util.option('--display-name', required=True, help=u"""The protected database name. You can change the displayName. Avoid entering confidential information.""")
@cli_util.option('--db-unique-name', required=True, help=u"""The dbUniqueName of the protected database in Recovery Service. You cannot change the unique name.""")
@cli_util.option('--password', required=True, help=u"""Password credential which can be used to connect to Protected Database. It must contain at least 2 uppercase, 2 lowercase, 2 numeric and 2 special characters. The special characters must be underscore (_), number sign (#) or hyphen (-). The password must not contain the username \"admin\", regardless of casing.""")
@cli_util.option('--protection-policy-id', required=True, help=u"""The OCID of the protection policy associated with the protected database.""")
@cli_util.option('--recovery-service-subnets', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of recovery service subnet resources associated with the protected database.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment that contains the protected database.""")
@cli_util.option('--database-size', type=custom_types.CliCaseInsensitiveChoice(["XS", "S", "M", "L", "XL", "XXL", "AUTO"]), help=u"""The size of the protected database. XS - Less than 5GB, S - 5GB to 50GB, M - 50GB to 500GB, L - 500GB to 1TB, XL - 1TB to 5TB, XXL - Greater than 5TB.""")
@cli_util.option('--database-id', help=u"""The OCID of the protected database.""")
@cli_util.option('--database-size-in-gbs', type=click.INT, help=u"""The size of the database, in gigabytes.""")
@cli_util.option('--change-rate', help=u"""The percentage of data changes that exist in the database between successive incremental backups.""")
@cli_util.option('--compression-ratio', help=u"""The compression ratio of the protected database. The compression ratio represents the ratio of compressed block size to expanded block size.""")
@cli_util.option('--is-redo-logs-shipped', type=click.BOOL, help=u"""The value TRUE indicates that the protected database is configured to use Real-time data protection, and redo-data is sent from the protected database to Recovery Service. Real-time data protection substantially reduces the window of potential data loss that exists between successive archived redo log backups.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. For more information, see [Resource Tags]""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'recovery-service-subnets': {'module': 'recovery', 'class': 'list[RecoveryServiceSubnetInput]'}, 'freeform-tags': {'module': 'recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'recovery', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'recovery-service-subnets': {'module': 'recovery', 'class': 'list[RecoveryServiceSubnetInput]'}, 'freeform-tags': {'module': 'recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'recovery', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'recovery', 'class': 'ProtectedDatabase'})
@cli_util.wrap_exceptions
def create_protected_database(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, db_unique_name, password, protection_policy_id, recovery_service_subnets, compartment_id, database_size, database_id, database_size_in_gbs, change_rate, compression_ratio, is_redo_logs_shipped, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['dbUniqueName'] = db_unique_name
    _details['password'] = password
    _details['protectionPolicyId'] = protection_policy_id
    _details['recoveryServiceSubnets'] = cli_util.parse_json_parameter("recovery_service_subnets", recovery_service_subnets)
    _details['compartmentId'] = compartment_id

    if database_size is not None:
        _details['databaseSize'] = database_size

    if database_id is not None:
        _details['databaseId'] = database_id

    if database_size_in_gbs is not None:
        _details['databaseSizeInGBs'] = database_size_in_gbs

    if change_rate is not None:
        _details['changeRate'] = change_rate

    if compression_ratio is not None:
        _details['compressionRatio'] = compression_ratio

    if is_redo_logs_shipped is not None:
        _details['isRedoLogsShipped'] = is_redo_logs_shipped

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('recovery', 'database_recovery', ctx)
    result = client.create_protected_database(
        create_protected_database_details=_details,
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


@protection_policy_group.command(name=cli_util.override('recovery.create_protection_policy.command_name', 'create'), help=u"""Creates a new Protection Policy. \n[Command Reference](createProtectionPolicy)""")
@cli_util.option('--display-name', required=True, help=u"""A user provided name for the protection policy. The 'displayName' does not have to be unique, and it can be modified. Avoid entering confidential information.""")
@cli_util.option('--backup-retention-period-in-days', required=True, type=click.INT, help=u"""The maximum number of days to retain backups for a protected database.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. For more information, see [Resource Tags]""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'recovery', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'recovery', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'recovery', 'class': 'ProtectionPolicy'})
@cli_util.wrap_exceptions
def create_protection_policy(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, backup_retention_period_in_days, compartment_id, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['backupRetentionPeriodInDays'] = backup_retention_period_in_days
    _details['compartmentId'] = compartment_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('recovery', 'database_recovery', ctx)
    result = client.create_protection_policy(
        create_protection_policy_details=_details,
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


@recovery_service_subnet_group.command(name=cli_util.override('recovery.create_recovery_service_subnet.command_name', 'create'), help=u"""Creates a new Recovery Service Subnet. \n[Command Reference](createRecoveryServiceSubnet)""")
@cli_util.option('--display-name', required=True, help=u"""A user-provided name for the recovery service subnet. The 'displayName' does not have to be unique, and it can be modified. Avoid entering confidential information.""")
@cli_util.option('--subnet-id', required=True, help=u"""The OCID of the subnet associated with the recovery service subnet. You can create a single backup network per virtual cloud network (VCN).""")
@cli_util.option('--vcn-id', required=True, help=u"""The OCID of the virtual cloud network (VCN) that contains the recovery service subnet. You can create a single recovery service subnet per VCN.""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment OCID.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. For more information, see [Resource Tags]""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'recovery', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'recovery', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'recovery', 'class': 'RecoveryServiceSubnet'})
@cli_util.wrap_exceptions
def create_recovery_service_subnet(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, subnet_id, vcn_id, compartment_id, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['subnetId'] = subnet_id
    _details['vcnId'] = vcn_id
    _details['compartmentId'] = compartment_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('recovery', 'database_recovery', ctx)
    result = client.create_recovery_service_subnet(
        create_recovery_service_subnet_details=_details,
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


@protected_database_group.command(name=cli_util.override('recovery.delete_protected_database.command_name', 'delete'), help=u"""Deletes a protected database based on the specified protected database ID. \n[Command Reference](deleteProtectedDatabase)""")
@cli_util.option('--protected-database-id', required=True, help=u"""The protected database OCID.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_protected_database(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, protected_database_id, if_match):

    if isinstance(protected_database_id, six.string_types) and len(protected_database_id.strip()) == 0:
        raise click.UsageError('Parameter --protected-database-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('recovery', 'database_recovery', ctx)
    result = client.delete_protected_database(
        protected_database_id=protected_database_id,
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


@protection_policy_group.command(name=cli_util.override('recovery.delete_protection_policy.command_name', 'delete'), help=u"""Deletes a specified protection policy. You can delete custom policies only. Deleting a Oracle predefined policies will result in status code 405 Method Not Allowed. \n[Command Reference](deleteProtectionPolicy)""")
@cli_util.option('--protection-policy-id', required=True, help=u"""The protection policy OCID.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_protection_policy(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, protection_policy_id, if_match):

    if isinstance(protection_policy_id, six.string_types) and len(protection_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --protection-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('recovery', 'database_recovery', ctx)
    result = client.delete_protection_policy(
        protection_policy_id=protection_policy_id,
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


@recovery_service_subnet_group.command(name=cli_util.override('recovery.delete_recovery_service_subnet.command_name', 'delete'), help=u"""Deletes a specified recovery service subnet. \n[Command Reference](deleteRecoveryServiceSubnet)""")
@cli_util.option('--recovery-service-subnet-id', required=True, help=u"""The recovery service subnet OCID.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_recovery_service_subnet(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, recovery_service_subnet_id, if_match):

    if isinstance(recovery_service_subnet_id, six.string_types) and len(recovery_service_subnet_id.strip()) == 0:
        raise click.UsageError('Parameter --recovery-service-subnet-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('recovery', 'database_recovery', ctx)
    result = client.delete_recovery_service_subnet(
        recovery_service_subnet_id=recovery_service_subnet_id,
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


@protected_database_group.command(name=cli_util.override('recovery.fetch_protected_database_configuration.command_name', 'fetch-protected-database-configuration'), help=u"""Downloads the network service configuration file 'tnsnames.ora' for a specified protected database. Applies to user-defined recovery systems only. \n[Command Reference](fetchProtectedDatabaseConfiguration)""")
@cli_util.option('--protected-database-id', required=True, help=u"""The protected database OCID.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@cli_util.option('--configuration-type', type=custom_types.CliCaseInsensitiveChoice(["CABUNDLE", "TNSNAMES", "HOSTS", "ALL"]), help=u"""Currently has four config options ALL, TNSNAMES, HOSTS and CABUNDLE. All will return a zipped folder containing the contents of both tnsnames and the certificateChainPem.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def fetch_protected_database_configuration(ctx, from_json, file, protected_database_id, configuration_type, if_match):

    if isinstance(protected_database_id, six.string_types) and len(protected_database_id.strip()) == 0:
        raise click.UsageError('Parameter --protected-database-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if configuration_type is not None:
        _details['configurationType'] = configuration_type

    client = cli_util.build_client('recovery', 'database_recovery', ctx)
    result = client.fetch_protected_database_configuration(
        protected_database_id=protected_database_id,
        fetch_protected_database_configuration_details=_details,
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


@protected_database_group.command(name=cli_util.override('recovery.get_protected_database.command_name', 'get'), help=u"""Gets information about a specified protected database. \n[Command Reference](getProtectedDatabase)""")
@cli_util.option('--protected-database-id', required=True, help=u"""The protected database OCID.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'recovery', 'class': 'ProtectedDatabase'})
@cli_util.wrap_exceptions
def get_protected_database(ctx, from_json, protected_database_id):

    if isinstance(protected_database_id, six.string_types) and len(protected_database_id.strip()) == 0:
        raise click.UsageError('Parameter --protected-database-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('recovery', 'database_recovery', ctx)
    result = client.get_protected_database(
        protected_database_id=protected_database_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@protection_policy_group.command(name=cli_util.override('recovery.get_protection_policy.command_name', 'get'), help=u"""Gets information about a specified protection policy. \n[Command Reference](getProtectionPolicy)""")
@cli_util.option('--protection-policy-id', required=True, help=u"""The protection policy OCID.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'recovery', 'class': 'ProtectionPolicy'})
@cli_util.wrap_exceptions
def get_protection_policy(ctx, from_json, protection_policy_id):

    if isinstance(protection_policy_id, six.string_types) and len(protection_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --protection-policy-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('recovery', 'database_recovery', ctx)
    result = client.get_protection_policy(
        protection_policy_id=protection_policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@recovery_service_subnet_group.command(name=cli_util.override('recovery.get_recovery_service_subnet.command_name', 'get'), help=u"""Gets information about a specified recovery service subnet. \n[Command Reference](getRecoveryServiceSubnet)""")
@cli_util.option('--recovery-service-subnet-id', required=True, help=u"""The recovery service subnet OCID.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'recovery', 'class': 'RecoveryServiceSubnet'})
@cli_util.wrap_exceptions
def get_recovery_service_subnet(ctx, from_json, recovery_service_subnet_id):

    if isinstance(recovery_service_subnet_id, six.string_types) and len(recovery_service_subnet_id.strip()) == 0:
        raise click.UsageError('Parameter --recovery-service-subnet-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('recovery', 'database_recovery', ctx)
    result = client.get_recovery_service_subnet(
        recovery_service_subnet_id=recovery_service_subnet_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('recovery.get_work_request.command_name', 'get'), help=u"""Gets the status of the work request based on the specified ID \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the work request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'recovery', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('recovery', 'database_recovery', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@protected_database_collection_group.command(name=cli_util.override('recovery.list_protected_databases.command_name', 'list-protected-databases'), help=u"""Lists the protected databases based on the specified parameters. \n[Command Reference](listProtectedDatabases)""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment OCID.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only the resources that match the specified lifecycle state.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire 'displayname' given.""")
@cli_util.option('--id', help=u"""The protected database OCID.""")
@cli_util.option('--protection-policy-id', help=u"""The protection policy OCID.""")
@cli_util.option('--recovery-service-subnet-id', help=u"""The recovery service subnet OCID.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (ASC) or descending (DESC). Allowed values are:   - ASC   - DESC""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. You can provide one sort order (sortOrder). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If you do not specify a value, then TIMECREATED is used as the default sort order. Allowed values are:   - TIMECREATED   - DISPLAYNAME""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'recovery', 'class': 'ProtectedDatabaseCollection'})
@cli_util.wrap_exceptions
def list_protected_databases(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, display_name, id, protection_policy_id, recovery_service_subnet_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if id is not None:
        kwargs['id'] = id
    if protection_policy_id is not None:
        kwargs['protection_policy_id'] = protection_policy_id
    if recovery_service_subnet_id is not None:
        kwargs['recovery_service_subnet_id'] = recovery_service_subnet_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('recovery', 'database_recovery', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_protected_databases,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_protected_databases,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_protected_databases(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@protection_policy_collection_group.command(name=cli_util.override('recovery.list_protection_policies.command_name', 'list-protection-policies'), help=u"""Gets a list of protection policies based on the specified parameters. \n[Command Reference](listProtectionPolicies)""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment OCID.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources their lifecycleState matches the given lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire 'displayname' given.""")
@cli_util.option('--protection-policy-id', help=u"""The protection policy OCID.""")
@cli_util.option('--owner', type=custom_types.CliCaseInsensitiveChoice(["oracle", "customer"]), help=u"""A filter to return only the policies that match the owner as 'Customer' or 'Oracle'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return. Specify a value greater than 4.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (ASC) or descending (DESC). Allowed values are:   - ASC   - DESC""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. You can provide one sort order (sortOrder). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If you do not specify a value, then TIMECREATED is used as the default sort order. Allowed values are:   - TIMECREATED   - DISPLAYNAME""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'recovery', 'class': 'ProtectionPolicyCollection'})
@cli_util.wrap_exceptions
def list_protection_policies(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, display_name, protection_policy_id, owner, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if protection_policy_id is not None:
        kwargs['protection_policy_id'] = protection_policy_id
    if owner is not None:
        kwargs['owner'] = owner
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('recovery', 'database_recovery', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_protection_policies,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_protection_policies,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_protection_policies(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@recovery_service_subnet_collection_group.command(name=cli_util.override('recovery.list_recovery_service_subnets.command_name', 'list-recovery-service-subnets'), help=u"""Returns a list of Recovery Service Subnets. \n[Command Reference](listRecoveryServiceSubnets)""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment OCID.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only the resources that match the specified lifecycle state. Allowed values are:   - CREATING   - UPDATING   - ACTIVE   - DELETING   - DELETED   - FAILED""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire 'displayname' given.""")
@cli_util.option('--id', help=u"""The recovery service subnet OCID.""")
@cli_util.option('--vcn-id', help=u"""The OCID of the virtual cloud network (VCN) associated with the recovery service subnet.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (ASC) or descending (DESC). Allowed values are:   - ASC   - DESC""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. You can provide one sort order (sortOrder). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If you do not specify a value, then TIMECREATED is used as the default sort order. Allowed values are:   - TIMECREATED   - DISPLAYNAME""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'recovery', 'class': 'RecoveryServiceSubnetCollection'})
@cli_util.wrap_exceptions
def list_recovery_service_subnets(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, display_name, id, vcn_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if id is not None:
        kwargs['id'] = id
    if vcn_id is not None:
        kwargs['vcn_id'] = vcn_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('recovery', 'database_recovery', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_recovery_service_subnets,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_recovery_service_subnets,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_recovery_service_subnets(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_collection_group.command(name=cli_util.override('recovery.list_work_request_errors.command_name', 'list-work-request-errors'), help=u"""Return a (paginated) list of errors for a given work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the work request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (ASC) or descending (DESC). Allowed values are:   - ASC   - DESC""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'recovery', 'class': 'WorkRequestErrorCollection'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('recovery', 'database_recovery', ctx)
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


@work_request_log_entry_collection_group.command(name=cli_util.override('recovery.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Return a (paginated) list of logs for a given work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the work request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (ASC) or descending (DESC). Allowed values are:   - ASC   - DESC""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'recovery', 'class': 'WorkRequestLogEntryCollection'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('recovery', 'database_recovery', ctx)
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


@work_request_summary_collection_group.command(name=cli_util.override('recovery.list_work_requests.command_name', 'list-work-requests'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment OCID.""")
@cli_util.option('--work-request-id', help=u"""Unique Oracle-assigned identifier of the work request.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help=u"""A filter to return only resources their lifecycleState matches the given OperationStatus.""")
@cli_util.option('--resource-id', help=u"""The ID of the resource affected by the work request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (ASC) or descending (DESC). Allowed values are:   - ASC   - DESC""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'recovery', 'class': 'WorkRequestSummaryCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, work_request_id, status, resource_id, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if work_request_id is not None:
        kwargs['work_request_id'] = work_request_id
    if status is not None:
        kwargs['status'] = status
    if resource_id is not None:
        kwargs['resource_id'] = resource_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('recovery', 'database_recovery', ctx)
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


@protected_database_group.command(name=cli_util.override('recovery.update_protected_database.command_name', 'update'), help=u"""Updates the Protected Database \n[Command Reference](updateProtectedDatabase)""")
@cli_util.option('--protected-database-id', required=True, help=u"""The protected database OCID.""")
@cli_util.option('--display-name', help=u"""The protected database name. You can change the displayName. Avoid entering confidential information.""")
@cli_util.option('--database-size', type=custom_types.CliCaseInsensitiveChoice(["XS", "S", "M", "L", "XL", "XXL", "AUTO"]), help=u"""The size of the database is allowed to be decreased. XS - Less than 5GB, S - 5GB to 50GB, M - 50GB to 500GB, L - 500GB to 1TB, XL - 1TB to 5TB, XXL - Greater than 5TB.""")
@cli_util.option('--database-size-in-gbs', type=click.INT, help=u"""The size of the database, in gigabytes.""")
@cli_util.option('--password', help=u"""Password credential which can be used to connect to Protected Database. It must contain at least 2 uppercase, 2 lowercase, 2 numeric and 2 special characters. The special characters must be underscore (_), number sign (#) or hyphen (-). The password must not contain the username \"admin\", regardless of casing. Password must not be same as current passsword.""")
@cli_util.option('--protection-policy-id', help=u"""The OCID of the protection policy associated with the protected database.""")
@cli_util.option('--recovery-service-subnets', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of recovery service subnet resources associated with the protected database.

This option is a JSON list with items of type RecoveryServiceSubnetInput.  For documentation on RecoveryServiceSubnetInput please see our API reference: https://docs.cloud.oracle.com/api/#/en/databaserecovery/20210216/datatypes/RecoveryServiceSubnetInput.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-redo-logs-shipped', type=click.BOOL, help=u"""The value TRUE indicates that the protected database is configured to use Real-time data protection, and redo-data is sent from the protected database to Recovery Service. Real-time data protection substantially reduces the window of potential data loss that exists between successive archived redo log backups. For this to be effective, additional configuration is needed on client side.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. For more information, see [Resource Tags]""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'recovery-service-subnets': {'module': 'recovery', 'class': 'list[RecoveryServiceSubnetInput]'}, 'freeform-tags': {'module': 'recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'recovery', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'recovery-service-subnets': {'module': 'recovery', 'class': 'list[RecoveryServiceSubnetInput]'}, 'freeform-tags': {'module': 'recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'recovery', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_protected_database(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, protected_database_id, display_name, database_size, database_size_in_gbs, password, protection_policy_id, recovery_service_subnets, is_redo_logs_shipped, freeform_tags, defined_tags, if_match):

    if isinstance(protected_database_id, six.string_types) and len(protected_database_id.strip()) == 0:
        raise click.UsageError('Parameter --protected-database-id cannot be whitespace or empty string')
    if not force:
        if recovery_service_subnets or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to recovery-service-subnets and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if database_size is not None:
        _details['databaseSize'] = database_size

    if database_size_in_gbs is not None:
        _details['databaseSizeInGBs'] = database_size_in_gbs

    if password is not None:
        _details['password'] = password

    if protection_policy_id is not None:
        _details['protectionPolicyId'] = protection_policy_id

    if recovery_service_subnets is not None:
        _details['recoveryServiceSubnets'] = cli_util.parse_json_parameter("recovery_service_subnets", recovery_service_subnets)

    if is_redo_logs_shipped is not None:
        _details['isRedoLogsShipped'] = is_redo_logs_shipped

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('recovery', 'database_recovery', ctx)
    result = client.update_protected_database(
        protected_database_id=protected_database_id,
        update_protected_database_details=_details,
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


@protection_policy_group.command(name=cli_util.override('recovery.update_protection_policy.command_name', 'update'), help=u"""Updates the specified protection policy. \n[Command Reference](updateProtectionPolicy)""")
@cli_util.option('--protection-policy-id', required=True, help=u"""The protection policy OCID.""")
@cli_util.option('--display-name', help=u"""A user provided name for the protection policy. The 'displayName' does not have to be unique, and it can be modified. Avoid entering confidential information.""")
@cli_util.option('--backup-retention-period-in-days', type=click.INT, help=u"""The maximum number of days to retain backups for a protected database.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. For more information, see [Resource Tags]""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'recovery', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'recovery', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_protection_policy(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, protection_policy_id, display_name, backup_retention_period_in_days, freeform_tags, defined_tags, if_match):

    if isinstance(protection_policy_id, six.string_types) and len(protection_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --protection-policy-id cannot be whitespace or empty string')
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

    if backup_retention_period_in_days is not None:
        _details['backupRetentionPeriodInDays'] = backup_retention_period_in_days

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('recovery', 'database_recovery', ctx)
    result = client.update_protection_policy(
        protection_policy_id=protection_policy_id,
        update_protection_policy_details=_details,
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


@recovery_service_subnet_group.command(name=cli_util.override('recovery.update_recovery_service_subnet.command_name', 'update'), help=u"""Updates the specified recovery service subnet. \n[Command Reference](updateRecoveryServiceSubnet)""")
@cli_util.option('--recovery-service-subnet-id', required=True, help=u"""The recovery service subnet OCID.""")
@cli_util.option('--display-name', help=u"""A user-provided name for the recovery service subnet. The 'displayName' does not have to be unique, and it can be modified. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. For more information, see [Resource Tags]""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'recovery', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'recovery', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_recovery_service_subnet(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, recovery_service_subnet_id, display_name, freeform_tags, defined_tags, if_match):

    if isinstance(recovery_service_subnet_id, six.string_types) and len(recovery_service_subnet_id.strip()) == 0:
        raise click.UsageError('Parameter --recovery-service-subnet-id cannot be whitespace or empty string')
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

    client = cli_util.build_client('recovery', 'database_recovery', ctx)
    result = client.update_recovery_service_subnet(
        recovery_service_subnet_id=recovery_service_subnet_id,
        update_recovery_service_subnet_details=_details,
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
