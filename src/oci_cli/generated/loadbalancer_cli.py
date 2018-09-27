# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from ..cli_root import cli
from .. import cli_constants  # noqa: F401
from .. import cli_util
from .. import json_skeleton_utils
from .. import custom_types  # noqa: F401
from ..aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('lb_root_group.command_name', 'lb'), cls=CommandGroupWithAlias, help=cli_util.override('lb_root_group.help', """API for the Load Balancing Service"""), short_help=cli_util.override('lb_root_group.short_help', """Load Balancing Service API"""))
@cli_util.help_option_group
def lb_root_group():
    pass


@click.command(cli_util.override('load_balancer_group.command_name', 'load-balancer'), cls=CommandGroupWithAlias, help="""The properties that define a load balancer. For more information, see [Managing a Load Balancer].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

For information about endpoints and signing API requests, see [About the API]. For information about available SDKs and tools, see [SDKS and Other Tools].""")
@cli_util.help_option_group
def load_balancer_group():
    pass


@click.command(cli_util.override('load_balancer_shape_group.command_name', 'load-balancer-shape'), cls=CommandGroupWithAlias, help="""A shape is a template that determines the total pre-provisioned bandwidth (ingress plus egress) for the load balancer.

Note that the pre-provisioned maximum capacity applies to aggregated connections, not to a single client attempting to use the full bandwidth.""")
@cli_util.help_option_group
def load_balancer_shape_group():
    pass


@click.command(cli_util.override('certificate_group.command_name', 'certificate'), cls=CommandGroupWithAlias, help="""The configuration details of a certificate bundle. For more information on SSL certficate configuration, see [Managing SSL Certificates].""")
@cli_util.help_option_group
def certificate_group():
    pass


@click.command(cli_util.override('listener_group.command_name', 'listener'), cls=CommandGroupWithAlias, help="""The listener's configuration. For more information on backend set configuration, see [Managing Load Balancer Listeners].""")
@cli_util.help_option_group
def listener_group():
    pass


@click.command(cli_util.override('work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""Many of the API requests you use to create and configure load balancing do not take effect immediately. In these cases, the request spawns an asynchronous work flow to fulfill the request. WorkRequest objects provide visibility for in-progress work flows. For more information about work requests, see [Viewing the State of a Work Request].""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('backend_set_health_group.command_name', 'backend-set-health'), cls=CommandGroupWithAlias, help="""The health status details for a backend set.

This object does not explicitly enumerate backend servers with a status of `OK`. However, they are included in the `totalBackendCount` sum.""")
@cli_util.help_option_group
def backend_set_health_group():
    pass


@click.command(cli_util.override('health_checker_group.command_name', 'health-checker'), cls=CommandGroupWithAlias, help="""The health check policy configuration. For more information, see [Editing Health Check Policies].""")
@cli_util.help_option_group
def health_checker_group():
    pass


@click.command(cli_util.override('path_route_set_group.command_name', 'path-route-set'), cls=CommandGroupWithAlias, help="""A named set of path route rules. For more information, see [Managing Request Routing].""")
@cli_util.help_option_group
def path_route_set_group():
    pass


@click.command(cli_util.override('load_balancer_protocol_group.command_name', 'load-balancer-protocol'), cls=CommandGroupWithAlias, help="""A protocol that defines the type of traffic accepted by a listener.""")
@cli_util.help_option_group
def load_balancer_protocol_group():
    pass


@click.command(cli_util.override('load_balancer_health_group.command_name', 'load-balancer-health'), cls=CommandGroupWithAlias, help="""The health status details for the specified load balancer.

This object does not explicitly enumerate backend sets with a status of `OK`. However, they are included in the `totalBackendSetCount` sum.""")
@cli_util.help_option_group
def load_balancer_health_group():
    pass


@click.command(cli_util.override('hostname_group.command_name', 'hostname'), cls=CommandGroupWithAlias, help="""A hostname resource associated with a load balancer for use by one or more listeners.""")
@cli_util.help_option_group
def hostname_group():
    pass


@click.command(cli_util.override('load_balancer_policy_group.command_name', 'load-balancer-policy'), cls=CommandGroupWithAlias, help="""A policy that determines how traffic is distributed among backend servers. For more information on load balancing policies, see [How Load Balancing Policies Work].""")
@cli_util.help_option_group
def load_balancer_policy_group():
    pass


@click.command(cli_util.override('backend_health_group.command_name', 'backend-health'), cls=CommandGroupWithAlias, help="""The health status of the specified backend server as reported by the primary and standby load balancers.""")
@cli_util.help_option_group
def backend_health_group():
    pass


@click.command(cli_util.override('backend_set_group.command_name', 'backend-set'), cls=CommandGroupWithAlias, help="""The configuration of a load balancer backend set. For more information on backend set configuration, see [Managing Backend Sets].""")
@cli_util.help_option_group
def backend_set_group():
    pass


@click.command(cli_util.override('backend_group.command_name', 'backend'), cls=CommandGroupWithAlias, help="""The configuration of a backend server that is a member of a load balancer backend set. For more information, see [Managing Backend Servers].""")
@cli_util.help_option_group
def backend_group():
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
lb_root_group.add_command(load_balancer_health_group)
lb_root_group.add_command(hostname_group)
lb_root_group.add_command(load_balancer_policy_group)
lb_root_group.add_command(backend_health_group)
lb_root_group.add_command(backend_set_group)
lb_root_group.add_command(backend_group)


@backend_group.command(name=cli_util.override('create_backend.command_name', 'create'), help="""Adds a backend server to a backend set.""")
@cli_util.option('--ip-address', required=True, help="""The IP address of the backend server.

Example: `10.0.0.3`""")
@cli_util.option('--port', required=True, type=click.INT, help="""The communication port for the backend server.

Example: `8080`""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer associated with the backend set and servers.""")
@cli_util.option('--backend-set-name', required=True, help="""The name of the backend set to add the backend server to.

Example: `example_backend_set`""")
@cli_util.option('--backup', type=click.BOOL, help="""Whether the load balancer should treat this server as a backup unit. If `true`, the load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as \"backup\" fail the health check policy.

Example: `false`""")
@cli_util.option('--drain', type=click.BOOL, help="""Whether the load balancer should drain this server. Servers marked \"drain\" receive no new incoming traffic.

Example: `false`""")
@cli_util.option('--offline', type=click.BOOL, help="""Whether the load balancer should treat this server as offline. Offline servers receive no incoming traffic.

Example: `false`""")
@cli_util.option('--weight', type=click.INT, help="""The load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted '3' receives 3 times the number of new connections as a server weighted '1'. For more information on load balancing policies, see [How Load Balancing Policies Work].

Example: `3`""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def create_backend(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, ip_address, port, load_balancer_id, backend_set_name, backup, drain, offline, weight):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['ipAddress'] = ip_address
    details['port'] = port

    if backup is not None:
        details['backup'] = backup

    if drain is not None:
        details['drain'] = drain

    if offline is not None:
        details['offline'] = offline

    if weight is not None:
        details['weight'] = weight

    client = cli_util.build_client('load_balancer', ctx)
    result = client.create_backend(
        load_balancer_id=load_balancer_id,
        backend_set_name=backend_set_name,
        create_backend_details=details,
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@backend_set_group.command(name=cli_util.override('create_backend_set.command_name', 'create'), help="""Adds a backend set to a load balancer.""")
@cli_util.option('--health-checker', required=True, type=custom_types.CLI_COMPLEX_TYPE, help="""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--name', required=True, help="""A friendly name for the backend set. It must be unique and it cannot be changed.

Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot contain spaces. Avoid entering confidential information.

Example: `example_backend_set`""")
@cli_util.option('--policy', required=True, help="""The load balancer policy for the backend set. To get a list of available policies, use the [ListPolicies] operation.

Example: `LEAST_CONNECTIONS`""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer on which to add a backend set.""")
@cli_util.option('--backends', type=custom_types.CLI_COMPLEX_TYPE, help="""

This option is a JSON list with items of type BackendDetails.  For documentation on BackendDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/loadbalancer/20170115/datatypes/BackendDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--session-persistence-configuration', type=custom_types.CLI_COMPLEX_TYPE, help="""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ssl-configuration', type=custom_types.CLI_COMPLEX_TYPE, help="""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'backends': {'module': 'load_balancer', 'class': 'list[BackendDetails]'}, 'health-checker': {'module': 'load_balancer', 'class': 'HealthCheckerDetails'}, 'session-persistence-configuration': {'module': 'load_balancer', 'class': 'SessionPersistenceConfigurationDetails'}, 'ssl-configuration': {'module': 'load_balancer', 'class': 'SSLConfigurationDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backends': {'module': 'load_balancer', 'class': 'list[BackendDetails]'}, 'health-checker': {'module': 'load_balancer', 'class': 'HealthCheckerDetails'}, 'session-persistence-configuration': {'module': 'load_balancer', 'class': 'SessionPersistenceConfigurationDetails'}, 'ssl-configuration': {'module': 'load_balancer', 'class': 'SSLConfigurationDetails'}})
@cli_util.wrap_exceptions
def create_backend_set(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, health_checker, name, policy, load_balancer_id, backends, session_persistence_configuration, ssl_configuration):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['healthChecker'] = cli_util.parse_json_parameter("health_checker", health_checker)
    details['name'] = name
    details['policy'] = policy

    if backends is not None:
        details['backends'] = cli_util.parse_json_parameter("backends", backends)

    if session_persistence_configuration is not None:
        details['sessionPersistenceConfiguration'] = cli_util.parse_json_parameter("session_persistence_configuration", session_persistence_configuration)

    if ssl_configuration is not None:
        details['sslConfiguration'] = cli_util.parse_json_parameter("ssl_configuration", ssl_configuration)

    client = cli_util.build_client('load_balancer', ctx)
    result = client.create_backend_set(
        load_balancer_id=load_balancer_id,
        create_backend_set_details=details,
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@certificate_group.command(name=cli_util.override('create_certificate.command_name', 'create'), help="""Creates an asynchronous request to add an SSL certificate bundle.""")
@cli_util.option('--certificate-name', required=True, help="""A friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores. Certificate bundle names cannot contain spaces. Avoid entering confidential information.

Example: `example_certificate_bundle`""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer on which to add the certificate bundle.""")
@cli_util.option('--ca-certificate', help="""The Certificate Authority certificate, or any interim certificate, that you received from your SSL certificate provider.

Example:

    -----BEGIN CERTIFICATE-----     MIIEczCCA1ugAwIBAgIBADANBgkqhkiG9w0BAQQFAD..AkGA1UEBhMCR0Ix     EzARBgNVBAgTClNvbWUtU3RhdGUxFDASBgNVBAoTC0..0EgTHRkMTcwNQYD     VQQLEy5DbGFzcyAxIFB1YmxpYyBQcmltYXJ5IENlcn..XRpb24gQXV0aG9y     aXR5MRQwEgYDVQQDEwtCZXN0IENBIEx0ZDAeFw0wMD..TUwMTZaFw0wMTAy     ...     -----END CERTIFICATE-----""")
@cli_util.option('--passphrase', help="""A passphrase for encrypted private keys. This is needed only if you created your certificate with a passphrase.""")
@cli_util.option('--private-key', help="""The SSL private key for your certificate, in PEM format.

Example:

    -----BEGIN RSA PRIVATE KEY-----     jO1O1v2ftXMsawM90tnXwc6xhOAT1gDBC9S8DKeca..JZNUgYYwNS0dP2UK     tmyN+XqVcAKw4HqVmChXy5b5msu8eIq3uc2NqNVtR..2ksSLukP8pxXcHyb     +sEwvM4uf8qbnHAqwnOnP9+KV9vds6BaH1eRA4CHz..n+NVZlzBsTxTlS16     /Umr7wJzVrMqK5sDiSu4WuaaBdqMGfL5hLsTjcBFD..Da2iyQmSKuVD4lIZ     ...     -----END RSA PRIVATE KEY-----""")
@cli_util.option('--public-certificate', help="""The public certificate, in PEM format, that you received from your SSL certificate provider.

Example:

    -----BEGIN CERTIFICATE-----     MIIC2jCCAkMCAg38MA0GCSqGSIb3DQEBBQUAMIGbM..QswCQYDVQQGEwJKU     A1UECBMFVG9reW8xEDAOBgNVBAcTB0NodW8ta3UxE..TAPBgNVBAoTCEZyY     MRgwFgYDVQQLEw9XZWJDZXJ0IFN1cHBvcnQxGDAWB..gNVBAMTD0ZyYW5rN     YiBDQTEjMCEGCSqGSIb3DQEJARYUc3VwcG9ydEBmc..mFuazRkZC5jb20wH     ...     -----END CERTIFICATE-----""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def create_certificate(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, certificate_name, load_balancer_id, ca_certificate, passphrase, private_key, public_certificate):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['certificateName'] = certificate_name

    if ca_certificate is not None:
        details['caCertificate'] = ca_certificate

    if passphrase is not None:
        details['passphrase'] = passphrase

    if private_key is not None:
        details['privateKey'] = private_key

    if public_certificate is not None:
        details['publicCertificate'] = public_certificate

    client = cli_util.build_client('load_balancer', ctx)
    result = client.create_certificate(
        load_balancer_id=load_balancer_id,
        create_certificate_details=details,
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@hostname_group.command(name=cli_util.override('create_hostname.command_name', 'create'), help="""Adds a hostname resource to the specified load balancer. For more information, see [Managing Request Routing].""")
@cli_util.option('--hostname', required=True, help="""A virtual hostname. For more information about virtual hostname string construction, see [Managing Request Routing].

Example: `app.example.com`""")
@cli_util.option('--name', required=True, help="""A friendly name for the hostname resource. It must be unique and it cannot be changed. Avoid entering confidential information.

Example: `example_hostname_001`""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer to add the hostname to.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def create_hostname(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, hostname, name, load_balancer_id):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['hostname'] = hostname
    details['name'] = name

    client = cli_util.build_client('load_balancer', ctx)
    result = client.create_hostname(
        load_balancer_id=load_balancer_id,
        create_hostname_details=details,
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@listener_group.command(name=cli_util.override('create_listener.command_name', 'create'), help="""Adds a listener to a load balancer.""")
@cli_util.option('--default-backend-set-name', required=True, help="""The name of the associated backend set.

Example: `example_backend_set`""")
@cli_util.option('--name', required=True, help="""A friendly name for the listener. It must be unique and it cannot be changed. Avoid entering confidential information.

Example: `example_listener`""")
@cli_util.option('--port', required=True, type=click.INT, help="""The communication port for the listener.

Example: `80`""")
@cli_util.option('--protocol', required=True, help="""The protocol on which the listener accepts connection requests. To get a list of valid protocols, use the [ListProtocols] operation.

Example: `HTTP`""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer on which to add a listener.""")
@cli_util.option('--connection-configuration', type=custom_types.CLI_COMPLEX_TYPE, help="""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--hostname-names', type=custom_types.CLI_COMPLEX_TYPE, help="""An array of hostname resource names.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--path-route-set-name', help="""The name of the set of path-based routing rules, [PathRouteSet], applied to this listener's traffic.

Example: `example_path_route_set`""")
@cli_util.option('--ssl-configuration', type=custom_types.CLI_COMPLEX_TYPE, help="""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'connection-configuration': {'module': 'load_balancer', 'class': 'ConnectionConfiguration'}, 'hostname-names': {'module': 'load_balancer', 'class': 'list[string]'}, 'ssl-configuration': {'module': 'load_balancer', 'class': 'SSLConfigurationDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'connection-configuration': {'module': 'load_balancer', 'class': 'ConnectionConfiguration'}, 'hostname-names': {'module': 'load_balancer', 'class': 'list[string]'}, 'ssl-configuration': {'module': 'load_balancer', 'class': 'SSLConfigurationDetails'}})
@cli_util.wrap_exceptions
def create_listener(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, default_backend_set_name, name, port, protocol, load_balancer_id, connection_configuration, hostname_names, path_route_set_name, ssl_configuration):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['defaultBackendSetName'] = default_backend_set_name
    details['name'] = name
    details['port'] = port
    details['protocol'] = protocol

    if connection_configuration is not None:
        details['connectionConfiguration'] = cli_util.parse_json_parameter("connection_configuration", connection_configuration)

    if hostname_names is not None:
        details['hostnameNames'] = cli_util.parse_json_parameter("hostname_names", hostname_names)

    if path_route_set_name is not None:
        details['pathRouteSetName'] = path_route_set_name

    if ssl_configuration is not None:
        details['sslConfiguration'] = cli_util.parse_json_parameter("ssl_configuration", ssl_configuration)

    client = cli_util.build_client('load_balancer', ctx)
    result = client.create_listener(
        load_balancer_id=load_balancer_id,
        create_listener_details=details,
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@load_balancer_group.command(name=cli_util.override('create_load_balancer.command_name', 'create'), help="""Creates a new load balancer in the specified compartment. For general information about load balancers, see [Overview of the Load Balancing Service].

For the purposes of access control, you must provide the OCID of the compartment where you want the load balancer to reside. Notice that the load balancer doesn't have to be in the same compartment as the VCN or backend set. If you're not sure which compartment to use, put the load balancer in the same compartment as the VCN. For information about access control and compartments, see [Overview of the IAM Service].

You must specify a display name for the load balancer. It does not have to be unique, and you can change it.

For information about Availability Domains, see [Regions and Availability Domains]. To get a list of Availability Domains, use the `ListAvailabilityDomains` operation in the Identity and Access Management Service API.

All Oracle Cloud Infrastructure resources, including load balancers, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. Fore more information, see [Resource Identifiers].

After you send your request, the new object's state will temporarily be PROVISIONING. Before using the object, first make sure its state has changed to RUNNING.

When you create a load balancer, the system assigns an IP address. To get the IP address, use the [GetLoadBalancer] operation.""")
@cli_util.option('--compartment-id', required=True, help="""The [OCID] of the compartment in which to create the load balancer.""")
@cli_util.option('--display-name', required=True, help="""A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.

Example: `example_load_balancer`""")
@cli_util.option('--shape-name', required=True, help="""A template that determines the total pre-provisioned bandwidth (ingress plus egress). To get a list of available shapes, use the [ListShapes] operation.

Example: `100Mbps`""")
@cli_util.option('--subnet-ids', required=True, type=custom_types.CLI_COMPLEX_TYPE, help="""An array of subnet [OCIDs].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--backend-sets', type=custom_types.CLI_COMPLEX_TYPE, help="""

This option is a JSON dictionary of type dict(str, BackendSetDetails).  For documentation on BackendSetDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/loadbalancer/20170115/datatypes/BackendSetDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--certificates', type=custom_types.CLI_COMPLEX_TYPE, help="""

This option is a JSON dictionary of type dict(str, CertificateDetails).  For documentation on CertificateDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/loadbalancer/20170115/datatypes/CertificateDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--hostnames', type=custom_types.CLI_COMPLEX_TYPE, help="""

This option is a JSON dictionary of type dict(str, HostnameDetails).  For documentation on HostnameDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/loadbalancer/20170115/datatypes/HostnameDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-private', type=click.BOOL, help="""Whether the load balancer has a VCN-local (private) IP address.

If \"true\", the service assigns a private IP address to the load balancer. The load balancer requires only one subnet to host both the primary and secondary load balancers. The private IP address is local to the subnet. The load balancer is accessible only from within the VCN that contains the associated subnet, or as further restricted by your security list rules. The load balancer can route traffic to any backend server that is reachable from the VCN.

For a private load balancer, both the primary and secondary load balancer hosts are within the same Availability Domain.

If \"false\", the service assigns a public IP address to the load balancer. A load balancer with a public IP address requires two subnets, each in a different Availability Domain. One subnet hosts the primary load balancer and the other hosts the secondary (standby) load balancer. A public load balancer is accessible from the internet, depending on your VCN's [security list rules].

Example: `true`""")
@cli_util.option('--listeners', type=custom_types.CLI_COMPLEX_TYPE, help="""

This option is a JSON dictionary of type dict(str, ListenerDetails).  For documentation on ListenerDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/loadbalancer/20170115/datatypes/ListenerDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--path-route-sets', type=custom_types.CLI_COMPLEX_TYPE, help="""

This option is a JSON dictionary of type dict(str, PathRouteSetDetails).  For documentation on PathRouteSetDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/loadbalancer/20170115/datatypes/PathRouteSetDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'backend-sets': {'module': 'load_balancer', 'class': 'dict(str, BackendSetDetails)'}, 'certificates': {'module': 'load_balancer', 'class': 'dict(str, CertificateDetails)'}, 'defined-tags': {'module': 'load_balancer', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'load_balancer', 'class': 'dict(str, string)'}, 'hostnames': {'module': 'load_balancer', 'class': 'dict(str, HostnameDetails)'}, 'listeners': {'module': 'load_balancer', 'class': 'dict(str, ListenerDetails)'}, 'path-route-sets': {'module': 'load_balancer', 'class': 'dict(str, PathRouteSetDetails)'}, 'subnet-ids': {'module': 'load_balancer', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backend-sets': {'module': 'load_balancer', 'class': 'dict(str, BackendSetDetails)'}, 'certificates': {'module': 'load_balancer', 'class': 'dict(str, CertificateDetails)'}, 'defined-tags': {'module': 'load_balancer', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'load_balancer', 'class': 'dict(str, string)'}, 'hostnames': {'module': 'load_balancer', 'class': 'dict(str, HostnameDetails)'}, 'listeners': {'module': 'load_balancer', 'class': 'dict(str, ListenerDetails)'}, 'path-route-sets': {'module': 'load_balancer', 'class': 'dict(str, PathRouteSetDetails)'}, 'subnet-ids': {'module': 'load_balancer', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def create_load_balancer(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, shape_name, subnet_ids, backend_sets, certificates, defined_tags, freeform_tags, hostnames, is_private, listeners, path_route_sets):
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['compartmentId'] = compartment_id
    details['displayName'] = display_name
    details['shapeName'] = shape_name
    details['subnetIds'] = cli_util.parse_json_parameter("subnet_ids", subnet_ids)

    if backend_sets is not None:
        details['backendSets'] = cli_util.parse_json_parameter("backend_sets", backend_sets)

    if certificates is not None:
        details['certificates'] = cli_util.parse_json_parameter("certificates", certificates)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if hostnames is not None:
        details['hostnames'] = cli_util.parse_json_parameter("hostnames", hostnames)

    if is_private is not None:
        details['isPrivate'] = is_private

    if listeners is not None:
        details['listeners'] = cli_util.parse_json_parameter("listeners", listeners)

    if path_route_sets is not None:
        details['pathRouteSets'] = cli_util.parse_json_parameter("path_route_sets", path_route_sets)

    client = cli_util.build_client('load_balancer', ctx)
    result = client.create_load_balancer(
        create_load_balancer_details=details,
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@path_route_set_group.command(name=cli_util.override('create_path_route_set.command_name', 'create'), help="""Adds a path route set to a load balancer. For more information, see [Managing Request Routing].""")
@cli_util.option('--name', required=True, help="""The name for this set of path route rules. It must be unique and it cannot be changed. Avoid entering confidential information.

Example: `example_path_route_set`""")
@cli_util.option('--path-routes', required=True, type=custom_types.CLI_COMPLEX_TYPE, help="""The set of path route rules.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer to add the path route set to.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state.""")
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

    details = {}
    details['name'] = name
    details['pathRoutes'] = cli_util.parse_json_parameter("path_routes", path_routes)

    client = cli_util.build_client('load_balancer', ctx)
    result = client.create_path_route_set(
        load_balancer_id=load_balancer_id,
        create_path_route_set_details=details,
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@backend_group.command(name=cli_util.override('delete_backend.command_name', 'delete'), help="""Removes a backend server from a given load balancer and backend set.""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer associated with the backend set and server.""")
@cli_util.option('--backend-set-name', required=True, help="""The name of the backend set associated with the backend server.

Example: `example_backend_set`""")
@cli_util.option('--backend-name', required=True, help="""The IP address and port of the backend server to remove.

Example: `10.0.0.3:8080`""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state.""")
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
    client = cli_util.build_client('load_balancer', ctx)
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@backend_set_group.command(name=cli_util.override('delete_backend_set.command_name', 'delete'), help="""Deletes the specified backend set. Note that deleting a backend set removes its backend servers from the load balancer.

Before you can delete a backend set, you must remove it from any active listeners.""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer associated with the backend set.""")
@cli_util.option('--backend-set-name', required=True, help="""The name of the backend set to delete.

Example: `example_backend_set`""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state.""")
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
    client = cli_util.build_client('load_balancer', ctx)
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@certificate_group.command(name=cli_util.override('delete_certificate.command_name', 'delete'), help="""Deletes an SSL certificate bundle from a load balancer.""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer associated with the certificate bundle to be deleted.""")
@cli_util.option('--certificate-name', required=True, help="""The name of the certificate bundle to delete.

Example: `example_certificate_bundle`""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state.""")
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
    client = cli_util.build_client('load_balancer', ctx)
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@hostname_group.command(name=cli_util.override('delete_hostname.command_name', 'delete'), help="""Deletes a hostname resource from the specified load balancer.""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer associated with the hostname to delete.""")
@cli_util.option('--name', required=True, help="""The name of the hostname resource to delete.

Example: `example_hostname_001`""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state.""")
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
    client = cli_util.build_client('load_balancer', ctx)
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@listener_group.command(name=cli_util.override('delete_listener.command_name', 'delete'), help="""Deletes a listener from a load balancer.""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer associated with the listener to delete.""")
@cli_util.option('--listener-name', required=True, help="""The name of the listener to delete.

Example: `example_listener`""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state.""")
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
    client = cli_util.build_client('load_balancer', ctx)
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@load_balancer_group.command(name=cli_util.override('delete_load_balancer.command_name', 'delete'), help="""Stops a load balancer and removes it from service.""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer to delete.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state.""")
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
    client = cli_util.build_client('load_balancer', ctx)
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@path_route_set_group.command(name=cli_util.override('delete_path_route_set.command_name', 'delete'), help="""Deletes a path route set from the specified load balancer.

To delete a path route rule from a path route set, use the [UpdatePathRouteSet] operation.""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer associated with the path route set to delete.""")
@cli_util.option('--path-route-set-name', required=True, help="""The name of the path route set to delete.

Example: `example_path_route_set`""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state.""")
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
    client = cli_util.build_client('load_balancer', ctx)
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@backend_group.command(name=cli_util.override('get_backend.command_name', 'get'), help="""Gets the specified backend server's configuration information.""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer associated with the backend set and server.""")
@cli_util.option('--backend-set-name', required=True, help="""The name of the backend set that includes the backend server.

Example: `example_backend_set`""")
@cli_util.option('--backend-name', required=True, help="""The IP address and port of the backend server to retrieve.

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
    client = cli_util.build_client('load_balancer', ctx)
    result = client.get_backend(
        load_balancer_id=load_balancer_id,
        backend_set_name=backend_set_name,
        backend_name=backend_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@backend_health_group.command(name=cli_util.override('get_backend_health.command_name', 'get'), help="""Gets the current health status of the specified backend server.""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer associated with the backend server health status to be retrieved.""")
@cli_util.option('--backend-set-name', required=True, help="""The name of the backend set associated with the backend server to retrieve the health status for.

Example: `example_backend_set`""")
@cli_util.option('--backend-name', required=True, help="""The IP address and port of the backend server to retrieve the health status for.

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
    client = cli_util.build_client('load_balancer', ctx)
    result = client.get_backend_health(
        load_balancer_id=load_balancer_id,
        backend_set_name=backend_set_name,
        backend_name=backend_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@backend_set_group.command(name=cli_util.override('get_backend_set.command_name', 'get'), help="""Gets the specified backend set's configuration information.""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the specified load balancer.""")
@cli_util.option('--backend-set-name', required=True, help="""The name of the backend set to retrieve.

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
    client = cli_util.build_client('load_balancer', ctx)
    result = client.get_backend_set(
        load_balancer_id=load_balancer_id,
        backend_set_name=backend_set_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@backend_set_health_group.command(name=cli_util.override('get_backend_set_health.command_name', 'get'), help="""Gets the health status for the specified backend set.""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer associated with the backend set health status to be retrieved.""")
@cli_util.option('--backend-set-name', required=True, help="""The name of the backend set to retrieve the health status for.

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
    client = cli_util.build_client('load_balancer', ctx)
    result = client.get_backend_set_health(
        load_balancer_id=load_balancer_id,
        backend_set_name=backend_set_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@health_checker_group.command(name=cli_util.override('get_health_checker.command_name', 'get'), help="""Gets the health check policy information for a given load balancer and backend set.""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer associated with the health check policy to be retrieved.""")
@cli_util.option('--backend-set-name', required=True, help="""The name of the backend set associated with the health check policy to be retrieved.

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
    client = cli_util.build_client('load_balancer', ctx)
    result = client.get_health_checker(
        load_balancer_id=load_balancer_id,
        backend_set_name=backend_set_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@hostname_group.command(name=cli_util.override('get_hostname.command_name', 'get'), help="""Gets the specified hostname resource's configuration information.""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the specified load balancer.""")
@cli_util.option('--name', required=True, help="""The name of the hostname resource to retrieve.

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
    client = cli_util.build_client('load_balancer', ctx)
    result = client.get_hostname(
        load_balancer_id=load_balancer_id,
        name=name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@load_balancer_group.command(name=cli_util.override('get_load_balancer.command_name', 'get'), help="""Gets the specified load balancer's configuration information.""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer to retrieve.""")
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
    client = cli_util.build_client('load_balancer', ctx)
    result = client.get_load_balancer(
        load_balancer_id=load_balancer_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@load_balancer_health_group.command(name=cli_util.override('get_load_balancer_health.command_name', 'get'), help="""Gets the health status for the specified load balancer.""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer to return health status for.""")
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
    client = cli_util.build_client('load_balancer', ctx)
    result = client.get_load_balancer_health(
        load_balancer_id=load_balancer_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@path_route_set_group.command(name=cli_util.override('get_path_route_set.command_name', 'get'), help="""Gets the specified path route set's configuration information.""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the specified load balancer.""")
@cli_util.option('--path-route-set-name', required=True, help="""The name of the path route set to retrieve.

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
    client = cli_util.build_client('load_balancer', ctx)
    result = client.get_path_route_set(
        load_balancer_id=load_balancer_id,
        path_route_set_name=path_route_set_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('get_work_request.command_name', 'get'), help="""Gets the details of a work request.""")
@cli_util.option('--work-request-id', required=True, help="""The [OCID] of the work request to retrieve.""")
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
    client = cli_util.build_client('load_balancer', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@backend_set_group.command(name=cli_util.override('list_backend_sets.command_name', 'list'), help="""Lists all backend sets associated with a given load balancer.""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer associated with the backend sets to retrieve.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'list[BackendSet]'})
@cli_util.wrap_exceptions
def list_backend_sets(ctx, from_json, load_balancer_id):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', ctx)
    result = client.list_backend_sets(
        load_balancer_id=load_balancer_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@backend_group.command(name=cli_util.override('list_backends.command_name', 'list'), help="""Lists the backend servers for a given load balancer and backend set.""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer associated with the backend set and servers.""")
@cli_util.option('--backend-set-name', required=True, help="""The name of the backend set associated with the backend servers.

Example: `example_backend_set`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'list[Backend]'})
@cli_util.wrap_exceptions
def list_backends(ctx, from_json, load_balancer_id, backend_set_name):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', ctx)
    result = client.list_backends(
        load_balancer_id=load_balancer_id,
        backend_set_name=backend_set_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@certificate_group.command(name=cli_util.override('list_certificates.command_name', 'list'), help="""Lists all SSL certificates bundles associated with a given load balancer.""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer associated with the certificate bundles to be listed.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'list[Certificate]'})
@cli_util.wrap_exceptions
def list_certificates(ctx, from_json, load_balancer_id):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', ctx)
    result = client.list_certificates(
        load_balancer_id=load_balancer_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@hostname_group.command(name=cli_util.override('list_hostnames.command_name', 'list'), help="""Lists all hostname resources associated with the specified load balancer.""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer associated with the hostnames to retrieve.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'list[Hostname]'})
@cli_util.wrap_exceptions
def list_hostnames(ctx, from_json, load_balancer_id):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', ctx)
    result = client.list_hostnames(
        load_balancer_id=load_balancer_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@load_balancer_health_group.command(name=cli_util.override('list_load_balancer_healths.command_name', 'list'), help="""Lists the summary health statuses for all load balancers in the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help="""The [OCID] of the compartment containing the load balancers to return health status information for.""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@cli_util.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.

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
    client = cli_util.build_client('load_balancer', ctx)
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


@load_balancer_group.command(name=cli_util.override('list_load_balancers.command_name', 'list'), help="""Lists all load balancers in the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help="""The [OCID] of the compartment containing the load balancers to list.""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@cli_util.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.

Example: `3`""")
@cli_util.option('--detail', help="""The level of detail to return for each result. Can be `full` or `simple`.

Example: `full`""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by.  You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--display-name', help="""A filter to return only resources that match the given display name exactly.

Example: `example_load_balancer`""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "FAILED", "ACTIVE", "DELETING", "DELETED"]), help="""A filter to return only resources that match the given lifecycle state.

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
    client = cli_util.build_client('load_balancer', ctx)
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


@path_route_set_group.command(name=cli_util.override('list_path_route_sets.command_name', 'list'), help="""Lists all path route sets associated with the specified load balancer.""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer associated with the path route sets to retrieve.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'load_balancer', 'class': 'list[PathRouteSet]'})
@cli_util.wrap_exceptions
def list_path_route_sets(ctx, from_json, load_balancer_id):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('load_balancer', ctx)
    result = client.list_path_route_sets(
        load_balancer_id=load_balancer_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@load_balancer_policy_group.command(name=cli_util.override('list_policies.command_name', 'list-policies'), help="""Lists the available load balancer policies.""")
@cli_util.option('--compartment-id', required=True, help="""The [OCID] of the compartment containing the load balancer policies to list.""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@cli_util.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.

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
    client = cli_util.build_client('load_balancer', ctx)
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


@load_balancer_protocol_group.command(name=cli_util.override('list_protocols.command_name', 'list-protocols'), help="""Lists all supported traffic protocols.""")
@cli_util.option('--compartment-id', required=True, help="""The [OCID] of the compartment containing the load balancer protocols to list.""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@cli_util.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.

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
    client = cli_util.build_client('load_balancer', ctx)
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


@load_balancer_shape_group.command(name=cli_util.override('list_shapes.command_name', 'list-shapes'), help="""Lists the valid load balancer shapes.""")
@cli_util.option('--compartment-id', required=True, help="""The [OCID] of the compartment containing the load balancer shapes to list.""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@cli_util.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.

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
    client = cli_util.build_client('load_balancer', ctx)
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


@work_request_group.command(name=cli_util.override('list_work_requests.command_name', 'list'), help="""Lists the work requests for a given load balancer.""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer associated with the work requests to retrieve.""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@cli_util.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.

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
    client = cli_util.build_client('load_balancer', ctx)
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


@backend_group.command(name=cli_util.override('update_backend.command_name', 'update'), help="""Updates the configuration of a backend server within the specified backend set.""")
@cli_util.option('--backup', required=True, type=click.BOOL, help="""Whether the load balancer should treat this server as a backup unit. If `true`, the load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as \"backup\" fail the health check policy.

Example: `false`""")
@cli_util.option('--drain', required=True, type=click.BOOL, help="""Whether the load balancer should drain this server. Servers marked \"drain\" receive no new incoming traffic.

Example: `false`""")
@cli_util.option('--offline', required=True, type=click.BOOL, help="""Whether the load balancer should treat this server as offline. Offline servers receive no incoming traffic.

Example: `false`""")
@cli_util.option('--weight', required=True, type=click.INT, help="""The load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted '3' receives 3 times the number of new connections as a server weighted '1'. For more information on load balancing policies, see [How Load Balancing Policies Work].

Example: `3`""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer associated with the backend set and server.""")
@cli_util.option('--backend-set-name', required=True, help="""The name of the backend set associated with the backend server.

Example: `example_backend_set`""")
@cli_util.option('--backend-name', required=True, help="""The IP address and port of the backend server to update.

Example: `10.0.0.3:8080`""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_backend(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, backup, drain, offline, weight, load_balancer_id, backend_set_name, backend_name):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')

    if isinstance(backend_name, six.string_types) and len(backend_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-name cannot be whitespace or empty string')
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['backup'] = backup
    details['drain'] = drain
    details['offline'] = offline
    details['weight'] = weight

    client = cli_util.build_client('load_balancer', ctx)
    result = client.update_backend(
        load_balancer_id=load_balancer_id,
        backend_set_name=backend_set_name,
        backend_name=backend_name,
        update_backend_details=details,
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@backend_set_group.command(name=cli_util.override('update_backend_set.command_name', 'update'), help="""Updates a backend set.""")
@cli_util.option('--backends', required=True, type=custom_types.CLI_COMPLEX_TYPE, help="""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--health-checker', required=True, type=custom_types.CLI_COMPLEX_TYPE, help="""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--policy', required=True, help="""The load balancer policy for the backend set. To get a list of available policies, use the [ListPolicies] operation.

Example: `LEAST_CONNECTIONS`""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer associated with the backend set.""")
@cli_util.option('--backend-set-name', required=True, help="""The name of the backend set to update.

Example: `example_backend_set`""")
@cli_util.option('--session-persistence-configuration', type=custom_types.CLI_COMPLEX_TYPE, help="""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ssl-configuration', type=custom_types.CLI_COMPLEX_TYPE, help="""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'backends': {'module': 'load_balancer', 'class': 'list[BackendDetails]'}, 'health-checker': {'module': 'load_balancer', 'class': 'HealthCheckerDetails'}, 'session-persistence-configuration': {'module': 'load_balancer', 'class': 'SessionPersistenceConfigurationDetails'}, 'ssl-configuration': {'module': 'load_balancer', 'class': 'SSLConfigurationDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backends': {'module': 'load_balancer', 'class': 'list[BackendDetails]'}, 'health-checker': {'module': 'load_balancer', 'class': 'HealthCheckerDetails'}, 'session-persistence-configuration': {'module': 'load_balancer', 'class': 'SessionPersistenceConfigurationDetails'}, 'ssl-configuration': {'module': 'load_balancer', 'class': 'SSLConfigurationDetails'}})
@cli_util.wrap_exceptions
def update_backend_set(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, backends, health_checker, policy, load_balancer_id, backend_set_name, session_persistence_configuration, ssl_configuration):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')
    if not force:
        if backends or health_checker or session_persistence_configuration or ssl_configuration:
            if not click.confirm("WARNING: Updates to backends and health-checker and session-persistence-configuration and ssl-configuration will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['backends'] = cli_util.parse_json_parameter("backends", backends)
    details['healthChecker'] = cli_util.parse_json_parameter("health_checker", health_checker)
    details['policy'] = policy

    if session_persistence_configuration is not None:
        details['sessionPersistenceConfiguration'] = cli_util.parse_json_parameter("session_persistence_configuration", session_persistence_configuration)

    if ssl_configuration is not None:
        details['sslConfiguration'] = cli_util.parse_json_parameter("ssl_configuration", ssl_configuration)

    client = cli_util.build_client('load_balancer', ctx)
    result = client.update_backend_set(
        load_balancer_id=load_balancer_id,
        backend_set_name=backend_set_name,
        update_backend_set_details=details,
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@health_checker_group.command(name=cli_util.override('update_health_checker.command_name', 'update'), help="""Updates the health check policy for a given load balancer and backend set.""")
@cli_util.option('--interval-in-millis', required=True, type=click.INT, help="""The interval between health checks, in milliseconds.

Example: `10000`""")
@cli_util.option('--port', required=True, type=click.INT, help="""The backend server port against which to run the health check.

Example: `8080`""")
@cli_util.option('--protocol', required=True, help="""The protocol the health check must use; either HTTP or TCP.

Example: `HTTP`""")
@cli_util.option('--response-body-regex', required=True, help="""A regular expression for parsing the response body from the backend server.

Example: `^((?!false).|\\s)*$`""")
@cli_util.option('--retries', required=True, type=click.INT, help="""The number of retries to attempt before a backend server is considered \"unhealthy\".

Example: `3`""")
@cli_util.option('--return-code', required=True, type=click.INT, help="""The status code a healthy backend server should return.

Example: `200`""")
@cli_util.option('--timeout-in-millis', required=True, type=click.INT, help="""The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply returns within this timeout period.

Example: `3000`""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer associated with the health check policy to be updated.""")
@cli_util.option('--backend-set-name', required=True, help="""The name of the backend set associated with the health check policy to be retrieved.

Example: `example_backend_set`""")
@cli_util.option('--url-path', help="""The path against which to run the health check.

Example: `/healthcheck`""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_health_checker(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, interval_in_millis, port, protocol, response_body_regex, retries, return_code, timeout_in_millis, load_balancer_id, backend_set_name, url_path):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(backend_set_name, six.string_types) and len(backend_set_name.strip()) == 0:
        raise click.UsageError('Parameter --backend-set-name cannot be whitespace or empty string')
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['intervalInMillis'] = interval_in_millis
    details['port'] = port
    details['protocol'] = protocol
    details['responseBodyRegex'] = response_body_regex
    details['retries'] = retries
    details['returnCode'] = return_code
    details['timeoutInMillis'] = timeout_in_millis

    if url_path is not None:
        details['urlPath'] = url_path

    client = cli_util.build_client('load_balancer', ctx)
    result = client.update_health_checker(
        load_balancer_id=load_balancer_id,
        backend_set_name=backend_set_name,
        health_checker=details,
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@hostname_group.command(name=cli_util.override('update_hostname.command_name', 'update'), help="""Overwrites an existing hostname resource on the specified load balancer. Use this operation to change a virtual hostname.""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer associated with the virtual hostname to update.""")
@cli_util.option('--name', required=True, help="""The name of the hostname resource to update.

Example: `example_hostname_001`""")
@cli_util.option('--hostname', help="""The virtual hostname to update. For more information about virtual hostname string construction, see [Managing Request Routing].

Example: `app.example.com`""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state.""")
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

    details = {}

    if hostname is not None:
        details['hostname'] = hostname

    client = cli_util.build_client('load_balancer', ctx)
    result = client.update_hostname(
        load_balancer_id=load_balancer_id,
        name=name,
        update_hostname_details=details,
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@listener_group.command(name=cli_util.override('update_listener.command_name', 'update'), help="""Updates a listener for a given load balancer.""")
@cli_util.option('--default-backend-set-name', required=True, help="""The name of the associated backend set.

Example: `example_backend_set`""")
@cli_util.option('--port', required=True, type=click.INT, help="""The communication port for the listener.

Example: `80`""")
@cli_util.option('--protocol', required=True, help="""The protocol on which the listener accepts connection requests. To get a list of valid protocols, use the [ListProtocols] operation.

Example: `HTTP`""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer associated with the listener to update.""")
@cli_util.option('--listener-name', required=True, help="""The name of the listener to update.

Example: `example_listener`""")
@cli_util.option('--connection-configuration', type=custom_types.CLI_COMPLEX_TYPE, help="""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--hostname-names', type=custom_types.CLI_COMPLEX_TYPE, help="""An array of hostname resource names.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--path-route-set-name', help="""The name of the set of path-based routing rules, [PathRouteSet], applied to this listener's traffic.

Example: `example_path_route_set`""")
@cli_util.option('--ssl-configuration', type=custom_types.CLI_COMPLEX_TYPE, help="""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'connection-configuration': {'module': 'load_balancer', 'class': 'ConnectionConfiguration'}, 'hostname-names': {'module': 'load_balancer', 'class': 'list[string]'}, 'ssl-configuration': {'module': 'load_balancer', 'class': 'SSLConfigurationDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'connection-configuration': {'module': 'load_balancer', 'class': 'ConnectionConfiguration'}, 'hostname-names': {'module': 'load_balancer', 'class': 'list[string]'}, 'ssl-configuration': {'module': 'load_balancer', 'class': 'SSLConfigurationDetails'}})
@cli_util.wrap_exceptions
def update_listener(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, default_backend_set_name, port, protocol, load_balancer_id, listener_name, connection_configuration, hostname_names, path_route_set_name, ssl_configuration):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')

    if isinstance(listener_name, six.string_types) and len(listener_name.strip()) == 0:
        raise click.UsageError('Parameter --listener-name cannot be whitespace or empty string')
    if not force:
        if connection_configuration or hostname_names or ssl_configuration:
            if not click.confirm("WARNING: Updates to connection-configuration and hostname-names and ssl-configuration will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['defaultBackendSetName'] = default_backend_set_name
    details['port'] = port
    details['protocol'] = protocol

    if connection_configuration is not None:
        details['connectionConfiguration'] = cli_util.parse_json_parameter("connection_configuration", connection_configuration)

    if hostname_names is not None:
        details['hostnameNames'] = cli_util.parse_json_parameter("hostname_names", hostname_names)

    if path_route_set_name is not None:
        details['pathRouteSetName'] = path_route_set_name

    if ssl_configuration is not None:
        details['sslConfiguration'] = cli_util.parse_json_parameter("ssl_configuration", ssl_configuration)

    client = cli_util.build_client('load_balancer', ctx)
    result = client.update_listener(
        load_balancer_id=load_balancer_id,
        listener_name=listener_name,
        update_listener_details=details,
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@load_balancer_group.command(name=cli_util.override('update_load_balancer.command_name', 'update'), help="""Updates a load balancer's configuration.""")
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer to update.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""The user-friendly display name for the load balancer. It does not have to be unique, and it is changeable. Avoid entering confidential information.

Example: `example_load_balancer`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'load_balancer', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'load_balancer', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'load_balancer', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'load_balancer', 'class': 'dict(str, string)'}})
@cli_util.wrap_exceptions
def update_load_balancer(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, load_balancer_id, defined_tags, display_name, freeform_tags):

    if isinstance(load_balancer_id, six.string_types) and len(load_balancer_id.strip()) == 0:
        raise click.UsageError('Parameter --load-balancer-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('load_balancer', ctx)
    result = client.update_load_balancer(
        load_balancer_id=load_balancer_id,
        update_load_balancer_details=details,
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@path_route_set_group.command(name=cli_util.override('update_path_route_set.command_name', 'update'), help="""Overwrites an existing path route set on the specified load balancer. Use this operation to add, delete, or alter path route rules in a path route set.

To add a new path route rule to a path route set, the `pathRoutes` in the [UpdatePathRouteSetDetails] object must include both the new path route rule to add and the existing path route rules to retain.""")
@cli_util.option('--path-routes', required=True, type=custom_types.CLI_COMPLEX_TYPE, help="""The set of path route rules.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--load-balancer-id', required=True, help="""The [OCID] of the load balancer associated with the path route set to update.""")
@cli_util.option('--path-route-set-name', required=True, help="""The name of the path route set to update.

Example: `example_path_route_set`""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state.""")
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

    details = {}
    details['pathRoutes'] = cli_util.parse_json_parameter("path_routes", path_routes)

    client = cli_util.build_client('load_balancer', ctx)
    result = client.update_path_route_set(
        load_balancer_id=load_balancer_id,
        path_route_set_name=path_route_set_name,
        update_path_route_set_details=details,
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
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
