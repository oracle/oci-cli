# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
import json
import six  # noqa: F401
from . import cli_util
from . import json_skeleton_utils
from . import retry_utils  # noqa: F401
from . import custom_types  # noqa: F401
from .generated import loadbalancer_cli


loadbalancer_cli.load_balancer_group.commands.pop('update')


def process_ssl_configuration_kwargs(kwargs):
    ssl_configuration = {}
    if kwargs['ssl_certificate_name']:
        ssl_configuration['certificateName'] = kwargs['ssl_certificate_name']

    if kwargs['ssl_verify_depth'] is not None:
        if kwargs['ssl_certificate_name'] is None:
            raise click.UsageError('--ssl-certificate-name option must be provided if --ssl-verify-depth is provided')

        ssl_configuration['verifyDepth'] = kwargs['ssl_verify_depth']

    if kwargs['ssl_verify_peer_certificate'] is not None:
        if kwargs['ssl_certificate_name'] is None:
            raise click.UsageError('--ssl-certificate-name option must be provided if --ssl-verify-peer-certificate is provided')

        ssl_configuration['verifyPeerCertificate'] = kwargs['ssl_verify_peer_certificate']

    if len(ssl_configuration) > 0:
        kwargs['ssl_configuration'] = json.dumps(ssl_configuration)

    # remove kwargs that create_backend_set wont recognize
    kwargs.pop('ssl_certificate_name')
    kwargs.pop('ssl_verify_depth')
    kwargs.pop('ssl_verify_peer_certificate')


def process_connection_configuration_kwargs(kwargs):
    if 'connection_configuration_idle_timeout' in kwargs and kwargs['connection_configuration_idle_timeout'] is not None:
        connection_configuration = {'idleTimeout': kwargs['connection_configuration_idle_timeout']}
        kwargs['connection_configuration'] = json.dumps(connection_configuration)

    kwargs.pop('connection_configuration_idle_timeout', None)


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
@click.option('--ca-certificate-file', type=click.File('r'), callback=cli_util.handle_optional_param, help="""The Certificate Authority certificate, or any interim certificate, that you received from your SSL certificate provider.

Example:

    -----BEGIN CERTIFICATE-----     MIIEczCCA1ugAwIBAgIBADANBgkqhkiG9w0BAQQFAD..AkGA1UEBhMCR0Ix     EzARBgNVBAgTClNvbWUtU3RhdGUxFDASBgNVBAoTC0..0EgTHRkMTcwNQYD     VQQLEy5DbGFzcyAxIFB1YmxpYyBQcmltYXJ5IENlcn..XRpb24gQXV0aG9y     aXR5MRQwEgYDVQQDEwtCZXN0IENBIEx0ZDAeFw0wMD..TUwMTZaFw0wMTAy     ...     -----END CERTIFICATE-----""")
@click.option('--private-key-file', type=click.File('r'), callback=cli_util.handle_optional_param, help="""The SSL private key for your certificate, in PEM format.

Example:

    -----BEGIN RSA PRIVATE KEY-----     jO1O1v2ftXMsawM90tnXwc6xhOAT1gDBC9S8DKeca..JZNUgYYwNS0dP2UK     tmyN+XqVcAKw4HqVmChXy5b5msu8eIq3uc2NqNVtR..2ksSLukP8pxXcHyb     +sEwvM4uf8qbnHAqwnOnP9+KV9vds6BaH1eRA4CHz..n+NVZlzBsTxTlS16     /Umr7wJzVrMqK5sDiSu4WuaaBdqMGfL5hLsTjcBFD..Da2iyQmSKuVD4lIZ     ...     -----END RSA PRIVATE KEY-----""")
@click.option('--public-certificate-file', type=click.File('r'), callback=cli_util.handle_optional_param, help="""The public certificate, in PEM format, that you received from your SSL certificate provider.

Example:

    -----BEGIN CERTIFICATE-----     MIIC2jCCAkMCAg38MA0GCSqGSIb3DQEBBQUAMIGbMQswCQYDVQQGEwJKUDEOMAwG     A1UECBMFVG9reW8xEDAOBgNVBAcTB0NodW8ta3UxETAPBgNVBAoTCEZyYW5rNERE     MRgwFgYDVQQLEw9XZWJDZXJ0IFN1cHBvcnQxGDAWBgNVBAMTD0ZyYW5rNEREIFdl     YiBDQTEjMCEGCSqGSIb3DQEJARYUc3VwcG9ydEBmcmFuazRkZC5jb20wHhcNMTIw     ...     -----END CERTIFICATE-----""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
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
@click.option('--health-checker-interval-in-ms', type=click.INT, callback=cli_util.handle_optional_param, help="""The interval between health checks, in milliseconds.""")
@click.option('--health-checker-port', type=click.INT, callback=cli_util.handle_optional_param, help="""The backend server port against which to run the health check. If the port is not specified, the load balancer uses the port information from the Backend object.""")
@click.option('--health-checker-protocol', type=click.STRING, callback=cli_util.handle_required_param, help="""The protocol the health check must use; either HTTP or TCP.  [required]""")
@click.option('--health-checker-response-body-regex', type=click.STRING, callback=cli_util.handle_optional_param, help="""A regular expression for parsing the response body from the backend server.""")
@click.option('--health-checker-retries', type=click.INT, callback=cli_util.handle_optional_param, help="""The number of retries to attempt before a backend server is considered "unhealthy".""")
@click.option('--health-checker-return-code', type=click.INT, callback=cli_util.handle_optional_param, help="""The status code a healthy backend server should return.""")
@click.option('--health-checker-timeout-in-ms', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply returns within this timeout period.""")
@click.option('--health-checker-url-path', type=click.STRING, callback=cli_util.handle_optional_param, help="""The path against which to run the health check.""")
@click.option('--session-persistence-cookie-name', type=click.STRING, callback=cli_util.handle_optional_param, help="""The name of the cookie used to detect a session initiated by the backend server. Use '*' to specify that any cookie set by the backend causes the session to persist.""")
@click.option('--session-persistence-disable-fallback', type=click.BOOL, callback=cli_util.handle_optional_param, help="""Whether the load balancer is prevented from directing traffic from a persistent session client to a different backend server if the original server is unavailable. Defaults to false.""")
@click.option('--ssl-certificate-name', type=click.STRING, callback=cli_util.handle_optional_param, help="""A friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores. Certificate bundle names cannot contain spaces. Avoid entering confidential information.""")
@click.option('--ssl-verify-depth', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum depth for peer certificate chain verification.""")
@click.option('--ssl-verify-peer-certificate', type=click.BOOL, callback=cli_util.handle_optional_param, help="""Whether the load balancer listener should verify peer certificates.""")
@json_skeleton_utils.get_cli_json_input_option({'backends': {'module': 'load_balancer', 'class': 'list[BackendDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backends': {'module': 'load_balancer', 'class': 'list[BackendDetails]'}})
@cli_util.wrap_exceptions
def create_backend_set(ctx, **kwargs):
    process_health_checker_kwargs(kwargs)
    process_session_persistence_configuration_kwargs(kwargs)
    process_ssl_configuration_kwargs(kwargs)

    ctx.invoke(loadbalancer_cli.create_backend_set, **kwargs)


@cli_util.copy_params_from_generated_command(loadbalancer_cli.update_backend_set, params_to_exclude=['health_checker', 'ssl_configuration', 'session_persistence_configuration'])
@loadbalancer_cli.backend_set_group.command(name='update', help="""Updates a backend set.""")
@click.option('--health-checker-interval-in-ms', type=click.INT, callback=cli_util.handle_optional_param, help="""The interval between health checks, in milliseconds.""")
@click.option('--health-checker-port', type=click.INT, callback=cli_util.handle_optional_param, help="""The backend server port against which to run the health check. If the port is not specified, the load balancer uses the port information from the Backend object.""")
@click.option('--health-checker-protocol', type=click.STRING, callback=cli_util.handle_required_param, help="""The protocol the health check must use; either HTTP or TCP.  [required]""")
@click.option('--health-checker-response-body-regex', type=click.STRING, callback=cli_util.handle_optional_param, help="""A regular expression for parsing the response body from the backend server.""")
@click.option('--health-checker-retries', type=click.INT, callback=cli_util.handle_optional_param, help="""The number of retries to attempt before a backend server is considered "unhealthy".""")
@click.option('--health-checker-return-code', type=click.INT, callback=cli_util.handle_optional_param, help="""The status code a healthy backend server should return.""")
@click.option('--health-checker-timeout-in-ms', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply returns within this timeout period.""")
@click.option('--health-checker-url-path', type=click.STRING, callback=cli_util.handle_optional_param, help="""The path against which to run the health check.""")
@click.option('--session-persistence-cookie-name', type=click.STRING, callback=cli_util.handle_optional_param, help="""The name of the cookie used to detect a session initiated by the backend server. Use '*' to specify that any cookie set by the backend causes the session to persist.""")
@click.option('--session-persistence-disable-fallback', type=click.BOOL, callback=cli_util.handle_optional_param, help="""Whether the load balancer is prevented from directing traffic from a persistent session client to a different backend server if the original server is unavailable. Defaults to false.""")
@click.option('--ssl-certificate-name', type=click.STRING, callback=cli_util.handle_optional_param, help="""A friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores. Certificate bundle names cannot contain spaces. Avoid entering confidential information.""")
@click.option('--ssl-verify-depth', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum depth for peer certificate chain verification.""")
@click.option('--ssl-verify-peer-certificate', type=click.BOOL, callback=cli_util.handle_optional_param, help="""Whether the load balancer listener should verify peer certificates.""")
@json_skeleton_utils.get_cli_json_input_option({'backends': {'module': 'load_balancer', 'class': 'list[BackendDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backends': {'module': 'load_balancer', 'class': 'list[BackendDetails]'}})
@cli_util.wrap_exceptions
def update_backend_set(ctx, **kwargs):
    process_health_checker_kwargs(kwargs)
    process_session_persistence_configuration_kwargs(kwargs)
    process_ssl_configuration_kwargs(kwargs)

    ctx.invoke(loadbalancer_cli.update_backend_set, **kwargs)


@cli_util.copy_params_from_generated_command(loadbalancer_cli.create_listener, params_to_exclude=['ssl_configuration', 'connection_configuration'])
@loadbalancer_cli.listener_group.command(name='create', help="""Adds a listener to a load balancer.""")
@click.option('--ssl-certificate-name', type=click.STRING, callback=cli_util.handle_optional_param, help="""A friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores. Certificate bundle names cannot contain spaces. Avoid entering confidential information.""")
@click.option('--ssl-verify-depth', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum depth for peer certificate chain verification.""")
@click.option('--ssl-verify-peer-certificate', type=click.BOOL, callback=cli_util.handle_optional_param, help="""Whether the load balancer listener should verify peer certificates.""")
@click.option('--connection-configuration-idle-timeout', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum idle time, in seconds, allowed between two successive receive or two successive send operations between the client and backend servers.""")
@json_skeleton_utils.get_cli_json_input_option({'ssl-configuration': {'module': 'load_balancer', 'class': 'SSLConfigurationDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'ssl-configuration': {'module': 'load_balancer', 'class': 'SSLConfigurationDetails'}})
@cli_util.wrap_exceptions
def create_listener(ctx, **kwargs):
    process_ssl_configuration_kwargs(kwargs)
    process_connection_configuration_kwargs(kwargs)

    ctx.invoke(loadbalancer_cli.create_listener, **kwargs)


@cli_util.copy_params_from_generated_command(loadbalancer_cli.update_listener, params_to_exclude=['ssl_configuration', 'connection_configuration'])
@loadbalancer_cli.listener_group.command(name='update', help="""Updates a listener for a given load balancer.""")
@click.option('--ssl-certificate-name', type=click.STRING, callback=cli_util.handle_optional_param, help="""A friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores. Certificate bundle names cannot contain spaces. Avoid entering confidential information.""")
@click.option('--ssl-verify-depth', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum depth for peer certificate chain verification.""")
@click.option('--ssl-verify-peer-certificate', type=click.BOOL, callback=cli_util.handle_optional_param, help="""Whether the load balancer listener should verify peer certificates.""")
@click.option('--connection-configuration-idle-timeout', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum idle time, in seconds, allowed between two successive receive or two successive send operations between the client and backend servers.""")
@json_skeleton_utils.get_cli_json_input_option({'ssl-configuration': {'module': 'load_balancer', 'class': 'SSLConfigurationDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'ssl-configuration': {'module': 'load_balancer', 'class': 'SSLConfigurationDetails'}})
@cli_util.wrap_exceptions
def update_listener(ctx, **kwargs):
    process_ssl_configuration_kwargs(kwargs)
    process_connection_configuration_kwargs(kwargs)

    ctx.invoke(loadbalancer_cli.update_listener, **kwargs)
