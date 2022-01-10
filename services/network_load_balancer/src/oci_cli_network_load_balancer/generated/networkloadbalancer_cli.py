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


@cli.command(cli_util.override('nlb.nlb_root_group.command_name', 'nlb'), cls=CommandGroupWithAlias, help=cli_util.override('nlb.nlb_root_group.help', """This describes the network load balancer API."""), short_help=cli_util.override('nlb.nlb_root_group.short_help', """NetworkLoadBalancer API"""))
@cli_util.help_option_group
def nlb_root_group():
    pass


@click.command(cli_util.override('nlb.listener_group.command_name', 'listener'), cls=CommandGroupWithAlias, help="""The congfiguration of the listener. For more information about backend set configuration, see [Managing Load Balancer Listeners].""")
@cli_util.help_option_group
def listener_group():
    pass


@click.command(cli_util.override('nlb.network_load_balancing_policy_group.command_name', 'network-load-balancing-policy'), cls=CommandGroupWithAlias, help="""Network load balancing policy.""")
@cli_util.help_option_group
def network_load_balancing_policy_group():
    pass


@click.command(cli_util.override('nlb.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""A log message from the running of a work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('nlb.backend_set_health_group.command_name', 'backend-set-health'), cls=CommandGroupWithAlias, help="""The health status details for a backend set.

This object does not explicitly enumerate backend servers with a status of `OK`. However, the backend sets are included in the `totalBackendCount` sum.""")
@cli_util.help_option_group
def backend_set_health_group():
    pass


@click.command(cli_util.override('nlb.health_checker_group.command_name', 'health-checker'), cls=CommandGroupWithAlias, help="""The health check policy configuration. For more information, see [Editing Health Check Policies].""")
@cli_util.help_option_group
def health_checker_group():
    pass


@click.command(cli_util.override('nlb.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""A description of work request status.""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('nlb.backend_set_summary_group.command_name', 'backend-set-summary'), cls=CommandGroupWithAlias, help="""The configuration of a network load balancer backend set. For more information about backend set configuration, see [Managing Backend Sets].

**Caution:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def backend_set_summary_group():
    pass


@click.command(cli_util.override('nlb.backend_summary_group.command_name', 'backend-summary'), cls=CommandGroupWithAlias, help="""The configuration of a backend server that is a member of a network load balancer backend set. For more information, see [Managing Backend Servers].""")
@cli_util.help_option_group
def backend_summary_group():
    pass


@click.command(cli_util.override('nlb.backend_health_group.command_name', 'backend-health'), cls=CommandGroupWithAlias, help="""The health status of the specified backend server.""")
@cli_util.help_option_group
def backend_health_group():
    pass


@click.command(cli_util.override('nlb.listener_summary_group.command_name', 'listener-summary'), cls=CommandGroupWithAlias, help="""The configuration of the listener. For more information about backend set configuration, see [Managing Load Balancer Listeners].""")
@cli_util.help_option_group
def listener_summary_group():
    pass


@click.command(cli_util.override('nlb.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while running a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('nlb.network_load_balancer_group.command_name', 'network-load-balancer'), cls=CommandGroupWithAlias, help="""The properties that define a network load balancer. For more information, see [Managing a network load balancer].

To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, contact an administrator. If you are an administrator who writes policies to give users access, then see [Getting Started with Policies].

For information about endpoints and signing API requests, see [About the API]. For information about available SDKs and tools, see [SDKS and Other Tools].""")
@cli_util.help_option_group
def network_load_balancer_group():
    pass


@click.command(cli_util.override('nlb.backend_set_group.command_name', 'backend-set'), cls=CommandGroupWithAlias, help="""The configuration of a network load balancer backend set. For more information about backend set configuration, see [Managing Backend Sets].

**Caution:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def backend_set_group():
    pass


@click.command(cli_util.override('nlb.backend_group.command_name', 'backend'), cls=CommandGroupWithAlias, help="""The configuration of a backend server that is a member of a network load balancer backend set. For more information, see [Managing Backend Servers].""")
@cli_util.help_option_group
def backend_group():
    pass


@click.command(cli_util.override('nlb.listener_protocols_group.command_name', 'listener-protocols'), cls=CommandGroupWithAlias, help="""Protocols supported for the listener of the network load balancer.""")
@cli_util.help_option_group
def listener_protocols_group():
    pass


@click.command(cli_util.override('nlb.network_load_balancer_health_group.command_name', 'network-load-balancer-health'), cls=CommandGroupWithAlias, help="""The health status details for the specified network load balancer.

This object does not explicitly enumerate backend sets with a status of `OK`. However, the backend sets are included in the `totalBackendSetCount` sum.""")
@cli_util.help_option_group
def network_load_balancer_health_group():
    pass


nlb_root_group.add_command(listener_group)
nlb_root_group.add_command(network_load_balancing_policy_group)
nlb_root_group.add_command(work_request_log_entry_group)
nlb_root_group.add_command(backend_set_health_group)
nlb_root_group.add_command(health_checker_group)
nlb_root_group.add_command(work_request_group)
nlb_root_group.add_command(backend_set_summary_group)
nlb_root_group.add_command(backend_summary_group)
nlb_root_group.add_command(backend_health_group)
nlb_root_group.add_command(listener_summary_group)
nlb_root_group.add_command(work_request_error_group)
nlb_root_group.add_command(network_load_balancer_group)
nlb_root_group.add_command(backend_set_group)
nlb_root_group.add_command(backend_group)
nlb_root_group.add_command(listener_protocols_group)
nlb_root_group.add_command(network_load_balancer_health_group)


@network_load_balancer_group.command(name=cli_util.override('nlb.change_network_load_balancer_compartment.command_name', 'change-compartment'), help=u"""Moves a network load balancer into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeNetworkLoadBalancerCompartment)""")
@cli_util.option('--network-load-balancer-id', required=True, help=u"""The [OCID] of the network load balancer to update.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to which to move the network load balancer.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the current etag value of the resource.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_network_load_balancer_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, network_load_balancer_id, compartment_id, if_match):

    if isinstance(network_load_balancer_id, six.string_types) and len(network_load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --network-load-balancer-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    result = client.change_network_load_balancer_compartment(
        network_load_balancer_id=network_load_balancer_id,
        change_network_load_balancer_compartment_details=_details,
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


@backend_group.command(name=cli_util.override('nlb.create_backend.command_name', 'create'), help=u"""Adds a backend server to a backend set. \n[Command Reference](createBackend)""")
@cli_util.option('--network-load-balancer-id', required=True, help=u"""The [OCID] of the network load balancer to update.""")
@cli_util.option('--port', required=True, type=click.INT, help=u"""The communication port for the backend server.

Example: `8080`""")
@cli_util.option('--backend-set-name', required=True, help=u"""The name of the backend set to which to add the backend server.

Example: `example_backend_set`""")
@cli_util.option('--name', help=u"""Optional unique name identifying the backend within the backend set. If not specified, then one will be generated. Example: `webServer1`""")
@cli_util.option('--ip-address', help=u"""The IP address of the backend server. Example: `10.0.0.3`""")
@cli_util.option('--target-id', help=u"""The IP OCID/Instance OCID associated with the backend server. Example: `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>`""")
@cli_util.option('--weight', type=click.INT, help=u"""The network load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted '3' receives three times the number of new connections as a server weighted '1'. For more information about load balancing policies, see [How Network Load Balancing Policies Work].

Example: `3`""")
@cli_util.option('--is-drain', type=click.BOOL, help=u"""Whether the network load balancer should drain this server. Servers marked \"isDrain\" receive no incoming traffic.

Example: `false`""")
@cli_util.option('--is-backup', type=click.BOOL, help=u"""Whether the network load balancer should treat this server as a backup unit. If `true`, then the network load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as \"isBackup\" fail the health check policy.

Example: `false`""")
@cli_util.option('--is-offline', type=click.BOOL, help=u"""Whether the network load balancer should treat this server as offline. Offline servers receive no incoming traffic.

Example: `false`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the current etag value of the resource.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def create_backend(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, network_load_balancer_id, port, backend_set_name, name, ip_address, target_id, weight, is_drain, is_backup, is_offline, if_match):

    if isinstance(network_load_balancer_id, six.string_types) and len(network_load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --network-load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['port'] = port

    if name is not None:
        _details['name'] = name

    if ip_address is not None:
        _details['ipAddress'] = ip_address

    if target_id is not None:
        _details['targetId'] = target_id

    if weight is not None:
        _details['weight'] = weight

    if is_drain is not None:
        _details['isDrain'] = is_drain

    if is_backup is not None:
        _details['isBackup'] = is_backup

    if is_offline is not None:
        _details['isOffline'] = is_offline

    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    result = client.create_backend(
        network_load_balancer_id=network_load_balancer_id,
        backend_set_name=backend_set_name,
        create_backend_details=_details,
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


@backend_set_group.command(name=cli_util.override('nlb.create_backend_set.command_name', 'create'), help=u"""Adds a backend set to a network load balancer. \n[Command Reference](createBackendSet)""")
@cli_util.option('--network-load-balancer-id', required=True, help=u"""The [OCID] of the network load balancer to update.""")
@cli_util.option('--name', required=True, help=u"""A user-friendly name for the backend set that must be unique and cannot be changed.

Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot contain spaces. Avoid entering confidential information.

Example: `example_backend_set`""")
@cli_util.option('--policy', required=True, type=custom_types.CliCaseInsensitiveChoice(["TWO_TUPLE", "THREE_TUPLE", "FIVE_TUPLE"]), help=u"""The network load balancer policy for the backend set.

Example: `FIVE_TUPLE``""")
@cli_util.option('--health-checker', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-preserve-source', type=click.BOOL, help=u"""If this parameter is enabled, then the network load balancer preserves the source IP of the packet when it is forwarded to backends. Backends see the original source IP. If the isPreserveSourceDestination parameter is enabled for the network load balancer resource, then this parameter cannot be disabled. The value is true by default.""")
@cli_util.option('--ip-version', type=custom_types.CliCaseInsensitiveChoice(["IPV4", "IPV6"]), help=u"""IP version associated with the backend set.""")
@cli_util.option('--backends', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of backends to be associated with the backend set.

This option is a JSON list with items of type BackendDetails.  For documentation on BackendDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/networkloadbalancer/20200501/datatypes/BackendDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the current etag value of the resource.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'backends': {'module': 'network_load_balancer', 'class': 'list[BackendDetails]'}, 'health-checker': {'module': 'network_load_balancer', 'class': 'HealthCheckerDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backends': {'module': 'network_load_balancer', 'class': 'list[BackendDetails]'}, 'health-checker': {'module': 'network_load_balancer', 'class': 'HealthCheckerDetails'}})
@cli_util.wrap_exceptions
def create_backend_set(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, network_load_balancer_id, name, policy, health_checker, is_preserve_source, ip_version, backends, if_match):

    if isinstance(network_load_balancer_id, six.string_types) and len(network_load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --network-load-balancer-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['policy'] = policy
    _details['healthChecker'] = cli_util.parse_json_parameter("health_checker", health_checker)

    if is_preserve_source is not None:
        _details['isPreserveSource'] = is_preserve_source

    if ip_version is not None:
        _details['ipVersion'] = ip_version

    if backends is not None:
        _details['backends'] = cli_util.parse_json_parameter("backends", backends)

    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    result = client.create_backend_set(
        network_load_balancer_id=network_load_balancer_id,
        create_backend_set_details=_details,
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


@listener_group.command(name=cli_util.override('nlb.create_listener.command_name', 'create'), help=u"""Adds a listener to a network load balancer. \n[Command Reference](createListener)""")
@cli_util.option('--network-load-balancer-id', required=True, help=u"""The [OCID] of the network load balancer to update.""")
@cli_util.option('--name', required=True, help=u"""A friendly name for the listener. It must be unique and it cannot be changed.

Example: `example_listener`""")
@cli_util.option('--default-backend-set-name', required=True, help=u"""The name of the associated backend set.

Example: `example_backend_set`""")
@cli_util.option('--port', required=True, type=click.INT, help=u"""The communication port for the listener.

Example: `80`""")
@cli_util.option('--protocol', required=True, type=custom_types.CliCaseInsensitiveChoice(["ANY", "TCP", "UDP", "TCP_AND_UDP"]), help=u"""The protocol on which the listener accepts connection requests. For public network load balancers, ANY protocol refers to TCP/UDP. For private network load balancers, ANY protocol refers to TCP/UDP/ICMP (note that ICMP requires isPreserveSourceDestination to be set to true). To get a list of valid protocols, use the [ListNetworkLoadBalancersProtocols] operation.

Example: `TCP`""")
@cli_util.option('--ip-version', type=custom_types.CliCaseInsensitiveChoice(["IPV4", "IPV6"]), help=u"""IP version associated with the listener.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the current etag value of the resource.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def create_listener(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, network_load_balancer_id, name, default_backend_set_name, port, protocol, ip_version, if_match):

    if isinstance(network_load_balancer_id, six.string_types) and len(network_load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --network-load-balancer-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['defaultBackendSetName'] = default_backend_set_name
    _details['port'] = port
    _details['protocol'] = protocol

    if ip_version is not None:
        _details['ipVersion'] = ip_version

    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    result = client.create_listener(
        network_load_balancer_id=network_load_balancer_id,
        create_listener_details=_details,
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


@network_load_balancer_group.command(name=cli_util.override('nlb.create_network_load_balancer.command_name', 'create'), help=u"""Creates a network load balancer. \n[Command Reference](createNetworkLoadBalancer)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing the network load balancer.""")
@cli_util.option('--display-name', required=True, help=u"""Network load balancer identifier, which can be renamed.""")
@cli_util.option('--subnet-id', required=True, help=u"""The subnet in which the network load balancer is spawned [OCIDs].""")
@cli_util.option('--is-preserve-source-destination', type=click.BOOL, help=u"""This parameter can be enabled only if backends are compute OCIDs. When enabled, the skipSourceDestinationCheck parameter is automatically enabled on the load balancer VNIC, and packets are sent to the backend with the entire IP header intact.""")
@cli_util.option('--reserved-ips', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of reserved Ips.

This option is a JSON list with items of type ReservedIP.  For documentation on ReservedIP please see our API reference: https://docs.cloud.oracle.com/api/#/en/networkloadbalancer/20200501/datatypes/ReservedIP.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-private', type=click.BOOL, help=u"""Whether the network load balancer has a virtual cloud network-local (private) IP address.

If \"true\", then the service assigns a private IP address to the network load balancer.

If \"false\", then the service assigns a public IP address to the network load balancer.

A public network load balancer is accessible from the internet, depending on the [security list rules] for your virtual cloud network. For more information about public and private network load balancers, see [How Network Load Balancing Works]. This value is true by default.

Example: `true`""")
@cli_util.option('--network-security-group-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of network security groups [OCIDs] associated with the network load balancer.

During the creation of the network load balancer, the service adds the new load balancer to the specified network security groups.

The benefits of associating the network load balancer with network security groups include:

*  Network security groups define network security rules to govern ingress and egress traffic for the network load balancer.

*  The network security rules of other resources can reference the network security groups associated with the network load balancer    to ensure access.

Example: [\"ocid1.nsg.oc1.phx.unique_ID\"]""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--nlb-ip-version', type=custom_types.CliCaseInsensitiveChoice(["IPV4", "IPV4_AND_IPV6"]), help=u"""IP version associated with the NLB.""")
@cli_util.option('--listeners', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Listeners associated with the network load balancer.

This option is a JSON dictionary of type dict(str, ListenerDetails).  For documentation on ListenerDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/networkloadbalancer/20200501/datatypes/ListenerDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--backend-sets', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Backend sets associated with the network load balancer.

This option is a JSON dictionary of type dict(str, BackendSetDetails).  For documentation on BackendSetDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/networkloadbalancer/20200501/datatypes/BackendSetDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'reserved-ips': {'module': 'network_load_balancer', 'class': 'list[ReservedIP]'}, 'network-security-group-ids': {'module': 'network_load_balancer', 'class': 'list[string]'}, 'listeners': {'module': 'network_load_balancer', 'class': 'dict(str, ListenerDetails)'}, 'backend-sets': {'module': 'network_load_balancer', 'class': 'dict(str, BackendSetDetails)'}, 'freeform-tags': {'module': 'network_load_balancer', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'network_load_balancer', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'reserved-ips': {'module': 'network_load_balancer', 'class': 'list[ReservedIP]'}, 'network-security-group-ids': {'module': 'network_load_balancer', 'class': 'list[string]'}, 'listeners': {'module': 'network_load_balancer', 'class': 'dict(str, ListenerDetails)'}, 'backend-sets': {'module': 'network_load_balancer', 'class': 'dict(str, BackendSetDetails)'}, 'freeform-tags': {'module': 'network_load_balancer', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'network_load_balancer', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'network_load_balancer', 'class': 'NetworkLoadBalancer'})
@cli_util.wrap_exceptions
def create_network_load_balancer(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, subnet_id, is_preserve_source_destination, reserved_ips, is_private, network_security_group_ids, nlb_ip_version, listeners, backend_sets, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['subnetId'] = subnet_id

    if is_preserve_source_destination is not None:
        _details['isPreserveSourceDestination'] = is_preserve_source_destination

    if reserved_ips is not None:
        _details['reservedIps'] = cli_util.parse_json_parameter("reserved_ips", reserved_ips)

    if is_private is not None:
        _details['isPrivate'] = is_private

    if network_security_group_ids is not None:
        _details['networkSecurityGroupIds'] = cli_util.parse_json_parameter("network_security_group_ids", network_security_group_ids)

    if nlb_ip_version is not None:
        _details['nlbIpVersion'] = nlb_ip_version

    if listeners is not None:
        _details['listeners'] = cli_util.parse_json_parameter("listeners", listeners)

    if backend_sets is not None:
        _details['backendSets'] = cli_util.parse_json_parameter("backend_sets", backend_sets)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    result = client.create_network_load_balancer(
        create_network_load_balancer_details=_details,
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


@backend_group.command(name=cli_util.override('nlb.delete_backend.command_name', 'delete'), help=u"""Removes a backend server from a given network load balancer and backend set. \n[Command Reference](deleteBackend)""")
@cli_util.option('--network-load-balancer-id', required=True, help=u"""The [OCID] of the network load balancer to update.""")
@cli_util.option('--backend-set-name', required=True, help=u"""The name of the backend set associated with the backend server.

Example: `example_backend_set`""")
@cli_util.option('--backend-name', required=True, help=u"""The name of the backend server to remove. If the backend was created with an explicitly specified name, that name should be used here. If the backend was created without explicitly specifying the name, but was created using ipAddress, this is specified as <ipAddress>:<port>. If the backend was created without explicitly specifying the name, but was created using targetId, this is specified as <targetId>:<port>.

Example: `10.0.0.3:8080` or `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>:8080`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the current etag value of the resource.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_backend(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, network_load_balancer_id, backend_set_name, backend_name, if_match):

    if isinstance(network_load_balancer_id, six.string_types) and len(network_load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --network-load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')

    if isinstance(backend_name, six.string_types) and len(backend_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    result = client.delete_backend(
        network_load_balancer_id=network_load_balancer_id,
        backend_set_name=backend_set_name,
        backend_name=backend_name,
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


@backend_set_group.command(name=cli_util.override('nlb.delete_backend_set.command_name', 'delete'), help=u"""Deletes the specified backend set. Note that deleting a backend set removes its backend servers from the network load balancer.

Before you can delete a backend set, you must remove it from any active listeners. \n[Command Reference](deleteBackendSet)""")
@cli_util.option('--network-load-balancer-id', required=True, help=u"""The [OCID] of the network load balancer to update.""")
@cli_util.option('--backend-set-name', required=True, help=u"""The name of the backend set to delete.

Example: `example_backend_set`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the current etag value of the resource.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_backend_set(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, network_load_balancer_id, backend_set_name, if_match):

    if isinstance(network_load_balancer_id, six.string_types) and len(network_load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --network-load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    result = client.delete_backend_set(
        network_load_balancer_id=network_load_balancer_id,
        backend_set_name=backend_set_name,
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


@listener_group.command(name=cli_util.override('nlb.delete_listener.command_name', 'delete'), help=u"""Deletes a listener from a network load balancer. \n[Command Reference](deleteListener)""")
@cli_util.option('--network-load-balancer-id', required=True, help=u"""The [OCID] of the network load balancer to update.""")
@cli_util.option('--listener-name', required=True, help=u"""The name of the listener to delete.

Example: `example_listener`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the current etag value of the resource.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_listener(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, network_load_balancer_id, listener_name, if_match):

    if isinstance(network_load_balancer_id, six.string_types) and len(network_load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --network-load-balancer-id cannot be whitespace or empty string')

    if isinstance(listener_name, six.string_types) and len(listener_name.strip()) == 0:
        raise click.UsageError('Parameter --listener-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    result = client.delete_listener(
        network_load_balancer_id=network_load_balancer_id,
        listener_name=listener_name,
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


@network_load_balancer_group.command(name=cli_util.override('nlb.delete_network_load_balancer.command_name', 'delete'), help=u"""Deletes a network load balancer resource by identifier. \n[Command Reference](deleteNetworkLoadBalancer)""")
@cli_util.option('--network-load-balancer-id', required=True, help=u"""The [OCID] of the network load balancer to update.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the current etag value of the resource.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_network_load_balancer(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, network_load_balancer_id, if_match):

    if isinstance(network_load_balancer_id, six.string_types) and len(network_load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --network-load-balancer-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    result = client.delete_network_load_balancer(
        network_load_balancer_id=network_load_balancer_id,
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


@backend_group.command(name=cli_util.override('nlb.get_backend.command_name', 'get'), help=u"""Retrieves the configuration information for the specified backend server. \n[Command Reference](getBackend)""")
@cli_util.option('--network-load-balancer-id', required=True, help=u"""The [OCID] of the network load balancer to update.""")
@cli_util.option('--backend-set-name', required=True, help=u"""The name of the backend set that includes the backend server.

Example: `example_backend_set`""")
@cli_util.option('--backend-name', required=True, help=u"""The name of the backend server to retrieve. If the backend was created with an explicitly specified name, that name should be used here. If the backend was created without explicitly specifying the name, but was created using ipAddress, this is specified as <ipAddress>:<port>. If the backend was created without explicitly specifying the name, but was created using targetId, this is specified as <targetId>:<port>.

Example: `10.0.0.3:8080` or `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>:8080`""")
@cli_util.option('--if-none-match', help=u"""The system returns the requested resource, with a 200 status, only if the resource has no etag matching the one specified. If the condition fails for the GET and HEAD methods, then the system returns the HTTP status code `304 (Not Modified)`.

Example: `example-etag`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'network_load_balancer', 'class': 'Backend'})
@cli_util.wrap_exceptions
def get_backend(ctx, from_json, network_load_balancer_id, backend_set_name, backend_name, if_none_match):

    if isinstance(network_load_balancer_id, six.string_types) and len(network_load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --network-load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')

    if isinstance(backend_name, six.string_types) and len(backend_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-name cannot be whitespace or empty string')

    kwargs = {}
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    result = client.get_backend(
        network_load_balancer_id=network_load_balancer_id,
        backend_set_name=backend_set_name,
        backend_name=backend_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@backend_health_group.command(name=cli_util.override('nlb.get_backend_health.command_name', 'get'), help=u"""Retrieves the current health status of the specified backend server. \n[Command Reference](getBackendHealth)""")
@cli_util.option('--network-load-balancer-id', required=True, help=u"""The [OCID] of the network load balancer to update.""")
@cli_util.option('--backend-set-name', required=True, help=u"""The name of the backend set associated with the backend server for which to retrieve the health status.

Example: `example_backend_set`""")
@cli_util.option('--backend-name', required=True, help=u"""The name of the backend server to retrieve health status for. If the backend was created with an explicitly specified name, that name should be used here. If the backend was created without explicitly specifying the name, but was created using ipAddress, this is specified as <ipAddress>:<port>. If the backend was created without explicitly specifying the name, but was created using targetId, this is specified as <targetId>:<port>.

Example: `10.0.0.3:8080` or `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>:8080`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'network_load_balancer', 'class': 'BackendHealth'})
@cli_util.wrap_exceptions
def get_backend_health(ctx, from_json, network_load_balancer_id, backend_set_name, backend_name):

    if isinstance(network_load_balancer_id, six.string_types) and len(network_load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --network-load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')

    if isinstance(backend_name, six.string_types) and len(backend_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    result = client.get_backend_health(
        network_load_balancer_id=network_load_balancer_id,
        backend_set_name=backend_set_name,
        backend_name=backend_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@backend_set_group.command(name=cli_util.override('nlb.get_backend_set.command_name', 'get'), help=u"""Retrieves the configuration information for the specified backend set. \n[Command Reference](getBackendSet)""")
@cli_util.option('--network-load-balancer-id', required=True, help=u"""The [OCID] of the network load balancer to update.""")
@cli_util.option('--backend-set-name', required=True, help=u"""The name of the backend set to retrieve.

Example: `example_backend_set`""")
@cli_util.option('--if-none-match', help=u"""The system returns the requested resource, with a 200 status, only if the resource has no etag matching the one specified. If the condition fails for the GET and HEAD methods, then the system returns the HTTP status code `304 (Not Modified)`.

Example: `example-etag`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'network_load_balancer', 'class': 'BackendSet'})
@cli_util.wrap_exceptions
def get_backend_set(ctx, from_json, network_load_balancer_id, backend_set_name, if_none_match):

    if isinstance(network_load_balancer_id, six.string_types) and len(network_load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --network-load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')

    kwargs = {}
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    result = client.get_backend_set(
        network_load_balancer_id=network_load_balancer_id,
        backend_set_name=backend_set_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@backend_set_health_group.command(name=cli_util.override('nlb.get_backend_set_health.command_name', 'get'), help=u"""Retrieves the health status for the specified backend set. \n[Command Reference](getBackendSetHealth)""")
@cli_util.option('--network-load-balancer-id', required=True, help=u"""The [OCID] of the network load balancer to update.""")
@cli_util.option('--backend-set-name', required=True, help=u"""The name of the backend set for which to retrieve the health status.

Example: `example_backend_set`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'network_load_balancer', 'class': 'BackendSetHealth'})
@cli_util.wrap_exceptions
def get_backend_set_health(ctx, from_json, network_load_balancer_id, backend_set_name):

    if isinstance(network_load_balancer_id, six.string_types) and len(network_load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --network-load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    result = client.get_backend_set_health(
        network_load_balancer_id=network_load_balancer_id,
        backend_set_name=backend_set_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@health_checker_group.command(name=cli_util.override('nlb.get_health_checker.command_name', 'get'), help=u"""Retrieves the health check policy information for a given network load balancer and backend set. \n[Command Reference](getHealthChecker)""")
@cli_util.option('--network-load-balancer-id', required=True, help=u"""The [OCID] of the network load balancer to update.""")
@cli_util.option('--backend-set-name', required=True, help=u"""The name of the backend set associated with the health check policy to be retrieved.

Example: `example_backend_set`""")
@cli_util.option('--if-none-match', help=u"""The system returns the requested resource, with a 200 status, only if the resource has no etag matching the one specified. If the condition fails for the GET and HEAD methods, then the system returns the HTTP status code `304 (Not Modified)`.

Example: `example-etag`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'network_load_balancer', 'class': 'HealthChecker'})
@cli_util.wrap_exceptions
def get_health_checker(ctx, from_json, network_load_balancer_id, backend_set_name, if_none_match):

    if isinstance(network_load_balancer_id, six.string_types) and len(network_load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --network-load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')

    kwargs = {}
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    result = client.get_health_checker(
        network_load_balancer_id=network_load_balancer_id,
        backend_set_name=backend_set_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@listener_group.command(name=cli_util.override('nlb.get_listener.command_name', 'get'), help=u"""Retrieves listener properties associated with a given network load balancer and listener name. \n[Command Reference](getListener)""")
@cli_util.option('--network-load-balancer-id', required=True, help=u"""The [OCID] of the network load balancer to update.""")
@cli_util.option('--listener-name', required=True, help=u"""The name of the listener to get.

Example: `example_listener`""")
@cli_util.option('--if-none-match', help=u"""The system returns the requested resource, with a 200 status, only if the resource has no etag matching the one specified. If the condition fails for the GET and HEAD methods, then the system returns the HTTP status code `304 (Not Modified)`.

Example: `example-etag`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'network_load_balancer', 'class': 'Listener'})
@cli_util.wrap_exceptions
def get_listener(ctx, from_json, network_load_balancer_id, listener_name, if_none_match):

    if isinstance(network_load_balancer_id, six.string_types) and len(network_load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --network-load-balancer-id cannot be whitespace or empty string')

    if isinstance(listener_name, six.string_types) and len(listener_name.strip()) == 0:
        raise click.UsageError('Parameter --listener-name cannot be whitespace or empty string')

    kwargs = {}
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    result = client.get_listener(
        network_load_balancer_id=network_load_balancer_id,
        listener_name=listener_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@network_load_balancer_group.command(name=cli_util.override('nlb.get_network_load_balancer.command_name', 'get'), help=u"""Retrieves network load balancer configuration information by identifier. \n[Command Reference](getNetworkLoadBalancer)""")
@cli_util.option('--network-load-balancer-id', required=True, help=u"""The [OCID] of the network load balancer to update.""")
@cli_util.option('--if-none-match', help=u"""The system returns the requested resource, with a 200 status, only if the resource has no etag matching the one specified. If the condition fails for the GET and HEAD methods, then the system returns the HTTP status code `304 (Not Modified)`.

Example: `example-etag`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'network_load_balancer', 'class': 'NetworkLoadBalancer'})
@cli_util.wrap_exceptions
def get_network_load_balancer(ctx, from_json, network_load_balancer_id, if_none_match):

    if isinstance(network_load_balancer_id, six.string_types) and len(network_load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --network-load-balancer-id cannot be whitespace or empty string')

    kwargs = {}
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    result = client.get_network_load_balancer(
        network_load_balancer_id=network_load_balancer_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@network_load_balancer_health_group.command(name=cli_util.override('nlb.get_network_load_balancer_health.command_name', 'get'), help=u"""Retrieves the health status for the specified network load balancer. \n[Command Reference](getNetworkLoadBalancerHealth)""")
@cli_util.option('--network-load-balancer-id', required=True, help=u"""The [OCID] of the network load balancer to update.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'network_load_balancer', 'class': 'NetworkLoadBalancerHealth'})
@cli_util.wrap_exceptions
def get_network_load_balancer_health(ctx, from_json, network_load_balancer_id):

    if isinstance(network_load_balancer_id, six.string_types) and len(network_load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --network-load-balancer-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    result = client.get_network_load_balancer_health(
        network_load_balancer_id=network_load_balancer_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('nlb.get_work_request.command_name', 'get'), help=u"""Retrieves the details of the work request with the given identifier. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The identifier of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'network_load_balancer', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@backend_set_summary_group.command(name=cli_util.override('nlb.list_backend_sets.command_name', 'list-backend-sets'), help=u"""Lists all backend sets associated with a given network load balancer. \n[Command Reference](listBackendSets)""")
@cli_util.option('--network-load-balancer-id', required=True, help=u"""The [OCID] of the network load balancer to update.""")
@cli_util.option('--if-none-match', help=u"""The system returns the requested resource, with a 200 status, only if the resource has no etag matching the one specified. If the condition fails for the GET and HEAD methods, then the system returns the HTTP status code `304 (Not Modified)`.

Example: `example-etag`""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""The page token representing the page from which to start retrieving results. For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' (ascending) or 'desc' (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order can be provided. The default order for timeCreated is descending. The default order for displayName is ascending. If no value is specified, then timeCreated is the default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'network_load_balancer', 'class': 'BackendSetCollection'})
@cli_util.wrap_exceptions
def list_backend_sets(ctx, from_json, all_pages, page_size, network_load_balancer_id, if_none_match, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(network_load_balancer_id, six.string_types) and len(network_load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --network-load-balancer-id cannot be whitespace or empty string')

    kwargs = {}
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_backend_sets,
            network_load_balancer_id=network_load_balancer_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_backend_sets,
            limit,
            page_size,
            network_load_balancer_id=network_load_balancer_id,
            **kwargs
        )
    else:
        result = client.list_backend_sets(
            network_load_balancer_id=network_load_balancer_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@backend_summary_group.command(name=cli_util.override('nlb.list_backends.command_name', 'list-backends'), help=u"""Lists the backend servers for a given network load balancer and backend set. \n[Command Reference](listBackends)""")
@cli_util.option('--network-load-balancer-id', required=True, help=u"""The [OCID] of the network load balancer to update.""")
@cli_util.option('--backend-set-name', required=True, help=u"""The name of the backend set associated with the backend servers.

Example: `example_backend_set`""")
@cli_util.option('--if-none-match', help=u"""The system returns the requested resource, with a 200 status, only if the resource has no etag matching the one specified. If the condition fails for the GET and HEAD methods, then the system returns the HTTP status code `304 (Not Modified)`.

Example: `example-etag`""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""The page token representing the page from which to start retrieving results. For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' (ascending) or 'desc' (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order can be provided. The default order for timeCreated is descending. The default order for displayName is ascending. If no value is specified, then timeCreated is the default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'network_load_balancer', 'class': 'BackendCollection'})
@cli_util.wrap_exceptions
def list_backends(ctx, from_json, all_pages, page_size, network_load_balancer_id, backend_set_name, if_none_match, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(network_load_balancer_id, six.string_types) and len(network_load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --network-load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')

    kwargs = {}
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_backends,
            network_load_balancer_id=network_load_balancer_id,
            backend_set_name=backend_set_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_backends,
            limit,
            page_size,
            network_load_balancer_id=network_load_balancer_id,
            backend_set_name=backend_set_name,
            **kwargs
        )
    else:
        result = client.list_backends(
            network_load_balancer_id=network_load_balancer_id,
            backend_set_name=backend_set_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@listener_summary_group.command(name=cli_util.override('nlb.list_listeners.command_name', 'list-listeners'), help=u"""Lists all listeners associated with a given network load balancer. \n[Command Reference](listListeners)""")
@cli_util.option('--network-load-balancer-id', required=True, help=u"""The [OCID] of the network load balancer to update.""")
@cli_util.option('--if-none-match', help=u"""The system returns the requested resource, with a 200 status, only if the resource has no etag matching the one specified. If the condition fails for the GET and HEAD methods, then the system returns the HTTP status code `304 (Not Modified)`.

Example: `example-etag`""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""The page token representing the page from which to start retrieving results. For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' (ascending) or 'desc' (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order can be provided. The default order for timeCreated is descending. The default order for displayName is ascending. If no value is specified, then timeCreated is the default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'network_load_balancer', 'class': 'ListenerCollection'})
@cli_util.wrap_exceptions
def list_listeners(ctx, from_json, all_pages, page_size, network_load_balancer_id, if_none_match, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(network_load_balancer_id, six.string_types) and len(network_load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --network-load-balancer-id cannot be whitespace or empty string')

    kwargs = {}
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_listeners,
            network_load_balancer_id=network_load_balancer_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_listeners,
            limit,
            page_size,
            network_load_balancer_id=network_load_balancer_id,
            **kwargs
        )
    else:
        result = client.list_listeners(
            network_load_balancer_id=network_load_balancer_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@network_load_balancer_health_group.command(name=cli_util.override('nlb.list_network_load_balancer_healths.command_name', 'list'), help=u"""Lists the summary health statuses for all network load balancers in the specified compartment. \n[Command Reference](listNetworkLoadBalancerHealths)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing the network load balancers to list.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' (ascending) or 'desc' (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order can be provided. The default order for timeCreated is descending. The default order for displayName is ascending. If no value is specified, then timeCreated is the default.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""The page token representing the page from which to start retrieving results. For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'network_load_balancer', 'class': 'NetworkLoadBalancerHealthCollection'})
@cli_util.wrap_exceptions
def list_network_load_balancer_healths(ctx, from_json, all_pages, page_size, compartment_id, sort_order, sort_by, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_network_load_balancer_healths,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_network_load_balancer_healths,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_network_load_balancer_healths(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@network_load_balancer_group.command(name=cli_util.override('nlb.list_network_load_balancers.command_name', 'list'), help=u"""Returns a list of network load balancers. \n[Command Reference](listNetworkLoadBalancers)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing the network load balancers to list.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources that match the given lifecycle state.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""The page token representing the page from which to start retrieving results. For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' (ascending) or 'desc' (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order can be provided. The default order for timeCreated is descending. The default order for displayName is ascending. If no value is specified, then timeCreated is the default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'network_load_balancer', 'class': 'NetworkLoadBalancerCollection'})
@cli_util.wrap_exceptions
def list_network_load_balancers(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, display_name, limit, page, sort_order, sort_by):

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
    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_network_load_balancers,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_network_load_balancers,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_network_load_balancers(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@network_load_balancing_policy_group.command(name=cli_util.override('nlb.list_network_load_balancers_policies.command_name', 'list-network-load-balancers-policies'), help=u"""Lists the available network load balancer policies. \n[Command Reference](listNetworkLoadBalancersPolicies)""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""The page token representing the page from which to start retrieving results. For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' (ascending) or 'desc' (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order can be provided. The default order for timeCreated is descending. The default order for displayName is ascending. If no value is specified, then timeCreated is the default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'network_load_balancer', 'class': 'NetworkLoadBalancersPolicyCollection'})
@cli_util.wrap_exceptions
def list_network_load_balancers_policies(ctx, from_json, all_pages, page_size, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_network_load_balancers_policies,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_network_load_balancers_policies,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_network_load_balancers_policies(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@listener_protocols_group.command(name=cli_util.override('nlb.list_network_load_balancers_protocols.command_name', 'list-network-load-balancers-protocols'), help=u"""This API has been deprecated so it won't return the updated list of supported protocls. Lists all supported traffic protocols. \n[Command Reference](listNetworkLoadBalancersProtocols)""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""The page token representing the page from which to start retrieving results. For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' (ascending) or 'desc' (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order can be provided. The default order for timeCreated is descending. The default order for displayName is ascending. If no value is specified, then timeCreated is the default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'network_load_balancer', 'class': 'NetworkLoadBalancersProtocolCollection'})
@cli_util.wrap_exceptions
def list_network_load_balancers_protocols(ctx, from_json, all_pages, page_size, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_network_load_balancers_protocols,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_network_load_balancers_protocols,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_network_load_balancers_protocols(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('nlb.list_work_request_errors.command_name', 'list'), help=u"""Return a (paginated) list of errors for a given work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The identifier of the asynchronous request.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing the network load balancers to list.""")
@cli_util.option('--page', help=u"""The page token representing the page from which to start retrieving results. For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'network_load_balancer', 'class': 'WorkRequestErrorCollection'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, compartment_id, page, limit):

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
    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_errors,
            work_request_id=work_request_id,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_errors,
            limit,
            page_size,
            work_request_id=work_request_id,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_work_request_errors(
            work_request_id=work_request_id,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_log_entry_group.command(name=cli_util.override('nlb.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Returns a (paginated) list of logs for a given work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The identifier of the asynchronous request.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing the network load balancers to list.""")
@cli_util.option('--page', help=u"""The page token representing the page from which to start retrieving results. For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'network_load_balancer', 'class': 'WorkRequestLogEntryCollection'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, compartment_id, page, limit):

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
    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_logs,
            work_request_id=work_request_id,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_logs,
            limit,
            page_size,
            work_request_id=work_request_id,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_work_request_logs(
            work_request_id=work_request_id,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('nlb.list_work_requests.command_name', 'list'), help=u"""Lists all work requests. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing the network load balancers to list.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""The page token representing the page from which to start retrieving results. For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'network_load_balancer', 'class': 'WorkRequestCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
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


@backend_group.command(name=cli_util.override('nlb.update_backend.command_name', 'update'), help=u"""Updates the configuration of a backend server within the specified backend set. \n[Command Reference](updateBackend)""")
@cli_util.option('--network-load-balancer-id', required=True, help=u"""The [OCID] of the network load balancer to update.""")
@cli_util.option('--backend-set-name', required=True, help=u"""The name of the backend set associated with the backend server.

Example: `example_backend_set`""")
@cli_util.option('--backend-name', required=True, help=u"""The name of the backend server to update. If the backend was created with an explicitly specified name, that name should be used here. If the backend was created without explicitly specifying the name, but was created using ipAddress, this is specified as <ipAddress>:<port>. If the backend was created without explicitly specifying the name, but was created using targetId, this is specified as <targetId>:<port>.

Example: `10.0.0.3:8080` or `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>:8080`""")
@cli_util.option('--weight', type=click.INT, help=u"""The load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted '3' receives three times the number of new connections as a server weighted '1'. For more information about load balancing policies, see [How Load Balancing Policies Work].

Example: `3`""")
@cli_util.option('--is-backup', type=click.BOOL, help=u"""Whether the network load balancer should treat this server as a backup unit. If `true`, then the network load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as \"isBackup\" fail the health check policy.

Example: `false`""")
@cli_util.option('--is-drain', type=click.BOOL, help=u"""Whether the network load balancer should drain this server. Servers marked \"isDrain\" receive no incoming traffic.

Example: `false`""")
@cli_util.option('--is-offline', type=click.BOOL, help=u"""Whether the network load balancer should treat this server as offline. Offline servers receive no incoming traffic.

Example: `false`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the current etag value of the resource.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_backend(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, network_load_balancer_id, backend_set_name, backend_name, weight, is_backup, is_drain, is_offline, if_match):

    if isinstance(network_load_balancer_id, six.string_types) and len(network_load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --network-load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')

    if isinstance(backend_name, six.string_types) and len(backend_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if weight is not None:
        _details['weight'] = weight

    if is_backup is not None:
        _details['isBackup'] = is_backup

    if is_drain is not None:
        _details['isDrain'] = is_drain

    if is_offline is not None:
        _details['isOffline'] = is_offline

    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    result = client.update_backend(
        network_load_balancer_id=network_load_balancer_id,
        backend_set_name=backend_set_name,
        backend_name=backend_name,
        update_backend_details=_details,
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


@backend_set_group.command(name=cli_util.override('nlb.update_backend_set.command_name', 'update'), help=u"""Updates a backend set. \n[Command Reference](updateBackendSet)""")
@cli_util.option('--network-load-balancer-id', required=True, help=u"""The [OCID] of the network load balancer to update.""")
@cli_util.option('--backend-set-name', required=True, help=u"""The name of the backend set to update.

Example: `example_backend_set`""")
@cli_util.option('--policy', help=u"""The network load balancer policy for the backend set. To get a list of available policies, use the [ListNetworkLoadBalancersPolicies] operation.

Example: `FIVE_TUPLE`""")
@cli_util.option('--is-preserve-source', type=click.BOOL, help=u"""If this parameter is enabled, then the network load balancer preserves the source IP of the packet when it is forwarded to backends. Backends see the original source IP. If the isPreserveSourceDestination parameter is enabled for the network load balancer resource, then this parameter cannot be disabled. The value is true by default.""")
@cli_util.option('--ip-version', type=custom_types.CliCaseInsensitiveChoice(["IPV4", "IPV6"]), help=u"""The IP version associated with the backend set.""")
@cli_util.option('--backends', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of backends associated with the backend set.

This option is a JSON list with items of type BackendDetails.  For documentation on BackendDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/networkloadbalancer/20200501/datatypes/BackendDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--health-checker', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the current etag value of the resource.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'backends': {'module': 'network_load_balancer', 'class': 'list[BackendDetails]'}, 'health-checker': {'module': 'network_load_balancer', 'class': 'HealthCheckerDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backends': {'module': 'network_load_balancer', 'class': 'list[BackendDetails]'}, 'health-checker': {'module': 'network_load_balancer', 'class': 'HealthCheckerDetails'}})
@cli_util.wrap_exceptions
def update_backend_set(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, network_load_balancer_id, backend_set_name, policy, is_preserve_source, ip_version, backends, health_checker, if_match):

    if isinstance(network_load_balancer_id, six.string_types) and len(network_load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --network-load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')
    if not force:
        if backends or health_checker:
            if not click.confirm("WARNING: Updates to backends and health-checker will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if policy is not None:
        _details['policy'] = policy

    if is_preserve_source is not None:
        _details['isPreserveSource'] = is_preserve_source

    if ip_version is not None:
        _details['ipVersion'] = ip_version

    if backends is not None:
        _details['backends'] = cli_util.parse_json_parameter("backends", backends)

    if health_checker is not None:
        _details['healthChecker'] = cli_util.parse_json_parameter("health_checker", health_checker)

    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    result = client.update_backend_set(
        network_load_balancer_id=network_load_balancer_id,
        backend_set_name=backend_set_name,
        update_backend_set_details=_details,
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


@health_checker_group.command(name=cli_util.override('nlb.update_health_checker.command_name', 'update'), help=u"""Updates the health check policy for a given network load balancer and backend set. \n[Command Reference](updateHealthChecker)""")
@cli_util.option('--network-load-balancer-id', required=True, help=u"""The [OCID] of the network load balancer to update.""")
@cli_util.option('--backend-set-name', required=True, help=u"""The name of the backend set associated with the health check policy to be retrieved.

Example: `example_backend_set`""")
@cli_util.option('--protocol', type=custom_types.CliCaseInsensitiveChoice(["HTTP", "HTTPS", "TCP", "UDP"]), help=u"""The protocol that the health check must use; either HTTP, UDP, or TCP.

Example: `HTTP`""")
@cli_util.option('--port', type=click.INT, help=u"""The backend server port against which to run the health check.

Example: `8080`""")
@cli_util.option('--retries', type=click.INT, help=u"""The number of retries to attempt before a backend server is considered \"unhealthy\". This number also applies when recovering a server to the \"healthy\" state.

Example: `3`""")
@cli_util.option('--timeout-in-millis', type=click.INT, help=u"""The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply returns within this timeout period.

Example: `3000`""")
@cli_util.option('--interval-in-millis', type=click.INT, help=u"""The interval between health checks, in milliseconds.

Example: `10000`""")
@cli_util.option('--url-path', help=u"""The path against which to run the health check.

Example: `/healthcheck`""")
@cli_util.option('--response-body-regex', help=u"""A regular expression for parsing the response body from the backend server.

Example: `^((?!false).|\\s)*$`""")
@cli_util.option('--return-code', type=click.INT, help=u"""The status code a healthy backend server should return. If you configure the health check policy to use the HTTP protocol, then you can use common HTTP status codes such as \"200\".

Example: `200`""")
@cli_util.option('--request-data', help=u"""Base64 encoded pattern to be sent as UDP or TCP health check probe.""")
@cli_util.option('--response-data', help=u"""Base64 encoded pattern to be validated as UDP or TCP health check probe response.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the current etag value of the resource.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_health_checker(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, network_load_balancer_id, backend_set_name, protocol, port, retries, timeout_in_millis, interval_in_millis, url_path, response_body_regex, return_code, request_data, response_data, if_match):

    if isinstance(network_load_balancer_id, six.string_types) and len(network_load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --network-load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if protocol is not None:
        _details['protocol'] = protocol

    if port is not None:
        _details['port'] = port

    if retries is not None:
        _details['retries'] = retries

    if timeout_in_millis is not None:
        _details['timeoutInMillis'] = timeout_in_millis

    if interval_in_millis is not None:
        _details['intervalInMillis'] = interval_in_millis

    if url_path is not None:
        _details['urlPath'] = url_path

    if response_body_regex is not None:
        _details['responseBodyRegex'] = response_body_regex

    if return_code is not None:
        _details['returnCode'] = return_code

    if request_data is not None:
        _details['requestData'] = request_data

    if response_data is not None:
        _details['responseData'] = response_data

    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    result = client.update_health_checker(
        network_load_balancer_id=network_load_balancer_id,
        backend_set_name=backend_set_name,
        update_health_checker_details=_details,
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


@listener_group.command(name=cli_util.override('nlb.update_listener.command_name', 'update'), help=u"""Updates a listener for a given network load balancer. \n[Command Reference](updateListener)""")
@cli_util.option('--network-load-balancer-id', required=True, help=u"""The [OCID] of the network load balancer to update.""")
@cli_util.option('--listener-name', required=True, help=u"""The name of the listener to update.

Example: `example_listener`""")
@cli_util.option('--default-backend-set-name', help=u"""The name of the associated backend set.

Example: `example_backend_set`""")
@cli_util.option('--port', type=click.INT, help=u"""The communication port for the listener.

Example: `80`""")
@cli_util.option('--protocol', type=custom_types.CliCaseInsensitiveChoice(["ANY", "TCP", "UDP", "TCP_AND_UDP"]), help=u"""The protocol on which the listener accepts connection requests. For public network load balancers, ANY protocol refers to TCP/UDP. For private network load balancers, ANY protocol refers to TCP/UDP/ICMP (note that ICMP requires isPreserveSourceDestination to be set to true). To get a list of valid protocols, use the [ListNetworkLoadBalancersProtocols] operation.

Example: `TCP`""")
@cli_util.option('--ip-version', type=custom_types.CliCaseInsensitiveChoice(["IPV4", "IPV6"]), help=u"""IP version associated with the listener.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the current etag value of the resource.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_listener(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, network_load_balancer_id, listener_name, default_backend_set_name, port, protocol, ip_version, if_match):

    if isinstance(network_load_balancer_id, six.string_types) and len(network_load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --network-load-balancer-id cannot be whitespace or empty string')

    if isinstance(listener_name, six.string_types) and len(listener_name.strip()) == 0:
        raise click.UsageError('Parameter --listener-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if default_backend_set_name is not None:
        _details['defaultBackendSetName'] = default_backend_set_name

    if port is not None:
        _details['port'] = port

    if protocol is not None:
        _details['protocol'] = protocol

    if ip_version is not None:
        _details['ipVersion'] = ip_version

    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    result = client.update_listener(
        network_load_balancer_id=network_load_balancer_id,
        listener_name=listener_name,
        update_listener_details=_details,
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


@network_load_balancer_group.command(name=cli_util.override('nlb.update_network_load_balancer.command_name', 'update'), help=u"""Updates the network load balancer \n[Command Reference](updateNetworkLoadBalancer)""")
@cli_util.option('--network-load-balancer-id', required=True, help=u"""The [OCID] of the network load balancer to update.""")
@cli_util.option('--display-name', help=u"""The user-friendly display name for the network load balancer, which does not have to be unique and can be changed. Avoid entering confidential information.

Example: `example_network_load_balancer`""")
@cli_util.option('--is-preserve-source-destination', type=click.BOOL, help=u"""This parameter can be enabled only if backends are compute OCIDs. When enabled, the skipSourceDestinationCheck parameter is automatically enabled on the load balancer VNIC, and packets are sent to the backend with the entire IP header intact.""")
@cli_util.option('--nlb-ip-version', type=custom_types.CliCaseInsensitiveChoice(["IPV4", "IPV4_AND_IPV6"]), help=u"""IP version associated with the NLB.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the current etag value of the resource.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'network_load_balancer', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'network_load_balancer', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'network_load_balancer', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'network_load_balancer', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_network_load_balancer(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, network_load_balancer_id, display_name, is_preserve_source_destination, nlb_ip_version, freeform_tags, defined_tags, if_match):

    if isinstance(network_load_balancer_id, six.string_types) and len(network_load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --network-load-balancer-id cannot be whitespace or empty string')
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

    if is_preserve_source_destination is not None:
        _details['isPreserveSourceDestination'] = is_preserve_source_destination

    if nlb_ip_version is not None:
        _details['nlbIpVersion'] = nlb_ip_version

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    result = client.update_network_load_balancer(
        network_load_balancer_id=network_load_balancer_id,
        update_network_load_balancer_details=_details,
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


@network_load_balancer_group.command(name=cli_util.override('nlb.update_network_security_groups.command_name', 'update-network-security-groups'), help=u"""Updates the network security groups associated with the specified network load balancer. \n[Command Reference](updateNetworkSecurityGroups)""")
@cli_util.option('--network-load-balancer-id', required=True, help=u"""The [OCID] of the network load balancer to update.""")
@cli_util.option('--network-security-group-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of network security group [OCIDs] associated with the network load balancer.

During the creation of the network load balancer, the service adds the new network load balancer to the specified network security groups.

The benefits of associating the network load balancer with network security groups include:

*  Network security groups define network security rules to govern ingress and egress traffic for the network load balancer.

*  The network security rules of other resources can reference the network security groups associated with the network load balancer    to ensure access.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the current etag value of the resource.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'network-security-group-ids': {'module': 'network_load_balancer', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'network-security-group-ids': {'module': 'network_load_balancer', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_network_security_groups(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, network_load_balancer_id, network_security_group_ids, if_match):

    if isinstance(network_load_balancer_id, six.string_types) and len(network_load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --network-load-balancer-id cannot be whitespace or empty string')
    if not force:
        if network_security_group_ids:
            if not click.confirm("WARNING: Updates to network-security-group-ids will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if network_security_group_ids is not None:
        _details['networkSecurityGroupIds'] = cli_util.parse_json_parameter("network_security_group_ids", network_security_group_ids)

    client = cli_util.build_client('network_load_balancer', 'network_load_balancer', ctx)
    result = client.update_network_security_groups(
        network_load_balancer_id=network_load_balancer_id,
        update_network_security_groups_details=_details,
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
