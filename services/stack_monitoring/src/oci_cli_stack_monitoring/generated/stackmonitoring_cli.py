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


@cli.command(cli_util.override('stack_monitoring.stack_monitoring_root_group.command_name', 'stack-monitoring'), cls=CommandGroupWithAlias, help=cli_util.override('stack_monitoring.stack_monitoring_root_group.help', """Stack Monitoring API."""), short_help=cli_util.override('stack_monitoring.stack_monitoring_root_group.short_help', """Stack Monitoring API"""))
@cli_util.help_option_group
def stack_monitoring_root_group():
    pass


@click.command(cli_util.override('stack_monitoring.discovery_job_collection_group.command_name', 'discovery-job-collection'), cls=CommandGroupWithAlias, help="""Result of the discovery Job search""")
@cli_util.help_option_group
def discovery_job_collection_group():
    pass


@click.command(cli_util.override('stack_monitoring.monitored_resource_group.command_name', 'monitored-resource'), cls=CommandGroupWithAlias, help="""The information about monitored resource.""")
@cli_util.help_option_group
def monitored_resource_group():
    pass


@click.command(cli_util.override('stack_monitoring.work_request_error_collection_group.command_name', 'work-request-error-collection'), cls=CommandGroupWithAlias, help="""Results of a workRequestError search. Contains both WorkRequestError items and other information, such as metadata.""")
@cli_util.help_option_group
def work_request_error_collection_group():
    pass


@click.command(cli_util.override('stack_monitoring.discovery_job_group.command_name', 'discovery-job'), cls=CommandGroupWithAlias, help="""The DiscoveryJob details.""")
@cli_util.help_option_group
def discovery_job_group():
    pass


@click.command(cli_util.override('stack_monitoring.work_request_summary_collection_group.command_name', 'work-request-summary-collection'), cls=CommandGroupWithAlias, help="""Results of a workRequest search. Contains both WorkRequest items and other information, such as metadata.""")
@cli_util.help_option_group
def work_request_summary_collection_group():
    pass


@click.command(cli_util.override('stack_monitoring.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""A description of workrequest status""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('stack_monitoring.discovery_job_log_collection_group.command_name', 'discovery-job-log-collection'), cls=CommandGroupWithAlias, help="""List of logs of a job""")
@cli_util.help_option_group
def discovery_job_log_collection_group():
    pass


@click.command(cli_util.override('stack_monitoring.work_request_log_entry_collection_group.command_name', 'work-request-log-entry-collection'), cls=CommandGroupWithAlias, help="""Results of a workRequestLog search. Contains both workRequestLog items and other information, such as metadata.""")
@cli_util.help_option_group
def work_request_log_entry_collection_group():
    pass


stack_monitoring_root_group.add_command(discovery_job_collection_group)
stack_monitoring_root_group.add_command(monitored_resource_group)
stack_monitoring_root_group.add_command(work_request_error_collection_group)
stack_monitoring_root_group.add_command(discovery_job_group)
stack_monitoring_root_group.add_command(work_request_summary_collection_group)
stack_monitoring_root_group.add_command(work_request_group)
stack_monitoring_root_group.add_command(discovery_job_log_collection_group)
stack_monitoring_root_group.add_command(work_request_log_entry_collection_group)


@monitored_resource_group.command(name=cli_util.override('stack_monitoring.associate_monitored_resources.command_name', 'associate'), help=u"""Create an association between two monitored resources. \n[Command Reference](associateMonitoredResources)""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier [OCID]""")
@cli_util.option('--association-type', required=True, help=u"""Association type to be created between source and destination resources""")
@cli_util.option('--source-resource-id', required=True, help=u"""Source Monitored Resource Identifier [OCID]""")
@cli_util.option('--destination-resource-id', required=True, help=u"""Destination Monitored Resource Identifier [OCID]""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'stack_monitoring', 'class': 'MonitoredResourceAssociation'})
@cli_util.wrap_exceptions
def associate_monitored_resources(ctx, from_json, compartment_id, association_type, source_resource_id, destination_resource_id, if_match):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['associationType'] = association_type
    _details['sourceResourceId'] = source_resource_id
    _details['destinationResourceId'] = destination_resource_id

    client = cli_util.build_client('stack_monitoring', 'stack_monitoring', ctx)
    result = client.associate_monitored_resources(
        associate_monitored_resources_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@monitored_resource_group.command(name=cli_util.override('stack_monitoring.change_monitored_resource_compartment.command_name', 'change-compartment'), help=u"""Moves a MonitoredResource resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeMonitoredResourceCompartment)""")
@cli_util.option('--monitored-resource-id', required=True, help=u"""The [OCID] of monitored resource.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_monitored_resource_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, monitored_resource_id, compartment_id, if_match):

    if isinstance(monitored_resource_id, six.string_types) and len(monitored_resource_id.strip()) == 0:
        raise click.UsageError('Parameter --monitored-resource-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('stack_monitoring', 'stack_monitoring', ctx)
    result = client.change_monitored_resource_compartment(
        monitored_resource_id=monitored_resource_id,
        change_monitored_resource_compartment_details=_details,
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


@discovery_job_group.command(name=cli_util.override('stack_monitoring.create_discovery_job.command_name', 'create'), help=u"""API to create discovery Job and submit discovery Details to agent. \n[Command Reference](createDiscoveryJob)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of Compartment""")
@cli_util.option('--discovery-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--discovery-type', type=custom_types.CliCaseInsensitiveChoice(["ADD", "ADD_WITH_RETRY", "REFRESH"]), help=u"""Add option submits new discovery Job. Add with retry option to re-submit failed discovery job. Refresh option refreshes the existing discovered resources.""")
@cli_util.option('--discovery-client', help=u"""Client who submits discovery job.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'discovery-details': {'module': 'stack_monitoring', 'class': 'DiscoveryDetails'}, 'freeform-tags': {'module': 'stack_monitoring', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'stack_monitoring', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'discovery-details': {'module': 'stack_monitoring', 'class': 'DiscoveryDetails'}, 'freeform-tags': {'module': 'stack_monitoring', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'stack_monitoring', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'stack_monitoring', 'class': 'DiscoveryJob'})
@cli_util.wrap_exceptions
def create_discovery_job(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, discovery_details, discovery_type, discovery_client, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['discoveryDetails'] = cli_util.parse_json_parameter("discovery_details", discovery_details)

    if discovery_type is not None:
        _details['discoveryType'] = discovery_type

    if discovery_client is not None:
        _details['discoveryClient'] = discovery_client

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('stack_monitoring', 'stack_monitoring', ctx)
    result = client.create_discovery_job(
        create_discovery_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_discovery_job') and callable(getattr(client, 'get_discovery_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_discovery_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@monitored_resource_group.command(name=cli_util.override('stack_monitoring.create_monitored_resource.command_name', 'create'), help=u"""Creates a new monitored resource for the given resource type \n[Command Reference](createMonitoredResource)""")
@cli_util.option('--name', required=True, help=u"""Monitored resource name""")
@cli_util.option('--type', required=True, help=u"""Monitored resource type""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier [OCID]""")
@cli_util.option('--display-name', help=u"""Monitored resource display name.""")
@cli_util.option('--host-name', help=u"""Host name of the monitored resource""")
@cli_util.option('--external-id', help=u"""External resource is any OCI resource identifier [OCID] which is not a Stack Monitoring service resource. Currently supports only OCI compute instance.""")
@cli_util.option('--management-agent-id', help=u"""Management Agent Identifier [OCID].""")
@cli_util.option('--resource-time-zone', help=u"""Time zone in the form of tz database canonical zone ID.""")
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of monitored resource properties

This option is a JSON list with items of type MonitoredResourceProperty.  For documentation on MonitoredResourceProperty please see our API reference: https://docs.cloud.oracle.com/api/#/en/stackmonitoring/20210330/datatypes/MonitoredResourceProperty.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--database-connection-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--credentials', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--aliases', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--external-resource-id', help=u"""Generally used by DBaaS to send the Database OCID stored on the DBaaS. The same will be passed to resource service to enable Stack Monitoring Service on DBM. This will be stored in Stack Monitoring Resource Service data store as identifier for monitored resource. If this header is not set as part of the request, then an id will be generated and stored for the resource.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'properties': {'module': 'stack_monitoring', 'class': 'list[MonitoredResourceProperty]'}, 'database-connection-details': {'module': 'stack_monitoring', 'class': 'ConnectionDetails'}, 'credentials': {'module': 'stack_monitoring', 'class': 'MonitoredResourceCredential'}, 'aliases': {'module': 'stack_monitoring', 'class': 'MonitoredResourceAliasCredential'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'properties': {'module': 'stack_monitoring', 'class': 'list[MonitoredResourceProperty]'}, 'database-connection-details': {'module': 'stack_monitoring', 'class': 'ConnectionDetails'}, 'credentials': {'module': 'stack_monitoring', 'class': 'MonitoredResourceCredential'}, 'aliases': {'module': 'stack_monitoring', 'class': 'MonitoredResourceAliasCredential'}}, output_type={'module': 'stack_monitoring', 'class': 'MonitoredResource'})
@cli_util.wrap_exceptions
def create_monitored_resource(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, type, compartment_id, display_name, host_name, external_id, management_agent_id, resource_time_zone, properties, database_connection_details, credentials, aliases, external_resource_id):

    kwargs = {}
    if external_resource_id is not None:
        kwargs['external_resource_id'] = external_resource_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['type'] = type
    _details['compartmentId'] = compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if host_name is not None:
        _details['hostName'] = host_name

    if external_id is not None:
        _details['externalId'] = external_id

    if management_agent_id is not None:
        _details['managementAgentId'] = management_agent_id

    if resource_time_zone is not None:
        _details['resourceTimeZone'] = resource_time_zone

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    if database_connection_details is not None:
        _details['databaseConnectionDetails'] = cli_util.parse_json_parameter("database_connection_details", database_connection_details)

    if credentials is not None:
        _details['credentials'] = cli_util.parse_json_parameter("credentials", credentials)

    if aliases is not None:
        _details['aliases'] = cli_util.parse_json_parameter("aliases", aliases)

    client = cli_util.build_client('stack_monitoring', 'stack_monitoring', ctx)
    result = client.create_monitored_resource(
        create_monitored_resource_details=_details,
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


@monitored_resource_group.command(name=cli_util.override('stack_monitoring.create_monitored_resource_pre_existing_credentials.command_name', 'create-monitored-resource-pre-existing-credentials'), help=u"""Creates a new monitored resource for the given resource type \n[Command Reference](createMonitoredResource)""")
@cli_util.option('--name', required=True, help=u"""Monitored resource name""")
@cli_util.option('--type', required=True, help=u"""Monitored resource type""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier [OCID]""")
@cli_util.option('--display-name', help=u"""Monitored resource display name.""")
@cli_util.option('--host-name', help=u"""Host name of the monitored resource""")
@cli_util.option('--external-id', help=u"""External resource is any OCI resource identifier [OCID] which is not a Stack Monitoring service resource. Currently supports only OCI compute instance.""")
@cli_util.option('--management-agent-id', help=u"""Management Agent Identifier [OCID].""")
@cli_util.option('--resource-time-zone', help=u"""Time zone in the form of tz database canonical zone ID.""")
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of monitored resource properties

This option is a JSON list with items of type MonitoredResourceProperty.  For documentation on MonitoredResourceProperty please see our API reference: https://docs.cloud.oracle.com/api/#/en/stackmonitoring/20210330/datatypes/MonitoredResourceProperty.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--database-connection-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--aliases', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--external-resource-id', help=u"""Generally used by DBaaS to send the Database OCID stored on the DBaaS. The same will be passed to resource service to enable Stack Monitoring Service on DBM. This will be stored in Stack Monitoring Resource Service data store as identifier for monitored resource. If this header is not set as part of the request, then an id will be generated and stored for the resource.""")
@cli_util.option('--credentials-source', help=u"""The source type and source name combination,delimited with (.) separator. {source type}.{source name} and source type max char limit is 63.""")
@cli_util.option('--credentials-name', help=u"""The name of the credential, within the context of the source.""")
@cli_util.option('--credentials-type', help=u"""The type of the credential ( ex. JMXCreds,DBCreds).""")
@cli_util.option('--credentials-description', help=u"""The user-specified textual description of the credential.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'properties': {'module': 'stack_monitoring', 'class': 'list[MonitoredResourceProperty]'}, 'database-connection-details': {'module': 'stack_monitoring', 'class': 'ConnectionDetails'}, 'aliases': {'module': 'stack_monitoring', 'class': 'MonitoredResourceAliasCredential'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'properties': {'module': 'stack_monitoring', 'class': 'list[MonitoredResourceProperty]'}, 'database-connection-details': {'module': 'stack_monitoring', 'class': 'ConnectionDetails'}, 'aliases': {'module': 'stack_monitoring', 'class': 'MonitoredResourceAliasCredential'}}, output_type={'module': 'stack_monitoring', 'class': 'MonitoredResource'})
@cli_util.wrap_exceptions
def create_monitored_resource_pre_existing_credentials(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, type, compartment_id, display_name, host_name, external_id, management_agent_id, resource_time_zone, properties, database_connection_details, aliases, external_resource_id, credentials_source, credentials_name, credentials_type, credentials_description):

    kwargs = {}
    if external_resource_id is not None:
        kwargs['external_resource_id'] = external_resource_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['credentials'] = {}
    _details['name'] = name
    _details['type'] = type
    _details['compartmentId'] = compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if host_name is not None:
        _details['hostName'] = host_name

    if external_id is not None:
        _details['externalId'] = external_id

    if management_agent_id is not None:
        _details['managementAgentId'] = management_agent_id

    if resource_time_zone is not None:
        _details['resourceTimeZone'] = resource_time_zone

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    if database_connection_details is not None:
        _details['databaseConnectionDetails'] = cli_util.parse_json_parameter("database_connection_details", database_connection_details)

    if aliases is not None:
        _details['aliases'] = cli_util.parse_json_parameter("aliases", aliases)

    if credentials_source is not None:
        _details['credentials']['source'] = credentials_source

    if credentials_name is not None:
        _details['credentials']['name'] = credentials_name

    if credentials_type is not None:
        _details['credentials']['type'] = credentials_type

    if credentials_description is not None:
        _details['credentials']['description'] = credentials_description

    _details['credentials']['credentialType'] = 'EXISTING'

    client = cli_util.build_client('stack_monitoring', 'stack_monitoring', ctx)
    result = client.create_monitored_resource(
        create_monitored_resource_details=_details,
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


@monitored_resource_group.command(name=cli_util.override('stack_monitoring.create_monitored_resource_encrypted_credentials.command_name', 'create-monitored-resource-encrypted-credentials'), help=u"""Creates a new monitored resource for the given resource type \n[Command Reference](createMonitoredResource)""")
@cli_util.option('--name', required=True, help=u"""Monitored resource name""")
@cli_util.option('--type', required=True, help=u"""Monitored resource type""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier [OCID]""")
@cli_util.option('--credentials-key-id', required=True, help=u"""The master key OCID and applicable only for property value type ENCRYPTION. Key OCID is passed as input to Key management service decrypt API to retrieve the encrypted property value text.""")
@cli_util.option('--credentials-properties', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The credential properties list. Credential property values will be encrypted format.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Monitored resource display name.""")
@cli_util.option('--host-name', help=u"""Host name of the monitored resource""")
@cli_util.option('--external-id', help=u"""External resource is any OCI resource identifier [OCID] which is not a Stack Monitoring service resource. Currently supports only OCI compute instance.""")
@cli_util.option('--management-agent-id', help=u"""Management Agent Identifier [OCID].""")
@cli_util.option('--resource-time-zone', help=u"""Time zone in the form of tz database canonical zone ID.""")
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of monitored resource properties

This option is a JSON list with items of type MonitoredResourceProperty.  For documentation on MonitoredResourceProperty please see our API reference: https://docs.cloud.oracle.com/api/#/en/stackmonitoring/20210330/datatypes/MonitoredResourceProperty.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--database-connection-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--aliases', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--external-resource-id', help=u"""Generally used by DBaaS to send the Database OCID stored on the DBaaS. The same will be passed to resource service to enable Stack Monitoring Service on DBM. This will be stored in Stack Monitoring Resource Service data store as identifier for monitored resource. If this header is not set as part of the request, then an id will be generated and stored for the resource.""")
@cli_util.option('--credentials-source', help=u"""The source type and source name combination,delimited with (.) separator. {source type}.{source name} and source type max char limit is 63.""")
@cli_util.option('--credentials-name', help=u"""The name of the credential, within the context of the source.""")
@cli_util.option('--credentials-type', help=u"""The type of the credential ( ex. JMXCreds,DBCreds).""")
@cli_util.option('--credentials-description', help=u"""The user-specified textual description of the credential.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'properties': {'module': 'stack_monitoring', 'class': 'list[MonitoredResourceProperty]'}, 'database-connection-details': {'module': 'stack_monitoring', 'class': 'ConnectionDetails'}, 'aliases': {'module': 'stack_monitoring', 'class': 'MonitoredResourceAliasCredential'}, 'credentials-properties': {'module': 'stack_monitoring', 'class': 'list[CredentialProperty]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'properties': {'module': 'stack_monitoring', 'class': 'list[MonitoredResourceProperty]'}, 'database-connection-details': {'module': 'stack_monitoring', 'class': 'ConnectionDetails'}, 'aliases': {'module': 'stack_monitoring', 'class': 'MonitoredResourceAliasCredential'}, 'credentials-properties': {'module': 'stack_monitoring', 'class': 'list[CredentialProperty]'}}, output_type={'module': 'stack_monitoring', 'class': 'MonitoredResource'})
@cli_util.wrap_exceptions
def create_monitored_resource_encrypted_credentials(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, type, compartment_id, credentials_key_id, credentials_properties, display_name, host_name, external_id, management_agent_id, resource_time_zone, properties, database_connection_details, aliases, external_resource_id, credentials_source, credentials_name, credentials_type, credentials_description):

    kwargs = {}
    if external_resource_id is not None:
        kwargs['external_resource_id'] = external_resource_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['credentials'] = {}
    _details['name'] = name
    _details['type'] = type
    _details['compartmentId'] = compartment_id
    _details['credentials']['keyId'] = credentials_key_id
    _details['credentials']['properties'] = cli_util.parse_json_parameter("credentials_properties", credentials_properties)

    if display_name is not None:
        _details['displayName'] = display_name

    if host_name is not None:
        _details['hostName'] = host_name

    if external_id is not None:
        _details['externalId'] = external_id

    if management_agent_id is not None:
        _details['managementAgentId'] = management_agent_id

    if resource_time_zone is not None:
        _details['resourceTimeZone'] = resource_time_zone

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    if database_connection_details is not None:
        _details['databaseConnectionDetails'] = cli_util.parse_json_parameter("database_connection_details", database_connection_details)

    if aliases is not None:
        _details['aliases'] = cli_util.parse_json_parameter("aliases", aliases)

    if credentials_source is not None:
        _details['credentials']['source'] = credentials_source

    if credentials_name is not None:
        _details['credentials']['name'] = credentials_name

    if credentials_type is not None:
        _details['credentials']['type'] = credentials_type

    if credentials_description is not None:
        _details['credentials']['description'] = credentials_description

    _details['credentials']['credentialType'] = 'ENCRYPTED'

    client = cli_util.build_client('stack_monitoring', 'stack_monitoring', ctx)
    result = client.create_monitored_resource(
        create_monitored_resource_details=_details,
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


@monitored_resource_group.command(name=cli_util.override('stack_monitoring.create_monitored_resource_plain_text_credentials.command_name', 'create-monitored-resource-plain-text-credentials'), help=u"""Creates a new monitored resource for the given resource type \n[Command Reference](createMonitoredResource)""")
@cli_util.option('--name', required=True, help=u"""Monitored resource name""")
@cli_util.option('--type', required=True, help=u"""Monitored resource type""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier [OCID]""")
@cli_util.option('--credentials-properties', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The credential properties list. Credential property values will be either in plain text format.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Monitored resource display name.""")
@cli_util.option('--host-name', help=u"""Host name of the monitored resource""")
@cli_util.option('--external-id', help=u"""External resource is any OCI resource identifier [OCID] which is not a Stack Monitoring service resource. Currently supports only OCI compute instance.""")
@cli_util.option('--management-agent-id', help=u"""Management Agent Identifier [OCID].""")
@cli_util.option('--resource-time-zone', help=u"""Time zone in the form of tz database canonical zone ID.""")
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of monitored resource properties

This option is a JSON list with items of type MonitoredResourceProperty.  For documentation on MonitoredResourceProperty please see our API reference: https://docs.cloud.oracle.com/api/#/en/stackmonitoring/20210330/datatypes/MonitoredResourceProperty.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--database-connection-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--aliases', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--external-resource-id', help=u"""Generally used by DBaaS to send the Database OCID stored on the DBaaS. The same will be passed to resource service to enable Stack Monitoring Service on DBM. This will be stored in Stack Monitoring Resource Service data store as identifier for monitored resource. If this header is not set as part of the request, then an id will be generated and stored for the resource.""")
@cli_util.option('--credentials-source', help=u"""The source type and source name combination,delimited with (.) separator. {source type}.{source name} and source type max char limit is 63.""")
@cli_util.option('--credentials-name', help=u"""The name of the credential, within the context of the source.""")
@cli_util.option('--credentials-type', help=u"""The type of the credential ( ex. JMXCreds,DBCreds).""")
@cli_util.option('--credentials-description', help=u"""The user-specified textual description of the credential.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'properties': {'module': 'stack_monitoring', 'class': 'list[MonitoredResourceProperty]'}, 'database-connection-details': {'module': 'stack_monitoring', 'class': 'ConnectionDetails'}, 'aliases': {'module': 'stack_monitoring', 'class': 'MonitoredResourceAliasCredential'}, 'credentials-properties': {'module': 'stack_monitoring', 'class': 'list[CredentialProperty]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'properties': {'module': 'stack_monitoring', 'class': 'list[MonitoredResourceProperty]'}, 'database-connection-details': {'module': 'stack_monitoring', 'class': 'ConnectionDetails'}, 'aliases': {'module': 'stack_monitoring', 'class': 'MonitoredResourceAliasCredential'}, 'credentials-properties': {'module': 'stack_monitoring', 'class': 'list[CredentialProperty]'}}, output_type={'module': 'stack_monitoring', 'class': 'MonitoredResource'})
@cli_util.wrap_exceptions
def create_monitored_resource_plain_text_credentials(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, type, compartment_id, credentials_properties, display_name, host_name, external_id, management_agent_id, resource_time_zone, properties, database_connection_details, aliases, external_resource_id, credentials_source, credentials_name, credentials_type, credentials_description):

    kwargs = {}
    if external_resource_id is not None:
        kwargs['external_resource_id'] = external_resource_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['credentials'] = {}
    _details['name'] = name
    _details['type'] = type
    _details['compartmentId'] = compartment_id
    _details['credentials']['properties'] = cli_util.parse_json_parameter("credentials_properties", credentials_properties)

    if display_name is not None:
        _details['displayName'] = display_name

    if host_name is not None:
        _details['hostName'] = host_name

    if external_id is not None:
        _details['externalId'] = external_id

    if management_agent_id is not None:
        _details['managementAgentId'] = management_agent_id

    if resource_time_zone is not None:
        _details['resourceTimeZone'] = resource_time_zone

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    if database_connection_details is not None:
        _details['databaseConnectionDetails'] = cli_util.parse_json_parameter("database_connection_details", database_connection_details)

    if aliases is not None:
        _details['aliases'] = cli_util.parse_json_parameter("aliases", aliases)

    if credentials_source is not None:
        _details['credentials']['source'] = credentials_source

    if credentials_name is not None:
        _details['credentials']['name'] = credentials_name

    if credentials_type is not None:
        _details['credentials']['type'] = credentials_type

    if credentials_description is not None:
        _details['credentials']['description'] = credentials_description

    _details['credentials']['credentialType'] = 'PLAINTEXT'

    client = cli_util.build_client('stack_monitoring', 'stack_monitoring', ctx)
    result = client.create_monitored_resource(
        create_monitored_resource_details=_details,
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


@discovery_job_group.command(name=cli_util.override('stack_monitoring.delete_discovery_job.command_name', 'delete'), help=u"""Deletes a DiscoveryJob by identifier \n[Command Reference](deleteDiscoveryJob)""")
@cli_util.option('--discovery-job-id', required=True, help=u"""The Discovery Job ID""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_discovery_job(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, discovery_job_id, if_match):

    if isinstance(discovery_job_id, six.string_types) and len(discovery_job_id.strip()) == 0:
        raise click.UsageError('Parameter --discovery-job-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('stack_monitoring', 'stack_monitoring', ctx)
    result = client.delete_discovery_job(
        discovery_job_id=discovery_job_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_discovery_job') and callable(getattr(client, 'get_discovery_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_discovery_job(discovery_job_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@monitored_resource_group.command(name=cli_util.override('stack_monitoring.delete_monitored_resource.command_name', 'delete'), help=u"""Deletes a monitored resource by identifier \n[Command Reference](deleteMonitoredResource)""")
@cli_util.option('--monitored-resource-id', required=True, help=u"""The [OCID] of monitored resource.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--is-delete-members', type=click.BOOL, help=u"""A filter to delete the associated children or not for given resource.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_monitored_resource(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, monitored_resource_id, if_match, is_delete_members):

    if isinstance(monitored_resource_id, six.string_types) and len(monitored_resource_id.strip()) == 0:
        raise click.UsageError('Parameter --monitored-resource-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if is_delete_members is not None:
        kwargs['is_delete_members'] = is_delete_members
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('stack_monitoring', 'stack_monitoring', ctx)
    result = client.delete_monitored_resource(
        monitored_resource_id=monitored_resource_id,
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


@monitored_resource_group.command(name=cli_util.override('stack_monitoring.disable_external_database.command_name', 'disable-external-database'), help=u"""Disable external database resource monitoring. \n[Command Reference](disableExternalDatabase)""")
@cli_util.option('--monitored-resource-id', required=True, help=u"""The [OCID] of monitored resource.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def disable_external_database(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, monitored_resource_id, if_match):

    if isinstance(monitored_resource_id, six.string_types) and len(monitored_resource_id.strip()) == 0:
        raise click.UsageError('Parameter --monitored-resource-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('stack_monitoring', 'stack_monitoring', ctx)
    result = client.disable_external_database(
        monitored_resource_id=monitored_resource_id,
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


@monitored_resource_group.command(name=cli_util.override('stack_monitoring.disassociate_monitored_resources.command_name', 'disassociate'), help=u"""Removes associations between two monitored resources. \n[Command Reference](disassociateMonitoredResources)""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier [OCID]""")
@cli_util.option('--association-type', help=u"""Association type to be created between source and destination resources""")
@cli_util.option('--source-resource-id', help=u"""Source Monitored Resource Identifier [OCID]""")
@cli_util.option('--destination-resource-id', help=u"""Destination Monitored Resource Identifier [OCID]""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def disassociate_monitored_resources(ctx, from_json, compartment_id, association_type, source_resource_id, destination_resource_id, if_match):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    if association_type is not None:
        _details['associationType'] = association_type

    if source_resource_id is not None:
        _details['sourceResourceId'] = source_resource_id

    if destination_resource_id is not None:
        _details['destinationResourceId'] = destination_resource_id

    client = cli_util.build_client('stack_monitoring', 'stack_monitoring', ctx)
    result = client.disassociate_monitored_resources(
        disassociate_monitored_resources_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@discovery_job_group.command(name=cli_util.override('stack_monitoring.get_discovery_job.command_name', 'get'), help=u"""API to get the details of discovery Job by identifier. \n[Command Reference](getDiscoveryJob)""")
@cli_util.option('--discovery-job-id', required=True, help=u"""The Discovery Job ID""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'stack_monitoring', 'class': 'DiscoveryJob'})
@cli_util.wrap_exceptions
def get_discovery_job(ctx, from_json, discovery_job_id):

    if isinstance(discovery_job_id, six.string_types) and len(discovery_job_id.strip()) == 0:
        raise click.UsageError('Parameter --discovery-job-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('stack_monitoring', 'stack_monitoring', ctx)
    result = client.get_discovery_job(
        discovery_job_id=discovery_job_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@monitored_resource_group.command(name=cli_util.override('stack_monitoring.get_monitored_resource.command_name', 'get'), help=u"""Gets a monitored resource by identifier \n[Command Reference](getMonitoredResource)""")
@cli_util.option('--monitored-resource-id', required=True, help=u"""The [OCID] of monitored resource.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'stack_monitoring', 'class': 'MonitoredResource'})
@cli_util.wrap_exceptions
def get_monitored_resource(ctx, from_json, monitored_resource_id):

    if isinstance(monitored_resource_id, six.string_types) and len(monitored_resource_id.strip()) == 0:
        raise click.UsageError('Parameter --monitored-resource-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('stack_monitoring', 'stack_monitoring', ctx)
    result = client.get_monitored_resource(
        monitored_resource_id=monitored_resource_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('stack_monitoring.get_work_request.command_name', 'get'), help=u"""Gets the status of the work request with the given ID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the work request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'stack_monitoring', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('stack_monitoring', 'stack_monitoring', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@discovery_job_log_collection_group.command(name=cli_util.override('stack_monitoring.list_discovery_job_logs.command_name', 'list-discovery-job-logs'), help=u"""API to get all the logs of a Discovery Job. \n[Command Reference](listDiscoveryJobLogs)""")
@cli_util.option('--discovery-job-id', required=True, help=u"""The Discovery Job ID""")
@cli_util.option('--log-type', type=custom_types.CliCaseInsensitiveChoice(["INFO", "WARNING", "ERROR", "SUCCESS"]), help=u"""The log type like INFO, WARNING, ERROR, SUCCESS""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "logType"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for logType is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'stack_monitoring', 'class': 'DiscoveryJobLogCollection'})
@cli_util.wrap_exceptions
def list_discovery_job_logs(ctx, from_json, all_pages, page_size, discovery_job_id, log_type, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(discovery_job_id, six.string_types) and len(discovery_job_id.strip()) == 0:
        raise click.UsageError('Parameter --discovery-job-id cannot be whitespace or empty string')

    kwargs = {}
    if log_type is not None:
        kwargs['log_type'] = log_type
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('stack_monitoring', 'stack_monitoring', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_discovery_job_logs,
            discovery_job_id=discovery_job_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_discovery_job_logs,
            limit,
            page_size,
            discovery_job_id=discovery_job_id,
            **kwargs
        )
    else:
        result = client.list_discovery_job_logs(
            discovery_job_id=discovery_job_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@discovery_job_collection_group.command(name=cli_util.override('stack_monitoring.list_discovery_jobs.command_name', 'list-discovery-jobs'), help=u"""API to get the details of all Discovery Jobs. \n[Command Reference](listDiscoveryJobs)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which data is listed.""")
@cli_util.option('--name', help=u"""A filter to return only discovery jobs that match the entire resource name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeUpdated", "resourceName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeUpdated is descending. Default order for resourceName is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'stack_monitoring', 'class': 'DiscoveryJobCollection'})
@cli_util.wrap_exceptions
def list_discovery_jobs(ctx, from_json, all_pages, page_size, compartment_id, name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('stack_monitoring', 'stack_monitoring', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_discovery_jobs,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_discovery_jobs,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_discovery_jobs(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_collection_group.command(name=cli_util.override('stack_monitoring.list_work_request_errors.command_name', 'list-work-request-errors'), help=u"""Return a (paginated) list of errors for a given work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the work request.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timestamp"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timestamp is descending. If no value is specified timestamp is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'stack_monitoring', 'class': 'WorkRequestErrorCollection'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('stack_monitoring', 'stack_monitoring', ctx)
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


@work_request_log_entry_collection_group.command(name=cli_util.override('stack_monitoring.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Return a (paginated) list of logs for a given work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the work request.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timestamp"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timestamp is descending. If no value is specified timestamp is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'stack_monitoring', 'class': 'WorkRequestLogEntryCollection'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('stack_monitoring', 'stack_monitoring', ctx)
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


@work_request_summary_collection_group.command(name=cli_util.override('stack_monitoring.list_work_requests.command_name', 'list-work-requests'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which data is listed.""")
@cli_util.option('--work-request-id', help=u"""The ID of the asynchronous work request.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help=u"""A filter to return only resources their lifecycleState matches the given OperationStatus.""")
@cli_util.option('--resource-id', help=u"""The ID of the resource affected by the work request.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending. If no value is specified timeAccepted is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'stack_monitoring', 'class': 'WorkRequestSummaryCollection'})
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
    client = cli_util.build_client('stack_monitoring', 'stack_monitoring', ctx)
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


@monitored_resource_group.command(name=cli_util.override('stack_monitoring.search_associated_resources.command_name', 'search-associated-resources'), help=u"""List associated monitored resources. \n[Command Reference](searchAssociatedResources)""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier [OCID]""")
@cli_util.option('--resource-type', help=u"""A filter to return associated resources that match resources of type. Either resourceId or resourceType should be provided.""")
@cli_util.option('--resource-id', help=u"""Monitored resource identifier for which the associated resources should be fetched. Either resourceId or resourceType should be provided.""")
@cli_util.option('--limit-level', type=click.INT, help=u"""The field which determines the depth of hierarchy while searching for associated resources. Possible values - 0 for all levels. And positive number to indicate different levels. Default value is 1, which indicates 1st level associations.""")
@cli_util.option('--association-types', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of association types to be searched for finding associated resources""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--fields', multiple=True, help=u"""Partial response refers to an optimization technique offered by the RESTful web APIs, to return only the information (fields) required by the client. In this mechanism, the client sends the required field names as the query parameters for an API to the server, and the server trims down the default response content by removing the fields that are not required by the client. The parameter controls which fields to return and should be a query string parameter called \"fields\" of an array type, provide the values as enums, and use collectionFormat.""")
@cli_util.option('--exclude-fields', multiple=True, help=u"""Partial response refers to an optimization technique offered by the RESTful web APIs, to return all the information except the fields requested to be excluded (excludeFields) by the client. In this mechanism, the client sends the exclude field names as the query parameters for an API to the server, and the server trims down the default response content by removing the fields that are not required by the client. The parameter controls which fields to exlude and to return and should be a query string parameter called \"excludeFields\" of an array type, provide the values as enums, and use collectionFormat.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@json_skeleton_utils.get_cli_json_input_option({'association-types': {'module': 'stack_monitoring', 'class': 'list[string]'}, 'fields': {'module': 'stack_monitoring', 'class': 'list[string]'}, 'exclude-fields': {'module': 'stack_monitoring', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'association-types': {'module': 'stack_monitoring', 'class': 'list[string]'}, 'fields': {'module': 'stack_monitoring', 'class': 'list[string]'}, 'exclude-fields': {'module': 'stack_monitoring', 'class': 'list[string]'}}, output_type={'module': 'stack_monitoring', 'class': 'AssociatedResourcesCollection'})
@cli_util.wrap_exceptions
def search_associated_resources(ctx, from_json, compartment_id, resource_type, resource_id, limit_level, association_types, fields, exclude_fields, if_match, limit, page):

    kwargs = {}
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if exclude_fields is not None and len(exclude_fields) > 0:
        kwargs['exclude_fields'] = exclude_fields
    if if_match is not None:
        kwargs['if_match'] = if_match
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    if resource_type is not None:
        _details['resourceType'] = resource_type

    if resource_id is not None:
        _details['resourceId'] = resource_id

    if limit_level is not None:
        _details['limitLevel'] = limit_level

    if association_types is not None:
        _details['associationTypes'] = cli_util.parse_json_parameter("association_types", association_types)

    client = cli_util.build_client('stack_monitoring', 'stack_monitoring', ctx)
    result = client.search_associated_resources(
        search_associated_resources_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@monitored_resource_group.command(name=cli_util.override('stack_monitoring.search_monitored_resource_associations.command_name', 'search-monitored-resource-associations'), help=u"""Returns a list of monitored resource associations. \n[Command Reference](searchMonitoredResourceAssociations)""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier [OCID]""")
@cli_util.option('--source-resource-id', help=u"""Source Monitored Resource Identifier [OCID]""")
@cli_util.option('--source-resource-name', help=u"""Source Monitored Resource Name""")
@cli_util.option('--source-resource-type', help=u"""Source Monitored Resource Type""")
@cli_util.option('--destination-resource-id', help=u"""Destination Monitored Resource Identifier [OCID]""")
@cli_util.option('--destination-resource-name', help=u"""Source Monitored Resource Name""")
@cli_util.option('--destination-resource-type', help=u"""Source Monitored Resource Type""")
@cli_util.option('--association-type', help=u"""Association type to be created between source and destination resources""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "ASSOC_TYPE"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for assocType is descending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'stack_monitoring', 'class': 'MonitoredResourceAssociationsCollection'})
@cli_util.wrap_exceptions
def search_monitored_resource_associations(ctx, from_json, compartment_id, source_resource_id, source_resource_name, source_resource_type, destination_resource_id, destination_resource_name, destination_resource_type, association_type, sort_by, sort_order, limit, page, if_match):

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    if source_resource_id is not None:
        _details['sourceResourceId'] = source_resource_id

    if source_resource_name is not None:
        _details['sourceResourceName'] = source_resource_name

    if source_resource_type is not None:
        _details['sourceResourceType'] = source_resource_type

    if destination_resource_id is not None:
        _details['destinationResourceId'] = destination_resource_id

    if destination_resource_name is not None:
        _details['destinationResourceName'] = destination_resource_name

    if destination_resource_type is not None:
        _details['destinationResourceType'] = destination_resource_type

    if association_type is not None:
        _details['associationType'] = association_type

    if sort_by is not None:
        _details['sortBy'] = sort_by

    if sort_order is not None:
        _details['sortOrder'] = sort_order

    client = cli_util.build_client('stack_monitoring', 'stack_monitoring', ctx)
    result = client.search_monitored_resource_associations(
        search_monitored_resource_associations_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@monitored_resource_group.command(name=cli_util.override('stack_monitoring.search_monitored_resource_members.command_name', 'search-monitored-resource-members'), help=u"""List resources which are members of the given monitored resource \n[Command Reference](searchMonitoredResourceMembers)""")
@cli_util.option('--monitored-resource-id', required=True, help=u"""The [OCID] of monitored resource.""")
@cli_util.option('--destination-resource-id', help=u"""Destination Monitored Resource Identifier [OCID]""")
@cli_util.option('--limit-level', type=click.INT, help=u"""The field which determines the depth of hierarchy while searching for members""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["resourceName", "resourceType", "sourceResourceType"]), help=u"""If this query parameter is specified, the result is sorted by this query parameter value.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'stack_monitoring', 'class': 'MonitoredResourceMembersCollection'})
@cli_util.wrap_exceptions
def search_monitored_resource_members(ctx, from_json, monitored_resource_id, destination_resource_id, limit_level, sort_by, sort_order, page, limit, if_match):

    if isinstance(monitored_resource_id, six.string_types) and len(monitored_resource_id.strip()) == 0:
        raise click.UsageError('Parameter --monitored-resource-id cannot be whitespace or empty string')

    kwargs = {}
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if destination_resource_id is not None:
        _details['destinationResourceId'] = destination_resource_id

    if limit_level is not None:
        _details['limitLevel'] = limit_level

    client = cli_util.build_client('stack_monitoring', 'stack_monitoring', ctx)
    result = client.search_monitored_resource_members(
        monitored_resource_id=monitored_resource_id,
        search_monitored_resource_members_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@monitored_resource_group.command(name=cli_util.override('stack_monitoring.search_monitored_resources.command_name', 'search'), help=u"""Returns a list of monitored resources. \n[Command Reference](searchMonitoredResources)""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier [OCID]""")
@cli_util.option('--name', help=u"""A filter to return resources that match exact resource name""")
@cli_util.option('--name-contains', help=u"""A filter to return resources that match resource name pattern given. The match is not case sensitive.""")
@cli_util.option('--type', help=u"""A filter to return resources that match resource type""")
@cli_util.option('--host-name', help=u"""A filter to return resources with host name match""")
@cli_util.option('--external-id', help=u"""External resource is any OCI resource identifier [OCID] which is not a Stack Monitoring service resource. Currently supports only following resource type identifiers - externalcontainerdatabase, externalnoncontainerdatabase, externalpluggabledatabase and OCI compute instance.""")
@cli_util.option('--host-name-contains', help=u"""A filter to return resources with host name pattern""")
@cli_util.option('--management-agent-id', help=u"""A filter to return resources with matching management agent id.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return resources with matching lifecycle state.""")
@cli_util.option('--time-created-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""Search for resources that were created within a specific date range, using this parameter to specify the earliest creation date for the returned list (inclusive). Specifying this parameter without the corresponding `timeCreatedLessThan` parameter will retrieve resources created from the given `timeCreatedGreaterThanOrEqualTo` to the current time, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by [RFC 3339].

**Example:** 2016-12-19T16:39:57.600Z""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-created-less-than', type=custom_types.CLI_DATETIME, help=u"""Search for resources that were created within a specific date range, using this parameter to specify the latest creation date for the returned list (exclusive). Specifying this parameter without the corresponding `timeCreatedGreaterThanOrEqualTo` parameter will retrieve all resources created before the specified end date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by [RFC 3339].

**Example:** 2016-12-19T16:39:57.600Z""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-updated-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""Search for resources that were updated within a specific date range, using this parameter to specify the earliest update date for the returned list (inclusive). Specifying this parameter without the corresponding `timeUpdatedLessThan` parameter will retrieve resources updated from the given `timeUpdatedGreaterThanOrEqualTo` to the current time, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by [RFC 3339].

**Example:** 2016-12-19T16:39:57.600Z""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-updated-less-than', type=custom_types.CLI_DATETIME, help=u"""Search for resources that were updated within a specific date range, using this parameter to specify the latest creation date for the returned list (exclusive). Specifying this parameter without the corresponding `timeUpdatedGreaterThanOrEqualTo` parameter will retrieve all resources updated before the specified end date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by [RFC 3339].

**Example:** 2016-12-19T16:39:57.600Z""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--resource-time-zone', help=u"""Time zone in the form of tz database canonical zone ID.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "RESOURCE_NAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for resources is ascending.""")
@cli_util.option('--property-equals', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Criteria based on resource property.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--fields', multiple=True, help=u"""Partial response refers to an optimization technique offered by the RESTful web APIs, to return only the information (fields) required by the client. In this mechanism, the client sends the required field names as the query parameters for an API to the server, and the server trims down the default response content by removing the fields that are not required by the client. The parameter controls which fields to return and should be a query string parameter called \"fields\" of an array type, provide the values as enums, and use collectionFormat.""")
@cli_util.option('--exclude-fields', multiple=True, help=u"""Partial response refers to an optimization technique offered by the RESTful web APIs, to return all the information except the fields requested to be excluded (excludeFields) by the client. In this mechanism, the client sends the exclude field names as the query parameters for an API to the server, and the server trims down the default response content by removing the fields that are not required by the client. The parameter controls which fields to exlude and to return and should be a query string parameter called \"excludeFields\" of an array type, provide the values as enums, and use collectionFormat.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'property-equals': {'module': 'stack_monitoring', 'class': 'dict(str, string)'}, 'fields': {'module': 'stack_monitoring', 'class': 'list[string]'}, 'exclude-fields': {'module': 'stack_monitoring', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'property-equals': {'module': 'stack_monitoring', 'class': 'dict(str, string)'}, 'fields': {'module': 'stack_monitoring', 'class': 'list[string]'}, 'exclude-fields': {'module': 'stack_monitoring', 'class': 'list[string]'}}, output_type={'module': 'stack_monitoring', 'class': 'MonitoredResourceCollection'})
@cli_util.wrap_exceptions
def search_monitored_resources(ctx, from_json, compartment_id, name, name_contains, type, host_name, external_id, host_name_contains, management_agent_id, lifecycle_state, time_created_greater_than_or_equal_to, time_created_less_than, time_updated_greater_than_or_equal_to, time_updated_less_than, resource_time_zone, sort_order, sort_by, property_equals, limit, page, fields, exclude_fields, if_match):

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if exclude_fields is not None and len(exclude_fields) > 0:
        kwargs['exclude_fields'] = exclude_fields
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    if name is not None:
        _details['name'] = name

    if name_contains is not None:
        _details['nameContains'] = name_contains

    if type is not None:
        _details['type'] = type

    if host_name is not None:
        _details['hostName'] = host_name

    if external_id is not None:
        _details['externalId'] = external_id

    if host_name_contains is not None:
        _details['hostNameContains'] = host_name_contains

    if management_agent_id is not None:
        _details['managementAgentId'] = management_agent_id

    if lifecycle_state is not None:
        _details['lifecycleState'] = lifecycle_state

    if time_created_greater_than_or_equal_to is not None:
        _details['timeCreatedGreaterThanOrEqualTo'] = time_created_greater_than_or_equal_to

    if time_created_less_than is not None:
        _details['timeCreatedLessThan'] = time_created_less_than

    if time_updated_greater_than_or_equal_to is not None:
        _details['timeUpdatedGreaterThanOrEqualTo'] = time_updated_greater_than_or_equal_to

    if time_updated_less_than is not None:
        _details['timeUpdatedLessThan'] = time_updated_less_than

    if resource_time_zone is not None:
        _details['resourceTimeZone'] = resource_time_zone

    if sort_order is not None:
        _details['sortOrder'] = sort_order

    if sort_by is not None:
        _details['sortBy'] = sort_by

    if property_equals is not None:
        _details['propertyEquals'] = cli_util.parse_json_parameter("property_equals", property_equals)

    client = cli_util.build_client('stack_monitoring', 'stack_monitoring', ctx)
    result = client.search_monitored_resources(
        search_monitored_resources_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@monitored_resource_group.command(name=cli_util.override('stack_monitoring.update_monitored_resource.command_name', 'update'), help=u"""Updates the Monitored Resource \n[Command Reference](updateMonitoredResource)""")
@cli_util.option('--monitored-resource-id', required=True, help=u"""The [OCID] of monitored resource.""")
@cli_util.option('--display-name', help=u"""Monitored resource display name.""")
@cli_util.option('--host-name', help=u"""Host name of the monitored resource""")
@cli_util.option('--resource-time-zone', help=u"""Time zone in the form of tz database canonical zone ID.""")
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of monitored resource properties

This option is a JSON list with items of type MonitoredResourceProperty.  For documentation on MonitoredResourceProperty please see our API reference: https://docs.cloud.oracle.com/api/#/en/stackmonitoring/20210330/datatypes/MonitoredResourceProperty.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--database-connection-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--credentials', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--aliases', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'properties': {'module': 'stack_monitoring', 'class': 'list[MonitoredResourceProperty]'}, 'database-connection-details': {'module': 'stack_monitoring', 'class': 'ConnectionDetails'}, 'credentials': {'module': 'stack_monitoring', 'class': 'MonitoredResourceCredential'}, 'aliases': {'module': 'stack_monitoring', 'class': 'MonitoredResourceAliasCredential'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'properties': {'module': 'stack_monitoring', 'class': 'list[MonitoredResourceProperty]'}, 'database-connection-details': {'module': 'stack_monitoring', 'class': 'ConnectionDetails'}, 'credentials': {'module': 'stack_monitoring', 'class': 'MonitoredResourceCredential'}, 'aliases': {'module': 'stack_monitoring', 'class': 'MonitoredResourceAliasCredential'}})
@cli_util.wrap_exceptions
def update_monitored_resource(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, monitored_resource_id, display_name, host_name, resource_time_zone, properties, database_connection_details, credentials, aliases, if_match):

    if isinstance(monitored_resource_id, six.string_types) and len(monitored_resource_id.strip()) == 0:
        raise click.UsageError('Parameter --monitored-resource-id cannot be whitespace or empty string')
    if not force:
        if properties or database_connection_details or credentials or aliases:
            if not click.confirm("WARNING: Updates to properties and database-connection-details and credentials and aliases will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if host_name is not None:
        _details['hostName'] = host_name

    if resource_time_zone is not None:
        _details['resourceTimeZone'] = resource_time_zone

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    if database_connection_details is not None:
        _details['databaseConnectionDetails'] = cli_util.parse_json_parameter("database_connection_details", database_connection_details)

    if credentials is not None:
        _details['credentials'] = cli_util.parse_json_parameter("credentials", credentials)

    if aliases is not None:
        _details['aliases'] = cli_util.parse_json_parameter("aliases", aliases)

    client = cli_util.build_client('stack_monitoring', 'stack_monitoring', ctx)
    result = client.update_monitored_resource(
        monitored_resource_id=monitored_resource_id,
        update_monitored_resource_details=_details,
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


@monitored_resource_group.command(name=cli_util.override('stack_monitoring.update_monitored_resource_pre_existing_credentials.command_name', 'update-monitored-resource-pre-existing-credentials'), help=u"""Updates the Monitored Resource \n[Command Reference](updateMonitoredResource)""")
@cli_util.option('--monitored-resource-id', required=True, help=u"""The [OCID] of monitored resource.""")
@cli_util.option('--display-name', help=u"""Monitored resource display name.""")
@cli_util.option('--host-name', help=u"""Host name of the monitored resource""")
@cli_util.option('--resource-time-zone', help=u"""Time zone in the form of tz database canonical zone ID.""")
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of monitored resource properties

This option is a JSON list with items of type MonitoredResourceProperty.  For documentation on MonitoredResourceProperty please see our API reference: https://docs.cloud.oracle.com/api/#/en/stackmonitoring/20210330/datatypes/MonitoredResourceProperty.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--database-connection-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--aliases', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--credentials-source', help=u"""The source type and source name combination,delimited with (.) separator. {source type}.{source name} and source type max char limit is 63.""")
@cli_util.option('--credentials-name', help=u"""The name of the credential, within the context of the source.""")
@cli_util.option('--credentials-type', help=u"""The type of the credential ( ex. JMXCreds,DBCreds).""")
@cli_util.option('--credentials-description', help=u"""The user-specified textual description of the credential.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'properties': {'module': 'stack_monitoring', 'class': 'list[MonitoredResourceProperty]'}, 'database-connection-details': {'module': 'stack_monitoring', 'class': 'ConnectionDetails'}, 'aliases': {'module': 'stack_monitoring', 'class': 'MonitoredResourceAliasCredential'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'properties': {'module': 'stack_monitoring', 'class': 'list[MonitoredResourceProperty]'}, 'database-connection-details': {'module': 'stack_monitoring', 'class': 'ConnectionDetails'}, 'aliases': {'module': 'stack_monitoring', 'class': 'MonitoredResourceAliasCredential'}})
@cli_util.wrap_exceptions
def update_monitored_resource_pre_existing_credentials(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, monitored_resource_id, display_name, host_name, resource_time_zone, properties, database_connection_details, aliases, if_match, credentials_source, credentials_name, credentials_type, credentials_description):

    if isinstance(monitored_resource_id, six.string_types) and len(monitored_resource_id.strip()) == 0:
        raise click.UsageError('Parameter --monitored-resource-id cannot be whitespace or empty string')
    if not force:
        if properties or database_connection_details or aliases:
            if not click.confirm("WARNING: Updates to properties and database-connection-details and aliases will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['credentials'] = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if host_name is not None:
        _details['hostName'] = host_name

    if resource_time_zone is not None:
        _details['resourceTimeZone'] = resource_time_zone

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    if database_connection_details is not None:
        _details['databaseConnectionDetails'] = cli_util.parse_json_parameter("database_connection_details", database_connection_details)

    if aliases is not None:
        _details['aliases'] = cli_util.parse_json_parameter("aliases", aliases)

    if credentials_source is not None:
        _details['credentials']['source'] = credentials_source

    if credentials_name is not None:
        _details['credentials']['name'] = credentials_name

    if credentials_type is not None:
        _details['credentials']['type'] = credentials_type

    if credentials_description is not None:
        _details['credentials']['description'] = credentials_description

    _details['credentials']['credentialType'] = 'EXISTING'

    client = cli_util.build_client('stack_monitoring', 'stack_monitoring', ctx)
    result = client.update_monitored_resource(
        monitored_resource_id=monitored_resource_id,
        update_monitored_resource_details=_details,
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


@monitored_resource_group.command(name=cli_util.override('stack_monitoring.update_monitored_resource_encrypted_credentials.command_name', 'update-monitored-resource-encrypted-credentials'), help=u"""Updates the Monitored Resource \n[Command Reference](updateMonitoredResource)""")
@cli_util.option('--monitored-resource-id', required=True, help=u"""The [OCID] of monitored resource.""")
@cli_util.option('--credentials-key-id', required=True, help=u"""The master key OCID and applicable only for property value type ENCRYPTION. Key OCID is passed as input to Key management service decrypt API to retrieve the encrypted property value text.""")
@cli_util.option('--credentials-properties', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The credential properties list. Credential property values will be encrypted format.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Monitored resource display name.""")
@cli_util.option('--host-name', help=u"""Host name of the monitored resource""")
@cli_util.option('--resource-time-zone', help=u"""Time zone in the form of tz database canonical zone ID.""")
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of monitored resource properties

This option is a JSON list with items of type MonitoredResourceProperty.  For documentation on MonitoredResourceProperty please see our API reference: https://docs.cloud.oracle.com/api/#/en/stackmonitoring/20210330/datatypes/MonitoredResourceProperty.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--database-connection-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--aliases', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--credentials-source', help=u"""The source type and source name combination,delimited with (.) separator. {source type}.{source name} and source type max char limit is 63.""")
@cli_util.option('--credentials-name', help=u"""The name of the credential, within the context of the source.""")
@cli_util.option('--credentials-type', help=u"""The type of the credential ( ex. JMXCreds,DBCreds).""")
@cli_util.option('--credentials-description', help=u"""The user-specified textual description of the credential.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'properties': {'module': 'stack_monitoring', 'class': 'list[MonitoredResourceProperty]'}, 'database-connection-details': {'module': 'stack_monitoring', 'class': 'ConnectionDetails'}, 'aliases': {'module': 'stack_monitoring', 'class': 'MonitoredResourceAliasCredential'}, 'credentials-properties': {'module': 'stack_monitoring', 'class': 'list[CredentialProperty]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'properties': {'module': 'stack_monitoring', 'class': 'list[MonitoredResourceProperty]'}, 'database-connection-details': {'module': 'stack_monitoring', 'class': 'ConnectionDetails'}, 'aliases': {'module': 'stack_monitoring', 'class': 'MonitoredResourceAliasCredential'}, 'credentials-properties': {'module': 'stack_monitoring', 'class': 'list[CredentialProperty]'}})
@cli_util.wrap_exceptions
def update_monitored_resource_encrypted_credentials(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, monitored_resource_id, credentials_key_id, credentials_properties, display_name, host_name, resource_time_zone, properties, database_connection_details, aliases, if_match, credentials_source, credentials_name, credentials_type, credentials_description):

    if isinstance(monitored_resource_id, six.string_types) and len(monitored_resource_id.strip()) == 0:
        raise click.UsageError('Parameter --monitored-resource-id cannot be whitespace or empty string')
    if not force:
        if properties or database_connection_details or aliases:
            if not click.confirm("WARNING: Updates to properties and database-connection-details and aliases will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['credentials'] = {}
    _details['credentials']['keyId'] = credentials_key_id
    _details['credentials']['properties'] = cli_util.parse_json_parameter("credentials_properties", credentials_properties)

    if display_name is not None:
        _details['displayName'] = display_name

    if host_name is not None:
        _details['hostName'] = host_name

    if resource_time_zone is not None:
        _details['resourceTimeZone'] = resource_time_zone

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    if database_connection_details is not None:
        _details['databaseConnectionDetails'] = cli_util.parse_json_parameter("database_connection_details", database_connection_details)

    if aliases is not None:
        _details['aliases'] = cli_util.parse_json_parameter("aliases", aliases)

    if credentials_source is not None:
        _details['credentials']['source'] = credentials_source

    if credentials_name is not None:
        _details['credentials']['name'] = credentials_name

    if credentials_type is not None:
        _details['credentials']['type'] = credentials_type

    if credentials_description is not None:
        _details['credentials']['description'] = credentials_description

    _details['credentials']['credentialType'] = 'ENCRYPTED'

    client = cli_util.build_client('stack_monitoring', 'stack_monitoring', ctx)
    result = client.update_monitored_resource(
        monitored_resource_id=monitored_resource_id,
        update_monitored_resource_details=_details,
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


@monitored_resource_group.command(name=cli_util.override('stack_monitoring.update_monitored_resource_plain_text_credentials.command_name', 'update-monitored-resource-plain-text-credentials'), help=u"""Updates the Monitored Resource \n[Command Reference](updateMonitoredResource)""")
@cli_util.option('--monitored-resource-id', required=True, help=u"""The [OCID] of monitored resource.""")
@cli_util.option('--credentials-properties', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The credential properties list. Credential property values will be either in plain text format.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Monitored resource display name.""")
@cli_util.option('--host-name', help=u"""Host name of the monitored resource""")
@cli_util.option('--resource-time-zone', help=u"""Time zone in the form of tz database canonical zone ID.""")
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of monitored resource properties

This option is a JSON list with items of type MonitoredResourceProperty.  For documentation on MonitoredResourceProperty please see our API reference: https://docs.cloud.oracle.com/api/#/en/stackmonitoring/20210330/datatypes/MonitoredResourceProperty.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--database-connection-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--aliases', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--credentials-source', help=u"""The source type and source name combination,delimited with (.) separator. {source type}.{source name} and source type max char limit is 63.""")
@cli_util.option('--credentials-name', help=u"""The name of the credential, within the context of the source.""")
@cli_util.option('--credentials-type', help=u"""The type of the credential ( ex. JMXCreds,DBCreds).""")
@cli_util.option('--credentials-description', help=u"""The user-specified textual description of the credential.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'properties': {'module': 'stack_monitoring', 'class': 'list[MonitoredResourceProperty]'}, 'database-connection-details': {'module': 'stack_monitoring', 'class': 'ConnectionDetails'}, 'aliases': {'module': 'stack_monitoring', 'class': 'MonitoredResourceAliasCredential'}, 'credentials-properties': {'module': 'stack_monitoring', 'class': 'list[CredentialProperty]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'properties': {'module': 'stack_monitoring', 'class': 'list[MonitoredResourceProperty]'}, 'database-connection-details': {'module': 'stack_monitoring', 'class': 'ConnectionDetails'}, 'aliases': {'module': 'stack_monitoring', 'class': 'MonitoredResourceAliasCredential'}, 'credentials-properties': {'module': 'stack_monitoring', 'class': 'list[CredentialProperty]'}})
@cli_util.wrap_exceptions
def update_monitored_resource_plain_text_credentials(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, monitored_resource_id, credentials_properties, display_name, host_name, resource_time_zone, properties, database_connection_details, aliases, if_match, credentials_source, credentials_name, credentials_type, credentials_description):

    if isinstance(monitored_resource_id, six.string_types) and len(monitored_resource_id.strip()) == 0:
        raise click.UsageError('Parameter --monitored-resource-id cannot be whitespace or empty string')
    if not force:
        if properties or database_connection_details or aliases:
            if not click.confirm("WARNING: Updates to properties and database-connection-details and aliases will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['credentials'] = {}
    _details['credentials']['properties'] = cli_util.parse_json_parameter("credentials_properties", credentials_properties)

    if display_name is not None:
        _details['displayName'] = display_name

    if host_name is not None:
        _details['hostName'] = host_name

    if resource_time_zone is not None:
        _details['resourceTimeZone'] = resource_time_zone

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    if database_connection_details is not None:
        _details['databaseConnectionDetails'] = cli_util.parse_json_parameter("database_connection_details", database_connection_details)

    if aliases is not None:
        _details['aliases'] = cli_util.parse_json_parameter("aliases", aliases)

    if credentials_source is not None:
        _details['credentials']['source'] = credentials_source

    if credentials_name is not None:
        _details['credentials']['name'] = credentials_name

    if credentials_type is not None:
        _details['credentials']['type'] = credentials_type

    if credentials_description is not None:
        _details['credentials']['description'] = credentials_description

    _details['credentials']['credentialType'] = 'PLAINTEXT'

    client = cli_util.build_client('stack_monitoring', 'stack_monitoring', ctx)
    result = client.update_monitored_resource(
        monitored_resource_id=monitored_resource_id,
        update_monitored_resource_details=_details,
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
