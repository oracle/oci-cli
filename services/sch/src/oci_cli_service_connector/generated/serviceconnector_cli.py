# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
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


@cli.command(cli_util.override('sch.sch_root_group.command_name', 'sch'), cls=CommandGroupWithAlias, help=cli_util.override('sch.sch_root_group.help', """Use the Service Connector Hub API to transfer data between services in Oracle Cloud Infrastructure.
For more information about Service Connector Hub, see
[Service Connector Hub Overview]."""), short_help=cli_util.override('sch.sch_root_group.short_help', """Service Connector Hub API"""))
@cli_util.help_option_group
def sch_root_group():
    pass


@click.command(cli_util.override('sch.service_connector_group.command_name', 'service-connector'), cls=CommandGroupWithAlias, help="""The configuration details of the flow defined by the service connector. For more information about flows defined by service connectors, see [Service Connector Hub Overview].""")
@cli_util.help_option_group
def service_connector_group():
    pass


@click.command(cli_util.override('sch.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('sch.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""A log message from the execution of a work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('sch.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""An object representing an asynchronous work flow.

Many of the API requests you use to create and configure service connectors do not take effect immediately. In these cases, the request spawns an asynchronous work flow to fulfill the request. WorkRequest objects provide visibility for in-progress work flows. For more information about work requests, see [Viewing the State of a Work Request].""")
@cli_util.help_option_group
def work_request_group():
    pass


sch_root_group.add_command(service_connector_group)
sch_root_group.add_command(work_request_error_group)
sch_root_group.add_command(work_request_log_entry_group)
sch_root_group.add_command(work_request_group)


@service_connector_group.command(name=cli_util.override('sch.activate_service_connector.command_name', 'activate'), help=u"""Activates the specified service connector.

After you send your request, the service connector's state is temporarily UPDATING. When the state changes to ACTIVE, data begins transferring from the source service to the target service. For instructions on activating service connectors, see [To activate a service connector]. \n[Command Reference](activateServiceConnector)""")
@cli_util.option('--service-connector-id', required=True, help=u"""The [OCID] of the service connector.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def activate_service_connector(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, service_connector_id, if_match):

    if isinstance(service_connector_id, six.string_types) and len(service_connector_id.strip()) == 0:
        raise click.UsageError('Parameter --service-connector-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('sch', 'service_connector', ctx)
    result = client.activate_service_connector(
        service_connector_id=service_connector_id,
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


@service_connector_group.command(name=cli_util.override('sch.change_service_connector_compartment.command_name', 'change-compartment'), help=u"""Moves a service connector into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment].

When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeServiceConnectorCompartment)""")
@cli_util.option('--service-connector-id', required=True, help=u"""The [OCID] of the service connector.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the service connector to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_service_connector_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, service_connector_id, compartment_id, if_match):

    if isinstance(service_connector_id, six.string_types) and len(service_connector_id.strip()) == 0:
        raise click.UsageError('Parameter --service-connector-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('sch', 'service_connector', ctx)
    result = client.change_service_connector_compartment(
        service_connector_id=service_connector_id,
        change_service_connector_compartment_details=_details,
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


@service_connector_group.command(name=cli_util.override('sch.create_service_connector.command_name', 'create'), help=u"""Creates a new service connector in the specified compartment. A service connector is a logically defined flow for moving data from a source service to a destination service in Oracle Cloud Infrastructure. For general information about service connectors, see [Service Connector Hub Overview].

For purposes of access control, you must provide the [OCID] of the compartment where you want the service connector to reside. Notice that the service connector doesn't have to be in the same compartment as the source or target services. For information about access control and compartments, see [Overview of the IAM Service].

After you send your request, the new service connector's state is temporarily CREATING. When the state changes to ACTIVE, data begins transferring from the source service to the target service. For instructions on deactivating and activating service connectors, see [To activate or deactivate a service connector]. \n[Command Reference](createServiceConnector)""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the comparment to create the service connector in.""")
@cli_util.option('--source', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--target', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""The description of the resource. Avoid entering confidential information.""")
@cli_util.option('--tasks', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of tasks.

This option is a JSON list with items of type TaskDetails.  For documentation on TaskDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/serviceconnector/20200909/datatypes/TaskDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source': {'module': 'sch', 'class': 'SourceDetails'}, 'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'target': {'module': 'sch', 'class': 'TargetDetails'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source': {'module': 'sch', 'class': 'SourceDetails'}, 'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'target': {'module': 'sch', 'class': 'TargetDetails'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_service_connector(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, source, target, description, tasks, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['source'] = cli_util.parse_json_parameter("source", source)
    _details['target'] = cli_util.parse_json_parameter("target", target)

    if description is not None:
        _details['description'] = description

    if tasks is not None:
        _details['tasks'] = cli_util.parse_json_parameter("tasks", tasks)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('sch', 'service_connector', ctx)
    result = client.create_service_connector(
        create_service_connector_details=_details,
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


@service_connector_group.command(name=cli_util.override('sch.create_service_connector_logging_source_details.command_name', 'create-service-connector-logging-source-details'), help=u"""Creates a new service connector in the specified compartment. A service connector is a logically defined flow for moving data from a source service to a destination service in Oracle Cloud Infrastructure. For general information about service connectors, see [Service Connector Hub Overview].

For purposes of access control, you must provide the [OCID] of the compartment where you want the service connector to reside. Notice that the service connector doesn't have to be in the same compartment as the source or target services. For information about access control and compartments, see [Overview of the IAM Service].

After you send your request, the new service connector's state is temporarily CREATING. When the state changes to ACTIVE, data begins transferring from the source service to the target service. For instructions on deactivating and activating service connectors, see [To activate or deactivate a service connector]. \n[Command Reference](createServiceConnector)""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the comparment to create the service connector in.""")
@cli_util.option('--target', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--source-log-sources', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The resources affected by this work request.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""The description of the resource. Avoid entering confidential information.""")
@cli_util.option('--tasks', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of tasks.

This option is a JSON list with items of type TaskDetails.  For documentation on TaskDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/serviceconnector/20200909/datatypes/TaskDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'target': {'module': 'sch', 'class': 'TargetDetails'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}, 'source-log-sources': {'module': 'sch', 'class': 'list[LogSource]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'target': {'module': 'sch', 'class': 'TargetDetails'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}, 'source-log-sources': {'module': 'sch', 'class': 'list[LogSource]'}})
@cli_util.wrap_exceptions
def create_service_connector_logging_source_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, target, source_log_sources, description, tasks, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['source'] = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['target'] = cli_util.parse_json_parameter("target", target)
    _details['source']['logSources'] = cli_util.parse_json_parameter("source_log_sources", source_log_sources)

    if description is not None:
        _details['description'] = description

    if tasks is not None:
        _details['tasks'] = cli_util.parse_json_parameter("tasks", tasks)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['source']['kind'] = 'logging'

    client = cli_util.build_client('sch', 'service_connector', ctx)
    result = client.create_service_connector(
        create_service_connector_details=_details,
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


@service_connector_group.command(name=cli_util.override('sch.create_service_connector_notifications_target_details.command_name', 'create-service-connector-notifications-target-details'), help=u"""Creates a new service connector in the specified compartment. A service connector is a logically defined flow for moving data from a source service to a destination service in Oracle Cloud Infrastructure. For general information about service connectors, see [Service Connector Hub Overview].

For purposes of access control, you must provide the [OCID] of the compartment where you want the service connector to reside. Notice that the service connector doesn't have to be in the same compartment as the source or target services. For information about access control and compartments, see [Overview of the IAM Service].

After you send your request, the new service connector's state is temporarily CREATING. When the state changes to ACTIVE, data begins transferring from the source service to the target service. For instructions on deactivating and activating service connectors, see [To activate or deactivate a service connector]. \n[Command Reference](createServiceConnector)""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the comparment to create the service connector in.""")
@cli_util.option('--source', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--target-topic-id', required=True, help=u"""The [OCID] of the topic.""")
@cli_util.option('--description', help=u"""The description of the resource. Avoid entering confidential information.""")
@cli_util.option('--tasks', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of tasks.

This option is a JSON list with items of type TaskDetails.  For documentation on TaskDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/serviceconnector/20200909/datatypes/TaskDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source': {'module': 'sch', 'class': 'SourceDetails'}, 'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source': {'module': 'sch', 'class': 'SourceDetails'}, 'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_service_connector_notifications_target_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, source, target_topic_id, description, tasks, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['target'] = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['source'] = cli_util.parse_json_parameter("source", source)
    _details['target']['topicId'] = target_topic_id

    if description is not None:
        _details['description'] = description

    if tasks is not None:
        _details['tasks'] = cli_util.parse_json_parameter("tasks", tasks)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['target']['kind'] = 'notifications'

    client = cli_util.build_client('sch', 'service_connector', ctx)
    result = client.create_service_connector(
        create_service_connector_details=_details,
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


@service_connector_group.command(name=cli_util.override('sch.create_service_connector_object_storage_target_details.command_name', 'create-service-connector-object-storage-target-details'), help=u"""Creates a new service connector in the specified compartment. A service connector is a logically defined flow for moving data from a source service to a destination service in Oracle Cloud Infrastructure. For general information about service connectors, see [Service Connector Hub Overview].

For purposes of access control, you must provide the [OCID] of the compartment where you want the service connector to reside. Notice that the service connector doesn't have to be in the same compartment as the source or target services. For information about access control and compartments, see [Overview of the IAM Service].

After you send your request, the new service connector's state is temporarily CREATING. When the state changes to ACTIVE, data begins transferring from the source service to the target service. For instructions on deactivating and activating service connectors, see [To activate or deactivate a service connector]. \n[Command Reference](createServiceConnector)""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the comparment to create the service connector in.""")
@cli_util.option('--source', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--target-bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""The description of the resource. Avoid entering confidential information.""")
@cli_util.option('--tasks', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of tasks.

This option is a JSON list with items of type TaskDetails.  For documentation on TaskDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/serviceconnector/20200909/datatypes/TaskDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--target-namespace', help=u"""The namespace.""")
@cli_util.option('--target-object-name-prefix', help=u"""The prefix of the objects. Avoid entering confidential information.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source': {'module': 'sch', 'class': 'SourceDetails'}, 'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source': {'module': 'sch', 'class': 'SourceDetails'}, 'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_service_connector_object_storage_target_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, source, target_bucket_name, description, tasks, freeform_tags, defined_tags, target_namespace, target_object_name_prefix):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['target'] = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['source'] = cli_util.parse_json_parameter("source", source)
    _details['target']['bucketName'] = target_bucket_name

    if description is not None:
        _details['description'] = description

    if tasks is not None:
        _details['tasks'] = cli_util.parse_json_parameter("tasks", tasks)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if target_namespace is not None:
        _details['target']['namespace'] = target_namespace

    if target_object_name_prefix is not None:
        _details['target']['objectNamePrefix'] = target_object_name_prefix

    _details['target']['kind'] = 'objectStorage'

    client = cli_util.build_client('sch', 'service_connector', ctx)
    result = client.create_service_connector(
        create_service_connector_details=_details,
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


@service_connector_group.command(name=cli_util.override('sch.create_service_connector_monitoring_target_details.command_name', 'create-service-connector-monitoring-target-details'), help=u"""Creates a new service connector in the specified compartment. A service connector is a logically defined flow for moving data from a source service to a destination service in Oracle Cloud Infrastructure. For general information about service connectors, see [Service Connector Hub Overview].

For purposes of access control, you must provide the [OCID] of the compartment where you want the service connector to reside. Notice that the service connector doesn't have to be in the same compartment as the source or target services. For information about access control and compartments, see [Overview of the IAM Service].

After you send your request, the new service connector's state is temporarily CREATING. When the state changes to ACTIVE, data begins transferring from the source service to the target service. For instructions on deactivating and activating service connectors, see [To activate or deactivate a service connector]. \n[Command Reference](createServiceConnector)""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the comparment to create the service connector in.""")
@cli_util.option('--source', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--target-compartment-id', required=True, help=u"""The [OCID] of the compartment containing the metric.""")
@cli_util.option('--target-metric-namespace', required=True, help=u"""The namespace of the metric.

Example: `oci_computeagent`""")
@cli_util.option('--target-metric', required=True, help=u"""The name of the metric.

Example: `CpuUtilization`""")
@cli_util.option('--description', help=u"""The description of the resource. Avoid entering confidential information.""")
@cli_util.option('--tasks', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of tasks.

This option is a JSON list with items of type TaskDetails.  For documentation on TaskDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/serviceconnector/20200909/datatypes/TaskDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source': {'module': 'sch', 'class': 'SourceDetails'}, 'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source': {'module': 'sch', 'class': 'SourceDetails'}, 'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_service_connector_monitoring_target_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, source, target_compartment_id, target_metric_namespace, target_metric, description, tasks, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['target'] = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['source'] = cli_util.parse_json_parameter("source", source)
    _details['target']['compartmentId'] = target_compartment_id
    _details['target']['metricNamespace'] = target_metric_namespace
    _details['target']['metric'] = target_metric

    if description is not None:
        _details['description'] = description

    if tasks is not None:
        _details['tasks'] = cli_util.parse_json_parameter("tasks", tasks)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['target']['kind'] = 'monitoring'

    client = cli_util.build_client('sch', 'service_connector', ctx)
    result = client.create_service_connector(
        create_service_connector_details=_details,
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


@service_connector_group.command(name=cli_util.override('sch.create_service_connector_functions_target_details.command_name', 'create-service-connector-functions-target-details'), help=u"""Creates a new service connector in the specified compartment. A service connector is a logically defined flow for moving data from a source service to a destination service in Oracle Cloud Infrastructure. For general information about service connectors, see [Service Connector Hub Overview].

For purposes of access control, you must provide the [OCID] of the compartment where you want the service connector to reside. Notice that the service connector doesn't have to be in the same compartment as the source or target services. For information about access control and compartments, see [Overview of the IAM Service].

After you send your request, the new service connector's state is temporarily CREATING. When the state changes to ACTIVE, data begins transferring from the source service to the target service. For instructions on deactivating and activating service connectors, see [To activate or deactivate a service connector]. \n[Command Reference](createServiceConnector)""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the comparment to create the service connector in.""")
@cli_util.option('--source', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--target-function-id', required=True, help=u"""The [OCID] of the function.""")
@cli_util.option('--description', help=u"""The description of the resource. Avoid entering confidential information.""")
@cli_util.option('--tasks', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of tasks.

This option is a JSON list with items of type TaskDetails.  For documentation on TaskDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/serviceconnector/20200909/datatypes/TaskDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source': {'module': 'sch', 'class': 'SourceDetails'}, 'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source': {'module': 'sch', 'class': 'SourceDetails'}, 'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_service_connector_functions_target_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, source, target_function_id, description, tasks, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['target'] = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['source'] = cli_util.parse_json_parameter("source", source)
    _details['target']['functionId'] = target_function_id

    if description is not None:
        _details['description'] = description

    if tasks is not None:
        _details['tasks'] = cli_util.parse_json_parameter("tasks", tasks)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['target']['kind'] = 'functions'

    client = cli_util.build_client('sch', 'service_connector', ctx)
    result = client.create_service_connector(
        create_service_connector_details=_details,
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


@service_connector_group.command(name=cli_util.override('sch.create_service_connector_streaming_target_details.command_name', 'create-service-connector-streaming-target-details'), help=u"""Creates a new service connector in the specified compartment. A service connector is a logically defined flow for moving data from a source service to a destination service in Oracle Cloud Infrastructure. For general information about service connectors, see [Service Connector Hub Overview].

For purposes of access control, you must provide the [OCID] of the compartment where you want the service connector to reside. Notice that the service connector doesn't have to be in the same compartment as the source or target services. For information about access control and compartments, see [Overview of the IAM Service].

After you send your request, the new service connector's state is temporarily CREATING. When the state changes to ACTIVE, data begins transferring from the source service to the target service. For instructions on deactivating and activating service connectors, see [To activate or deactivate a service connector]. \n[Command Reference](createServiceConnector)""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the comparment to create the service connector in.""")
@cli_util.option('--source', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--target-stream-id', required=True, help=u"""The [OCID] of the stream.""")
@cli_util.option('--description', help=u"""The description of the resource. Avoid entering confidential information.""")
@cli_util.option('--tasks', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of tasks.

This option is a JSON list with items of type TaskDetails.  For documentation on TaskDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/serviceconnector/20200909/datatypes/TaskDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source': {'module': 'sch', 'class': 'SourceDetails'}, 'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source': {'module': 'sch', 'class': 'SourceDetails'}, 'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_service_connector_streaming_target_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, source, target_stream_id, description, tasks, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['target'] = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['source'] = cli_util.parse_json_parameter("source", source)
    _details['target']['streamId'] = target_stream_id

    if description is not None:
        _details['description'] = description

    if tasks is not None:
        _details['tasks'] = cli_util.parse_json_parameter("tasks", tasks)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['target']['kind'] = 'streaming'

    client = cli_util.build_client('sch', 'service_connector', ctx)
    result = client.create_service_connector(
        create_service_connector_details=_details,
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


@service_connector_group.command(name=cli_util.override('sch.deactivate_service_connector.command_name', 'deactivate'), help=u"""Deactivates the specified service connector.

After you send your request, the service connector's state is temporarily UPDATING and any data transfer stops. The state then changes to INACTIVE. For instructions on deactivating service connectors, see [To deactivate a service connector]. \n[Command Reference](deactivateServiceConnector)""")
@cli_util.option('--service-connector-id', required=True, help=u"""The [OCID] of the service connector.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def deactivate_service_connector(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, service_connector_id, if_match):

    if isinstance(service_connector_id, six.string_types) and len(service_connector_id.strip()) == 0:
        raise click.UsageError('Parameter --service-connector-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('sch', 'service_connector', ctx)
    result = client.deactivate_service_connector(
        service_connector_id=service_connector_id,
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


@service_connector_group.command(name=cli_util.override('sch.delete_service_connector.command_name', 'delete'), help=u"""Deletes the specified service connector.

After you send your request, the service connector's state is temporarily DELETING and any data transfer stops. The state then changes to DELETED. \n[Command Reference](deleteServiceConnector)""")
@cli_util.option('--service-connector-id', required=True, help=u"""The [OCID] of the service connector.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_service_connector(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, service_connector_id, if_match):

    if isinstance(service_connector_id, six.string_types) and len(service_connector_id.strip()) == 0:
        raise click.UsageError('Parameter --service-connector-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('sch', 'service_connector', ctx)
    result = client.delete_service_connector(
        service_connector_id=service_connector_id,
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


@service_connector_group.command(name=cli_util.override('sch.get_service_connector.command_name', 'get'), help=u"""Gets the specified service connector's configuration information. \n[Command Reference](getServiceConnector)""")
@cli_util.option('--service-connector-id', required=True, help=u"""The [OCID] of the service connector.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'sch', 'class': 'ServiceConnector'})
@cli_util.wrap_exceptions
def get_service_connector(ctx, from_json, service_connector_id):

    if isinstance(service_connector_id, six.string_types) and len(service_connector_id.strip()) == 0:
        raise click.UsageError('Parameter --service-connector-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('sch', 'service_connector', ctx)
    result = client.get_service_connector(
        service_connector_id=service_connector_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('sch.get_work_request.command_name', 'get'), help=u"""Gets the details of the specified work request. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the work request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'sch', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('sch', 'service_connector', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@service_connector_group.command(name=cli_util.override('sch.list_service_connectors.command_name', 'list'), help=u"""Lists service connectors in the specified compartment. \n[Command Reference](listServiceConnectors)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment for this request.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources that match the given lifecycle state.

Example: `ACTIVE`""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.

Example: `example_service_connector`""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""For list pagination. The value of the opc-next-page response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for `timeCreated` is descending. Default order for `displayName` is ascending. If no value is specified `timeCreated` is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'sch', 'class': 'ServiceConnectorCollection'})
@cli_util.wrap_exceptions
def list_service_connectors(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, display_name, limit, page, sort_order, sort_by):

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
    client = cli_util.build_client('sch', 'service_connector', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_service_connectors,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_service_connectors,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_service_connectors(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('sch.list_work_request_errors.command_name', 'list'), help=u"""Lists work request errors for the specified work request. Results are paginated. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the work request.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the opc-next-page response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'sch', 'class': 'WorkRequestErrorCollection'})
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
    client = cli_util.build_client('sch', 'service_connector', ctx)
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


@work_request_log_entry_group.command(name=cli_util.override('sch.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Lists logs for the specified work request. Results are paginated. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the work request.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the opc-next-page response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'sch', 'class': 'WorkRequestLogEntryCollection'})
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
    client = cli_util.build_client('sch', 'service_connector', ctx)
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


@work_request_group.command(name=cli_util.override('sch.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in the specified compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment for this request.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the opc-next-page response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'sch', 'class': 'WorkRequestCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('sch', 'service_connector', ctx)
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


@service_connector_group.command(name=cli_util.override('sch.update_service_connector.command_name', 'update'), help=u"""Updates the configuration information for the specified service connector.

After you send your request, the service connector's state is temporarily UPDATING and any data transfer pauses. The state then changes back to its original value: if ACTIVE, then data transfer resumes. \n[Command Reference](updateServiceConnector)""")
@cli_util.option('--service-connector-id', required=True, help=u"""The [OCID] of the service connector.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""The description of the resource. Avoid entering confidential information.""")
@cli_util.option('--source', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--tasks', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of the tasks.

This option is a JSON list with items of type TaskDetails.  For documentation on TaskDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/serviceconnector/20200909/datatypes/TaskDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--target', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source': {'module': 'sch', 'class': 'SourceDetails'}, 'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'target': {'module': 'sch', 'class': 'TargetDetails'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source': {'module': 'sch', 'class': 'SourceDetails'}, 'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'target': {'module': 'sch', 'class': 'TargetDetails'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_service_connector(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, service_connector_id, display_name, description, source, tasks, target, freeform_tags, defined_tags, if_match):

    if isinstance(service_connector_id, six.string_types) and len(service_connector_id.strip()) == 0:
        raise click.UsageError('Parameter --service-connector-id cannot be whitespace or empty string')
    if not force:
        if source or tasks or target or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to source and tasks and target and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
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

    if source is not None:
        _details['source'] = cli_util.parse_json_parameter("source", source)

    if tasks is not None:
        _details['tasks'] = cli_util.parse_json_parameter("tasks", tasks)

    if target is not None:
        _details['target'] = cli_util.parse_json_parameter("target", target)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('sch', 'service_connector', ctx)
    result = client.update_service_connector(
        service_connector_id=service_connector_id,
        update_service_connector_details=_details,
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


@service_connector_group.command(name=cli_util.override('sch.update_service_connector_logging_source_details.command_name', 'update-service-connector-logging-source-details'), help=u"""Updates the configuration information for the specified service connector.

After you send your request, the service connector's state is temporarily UPDATING and any data transfer pauses. The state then changes back to its original value: if ACTIVE, then data transfer resumes. \n[Command Reference](updateServiceConnector)""")
@cli_util.option('--service-connector-id', required=True, help=u"""The [OCID] of the service connector.""")
@cli_util.option('--source-log-sources', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The resources affected by this work request.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""The description of the resource. Avoid entering confidential information.""")
@cli_util.option('--tasks', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of the tasks.

This option is a JSON list with items of type TaskDetails.  For documentation on TaskDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/serviceconnector/20200909/datatypes/TaskDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--target', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'target': {'module': 'sch', 'class': 'TargetDetails'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}, 'source-log-sources': {'module': 'sch', 'class': 'list[LogSource]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'target': {'module': 'sch', 'class': 'TargetDetails'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}, 'source-log-sources': {'module': 'sch', 'class': 'list[LogSource]'}})
@cli_util.wrap_exceptions
def update_service_connector_logging_source_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, service_connector_id, source_log_sources, display_name, description, tasks, target, freeform_tags, defined_tags, if_match):

    if isinstance(service_connector_id, six.string_types) and len(service_connector_id.strip()) == 0:
        raise click.UsageError('Parameter --service-connector-id cannot be whitespace or empty string')
    if not force:
        if tasks or target or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to tasks and target and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['source'] = {}
    _details['source']['logSources'] = cli_util.parse_json_parameter("source_log_sources", source_log_sources)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if tasks is not None:
        _details['tasks'] = cli_util.parse_json_parameter("tasks", tasks)

    if target is not None:
        _details['target'] = cli_util.parse_json_parameter("target", target)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['source']['kind'] = 'logging'

    client = cli_util.build_client('sch', 'service_connector', ctx)
    result = client.update_service_connector(
        service_connector_id=service_connector_id,
        update_service_connector_details=_details,
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


@service_connector_group.command(name=cli_util.override('sch.update_service_connector_notifications_target_details.command_name', 'update-service-connector-notifications-target-details'), help=u"""Updates the configuration information for the specified service connector.

After you send your request, the service connector's state is temporarily UPDATING and any data transfer pauses. The state then changes back to its original value: if ACTIVE, then data transfer resumes. \n[Command Reference](updateServiceConnector)""")
@cli_util.option('--service-connector-id', required=True, help=u"""The [OCID] of the service connector.""")
@cli_util.option('--target-topic-id', required=True, help=u"""The [OCID] of the topic.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""The description of the resource. Avoid entering confidential information.""")
@cli_util.option('--source', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--tasks', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of the tasks.

This option is a JSON list with items of type TaskDetails.  For documentation on TaskDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/serviceconnector/20200909/datatypes/TaskDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source': {'module': 'sch', 'class': 'SourceDetails'}, 'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source': {'module': 'sch', 'class': 'SourceDetails'}, 'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_service_connector_notifications_target_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, service_connector_id, target_topic_id, display_name, description, source, tasks, freeform_tags, defined_tags, if_match):

    if isinstance(service_connector_id, six.string_types) and len(service_connector_id.strip()) == 0:
        raise click.UsageError('Parameter --service-connector-id cannot be whitespace or empty string')
    if not force:
        if source or tasks or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to source and tasks and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['target'] = {}
    _details['target']['topicId'] = target_topic_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if source is not None:
        _details['source'] = cli_util.parse_json_parameter("source", source)

    if tasks is not None:
        _details['tasks'] = cli_util.parse_json_parameter("tasks", tasks)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['target']['kind'] = 'notifications'

    client = cli_util.build_client('sch', 'service_connector', ctx)
    result = client.update_service_connector(
        service_connector_id=service_connector_id,
        update_service_connector_details=_details,
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


@service_connector_group.command(name=cli_util.override('sch.update_service_connector_object_storage_target_details.command_name', 'update-service-connector-object-storage-target-details'), help=u"""Updates the configuration information for the specified service connector.

After you send your request, the service connector's state is temporarily UPDATING and any data transfer pauses. The state then changes back to its original value: if ACTIVE, then data transfer resumes. \n[Command Reference](updateServiceConnector)""")
@cli_util.option('--service-connector-id', required=True, help=u"""The [OCID] of the service connector.""")
@cli_util.option('--target-bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""The description of the resource. Avoid entering confidential information.""")
@cli_util.option('--source', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--tasks', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of the tasks.

This option is a JSON list with items of type TaskDetails.  For documentation on TaskDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/serviceconnector/20200909/datatypes/TaskDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--target-namespace', help=u"""The namespace.""")
@cli_util.option('--target-object-name-prefix', help=u"""The prefix of the objects. Avoid entering confidential information.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source': {'module': 'sch', 'class': 'SourceDetails'}, 'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source': {'module': 'sch', 'class': 'SourceDetails'}, 'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_service_connector_object_storage_target_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, service_connector_id, target_bucket_name, display_name, description, source, tasks, freeform_tags, defined_tags, if_match, target_namespace, target_object_name_prefix):

    if isinstance(service_connector_id, six.string_types) and len(service_connector_id.strip()) == 0:
        raise click.UsageError('Parameter --service-connector-id cannot be whitespace or empty string')
    if not force:
        if source or tasks or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to source and tasks and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['target'] = {}
    _details['target']['bucketName'] = target_bucket_name

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if source is not None:
        _details['source'] = cli_util.parse_json_parameter("source", source)

    if tasks is not None:
        _details['tasks'] = cli_util.parse_json_parameter("tasks", tasks)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if target_namespace is not None:
        _details['target']['namespace'] = target_namespace

    if target_object_name_prefix is not None:
        _details['target']['objectNamePrefix'] = target_object_name_prefix

    _details['target']['kind'] = 'objectStorage'

    client = cli_util.build_client('sch', 'service_connector', ctx)
    result = client.update_service_connector(
        service_connector_id=service_connector_id,
        update_service_connector_details=_details,
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


@service_connector_group.command(name=cli_util.override('sch.update_service_connector_monitoring_target_details.command_name', 'update-service-connector-monitoring-target-details'), help=u"""Updates the configuration information for the specified service connector.

After you send your request, the service connector's state is temporarily UPDATING and any data transfer pauses. The state then changes back to its original value: if ACTIVE, then data transfer resumes. \n[Command Reference](updateServiceConnector)""")
@cli_util.option('--service-connector-id', required=True, help=u"""The [OCID] of the service connector.""")
@cli_util.option('--target-compartment-id', required=True, help=u"""The [OCID] of the compartment containing the metric.""")
@cli_util.option('--target-metric-namespace', required=True, help=u"""The namespace of the metric.

Example: `oci_computeagent`""")
@cli_util.option('--target-metric', required=True, help=u"""The name of the metric.

Example: `CpuUtilization`""")
@cli_util.option('--display-name', help=u"""A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""The description of the resource. Avoid entering confidential information.""")
@cli_util.option('--source', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--tasks', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of the tasks.

This option is a JSON list with items of type TaskDetails.  For documentation on TaskDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/serviceconnector/20200909/datatypes/TaskDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source': {'module': 'sch', 'class': 'SourceDetails'}, 'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source': {'module': 'sch', 'class': 'SourceDetails'}, 'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_service_connector_monitoring_target_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, service_connector_id, target_compartment_id, target_metric_namespace, target_metric, display_name, description, source, tasks, freeform_tags, defined_tags, if_match):

    if isinstance(service_connector_id, six.string_types) and len(service_connector_id.strip()) == 0:
        raise click.UsageError('Parameter --service-connector-id cannot be whitespace or empty string')
    if not force:
        if source or tasks or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to source and tasks and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['target'] = {}
    _details['target']['compartmentId'] = target_compartment_id
    _details['target']['metricNamespace'] = target_metric_namespace
    _details['target']['metric'] = target_metric

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if source is not None:
        _details['source'] = cli_util.parse_json_parameter("source", source)

    if tasks is not None:
        _details['tasks'] = cli_util.parse_json_parameter("tasks", tasks)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['target']['kind'] = 'monitoring'

    client = cli_util.build_client('sch', 'service_connector', ctx)
    result = client.update_service_connector(
        service_connector_id=service_connector_id,
        update_service_connector_details=_details,
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


@service_connector_group.command(name=cli_util.override('sch.update_service_connector_functions_target_details.command_name', 'update-service-connector-functions-target-details'), help=u"""Updates the configuration information for the specified service connector.

After you send your request, the service connector's state is temporarily UPDATING and any data transfer pauses. The state then changes back to its original value: if ACTIVE, then data transfer resumes. \n[Command Reference](updateServiceConnector)""")
@cli_util.option('--service-connector-id', required=True, help=u"""The [OCID] of the service connector.""")
@cli_util.option('--target-function-id', required=True, help=u"""The [OCID] of the function.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""The description of the resource. Avoid entering confidential information.""")
@cli_util.option('--source', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--tasks', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of the tasks.

This option is a JSON list with items of type TaskDetails.  For documentation on TaskDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/serviceconnector/20200909/datatypes/TaskDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source': {'module': 'sch', 'class': 'SourceDetails'}, 'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source': {'module': 'sch', 'class': 'SourceDetails'}, 'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_service_connector_functions_target_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, service_connector_id, target_function_id, display_name, description, source, tasks, freeform_tags, defined_tags, if_match):

    if isinstance(service_connector_id, six.string_types) and len(service_connector_id.strip()) == 0:
        raise click.UsageError('Parameter --service-connector-id cannot be whitespace or empty string')
    if not force:
        if source or tasks or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to source and tasks and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['target'] = {}
    _details['target']['functionId'] = target_function_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if source is not None:
        _details['source'] = cli_util.parse_json_parameter("source", source)

    if tasks is not None:
        _details['tasks'] = cli_util.parse_json_parameter("tasks", tasks)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['target']['kind'] = 'functions'

    client = cli_util.build_client('sch', 'service_connector', ctx)
    result = client.update_service_connector(
        service_connector_id=service_connector_id,
        update_service_connector_details=_details,
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


@service_connector_group.command(name=cli_util.override('sch.update_service_connector_streaming_target_details.command_name', 'update-service-connector-streaming-target-details'), help=u"""Updates the configuration information for the specified service connector.

After you send your request, the service connector's state is temporarily UPDATING and any data transfer pauses. The state then changes back to its original value: if ACTIVE, then data transfer resumes. \n[Command Reference](updateServiceConnector)""")
@cli_util.option('--service-connector-id', required=True, help=u"""The [OCID] of the service connector.""")
@cli_util.option('--target-stream-id', required=True, help=u"""The [OCID] of the stream.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""The description of the resource. Avoid entering confidential information.""")
@cli_util.option('--source', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--tasks', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of the tasks.

This option is a JSON list with items of type TaskDetails.  For documentation on TaskDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/serviceconnector/20200909/datatypes/TaskDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source': {'module': 'sch', 'class': 'SourceDetails'}, 'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source': {'module': 'sch', 'class': 'SourceDetails'}, 'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_service_connector_streaming_target_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, service_connector_id, target_stream_id, display_name, description, source, tasks, freeform_tags, defined_tags, if_match):

    if isinstance(service_connector_id, six.string_types) and len(service_connector_id.strip()) == 0:
        raise click.UsageError('Parameter --service-connector-id cannot be whitespace or empty string')
    if not force:
        if source or tasks or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to source and tasks and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['target'] = {}
    _details['target']['streamId'] = target_stream_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if source is not None:
        _details['source'] = cli_util.parse_json_parameter("source", source)

    if tasks is not None:
        _details['tasks'] = cli_util.parse_json_parameter("tasks", tasks)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['target']['kind'] = 'streaming'

    client = cli_util.build_client('sch', 'service_connector', ctx)
    result = client.update_service_connector(
        service_connector_id=service_connector_id,
        update_service_connector_details=_details,
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
