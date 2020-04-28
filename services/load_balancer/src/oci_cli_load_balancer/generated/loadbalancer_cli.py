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


@cli.command(cli_util.override('lb.lb_root_group.command_name', 'lb'), cls=CommandGroupWithAlias, help=cli_util.override('lb.lb_root_group.help', """API for the Load Balancing service. Use this API to manage load balancers, backend sets, and related items. For more
information, see [Overview of Load Balancing]."""), short_help=cli_util.override('lb.lb_root_group.short_help', """Load Balancing API"""))
@cli_util.help_option_group
def lb_root_group():
    pass


@click.command(cli_util.override('lb.load_balancer_group.command_name', 'load-balancer'), cls=CommandGroupWithAlias, help="""The properties that define a load balancer. For more information, see [Managing a Load Balancer].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

For information about endpoints and signing API requests, see [About the API]. For information about available SDKs and tools, see [SDKS and Other Tools].""")
@cli_util.help_option_group
def load_balancer_group():
    pass


@click.command(cli_util.override('lb.load_balancer_shape_group.command_name', 'load-balancer-shape'), cls=CommandGroupWithAlias, help="""A shape is a template that determines the total pre-provisioned bandwidth (ingress plus egress) for the load balancer.

Note that the pre-provisioned maximum capacity applies to aggregated connections, not to a single client attempting to use the full bandwidth.""")
@cli_util.help_option_group
def load_balancer_shape_group():
    pass


@click.command(cli_util.override('lb.certificate_group.command_name', 'certificate'), cls=CommandGroupWithAlias, help="""The configuration details of a certificate bundle. For more information on SSL certficate configuration, see [Managing SSL Certificates].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def certificate_group():
    pass


@click.command(cli_util.override('lb.listener_group.command_name', 'listener'), cls=CommandGroupWithAlias, help="""The listener's configuration. For more information on backend set configuration, see [Managing Load Balancer Listeners].""")
@cli_util.help_option_group
def listener_group():
    pass


@click.command(cli_util.override('lb.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""Many of the API requests you use to create and configure load balancing do not take effect immediately. In these cases, the request spawns an asynchronous work flow to fulfill the request. WorkRequest objects provide visibility for in-progress work flows. For more information about work requests, see [Viewing the State of a Work Request].""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('lb.backend_set_health_group.command_name', 'backend-set-health'), cls=CommandGroupWithAlias, help="""The health status details for a backend set.

This object does not explicitly enumerate backend servers with a status of `OK`. However, they are included in the `totalBackendCount` sum.""")
@cli_util.help_option_group
def backend_set_health_group():
    pass


@click.command(cli_util.override('lb.health_checker_group.command_name', 'health-checker'), cls=CommandGroupWithAlias, help="""The health check policy configuration. For more information, see [Editing Health Check Policies].""")
@cli_util.help_option_group
def health_checker_group():
    pass


@click.command(cli_util.override('lb.path_route_set_group.command_name', 'path-route-set'), cls=CommandGroupWithAlias, help="""A named set of path route rules. For more information, see [Managing Request Routing].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def path_route_set_group():
    pass


@click.command(cli_util.override('lb.load_balancer_protocol_group.command_name', 'load-balancer-protocol'), cls=CommandGroupWithAlias, help="""A protocol that defines the type of traffic accepted by a listener.""")
@cli_util.help_option_group
def load_balancer_protocol_group():
    pass


@click.command(cli_util.override('lb.listener_rule_group.command_name', 'listener-rule'), cls=CommandGroupWithAlias, help="""The attributes of a rule associated with the specified listener, and the name of the rule set that the rule belongs to.""")
@cli_util.help_option_group
def listener_rule_group():
    pass


@click.command(cli_util.override('lb.load_balancer_health_group.command_name', 'load-balancer-health'), cls=CommandGroupWithAlias, help="""The health status details for the specified load balancer.

This object does not explicitly enumerate backend sets with a status of `OK`. However, they are included in the `totalBackendSetCount` sum.""")
@cli_util.help_option_group
def load_balancer_health_group():
    pass


@click.command(cli_util.override('lb.hostname_group.command_name', 'hostname'), cls=CommandGroupWithAlias, help="""A hostname resource associated with a load balancer for use by one or more listeners.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def hostname_group():
    pass


@click.command(cli_util.override('lb.load_balancer_policy_group.command_name', 'load-balancer-policy'), cls=CommandGroupWithAlias, help="""A policy that determines how traffic is distributed among backend servers. For more information on load balancing policies, see [How Load Balancing Policies Work].""")
@cli_util.help_option_group
def load_balancer_policy_group():
    pass


@click.command(cli_util.override('lb.backend_health_group.command_name', 'backend-health'), cls=CommandGroupWithAlias, help="""The health status of the specified backend server as reported by the primary and standby load balancers.""")
@cli_util.help_option_group
def backend_health_group():
    pass


@click.command(cli_util.override('lb.rule_set_group.command_name', 'rule-set'), cls=CommandGroupWithAlias, help="""A named set of rules associated with a load balancer. Rules are objects that represent actions to apply to a listener, such as adding, altering, or removing HTTP headers. For more information, see [Managing Rule Sets].""")
@cli_util.help_option_group
def rule_set_group():
    pass


@click.command(cli_util.override('lb.backend_set_group.command_name', 'backend-set'), cls=CommandGroupWithAlias, help="""The configuration of a load balancer backend set. For more information on backend set configuration, see [Managing Backend Sets].

**Note:** The `sessionPersistenceConfiguration` (application cookie stickiness) and `lbCookieSessionPersistenceConfiguration` (LB cookie stickiness) attributes are mutually exclusive. To avoid returning an error, configure only one of these two attributes per backend set.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def backend_set_group():
    pass


@click.command(cli_util.override('lb.backend_group.command_name', 'backend'), cls=CommandGroupWithAlias, help="""The configuration of a backend server that is a member of a load balancer backend set. For more information, see [Managing Backend Servers].""")
@cli_util.help_option_group
def backend_group():
    pass


@click.command(cli_util.override('lb.network_security_groups_group.command_name', 'network-security-groups'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def network_security_groups_group():
    pass


lb_root_group.add_command(load_balancer_group)
lb_root_group.add_command(load_balancer_shape_group)
lb_root_group.add_command(certificate_group)
lb_root_group.add_command(listener_group)
lb_root_group.add_command(work_request_group)
lb_root_group.add_command(backend_set_health_group)
lb_root_group.add_command(health_checker_group)
lb_root_group.add_command(path_route_set_group)
lb_root_group.add_command(load_balancer_protocol_group)
lb_root_group.add_command(listener_rule_group)
lb_root_group.add_command(load_balancer_health_group)
lb_root_group.add_command(hostname_group)
lb_root_group.add_command(load_balancer_policy_group)
lb_root_group.add_command(backend_health_group)
lb_root_group.add_command(rule_set_group)
lb_root_group.add_command(backend_set_group)
lb_root_group.add_command(backend_group)
lb_root_group.add_command(network_security_groups_group)


@load_balancer_group.command(name=cli_util.override('lb.change_load_balancer_compartment.command_name', 'change-compartment'), help=u"""Moves a load balancer into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment].""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer to move.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the load balancer to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. Set the if-match parameter to the value of the ETag from a previous GET or POST response for that resource. The resource is moved only if the ETag you provide matches the resource's current ETag value.

Example: `example-etag`""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_load_balancer_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, load_balancer_id, compartment_id, if_match):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.change_load_balancer_compartment(
        load_balancer_id=load_balancer_id,
        change_load_balancer_compartment_details=_details,
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
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@backend_group.command(name=cli_util.override('lb.create_backend.command_name', 'create'), help=u"""Adds a backend server to a backend set.""")
@cli_util.option('--ip-address', required=True, help=u"""The IP address of the backend server.

Example: `10.0.0.3`""")
@cli_util.option('--port', required=True, type=click.INT, help=u"""The communication port for the backend server.

Example: `8080`""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer associated with the backend set and servers.""")
@cli_util.option('--backend-set-name', required=True, help=u"""The name of the backend set to add the backend server to.

Example: `example_backend_set`""")
@cli_util.option('--weight', type=click.INT, help=u"""The load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted '3' receives 3 times the number of new connections as a server weighted '1'. For more information on load balancing policies, see [How Load Balancing Policies Work].

Example: `3`""")
@cli_util.option('--backup', type=click.BOOL, help=u"""Whether the load balancer should treat this server as a backup unit. If `true`, the load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as \"backup\" fail the health check policy.

**Note:** You cannot add a backend server marked as `backup` to a backend set that uses the IP Hash policy.

Example: `false`""")
@cli_util.option('--drain', type=click.BOOL, help=u"""Whether the load balancer should drain this server. Servers marked \"drain\" receive no new incoming traffic.

Example: `false`""")
@cli_util.option('--offline', type=click.BOOL, help=u"""Whether the load balancer should treat this server as offline. Offline servers receive no incoming traffic.

Example: `false`""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def create_backend(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, ip_address, port, load_balancer_id, backend_set_name, weight, backup, drain, offline):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['ipAddress'] = ip_address
    _details['port'] = port

    if weight is not None:
        _details['weight'] = weight

    if backup is not None:
        _details['backup'] = backup

    if drain is not None:
        _details['drain'] = drain

    if offline is not None:
        _details['offline'] = offline

    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.create_backend(
        load_balancer_id=load_balancer_id,
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
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@backend_set_group.command(name=cli_util.override('lb.create_backend_set.command_name', 'create'), help=u"""Adds a backend set to a load balancer.""")
@cli_util.option('--name', required=True, help=u"""A friendly name for the backend set. It must be unique and it cannot be changed.

Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot contain spaces. Avoid entering confidential information.

Example: `example_backend_set`""")
@cli_util.option('--policy', required=True, help=u"""The load balancer policy for the backend set. To get a list of available policies, use the [ListPolicies] operation.

Example: `LEAST_CONNECTIONS`""")
@cli_util.option('--health-checker', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer on which to add a backend set.""")
@cli_util.option('--backends', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON list with items of type BackendDetails.  For documentation on BackendDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/loadbalancer/20170115/datatypes/BackendDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ssl-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--session-persistence-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--lb-cookie-session-persistence-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'backends': {'module': 'load_balancer', 'class': 'list[BackendDetails]'}, 'health-checker': {'module': 'load_balancer', 'class': 'HealthCheckerDetails'}, 'ssl-configuration': {'module': 'load_balancer', 'class': 'SSLConfigurationDetails'}, 'session-persistence-configuration': {'module': 'load_balancer', 'class': 'SessionPersistenceConfigurationDetails'}, 'lb-cookie-session-persistence-configuration': {'module': 'load_balancer', 'class': 'LBCookieSessionPersistenceConfigurationDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backends': {'module': 'load_balancer', 'class': 'list[BackendDetails]'}, 'health-checker': {'module': 'load_balancer', 'class': 'HealthCheckerDetails'}, 'ssl-configuration': {'module': 'load_balancer', 'class': 'SSLConfigurationDetails'}, 'session-persistence-configuration': {'module': 'load_balancer', 'class': 'SessionPersistenceConfigurationDetails'}, 'lb-cookie-session-persistence-configuration': {'module': 'load_balancer', 'class': 'LBCookieSessionPersistenceConfigurationDetails'}})
@cli_util.wrap_exceptions
def create_backend_set(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, policy, health_checker, load_balancer_id, backends, ssl_configuration, session_persistence_configuration, lb_cookie_session_persistence_configuration):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['policy'] = policy
    _details['healthChecker'] = cli_util.parse_json_parameter("health_checker", health_checker)

    if backends is not None:
        _details['backends'] = cli_util.parse_json_parameter("backends", backends)

    if ssl_configuration is not None:
        _details['sslConfiguration'] = cli_util.parse_json_parameter("ssl_configuration", ssl_configuration)

    if session_persistence_configuration is not None:
        _details['sessionPersistenceConfiguration'] = cli_util.parse_json_parameter("session_persistence_configuration", session_persistence_configuration)

    if lb_cookie_session_persistence_configuration is not None:
        _details['lbCookieSessionPersistenceConfiguration'] = cli_util.parse_json_parameter("lb_cookie_session_persistence_configuration", lb_cookie_session_persistence_configuration)

    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.create_backend_set(
        load_balancer_id=load_balancer_id,
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
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@certificate_group.command(name=cli_util.override('lb.create_certificate.command_name', 'create'), help=u"""Creates an asynchronous request to add an SSL certificate bundle.""")
@cli_util.option('--certificate-name', required=True, help=u"""A friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores. Certificate bundle names cannot contain spaces. Avoid entering confidential information.

Example: `example_certificate_bundle`""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer on which to add the certificate bundle.""")
@cli_util.option('--passphrase', help=u"""A passphrase for encrypted private keys. This is needed only if you created your certificate with a passphrase.""")
@cli_util.option('--private-key', help=u"""The SSL private key for your certificate, in PEM format.

Example:

    -----BEGIN RSA PRIVATE KEY-----     jO1O1v2ftXMsawM90tnXwc6xhOAT1gDBC9S8DKeca..JZNUgYYwNS0dP2UK     tmyN+XqVcAKw4HqVmChXy5b5msu8eIq3uc2NqNVtR..2ksSLukP8pxXcHyb     +sEwvM4uf8qbnHAqwnOnP9+KV9vds6BaH1eRA4CHz..n+NVZlzBsTxTlS16     /Umr7wJzVrMqK5sDiSu4WuaaBdqMGfL5hLsTjcBFD..Da2iyQmSKuVD4lIZ     ...     -----END RSA PRIVATE KEY-----""")
@cli_util.option('--public-certificate', help=u"""The public certificate, in PEM format, that you received from your SSL certificate provider.

Example:

    -----BEGIN CERTIFICATE-----     MIIC2jCCAkMCAg38MA0GCSqGSIb3DQEBBQUAMIGbM..QswCQYDVQQGEwJKU     A1UECBMFVG9reW8xEDAOBgNVBAcTB0NodW8ta3UxE..TAPBgNVBAoTCEZyY     MRgwFgYDVQQLEw9XZWJDZXJ0IFN1cHBvcnQxGDAWB..gNVBAMTD0ZyYW5rN     YiBDQTEjMCEGCSqGSIb3DQEJARYUc3VwcG9ydEBmc..mFuazRkZC5jb20wH     ...     -----END CERTIFICATE-----""")
@cli_util.option('--ca-certificate', help=u"""The Certificate Authority certificate, or any interim certificate, that you received from your SSL certificate provider.

Example:

    -----BEGIN CERTIFICATE-----     MIIEczCCA1ugAwIBAgIBADANBgkqhkiG9w0BAQQFAD..AkGA1UEBhMCR0Ix     EzARBgNVBAgTClNvbWUtU3RhdGUxFDASBgNVBAoTC0..0EgTHRkMTcwNQYD     VQQLEy5DbGFzcyAxIFB1YmxpYyBQcmltYXJ5IENlcn..XRpb24gQXV0aG9y     aXR5MRQwEgYDVQQDEwtCZXN0IENBIEx0ZDAeFw0wMD..TUwMTZaFw0wMTAy     ...     -----END CERTIFICATE-----""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def create_certificate(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, certificate_name, load_balancer_id, passphrase, private_key, public_certificate, ca_certificate):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['certificateName'] = certificate_name

    if passphrase is not None:
        _details['passphrase'] = passphrase

    if private_key is not None:
        _details['privateKey'] = private_key

    if public_certificate is not None:
        _details['publicCertificate'] = public_certificate

    if ca_certificate is not None:
        _details['caCertificate'] = ca_certificate

    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.create_certificate(
        load_balancer_id=load_balancer_id,
        create_certificate_details=_details,
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
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@hostname_group.command(name=cli_util.override('lb.create_hostname.command_name', 'create'), help=u"""Adds a hostname resource to the specified load balancer. For more information, see [Managing Request Routing].""")
@cli_util.option('--name', required=True, help=u"""A friendly name for the hostname resource. It must be unique and it cannot be changed. Avoid entering confidential information.

Example: `example_hostname_001`""")
@cli_util.option('--hostname', required=True, help=u"""A virtual hostname. For more information about virtual hostname string construction, see [Managing Request Routing].

Example: `app.example.com`""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer to add the hostname to.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def create_hostname(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, hostname, load_balancer_id):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['hostname'] = hostname

    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.create_hostname(
        load_balancer_id=load_balancer_id,
        create_hostname_details=_details,
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
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@listener_group.command(name=cli_util.override('lb.create_listener.command_name', 'create'), help=u"""Adds a listener to a load balancer.""")
@cli_util.option('--default-backend-set-name', required=True, help=u"""The name of the associated backend set.

Example: `example_backend_set`""")
@cli_util.option('--port', required=True, type=click.INT, help=u"""The communication port for the listener.

Example: `80`""")
@cli_util.option('--protocol', required=True, help=u"""The protocol on which the listener accepts connection requests. To get a list of valid protocols, use the [ListProtocols] operation.

Example: `HTTP`""")
@cli_util.option('--name', required=True, help=u"""A friendly name for the listener. It must be unique and it cannot be changed. Avoid entering confidential information.

Example: `example_listener`""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer on which to add a listener.""")
@cli_util.option('--hostname-names', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of hostname resource names.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--path-route-set-name', help=u"""The name of the set of path-based routing rules, [PathRouteSet], applied to this listener's traffic.

Example: `example_path_route_set`""")
@cli_util.option('--ssl-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--rule-set-names', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The names of the [rule sets] to apply to the listener.

Example: [\"example_rule_set\"]""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'hostname-names': {'module': 'load_balancer', 'class': 'list[string]'}, 'ssl-configuration': {'module': 'load_balancer', 'class': 'SSLConfigurationDetails'}, 'connection-configuration': {'module': 'load_balancer', 'class': 'ConnectionConfiguration'}, 'rule-set-names': {'module': 'load_balancer', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'hostname-names': {'module': 'load_balancer', 'class': 'list[string]'}, 'ssl-configuration': {'module': 'load_balancer', 'class': 'SSLConfigurationDetails'}, 'connection-configuration': {'module': 'load_balancer', 'class': 'ConnectionConfiguration'}, 'rule-set-names': {'module': 'load_balancer', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def create_listener(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, default_backend_set_name, port, protocol, name, load_balancer_id, hostname_names, path_route_set_name, ssl_configuration, connection_configuration, rule_set_names):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['defaultBackendSetName'] = default_backend_set_name
    _details['port'] = port
    _details['protocol'] = protocol
    _details['name'] = name

    if hostname_names is not None:
        _details['hostnameNames'] = cli_util.parse_json_parameter("hostname_names", hostname_names)

    if path_route_set_name is not None:
        _details['pathRouteSetName'] = path_route_set_name

    if ssl_configuration is not None:
        _details['sslConfiguration'] = cli_util.parse_json_parameter("ssl_configuration", ssl_configuration)

    if connection_configuration is not None:
        _details['connectionConfiguration'] = cli_util.parse_json_parameter("connection_configuration", connection_configuration)

    if rule_set_names is not None:
        _details['ruleSetNames'] = cli_util.parse_json_parameter("rule_set_names", rule_set_names)

    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.create_listener(
        load_balancer_id=load_balancer_id,
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
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@load_balancer_group.command(name=cli_util.override('lb.create_load_balancer.command_name', 'create'), help=u"""Creates a new load balancer in the specified compartment. For general information about load balancers, see [Overview of the Load Balancing Service].

For the purposes of access control, you must provide the OCID of the compartment where you want the load balancer to reside. Notice that the load balancer doesn't have to be in the same compartment as the VCN or backend set. If you're not sure which compartment to use, put the load balancer in the same compartment as the VCN. For information about access control and compartments, see [Overview of the IAM Service].

You must specify a display name for the load balancer. It does not have to be unique, and you can change it.

For information about Availability Domains, see [Regions and Availability Domains]. To get a list of Availability Domains, use the `ListAvailabilityDomains` operation in the Identity and Access Management Service API.

All Oracle Cloud Infrastructure resources, including load balancers, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. Fore more information, see [Resource Identifiers].

After you send your request, the new object's state will temporarily be PROVISIONING. Before using the object, first make sure its state has changed to RUNNING.

When you create a load balancer, the system assigns an IP address. To get the IP address, use the [GetLoadBalancer] operation.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which to create the load balancer.""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.

Example: `example_load_balancer`""")
@cli_util.option('--shape-name', required=True, help=u"""A template that determines the total pre-provisioned bandwidth (ingress plus egress). To get a list of available shapes, use the [ListShapes] operation.

Example: `100Mbps`""")
@cli_util.option('--subnet-ids', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of subnet [OCIDs].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-private', type=click.BOOL, help=u"""Whether the load balancer has a VCN-local (private) IP address.

If \"true\", the service assigns a private IP address to the load balancer.

If \"false\", the service assigns a public IP address to the load balancer.

A public load balancer is accessible from the internet, depending on your VCN's [security list rules]. For more information about public and private load balancers, see [How Load Balancing Works].

Example: `true`""")
@cli_util.option('--ip-mode', type=custom_types.CliCaseInsensitiveChoice(["IPV4", "IPV6"]), help=u"""Whether the load balancer has an IPv4 or IPv6 IP address.

If \"IPV4\", the service assigns an IPv4 address and the load balancer supports IPv4 traffic.

If \"IPV6\", the service assigns an IPv6 address and the load balancer supports IPv6 traffic.

Example: \"ipMode\":\"IPV6\"""")
@cli_util.option('--listeners', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON dictionary of type dict(str, ListenerDetails).  For documentation on ListenerDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/loadbalancer/20170115/datatypes/ListenerDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--hostnames', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON dictionary of type dict(str, HostnameDetails).  For documentation on HostnameDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/loadbalancer/20170115/datatypes/HostnameDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--backend-sets', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON dictionary of type dict(str, BackendSetDetails).  For documentation on BackendSetDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/loadbalancer/20170115/datatypes/BackendSetDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--network-security-group-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of NSG [OCIDs] associated with this load balancer.

During the load balancer's creation, the service adds the new load balancer to the specified NSGs.

The benefits of using NSGs with the load balancer include:

*  NSGs define network security rules to govern ingress and egress traffic for the load balancer.

*  The network security rules of other resources can reference the NSGs associated with the load balancer    to ensure access.

Example: `[\"ocid1.nsg.oc1.phx.unique_ID\"]`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--certificates', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON dictionary of type dict(str, CertificateDetails).  For documentation on CertificateDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/loadbalancer/20170115/datatypes/CertificateDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--path-route-sets', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON dictionary of type dict(str, PathRouteSetDetails).  For documentation on PathRouteSetDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/loadbalancer/20170115/datatypes/PathRouteSetDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--rule-sets', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON dictionary of type dict(str, RuleSetDetails).  For documentation on RuleSetDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/loadbalancer/20170115/datatypes/RuleSetDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'listeners': {'module': 'load_balancer', 'class': 'dict(str, ListenerDetails)'}, 'hostnames': {'module': 'load_balancer', 'class': 'dict(str, HostnameDetails)'}, 'backend-sets': {'module': 'load_balancer', 'class': 'dict(str, BackendSetDetails)'}, 'network-security-group-ids': {'module': 'load_balancer', 'class': 'list[string]'}, 'subnet-ids': {'module': 'load_balancer', 'class': 'list[string]'}, 'certificates': {'module': 'load_balancer', 'class': 'dict(str, CertificateDetails)'}, 'path-route-sets': {'module': 'load_balancer', 'class': 'dict(str, PathRouteSetDetails)'}, 'freeform-tags': {'module': 'load_balancer', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'load_balancer', 'class': 'dict(str, dict(str, object))'}, 'rule-sets': {'module': 'load_balancer', 'class': 'dict(str, RuleSetDetails)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'listeners': {'module': 'load_balancer', 'class': 'dict(str, ListenerDetails)'}, 'hostnames': {'module': 'load_balancer', 'class': 'dict(str, HostnameDetails)'}, 'backend-sets': {'module': 'load_balancer', 'class': 'dict(str, BackendSetDetails)'}, 'network-security-group-ids': {'module': 'load_balancer', 'class': 'list[string]'}, 'subnet-ids': {'module': 'load_balancer', 'class': 'list[string]'}, 'certificates': {'module': 'load_balancer', 'class': 'dict(str, CertificateDetails)'}, 'path-route-sets': {'module': 'load_balancer', 'class': 'dict(str, PathRouteSetDetails)'}, 'freeform-tags': {'module': 'load_balancer', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'load_balancer', 'class': 'dict(str, dict(str, object))'}, 'rule-sets': {'module': 'load_balancer', 'class': 'dict(str, RuleSetDetails)'}})
@cli_util.wrap_exceptions
def create_load_balancer(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, shape_name, subnet_ids, is_private, ip_mode, listeners, hostnames, backend_sets, network_security_group_ids, certificates, path_route_sets, freeform_tags, defined_tags, rule_sets):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['shapeName'] = shape_name
    _details['subnetIds'] = cli_util.parse_json_parameter("subnet_ids", subnet_ids)

    if is_private is not None:
        _details['isPrivate'] = is_private

    if ip_mode is not None:
        _details['ipMode'] = ip_mode

    if listeners is not None:
        _details['listeners'] = cli_util.parse_json_parameter("listeners", listeners)

    if hostnames is not None:
        _details['hostnames'] = cli_util.parse_json_parameter("hostnames", hostnames)

    if backend_sets is not None:
        _details['backendSets'] = cli_util.parse_json_parameter("backend_sets", backend_sets)

    if network_security_group_ids is not None:
        _details['networkSecurityGroupIds'] = cli_util.parse_json_parameter("network_security_group_ids", network_security_group_ids)

    if certificates is not None:
        _details['certificates'] = cli_util.parse_json_parameter("certificates", certificates)

    if path_route_sets is not None:
        _details['pathRouteSets'] = cli_util.parse_json_parameter("path_route_sets", path_route_sets)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if rule_sets is not None:
        _details['ruleSets'] = cli_util.parse_json_parameter("rule_sets", rule_sets)

    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.create_load_balancer(
        create_load_balancer_details=_details,
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
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
                if hasattr(client, 'get_load_balancer') and callable(getattr(client, 'get_load_balancer')) and hasattr(result.data, 'load_balancer_id'):
                    result = client.get_load_balancer(result.data.load_balancer_id)
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


@path_route_set_group.command(name=cli_util.override('lb.create_path_route_set.command_name', 'create'), help=u"""Adds a path route set to a load balancer. For more information, see [Managing Request Routing].""")
@cli_util.option('--name', required=True, help=u"""The name for this set of path route rules. It must be unique and it cannot be changed. Avoid entering confidential information.

Example: `example_path_route_set`""")
@cli_util.option('--path-routes', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The set of path route rules.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer to add the path route set to.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'path-routes': {'module': 'load_balancer', 'class': 'list[PathRoute]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'path-routes': {'module': 'load_balancer', 'class': 'list[PathRoute]'}})
@cli_util.wrap_exceptions
def create_path_route_set(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, path_routes, load_balancer_id):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['pathRoutes'] = cli_util.parse_json_parameter("path_routes", path_routes)

    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.create_path_route_set(
        load_balancer_id=load_balancer_id,
        create_path_route_set_details=_details,
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
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@rule_set_group.command(name=cli_util.override('lb.create_rule_set.command_name', 'create'), help=u"""Creates a new rule set associated with the specified load balancer. For more information, see [Managing Rule Sets].""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the specified load balancer.""")
@cli_util.option('--name', required=True, help=u"""The name for this set of rules. It must be unique and it cannot be changed. Avoid entering confidential information.

Example: `example_rule_set`""")
@cli_util.option('--items', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of rules that compose the rule set.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'load_balancer', 'class': 'list[Rule]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'load_balancer', 'class': 'list[Rule]'}})
@cli_util.wrap_exceptions
def create_rule_set(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, load_balancer_id, name, items):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.create_rule_set(
        load_balancer_id=load_balancer_id,
        create_rule_set_details=_details,
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
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@backend_group.command(name=cli_util.override('lb.delete_backend.command_name', 'delete'), help=u"""Removes a backend server from a given load balancer and backend set.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer associated with the backend set and server.""")
@cli_util.option('--backend-set-name', required=True, help=u"""The name of the backend set associated with the backend server.

Example: `example_backend_set`""")
@cli_util.option('--backend-name', required=True, help=u"""The IP address and port of the backend server to remove.

Example: `10.0.0.3:8080`""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_backend(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, load_balancer_id, backend_set_name, backend_name):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')

    if isinstance(backend_name, six.string_types) and len(backend_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.delete_backend(
        load_balancer_id=load_balancer_id,
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
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@backend_set_group.command(name=cli_util.override('lb.delete_backend_set.command_name', 'delete'), help=u"""Deletes the specified backend set. Note that deleting a backend set removes its backend servers from the load balancer.

Before you can delete a backend set, you must remove it from any active listeners.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer associated with the backend set.""")
@cli_util.option('--backend-set-name', required=True, help=u"""The name of the backend set to delete.

Example: `example_backend_set`""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_backend_set(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, load_balancer_id, backend_set_name):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.delete_backend_set(
        load_balancer_id=load_balancer_id,
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
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@certificate_group.command(name=cli_util.override('lb.delete_certificate.command_name', 'delete'), help=u"""Deletes an SSL certificate bundle from a load balancer.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer associated with the certificate bundle to be deleted.""")
@cli_util.option('--certificate-name', required=True, help=u"""The name of the certificate bundle to delete.

Example: `example_certificate_bundle`""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_certificate(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, load_balancer_id, certificate_name):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(certificate_name, six.string_types) and len(certificate_name.strip()) == 0:
        raise click.UsageError('Parameter --certificate-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.delete_certificate(
        load_balancer_id=load_balancer_id,
        certificate_name=certificate_name,
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
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@hostname_group.command(name=cli_util.override('lb.delete_hostname.command_name', 'delete'), help=u"""Deletes a hostname resource from the specified load balancer.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer associated with the hostname to delete.""")
@cli_util.option('--name', required=True, help=u"""The name of the hostname resource to delete.

Example: `example_hostname_001`""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_hostname(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, load_balancer_id, name):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(name, six.string_types) and len(name.strip()) == 0:
        raise click.UsageError('Parameter --name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.delete_hostname(
        load_balancer_id=load_balancer_id,
        name=name,
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
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@listener_group.command(name=cli_util.override('lb.delete_listener.command_name', 'delete'), help=u"""Deletes a listener from a load balancer.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer associated with the listener to delete.""")
@cli_util.option('--listener-name', required=True, help=u"""The name of the listener to delete.

Example: `example_listener`""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_listener(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, load_balancer_id, listener_name):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(listener_name, six.string_types) and len(listener_name.strip()) == 0:
        raise click.UsageError('Parameter --listener-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.delete_listener(
        load_balancer_id=load_balancer_id,
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
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@load_balancer_group.command(name=cli_util.override('lb.delete_load_balancer.command_name', 'delete'), help=u"""Stops a load balancer and removes it from service.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer to delete.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_load_balancer(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, load_balancer_id):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.delete_load_balancer(
        load_balancer_id=load_balancer_id,
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
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@path_route_set_group.command(name=cli_util.override('lb.delete_path_route_set.command_name', 'delete'), help=u"""Deletes a path route set from the specified load balancer.

To delete a path route rule from a path route set, use the [UpdatePathRouteSet] operation.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer associated with the path route set to delete.""")
@cli_util.option('--path-route-set-name', required=True, help=u"""The name of the path route set to delete.

Example: `example_path_route_set`""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_path_route_set(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, load_balancer_id, path_route_set_name):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(path_route_set_name, six.string_types) and len(path_route_set_name.strip()) == 0:
        raise click.UsageError('Parameter --path-route-set-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.delete_path_route_set(
        load_balancer_id=load_balancer_id,
        path_route_set_name=path_route_set_name,
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
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@rule_set_group.command(name=cli_util.override('lb.delete_rule_set.command_name', 'delete'), help=u"""Deletes a rule set from the specified load balancer.

To delete a rule from a rule set, use the [UpdateRuleSet] operation.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the specified load balancer.""")
@cli_util.option('--rule-set-name', required=True, help=u"""The name of the rule set to delete.

Example: `example_rule_set`""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_rule_set(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, load_balancer_id, rule_set_name):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(rule_set_name, six.string_types) and len(rule_set_name.strip()) == 0:
        raise click.UsageError('Parameter --rule-set-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.delete_rule_set(
        load_balancer_id=load_balancer_id,
        rule_set_name=rule_set_name,
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
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@backend_group.command(name=cli_util.override('lb.get_backend.command_name', 'get'), help=u"""Gets the specified backend server's configuration information.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer associated with the backend set and server.""")
@cli_util.option('--backend-set-name', required=True, help=u"""The name of the backend set that includes the backend server.

Example: `example_backend_set`""")
@cli_util.option('--backend-name', required=True, help=u"""The IP address and port of the backend server to retrieve.

Example: `10.0.0.3:8080`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'Backend'})
@cli_util.wrap_exceptions
def get_backend(ctx, from_json, load_balancer_id, backend_set_name, backend_name):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')

    if isinstance(backend_name, six.string_types) and len(backend_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.get_backend(
        load_balancer_id=load_balancer_id,
        backend_set_name=backend_set_name,
        backend_name=backend_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@backend_health_group.command(name=cli_util.override('lb.get_backend_health.command_name', 'get'), help=u"""Gets the current health status of the specified backend server.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer associated with the backend server health status to be retrieved.""")
@cli_util.option('--backend-set-name', required=True, help=u"""The name of the backend set associated with the backend server to retrieve the health status for.

Example: `example_backend_set`""")
@cli_util.option('--backend-name', required=True, help=u"""The IP address and port of the backend server to retrieve the health status for.

Example: `10.0.0.3:8080`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'BackendHealth'})
@cli_util.wrap_exceptions
def get_backend_health(ctx, from_json, load_balancer_id, backend_set_name, backend_name):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')

    if isinstance(backend_name, six.string_types) and len(backend_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.get_backend_health(
        load_balancer_id=load_balancer_id,
        backend_set_name=backend_set_name,
        backend_name=backend_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@backend_set_group.command(name=cli_util.override('lb.get_backend_set.command_name', 'get'), help=u"""Gets the specified backend set's configuration information.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the specified load balancer.""")
@cli_util.option('--backend-set-name', required=True, help=u"""The name of the backend set to retrieve.

Example: `example_backend_set`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'BackendSet'})
@cli_util.wrap_exceptions
def get_backend_set(ctx, from_json, load_balancer_id, backend_set_name):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.get_backend_set(
        load_balancer_id=load_balancer_id,
        backend_set_name=backend_set_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@backend_set_health_group.command(name=cli_util.override('lb.get_backend_set_health.command_name', 'get'), help=u"""Gets the health status for the specified backend set.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer associated with the backend set health status to be retrieved.""")
@cli_util.option('--backend-set-name', required=True, help=u"""The name of the backend set to retrieve the health status for.

Example: `example_backend_set`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'BackendSetHealth'})
@cli_util.wrap_exceptions
def get_backend_set_health(ctx, from_json, load_balancer_id, backend_set_name):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.get_backend_set_health(
        load_balancer_id=load_balancer_id,
        backend_set_name=backend_set_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@health_checker_group.command(name=cli_util.override('lb.get_health_checker.command_name', 'get'), help=u"""Gets the health check policy information for a given load balancer and backend set.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer associated with the health check policy to be retrieved.""")
@cli_util.option('--backend-set-name', required=True, help=u"""The name of the backend set associated with the health check policy to be retrieved.

Example: `example_backend_set`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'HealthChecker'})
@cli_util.wrap_exceptions
def get_health_checker(ctx, from_json, load_balancer_id, backend_set_name):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.get_health_checker(
        load_balancer_id=load_balancer_id,
        backend_set_name=backend_set_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@hostname_group.command(name=cli_util.override('lb.get_hostname.command_name', 'get'), help=u"""Gets the specified hostname resource's configuration information.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the specified load balancer.""")
@cli_util.option('--name', required=True, help=u"""The name of the hostname resource to retrieve.

Example: `example_hostname_001`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'Hostname'})
@cli_util.wrap_exceptions
def get_hostname(ctx, from_json, load_balancer_id, name):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(name, six.string_types) and len(name.strip()) == 0:
        raise click.UsageError('Parameter --name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.get_hostname(
        load_balancer_id=load_balancer_id,
        name=name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@load_balancer_group.command(name=cli_util.override('lb.get_load_balancer.command_name', 'get'), help=u"""Gets the specified load balancer's configuration information.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer to retrieve.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'LoadBalancer'})
@cli_util.wrap_exceptions
def get_load_balancer(ctx, from_json, load_balancer_id):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.get_load_balancer(
        load_balancer_id=load_balancer_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@load_balancer_health_group.command(name=cli_util.override('lb.get_load_balancer_health.command_name', 'get'), help=u"""Gets the health status for the specified load balancer.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer to return health status for.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'LoadBalancerHealth'})
@cli_util.wrap_exceptions
def get_load_balancer_health(ctx, from_json, load_balancer_id):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.get_load_balancer_health(
        load_balancer_id=load_balancer_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@path_route_set_group.command(name=cli_util.override('lb.get_path_route_set.command_name', 'get'), help=u"""Gets the specified path route set's configuration information.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the specified load balancer.""")
@cli_util.option('--path-route-set-name', required=True, help=u"""The name of the path route set to retrieve.

Example: `example_path_route_set`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'PathRouteSet'})
@cli_util.wrap_exceptions
def get_path_route_set(ctx, from_json, load_balancer_id, path_route_set_name):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(path_route_set_name, six.string_types) and len(path_route_set_name.strip()) == 0:
        raise click.UsageError('Parameter --path-route-set-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.get_path_route_set(
        load_balancer_id=load_balancer_id,
        path_route_set_name=path_route_set_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@rule_set_group.command(name=cli_util.override('lb.get_rule_set.command_name', 'get'), help=u"""Gets the specified set of rules.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the specified load balancer.""")
@cli_util.option('--rule-set-name', required=True, help=u"""The name of the rule set to retrieve.

Example: `example_rule_set`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'RuleSet'})
@cli_util.wrap_exceptions
def get_rule_set(ctx, from_json, load_balancer_id, rule_set_name):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(rule_set_name, six.string_types) and len(rule_set_name.strip()) == 0:
        raise click.UsageError('Parameter --rule-set-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.get_rule_set(
        load_balancer_id=load_balancer_id,
        rule_set_name=rule_set_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('lb.get_work_request.command_name', 'get'), help=u"""Gets the details of a work request.""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the work request to retrieve.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@backend_set_group.command(name=cli_util.override('lb.list_backend_sets.command_name', 'list'), help=u"""Lists all backend sets associated with a given load balancer.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer associated with the backend sets to retrieve.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'list[BackendSet]'})
@cli_util.wrap_exceptions
def list_backend_sets(ctx, from_json, all_pages, load_balancer_id):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.list_backend_sets(
        load_balancer_id=load_balancer_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@backend_group.command(name=cli_util.override('lb.list_backends.command_name', 'list'), help=u"""Lists the backend servers for a given load balancer and backend set.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer associated with the backend set and servers.""")
@cli_util.option('--backend-set-name', required=True, help=u"""The name of the backend set associated with the backend servers.

Example: `example_backend_set`""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'list[Backend]'})
@cli_util.wrap_exceptions
def list_backends(ctx, from_json, all_pages, load_balancer_id, backend_set_name):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.list_backends(
        load_balancer_id=load_balancer_id,
        backend_set_name=backend_set_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@certificate_group.command(name=cli_util.override('lb.list_certificates.command_name', 'list'), help=u"""Lists all SSL certificates bundles associated with a given load balancer.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer associated with the certificate bundles to be listed.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'list[Certificate]'})
@cli_util.wrap_exceptions
def list_certificates(ctx, from_json, all_pages, load_balancer_id):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.list_certificates(
        load_balancer_id=load_balancer_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@hostname_group.command(name=cli_util.override('lb.list_hostnames.command_name', 'list'), help=u"""Lists all hostname resources associated with the specified load balancer.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer associated with the hostnames to retrieve.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'list[Hostname]'})
@cli_util.wrap_exceptions
def list_hostnames(ctx, from_json, all_pages, load_balancer_id):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.list_hostnames(
        load_balancer_id=load_balancer_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@listener_rule_group.command(name=cli_util.override('lb.list_listener_rules.command_name', 'list'), help=u"""Lists all of the rules from all of the rule sets associated with the specified listener. The response organizes the rules in the following order:

*  Access control rules *  Allow method rules *  Request header rules *  Response header rules""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer associated with the listener.""")
@cli_util.option('--listener-name', required=True, help=u"""The name of the listener the rules are associated with.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'list[ListenerRuleSummary]'})
@cli_util.wrap_exceptions
def list_listener_rules(ctx, from_json, all_pages, load_balancer_id, listener_name):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(listener_name, six.string_types) and len(listener_name.strip()) == 0:
        raise click.UsageError('Parameter --listener-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.list_listener_rules(
        load_balancer_id=load_balancer_id,
        listener_name=listener_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@load_balancer_health_group.command(name=cli_util.override('lb.list_load_balancer_healths.command_name', 'list'), help=u"""Lists the summary health statuses for all load balancers in the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing the load balancers to return health status information for.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `3`""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'list[LoadBalancerHealthSummary]'})
@cli_util.wrap_exceptions
def list_load_balancer_healths(ctx, from_json, all_pages, page_size, compartment_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_load_balancer_healths,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_load_balancer_healths,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_load_balancer_healths(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@load_balancer_group.command(name=cli_util.override('lb.list_load_balancers.command_name', 'list'), help=u"""Lists all load balancers in the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing the load balancers to list.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `3`""")
@cli_util.option('--detail', help=u"""The level of detail to return for each result. Can be `full` or `simple`.

Example: `full`""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by.  You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.

Example: `example_load_balancer`""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "FAILED", "ACTIVE", "DELETING", "DELETED"]), help=u"""A filter to return only resources that match the given lifecycle state.

Example: `SUCCEEDED`""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'list[LoadBalancer]'})
@cli_util.wrap_exceptions
def list_load_balancers(ctx, from_json, all_pages, page_size, compartment_id, limit, page, detail, sort_by, sort_order, display_name, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if detail is not None:
        kwargs['detail'] = detail
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_load_balancers,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_load_balancers,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_load_balancers(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@path_route_set_group.command(name=cli_util.override('lb.list_path_route_sets.command_name', 'list'), help=u"""Lists all path route sets associated with the specified load balancer.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer associated with the path route sets to retrieve.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'list[PathRouteSet]'})
@cli_util.wrap_exceptions
def list_path_route_sets(ctx, from_json, all_pages, load_balancer_id):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.list_path_route_sets(
        load_balancer_id=load_balancer_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@load_balancer_policy_group.command(name=cli_util.override('lb.list_policies.command_name', 'list-policies'), help=u"""Lists the available load balancer policies.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing the load balancer policies to list.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `3`""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'list[LoadBalancerPolicy]'})
@cli_util.wrap_exceptions
def list_policies(ctx, from_json, all_pages, page_size, compartment_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_policies,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_policies,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_policies(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@load_balancer_protocol_group.command(name=cli_util.override('lb.list_protocols.command_name', 'list-protocols'), help=u"""Lists all supported traffic protocols.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing the load balancer protocols to list.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `3`""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'list[LoadBalancerProtocol]'})
@cli_util.wrap_exceptions
def list_protocols(ctx, from_json, all_pages, page_size, compartment_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_protocols,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_protocols,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_protocols(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@rule_set_group.command(name=cli_util.override('lb.list_rule_sets.command_name', 'list'), help=u"""Lists all rule sets associated with the specified load balancer.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the specified load balancer.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'list[RuleSet]'})
@cli_util.wrap_exceptions
def list_rule_sets(ctx, from_json, all_pages, load_balancer_id):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.list_rule_sets(
        load_balancer_id=load_balancer_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@load_balancer_shape_group.command(name=cli_util.override('lb.list_shapes.command_name', 'list-shapes'), help=u"""Lists the valid load balancer shapes.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing the load balancer shapes to list.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `3`""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'list[LoadBalancerShape]'})
@cli_util.wrap_exceptions
def list_shapes(ctx, from_json, all_pages, page_size, compartment_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_shapes,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_shapes,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_shapes(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('lb.list_work_requests.command_name', 'list'), help=u"""Lists the work requests for a given load balancer.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer associated with the work requests to retrieve.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `3`""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'list[WorkRequest]'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, load_balancer_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            load_balancer_id=load_balancer_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            load_balancer_id=load_balancer_id,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            load_balancer_id=load_balancer_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@backend_group.command(name=cli_util.override('lb.update_backend.command_name', 'update'), help=u"""Updates the configuration of a backend server within the specified backend set.""")
@cli_util.option('--weight', required=True, type=click.INT, help=u"""The load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted '3' receives 3 times the number of new connections as a server weighted '1'. For more information on load balancing policies, see [How Load Balancing Policies Work].

Example: `3`""")
@cli_util.option('--backup', required=True, type=click.BOOL, help=u"""Whether the load balancer should treat this server as a backup unit. If `true`, the load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as \"backup\" fail the health check policy.

**Note:** You cannot add a backend server marked as `backup` to a backend set that uses the IP Hash policy.

Example: `false`""")
@cli_util.option('--drain', required=True, type=click.BOOL, help=u"""Whether the load balancer should drain this server. Servers marked \"drain\" receive no new incoming traffic.

Example: `false`""")
@cli_util.option('--offline', required=True, type=click.BOOL, help=u"""Whether the load balancer should treat this server as offline. Offline servers receive no incoming traffic.

Example: `false`""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer associated with the backend set and server.""")
@cli_util.option('--backend-set-name', required=True, help=u"""The name of the backend set associated with the backend server.

Example: `example_backend_set`""")
@cli_util.option('--backend-name', required=True, help=u"""The IP address and port of the backend server to update.

Example: `10.0.0.3:8080`""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_backend(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, weight, backup, drain, offline, load_balancer_id, backend_set_name, backend_name):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')

    if isinstance(backend_name, six.string_types) and len(backend_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['weight'] = weight
    _details['backup'] = backup
    _details['drain'] = drain
    _details['offline'] = offline

    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.update_backend(
        load_balancer_id=load_balancer_id,
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
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@backend_set_group.command(name=cli_util.override('lb.update_backend_set.command_name', 'update'), help=u"""Updates a backend set.""")
@cli_util.option('--policy', required=True, help=u"""The load balancer policy for the backend set. To get a list of available policies, use the [ListPolicies] operation.

Example: `LEAST_CONNECTIONS`""")
@cli_util.option('--backends', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--health-checker', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer associated with the backend set.""")
@cli_util.option('--backend-set-name', required=True, help=u"""The name of the backend set to update.

Example: `example_backend_set`""")
@cli_util.option('--ssl-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--session-persistence-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--lb-cookie-session-persistence-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'backends': {'module': 'load_balancer', 'class': 'list[BackendDetails]'}, 'health-checker': {'module': 'load_balancer', 'class': 'HealthCheckerDetails'}, 'ssl-configuration': {'module': 'load_balancer', 'class': 'SSLConfigurationDetails'}, 'session-persistence-configuration': {'module': 'load_balancer', 'class': 'SessionPersistenceConfigurationDetails'}, 'lb-cookie-session-persistence-configuration': {'module': 'load_balancer', 'class': 'LBCookieSessionPersistenceConfigurationDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backends': {'module': 'load_balancer', 'class': 'list[BackendDetails]'}, 'health-checker': {'module': 'load_balancer', 'class': 'HealthCheckerDetails'}, 'ssl-configuration': {'module': 'load_balancer', 'class': 'SSLConfigurationDetails'}, 'session-persistence-configuration': {'module': 'load_balancer', 'class': 'SessionPersistenceConfigurationDetails'}, 'lb-cookie-session-persistence-configuration': {'module': 'load_balancer', 'class': 'LBCookieSessionPersistenceConfigurationDetails'}})
@cli_util.wrap_exceptions
def update_backend_set(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, policy, backends, health_checker, load_balancer_id, backend_set_name, ssl_configuration, session_persistence_configuration, lb_cookie_session_persistence_configuration):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')
    if not force:
        if backends or health_checker or ssl_configuration or session_persistence_configuration or lb_cookie_session_persistence_configuration:
            if not click.confirm("WARNING: Updates to backends and health-checker and ssl-configuration and session-persistence-configuration and lb-cookie-session-persistence-configuration will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['policy'] = policy
    _details['backends'] = cli_util.parse_json_parameter("backends", backends)
    _details['healthChecker'] = cli_util.parse_json_parameter("health_checker", health_checker)

    if ssl_configuration is not None:
        _details['sslConfiguration'] = cli_util.parse_json_parameter("ssl_configuration", ssl_configuration)

    if session_persistence_configuration is not None:
        _details['sessionPersistenceConfiguration'] = cli_util.parse_json_parameter("session_persistence_configuration", session_persistence_configuration)

    if lb_cookie_session_persistence_configuration is not None:
        _details['lbCookieSessionPersistenceConfiguration'] = cli_util.parse_json_parameter("lb_cookie_session_persistence_configuration", lb_cookie_session_persistence_configuration)

    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.update_backend_set(
        load_balancer_id=load_balancer_id,
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
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@health_checker_group.command(name=cli_util.override('lb.update_health_checker.command_name', 'update'), help=u"""Updates the health check policy for a given load balancer and backend set.""")
@cli_util.option('--protocol', required=True, help=u"""The protocol the health check must use; either HTTP or TCP.

Example: `HTTP`""")
@cli_util.option('--port', required=True, type=click.INT, help=u"""The backend server port against which to run the health check.

Example: `8080`""")
@cli_util.option('--return-code', required=True, type=click.INT, help=u"""The status code a healthy backend server should return.

Example: `200`""")
@cli_util.option('--retries', required=True, type=click.INT, help=u"""The number of retries to attempt before a backend server is considered \"unhealthy\". This number also applies when recovering a server to the \"healthy\" state.

Example: `3`""")
@cli_util.option('--timeout-in-millis', required=True, type=click.INT, help=u"""The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply returns within this timeout period.

Example: `3000`""")
@cli_util.option('--interval-in-millis', required=True, type=click.INT, help=u"""The interval between health checks, in milliseconds.

Example: `10000`""")
@cli_util.option('--response-body-regex', required=True, help=u"""A regular expression for parsing the response body from the backend server.

Example: `^((?!false).|\\s)*$`""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer associated with the health check policy to be updated.""")
@cli_util.option('--backend-set-name', required=True, help=u"""The name of the backend set associated with the health check policy to be retrieved.

Example: `example_backend_set`""")
@cli_util.option('--url-path', help=u"""The path against which to run the health check.

Example: `/healthcheck`""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_health_checker(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, protocol, port, return_code, retries, timeout_in_millis, interval_in_millis, response_body_regex, load_balancer_id, backend_set_name, url_path):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['protocol'] = protocol
    _details['port'] = port
    _details['returnCode'] = return_code
    _details['retries'] = retries
    _details['timeoutInMillis'] = timeout_in_millis
    _details['intervalInMillis'] = interval_in_millis
    _details['responseBodyRegex'] = response_body_regex

    if url_path is not None:
        _details['urlPath'] = url_path

    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.update_health_checker(
        load_balancer_id=load_balancer_id,
        backend_set_name=backend_set_name,
        health_checker=_details,
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
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@hostname_group.command(name=cli_util.override('lb.update_hostname.command_name', 'update'), help=u"""Overwrites an existing hostname resource on the specified load balancer. Use this operation to change a virtual hostname.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer associated with the virtual hostname to update.""")
@cli_util.option('--name', required=True, help=u"""The name of the hostname resource to update.

Example: `example_hostname_001`""")
@cli_util.option('--hostname', help=u"""The virtual hostname to update. For more information about virtual hostname string construction, see [Managing Request Routing].

Example: `app.example.com`""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_hostname(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, load_balancer_id, name, hostname):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(name, six.string_types) and len(name.strip()) == 0:
        raise click.UsageError('Parameter --name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if hostname is not None:
        _details['hostname'] = hostname

    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.update_hostname(
        load_balancer_id=load_balancer_id,
        name=name,
        update_hostname_details=_details,
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
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@listener_group.command(name=cli_util.override('lb.update_listener.command_name', 'update'), help=u"""Updates a listener for a given load balancer.""")
@cli_util.option('--default-backend-set-name', required=True, help=u"""The name of the associated backend set.

Example: `example_backend_set`""")
@cli_util.option('--port', required=True, type=click.INT, help=u"""The communication port for the listener.

Example: `80`""")
@cli_util.option('--protocol', required=True, help=u"""The protocol on which the listener accepts connection requests. To get a list of valid protocols, use the [ListProtocols] operation.

Example: `HTTP`""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer associated with the listener to update.""")
@cli_util.option('--listener-name', required=True, help=u"""The name of the listener to update.

Example: `example_listener`""")
@cli_util.option('--hostname-names', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of hostname resource names.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--path-route-set-name', help=u"""The name of the set of path-based routing rules, [PathRouteSet], applied to this listener's traffic.

Example: `example_path_route_set`""")
@cli_util.option('--ssl-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--rule-set-names', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The names of the [rule sets] to apply to the listener.

Example: [\"example_rule_set\"]""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'hostname-names': {'module': 'load_balancer', 'class': 'list[string]'}, 'ssl-configuration': {'module': 'load_balancer', 'class': 'SSLConfigurationDetails'}, 'connection-configuration': {'module': 'load_balancer', 'class': 'ConnectionConfiguration'}, 'rule-set-names': {'module': 'load_balancer', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'hostname-names': {'module': 'load_balancer', 'class': 'list[string]'}, 'ssl-configuration': {'module': 'load_balancer', 'class': 'SSLConfigurationDetails'}, 'connection-configuration': {'module': 'load_balancer', 'class': 'ConnectionConfiguration'}, 'rule-set-names': {'module': 'load_balancer', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_listener(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, default_backend_set_name, port, protocol, load_balancer_id, listener_name, hostname_names, path_route_set_name, ssl_configuration, connection_configuration, rule_set_names):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(listener_name, six.string_types) and len(listener_name.strip()) == 0:
        raise click.UsageError('Parameter --listener-name cannot be whitespace or empty string')
    if not force:
        if hostname_names or ssl_configuration or connection_configuration or rule_set_names:
            if not click.confirm("WARNING: Updates to hostname-names and ssl-configuration and connection-configuration and rule-set-names will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['defaultBackendSetName'] = default_backend_set_name
    _details['port'] = port
    _details['protocol'] = protocol

    if hostname_names is not None:
        _details['hostnameNames'] = cli_util.parse_json_parameter("hostname_names", hostname_names)

    if path_route_set_name is not None:
        _details['pathRouteSetName'] = path_route_set_name

    if ssl_configuration is not None:
        _details['sslConfiguration'] = cli_util.parse_json_parameter("ssl_configuration", ssl_configuration)

    if connection_configuration is not None:
        _details['connectionConfiguration'] = cli_util.parse_json_parameter("connection_configuration", connection_configuration)

    if rule_set_names is not None:
        _details['ruleSetNames'] = cli_util.parse_json_parameter("rule_set_names", rule_set_names)

    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.update_listener(
        load_balancer_id=load_balancer_id,
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
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@load_balancer_group.command(name=cli_util.override('lb.update_load_balancer.command_name', 'update'), help=u"""Updates a load balancer's configuration.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer to update.""")
@cli_util.option('--display-name', help=u"""The user-friendly display name for the load balancer. It does not have to be unique, and it is changeable. Avoid entering confidential information.

Example: `example_load_balancer`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'load_balancer', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'load_balancer', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'load_balancer', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'load_balancer', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_load_balancer(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, load_balancer_id, display_name, freeform_tags, defined_tags):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.update_load_balancer(
        load_balancer_id=load_balancer_id,
        update_load_balancer_details=_details,
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
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
                if hasattr(client, 'get_load_balancer') and callable(getattr(client, 'get_load_balancer')) and hasattr(result.data, 'load_balancer_id'):
                    result = client.get_load_balancer(result.data.load_balancer_id)
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


@network_security_groups_group.command(name=cli_util.override('lb.update_network_security_groups.command_name', 'update'), help=u"""Updates the network security groups associated with the specified load balancer.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer to update the NSGs for.""")
@cli_util.option('--network-security-group-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of NSG [OCIDs] associated with the load balancer.

During the load balancer's creation, the service adds the new load balancer to the specified NSGs.

The benefits of associating the load balancer with NSGs include:

*  NSGs define network security rules to govern ingress and egress traffic for the load balancer.

*  The network security rules of other resources can reference the NSGs associated with the load balancer    to ensure access.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'network-security-group-ids': {'module': 'load_balancer', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'network-security-group-ids': {'module': 'load_balancer', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_network_security_groups(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, load_balancer_id, network_security_group_ids):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')
    if not force:
        if network_security_group_ids:
            if not click.confirm("WARNING: Updates to network-security-group-ids will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if network_security_group_ids is not None:
        _details['networkSecurityGroupIds'] = cli_util.parse_json_parameter("network_security_group_ids", network_security_group_ids)

    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.update_network_security_groups(
        load_balancer_id=load_balancer_id,
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
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@path_route_set_group.command(name=cli_util.override('lb.update_path_route_set.command_name', 'update'), help=u"""Overwrites an existing path route set on the specified load balancer. Use this operation to add, delete, or alter path route rules in a path route set.

To add a new path route rule to a path route set, the `pathRoutes` in the [UpdatePathRouteSetDetails] object must include both the new path route rule to add and the existing path route rules to retain.""")
@cli_util.option('--path-routes', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The set of path route rules.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the load balancer associated with the path route set to update.""")
@cli_util.option('--path-route-set-name', required=True, help=u"""The name of the path route set to update.

Example: `example_path_route_set`""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'path-routes': {'module': 'load_balancer', 'class': 'list[PathRoute]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'path-routes': {'module': 'load_balancer', 'class': 'list[PathRoute]'}})
@cli_util.wrap_exceptions
def update_path_route_set(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, path_routes, load_balancer_id, path_route_set_name):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(path_route_set_name, six.string_types) and len(path_route_set_name.strip()) == 0:
        raise click.UsageError('Parameter --path-route-set-name cannot be whitespace or empty string')
    if not force:
        if path_routes:
            if not click.confirm("WARNING: Updates to path-routes will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['pathRoutes'] = cli_util.parse_json_parameter("path_routes", path_routes)

    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.update_path_route_set(
        load_balancer_id=load_balancer_id,
        path_route_set_name=path_route_set_name,
        update_path_route_set_details=_details,
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
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@rule_set_group.command(name=cli_util.override('lb.update_rule_set.command_name', 'update'), help=u"""Overwrites an existing set of rules on the specified load balancer. Use this operation to add or alter the rules in a rule set.

To add a new rule to a set, the body must include both the new rule to add and the existing rules to retain.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The [OCID] of the specified load balancer.""")
@cli_util.option('--rule-set-name', required=True, help=u"""The name of the rule set to update.

Example: `example_rule_set`""")
@cli_util.option('--items', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of rules that compose the rule set.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'load_balancer', 'class': 'list[Rule]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'load_balancer', 'class': 'list[Rule]'}})
@cli_util.wrap_exceptions
def update_rule_set(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, load_balancer_id, rule_set_name, items):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(rule_set_name, six.string_types) and len(rule_set_name.strip()) == 0:
        raise click.UsageError('Parameter --rule-set-name cannot be whitespace or empty string')
    if not force:
        if items:
            if not click.confirm("WARNING: Updates to items will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('load_balancer', 'load_balancer', ctx)
    result = client.update_rule_set(
        load_balancer_id=load_balancer_id,
        rule_set_name=rule_set_name,
        update_rule_set_details=_details,
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
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
