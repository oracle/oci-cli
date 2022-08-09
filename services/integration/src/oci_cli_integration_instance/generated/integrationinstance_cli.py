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


@cli.command(cli_util.override('integration.integration_root_group.command_name', 'integration'), cls=CommandGroupWithAlias, help=cli_util.override('integration.integration_root_group.help', """Oracle Integration API."""), short_help=cli_util.override('integration.integration_root_group.short_help', """Oracle Integration API"""))
@cli_util.help_option_group
def integration_root_group():
    pass


@click.command(cli_util.override('integration.integration_instance_group.command_name', 'integration-instance'), cls=CommandGroupWithAlias, help="""Description of Integration Instance.""")
@cli_util.help_option_group
def integration_instance_group():
    pass


@click.command(cli_util.override('integration.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""Errors related to a specific work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('integration.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""Log entries related to a specific work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('integration.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""A description of work request status.""")
@cli_util.help_option_group
def work_request_group():
    pass


integration_root_group.add_command(integration_instance_group)
integration_root_group.add_command(work_request_error_group)
integration_root_group.add_command(work_request_log_entry_group)
integration_root_group.add_command(work_request_group)


@integration_instance_group.command(name=cli_util.override('integration.change_integration_instance_compartment.command_name', 'change-compartment'), help=u"""Change the compartment for an integration instance \n[Command Reference](changeIntegrationInstanceCompartment)""")
@cli_util.option('--integration-instance-id', required=True, help=u"""Unique Integration Instance identifier.""")
@cli_util.option('--compartment-id', help=u"""Compartment Identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_integration_instance_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, integration_instance_id, compartment_id, if_match):

    if isinstance(integration_instance_id, six.string_types) and len(integration_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --integration-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    client = cli_util.build_client('integration', 'integration_instance', ctx)
    result = client.change_integration_instance_compartment(
        integration_instance_id=integration_instance_id,
        change_integration_instance_compartment_details=_details,
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


@integration_instance_group.command(name=cli_util.override('integration.change_integration_instance_network_endpoint.command_name', 'change-integration-instance-network-endpoint'), help=u"""Change an Integration instance network endpoint. The operation is long-running and creates a new WorkRequest. \n[Command Reference](changeIntegrationInstanceNetworkEndpoint)""")
@cli_util.option('--integration-instance-id', required=True, help=u"""Unique Integration Instance identifier.""")
@cli_util.option('--network-endpoint-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'network-endpoint-details': {'module': 'integration', 'class': 'NetworkEndpointDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'network-endpoint-details': {'module': 'integration', 'class': 'NetworkEndpointDetails'}})
@cli_util.wrap_exceptions
def change_integration_instance_network_endpoint(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, integration_instance_id, network_endpoint_details, if_match):

    if isinstance(integration_instance_id, six.string_types) and len(integration_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --integration-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if network_endpoint_details is not None:
        _details['networkEndpointDetails'] = cli_util.parse_json_parameter("network_endpoint_details", network_endpoint_details)

    client = cli_util.build_client('integration', 'integration_instance', ctx)
    result = client.change_integration_instance_network_endpoint(
        integration_instance_id=integration_instance_id,
        change_integration_instance_network_endpoint_details=_details,
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


@integration_instance_group.command(name=cli_util.override('integration.change_integration_instance_network_endpoint_public_endpoint_details.command_name', 'change-integration-instance-network-endpoint-public-endpoint-details'), help=u"""Change an Integration instance network endpoint. The operation is long-running and creates a new WorkRequest. \n[Command Reference](changeIntegrationInstanceNetworkEndpoint)""")
@cli_util.option('--integration-instance-id', required=True, help=u"""Unique Integration Instance identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--network-endpoint-details-allowlisted-http-ips', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Source IP addresses or IP address ranges ingress rules. (ex: \"168.122.59.5\", \"10.20.30.0/26\") An invalid IP or CIDR block will result in a 400 response.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--network-endpoint-details-allowlisted-http-vcns', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Virtual Cloud Networks allowed to access this network endpoint.

This option is a JSON list with items of type VirtualCloudNetwork.  For documentation on VirtualCloudNetwork please see our API reference: https://docs.cloud.oracle.com/api/#/en/integrationinstance/20190131/datatypes/VirtualCloudNetwork.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--network-endpoint-details-is-integration-vcn-allowlisted', type=click.BOOL, help=u"""The Integration service's VCN is allow-listed to allow integrations to call back into other integrations""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'network-endpoint-details-allowlisted-http-ips': {'module': 'integration', 'class': 'list[string]'}, 'network-endpoint-details-allowlisted-http-vcns': {'module': 'integration', 'class': 'list[VirtualCloudNetwork]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'network-endpoint-details-allowlisted-http-ips': {'module': 'integration', 'class': 'list[string]'}, 'network-endpoint-details-allowlisted-http-vcns': {'module': 'integration', 'class': 'list[VirtualCloudNetwork]'}})
@cli_util.wrap_exceptions
def change_integration_instance_network_endpoint_public_endpoint_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, integration_instance_id, if_match, network_endpoint_details_allowlisted_http_ips, network_endpoint_details_allowlisted_http_vcns, network_endpoint_details_is_integration_vcn_allowlisted):

    if isinstance(integration_instance_id, six.string_types) and len(integration_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --integration-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['networkEndpointDetails'] = {}

    if network_endpoint_details_allowlisted_http_ips is not None:
        _details['networkEndpointDetails']['allowlistedHttpIps'] = cli_util.parse_json_parameter("network_endpoint_details_allowlisted_http_ips", network_endpoint_details_allowlisted_http_ips)

    if network_endpoint_details_allowlisted_http_vcns is not None:
        _details['networkEndpointDetails']['allowlistedHttpVcns'] = cli_util.parse_json_parameter("network_endpoint_details_allowlisted_http_vcns", network_endpoint_details_allowlisted_http_vcns)

    if network_endpoint_details_is_integration_vcn_allowlisted is not None:
        _details['networkEndpointDetails']['isIntegrationVcnAllowlisted'] = network_endpoint_details_is_integration_vcn_allowlisted

    _details['networkEndpointDetails']['networkEndpointType'] = 'PUBLIC'

    client = cli_util.build_client('integration', 'integration_instance', ctx)
    result = client.change_integration_instance_network_endpoint(
        integration_instance_id=integration_instance_id,
        change_integration_instance_network_endpoint_details=_details,
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


@integration_instance_group.command(name=cli_util.override('integration.create_integration_instance.command_name', 'create'), help=u"""Creates a new Integration Instance. \n[Command Reference](createIntegrationInstance)""")
@cli_util.option('--display-name', required=True, help=u"""Integration Instance Identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier.""")
@cli_util.option('--integration-instance-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["STANDARD", "ENTERPRISE", "STANDARDX", "ENTERPRISEX"]), help=u"""Standard or Enterprise type, Oracle Integration Generation 2 uses ENTERPRISE and STANDARD, Oracle Integration 3 uses ENTERPRISEX and STANDARDX""")
@cli_util.option('--is-byol', required=True, type=click.BOOL, help=u"""Bring your own license.""")
@cli_util.option('--message-packs', required=True, type=click.INT, help=u"""The number of configured message packs""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--idcs-at', help=u"""IDCS Authentication token. This is required for all realms with IDCS. Its optional as its not required for non IDCS realms.""")
@cli_util.option('--is-visual-builder-enabled', type=click.BOOL, help=u"""Visual Builder is enabled or not.""")
@cli_util.option('--custom-endpoint', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--alternate-custom-endpoints', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of alternate custom endpoints to be used for the integration instance URL (contact Oracle for alternateCustomEndpoints availability for a specific instance).

This option is a JSON list with items of type CreateCustomEndpointDetails.  For documentation on CreateCustomEndpointDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/integrationinstance/20190131/datatypes/CreateCustomEndpointDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--consumption-model', type=custom_types.CliCaseInsensitiveChoice(["UCM", "GOV", "OIC4SAAS"]), help=u"""Optional parameter specifying which entitlement to use for billing purposes. Only required if the account possesses more than one entitlement.""")
@cli_util.option('--is-file-server-enabled', type=click.BOOL, help=u"""The file server is enabled or not.""")
@cli_util.option('--network-endpoint-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--shape', type=custom_types.CliCaseInsensitiveChoice(["DEVELOPMENT", "PRODUCTION"]), help=u"""Shape""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'integration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'integration', 'class': 'dict(str, dict(str, object))'}, 'custom-endpoint': {'module': 'integration', 'class': 'CreateCustomEndpointDetails'}, 'alternate-custom-endpoints': {'module': 'integration', 'class': 'list[CreateCustomEndpointDetails]'}, 'network-endpoint-details': {'module': 'integration', 'class': 'NetworkEndpointDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'integration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'integration', 'class': 'dict(str, dict(str, object))'}, 'custom-endpoint': {'module': 'integration', 'class': 'CreateCustomEndpointDetails'}, 'alternate-custom-endpoints': {'module': 'integration', 'class': 'list[CreateCustomEndpointDetails]'}, 'network-endpoint-details': {'module': 'integration', 'class': 'NetworkEndpointDetails'}})
@cli_util.wrap_exceptions
def create_integration_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, integration_instance_type, is_byol, message_packs, freeform_tags, defined_tags, idcs_at, is_visual_builder_enabled, custom_endpoint, alternate_custom_endpoints, consumption_model, is_file_server_enabled, network_endpoint_details, shape):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['integrationInstanceType'] = integration_instance_type
    _details['isByol'] = is_byol
    _details['messagePacks'] = message_packs

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if idcs_at is not None:
        _details['idcsAt'] = idcs_at

    if is_visual_builder_enabled is not None:
        _details['isVisualBuilderEnabled'] = is_visual_builder_enabled

    if custom_endpoint is not None:
        _details['customEndpoint'] = cli_util.parse_json_parameter("custom_endpoint", custom_endpoint)

    if alternate_custom_endpoints is not None:
        _details['alternateCustomEndpoints'] = cli_util.parse_json_parameter("alternate_custom_endpoints", alternate_custom_endpoints)

    if consumption_model is not None:
        _details['consumptionModel'] = consumption_model

    if is_file_server_enabled is not None:
        _details['isFileServerEnabled'] = is_file_server_enabled

    if network_endpoint_details is not None:
        _details['networkEndpointDetails'] = cli_util.parse_json_parameter("network_endpoint_details", network_endpoint_details)

    if shape is not None:
        _details['shape'] = shape

    client = cli_util.build_client('integration', 'integration_instance', ctx)
    result = client.create_integration_instance(
        create_integration_instance_details=_details,
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


@integration_instance_group.command(name=cli_util.override('integration.create_integration_instance_public_endpoint_details.command_name', 'create-integration-instance-public-endpoint-details'), help=u"""Creates a new Integration Instance. \n[Command Reference](createIntegrationInstance)""")
@cli_util.option('--display-name', required=True, help=u"""Integration Instance Identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier.""")
@cli_util.option('--integration-instance-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["STANDARD", "ENTERPRISE", "STANDARDX", "ENTERPRISEX"]), help=u"""Standard or Enterprise type, Oracle Integration Generation 2 uses ENTERPRISE and STANDARD, Oracle Integration 3 uses ENTERPRISEX and STANDARDX""")
@cli_util.option('--is-byol', required=True, type=click.BOOL, help=u"""Bring your own license.""")
@cli_util.option('--message-packs', required=True, type=click.INT, help=u"""The number of configured message packs""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--idcs-at', help=u"""IDCS Authentication token. This is required for all realms with IDCS. Its optional as its not required for non IDCS realms.""")
@cli_util.option('--is-visual-builder-enabled', type=click.BOOL, help=u"""Visual Builder is enabled or not.""")
@cli_util.option('--custom-endpoint', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--alternate-custom-endpoints', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of alternate custom endpoints to be used for the integration instance URL (contact Oracle for alternateCustomEndpoints availability for a specific instance).

This option is a JSON list with items of type CreateCustomEndpointDetails.  For documentation on CreateCustomEndpointDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/integrationinstance/20190131/datatypes/CreateCustomEndpointDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--consumption-model', type=custom_types.CliCaseInsensitiveChoice(["UCM", "GOV", "OIC4SAAS"]), help=u"""Optional parameter specifying which entitlement to use for billing purposes. Only required if the account possesses more than one entitlement.""")
@cli_util.option('--is-file-server-enabled', type=click.BOOL, help=u"""The file server is enabled or not.""")
@cli_util.option('--shape', type=custom_types.CliCaseInsensitiveChoice(["DEVELOPMENT", "PRODUCTION"]), help=u"""Shape""")
@cli_util.option('--network-endpoint-details-allowlisted-http-ips', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Source IP addresses or IP address ranges ingress rules. (ex: \"168.122.59.5\", \"10.20.30.0/26\") An invalid IP or CIDR block will result in a 400 response.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--network-endpoint-details-allowlisted-http-vcns', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Virtual Cloud Networks allowed to access this network endpoint.

This option is a JSON list with items of type VirtualCloudNetwork.  For documentation on VirtualCloudNetwork please see our API reference: https://docs.cloud.oracle.com/api/#/en/integrationinstance/20190131/datatypes/VirtualCloudNetwork.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--network-endpoint-details-is-integration-vcn-allowlisted', type=click.BOOL, help=u"""The Integration service's VCN is allow-listed to allow integrations to call back into other integrations""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'integration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'integration', 'class': 'dict(str, dict(str, object))'}, 'custom-endpoint': {'module': 'integration', 'class': 'CreateCustomEndpointDetails'}, 'alternate-custom-endpoints': {'module': 'integration', 'class': 'list[CreateCustomEndpointDetails]'}, 'network-endpoint-details-allowlisted-http-ips': {'module': 'integration', 'class': 'list[string]'}, 'network-endpoint-details-allowlisted-http-vcns': {'module': 'integration', 'class': 'list[VirtualCloudNetwork]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'integration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'integration', 'class': 'dict(str, dict(str, object))'}, 'custom-endpoint': {'module': 'integration', 'class': 'CreateCustomEndpointDetails'}, 'alternate-custom-endpoints': {'module': 'integration', 'class': 'list[CreateCustomEndpointDetails]'}, 'network-endpoint-details-allowlisted-http-ips': {'module': 'integration', 'class': 'list[string]'}, 'network-endpoint-details-allowlisted-http-vcns': {'module': 'integration', 'class': 'list[VirtualCloudNetwork]'}})
@cli_util.wrap_exceptions
def create_integration_instance_public_endpoint_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, integration_instance_type, is_byol, message_packs, freeform_tags, defined_tags, idcs_at, is_visual_builder_enabled, custom_endpoint, alternate_custom_endpoints, consumption_model, is_file_server_enabled, shape, network_endpoint_details_allowlisted_http_ips, network_endpoint_details_allowlisted_http_vcns, network_endpoint_details_is_integration_vcn_allowlisted):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['networkEndpointDetails'] = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['integrationInstanceType'] = integration_instance_type
    _details['isByol'] = is_byol
    _details['messagePacks'] = message_packs

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if idcs_at is not None:
        _details['idcsAt'] = idcs_at

    if is_visual_builder_enabled is not None:
        _details['isVisualBuilderEnabled'] = is_visual_builder_enabled

    if custom_endpoint is not None:
        _details['customEndpoint'] = cli_util.parse_json_parameter("custom_endpoint", custom_endpoint)

    if alternate_custom_endpoints is not None:
        _details['alternateCustomEndpoints'] = cli_util.parse_json_parameter("alternate_custom_endpoints", alternate_custom_endpoints)

    if consumption_model is not None:
        _details['consumptionModel'] = consumption_model

    if is_file_server_enabled is not None:
        _details['isFileServerEnabled'] = is_file_server_enabled

    if shape is not None:
        _details['shape'] = shape

    if network_endpoint_details_allowlisted_http_ips is not None:
        _details['networkEndpointDetails']['allowlistedHttpIps'] = cli_util.parse_json_parameter("network_endpoint_details_allowlisted_http_ips", network_endpoint_details_allowlisted_http_ips)

    if network_endpoint_details_allowlisted_http_vcns is not None:
        _details['networkEndpointDetails']['allowlistedHttpVcns'] = cli_util.parse_json_parameter("network_endpoint_details_allowlisted_http_vcns", network_endpoint_details_allowlisted_http_vcns)

    if network_endpoint_details_is_integration_vcn_allowlisted is not None:
        _details['networkEndpointDetails']['isIntegrationVcnAllowlisted'] = network_endpoint_details_is_integration_vcn_allowlisted

    _details['networkEndpointDetails']['networkEndpointType'] = 'PUBLIC'

    client = cli_util.build_client('integration', 'integration_instance', ctx)
    result = client.create_integration_instance(
        create_integration_instance_details=_details,
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


@integration_instance_group.command(name=cli_util.override('integration.delete_integration_instance.command_name', 'delete'), help=u"""Deletes an Integration Instance resource by identifier. \n[Command Reference](deleteIntegrationInstance)""")
@cli_util.option('--integration-instance-id', required=True, help=u"""Unique Integration Instance identifier.""")
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
def delete_integration_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, integration_instance_id, if_match):

    if isinstance(integration_instance_id, six.string_types) and len(integration_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --integration-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('integration', 'integration_instance', ctx)
    result = client.delete_integration_instance(
        integration_instance_id=integration_instance_id,
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


@integration_instance_group.command(name=cli_util.override('integration.get_integration_instance.command_name', 'get'), help=u"""Gets a IntegrationInstance by identifier \n[Command Reference](getIntegrationInstance)""")
@cli_util.option('--integration-instance-id', required=True, help=u"""Unique Integration Instance identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'integration', 'class': 'IntegrationInstance'})
@cli_util.wrap_exceptions
def get_integration_instance(ctx, from_json, integration_instance_id):

    if isinstance(integration_instance_id, six.string_types) and len(integration_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --integration-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('integration', 'integration_instance', ctx)
    result = client.get_integration_instance(
        integration_instance_id=integration_instance_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('integration.get_work_request.command_name', 'get'), help=u"""Gets the status of the work request with the given ID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'integration', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('integration', 'integration_instance', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@integration_instance_group.command(name=cli_util.override('integration.list_integration_instances.command_name', 'list'), help=u"""Returns a list of Integration Instances. \n[Command Reference](listIntegrationInstances)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable.

Example: `My new resource`""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""Life cycle state to query on.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'integration', 'class': 'list[IntegrationInstanceSummary]'})
@cli_util.wrap_exceptions
def list_integration_instances(ctx, from_json, all_pages, page_size, compartment_id, display_name, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
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
    client = cli_util.build_client('integration', 'integration_instance', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_integration_instances,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_integration_instances,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_integration_instances(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('integration.list_work_request_errors.command_name', 'list'), help=u"""Get the errors of a work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'integration', 'class': 'list[WorkRequestError]'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, compartment_id, work_request_id, limit, page):

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
    client = cli_util.build_client('integration', 'integration_instance', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_errors,
            compartment_id=compartment_id,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_errors,
            limit,
            page_size,
            compartment_id=compartment_id,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_errors(
            compartment_id=compartment_id,
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_log_entry_group.command(name=cli_util.override('integration.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Get the logs of a work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'integration', 'class': 'list[WorkRequestLogEntry]'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, compartment_id, work_request_id, limit, page):

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
    client = cli_util.build_client('integration', 'integration_instance', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_logs,
            compartment_id=compartment_id,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_logs,
            limit,
            page_size,
            compartment_id=compartment_id,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_logs(
            compartment_id=compartment_id,
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('integration.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--integration-instance-id', help=u"""The Integration Instance identifier to use to filter results""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'integration', 'class': 'list[WorkRequestSummary]'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, page, limit, integration_instance_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if integration_instance_id is not None:
        kwargs['integration_instance_id'] = integration_instance_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('integration', 'integration_instance', ctx)
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


@integration_instance_group.command(name=cli_util.override('integration.start_integration_instance.command_name', 'start'), help=u"""Start an integration instance that was previously in an INACTIVE state \n[Command Reference](startIntegrationInstance)""")
@cli_util.option('--integration-instance-id', required=True, help=u"""Unique Integration Instance identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def start_integration_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, integration_instance_id, if_match):

    if isinstance(integration_instance_id, six.string_types) and len(integration_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --integration-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('integration', 'integration_instance', ctx)
    result = client.start_integration_instance(
        integration_instance_id=integration_instance_id,
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


@integration_instance_group.command(name=cli_util.override('integration.stop_integration_instance.command_name', 'stop'), help=u"""Stop an integration instance that was previously in an ACTIVE state \n[Command Reference](stopIntegrationInstance)""")
@cli_util.option('--integration-instance-id', required=True, help=u"""Unique Integration Instance identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def stop_integration_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, integration_instance_id, if_match):

    if isinstance(integration_instance_id, six.string_types) and len(integration_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --integration-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('integration', 'integration_instance', ctx)
    result = client.stop_integration_instance(
        integration_instance_id=integration_instance_id,
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


@integration_instance_group.command(name=cli_util.override('integration.update_integration_instance.command_name', 'update'), help=u"""Updates the Integration Instance. \n[Command Reference](updateIntegrationInstance)""")
@cli_util.option('--integration-instance-id', required=True, help=u"""Unique Integration Instance identifier.""")
@cli_util.option('--display-name', help=u"""Integration Instance Identifier.""")
@cli_util.option('--integration-instance-type', type=custom_types.CliCaseInsensitiveChoice(["STANDARD", "ENTERPRISE", "STANDARDX", "ENTERPRISEX"]), help=u"""Standard or Enterprise type, Oracle Integration Generation 2 uses ENTERPRISE and STANDARD, Oracle Integration 3 uses ENTERPRISEX and STANDARDX""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-byol', type=click.BOOL, help=u"""Bring your own license.""")
@cli_util.option('--message-packs', type=click.INT, help=u"""The number of configured message packs""")
@cli_util.option('--is-file-server-enabled', type=click.BOOL, help=u"""The file server is enabled or not.""")
@cli_util.option('--is-visual-builder-enabled', type=click.BOOL, help=u"""Visual Builder is enabled or not.""")
@cli_util.option('--custom-endpoint', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--alternate-custom-endpoints', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of alternate custom endpoints to be used for the integration instance URL (contact Oracle for alternateCustomEndpoints availability for a specific instance).

This option is a JSON list with items of type UpdateCustomEndpointDetails.  For documentation on UpdateCustomEndpointDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/integrationinstance/20190131/datatypes/UpdateCustomEndpointDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'integration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'integration', 'class': 'dict(str, dict(str, object))'}, 'custom-endpoint': {'module': 'integration', 'class': 'UpdateCustomEndpointDetails'}, 'alternate-custom-endpoints': {'module': 'integration', 'class': 'list[UpdateCustomEndpointDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'integration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'integration', 'class': 'dict(str, dict(str, object))'}, 'custom-endpoint': {'module': 'integration', 'class': 'UpdateCustomEndpointDetails'}, 'alternate-custom-endpoints': {'module': 'integration', 'class': 'list[UpdateCustomEndpointDetails]'}})
@cli_util.wrap_exceptions
def update_integration_instance(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, integration_instance_id, display_name, integration_instance_type, freeform_tags, defined_tags, is_byol, message_packs, is_file_server_enabled, is_visual_builder_enabled, custom_endpoint, alternate_custom_endpoints, if_match):

    if isinstance(integration_instance_id, six.string_types) and len(integration_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --integration-instance-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or custom_endpoint or alternate_custom_endpoints:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and custom-endpoint and alternate-custom-endpoints will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if integration_instance_type is not None:
        _details['integrationInstanceType'] = integration_instance_type

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if is_byol is not None:
        _details['isByol'] = is_byol

    if message_packs is not None:
        _details['messagePacks'] = message_packs

    if is_file_server_enabled is not None:
        _details['isFileServerEnabled'] = is_file_server_enabled

    if is_visual_builder_enabled is not None:
        _details['isVisualBuilderEnabled'] = is_visual_builder_enabled

    if custom_endpoint is not None:
        _details['customEndpoint'] = cli_util.parse_json_parameter("custom_endpoint", custom_endpoint)

    if alternate_custom_endpoints is not None:
        _details['alternateCustomEndpoints'] = cli_util.parse_json_parameter("alternate_custom_endpoints", alternate_custom_endpoints)

    client = cli_util.build_client('integration', 'integration_instance', ctx)
    result = client.update_integration_instance(
        integration_instance_id=integration_instance_id,
        update_integration_instance_details=_details,
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
