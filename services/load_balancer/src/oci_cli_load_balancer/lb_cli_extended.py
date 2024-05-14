# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import json
import six  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from services.load_balancer.src.oci_cli_load_balancer.generated import loadbalancer_cli

# Rename some commands and groups
cli_util.rename_command(loadbalancer_cli, loadbalancer_cli.lb_root_group, loadbalancer_cli.load_balancer_policy_group, "policy")
cli_util.rename_command(loadbalancer_cli, loadbalancer_cli.lb_root_group, loadbalancer_cli.load_balancer_protocol_group, "protocol")
cli_util.rename_command(loadbalancer_cli, loadbalancer_cli.lb_root_group, loadbalancer_cli.load_balancer_shape_group, "shape")
cli_util.rename_command(loadbalancer_cli, loadbalancer_cli.lb_root_group, loadbalancer_cli.network_security_groups_group, "nsg")
cli_util.rename_command(loadbalancer_cli, loadbalancer_cli.load_balancer_policy_group, loadbalancer_cli.list_policies, "list")
cli_util.rename_command(loadbalancer_cli, loadbalancer_cli.load_balancer_protocol_group, loadbalancer_cli.list_protocols, "list")
cli_util.rename_command(loadbalancer_cli, loadbalancer_cli.load_balancer_shape_group, loadbalancer_cli.list_shapes, "list")


@cli_util.copy_params_from_generated_command(loadbalancer_cli.create_load_balancer, params_to_exclude=['network_security_group_ids'])
@loadbalancer_cli.load_balancer_group.command(name=cli_util.override('create_load_balancer.command_name', 'create'), help=loadbalancer_cli.create_load_balancer.help)
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The array of NSG [OCIDs] to be used by this Load Balancer.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'shape-details': {'module': 'load_balancer', 'class': 'ShapeDetails'}, 'reserved-ips': {'module': 'load_balancer', 'class': 'list[ReservedIP]'}, 'listeners': {'module': 'load_balancer', 'class': 'dict(str, ListenerDetails)'}, 'hostnames': {'module': 'load_balancer', 'class': 'dict(str, HostnameDetails)'}, 'backend-sets': {'module': 'load_balancer', 'class': 'dict(str, BackendSetDetails)'}, 'network-security-group-ids': {'module': 'load_balancer', 'class': 'list[string]'}, 'nsg-ids': {'module': 'load_balancer', 'class': 'list[string]'}, 'subnet-ids': {'module': 'load_balancer', 'class': 'list[string]'}, 'certificates': {'module': 'load_balancer', 'class': 'dict(str, CertificateDetails)'}, 'ssl-cipher-suites': {'module': 'load_balancer', 'class': 'dict(str, SSLCipherSuiteDetails)'}, 'path-route-sets': {'module': 'load_balancer', 'class': 'dict(str, PathRouteSetDetails)'}, 'freeform-tags': {'module': 'load_balancer', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'load_balancer', 'class': 'dict(str, dict(str, object))'}, 'rule-sets': {'module': 'load_balancer', 'class': 'dict(str, RuleSetDetails)'}})
@cli_util.wrap_exceptions
def create_load_balancer_extended(ctx, **kwargs):
    if 'nsg_ids' in kwargs:
        kwargs['network_security_group_ids'] = kwargs['nsg_ids']
        kwargs.pop('nsg_ids')
    ctx.invoke(loadbalancer_cli.create_load_balancer, **kwargs)


@cli_util.copy_params_from_generated_command(loadbalancer_cli.update_network_security_groups, params_to_exclude=['network_security_group_ids'])
@loadbalancer_cli.network_security_groups_group.command(name=cli_util.override('update_network_security_groups.command_name', 'update'), help=loadbalancer_cli.update_network_security_groups.help)
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The array of NSG [OCIDs] to be used by this Load Balancer.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'nsg-ids': {'module': 'load_balancer', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_network_security_groups_extended(ctx, **kwargs):
    if 'nsg_ids' in kwargs:
        kwargs['network_security_group_ids'] = kwargs['nsg_ids']
        kwargs.pop('nsg_ids')
    ctx.invoke(loadbalancer_cli.update_network_security_groups, **kwargs)


def process_ssl_configuration_kwargs_for_listener(kwargs):
    ssl_configuration = {}
    if kwargs['ssl_certificate_name'] is not None and kwargs['ssl_certificate_ids'] is not None:
        raise click.UsageError('--ssl-certificate-name and --ssl-certificate-ids option cannot be provided together')

    if kwargs['ssl_certificate_name']:
        ssl_configuration['certificateName'] = kwargs['ssl_certificate_name']

    if kwargs['ssl_certificate_ids']:
        ssl_configuration['certificateIds'] = cli_util.parse_json_parameter("ssl_certificate_ids", kwargs['ssl_certificate_ids'])

    if kwargs['ssl_verify_depth'] is not None:
        if kwargs['ssl_certificate_name'] is None and kwargs['ssl_certificate_ids'] is None:
            raise click.UsageError('--ssl-certificate-name or --ssl-certificate-ids option must be provided if --ssl-verify-depth is provided')

        ssl_configuration['verifyDepth'] = kwargs['ssl_verify_depth']

    if kwargs['ssl_verify_peer_certificate'] is not None:
        if kwargs['ssl_certificate_name'] is None and kwargs['ssl_certificate_ids'] is None:
            raise click.UsageError('--ssl-certificate-name or --ssl-certificate-ids option must be provided if --ssl-verify-peer-certificate is provided')

        ssl_configuration['verifyPeerCertificate'] = kwargs['ssl_verify_peer_certificate']

    if kwargs['protocols'] is not None:
        if kwargs['ssl_certificate_name'] is None and kwargs['ssl_certificate_ids'] is None:
            raise click.UsageError('--ssl-certificate-name or --ssl-certificate-ids option must be provided if --protocols is provided')

        ssl_configuration['protocols'] = cli_util.parse_json_parameter("protocols", kwargs['protocols'])

    if kwargs['cipher_suite_name'] is not None:
        if kwargs['ssl_certificate_name'] is None and kwargs['ssl_certificate_ids'] is None:
            raise click.UsageError('--ssl-certificate-name or --ssl-certificate-ids option must be provided if --cipher-suite-name is provided')

        ssl_configuration['cipherSuiteName'] = kwargs['cipher_suite_name']

    if kwargs['server_order_preference'] is not None:
        if kwargs['ssl_certificate_name'] is None and kwargs['ssl_certificate_ids'] is None:
            raise click.UsageError('--ssl-certificate-name or --ssl-certificate-ids option must be provided if --server-order-preference is provided')

        ssl_configuration['serverOrderPreference'] = kwargs['server_order_preference']

    if kwargs['ssl_session_resumption'] is not None:
        if kwargs['ssl_certificate_name'] is None and kwargs['ssl_certificate_ids'] is None:
            raise click.UsageError('--ssl-certificate-name or --ssl-certificate-ids option must be provided if --ssl-session-resumption is provided')

        ssl_configuration['hasSessionResumption'] = kwargs['ssl_session_resumption']

    if len(ssl_configuration) > 0:
        kwargs['ssl_configuration'] = json.dumps(ssl_configuration)

    # remove kwargs that create_backend_set wont recognize
    kwargs.pop('ssl_certificate_name')
    kwargs.pop('ssl_certificate_ids')
    kwargs.pop('ssl_verify_depth')
    kwargs.pop('ssl_verify_peer_certificate')
    kwargs.pop('protocols')
    kwargs.pop('cipher_suite_name')
    kwargs.pop('server_order_preference')
    kwargs.pop('ssl_session_resumption')


def process_ssl_configuration_kwargs(kwargs):
    ssl_configuration = {}
    if kwargs['ssl_certificate_name'] is not None and kwargs['ssl_certificate_ids'] is not None:
        raise click.UsageError('--ssl-certificate-name and --ssl-certificate-ids option cannot be provided together')

    if kwargs['ssl_certificate_name']:
        ssl_configuration['certificateName'] = kwargs['ssl_certificate_name']

    if kwargs['ssl_certificate_ids']:
        ssl_configuration['certificateIds'] = cli_util.parse_json_parameter("ssl_certificate_ids", kwargs['ssl_certificate_ids'])

    if kwargs['ssl_verify_depth'] is not None:
        if kwargs['ssl_certificate_name'] is None and kwargs['ssl_certificate_ids'] is None:
            raise click.UsageError('--ssl-certificate-name or --ssl-certificate-ids option must be provided if --ssl-verify-depth is provided')

        ssl_configuration['verifyDepth'] = kwargs['ssl_verify_depth']

    if kwargs['ssl_verify_peer_certificate'] is not None:
        if kwargs['ssl_certificate_name'] is None and kwargs['ssl_certificate_ids'] is None:
            raise click.UsageError('--ssl-certificate-name or --ssl-certificate-ids option must be provided if --ssl-verify-peer-certificate is provided')

        ssl_configuration['verifyPeerCertificate'] = kwargs['ssl_verify_peer_certificate']

    if kwargs['protocols'] is not None:
        if kwargs['ssl_certificate_name'] is None and kwargs['ssl_certificate_ids'] is None:
            raise click.UsageError('--ssl-certificate-name or --ssl-certificate-ids option must be provided if --protocols is provided')

        ssl_configuration['protocols'] = cli_util.parse_json_parameter("protocols", kwargs['protocols'])

    if kwargs['cipher_suite_name'] is not None:
        if kwargs['ssl_certificate_name'] is None and kwargs['ssl_certificate_ids'] is None:
            raise click.UsageError('--ssl-certificate-name or --ssl-certificate-ids option must be provided if --cipher-suite-name is provided')

        ssl_configuration['cipherSuiteName'] = kwargs['cipher_suite_name']

    if kwargs['server_order_preference'] is not None:
        if kwargs['ssl_certificate_name'] is None and kwargs['ssl_certificate_ids'] is None:
            raise click.UsageError('--ssl-certificate-name or --ssl-certificate-ids option must be provided if --server-order-preference is provided')

        ssl_configuration['serverOrderPreference'] = kwargs['server_order_preference']

    if len(ssl_configuration) > 0:
        kwargs['ssl_configuration'] = json.dumps(ssl_configuration)

    # remove kwargs that create_backend_set wont recognize
    kwargs.pop('ssl_certificate_name')
    kwargs.pop('ssl_certificate_ids')
    kwargs.pop('ssl_verify_depth')
    kwargs.pop('ssl_verify_peer_certificate')
    kwargs.pop('protocols')
    kwargs.pop('cipher_suite_name')
    kwargs.pop('server_order_preference')


def process_connection_configuration_kwargs(kwargs):
    connection_configuration = {}
    if 'connection_configuration_idle_timeout' in kwargs and kwargs['connection_configuration_idle_timeout'] is not None:
        connection_configuration['idleTimeout'] = kwargs['connection_configuration_idle_timeout']
    if 'connection_configuration_backend_tcp_proxy_protocol_version' in kwargs and kwargs['connection_configuration_backend_tcp_proxy_protocol_version'] is not None:
        connection_configuration['backendTcpProxyProtocolVersion'] = kwargs['connection_configuration_backend_tcp_proxy_protocol_version']

    if len(connection_configuration):
        kwargs['connection_configuration'] = json.dumps(connection_configuration)

    kwargs.pop('connection_configuration_idle_timeout', None)
    kwargs.pop('connection_configuration_backend_tcp_proxy_protocol_version', None)


def process_session_persistence_configuration_kwargs(kwargs):
    session_persistence_configuration = {}
    if kwargs['session_persistence_cookie_name'] is not None:
        session_persistence_configuration['cookieName'] = kwargs['session_persistence_cookie_name']

    if kwargs['session_persistence_disable_fallback'] is not None:
        session_persistence_configuration['disableFallback'] = kwargs['session_persistence_disable_fallback']

    if len(session_persistence_configuration) > 0:
        kwargs['session_persistence_configuration'] = json.dumps(session_persistence_configuration)

    kwargs.pop('session_persistence_cookie_name')
    kwargs.pop('session_persistence_disable_fallback')


def process_health_checker_kwargs(kwargs):
    healthChecker = {}
    healthChecker['protocol'] = kwargs['health_checker_protocol']

    if kwargs['health_checker_interval_in_ms'] is not None:
        healthChecker['intervalInMillis'] = kwargs['health_checker_interval_in_ms']

    if kwargs['health_checker_port'] is not None:
        healthChecker['port'] = kwargs['health_checker_port']

    if kwargs['health_checker_response_body_regex'] is not None:
        healthChecker['responseBodyRegex'] = kwargs['health_checker_response_body_regex']

    if kwargs['health_checker_retries'] is not None:
        healthChecker['retries'] = kwargs['health_checker_retries']

    if kwargs['health_checker_return_code'] is not None:
        healthChecker['returnCode'] = kwargs['health_checker_return_code']

    if kwargs['health_checker_timeout_in_ms'] is not None:
        healthChecker['timeoutInMillis'] = kwargs['health_checker_timeout_in_ms']

    if kwargs['health_checker_url_path'] is not None:
        healthChecker['urlPath'] = kwargs['health_checker_url_path']

    kwargs['health_checker'] = json.dumps(healthChecker)

    # remove kwargs that create_backend_set wont recognize
    kwargs.pop('health_checker_interval_in_ms')
    kwargs.pop('health_checker_port')
    kwargs.pop('health_checker_protocol')
    kwargs.pop('health_checker_response_body_regex')
    kwargs.pop('health_checker_retries')
    kwargs.pop('health_checker_return_code')
    kwargs.pop('health_checker_timeout_in_ms')
    kwargs.pop('health_checker_url_path')


@cli_util.copy_params_from_generated_command(loadbalancer_cli.create_certificate, params_to_exclude=['ca_certificate', 'private_key', 'public_certificate'])
@loadbalancer_cli.certificate_group.command(name=cli_util.override('create_certificate.command_name', 'create'), help="""Creates an asynchronous request to add an SSL certificate.""")
@cli_util.option('--ca-certificate-file', type=click.File('r'), help="""The Certificate Authority certificate, or any interim certificate, that you received from your SSL certificate provider.

Example:

    -----BEGIN CERTIFICATE-----     MIIEczCCA1ugAwIBAgIBADANBgkqhkiG9w0BAQQFAD..AkGA1UEBhMCR0Ix     EzARBgNVBAgTClNvbWUtU3RhdGUxFDASBgNVBAoTC0..0EgTHRkMTcwNQYD     VQQLEy5DbGFzcyAxIFB1YmxpYyBQcmltYXJ5IENlcn..XRpb24gQXV0aG9y     aXR5MRQwEgYDVQQDEwtCZXN0IENBIEx0ZDAeFw0wMD..TUwMTZaFw0wMTAy     ...     -----END CERTIFICATE-----""")
@cli_util.option('--private-key-file', type=click.File('r'), help="""The SSL private key for your certificate, in PEM format.

Example:

    -----BEGIN RSA PRIVATE KEY-----     jO1O1v2ftXMsawM90tnXwc6xhOAT1gDBC9S8DKeca..JZNUgYYwNS0dP2UK     tmyN+XqVcAKw4HqVmChXy5b5msu8eIq3uc2NqNVtR..2ksSLukP8pxXcHyb     +sEwvM4uf8qbnHAqwnOnP9+KV9vds6BaH1eRA4CHz..n+NVZlzBsTxTlS16     /Umr7wJzVrMqK5sDiSu4WuaaBdqMGfL5hLsTjcBFD..Da2iyQmSKuVD4lIZ     ...     -----END RSA PRIVATE KEY-----""")
@cli_util.option('--public-certificate-file', type=click.File('r'), help="""The public certificate, in PEM format, that you received from your SSL certificate provider.

Example:

    -----BEGIN CERTIFICATE-----     MIIC2jCCAkMCAg38MA0GCSqGSIb3DQEBBQUAMIGbMQswCQYDVQQGEwJKUDEOMAwG     A1UECBMFVG9reW8xEDAOBgNVBAcTB0NodW8ta3UxETAPBgNVBAoTCEZyYW5rNERE     MRgwFgYDVQQLEw9XZWJDZXJ0IFN1cHBvcnQxGDAWBgNVBAMTD0ZyYW5rNEREIFdl     YiBDQTEjMCEGCSqGSIb3DQEJARYUc3VwcG9ydEBmcmFuazRkZC5jb20wHhcNMTIw     ...     -----END CERTIFICATE-----""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def create_certificate(ctx, **kwargs):
    ca_certificate_file = kwargs.get('ca_certificate_file')
    if ca_certificate_file:
        kwargs['ca_certificate'] = ca_certificate_file.read()

    private_key_file = kwargs.get('private_key_file')
    if private_key_file:
        kwargs['private_key'] = private_key_file.read()

    public_certificate_file = kwargs.get('public_certificate_file')
    if public_certificate_file:
        kwargs['public_certificate'] = public_certificate_file.read()

    kwargs.pop('ca_certificate_file')
    kwargs.pop('private_key_file')
    kwargs.pop('public_certificate_file')

    ctx.invoke(loadbalancer_cli.create_certificate, **kwargs)


@cli_util.copy_params_from_generated_command(loadbalancer_cli.create_backend_set, params_to_exclude=['health_checker', 'ssl_configuration', 'session_persistence_configuration'])
@loadbalancer_cli.backend_set_group.command(name=cli_util.override('create_backend_set.command_name', 'create'), help="""Adds a backend set to a load balancer.""")
@cli_util.option('--health-checker-interval-in-ms', type=click.INT, help="""The interval between health checks, in milliseconds.""")
@cli_util.option('--health-checker-port', type=click.INT, help="""The backend server port against which to run the health check. If the port is not specified, the load balancer uses the port information from the Backend object.""")
@cli_util.option('--health-checker-protocol', type=click.STRING, required=True, help="""The protocol the health check must use; either HTTP or TCP.""")
@cli_util.option('--health-checker-response-body-regex', type=click.STRING, help="""A regular expression for parsing the response body from the backend server.""")
@cli_util.option('--health-checker-retries', type=click.INT, help="""The number of retries to attempt before a backend server is considered "unhealthy".""")
@cli_util.option('--health-checker-return-code', type=click.INT, help="""The status code a healthy backend server should return.""")
@cli_util.option('--health-checker-timeout-in-ms', type=click.INT, help="""The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply returns within this timeout period.""")
@cli_util.option('--health-checker-url-path', type=click.STRING, help="""The path against which to run the health check.""")
@cli_util.option('--session-persistence-cookie-name', type=click.STRING, help="""The name of the cookie used to detect a session initiated by the backend server. Use '*' to specify that any cookie set by the backend causes the session to persist.""")
@cli_util.option('--session-persistence-disable-fallback', type=click.BOOL, help="""Whether the load balancer is prevented from directing traffic from a persistent session client to a different backend server if the original server is unavailable. Defaults to false.""")
@cli_util.option('--ssl-certificate-name', type=click.STRING, help="""A friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores. Certificate bundle names cannot contain spaces. Avoid entering confidential information.""")
@cli_util.option('--ssl-certificate-ids', type=custom_types.CLI_COMPLEX_TYPE, help="""A list of OCI Certificates [OCIDs] to be used by this Load Balancer.""")
@cli_util.option('--ssl-verify-depth', type=click.INT, help="""The maximum depth for peer certificate chain verification.""")
@cli_util.option('--ssl-verify-peer-certificate', type=click.BOOL, help="""Whether the load balancer listener should verify peer certificates.""")
@cli_util.option('--protocols', type=custom_types.CLI_COMPLEX_TYPE, help="""A list of protocols to be configured for backend. It must be a list of strings.

Example: ["TLSv1.1","TLSv1.2"]""")
@cli_util.option('--cipher-suite-name', type=click.STRING, help="""Cipher suite name for backend.""")
@cli_util.option('--server-order-preference', type=click.STRING, help="""Server order preference for backend.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backends': {'module': 'load_balancer', 'class': 'list[BackendDetails]'}, 'lb-cookie-session-persistence-configuration': {'module': 'load_balancer', 'class': 'LBCookieSessionPersistenceConfigurationDetails'}, 'protocols': {'module': 'load_balancer', 'class': 'list[string]'}, 'ssl-certificate-ids': {'module': 'load_balancer', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def create_backend_set(ctx, **kwargs):
    process_health_checker_kwargs(kwargs)
    process_session_persistence_configuration_kwargs(kwargs)
    process_ssl_configuration_kwargs(kwargs)

    ctx.invoke(loadbalancer_cli.create_backend_set, **kwargs)


@cli_util.copy_params_from_generated_command(loadbalancer_cli.update_backend_set, params_to_exclude=['health_checker', 'ssl_configuration', 'session_persistence_configuration'])
@loadbalancer_cli.backend_set_group.command(name='update', help="""Updates a backend set.""")
@cli_util.option('--health-checker-interval-in-ms', type=click.INT, help="""The interval between health checks, in milliseconds.""")
@cli_util.option('--health-checker-port', type=click.INT, help="""The backend server port against which to run the health check. If the port is not specified, the load balancer uses the port information from the Backend object.""")
@cli_util.option('--health-checker-protocol', type=click.STRING, required=True, help="""The protocol the health check must use; either HTTP or TCP.""")
@cli_util.option('--health-checker-response-body-regex', type=click.STRING, help="""A regular expression for parsing the response body from the backend server.""")
@cli_util.option('--health-checker-retries', type=click.INT, help="""The number of retries to attempt before a backend server is considered "unhealthy".""")
@cli_util.option('--health-checker-return-code', type=click.INT, help="""The status code a healthy backend server should return.""")
@cli_util.option('--health-checker-timeout-in-ms', type=click.INT, help="""The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply returns within this timeout period.""")
@cli_util.option('--health-checker-url-path', type=click.STRING, help="""The path against which to run the health check.""")
@cli_util.option('--session-persistence-cookie-name', type=click.STRING, help="""The name of the cookie used to detect a session initiated by the backend server. Use '*' to specify that any cookie set by the backend causes the session to persist.""")
@cli_util.option('--session-persistence-disable-fallback', type=click.BOOL, help="""Whether the load balancer is prevented from directing traffic from a persistent session client to a different backend server if the original server is unavailable. Defaults to false.""")
@cli_util.option('--ssl-certificate-name', type=click.STRING, help="""A friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores. Certificate bundle names cannot contain spaces. Avoid entering confidential information.""")
@cli_util.option('--ssl-certificate-ids', type=custom_types.CLI_COMPLEX_TYPE, help="""A list of OCI Certificates [OCIDs] to be used by this Load Balancer.""")
@cli_util.option('--ssl-verify-depth', type=click.INT, help="""The maximum depth for peer certificate chain verification.""")
@cli_util.option('--ssl-verify-peer-certificate', type=click.BOOL, help="""Whether the load balancer listener should verify peer certificates.""")
@cli_util.option('--protocols', type=custom_types.CLI_COMPLEX_TYPE, help="""A list of protocols to be configured for backend. It must be a list of strings.

Example: ["TLSv1.1","TLSv1.2"]""")
@cli_util.option('--cipher-suite-name', type=click.STRING, help="""Cipher suite name for backend.""")
@cli_util.option('--server-order-preference', type=click.STRING, help="""Server order preference for backend.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backends': {'module': 'load_balancer', 'class': 'list[BackendDetails]'}, 'lb-cookie-session-persistence-configuration': {'module': 'load_balancer', 'class': 'LBCookieSessionPersistenceConfigurationDetails'}, 'protocols': {'module': 'load_balancer', 'class': 'list[string]'}, 'ssl-certificate-ids': {'module': 'load_balancer', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_backend_set(ctx, **kwargs):
    process_health_checker_kwargs(kwargs)
    process_session_persistence_configuration_kwargs(kwargs)
    process_ssl_configuration_kwargs(kwargs)

    ctx.invoke(loadbalancer_cli.update_backend_set, **kwargs)


@cli_util.copy_params_from_generated_command(loadbalancer_cli.create_listener, params_to_exclude=['ssl_configuration', 'connection_configuration'])
@loadbalancer_cli.listener_group.command(name='create', help="""Adds a listener to a load balancer.""")
@cli_util.option('--ssl-certificate-name', type=click.STRING, help="""A friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores. Certificate bundle names cannot contain spaces. Avoid entering confidential information.""")
@cli_util.option('--ssl-certificate-ids', type=custom_types.CLI_COMPLEX_TYPE, help="""A list of OCI Certificates [OCIDs] to be used by this Load Balancer.""")
@cli_util.option('--ssl-verify-depth', type=click.INT, help="""The maximum depth for peer certificate chain verification.""")
@cli_util.option('--ssl-verify-peer-certificate', type=click.BOOL, help="""Whether the load balancer listener should verify peer certificates.""")
@cli_util.option('--connection-configuration-backend-tcp-proxy-protocol-version', type=click.INT, help="""Connection Configuration Backend TCP Proxy Protocol Version.""")
@cli_util.option('--protocols', type=custom_types.CLI_COMPLEX_TYPE, help="""List of protocols to be configured for listener. It must be a list of strings.

Example: ["TLSv1.1","TLSv1.2"]""")
@cli_util.option('--cipher-suite-name', type=click.STRING, help="""Cipher suite name for listener.""")
@cli_util.option('--server-order-preference', type=click.STRING, help="""Server order preference for listener.""")
@cli_util.option('--connection-configuration-idle-timeout', type=click.INT, help="""The maximum idle time, in seconds, allowed between two successive receive or two successive send operations between the client and backend servers.""")
@cli_util.option('--ssl-session-resumption', type=click.BOOL, help="""Whether the load balancer listener should resume an encrypted session by reusing the cryptographic parameters of a previous TLS session, without having to perform a full handshake again.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'hostname-names': {'module': 'load_balancer', 'class': 'list[string]'}, 'ssl-configuration': {'module': 'load_balancer', 'class': 'SSLConfigurationDetails'}, 'rule-set-names': {'module': 'load_balancer', 'class': 'list[string]'}, 'protocols': {'module': 'load_balancer', 'class': 'list[string]'}, 'ssl-certificate-ids': {'module': 'load_balancer', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def create_listener(ctx, **kwargs):
    process_ssl_configuration_kwargs_for_listener(kwargs)
    process_connection_configuration_kwargs(kwargs)

    ctx.invoke(loadbalancer_cli.create_listener, **kwargs)


@cli_util.copy_params_from_generated_command(loadbalancer_cli.update_listener, params_to_exclude=['ssl_configuration', 'connection_configuration'])
@loadbalancer_cli.listener_group.command(name='update', help="""Updates a listener for a given load balancer.""")
@cli_util.option('--ssl-certificate-name', type=click.STRING, help="""A friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores. Certificate bundle names cannot contain spaces. Avoid entering confidential information.""")
@cli_util.option('--ssl-certificate-ids', type=custom_types.CLI_COMPLEX_TYPE, help="""A list of OCI Certificates [OCIDs] to be used by this Load Balancer.""")
@cli_util.option('--ssl-verify-depth', type=click.INT, help="""The maximum depth for peer certificate chain verification.""")
@cli_util.option('--ssl-verify-peer-certificate', type=click.BOOL, help="""Whether the load balancer listener should verify peer certificates.""")
@cli_util.option('--connection-configuration-backend-tcp-proxy-protocol-version', type=click.INT, help="""Connection Configuration Backend TCP Proxy Protocol Version.""")
@cli_util.option('--protocols', type=custom_types.CLI_COMPLEX_TYPE, help="""List of protocols to be configured for listener. It must be a list of strings.

Example: ["TLSv1.1","TLSv1.2"]""")
@cli_util.option('--cipher-suite-name', type=click.STRING, help="""Cipher suite name for listener.""")
@cli_util.option('--server-order-preference', type=click.STRING, help="""Server order preference for listener.""")
@cli_util.option('--connection-configuration-idle-timeout', type=click.INT, help="""The maximum idle time, in seconds, allowed between two successive receive or two successive send operations between the client and backend servers.""")
@cli_util.option('--ssl-session-resumption', type=click.BOOL, help="""Whether the load balancer listener should resume an encrypted session by reusing the cryptographic parameters of a previous TLS session, without having to perform a full handshake again.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'hostname-names': {'module': 'load_balancer', 'class': 'list[string]'}, 'ssl-configuration': {'module': 'load_balancer', 'class': 'SSLConfigurationDetails'}, 'rule-set-names': {'module': 'load_balancer', 'class': 'list[string]'}, 'protocols': {'module': 'load_balancer', 'class': 'list[string]'}, 'ssl-certificate-ids': {'module': 'load_balancer', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_listener(ctx, **kwargs):
    process_ssl_configuration_kwargs_for_listener(kwargs)
    process_connection_configuration_kwargs(kwargs)

    ctx.invoke(loadbalancer_cli.update_listener, **kwargs)
