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


@cli.command(cli_util.override('application_migration.application_migration_root_group.command_name', 'application-migration'), cls=CommandGroupWithAlias, help=cli_util.override('application_migration.application_migration_root_group.help', """Application Migration simplifies the migration of applications from Oracle Cloud Infrastructure Classic to Oracle Cloud Infrastructure.
You can use Application Migration API to migrate applications, such as Oracle Java Cloud Service, SOA Cloud Service, and Integration Classic
instances, to Oracle Cloud Infrastructure. For more information, see
[Overview of Application Migration]."""), short_help=cli_util.override('application_migration.application_migration_root_group.short_help', """Application Migration API"""))
@cli_util.help_option_group
def application_migration_root_group():
    pass


@click.command(cli_util.override('application_migration.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing an operation that is tracked by a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('application_migration.migration_group.command_name', 'migration'), cls=CommandGroupWithAlias, help="""The properties that define a migration. A migration represents the end-to-end workflow of moving an application from a source environment to Oracle Cloud Infrastructure. Each migration moves a single application to Oracle Cloud Infrastructure. For more information, see [Manage Migrations].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def migration_group():
    pass


@click.command(cli_util.override('application_migration.source_application_group.command_name', 'source-application'), cls=CommandGroupWithAlias, help="""Details about an application running in the source environment that you can migrate to Oracle Cloud Infrastructure.""")
@cli_util.help_option_group
def source_application_group():
    pass


@click.command(cli_util.override('application_migration.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""A log message about the execution of an operation that is tracked by a work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('application_migration.source_group.command_name', 'source'), cls=CommandGroupWithAlias, help="""The properties that define a source. Source refers to the source environment from which you migrate an application to Oracle Cloud Infrastructure. For more information, see [Manage Sources].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def source_group():
    pass


@click.command(cli_util.override('application_migration.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""An asynchronous work request.""")
@cli_util.help_option_group
def work_request_group():
    pass


application_migration_root_group.add_command(work_request_error_group)
application_migration_root_group.add_command(migration_group)
application_migration_root_group.add_command(source_application_group)
application_migration_root_group.add_command(work_request_log_entry_group)
application_migration_root_group.add_command(source_group)
application_migration_root_group.add_command(work_request_group)


@work_request_group.command(name=cli_util.override('application_migration.cancel_work_request.command_name', 'cancel'), help=u"""Cancels the specified work request. When you cancel a work request, it causes the in-progress task to be canceled. For example, if the create migration work request is in the accepted or in progress state for a long time, you can cancel the work request.

When you cancel a work request, the state of the work request changes to cancelling, and then to the cancelled state. \n[Command Reference](cancelWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the work request.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_work_request(ctx, from_json, work_request_id, if_match):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.cancel_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@migration_group.command(name=cli_util.override('application_migration.change_migration_compartment.command_name', 'change-compartment'), help=u"""Moves the specified migration into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeMigrationCompartment)""")
@cli_util.option('--migration-id', required=True, help=u"""The [OCID] of the migration.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the resource to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_migration_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, migration_id, compartment_id, if_match):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.change_migration_compartment(
        migration_id=migration_id,
        change_migration_compartment_details=_details,
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


@source_group.command(name=cli_util.override('application_migration.change_source_compartment.command_name', 'change-compartment'), help=u"""Moves the specified source into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeSourceCompartment)""")
@cli_util.option('--source-id', required=True, help=u"""The [OCID] of the source.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the resource to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_source_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, source_id, compartment_id, if_match):

    if isinstance(source_id, six.string_types) and len(source_id.strip()) == 0:
        raise click.UsageError('Parameter --source-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.change_source_compartment(
        source_id=source_id,
        change_source_compartment_details=_details,
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


@migration_group.command(name=cli_util.override('application_migration.create_migration.command_name', 'create'), help=u"""Creates a migration. A migration represents the end-to-end workflow of moving an application from a source environment to Oracle Cloud Infrastructure. Each migration moves a single application to Oracle Cloud Infrastructure. For more information, see [Manage Migrations].

When you create a migration, provide the required information to let Application Migration access the source environment. Application Migration uses this information to access the application in the source environment and discover application artifacts.

All Oracle Cloud Infrastructure resources, including migrations, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. For more information, see Resource Identifiers.

After you send your request, a migration is created in the compartment that contains the source. The new migration's lifecycle state will temporarily be <code>CREATING</code> and the state of the migration will be <code>DISCOVERING_APPLICATION</code>. During this phase, Application Migration sets the template for the <code>serviceConfig</code> and <code>applicationConfig</code> fields of the migration. When this operation is complete, the state of the migration changes to <code>MISSING_CONFIG_VALUES</code>. Next, you'll need to update the migration to provide configuration values. Before updating the migration, ensure that its state has changed to <code>MISSING_CONFIG_VALUES</code>.

To track the progress of this operation, you can monitor the status of the Create Migration and Discover Application work requests by using the <code>[GetWorkRequest]</code> REST API operation on the work request or by viewing the status of the work request in the console. \n[Command Reference](createMigration)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment that contains the source.""")
@cli_util.option('--source-id', required=True, help=u"""The [OCID] of the source.""")
@cli_util.option('--application-name', required=True, help=u"""Name of the application that you want to migrate from the source environment.""")
@cli_util.option('--discovery-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""User-friendly name of the application. This will be the name of the migrated application in Oracle Cloud Infrastructure.""")
@cli_util.option('--description', help=u"""Description of the application that you are migrating.""")
@cli_util.option('--pre-created-target-database-type', type=custom_types.CliCaseInsensitiveChoice(["DATABASE_SYSTEM", "NOT_SET"]), help=u"""The pre-existing database type to be used in this migration. Currently, Application migration only supports Oracle Cloud Infrastructure databases and this option is currently available only for `JAVA_CLOUD_SERVICE` and `WEBLOGIC_CLOUD_SERVICE` target instance types.""")
@cli_util.option('--is-selective-migration', type=click.BOOL, help=u"""If set to `true`, Application Migration migrates the application resources selectively depending on the source.""")
@cli_util.option('--service-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'discovery-details': {'module': 'application_migration', 'class': 'DiscoveryDetails'}, 'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'discovery-details': {'module': 'application_migration', 'class': 'DiscoveryDetails'}, 'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'application_migration', 'class': 'Migration'})
@cli_util.wrap_exceptions
def create_migration(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, source_id, application_name, discovery_details, display_name, description, pre_created_target_database_type, is_selective_migration, service_config, application_config, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['sourceId'] = source_id
    _details['applicationName'] = application_name
    _details['discoveryDetails'] = cli_util.parse_json_parameter("discovery_details", discovery_details)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if pre_created_target_database_type is not None:
        _details['preCreatedTargetDatabaseType'] = pre_created_target_database_type

    if is_selective_migration is not None:
        _details['isSelectiveMigration'] = is_selective_migration

    if service_config is not None:
        _details['serviceConfig'] = cli_util.parse_json_parameter("service_config", service_config)

    if application_config is not None:
        _details['applicationConfig'] = cli_util.parse_json_parameter("application_config", application_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
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


@migration_group.command(name=cli_util.override('application_migration.create_migration_oic_discovery_details.command_name', 'create-migration-oic-discovery-details'), help=u"""Creates a migration. A migration represents the end-to-end workflow of moving an application from a source environment to Oracle Cloud Infrastructure. Each migration moves a single application to Oracle Cloud Infrastructure. For more information, see [Manage Migrations].

When you create a migration, provide the required information to let Application Migration access the source environment. Application Migration uses this information to access the application in the source environment and discover application artifacts.

All Oracle Cloud Infrastructure resources, including migrations, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. For more information, see Resource Identifiers.

After you send your request, a migration is created in the compartment that contains the source. The new migration's lifecycle state will temporarily be <code>CREATING</code> and the state of the migration will be <code>DISCOVERING_APPLICATION</code>. During this phase, Application Migration sets the template for the <code>serviceConfig</code> and <code>applicationConfig</code> fields of the migration. When this operation is complete, the state of the migration changes to <code>MISSING_CONFIG_VALUES</code>. Next, you'll need to update the migration to provide configuration values. Before updating the migration, ensure that its state has changed to <code>MISSING_CONFIG_VALUES</code>.

To track the progress of this operation, you can monitor the status of the Create Migration and Discover Application work requests by using the <code>[GetWorkRequest]</code> REST API operation on the work request or by viewing the status of the work request in the console. \n[Command Reference](createMigration)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment that contains the source.""")
@cli_util.option('--source-id', required=True, help=u"""The [OCID] of the source.""")
@cli_util.option('--application-name', required=True, help=u"""Name of the application that you want to migrate from the source environment.""")
@cli_util.option('--discovery-details-service-instance-user', required=True, help=u"""Application administrator username to access the Oracle Integration Classic instance in the source environment.""")
@cli_util.option('--discovery-details-service-instance-password', required=True, help=u"""Password for this user.""")
@cli_util.option('--display-name', help=u"""User-friendly name of the application. This will be the name of the migrated application in Oracle Cloud Infrastructure.""")
@cli_util.option('--description', help=u"""Description of the application that you are migrating.""")
@cli_util.option('--pre-created-target-database-type', type=custom_types.CliCaseInsensitiveChoice(["DATABASE_SYSTEM", "NOT_SET"]), help=u"""The pre-existing database type to be used in this migration. Currently, Application migration only supports Oracle Cloud Infrastructure databases and this option is currently available only for `JAVA_CLOUD_SERVICE` and `WEBLOGIC_CLOUD_SERVICE` target instance types.""")
@cli_util.option('--is-selective-migration', type=click.BOOL, help=u"""If set to `true`, Application Migration migrates the application resources selectively depending on the source.""")
@cli_util.option('--service-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'application_migration', 'class': 'Migration'})
@cli_util.wrap_exceptions
def create_migration_oic_discovery_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, source_id, application_name, discovery_details_service_instance_user, discovery_details_service_instance_password, display_name, description, pre_created_target_database_type, is_selective_migration, service_config, application_config, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['discoveryDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['sourceId'] = source_id
    _details['applicationName'] = application_name
    _details['discoveryDetails']['serviceInstanceUser'] = discovery_details_service_instance_user
    _details['discoveryDetails']['serviceInstancePassword'] = discovery_details_service_instance_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if pre_created_target_database_type is not None:
        _details['preCreatedTargetDatabaseType'] = pre_created_target_database_type

    if is_selective_migration is not None:
        _details['isSelectiveMigration'] = is_selective_migration

    if service_config is not None:
        _details['serviceConfig'] = cli_util.parse_json_parameter("service_config", service_config)

    if application_config is not None:
        _details['applicationConfig'] = cli_util.parse_json_parameter("application_config", application_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['discoveryDetails']['type'] = 'OIC'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
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


@migration_group.command(name=cli_util.override('application_migration.create_migration_pcs_discovery_details.command_name', 'create-migration-pcs-discovery-details'), help=u"""Creates a migration. A migration represents the end-to-end workflow of moving an application from a source environment to Oracle Cloud Infrastructure. Each migration moves a single application to Oracle Cloud Infrastructure. For more information, see [Manage Migrations].

When you create a migration, provide the required information to let Application Migration access the source environment. Application Migration uses this information to access the application in the source environment and discover application artifacts.

All Oracle Cloud Infrastructure resources, including migrations, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. For more information, see Resource Identifiers.

After you send your request, a migration is created in the compartment that contains the source. The new migration's lifecycle state will temporarily be <code>CREATING</code> and the state of the migration will be <code>DISCOVERING_APPLICATION</code>. During this phase, Application Migration sets the template for the <code>serviceConfig</code> and <code>applicationConfig</code> fields of the migration. When this operation is complete, the state of the migration changes to <code>MISSING_CONFIG_VALUES</code>. Next, you'll need to update the migration to provide configuration values. Before updating the migration, ensure that its state has changed to <code>MISSING_CONFIG_VALUES</code>.

To track the progress of this operation, you can monitor the status of the Create Migration and Discover Application work requests by using the <code>[GetWorkRequest]</code> REST API operation on the work request or by viewing the status of the work request in the console. \n[Command Reference](createMigration)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment that contains the source.""")
@cli_util.option('--source-id', required=True, help=u"""The [OCID] of the source.""")
@cli_util.option('--application-name', required=True, help=u"""Name of the application that you want to migrate from the source environment.""")
@cli_util.option('--discovery-details-service-instance-user', required=True, help=u"""Application administrator username to access the Oracle Process Cloud Service application in the source environment.""")
@cli_util.option('--discovery-details-service-instance-password', required=True, help=u"""Password for this user.""")
@cli_util.option('--display-name', help=u"""User-friendly name of the application. This will be the name of the migrated application in Oracle Cloud Infrastructure.""")
@cli_util.option('--description', help=u"""Description of the application that you are migrating.""")
@cli_util.option('--pre-created-target-database-type', type=custom_types.CliCaseInsensitiveChoice(["DATABASE_SYSTEM", "NOT_SET"]), help=u"""The pre-existing database type to be used in this migration. Currently, Application migration only supports Oracle Cloud Infrastructure databases and this option is currently available only for `JAVA_CLOUD_SERVICE` and `WEBLOGIC_CLOUD_SERVICE` target instance types.""")
@cli_util.option('--is-selective-migration', type=click.BOOL, help=u"""If set to `true`, Application Migration migrates the application resources selectively depending on the source.""")
@cli_util.option('--service-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'application_migration', 'class': 'Migration'})
@cli_util.wrap_exceptions
def create_migration_pcs_discovery_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, source_id, application_name, discovery_details_service_instance_user, discovery_details_service_instance_password, display_name, description, pre_created_target_database_type, is_selective_migration, service_config, application_config, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['discoveryDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['sourceId'] = source_id
    _details['applicationName'] = application_name
    _details['discoveryDetails']['serviceInstanceUser'] = discovery_details_service_instance_user
    _details['discoveryDetails']['serviceInstancePassword'] = discovery_details_service_instance_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if pre_created_target_database_type is not None:
        _details['preCreatedTargetDatabaseType'] = pre_created_target_database_type

    if is_selective_migration is not None:
        _details['isSelectiveMigration'] = is_selective_migration

    if service_config is not None:
        _details['serviceConfig'] = cli_util.parse_json_parameter("service_config", service_config)

    if application_config is not None:
        _details['applicationConfig'] = cli_util.parse_json_parameter("application_config", application_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['discoveryDetails']['type'] = 'PCS'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
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


@migration_group.command(name=cli_util.override('application_migration.create_migration_ics_discovery_details.command_name', 'create-migration-ics-discovery-details'), help=u"""Creates a migration. A migration represents the end-to-end workflow of moving an application from a source environment to Oracle Cloud Infrastructure. Each migration moves a single application to Oracle Cloud Infrastructure. For more information, see [Manage Migrations].

When you create a migration, provide the required information to let Application Migration access the source environment. Application Migration uses this information to access the application in the source environment and discover application artifacts.

All Oracle Cloud Infrastructure resources, including migrations, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. For more information, see Resource Identifiers.

After you send your request, a migration is created in the compartment that contains the source. The new migration's lifecycle state will temporarily be <code>CREATING</code> and the state of the migration will be <code>DISCOVERING_APPLICATION</code>. During this phase, Application Migration sets the template for the <code>serviceConfig</code> and <code>applicationConfig</code> fields of the migration. When this operation is complete, the state of the migration changes to <code>MISSING_CONFIG_VALUES</code>. Next, you'll need to update the migration to provide configuration values. Before updating the migration, ensure that its state has changed to <code>MISSING_CONFIG_VALUES</code>.

To track the progress of this operation, you can monitor the status of the Create Migration and Discover Application work requests by using the <code>[GetWorkRequest]</code> REST API operation on the work request or by viewing the status of the work request in the console. \n[Command Reference](createMigration)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment that contains the source.""")
@cli_util.option('--source-id', required=True, help=u"""The [OCID] of the source.""")
@cli_util.option('--application-name', required=True, help=u"""Name of the application that you want to migrate from the source environment.""")
@cli_util.option('--discovery-details-service-instance-user', required=True, help=u"""Application administrator username to access the Oracle Integration Cloud Service application in the source environment.""")
@cli_util.option('--discovery-details-service-instance-password', required=True, help=u"""Password for this user.""")
@cli_util.option('--display-name', help=u"""User-friendly name of the application. This will be the name of the migrated application in Oracle Cloud Infrastructure.""")
@cli_util.option('--description', help=u"""Description of the application that you are migrating.""")
@cli_util.option('--pre-created-target-database-type', type=custom_types.CliCaseInsensitiveChoice(["DATABASE_SYSTEM", "NOT_SET"]), help=u"""The pre-existing database type to be used in this migration. Currently, Application migration only supports Oracle Cloud Infrastructure databases and this option is currently available only for `JAVA_CLOUD_SERVICE` and `WEBLOGIC_CLOUD_SERVICE` target instance types.""")
@cli_util.option('--is-selective-migration', type=click.BOOL, help=u"""If set to `true`, Application Migration migrates the application resources selectively depending on the source.""")
@cli_util.option('--service-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'application_migration', 'class': 'Migration'})
@cli_util.wrap_exceptions
def create_migration_ics_discovery_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, source_id, application_name, discovery_details_service_instance_user, discovery_details_service_instance_password, display_name, description, pre_created_target_database_type, is_selective_migration, service_config, application_config, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['discoveryDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['sourceId'] = source_id
    _details['applicationName'] = application_name
    _details['discoveryDetails']['serviceInstanceUser'] = discovery_details_service_instance_user
    _details['discoveryDetails']['serviceInstancePassword'] = discovery_details_service_instance_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if pre_created_target_database_type is not None:
        _details['preCreatedTargetDatabaseType'] = pre_created_target_database_type

    if is_selective_migration is not None:
        _details['isSelectiveMigration'] = is_selective_migration

    if service_config is not None:
        _details['serviceConfig'] = cli_util.parse_json_parameter("service_config", service_config)

    if application_config is not None:
        _details['applicationConfig'] = cli_util.parse_json_parameter("application_config", application_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['discoveryDetails']['type'] = 'ICS'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
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


@migration_group.command(name=cli_util.override('application_migration.create_migration_oac_discovery_details.command_name', 'create-migration-oac-discovery-details'), help=u"""Creates a migration. A migration represents the end-to-end workflow of moving an application from a source environment to Oracle Cloud Infrastructure. Each migration moves a single application to Oracle Cloud Infrastructure. For more information, see [Manage Migrations].

When you create a migration, provide the required information to let Application Migration access the source environment. Application Migration uses this information to access the application in the source environment and discover application artifacts.

All Oracle Cloud Infrastructure resources, including migrations, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. For more information, see Resource Identifiers.

After you send your request, a migration is created in the compartment that contains the source. The new migration's lifecycle state will temporarily be <code>CREATING</code> and the state of the migration will be <code>DISCOVERING_APPLICATION</code>. During this phase, Application Migration sets the template for the <code>serviceConfig</code> and <code>applicationConfig</code> fields of the migration. When this operation is complete, the state of the migration changes to <code>MISSING_CONFIG_VALUES</code>. Next, you'll need to update the migration to provide configuration values. Before updating the migration, ensure that its state has changed to <code>MISSING_CONFIG_VALUES</code>.

To track the progress of this operation, you can monitor the status of the Create Migration and Discover Application work requests by using the <code>[GetWorkRequest]</code> REST API operation on the work request or by viewing the status of the work request in the console. \n[Command Reference](createMigration)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment that contains the source.""")
@cli_util.option('--source-id', required=True, help=u"""The [OCID] of the source.""")
@cli_util.option('--application-name', required=True, help=u"""Name of the application that you want to migrate from the source environment.""")
@cli_util.option('--discovery-details-service-instance-user', required=True, help=u"""This field is currently not supported. You must enter a value, such as <code>unused</code>. However, the value that you enter is ignored.""")
@cli_util.option('--discovery-details-service-instance-password', required=True, help=u"""This field is currently not supported. You must enter a value, such as <code>unused</code>. However, the value that you enter is ignored.""")
@cli_util.option('--display-name', help=u"""User-friendly name of the application. This will be the name of the migrated application in Oracle Cloud Infrastructure.""")
@cli_util.option('--description', help=u"""Description of the application that you are migrating.""")
@cli_util.option('--pre-created-target-database-type', type=custom_types.CliCaseInsensitiveChoice(["DATABASE_SYSTEM", "NOT_SET"]), help=u"""The pre-existing database type to be used in this migration. Currently, Application migration only supports Oracle Cloud Infrastructure databases and this option is currently available only for `JAVA_CLOUD_SERVICE` and `WEBLOGIC_CLOUD_SERVICE` target instance types.""")
@cli_util.option('--is-selective-migration', type=click.BOOL, help=u"""If set to `true`, Application Migration migrates the application resources selectively depending on the source.""")
@cli_util.option('--service-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'application_migration', 'class': 'Migration'})
@cli_util.wrap_exceptions
def create_migration_oac_discovery_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, source_id, application_name, discovery_details_service_instance_user, discovery_details_service_instance_password, display_name, description, pre_created_target_database_type, is_selective_migration, service_config, application_config, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['discoveryDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['sourceId'] = source_id
    _details['applicationName'] = application_name
    _details['discoveryDetails']['serviceInstanceUser'] = discovery_details_service_instance_user
    _details['discoveryDetails']['serviceInstancePassword'] = discovery_details_service_instance_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if pre_created_target_database_type is not None:
        _details['preCreatedTargetDatabaseType'] = pre_created_target_database_type

    if is_selective_migration is not None:
        _details['isSelectiveMigration'] = is_selective_migration

    if service_config is not None:
        _details['serviceConfig'] = cli_util.parse_json_parameter("service_config", service_config)

    if application_config is not None:
        _details['applicationConfig'] = cli_util.parse_json_parameter("application_config", application_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['discoveryDetails']['type'] = 'OAC'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
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


@migration_group.command(name=cli_util.override('application_migration.create_migration_jcs_discovery_details.command_name', 'create-migration-jcs-discovery-details'), help=u"""Creates a migration. A migration represents the end-to-end workflow of moving an application from a source environment to Oracle Cloud Infrastructure. Each migration moves a single application to Oracle Cloud Infrastructure. For more information, see [Manage Migrations].

When you create a migration, provide the required information to let Application Migration access the source environment. Application Migration uses this information to access the application in the source environment and discover application artifacts.

All Oracle Cloud Infrastructure resources, including migrations, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. For more information, see Resource Identifiers.

After you send your request, a migration is created in the compartment that contains the source. The new migration's lifecycle state will temporarily be <code>CREATING</code> and the state of the migration will be <code>DISCOVERING_APPLICATION</code>. During this phase, Application Migration sets the template for the <code>serviceConfig</code> and <code>applicationConfig</code> fields of the migration. When this operation is complete, the state of the migration changes to <code>MISSING_CONFIG_VALUES</code>. Next, you'll need to update the migration to provide configuration values. Before updating the migration, ensure that its state has changed to <code>MISSING_CONFIG_VALUES</code>.

To track the progress of this operation, you can monitor the status of the Create Migration and Discover Application work requests by using the <code>[GetWorkRequest]</code> REST API operation on the work request or by viewing the status of the work request in the console. \n[Command Reference](createMigration)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment that contains the source.""")
@cli_util.option('--source-id', required=True, help=u"""The [OCID] of the source.""")
@cli_util.option('--application-name', required=True, help=u"""Name of the application that you want to migrate from the source environment.""")
@cli_util.option('--discovery-details-weblogic-user', required=True, help=u"""WebLogic administrator username for the Oracle Java Cloud Service application in the source environment.""")
@cli_util.option('--discovery-details-weblogic-password', required=True, help=u"""The password of the WebLogic administrator for the Oracle Java Cloud Service application in the source environment.""")
@cli_util.option('--display-name', help=u"""User-friendly name of the application. This will be the name of the migrated application in Oracle Cloud Infrastructure.""")
@cli_util.option('--description', help=u"""Description of the application that you are migrating.""")
@cli_util.option('--pre-created-target-database-type', type=custom_types.CliCaseInsensitiveChoice(["DATABASE_SYSTEM", "NOT_SET"]), help=u"""The pre-existing database type to be used in this migration. Currently, Application migration only supports Oracle Cloud Infrastructure databases and this option is currently available only for `JAVA_CLOUD_SERVICE` and `WEBLOGIC_CLOUD_SERVICE` target instance types.""")
@cli_util.option('--is-selective-migration', type=click.BOOL, help=u"""If set to `true`, Application Migration migrates the application resources selectively depending on the source.""")
@cli_util.option('--service-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'application_migration', 'class': 'Migration'})
@cli_util.wrap_exceptions
def create_migration_jcs_discovery_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, source_id, application_name, discovery_details_weblogic_user, discovery_details_weblogic_password, display_name, description, pre_created_target_database_type, is_selective_migration, service_config, application_config, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['discoveryDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['sourceId'] = source_id
    _details['applicationName'] = application_name
    _details['discoveryDetails']['weblogicUser'] = discovery_details_weblogic_user
    _details['discoveryDetails']['weblogicPassword'] = discovery_details_weblogic_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if pre_created_target_database_type is not None:
        _details['preCreatedTargetDatabaseType'] = pre_created_target_database_type

    if is_selective_migration is not None:
        _details['isSelectiveMigration'] = is_selective_migration

    if service_config is not None:
        _details['serviceConfig'] = cli_util.parse_json_parameter("service_config", service_config)

    if application_config is not None:
        _details['applicationConfig'] = cli_util.parse_json_parameter("application_config", application_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['discoveryDetails']['type'] = 'JCS'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
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


@migration_group.command(name=cli_util.override('application_migration.create_migration_soacs_discovery_details.command_name', 'create-migration-soacs-discovery-details'), help=u"""Creates a migration. A migration represents the end-to-end workflow of moving an application from a source environment to Oracle Cloud Infrastructure. Each migration moves a single application to Oracle Cloud Infrastructure. For more information, see [Manage Migrations].

When you create a migration, provide the required information to let Application Migration access the source environment. Application Migration uses this information to access the application in the source environment and discover application artifacts.

All Oracle Cloud Infrastructure resources, including migrations, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. For more information, see Resource Identifiers.

After you send your request, a migration is created in the compartment that contains the source. The new migration's lifecycle state will temporarily be <code>CREATING</code> and the state of the migration will be <code>DISCOVERING_APPLICATION</code>. During this phase, Application Migration sets the template for the <code>serviceConfig</code> and <code>applicationConfig</code> fields of the migration. When this operation is complete, the state of the migration changes to <code>MISSING_CONFIG_VALUES</code>. Next, you'll need to update the migration to provide configuration values. Before updating the migration, ensure that its state has changed to <code>MISSING_CONFIG_VALUES</code>.

To track the progress of this operation, you can monitor the status of the Create Migration and Discover Application work requests by using the <code>[GetWorkRequest]</code> REST API operation on the work request or by viewing the status of the work request in the console. \n[Command Reference](createMigration)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment that contains the source.""")
@cli_util.option('--source-id', required=True, help=u"""The [OCID] of the source.""")
@cli_util.option('--application-name', required=True, help=u"""Name of the application that you want to migrate from the source environment.""")
@cli_util.option('--discovery-details-weblogic-user', required=True, help=u"""WebLogic administrator username for the Oracle SOA Cloud Service application in the source environment.""")
@cli_util.option('--discovery-details-weblogic-password', required=True, help=u"""Password for this user.""")
@cli_util.option('--display-name', help=u"""User-friendly name of the application. This will be the name of the migrated application in Oracle Cloud Infrastructure.""")
@cli_util.option('--description', help=u"""Description of the application that you are migrating.""")
@cli_util.option('--pre-created-target-database-type', type=custom_types.CliCaseInsensitiveChoice(["DATABASE_SYSTEM", "NOT_SET"]), help=u"""The pre-existing database type to be used in this migration. Currently, Application migration only supports Oracle Cloud Infrastructure databases and this option is currently available only for `JAVA_CLOUD_SERVICE` and `WEBLOGIC_CLOUD_SERVICE` target instance types.""")
@cli_util.option('--is-selective-migration', type=click.BOOL, help=u"""If set to `true`, Application Migration migrates the application resources selectively depending on the source.""")
@cli_util.option('--service-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'application_migration', 'class': 'Migration'})
@cli_util.wrap_exceptions
def create_migration_soacs_discovery_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, source_id, application_name, discovery_details_weblogic_user, discovery_details_weblogic_password, display_name, description, pre_created_target_database_type, is_selective_migration, service_config, application_config, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['discoveryDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['sourceId'] = source_id
    _details['applicationName'] = application_name
    _details['discoveryDetails']['weblogicUser'] = discovery_details_weblogic_user
    _details['discoveryDetails']['weblogicPassword'] = discovery_details_weblogic_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if pre_created_target_database_type is not None:
        _details['preCreatedTargetDatabaseType'] = pre_created_target_database_type

    if is_selective_migration is not None:
        _details['isSelectiveMigration'] = is_selective_migration

    if service_config is not None:
        _details['serviceConfig'] = cli_util.parse_json_parameter("service_config", service_config)

    if application_config is not None:
        _details['applicationConfig'] = cli_util.parse_json_parameter("application_config", application_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['discoveryDetails']['type'] = 'SOACS'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
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


@source_group.command(name=cli_util.override('application_migration.create_source.command_name', 'create'), help=u"""Creates a source in the specified compartment. In Application Migration, a source refers to the environment from which the application is being migrated. For more information, see [Manage Sources].

All Oracle Cloud Infrastructure resources, including sources, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console.

After you send your request, a source is created in the specified compartment. The new source's lifecycle state will temporarily be <code>CREATING</code>. Application Migration connects to the source environment with the authentication credentials that you have provided. If the connection is established, the status of the source changes to <code>ACTIVE</code> and Application Migration fetches the list of applications that are available for migration in the source environment.

To track the progress of the operation, you can monitor the status of the Create Source work request by using the <code>[GetWorkRequest]</code> REST API operation on the work request or by viewing the status of the work request in the console.

Ensure that the state of the source has changed to <code>ACTIVE</code>, before you retrieve the list of applications from the source environment using the <code>[ListSourceApplications]</code> REST API call. \n[Command Reference](createSource)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment that contains the source.""")
@cli_util.option('--source-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--description', help=u"""Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--authorization-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'application_migration', 'class': 'Source'})
@cli_util.wrap_exceptions
def create_source(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, source_details, display_name, description, authorization_details, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if authorization_details is not None:
        _details['authorizationDetails'] = cli_util.parse_json_parameter("authorization_details", authorization_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.create_source(
        create_source_details=_details,
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


@source_group.command(name=cli_util.override('application_migration.create_source_import_source_details.command_name', 'create-source-import-source-details'), help=u"""Creates a source in the specified compartment. In Application Migration, a source refers to the environment from which the application is being migrated. For more information, see [Manage Sources].

All Oracle Cloud Infrastructure resources, including sources, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console.

After you send your request, a source is created in the specified compartment. The new source's lifecycle state will temporarily be <code>CREATING</code>. Application Migration connects to the source environment with the authentication credentials that you have provided. If the connection is established, the status of the source changes to <code>ACTIVE</code> and Application Migration fetches the list of applications that are available for migration in the source environment.

To track the progress of the operation, you can monitor the status of the Create Source work request by using the <code>[GetWorkRequest]</code> REST API operation on the work request or by viewing the status of the work request in the console.

Ensure that the state of the source has changed to <code>ACTIVE</code>, before you retrieve the list of applications from the source environment using the <code>[ListSourceApplications]</code> REST API call. \n[Command Reference](createSource)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment that contains the source.""")
@cli_util.option('--source-details-manifest', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--source-details-namespace', required=True, help=u"""the object storage namespace where the bucket and uploaded object resides""")
@cli_util.option('--source-details-bucket', required=True, help=u"""the bucket wherein the export archive exists in object storage""")
@cli_util.option('--source-details-object-name', required=True, help=u"""the name of the archive as it exists in object storage""")
@cli_util.option('--display-name', help=u"""Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--description', help=u"""Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--authorization-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}, 'source-details-manifest': {'module': 'application_migration', 'class': 'ImportManifest'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}, 'source-details-manifest': {'module': 'application_migration', 'class': 'ImportManifest'}}, output_type={'module': 'application_migration', 'class': 'Source'})
@cli_util.wrap_exceptions
def create_source_import_source_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, source_details_manifest, source_details_namespace, source_details_bucket, source_details_object_name, display_name, description, authorization_details, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['sourceDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['sourceDetails']['manifest'] = cli_util.parse_json_parameter("source_details_manifest", source_details_manifest)
    _details['sourceDetails']['namespace'] = source_details_namespace
    _details['sourceDetails']['bucket'] = source_details_bucket
    _details['sourceDetails']['objectName'] = source_details_object_name

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if authorization_details is not None:
        _details['authorizationDetails'] = cli_util.parse_json_parameter("authorization_details", authorization_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['sourceDetails']['type'] = 'IMPORT'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.create_source(
        create_source_details=_details,
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


@source_group.command(name=cli_util.override('application_migration.create_source_occ_source_details.command_name', 'create-source-occ-source-details'), help=u"""Creates a source in the specified compartment. In Application Migration, a source refers to the environment from which the application is being migrated. For more information, see [Manage Sources].

All Oracle Cloud Infrastructure resources, including sources, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console.

After you send your request, a source is created in the specified compartment. The new source's lifecycle state will temporarily be <code>CREATING</code>. Application Migration connects to the source environment with the authentication credentials that you have provided. If the connection is established, the status of the source changes to <code>ACTIVE</code> and Application Migration fetches the list of applications that are available for migration in the source environment.

To track the progress of the operation, you can monitor the status of the Create Source work request by using the <code>[GetWorkRequest]</code> REST API operation on the work request or by viewing the status of the work request in the console.

Ensure that the state of the source has changed to <code>ACTIVE</code>, before you retrieve the list of applications from the source environment using the <code>[ListSourceApplications]</code> REST API call. \n[Command Reference](createSource)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment that contains the source.""")
@cli_util.option('--source-details-compute-account', required=True, help=u"""If you are using an Oracle Cloud@Customer account with Identity Cloud Service (IDCS), enter the service instance ID. For example, if Compute-567890123 is the account name of your Oracle Cloud@Customer Compute service entitlement, then enter 567890123.""")
@cli_util.option('--display-name', help=u"""Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--description', help=u"""Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--authorization-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'application_migration', 'class': 'Source'})
@cli_util.wrap_exceptions
def create_source_occ_source_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, source_details_compute_account, display_name, description, authorization_details, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['sourceDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['sourceDetails']['computeAccount'] = source_details_compute_account

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if authorization_details is not None:
        _details['authorizationDetails'] = cli_util.parse_json_parameter("authorization_details", authorization_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['sourceDetails']['type'] = 'OCC'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.create_source(
        create_source_details=_details,
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


@source_group.command(name=cli_util.override('application_migration.create_source_internal_source_details.command_name', 'create-source-internal-source-details'), help=u"""Creates a source in the specified compartment. In Application Migration, a source refers to the environment from which the application is being migrated. For more information, see [Manage Sources].

All Oracle Cloud Infrastructure resources, including sources, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console.

After you send your request, a source is created in the specified compartment. The new source's lifecycle state will temporarily be <code>CREATING</code>. Application Migration connects to the source environment with the authentication credentials that you have provided. If the connection is established, the status of the source changes to <code>ACTIVE</code> and Application Migration fetches the list of applications that are available for migration in the source environment.

To track the progress of the operation, you can monitor the status of the Create Source work request by using the <code>[GetWorkRequest]</code> REST API operation on the work request or by viewing the status of the work request in the console.

Ensure that the state of the source has changed to <code>ACTIVE</code>, before you retrieve the list of applications from the source environment using the <code>[ListSourceApplications]</code> REST API call. \n[Command Reference](createSource)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment that contains the source.""")
@cli_util.option('--source-details-account-name', required=True, help=u"""The identity domain ID of your traditional Oracle Cloud Infrastructure - Classic account.""")
@cli_util.option('--display-name', help=u"""Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--description', help=u"""Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--authorization-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'application_migration', 'class': 'Source'})
@cli_util.wrap_exceptions
def create_source_internal_source_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, source_details_account_name, display_name, description, authorization_details, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['sourceDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['sourceDetails']['accountName'] = source_details_account_name

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if authorization_details is not None:
        _details['authorizationDetails'] = cli_util.parse_json_parameter("authorization_details", authorization_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['sourceDetails']['type'] = 'INTERNAL_COMPUTE'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.create_source(
        create_source_details=_details,
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


@source_group.command(name=cli_util.override('application_migration.create_source_ocic_source_details.command_name', 'create-source-ocic-source-details'), help=u"""Creates a source in the specified compartment. In Application Migration, a source refers to the environment from which the application is being migrated. For more information, see [Manage Sources].

All Oracle Cloud Infrastructure resources, including sources, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console.

After you send your request, a source is created in the specified compartment. The new source's lifecycle state will temporarily be <code>CREATING</code>. Application Migration connects to the source environment with the authentication credentials that you have provided. If the connection is established, the status of the source changes to <code>ACTIVE</code> and Application Migration fetches the list of applications that are available for migration in the source environment.

To track the progress of the operation, you can monitor the status of the Create Source work request by using the <code>[GetWorkRequest]</code> REST API operation on the work request or by viewing the status of the work request in the console.

Ensure that the state of the source has changed to <code>ACTIVE</code>, before you retrieve the list of applications from the source environment using the <code>[ListSourceApplications]</code> REST API call. \n[Command Reference](createSource)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment that contains the source.""")
@cli_util.option('--source-details-region', required=True, help=u"""The Oracle Cloud Infrastructure - Classic region from which you want to migrate your applications. For example, uscom-east-1 or uscom-central-1.""")
@cli_util.option('--source-details-compute-account', required=True, help=u"""If you are using an Oracle Cloud Infrastructure - Classic account with Identity Cloud Service (IDCS), enter the service instance ID. For example, if Compute-567890123 is the account name of your Oracle Cloud Infrastructure Classic Compute service entitlement, then enter 567890123.

If you are using a traditional Oracle Cloud Infrastructure - Classic account, enter your identity domain ID.""")
@cli_util.option('--display-name', help=u"""Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--description', help=u"""Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--authorization-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'application_migration', 'class': 'Source'})
@cli_util.wrap_exceptions
def create_source_ocic_source_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, source_details_region, source_details_compute_account, display_name, description, authorization_details, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['sourceDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['sourceDetails']['region'] = source_details_region
    _details['sourceDetails']['computeAccount'] = source_details_compute_account

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if authorization_details is not None:
        _details['authorizationDetails'] = cli_util.parse_json_parameter("authorization_details", authorization_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['sourceDetails']['type'] = 'OCIC'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.create_source(
        create_source_details=_details,
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


@source_group.command(name=cli_util.override('application_migration.create_source_occ_authorization_details.command_name', 'create-source-occ-authorization-details'), help=u"""Creates a source in the specified compartment. In Application Migration, a source refers to the environment from which the application is being migrated. For more information, see [Manage Sources].

All Oracle Cloud Infrastructure resources, including sources, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console.

After you send your request, a source is created in the specified compartment. The new source's lifecycle state will temporarily be <code>CREATING</code>. Application Migration connects to the source environment with the authentication credentials that you have provided. If the connection is established, the status of the source changes to <code>ACTIVE</code> and Application Migration fetches the list of applications that are available for migration in the source environment.

To track the progress of the operation, you can monitor the status of the Create Source work request by using the <code>[GetWorkRequest]</code> REST API operation on the work request or by viewing the status of the work request in the console.

Ensure that the state of the source has changed to <code>ACTIVE</code>, before you retrieve the list of applications from the source environment using the <code>[ListSourceApplications]</code> REST API call. \n[Command Reference](createSource)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment that contains the source.""")
@cli_util.option('--source-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--authorization-details-username', required=True, help=u"""User with Compute Operations role in Oracle Cloud@Customer.""")
@cli_util.option('--authorization-details-password', required=True, help=u"""Password for this user.""")
@cli_util.option('--display-name', help=u"""Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--description', help=u"""Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'application_migration', 'class': 'Source'})
@cli_util.wrap_exceptions
def create_source_occ_authorization_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, source_details, authorization_details_username, authorization_details_password, display_name, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['authorizationDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)
    _details['authorizationDetails']['username'] = authorization_details_username
    _details['authorizationDetails']['password'] = authorization_details_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['authorizationDetails']['type'] = 'OCC'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.create_source(
        create_source_details=_details,
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


@source_group.command(name=cli_util.override('application_migration.create_source_internal_authorization_details.command_name', 'create-source-internal-authorization-details'), help=u"""Creates a source in the specified compartment. In Application Migration, a source refers to the environment from which the application is being migrated. For more information, see [Manage Sources].

All Oracle Cloud Infrastructure resources, including sources, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console.

After you send your request, a source is created in the specified compartment. The new source's lifecycle state will temporarily be <code>CREATING</code>. Application Migration connects to the source environment with the authentication credentials that you have provided. If the connection is established, the status of the source changes to <code>ACTIVE</code> and Application Migration fetches the list of applications that are available for migration in the source environment.

To track the progress of the operation, you can monitor the status of the Create Source work request by using the <code>[GetWorkRequest]</code> REST API operation on the work request or by viewing the status of the work request in the console.

Ensure that the state of the source has changed to <code>ACTIVE</code>, before you retrieve the list of applications from the source environment using the <code>[ListSourceApplications]</code> REST API call. \n[Command Reference](createSource)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment that contains the source.""")
@cli_util.option('--source-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--authorization-details-username', required=True, help=u"""User with Compute Operations role in Oracle Cloud Infrastructure - Classic.""")
@cli_util.option('--authorization-details-password', required=True, help=u"""Password for this user.""")
@cli_util.option('--display-name', help=u"""Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--description', help=u"""Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'application_migration', 'class': 'Source'})
@cli_util.wrap_exceptions
def create_source_internal_authorization_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, source_details, authorization_details_username, authorization_details_password, display_name, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['authorizationDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)
    _details['authorizationDetails']['username'] = authorization_details_username
    _details['authorizationDetails']['password'] = authorization_details_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['authorizationDetails']['type'] = 'INTERNAL_COMPUTE'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.create_source(
        create_source_details=_details,
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


@source_group.command(name=cli_util.override('application_migration.create_source_ocic_authorization_token_details.command_name', 'create-source-ocic-authorization-token-details'), help=u"""Creates a source in the specified compartment. In Application Migration, a source refers to the environment from which the application is being migrated. For more information, see [Manage Sources].

All Oracle Cloud Infrastructure resources, including sources, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console.

After you send your request, a source is created in the specified compartment. The new source's lifecycle state will temporarily be <code>CREATING</code>. Application Migration connects to the source environment with the authentication credentials that you have provided. If the connection is established, the status of the source changes to <code>ACTIVE</code> and Application Migration fetches the list of applications that are available for migration in the source environment.

To track the progress of the operation, you can monitor the status of the Create Source work request by using the <code>[GetWorkRequest]</code> REST API operation on the work request or by viewing the status of the work request in the console.

Ensure that the state of the source has changed to <code>ACTIVE</code>, before you retrieve the list of applications from the source environment using the <code>[ListSourceApplications]</code> REST API call. \n[Command Reference](createSource)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment that contains the source.""")
@cli_util.option('--source-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--authorization-details-client-app-url', required=True, help=u"""AuthClient app url resource that the accesstoken is for.""")
@cli_util.option('--authorization-details-access-token', required=True, help=u"""AccessToken to access the app endpoint.""")
@cli_util.option('--display-name', help=u"""Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--description', help=u"""Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'application_migration', 'class': 'Source'})
@cli_util.wrap_exceptions
def create_source_ocic_authorization_token_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, source_details, authorization_details_client_app_url, authorization_details_access_token, display_name, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['authorizationDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)
    _details['authorizationDetails']['clientAppUrl'] = authorization_details_client_app_url
    _details['authorizationDetails']['accessToken'] = authorization_details_access_token

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['authorizationDetails']['type'] = 'OCIC_IDCS'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.create_source(
        create_source_details=_details,
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


@source_group.command(name=cli_util.override('application_migration.create_source_ocic_authorization_details.command_name', 'create-source-ocic-authorization-details'), help=u"""Creates a source in the specified compartment. In Application Migration, a source refers to the environment from which the application is being migrated. For more information, see [Manage Sources].

All Oracle Cloud Infrastructure resources, including sources, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console.

After you send your request, a source is created in the specified compartment. The new source's lifecycle state will temporarily be <code>CREATING</code>. Application Migration connects to the source environment with the authentication credentials that you have provided. If the connection is established, the status of the source changes to <code>ACTIVE</code> and Application Migration fetches the list of applications that are available for migration in the source environment.

To track the progress of the operation, you can monitor the status of the Create Source work request by using the <code>[GetWorkRequest]</code> REST API operation on the work request or by viewing the status of the work request in the console.

Ensure that the state of the source has changed to <code>ACTIVE</code>, before you retrieve the list of applications from the source environment using the <code>[ListSourceApplications]</code> REST API call. \n[Command Reference](createSource)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment that contains the source.""")
@cli_util.option('--source-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--authorization-details-username', required=True, help=u"""User with Compute Operations role in Oracle Cloud Infrastructure - Classic.""")
@cli_util.option('--authorization-details-password', required=True, help=u"""Password for this user.""")
@cli_util.option('--display-name', help=u"""Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--description', help=u"""Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'application_migration', 'class': 'Source'})
@cli_util.wrap_exceptions
def create_source_ocic_authorization_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, source_details, authorization_details_username, authorization_details_password, display_name, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['authorizationDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)
    _details['authorizationDetails']['username'] = authorization_details_username
    _details['authorizationDetails']['password'] = authorization_details_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['authorizationDetails']['type'] = 'OCIC'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.create_source(
        create_source_details=_details,
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


@migration_group.command(name=cli_util.override('application_migration.delete_migration.command_name', 'delete'), help=u"""Deletes the specified migration.

If you have migrated the application or for any other reason if you no longer require a migration, then you can delete the relevant migration. You can delete a migration, irrespective of its state. If any work request is being processed for the migration that you want to delete, then the associated work requests are cancelled and then the migration is deleted. \n[Command Reference](deleteMigration)""")
@cli_util.option('--migration-id', required=True, help=u"""The [OCID] of the migration.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
    client = cli_util.build_client('application_migration', 'application_migration', ctx)
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


@source_group.command(name=cli_util.override('application_migration.delete_source.command_name', 'delete'), help=u"""Deletes the specified source.

Before deleting a source, you must delete all the migrations associated with the source. If you have migrated all the required applications in a source or for any other reason you no longer require a source, then you can delete the relevant source. \n[Command Reference](deleteSource)""")
@cli_util.option('--source-id', required=True, help=u"""The [OCID] of the source.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_source(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, source_id, if_match):

    if isinstance(source_id, six.string_types) and len(source_id.strip()) == 0:
        raise click.UsageError('Parameter --source-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.delete_source(
        source_id=source_id,
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


@migration_group.command(name=cli_util.override('application_migration.get_migration.command_name', 'get'), help=u"""Retrieves details of the specified migration. \n[Command Reference](getMigration)""")
@cli_util.option('--migration-id', required=True, help=u"""The [OCID] of the migration.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'application_migration', 'class': 'Migration'})
@cli_util.wrap_exceptions
def get_migration(ctx, from_json, migration_id):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.get_migration(
        migration_id=migration_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@source_group.command(name=cli_util.override('application_migration.get_source.command_name', 'get'), help=u"""Retrieves details of the specified source. Specify the OCID of the source for which you want to retrieve details. \n[Command Reference](getSource)""")
@cli_util.option('--source-id', required=True, help=u"""The [OCID] of the source.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'application_migration', 'class': 'Source'})
@cli_util.wrap_exceptions
def get_source(ctx, from_json, source_id):

    if isinstance(source_id, six.string_types) and len(source_id.strip()) == 0:
        raise click.UsageError('Parameter --source-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.get_source(
        source_id=source_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('application_migration.get_work_request.command_name', 'get'), help=u"""Gets the details of the specified work request. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the work request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'application_migration', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@migration_group.command(name=cli_util.override('application_migration.list_migrations.command_name', 'list'), help=u"""Retrieves details of all the migrations that are available in the specified compartment. \n[Command Reference](listMigrations)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of a compartment. Retrieves details of objects in the specified compartment.""")
@cli_util.option('--id', help=u"""The [OCID] on which to query for a migration.""")
@cli_util.option('--limit', type=click.INT, help=u"""The number of items returned in a paginated `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order, either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""Specifies the field on which to sort. By default, `TIMECREATED` is ordered descending. By default, `DISPLAYNAME` is ordered ascending. Note that you can sort only on one field.""")
@cli_util.option('--display-name', help=u"""Display name on which to query.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "SUCCEEDED", "DELETING", "DELETED"]), help=u"""This field is not supported. Do not use.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'application_migration', 'class': 'list[MigrationSummary]'})
@cli_util.wrap_exceptions
def list_migrations(ctx, from_json, all_pages, page_size, compartment_id, id, limit, page, sort_order, sort_by, display_name, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('application_migration', 'application_migration', ctx)
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


@source_application_group.command(name=cli_util.override('application_migration.list_source_applications.command_name', 'list'), help=u"""Retrieves details of all the applications associated with the specified source. This list is generated dynamically by interrogating the source and the list changes as applications are started or stopped in the source environment. \n[Command Reference](listSourceApplications)""")
@cli_util.option('--source-id', required=True, help=u"""The [OCID] of the source.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of a compartment. Retrieves details of objects in the specified compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""The number of items returned in a paginated `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order, either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""Specifies the field on which to sort. By default, `TIMECREATED` is ordered descending. By default, `DISPLAYNAME` is ordered ascending. Note that you can sort only on one field.""")
@cli_util.option('--display-name', help=u"""Resource name on which to query.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'application_migration', 'class': 'list[SourceApplicationSummary]'})
@cli_util.wrap_exceptions
def list_source_applications(ctx, from_json, all_pages, page_size, source_id, compartment_id, limit, page, sort_order, sort_by, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(source_id, six.string_types) and len(source_id.strip()) == 0:
        raise click.UsageError('Parameter --source-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if display_name is not None:
        kwargs['display_name'] = display_name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_source_applications,
            source_id=source_id,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_source_applications,
            limit,
            page_size,
            source_id=source_id,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_source_applications(
            source_id=source_id,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@source_group.command(name=cli_util.override('application_migration.list_sources.command_name', 'list'), help=u"""Retrieves details of all the sources that are available in the specified compartment and match the specified query criteria. If you don't specify any query criteria, then details of all the sources are displayed. To filter the retrieved results, you can pass one or more of the following query parameters, by appending them to the URI as shown in the following example. \n[Command Reference](listSources)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of a compartment. Retrieves details of objects in the specified compartment.""")
@cli_util.option('--id', help=u"""The [OCID] on which to query for a source.""")
@cli_util.option('--limit', type=click.INT, help=u"""The number of items returned in a paginated `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order, either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""Specifies the field on which to sort. By default, `TIMECREATED` is ordered descending. By default, `DISPLAYNAME` is ordered ascending. Note that you can sort only on one field.""")
@cli_util.option('--display-name', help=u"""Display name on which to query.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "DELETING", "UPDATING", "ACTIVE", "INACTIVE", "DELETED"]), help=u"""Retrieves details of sources in the specified lifecycle state.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'application_migration', 'class': 'list[SourceSummary]'})
@cli_util.wrap_exceptions
def list_sources(ctx, from_json, all_pages, page_size, compartment_id, id, limit, page, sort_order, sort_by, display_name, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_sources,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_sources,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_sources(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('application_migration.list_work_request_errors.command_name', 'list'), help=u"""Retrieves details of the errors encountered while executing an operation that is tracked by the specified work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the work request.""")
@cli_util.option('--limit', type=click.INT, help=u"""The number of items returned in a paginated `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order, either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'application_migration', 'class': 'list[WorkRequestError]'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, limit, page, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('application_migration', 'application_migration', ctx)
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


@work_request_log_entry_group.command(name=cli_util.override('application_migration.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Retrieves logs for the specified work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the work request.""")
@cli_util.option('--limit', type=click.INT, help=u"""The number of items returned in a paginated `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order, either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'application_migration', 'class': 'list[WorkRequestLogEntry]'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, limit, page, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('application_migration', 'application_migration', ctx)
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


@work_request_group.command(name=cli_util.override('application_migration.list_work_requests.command_name', 'list'), help=u"""Retrieves details of all the work requests and match the specified query criteria. To filter the retrieved results, you can pass one or more of the following query parameters, by appending them to the URI as shown in the following example. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of a compartment. Retrieves details of objects in the specified compartment.""")
@cli_util.option('--resource-id', help=u"""The [OCID] for a resource. Retrieves details of the specified resource.""")
@cli_util.option('--limit', type=click.INT, help=u"""The number of items returned in a paginated `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'application_migration', 'class': 'list[WorkRequestSummary]'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, resource_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if resource_id is not None:
        kwargs['resource_id'] = resource_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('application_migration', 'application_migration', ctx)
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


@migration_group.command(name=cli_util.override('application_migration.migrate_application.command_name', 'migrate-application'), help=u"""Starts migrating the specified application to Oracle Cloud Infrastructure.

Before sending this request, ensure that you have provided configuration details to update the migration and the state of the migration is <code>READY</code>.

After you send this request, the migration's state will temporarily be <code>MIGRATING</code>.

To track the progress of the operation, you can monitor the status of the Migrate Application work request by using the <code>[GetWorkRequest]</code> REST API operation on the work request or by viewing the status of the work request in the console. When this work request is processed successfully, Application Migration creates the required resources in the target environment and the state of the migration changes to <code>MIGRATION_SUCCEEDED</code>. \n[Command Reference](migrateApplication)""")
@cli_util.option('--migration-id', required=True, help=u"""The [OCID] of the migration.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def migrate_application(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, migration_id, if_match):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.migrate_application(
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


@migration_group.command(name=cli_util.override('application_migration.update_migration.command_name', 'update'), help=u"""Updates the configuration details for the specified migration.

When you create a migration, Application Migration sets the template for the <code>serviceConfig</code> and <code>applicationConfig</code> attributes of the migration. When you update the migration, you must provide values for these fields to specify configuration information for the application in the target environment.



Before updating the migration, complete the following tasks: <ol> <li>Identify the migration that you want to update and ensure that the migration is in the <code>MISSING_CONFIG_VALUES</code> state.</li> <li>Get details of the migration using the <code>GetMigration</code> command. This returns the  template for the <code>serviceConfig</code> and <code>applicationConfig</code> attributes of the migration.</li> <li>You must fill out the required details for the <code>serviceConfig</code> and <code>applicationConfig</code> attributes. The <code>isRequired</code> attribute of a configuration property indicates whether it is mandatory to provide a value.</li> <li>You can provide values for the optional configuration properties or you can delete the optional properties for which you do not provide values. Note that you cannot add any property that is not present in the template.</li> </ol>

To update the migration, pass the configuration values in the request body. The information that you must provide depends on the type of application that you are migrating. For reference information about configuration fields, see [Provide Configuration Information].

To track the progress of the operation, you can monitor the status of the Update Migration work request by using the <code>[GetWorkRequest]</code> REST API operation on the work request or by viewing the status of the work request in the console.

When the migration has been updated, the state of the migration changes to <code>READY</code>. After updating the migration, you can start the migration whenever you are ready. \n[Command Reference](updateMigration)""")
@cli_util.option('--migration-id', required=True, help=u"""The [OCID] of the migration.""")
@cli_util.option('--display-name', help=u"""User-friendly name of the migration.""")
@cli_util.option('--description', help=u"""Description of the migration.""")
@cli_util.option('--discovery-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-selective-migration', type=click.BOOL, help=u"""If set to `true`, Application Migration migrates the application resources selectively depending on the source.""")
@cli_util.option('--service-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'discovery-details': {'module': 'application_migration', 'class': 'DiscoveryDetails'}, 'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'discovery-details': {'module': 'application_migration', 'class': 'DiscoveryDetails'}, 'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_migration(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, migration_id, display_name, description, discovery_details, is_selective_migration, service_config, application_config, freeform_tags, defined_tags, if_match):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')
    if not force:
        if discovery_details or service_config or application_config or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to discovery-details and service-config and application-config and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
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

    if discovery_details is not None:
        _details['discoveryDetails'] = cli_util.parse_json_parameter("discovery_details", discovery_details)

    if is_selective_migration is not None:
        _details['isSelectiveMigration'] = is_selective_migration

    if service_config is not None:
        _details['serviceConfig'] = cli_util.parse_json_parameter("service_config", service_config)

    if application_config is not None:
        _details['applicationConfig'] = cli_util.parse_json_parameter("application_config", application_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
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


@migration_group.command(name=cli_util.override('application_migration.update_migration_oic_discovery_details.command_name', 'update-migration-oic-discovery-details'), help=u"""Updates the configuration details for the specified migration.

When you create a migration, Application Migration sets the template for the <code>serviceConfig</code> and <code>applicationConfig</code> attributes of the migration. When you update the migration, you must provide values for these fields to specify configuration information for the application in the target environment.



Before updating the migration, complete the following tasks: <ol> <li>Identify the migration that you want to update and ensure that the migration is in the <code>MISSING_CONFIG_VALUES</code> state.</li> <li>Get details of the migration using the <code>GetMigration</code> command. This returns the  template for the <code>serviceConfig</code> and <code>applicationConfig</code> attributes of the migration.</li> <li>You must fill out the required details for the <code>serviceConfig</code> and <code>applicationConfig</code> attributes. The <code>isRequired</code> attribute of a configuration property indicates whether it is mandatory to provide a value.</li> <li>You can provide values for the optional configuration properties or you can delete the optional properties for which you do not provide values. Note that you cannot add any property that is not present in the template.</li> </ol>

To update the migration, pass the configuration values in the request body. The information that you must provide depends on the type of application that you are migrating. For reference information about configuration fields, see [Provide Configuration Information].

To track the progress of the operation, you can monitor the status of the Update Migration work request by using the <code>[GetWorkRequest]</code> REST API operation on the work request or by viewing the status of the work request in the console.

When the migration has been updated, the state of the migration changes to <code>READY</code>. After updating the migration, you can start the migration whenever you are ready. \n[Command Reference](updateMigration)""")
@cli_util.option('--migration-id', required=True, help=u"""The [OCID] of the migration.""")
@cli_util.option('--discovery-details-service-instance-user', required=True, help=u"""Application administrator username to access the Oracle Integration Classic instance in the source environment.""")
@cli_util.option('--discovery-details-service-instance-password', required=True, help=u"""Password for this user.""")
@cli_util.option('--display-name', help=u"""User-friendly name of the migration.""")
@cli_util.option('--description', help=u"""Description of the migration.""")
@cli_util.option('--is-selective-migration', type=click.BOOL, help=u"""If set to `true`, Application Migration migrates the application resources selectively depending on the source.""")
@cli_util.option('--service-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_migration_oic_discovery_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, migration_id, discovery_details_service_instance_user, discovery_details_service_instance_password, display_name, description, is_selective_migration, service_config, application_config, freeform_tags, defined_tags, if_match):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')
    if not force:
        if service_config or application_config or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to service-config and application-config and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['discoveryDetails'] = {}
    _details['discoveryDetails']['serviceInstanceUser'] = discovery_details_service_instance_user
    _details['discoveryDetails']['serviceInstancePassword'] = discovery_details_service_instance_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if is_selective_migration is not None:
        _details['isSelectiveMigration'] = is_selective_migration

    if service_config is not None:
        _details['serviceConfig'] = cli_util.parse_json_parameter("service_config", service_config)

    if application_config is not None:
        _details['applicationConfig'] = cli_util.parse_json_parameter("application_config", application_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['discoveryDetails']['type'] = 'OIC'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
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


@migration_group.command(name=cli_util.override('application_migration.update_migration_pcs_discovery_details.command_name', 'update-migration-pcs-discovery-details'), help=u"""Updates the configuration details for the specified migration.

When you create a migration, Application Migration sets the template for the <code>serviceConfig</code> and <code>applicationConfig</code> attributes of the migration. When you update the migration, you must provide values for these fields to specify configuration information for the application in the target environment.



Before updating the migration, complete the following tasks: <ol> <li>Identify the migration that you want to update and ensure that the migration is in the <code>MISSING_CONFIG_VALUES</code> state.</li> <li>Get details of the migration using the <code>GetMigration</code> command. This returns the  template for the <code>serviceConfig</code> and <code>applicationConfig</code> attributes of the migration.</li> <li>You must fill out the required details for the <code>serviceConfig</code> and <code>applicationConfig</code> attributes. The <code>isRequired</code> attribute of a configuration property indicates whether it is mandatory to provide a value.</li> <li>You can provide values for the optional configuration properties or you can delete the optional properties for which you do not provide values. Note that you cannot add any property that is not present in the template.</li> </ol>

To update the migration, pass the configuration values in the request body. The information that you must provide depends on the type of application that you are migrating. For reference information about configuration fields, see [Provide Configuration Information].

To track the progress of the operation, you can monitor the status of the Update Migration work request by using the <code>[GetWorkRequest]</code> REST API operation on the work request or by viewing the status of the work request in the console.

When the migration has been updated, the state of the migration changes to <code>READY</code>. After updating the migration, you can start the migration whenever you are ready. \n[Command Reference](updateMigration)""")
@cli_util.option('--migration-id', required=True, help=u"""The [OCID] of the migration.""")
@cli_util.option('--discovery-details-service-instance-user', required=True, help=u"""Application administrator username to access the Oracle Process Cloud Service application in the source environment.""")
@cli_util.option('--discovery-details-service-instance-password', required=True, help=u"""Password for this user.""")
@cli_util.option('--display-name', help=u"""User-friendly name of the migration.""")
@cli_util.option('--description', help=u"""Description of the migration.""")
@cli_util.option('--is-selective-migration', type=click.BOOL, help=u"""If set to `true`, Application Migration migrates the application resources selectively depending on the source.""")
@cli_util.option('--service-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_migration_pcs_discovery_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, migration_id, discovery_details_service_instance_user, discovery_details_service_instance_password, display_name, description, is_selective_migration, service_config, application_config, freeform_tags, defined_tags, if_match):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')
    if not force:
        if service_config or application_config or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to service-config and application-config and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['discoveryDetails'] = {}
    _details['discoveryDetails']['serviceInstanceUser'] = discovery_details_service_instance_user
    _details['discoveryDetails']['serviceInstancePassword'] = discovery_details_service_instance_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if is_selective_migration is not None:
        _details['isSelectiveMigration'] = is_selective_migration

    if service_config is not None:
        _details['serviceConfig'] = cli_util.parse_json_parameter("service_config", service_config)

    if application_config is not None:
        _details['applicationConfig'] = cli_util.parse_json_parameter("application_config", application_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['discoveryDetails']['type'] = 'PCS'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
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


@migration_group.command(name=cli_util.override('application_migration.update_migration_ics_discovery_details.command_name', 'update-migration-ics-discovery-details'), help=u"""Updates the configuration details for the specified migration.

When you create a migration, Application Migration sets the template for the <code>serviceConfig</code> and <code>applicationConfig</code> attributes of the migration. When you update the migration, you must provide values for these fields to specify configuration information for the application in the target environment.



Before updating the migration, complete the following tasks: <ol> <li>Identify the migration that you want to update and ensure that the migration is in the <code>MISSING_CONFIG_VALUES</code> state.</li> <li>Get details of the migration using the <code>GetMigration</code> command. This returns the  template for the <code>serviceConfig</code> and <code>applicationConfig</code> attributes of the migration.</li> <li>You must fill out the required details for the <code>serviceConfig</code> and <code>applicationConfig</code> attributes. The <code>isRequired</code> attribute of a configuration property indicates whether it is mandatory to provide a value.</li> <li>You can provide values for the optional configuration properties or you can delete the optional properties for which you do not provide values. Note that you cannot add any property that is not present in the template.</li> </ol>

To update the migration, pass the configuration values in the request body. The information that you must provide depends on the type of application that you are migrating. For reference information about configuration fields, see [Provide Configuration Information].

To track the progress of the operation, you can monitor the status of the Update Migration work request by using the <code>[GetWorkRequest]</code> REST API operation on the work request or by viewing the status of the work request in the console.

When the migration has been updated, the state of the migration changes to <code>READY</code>. After updating the migration, you can start the migration whenever you are ready. \n[Command Reference](updateMigration)""")
@cli_util.option('--migration-id', required=True, help=u"""The [OCID] of the migration.""")
@cli_util.option('--discovery-details-service-instance-user', required=True, help=u"""Application administrator username to access the Oracle Integration Cloud Service application in the source environment.""")
@cli_util.option('--discovery-details-service-instance-password', required=True, help=u"""Password for this user.""")
@cli_util.option('--display-name', help=u"""User-friendly name of the migration.""")
@cli_util.option('--description', help=u"""Description of the migration.""")
@cli_util.option('--is-selective-migration', type=click.BOOL, help=u"""If set to `true`, Application Migration migrates the application resources selectively depending on the source.""")
@cli_util.option('--service-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_migration_ics_discovery_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, migration_id, discovery_details_service_instance_user, discovery_details_service_instance_password, display_name, description, is_selective_migration, service_config, application_config, freeform_tags, defined_tags, if_match):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')
    if not force:
        if service_config or application_config or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to service-config and application-config and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['discoveryDetails'] = {}
    _details['discoveryDetails']['serviceInstanceUser'] = discovery_details_service_instance_user
    _details['discoveryDetails']['serviceInstancePassword'] = discovery_details_service_instance_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if is_selective_migration is not None:
        _details['isSelectiveMigration'] = is_selective_migration

    if service_config is not None:
        _details['serviceConfig'] = cli_util.parse_json_parameter("service_config", service_config)

    if application_config is not None:
        _details['applicationConfig'] = cli_util.parse_json_parameter("application_config", application_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['discoveryDetails']['type'] = 'ICS'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
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


@migration_group.command(name=cli_util.override('application_migration.update_migration_oac_discovery_details.command_name', 'update-migration-oac-discovery-details'), help=u"""Updates the configuration details for the specified migration.

When you create a migration, Application Migration sets the template for the <code>serviceConfig</code> and <code>applicationConfig</code> attributes of the migration. When you update the migration, you must provide values for these fields to specify configuration information for the application in the target environment.



Before updating the migration, complete the following tasks: <ol> <li>Identify the migration that you want to update and ensure that the migration is in the <code>MISSING_CONFIG_VALUES</code> state.</li> <li>Get details of the migration using the <code>GetMigration</code> command. This returns the  template for the <code>serviceConfig</code> and <code>applicationConfig</code> attributes of the migration.</li> <li>You must fill out the required details for the <code>serviceConfig</code> and <code>applicationConfig</code> attributes. The <code>isRequired</code> attribute of a configuration property indicates whether it is mandatory to provide a value.</li> <li>You can provide values for the optional configuration properties or you can delete the optional properties for which you do not provide values. Note that you cannot add any property that is not present in the template.</li> </ol>

To update the migration, pass the configuration values in the request body. The information that you must provide depends on the type of application that you are migrating. For reference information about configuration fields, see [Provide Configuration Information].

To track the progress of the operation, you can monitor the status of the Update Migration work request by using the <code>[GetWorkRequest]</code> REST API operation on the work request or by viewing the status of the work request in the console.

When the migration has been updated, the state of the migration changes to <code>READY</code>. After updating the migration, you can start the migration whenever you are ready. \n[Command Reference](updateMigration)""")
@cli_util.option('--migration-id', required=True, help=u"""The [OCID] of the migration.""")
@cli_util.option('--discovery-details-service-instance-user', required=True, help=u"""This field is currently not supported. You must enter a value, such as <code>unused</code>. However, the value that you enter is ignored.""")
@cli_util.option('--discovery-details-service-instance-password', required=True, help=u"""This field is currently not supported. You must enter a value, such as <code>unused</code>. However, the value that you enter is ignored.""")
@cli_util.option('--display-name', help=u"""User-friendly name of the migration.""")
@cli_util.option('--description', help=u"""Description of the migration.""")
@cli_util.option('--is-selective-migration', type=click.BOOL, help=u"""If set to `true`, Application Migration migrates the application resources selectively depending on the source.""")
@cli_util.option('--service-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_migration_oac_discovery_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, migration_id, discovery_details_service_instance_user, discovery_details_service_instance_password, display_name, description, is_selective_migration, service_config, application_config, freeform_tags, defined_tags, if_match):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')
    if not force:
        if service_config or application_config or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to service-config and application-config and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['discoveryDetails'] = {}
    _details['discoveryDetails']['serviceInstanceUser'] = discovery_details_service_instance_user
    _details['discoveryDetails']['serviceInstancePassword'] = discovery_details_service_instance_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if is_selective_migration is not None:
        _details['isSelectiveMigration'] = is_selective_migration

    if service_config is not None:
        _details['serviceConfig'] = cli_util.parse_json_parameter("service_config", service_config)

    if application_config is not None:
        _details['applicationConfig'] = cli_util.parse_json_parameter("application_config", application_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['discoveryDetails']['type'] = 'OAC'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
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


@migration_group.command(name=cli_util.override('application_migration.update_migration_jcs_discovery_details.command_name', 'update-migration-jcs-discovery-details'), help=u"""Updates the configuration details for the specified migration.

When you create a migration, Application Migration sets the template for the <code>serviceConfig</code> and <code>applicationConfig</code> attributes of the migration. When you update the migration, you must provide values for these fields to specify configuration information for the application in the target environment.



Before updating the migration, complete the following tasks: <ol> <li>Identify the migration that you want to update and ensure that the migration is in the <code>MISSING_CONFIG_VALUES</code> state.</li> <li>Get details of the migration using the <code>GetMigration</code> command. This returns the  template for the <code>serviceConfig</code> and <code>applicationConfig</code> attributes of the migration.</li> <li>You must fill out the required details for the <code>serviceConfig</code> and <code>applicationConfig</code> attributes. The <code>isRequired</code> attribute of a configuration property indicates whether it is mandatory to provide a value.</li> <li>You can provide values for the optional configuration properties or you can delete the optional properties for which you do not provide values. Note that you cannot add any property that is not present in the template.</li> </ol>

To update the migration, pass the configuration values in the request body. The information that you must provide depends on the type of application that you are migrating. For reference information about configuration fields, see [Provide Configuration Information].

To track the progress of the operation, you can monitor the status of the Update Migration work request by using the <code>[GetWorkRequest]</code> REST API operation on the work request or by viewing the status of the work request in the console.

When the migration has been updated, the state of the migration changes to <code>READY</code>. After updating the migration, you can start the migration whenever you are ready. \n[Command Reference](updateMigration)""")
@cli_util.option('--migration-id', required=True, help=u"""The [OCID] of the migration.""")
@cli_util.option('--discovery-details-weblogic-user', required=True, help=u"""WebLogic administrator username for the Oracle Java Cloud Service application in the source environment.""")
@cli_util.option('--discovery-details-weblogic-password', required=True, help=u"""The password of the WebLogic administrator for the Oracle Java Cloud Service application in the source environment.""")
@cli_util.option('--display-name', help=u"""User-friendly name of the migration.""")
@cli_util.option('--description', help=u"""Description of the migration.""")
@cli_util.option('--is-selective-migration', type=click.BOOL, help=u"""If set to `true`, Application Migration migrates the application resources selectively depending on the source.""")
@cli_util.option('--service-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_migration_jcs_discovery_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, migration_id, discovery_details_weblogic_user, discovery_details_weblogic_password, display_name, description, is_selective_migration, service_config, application_config, freeform_tags, defined_tags, if_match):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')
    if not force:
        if service_config or application_config or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to service-config and application-config and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['discoveryDetails'] = {}
    _details['discoveryDetails']['weblogicUser'] = discovery_details_weblogic_user
    _details['discoveryDetails']['weblogicPassword'] = discovery_details_weblogic_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if is_selective_migration is not None:
        _details['isSelectiveMigration'] = is_selective_migration

    if service_config is not None:
        _details['serviceConfig'] = cli_util.parse_json_parameter("service_config", service_config)

    if application_config is not None:
        _details['applicationConfig'] = cli_util.parse_json_parameter("application_config", application_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['discoveryDetails']['type'] = 'JCS'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
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


@migration_group.command(name=cli_util.override('application_migration.update_migration_soacs_discovery_details.command_name', 'update-migration-soacs-discovery-details'), help=u"""Updates the configuration details for the specified migration.

When you create a migration, Application Migration sets the template for the <code>serviceConfig</code> and <code>applicationConfig</code> attributes of the migration. When you update the migration, you must provide values for these fields to specify configuration information for the application in the target environment.



Before updating the migration, complete the following tasks: <ol> <li>Identify the migration that you want to update and ensure that the migration is in the <code>MISSING_CONFIG_VALUES</code> state.</li> <li>Get details of the migration using the <code>GetMigration</code> command. This returns the  template for the <code>serviceConfig</code> and <code>applicationConfig</code> attributes of the migration.</li> <li>You must fill out the required details for the <code>serviceConfig</code> and <code>applicationConfig</code> attributes. The <code>isRequired</code> attribute of a configuration property indicates whether it is mandatory to provide a value.</li> <li>You can provide values for the optional configuration properties or you can delete the optional properties for which you do not provide values. Note that you cannot add any property that is not present in the template.</li> </ol>

To update the migration, pass the configuration values in the request body. The information that you must provide depends on the type of application that you are migrating. For reference information about configuration fields, see [Provide Configuration Information].

To track the progress of the operation, you can monitor the status of the Update Migration work request by using the <code>[GetWorkRequest]</code> REST API operation on the work request or by viewing the status of the work request in the console.

When the migration has been updated, the state of the migration changes to <code>READY</code>. After updating the migration, you can start the migration whenever you are ready. \n[Command Reference](updateMigration)""")
@cli_util.option('--migration-id', required=True, help=u"""The [OCID] of the migration.""")
@cli_util.option('--discovery-details-weblogic-user', required=True, help=u"""WebLogic administrator username for the Oracle SOA Cloud Service application in the source environment.""")
@cli_util.option('--discovery-details-weblogic-password', required=True, help=u"""Password for this user.""")
@cli_util.option('--display-name', help=u"""User-friendly name of the migration.""")
@cli_util.option('--description', help=u"""Description of the migration.""")
@cli_util.option('--is-selective-migration', type=click.BOOL, help=u"""If set to `true`, Application Migration migrates the application resources selectively depending on the source.""")
@cli_util.option('--service-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_migration_soacs_discovery_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, migration_id, discovery_details_weblogic_user, discovery_details_weblogic_password, display_name, description, is_selective_migration, service_config, application_config, freeform_tags, defined_tags, if_match):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')
    if not force:
        if service_config or application_config or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to service-config and application-config and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['discoveryDetails'] = {}
    _details['discoveryDetails']['weblogicUser'] = discovery_details_weblogic_user
    _details['discoveryDetails']['weblogicPassword'] = discovery_details_weblogic_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if is_selective_migration is not None:
        _details['isSelectiveMigration'] = is_selective_migration

    if service_config is not None:
        _details['serviceConfig'] = cli_util.parse_json_parameter("service_config", service_config)

    if application_config is not None:
        _details['applicationConfig'] = cli_util.parse_json_parameter("application_config", application_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['discoveryDetails']['type'] = 'SOACS'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
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


@source_group.command(name=cli_util.override('application_migration.update_source.command_name', 'update'), help=u"""You can update the authorization details to access the source environment from which you want to migrate applications to Oracle Cloud Infrastructure. You can also update the description and tags of a source.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API. \n[Command Reference](updateSource)""")
@cli_util.option('--source-id', required=True, help=u"""The [OCID] of the source.""")
@cli_util.option('--display-name', help=u"""Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--description', help=u"""Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--source-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--authorization-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_source(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, source_id, display_name, description, source_details, authorization_details, freeform_tags, defined_tags, if_match):

    if isinstance(source_id, six.string_types) and len(source_id.strip()) == 0:
        raise click.UsageError('Parameter --source-id cannot be whitespace or empty string')
    if not force:
        if source_details or authorization_details or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to source-details and authorization-details and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
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

    if source_details is not None:
        _details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)

    if authorization_details is not None:
        _details['authorizationDetails'] = cli_util.parse_json_parameter("authorization_details", authorization_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.update_source(
        source_id=source_id,
        update_source_details=_details,
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


@source_group.command(name=cli_util.override('application_migration.update_source_import_source_details.command_name', 'update-source-import-source-details'), help=u"""You can update the authorization details to access the source environment from which you want to migrate applications to Oracle Cloud Infrastructure. You can also update the description and tags of a source.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API. \n[Command Reference](updateSource)""")
@cli_util.option('--source-id', required=True, help=u"""The [OCID] of the source.""")
@cli_util.option('--source-details-manifest', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--source-details-namespace', required=True, help=u"""the object storage namespace where the bucket and uploaded object resides""")
@cli_util.option('--source-details-bucket', required=True, help=u"""the bucket wherein the export archive exists in object storage""")
@cli_util.option('--source-details-object-name', required=True, help=u"""the name of the archive as it exists in object storage""")
@cli_util.option('--display-name', help=u"""Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--description', help=u"""Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--authorization-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}, 'source-details-manifest': {'module': 'application_migration', 'class': 'ImportManifest'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}, 'source-details-manifest': {'module': 'application_migration', 'class': 'ImportManifest'}})
@cli_util.wrap_exceptions
def update_source_import_source_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, source_id, source_details_manifest, source_details_namespace, source_details_bucket, source_details_object_name, display_name, description, authorization_details, freeform_tags, defined_tags, if_match):

    if isinstance(source_id, six.string_types) and len(source_id.strip()) == 0:
        raise click.UsageError('Parameter --source-id cannot be whitespace or empty string')
    if not force:
        if authorization_details or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to authorization-details and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['sourceDetails'] = {}
    _details['sourceDetails']['manifest'] = cli_util.parse_json_parameter("source_details_manifest", source_details_manifest)
    _details['sourceDetails']['namespace'] = source_details_namespace
    _details['sourceDetails']['bucket'] = source_details_bucket
    _details['sourceDetails']['objectName'] = source_details_object_name

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if authorization_details is not None:
        _details['authorizationDetails'] = cli_util.parse_json_parameter("authorization_details", authorization_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['sourceDetails']['type'] = 'IMPORT'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.update_source(
        source_id=source_id,
        update_source_details=_details,
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


@source_group.command(name=cli_util.override('application_migration.update_source_occ_source_details.command_name', 'update-source-occ-source-details'), help=u"""You can update the authorization details to access the source environment from which you want to migrate applications to Oracle Cloud Infrastructure. You can also update the description and tags of a source.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API. \n[Command Reference](updateSource)""")
@cli_util.option('--source-id', required=True, help=u"""The [OCID] of the source.""")
@cli_util.option('--source-details-compute-account', required=True, help=u"""If you are using an Oracle Cloud@Customer account with Identity Cloud Service (IDCS), enter the service instance ID. For example, if Compute-567890123 is the account name of your Oracle Cloud@Customer Compute service entitlement, then enter 567890123.""")
@cli_util.option('--display-name', help=u"""Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--description', help=u"""Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--authorization-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_source_occ_source_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, source_id, source_details_compute_account, display_name, description, authorization_details, freeform_tags, defined_tags, if_match):

    if isinstance(source_id, six.string_types) and len(source_id.strip()) == 0:
        raise click.UsageError('Parameter --source-id cannot be whitespace or empty string')
    if not force:
        if authorization_details or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to authorization-details and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['sourceDetails'] = {}
    _details['sourceDetails']['computeAccount'] = source_details_compute_account

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if authorization_details is not None:
        _details['authorizationDetails'] = cli_util.parse_json_parameter("authorization_details", authorization_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['sourceDetails']['type'] = 'OCC'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.update_source(
        source_id=source_id,
        update_source_details=_details,
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


@source_group.command(name=cli_util.override('application_migration.update_source_internal_source_details.command_name', 'update-source-internal-source-details'), help=u"""You can update the authorization details to access the source environment from which you want to migrate applications to Oracle Cloud Infrastructure. You can also update the description and tags of a source.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API. \n[Command Reference](updateSource)""")
@cli_util.option('--source-id', required=True, help=u"""The [OCID] of the source.""")
@cli_util.option('--source-details-account-name', required=True, help=u"""The identity domain ID of your traditional Oracle Cloud Infrastructure - Classic account.""")
@cli_util.option('--display-name', help=u"""Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--description', help=u"""Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--authorization-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_source_internal_source_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, source_id, source_details_account_name, display_name, description, authorization_details, freeform_tags, defined_tags, if_match):

    if isinstance(source_id, six.string_types) and len(source_id.strip()) == 0:
        raise click.UsageError('Parameter --source-id cannot be whitespace or empty string')
    if not force:
        if authorization_details or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to authorization-details and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['sourceDetails'] = {}
    _details['sourceDetails']['accountName'] = source_details_account_name

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if authorization_details is not None:
        _details['authorizationDetails'] = cli_util.parse_json_parameter("authorization_details", authorization_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['sourceDetails']['type'] = 'INTERNAL_COMPUTE'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.update_source(
        source_id=source_id,
        update_source_details=_details,
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


@source_group.command(name=cli_util.override('application_migration.update_source_ocic_source_details.command_name', 'update-source-ocic-source-details'), help=u"""You can update the authorization details to access the source environment from which you want to migrate applications to Oracle Cloud Infrastructure. You can also update the description and tags of a source.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API. \n[Command Reference](updateSource)""")
@cli_util.option('--source-id', required=True, help=u"""The [OCID] of the source.""")
@cli_util.option('--source-details-region', required=True, help=u"""The Oracle Cloud Infrastructure - Classic region from which you want to migrate your applications. For example, uscom-east-1 or uscom-central-1.""")
@cli_util.option('--source-details-compute-account', required=True, help=u"""If you are using an Oracle Cloud Infrastructure - Classic account with Identity Cloud Service (IDCS), enter the service instance ID. For example, if Compute-567890123 is the account name of your Oracle Cloud Infrastructure Classic Compute service entitlement, then enter 567890123.

If you are using a traditional Oracle Cloud Infrastructure - Classic account, enter your identity domain ID.""")
@cli_util.option('--display-name', help=u"""Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--description', help=u"""Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--authorization-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_source_ocic_source_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, source_id, source_details_region, source_details_compute_account, display_name, description, authorization_details, freeform_tags, defined_tags, if_match):

    if isinstance(source_id, six.string_types) and len(source_id.strip()) == 0:
        raise click.UsageError('Parameter --source-id cannot be whitespace or empty string')
    if not force:
        if authorization_details or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to authorization-details and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['sourceDetails'] = {}
    _details['sourceDetails']['region'] = source_details_region
    _details['sourceDetails']['computeAccount'] = source_details_compute_account

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if authorization_details is not None:
        _details['authorizationDetails'] = cli_util.parse_json_parameter("authorization_details", authorization_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['sourceDetails']['type'] = 'OCIC'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.update_source(
        source_id=source_id,
        update_source_details=_details,
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


@source_group.command(name=cli_util.override('application_migration.update_source_occ_authorization_details.command_name', 'update-source-occ-authorization-details'), help=u"""You can update the authorization details to access the source environment from which you want to migrate applications to Oracle Cloud Infrastructure. You can also update the description and tags of a source.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API. \n[Command Reference](updateSource)""")
@cli_util.option('--source-id', required=True, help=u"""The [OCID] of the source.""")
@cli_util.option('--authorization-details-username', required=True, help=u"""User with Compute Operations role in Oracle Cloud@Customer.""")
@cli_util.option('--authorization-details-password', required=True, help=u"""Password for this user.""")
@cli_util.option('--display-name', help=u"""Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--description', help=u"""Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--source-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_source_occ_authorization_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, source_id, authorization_details_username, authorization_details_password, display_name, description, source_details, freeform_tags, defined_tags, if_match):

    if isinstance(source_id, six.string_types) and len(source_id.strip()) == 0:
        raise click.UsageError('Parameter --source-id cannot be whitespace or empty string')
    if not force:
        if source_details or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to source-details and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['authorizationDetails'] = {}
    _details['authorizationDetails']['username'] = authorization_details_username
    _details['authorizationDetails']['password'] = authorization_details_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if source_details is not None:
        _details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['authorizationDetails']['type'] = 'OCC'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.update_source(
        source_id=source_id,
        update_source_details=_details,
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


@source_group.command(name=cli_util.override('application_migration.update_source_internal_authorization_details.command_name', 'update-source-internal-authorization-details'), help=u"""You can update the authorization details to access the source environment from which you want to migrate applications to Oracle Cloud Infrastructure. You can also update the description and tags of a source.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API. \n[Command Reference](updateSource)""")
@cli_util.option('--source-id', required=True, help=u"""The [OCID] of the source.""")
@cli_util.option('--authorization-details-username', required=True, help=u"""User with Compute Operations role in Oracle Cloud Infrastructure - Classic.""")
@cli_util.option('--authorization-details-password', required=True, help=u"""Password for this user.""")
@cli_util.option('--display-name', help=u"""Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--description', help=u"""Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--source-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_source_internal_authorization_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, source_id, authorization_details_username, authorization_details_password, display_name, description, source_details, freeform_tags, defined_tags, if_match):

    if isinstance(source_id, six.string_types) and len(source_id.strip()) == 0:
        raise click.UsageError('Parameter --source-id cannot be whitespace or empty string')
    if not force:
        if source_details or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to source-details and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['authorizationDetails'] = {}
    _details['authorizationDetails']['username'] = authorization_details_username
    _details['authorizationDetails']['password'] = authorization_details_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if source_details is not None:
        _details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['authorizationDetails']['type'] = 'INTERNAL_COMPUTE'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.update_source(
        source_id=source_id,
        update_source_details=_details,
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


@source_group.command(name=cli_util.override('application_migration.update_source_ocic_authorization_token_details.command_name', 'update-source-ocic-authorization-token-details'), help=u"""You can update the authorization details to access the source environment from which you want to migrate applications to Oracle Cloud Infrastructure. You can also update the description and tags of a source.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API. \n[Command Reference](updateSource)""")
@cli_util.option('--source-id', required=True, help=u"""The [OCID] of the source.""")
@cli_util.option('--authorization-details-client-app-url', required=True, help=u"""AuthClient app url resource that the accesstoken is for.""")
@cli_util.option('--authorization-details-access-token', required=True, help=u"""AccessToken to access the app endpoint.""")
@cli_util.option('--display-name', help=u"""Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--description', help=u"""Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--source-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_source_ocic_authorization_token_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, source_id, authorization_details_client_app_url, authorization_details_access_token, display_name, description, source_details, freeform_tags, defined_tags, if_match):

    if isinstance(source_id, six.string_types) and len(source_id.strip()) == 0:
        raise click.UsageError('Parameter --source-id cannot be whitespace or empty string')
    if not force:
        if source_details or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to source-details and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['authorizationDetails'] = {}
    _details['authorizationDetails']['clientAppUrl'] = authorization_details_client_app_url
    _details['authorizationDetails']['accessToken'] = authorization_details_access_token

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if source_details is not None:
        _details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['authorizationDetails']['type'] = 'OCIC_IDCS'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.update_source(
        source_id=source_id,
        update_source_details=_details,
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


@source_group.command(name=cli_util.override('application_migration.update_source_ocic_authorization_details.command_name', 'update-source-ocic-authorization-details'), help=u"""You can update the authorization details to access the source environment from which you want to migrate applications to Oracle Cloud Infrastructure. You can also update the description and tags of a source.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API. \n[Command Reference](updateSource)""")
@cli_util.option('--source-id', required=True, help=u"""The [OCID] of the source.""")
@cli_util.option('--authorization-details-username', required=True, help=u"""User with Compute Operations role in Oracle Cloud Infrastructure - Classic.""")
@cli_util.option('--authorization-details-password', required=True, help=u"""Password for this user.""")
@cli_util.option('--display-name', help=u"""Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--description', help=u"""Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.""")
@cli_util.option('--source-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_source_ocic_authorization_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, source_id, authorization_details_username, authorization_details_password, display_name, description, source_details, freeform_tags, defined_tags, if_match):

    if isinstance(source_id, six.string_types) and len(source_id.strip()) == 0:
        raise click.UsageError('Parameter --source-id cannot be whitespace or empty string')
    if not force:
        if source_details or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to source-details and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['authorizationDetails'] = {}
    _details['authorizationDetails']['username'] = authorization_details_username
    _details['authorizationDetails']['password'] = authorization_details_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if source_details is not None:
        _details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['authorizationDetails']['type'] = 'OCIC'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.update_source(
        source_id=source_id,
        update_source_details=_details,
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
