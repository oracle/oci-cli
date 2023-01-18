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


@cli.command(cli_util.override('analytics.analytics_root_group.command_name', 'analytics'), cls=CommandGroupWithAlias, help=cli_util.override('analytics.analytics_root_group.help', """Analytics API."""), short_help=cli_util.override('analytics.analytics_root_group.short_help', """Analytics API"""))
@cli_util.help_option_group
def analytics_root_group():
    pass


@click.command(cli_util.override('analytics.work_request_log_group.command_name', 'work-request-log'), cls=CommandGroupWithAlias, help="""Log entries related to a specific work request.""")
@cli_util.help_option_group
def work_request_log_group():
    pass


@click.command(cli_util.override('analytics.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""Error encountered during the execution of a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('analytics.analytics_instance_group.command_name', 'analytics-instance'), cls=CommandGroupWithAlias, help="""Analytics Instance metadata.""")
@cli_util.help_option_group
def analytics_instance_group():
    pass


@click.command(cli_util.override('analytics.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""An asynchronous work request.""")
@cli_util.help_option_group
def work_request_group():
    pass


analytics_root_group.add_command(work_request_log_group)
analytics_root_group.add_command(work_request_error_group)
analytics_root_group.add_command(analytics_instance_group)
analytics_root_group.add_command(work_request_group)


@analytics_instance_group.command(name=cli_util.override('analytics.change_analytics_instance_compartment.command_name', 'change-compartment'), help=u"""Change the compartment of an Analytics instance. The operation is long-running and creates a new WorkRequest. \n[Command Reference](changeAnalyticsInstanceCompartment)""")
@cli_util.option('--analytics-instance-id', required=True, help=u"""The OCID of the AnalyticsInstance.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the new compartment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_analytics_instance_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, analytics_instance_id, compartment_id, if_match):

    if isinstance(analytics_instance_id, six.string_types) and len(analytics_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --analytics-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('analytics', 'analytics', ctx)
    result = client.change_analytics_instance_compartment(
        analytics_instance_id=analytics_instance_id,
        change_compartment_details=_details,
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


@analytics_instance_group.command(name=cli_util.override('analytics.change_analytics_instance_network_endpoint.command_name', 'change-analytics-instance-network-endpoint'), help=u"""Change an Analytics instance network endpoint. The operation is long-running and creates a new WorkRequest. \n[Command Reference](changeAnalyticsInstanceNetworkEndpoint)""")
@cli_util.option('--analytics-instance-id', required=True, help=u"""The OCID of the AnalyticsInstance.""")
@cli_util.option('--network-endpoint-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'network-endpoint-details': {'module': 'analytics', 'class': 'NetworkEndpointDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'network-endpoint-details': {'module': 'analytics', 'class': 'NetworkEndpointDetails'}})
@cli_util.wrap_exceptions
def change_analytics_instance_network_endpoint(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, analytics_instance_id, network_endpoint_details, if_match):

    if isinstance(analytics_instance_id, six.string_types) and len(analytics_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --analytics-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['networkEndpointDetails'] = cli_util.parse_json_parameter("network_endpoint_details", network_endpoint_details)

    client = cli_util.build_client('analytics', 'analytics', ctx)
    result = client.change_analytics_instance_network_endpoint(
        analytics_instance_id=analytics_instance_id,
        change_analytics_instance_network_endpoint_details=_details,
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


@analytics_instance_group.command(name=cli_util.override('analytics.change_analytics_instance_network_endpoint_private_endpoint_details.command_name', 'change-analytics-instance-network-endpoint-private-endpoint-details'), help=u"""Change an Analytics instance network endpoint. The operation is long-running and creates a new WorkRequest. \n[Command Reference](changeAnalyticsInstanceNetworkEndpoint)""")
@cli_util.option('--analytics-instance-id', required=True, help=u"""The OCID of the AnalyticsInstance.""")
@cli_util.option('--network-endpoint-details-vcn-id', required=True, help=u"""The VCN OCID for the private endpoint.""")
@cli_util.option('--network-endpoint-details-subnet-id', required=True, help=u"""The subnet OCID for the private endpoint.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--network-endpoint-details-network-security-group-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Network Security Group OCIDs for an Analytics instance.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'network-endpoint-details-network-security-group-ids': {'module': 'analytics', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'network-endpoint-details-network-security-group-ids': {'module': 'analytics', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def change_analytics_instance_network_endpoint_private_endpoint_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, analytics_instance_id, network_endpoint_details_vcn_id, network_endpoint_details_subnet_id, if_match, network_endpoint_details_network_security_group_ids):

    if isinstance(analytics_instance_id, six.string_types) and len(analytics_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --analytics-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['networkEndpointDetails'] = {}
    _details['networkEndpointDetails']['vcnId'] = network_endpoint_details_vcn_id
    _details['networkEndpointDetails']['subnetId'] = network_endpoint_details_subnet_id

    if network_endpoint_details_network_security_group_ids is not None:
        _details['networkEndpointDetails']['networkSecurityGroupIds'] = cli_util.parse_json_parameter("network_endpoint_details_network_security_group_ids", network_endpoint_details_network_security_group_ids)

    _details['networkEndpointDetails']['networkEndpointType'] = 'PRIVATE'

    client = cli_util.build_client('analytics', 'analytics', ctx)
    result = client.change_analytics_instance_network_endpoint(
        analytics_instance_id=analytics_instance_id,
        change_analytics_instance_network_endpoint_details=_details,
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


@analytics_instance_group.command(name=cli_util.override('analytics.change_analytics_instance_network_endpoint_public_endpoint_details.command_name', 'change-analytics-instance-network-endpoint-public-endpoint-details'), help=u"""Change an Analytics instance network endpoint. The operation is long-running and creates a new WorkRequest. \n[Command Reference](changeAnalyticsInstanceNetworkEndpoint)""")
@cli_util.option('--analytics-instance-id', required=True, help=u"""The OCID of the AnalyticsInstance.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--network-endpoint-details-whitelisted-ips', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Source IP addresses or IP address ranges in ingress rules.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--network-endpoint-details-whitelisted-vcns', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Virtual Cloud Networks allowed to access this network endpoint.

This option is a JSON list with items of type VirtualCloudNetwork.  For documentation on VirtualCloudNetwork please see our API reference: https://docs.cloud.oracle.com/api/#/en/analytics/20190331/datatypes/VirtualCloudNetwork.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--network-endpoint-details-whitelisted-services', type=custom_types.CliCaseInsensitiveChoice(["ALL"]), help=u"""Oracle Cloud Services that are allowed to access this Analytics instance.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'network-endpoint-details-whitelisted-ips': {'module': 'analytics', 'class': 'list[string]'}, 'network-endpoint-details-whitelisted-vcns': {'module': 'analytics', 'class': 'list[VirtualCloudNetwork]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'network-endpoint-details-whitelisted-ips': {'module': 'analytics', 'class': 'list[string]'}, 'network-endpoint-details-whitelisted-vcns': {'module': 'analytics', 'class': 'list[VirtualCloudNetwork]'}})
@cli_util.wrap_exceptions
def change_analytics_instance_network_endpoint_public_endpoint_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, analytics_instance_id, if_match, network_endpoint_details_whitelisted_ips, network_endpoint_details_whitelisted_vcns, network_endpoint_details_whitelisted_services):

    if isinstance(analytics_instance_id, six.string_types) and len(analytics_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --analytics-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['networkEndpointDetails'] = {}

    if network_endpoint_details_whitelisted_ips is not None:
        _details['networkEndpointDetails']['whitelistedIps'] = cli_util.parse_json_parameter("network_endpoint_details_whitelisted_ips", network_endpoint_details_whitelisted_ips)

    if network_endpoint_details_whitelisted_vcns is not None:
        _details['networkEndpointDetails']['whitelistedVcns'] = cli_util.parse_json_parameter("network_endpoint_details_whitelisted_vcns", network_endpoint_details_whitelisted_vcns)

    if network_endpoint_details_whitelisted_services is not None:
        _details['networkEndpointDetails']['whitelistedServices'] = cli_util.parse_json_parameter("network_endpoint_details_whitelisted_services", network_endpoint_details_whitelisted_services)

    _details['networkEndpointDetails']['networkEndpointType'] = 'PUBLIC'

    client = cli_util.build_client('analytics', 'analytics', ctx)
    result = client.change_analytics_instance_network_endpoint(
        analytics_instance_id=analytics_instance_id,
        change_analytics_instance_network_endpoint_details=_details,
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


@analytics_instance_group.command(name=cli_util.override('analytics.create_analytics_instance.command_name', 'create'), help=u"""Create a new AnalyticsInstance in the specified compartment. The operation is long-running and creates a new WorkRequest. \n[Command Reference](createAnalyticsInstance)""")
@cli_util.option('--name', required=True, help=u"""The name of the Analytics instance. This name must be unique in the tenancy and cannot be changed.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--feature-set', required=True, type=custom_types.CliCaseInsensitiveChoice(["SELF_SERVICE_ANALYTICS", "ENTERPRISE_ANALYTICS"]), help=u"""Analytics feature set.""")
@cli_util.option('--capacity', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--license-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]), help=u"""The license used for the service.""")
@cli_util.option('--description', help=u"""Optional description.""")
@cli_util.option('--email-notification', help=u"""Email address receiving notifications.""")
@cli_util.option('--network-endpoint-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--idcs-access-token', help=u"""IDCS access token identifying a stripe and service administrator user.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--kms-key-id', help=u"""The [OCID] of the OCI Vault Key encrypting the customer data stored in this Analytics instance. A null value indicates Oracle managed default encryption.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'capacity': {'module': 'analytics', 'class': 'Capacity'}, 'network-endpoint-details': {'module': 'analytics', 'class': 'NetworkEndpointDetails'}, 'defined-tags': {'module': 'analytics', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'analytics', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'capacity': {'module': 'analytics', 'class': 'Capacity'}, 'network-endpoint-details': {'module': 'analytics', 'class': 'NetworkEndpointDetails'}, 'defined-tags': {'module': 'analytics', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'analytics', 'class': 'dict(str, string)'}}, output_type={'module': 'analytics', 'class': 'AnalyticsInstance'})
@cli_util.wrap_exceptions
def create_analytics_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, compartment_id, feature_set, capacity, license_type, description, email_notification, network_endpoint_details, idcs_access_token, defined_tags, freeform_tags, kms_key_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['compartmentId'] = compartment_id
    _details['featureSet'] = feature_set
    _details['capacity'] = cli_util.parse_json_parameter("capacity", capacity)
    _details['licenseType'] = license_type

    if description is not None:
        _details['description'] = description

    if email_notification is not None:
        _details['emailNotification'] = email_notification

    if network_endpoint_details is not None:
        _details['networkEndpointDetails'] = cli_util.parse_json_parameter("network_endpoint_details", network_endpoint_details)

    if idcs_access_token is not None:
        _details['idcsAccessToken'] = idcs_access_token

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if kms_key_id is not None:
        _details['kmsKeyId'] = kms_key_id

    client = cli_util.build_client('analytics', 'analytics', ctx)
    result = client.create_analytics_instance(
        create_analytics_instance_details=_details,
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


@analytics_instance_group.command(name=cli_util.override('analytics.create_analytics_instance_private_endpoint_details.command_name', 'create-analytics-instance-private-endpoint-details'), help=u"""Create a new AnalyticsInstance in the specified compartment. The operation is long-running and creates a new WorkRequest. \n[Command Reference](createAnalyticsInstance)""")
@cli_util.option('--name', required=True, help=u"""The name of the Analytics instance. This name must be unique in the tenancy and cannot be changed.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--feature-set', required=True, type=custom_types.CliCaseInsensitiveChoice(["SELF_SERVICE_ANALYTICS", "ENTERPRISE_ANALYTICS"]), help=u"""Analytics feature set.""")
@cli_util.option('--capacity', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--license-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]), help=u"""The license used for the service.""")
@cli_util.option('--network-endpoint-details-vcn-id', required=True, help=u"""The VCN OCID for the private endpoint.""")
@cli_util.option('--network-endpoint-details-subnet-id', required=True, help=u"""The subnet OCID for the private endpoint.""")
@cli_util.option('--description', help=u"""Optional description.""")
@cli_util.option('--email-notification', help=u"""Email address receiving notifications.""")
@cli_util.option('--idcs-access-token', help=u"""IDCS access token identifying a stripe and service administrator user.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--kms-key-id', help=u"""The [OCID] of the OCI Vault Key encrypting the customer data stored in this Analytics instance. A null value indicates Oracle managed default encryption.""")
@cli_util.option('--network-endpoint-details-network-security-group-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Network Security Group OCIDs for an Analytics instance.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'capacity': {'module': 'analytics', 'class': 'Capacity'}, 'defined-tags': {'module': 'analytics', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'analytics', 'class': 'dict(str, string)'}, 'network-endpoint-details-network-security-group-ids': {'module': 'analytics', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'capacity': {'module': 'analytics', 'class': 'Capacity'}, 'defined-tags': {'module': 'analytics', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'analytics', 'class': 'dict(str, string)'}, 'network-endpoint-details-network-security-group-ids': {'module': 'analytics', 'class': 'list[string]'}}, output_type={'module': 'analytics', 'class': 'AnalyticsInstance'})
@cli_util.wrap_exceptions
def create_analytics_instance_private_endpoint_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, compartment_id, feature_set, capacity, license_type, network_endpoint_details_vcn_id, network_endpoint_details_subnet_id, description, email_notification, idcs_access_token, defined_tags, freeform_tags, kms_key_id, network_endpoint_details_network_security_group_ids):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['networkEndpointDetails'] = {}
    _details['name'] = name
    _details['compartmentId'] = compartment_id
    _details['featureSet'] = feature_set
    _details['capacity'] = cli_util.parse_json_parameter("capacity", capacity)
    _details['licenseType'] = license_type
    _details['networkEndpointDetails']['vcnId'] = network_endpoint_details_vcn_id
    _details['networkEndpointDetails']['subnetId'] = network_endpoint_details_subnet_id

    if description is not None:
        _details['description'] = description

    if email_notification is not None:
        _details['emailNotification'] = email_notification

    if idcs_access_token is not None:
        _details['idcsAccessToken'] = idcs_access_token

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if kms_key_id is not None:
        _details['kmsKeyId'] = kms_key_id

    if network_endpoint_details_network_security_group_ids is not None:
        _details['networkEndpointDetails']['networkSecurityGroupIds'] = cli_util.parse_json_parameter("network_endpoint_details_network_security_group_ids", network_endpoint_details_network_security_group_ids)

    _details['networkEndpointDetails']['networkEndpointType'] = 'PRIVATE'

    client = cli_util.build_client('analytics', 'analytics', ctx)
    result = client.create_analytics_instance(
        create_analytics_instance_details=_details,
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


@analytics_instance_group.command(name=cli_util.override('analytics.create_analytics_instance_public_endpoint_details.command_name', 'create-analytics-instance-public-endpoint-details'), help=u"""Create a new AnalyticsInstance in the specified compartment. The operation is long-running and creates a new WorkRequest. \n[Command Reference](createAnalyticsInstance)""")
@cli_util.option('--name', required=True, help=u"""The name of the Analytics instance. This name must be unique in the tenancy and cannot be changed.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--feature-set', required=True, type=custom_types.CliCaseInsensitiveChoice(["SELF_SERVICE_ANALYTICS", "ENTERPRISE_ANALYTICS"]), help=u"""Analytics feature set.""")
@cli_util.option('--capacity', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--license-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]), help=u"""The license used for the service.""")
@cli_util.option('--description', help=u"""Optional description.""")
@cli_util.option('--email-notification', help=u"""Email address receiving notifications.""")
@cli_util.option('--idcs-access-token', help=u"""IDCS access token identifying a stripe and service administrator user.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--kms-key-id', help=u"""The [OCID] of the OCI Vault Key encrypting the customer data stored in this Analytics instance. A null value indicates Oracle managed default encryption.""")
@cli_util.option('--network-endpoint-details-whitelisted-ips', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Source IP addresses or IP address ranges in ingress rules.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--network-endpoint-details-whitelisted-vcns', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Virtual Cloud Networks allowed to access this network endpoint.

This option is a JSON list with items of type VirtualCloudNetwork.  For documentation on VirtualCloudNetwork please see our API reference: https://docs.cloud.oracle.com/api/#/en/analytics/20190331/datatypes/VirtualCloudNetwork.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--network-endpoint-details-whitelisted-services', type=custom_types.CliCaseInsensitiveChoice(["ALL"]), help=u"""Oracle Cloud Services that are allowed to access this Analytics instance.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'capacity': {'module': 'analytics', 'class': 'Capacity'}, 'defined-tags': {'module': 'analytics', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'analytics', 'class': 'dict(str, string)'}, 'network-endpoint-details-whitelisted-ips': {'module': 'analytics', 'class': 'list[string]'}, 'network-endpoint-details-whitelisted-vcns': {'module': 'analytics', 'class': 'list[VirtualCloudNetwork]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'capacity': {'module': 'analytics', 'class': 'Capacity'}, 'defined-tags': {'module': 'analytics', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'analytics', 'class': 'dict(str, string)'}, 'network-endpoint-details-whitelisted-ips': {'module': 'analytics', 'class': 'list[string]'}, 'network-endpoint-details-whitelisted-vcns': {'module': 'analytics', 'class': 'list[VirtualCloudNetwork]'}}, output_type={'module': 'analytics', 'class': 'AnalyticsInstance'})
@cli_util.wrap_exceptions
def create_analytics_instance_public_endpoint_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, compartment_id, feature_set, capacity, license_type, description, email_notification, idcs_access_token, defined_tags, freeform_tags, kms_key_id, network_endpoint_details_whitelisted_ips, network_endpoint_details_whitelisted_vcns, network_endpoint_details_whitelisted_services):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['networkEndpointDetails'] = {}
    _details['name'] = name
    _details['compartmentId'] = compartment_id
    _details['featureSet'] = feature_set
    _details['capacity'] = cli_util.parse_json_parameter("capacity", capacity)
    _details['licenseType'] = license_type

    if description is not None:
        _details['description'] = description

    if email_notification is not None:
        _details['emailNotification'] = email_notification

    if idcs_access_token is not None:
        _details['idcsAccessToken'] = idcs_access_token

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if kms_key_id is not None:
        _details['kmsKeyId'] = kms_key_id

    if network_endpoint_details_whitelisted_ips is not None:
        _details['networkEndpointDetails']['whitelistedIps'] = cli_util.parse_json_parameter("network_endpoint_details_whitelisted_ips", network_endpoint_details_whitelisted_ips)

    if network_endpoint_details_whitelisted_vcns is not None:
        _details['networkEndpointDetails']['whitelistedVcns'] = cli_util.parse_json_parameter("network_endpoint_details_whitelisted_vcns", network_endpoint_details_whitelisted_vcns)

    if network_endpoint_details_whitelisted_services is not None:
        _details['networkEndpointDetails']['whitelistedServices'] = cli_util.parse_json_parameter("network_endpoint_details_whitelisted_services", network_endpoint_details_whitelisted_services)

    _details['networkEndpointDetails']['networkEndpointType'] = 'PUBLIC'

    client = cli_util.build_client('analytics', 'analytics', ctx)
    result = client.create_analytics_instance(
        create_analytics_instance_details=_details,
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


@analytics_instance_group.command(name=cli_util.override('analytics.create_private_access_channel.command_name', 'create-private-access-channel'), help=u"""Create an Private access Channel for the Analytics instance. The operation is long-running and creates a new WorkRequest. \n[Command Reference](createPrivateAccessChannel)""")
@cli_util.option('--analytics-instance-id', required=True, help=u"""The OCID of the AnalyticsInstance.""")
@cli_util.option('--display-name', required=True, help=u"""Display Name of the Private Access Channel.""")
@cli_util.option('--vcn-id', required=True, help=u"""OCID of the customer VCN peered with private access channel.""")
@cli_util.option('--subnet-id', required=True, help=u"""OCID of the customer subnet connected to private access channel.""")
@cli_util.option('--private-source-dns-zones', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Private Source DNS zones registered with Private Access Channel, where datasource hostnames from these dns zones / domains will be resolved in the peered VCN for access from Analytics Instance. Min of 1 is required and Max of 30 Private Source DNS zones can be registered.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--private-source-scan-hosts', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Private Source DB SCAN hosts registered with Private Access Channel for access from Analytics Instance.

This option is a JSON list with items of type PrivateSourceScanHost.  For documentation on PrivateSourceScanHost please see our API reference: https://docs.cloud.oracle.com/api/#/en/analytics/20190331/datatypes/PrivateSourceScanHost.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--network-security-group-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Network Security Group OCIDs for an Analytics instance.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'private-source-dns-zones': {'module': 'analytics', 'class': 'list[PrivateSourceDnsZone]'}, 'private-source-scan-hosts': {'module': 'analytics', 'class': 'list[PrivateSourceScanHost]'}, 'network-security-group-ids': {'module': 'analytics', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'private-source-dns-zones': {'module': 'analytics', 'class': 'list[PrivateSourceDnsZone]'}, 'private-source-scan-hosts': {'module': 'analytics', 'class': 'list[PrivateSourceScanHost]'}, 'network-security-group-ids': {'module': 'analytics', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def create_private_access_channel(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, analytics_instance_id, display_name, vcn_id, subnet_id, private_source_dns_zones, private_source_scan_hosts, network_security_group_ids):

    if isinstance(analytics_instance_id, six.string_types) and len(analytics_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --analytics-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['vcnId'] = vcn_id
    _details['subnetId'] = subnet_id
    _details['privateSourceDnsZones'] = cli_util.parse_json_parameter("private_source_dns_zones", private_source_dns_zones)

    if private_source_scan_hosts is not None:
        _details['privateSourceScanHosts'] = cli_util.parse_json_parameter("private_source_scan_hosts", private_source_scan_hosts)

    if network_security_group_ids is not None:
        _details['networkSecurityGroupIds'] = cli_util.parse_json_parameter("network_security_group_ids", network_security_group_ids)

    client = cli_util.build_client('analytics', 'analytics', ctx)
    result = client.create_private_access_channel(
        analytics_instance_id=analytics_instance_id,
        create_private_access_channel_details=_details,
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


@analytics_instance_group.command(name=cli_util.override('analytics.create_vanity_url.command_name', 'create-vanity-url'), help=u"""Allows specifying a custom host name to be used to access the analytics instance.  This requires prior setup of DNS entry and certificate for this host. \n[Command Reference](createVanityUrl)""")
@cli_util.option('--analytics-instance-id', required=True, help=u"""The OCID of the AnalyticsInstance.""")
@cli_util.option('--hosts', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of fully qualified hostnames supported by this vanity URL definition (max of 3).""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--private-key', required=True, help=u"""PEM Private key for HTTPS connections.""")
@cli_util.option('--public-certificate', required=True, help=u"""PEM certificate for HTTPS connections.""")
@cli_util.option('--ca-certificate', required=True, help=u"""PEM CA certificate(s) for HTTPS connections. This may include multiple PEM certificates.""")
@cli_util.option('--description', help=u"""Optional description.""")
@cli_util.option('--passphrase', help=u"""Passphrase for the PEM Private key (if any).""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'hosts': {'module': 'analytics', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'hosts': {'module': 'analytics', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def create_vanity_url(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, analytics_instance_id, hosts, private_key, public_certificate, ca_certificate, description, passphrase):

    if isinstance(analytics_instance_id, six.string_types) and len(analytics_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --analytics-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['hosts'] = cli_util.parse_json_parameter("hosts", hosts)
    _details['privateKey'] = private_key
    _details['publicCertificate'] = public_certificate
    _details['caCertificate'] = ca_certificate

    if description is not None:
        _details['description'] = description

    if passphrase is not None:
        _details['passphrase'] = passphrase

    client = cli_util.build_client('analytics', 'analytics', ctx)
    result = client.create_vanity_url(
        analytics_instance_id=analytics_instance_id,
        create_vanity_url_details=_details,
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


@analytics_instance_group.command(name=cli_util.override('analytics.delete_analytics_instance.command_name', 'delete'), help=u"""Terminates the specified Analytics instance. The operation is long-running and creates a new WorkRequest. \n[Command Reference](deleteAnalyticsInstance)""")
@cli_util.option('--analytics-instance-id', required=True, help=u"""The OCID of the AnalyticsInstance.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_analytics_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, analytics_instance_id, if_match):

    if isinstance(analytics_instance_id, six.string_types) and len(analytics_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --analytics-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('analytics', 'analytics', ctx)
    result = client.delete_analytics_instance(
        analytics_instance_id=analytics_instance_id,
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


@analytics_instance_group.command(name=cli_util.override('analytics.delete_private_access_channel.command_name', 'delete-private-access-channel'), help=u"""Delete an Analytics instance's Private access channel with the given unique identifier key. \n[Command Reference](deletePrivateAccessChannel)""")
@cli_util.option('--private-access-channel-key', required=True, help=u"""The unique identifier key of the Private Access Channel.""")
@cli_util.option('--analytics-instance-id', required=True, help=u"""The OCID of the AnalyticsInstance.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_private_access_channel(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, private_access_channel_key, analytics_instance_id, if_match):

    if isinstance(private_access_channel_key, six.string_types) and len(private_access_channel_key.strip()) == 0:
        raise click.UsageError('Parameter --private-access-channel-key cannot be whitespace or empty string')

    if isinstance(analytics_instance_id, six.string_types) and len(analytics_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --analytics-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('analytics', 'analytics', ctx)
    result = client.delete_private_access_channel(
        private_access_channel_key=private_access_channel_key,
        analytics_instance_id=analytics_instance_id,
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


@analytics_instance_group.command(name=cli_util.override('analytics.delete_vanity_url.command_name', 'delete-vanity-url'), help=u"""Allows deleting a previously created vanity url. \n[Command Reference](deleteVanityUrl)""")
@cli_util.option('--analytics-instance-id', required=True, help=u"""The OCID of the AnalyticsInstance.""")
@cli_util.option('--vanity-url-key', required=True, help=u"""Specify unique identifier key of a vanity url to update or delete.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_vanity_url(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, analytics_instance_id, vanity_url_key, if_match):

    if isinstance(analytics_instance_id, six.string_types) and len(analytics_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --analytics-instance-id cannot be whitespace or empty string')

    if isinstance(vanity_url_key, six.string_types) and len(vanity_url_key.strip()) == 0:
        raise click.UsageError('Parameter --vanity-url-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('analytics', 'analytics', ctx)
    result = client.delete_vanity_url(
        analytics_instance_id=analytics_instance_id,
        vanity_url_key=vanity_url_key,
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


@work_request_group.command(name=cli_util.override('analytics.delete_work_request.command_name', 'delete'), help=u"""Cancel a work request that has not started yet. \n[Command Reference](deleteWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the work request.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_work_request(ctx, from_json, work_request_id, if_match):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('analytics', 'analytics', ctx)
    result = client.delete_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@analytics_instance_group.command(name=cli_util.override('analytics.get_analytics_instance.command_name', 'get'), help=u"""Info for a specific Analytics instance. \n[Command Reference](getAnalyticsInstance)""")
@cli_util.option('--analytics-instance-id', required=True, help=u"""The OCID of the AnalyticsInstance.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'analytics', 'class': 'AnalyticsInstance'})
@cli_util.wrap_exceptions
def get_analytics_instance(ctx, from_json, analytics_instance_id):

    if isinstance(analytics_instance_id, six.string_types) and len(analytics_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --analytics-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('analytics', 'analytics', ctx)
    result = client.get_analytics_instance(
        analytics_instance_id=analytics_instance_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@analytics_instance_group.command(name=cli_util.override('analytics.get_private_access_channel.command_name', 'get-private-access-channel'), help=u"""Retrieve private access channel in the specified Analytics Instance. \n[Command Reference](getPrivateAccessChannel)""")
@cli_util.option('--private-access-channel-key', required=True, help=u"""The unique identifier key of the Private Access Channel.""")
@cli_util.option('--analytics-instance-id', required=True, help=u"""The OCID of the AnalyticsInstance.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'analytics', 'class': 'PrivateAccessChannel'})
@cli_util.wrap_exceptions
def get_private_access_channel(ctx, from_json, private_access_channel_key, analytics_instance_id):

    if isinstance(private_access_channel_key, six.string_types) and len(private_access_channel_key.strip()) == 0:
        raise click.UsageError('Parameter --private-access-channel-key cannot be whitespace or empty string')

    if isinstance(analytics_instance_id, six.string_types) and len(analytics_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --analytics-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('analytics', 'analytics', ctx)
    result = client.get_private_access_channel(
        private_access_channel_key=private_access_channel_key,
        analytics_instance_id=analytics_instance_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('analytics.get_work_request.command_name', 'get'), help=u"""Get the details of a work request. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the work request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'analytics', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('analytics', 'analytics', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@analytics_instance_group.command(name=cli_util.override('analytics.list_analytics_instances.command_name', 'list'), help=u"""List Analytics instances. \n[Command Reference](listAnalyticsInstances)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the given name exactly.""")
@cli_util.option('--capacity-type', type=custom_types.CliCaseInsensitiveChoice(["OLPU_COUNT", "USER_COUNT"]), help=u"""A filter to only return resources matching the capacity type enum. Values are case-insensitive.""")
@cli_util.option('--feature-set', type=custom_types.CliCaseInsensitiveChoice(["SELF_SERVICE_ANALYTICS", "ENTERPRISE_ANALYTICS"]), help=u"""A filter to only return resources matching the feature set. Values are case-insensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "INACTIVE", "UPDATING"]), help=u"""A filter to only return resources matching the lifecycle state. The state value is case-insensitive.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["capacityType", "capacityValue", "featureSet", "lifecycleState", "name", "timeCreated"]), help=u"""The field to sort by (one column only). Default sort order is ascending exception of `timeCreated` column (descending).""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'analytics', 'class': 'list[AnalyticsInstanceSummary]'})
@cli_util.wrap_exceptions
def list_analytics_instances(ctx, from_json, all_pages, page_size, compartment_id, name, capacity_type, feature_set, lifecycle_state, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if capacity_type is not None:
        kwargs['capacity_type'] = capacity_type
    if feature_set is not None:
        kwargs['feature_set'] = feature_set
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('analytics', 'analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_analytics_instances,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_analytics_instances,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_analytics_instances(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('analytics.list_work_request_errors.command_name', 'list'), help=u"""Get the errors of a work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the work request.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'analytics', 'class': 'list[WorkRequestError]'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('analytics', 'analytics', ctx)
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


@work_request_log_group.command(name=cli_util.override('analytics.list_work_request_logs.command_name', 'list'), help=u"""Get the logs of a work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the work request.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'analytics', 'class': 'list[WorkRequestLog]'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('analytics', 'analytics', ctx)
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


@work_request_group.command(name=cli_util.override('analytics.list_work_requests.command_name', 'list'), help=u"""List all work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--resource-id', help=u"""The OCID of the resource associated with a work request.""")
@cli_util.option('--resource-type', type=custom_types.CliCaseInsensitiveChoice(["ANALYTICS_INSTANCE"]), help=u"""Type of the resource associated with a work request.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help=u"""One or more work request status values to filter on.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "operationType", "status", "timeAccepted", "timeStarted", "timeFinished"]), help=u"""The field used for sorting work request results.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'analytics', 'class': 'list[WorkRequestSummary]'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, resource_id, resource_type, status, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if resource_id is not None:
        kwargs['resource_id'] = resource_id
    if resource_type is not None:
        kwargs['resource_type'] = resource_type
    if status is not None and len(status) > 0:
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
    client = cli_util.build_client('analytics', 'analytics', ctx)
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


@analytics_instance_group.command(name=cli_util.override('analytics.scale_analytics_instance.command_name', 'scale'), help=u"""Scale an Analytics instance up or down. The operation is long-running and creates a new WorkRequest. \n[Command Reference](scaleAnalyticsInstance)""")
@cli_util.option('--analytics-instance-id', required=True, help=u"""The OCID of the AnalyticsInstance.""")
@cli_util.option('--capacity', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'capacity': {'module': 'analytics', 'class': 'Capacity'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'capacity': {'module': 'analytics', 'class': 'Capacity'}})
@cli_util.wrap_exceptions
def scale_analytics_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, analytics_instance_id, capacity, if_match):

    if isinstance(analytics_instance_id, six.string_types) and len(analytics_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --analytics-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['capacity'] = cli_util.parse_json_parameter("capacity", capacity)

    client = cli_util.build_client('analytics', 'analytics', ctx)
    result = client.scale_analytics_instance(
        analytics_instance_id=analytics_instance_id,
        scale_analytics_instance_details=_details,
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


@analytics_instance_group.command(name=cli_util.override('analytics.set_kms_key.command_name', 'set-kms-key'), help=u"""Encrypts the customer data of this Analytics instance using either a customer OCI Vault Key or Oracle managed default key. \n[Command Reference](setKmsKey)""")
@cli_util.option('--analytics-instance-id', required=True, help=u"""The OCID of the AnalyticsInstance.""")
@cli_util.option('--kms-key-id', required=True, help=u"""OCID of the OCI Vault Key encrypting the customer data stored in this Analytics instance. An empty value indicates Oracle managed default encryption (null is not supported in this API).""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def set_kms_key(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, analytics_instance_id, kms_key_id, if_match):

    if isinstance(analytics_instance_id, six.string_types) and len(analytics_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --analytics-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['kmsKeyId'] = kms_key_id

    client = cli_util.build_client('analytics', 'analytics', ctx)
    result = client.set_kms_key(
        analytics_instance_id=analytics_instance_id,
        set_kms_key_details=_details,
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


@analytics_instance_group.command(name=cli_util.override('analytics.start_analytics_instance.command_name', 'start'), help=u"""Starts the specified Analytics instance. The operation is long-running and creates a new WorkRequest. \n[Command Reference](startAnalyticsInstance)""")
@cli_util.option('--analytics-instance-id', required=True, help=u"""The OCID of the AnalyticsInstance.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def start_analytics_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, analytics_instance_id, if_match):

    if isinstance(analytics_instance_id, six.string_types) and len(analytics_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --analytics-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('analytics', 'analytics', ctx)
    result = client.start_analytics_instance(
        analytics_instance_id=analytics_instance_id,
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


@analytics_instance_group.command(name=cli_util.override('analytics.stop_analytics_instance.command_name', 'stop'), help=u"""Stop the specified Analytics instance. The operation is long-running and creates a new WorkRequest. \n[Command Reference](stopAnalyticsInstance)""")
@cli_util.option('--analytics-instance-id', required=True, help=u"""The OCID of the AnalyticsInstance.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def stop_analytics_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, analytics_instance_id, if_match):

    if isinstance(analytics_instance_id, six.string_types) and len(analytics_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --analytics-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('analytics', 'analytics', ctx)
    result = client.stop_analytics_instance(
        analytics_instance_id=analytics_instance_id,
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


@analytics_instance_group.command(name=cli_util.override('analytics.update_analytics_instance.command_name', 'update'), help=u"""Updates certain fields of an Analytics instance. Fields that are not provided in the request will not be updated. \n[Command Reference](updateAnalyticsInstance)""")
@cli_util.option('--analytics-instance-id', required=True, help=u"""The OCID of the AnalyticsInstance.""")
@cli_util.option('--description', help=u"""Optional description.""")
@cli_util.option('--email-notification', help=u"""Email address receiving notifications.""")
@cli_util.option('--license-type', type=custom_types.CliCaseInsensitiveChoice(["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]), help=u"""The license used for the service.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "INACTIVE", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'analytics', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'analytics', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'analytics', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'analytics', 'class': 'dict(str, string)'}}, output_type={'module': 'analytics', 'class': 'AnalyticsInstance'})
@cli_util.wrap_exceptions
def update_analytics_instance(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, analytics_instance_id, description, email_notification, license_type, defined_tags, freeform_tags, if_match):

    if isinstance(analytics_instance_id, six.string_types) and len(analytics_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --analytics-instance-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if email_notification is not None:
        _details['emailNotification'] = email_notification

    if license_type is not None:
        _details['licenseType'] = license_type

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('analytics', 'analytics', ctx)
    result = client.update_analytics_instance(
        analytics_instance_id=analytics_instance_id,
        update_analytics_instance_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_analytics_instance') and callable(getattr(client, 'get_analytics_instance')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_analytics_instance(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@analytics_instance_group.command(name=cli_util.override('analytics.update_private_access_channel.command_name', 'update-private-access-channel'), help=u"""Update the Private Access Channel with the given unique identifier key in the specified Analytics Instance. \n[Command Reference](updatePrivateAccessChannel)""")
@cli_util.option('--private-access-channel-key', required=True, help=u"""The unique identifier key of the Private Access Channel.""")
@cli_util.option('--analytics-instance-id', required=True, help=u"""The OCID of the AnalyticsInstance.""")
@cli_util.option('--display-name', help=u"""Display Name of the Private Access Channel.""")
@cli_util.option('--vcn-id', help=u"""OCID of the customer VCN peered with private access channel.""")
@cli_util.option('--subnet-id', help=u"""OCID of the customer subnet connected to private access channel.""")
@cli_util.option('--private-source-dns-zones', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Private Source DNS zones registered with Private Access Channel, where datasource hostnames from these dns zones / domains will be resolved in the peered VCN for access from Analytics Instance. Min of 1 is required and Max of 30 Private Source DNS zones can be registered.

This option is a JSON list with items of type PrivateSourceDnsZone.  For documentation on PrivateSourceDnsZone please see our API reference: https://docs.cloud.oracle.com/api/#/en/analytics/20190331/datatypes/PrivateSourceDnsZone.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--private-source-scan-hosts', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Private Source DB SCAN hosts registered with Private Access Channel for access from Analytics Instance.

This option is a JSON list with items of type PrivateSourceScanHost.  For documentation on PrivateSourceScanHost please see our API reference: https://docs.cloud.oracle.com/api/#/en/analytics/20190331/datatypes/PrivateSourceScanHost.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--network-security-group-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Network Security Group OCIDs for an Analytics instance.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'private-source-dns-zones': {'module': 'analytics', 'class': 'list[PrivateSourceDnsZone]'}, 'private-source-scan-hosts': {'module': 'analytics', 'class': 'list[PrivateSourceScanHost]'}, 'network-security-group-ids': {'module': 'analytics', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'private-source-dns-zones': {'module': 'analytics', 'class': 'list[PrivateSourceDnsZone]'}, 'private-source-scan-hosts': {'module': 'analytics', 'class': 'list[PrivateSourceScanHost]'}, 'network-security-group-ids': {'module': 'analytics', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_private_access_channel(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, private_access_channel_key, analytics_instance_id, display_name, vcn_id, subnet_id, private_source_dns_zones, private_source_scan_hosts, network_security_group_ids, if_match):

    if isinstance(private_access_channel_key, six.string_types) and len(private_access_channel_key.strip()) == 0:
        raise click.UsageError('Parameter --private-access-channel-key cannot be whitespace or empty string')

    if isinstance(analytics_instance_id, six.string_types) and len(analytics_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --analytics-instance-id cannot be whitespace or empty string')
    if not force:
        if private_source_dns_zones or private_source_scan_hosts or network_security_group_ids:
            if not click.confirm("WARNING: Updates to private-source-dns-zones and private-source-scan-hosts and network-security-group-ids will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if vcn_id is not None:
        _details['vcnId'] = vcn_id

    if subnet_id is not None:
        _details['subnetId'] = subnet_id

    if private_source_dns_zones is not None:
        _details['privateSourceDnsZones'] = cli_util.parse_json_parameter("private_source_dns_zones", private_source_dns_zones)

    if private_source_scan_hosts is not None:
        _details['privateSourceScanHosts'] = cli_util.parse_json_parameter("private_source_scan_hosts", private_source_scan_hosts)

    if network_security_group_ids is not None:
        _details['networkSecurityGroupIds'] = cli_util.parse_json_parameter("network_security_group_ids", network_security_group_ids)

    client = cli_util.build_client('analytics', 'analytics', ctx)
    result = client.update_private_access_channel(
        private_access_channel_key=private_access_channel_key,
        analytics_instance_id=analytics_instance_id,
        update_private_access_channel_details=_details,
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


@analytics_instance_group.command(name=cli_util.override('analytics.update_vanity_url.command_name', 'update-vanity-url'), help=u"""Allows uploading a new certificate for a vanity url, which will have to be done when the current certificate is expiring. \n[Command Reference](updateVanityUrl)""")
@cli_util.option('--analytics-instance-id', required=True, help=u"""The OCID of the AnalyticsInstance.""")
@cli_util.option('--vanity-url-key', required=True, help=u"""Specify unique identifier key of a vanity url to update or delete.""")
@cli_util.option('--private-key', required=True, help=u"""PEM Private key for HTTPS connections.""")
@cli_util.option('--public-certificate', required=True, help=u"""PEM certificate for HTTPS connections.""")
@cli_util.option('--ca-certificate', required=True, help=u"""PEM CA certificate(s) for HTTPS connections. This may include multiple PEM certificates.""")
@cli_util.option('--passphrase', help=u"""Passphrase for the PEM Private key (if any).""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_vanity_url(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, analytics_instance_id, vanity_url_key, private_key, public_certificate, ca_certificate, passphrase, if_match):

    if isinstance(analytics_instance_id, six.string_types) and len(analytics_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --analytics-instance-id cannot be whitespace or empty string')

    if isinstance(vanity_url_key, six.string_types) and len(vanity_url_key.strip()) == 0:
        raise click.UsageError('Parameter --vanity-url-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['privateKey'] = private_key
    _details['publicCertificate'] = public_certificate
    _details['caCertificate'] = ca_certificate

    if passphrase is not None:
        _details['passphrase'] = passphrase

    client = cli_util.build_client('analytics', 'analytics', ctx)
    result = client.update_vanity_url(
        analytics_instance_id=analytics_instance_id,
        vanity_url_key=vanity_url_key,
        update_vanity_url_details=_details,
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
