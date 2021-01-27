# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click
import json

from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from services.analytics.src.oci_cli_analytics.generated import analytics_cli

#
# Customizations for:
#     oci analytics analytics-instance create
#
# --idcs-access-token replaced by --idcs-access-token-file file paramenter.
# --capacity complex type replaced by --capacity-type and --capacity-value
#


@cli_util.copy_params_from_generated_command(analytics_cli.create_analytics_instance, params_to_exclude=['capacity', 'idcs_access_token'])
@analytics_cli.analytics_instance_group.command(name='create', help=analytics_cli.create_analytics_instance.help)
@cli_util.option('--idcs-access-token-file', type=click.File('r'), help=u"""A file containing the IDCS access token identifying a stripe and service administrator user.""")
@cli_util.option('--capacity-type', required=True, help=u"""The capacity model to use.""")
@cli_util.option('--capacity-value', type=click.INT, required=True, help=u"""The capacity value selected (OLPU count, number of users, ...etc...). This parameter affects the number of CPUs, amount of memory or other resources allocated to the instance.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'network-endpoint-details': {'module': 'analytics', 'class': 'NetworkEndpointDetails'}, 'defined-tags': {'module': 'analytics', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'analytics', 'class': 'dict(str, string)'}}, output_type={'module': 'analytics', 'class': 'AnalyticsInstance'})
@cli_util.wrap_exceptions
def create_analytics_instance_extended(ctx, **kwargs):

    # "capcity" complex type.
    capacity = {}

    # Add "capacityType" parameter.
    if 'capacity_type' in kwargs and kwargs['capacity_type']:
        capacity['capacityType'] = kwargs['capacity_type']

    # Add "capacityValue" parameter.
    if 'capacity_value' in kwargs and kwargs['capacity_value']:
        capacity['capacityValue'] = kwargs['capacity_value']

    # Set "--idcs-access-token" to the content of file "--idcs-access-token-file"
    if 'idcs_access_token_file' in kwargs and kwargs['idcs_access_token_file']:
        content = [line.rstrip('\n') for line in kwargs['idcs_access_token_file']]
        kwargs['idcs_access_token'] = ''.join(content).strip()

    # Set "--capacity" complex type from the values collected above.
    kwargs['capacity'] = json.dumps(capacity)

    # Remove the extram parameters not expected on base method "create_analytics_instance".
    del kwargs['capacity_type']
    del kwargs['capacity_value']
    del kwargs['idcs_access_token_file']

    # Invoke base method "create_analytics_instance"
    ctx.invoke(analytics_cli.create_analytics_instance, **kwargs)


@cli_util.copy_params_from_generated_command(analytics_cli.create_vanity_url, params_to_exclude=['ca_certificate', 'private_key', 'public_certificate'])
@analytics_cli.analytics_instance_group.command(name=cli_util.override('analytics.create_vanity_url.command_name', 'create-vanity-url'), help=analytics_cli.create_vanity_url.help)
@cli_util.option('--private-key-file', required=True, type=click.File('r'), help=u"""PEM Private key file for HTTPS connections.""")
@cli_util.option('--public-certificate-file', required=True, type=click.File('r'), help=u"""PEM certificate file for HTTPS connections.""")
@cli_util.option('--ca-certificate-file', required=True, type=click.File('r'), help=u"""PEM CA certificate(s) file for HTTPS connections. This may include multiple PEM certificates.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'hosts': {'module': 'analytics', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def create_vanity_url_extended(ctx, **kwargs):

    # Set "--private-key" to the content of file "--private-key-file"
    private_key_file = kwargs.get('private_key_file')
    if private_key_file:
        kwargs['private_key'] = private_key_file.read()

    # Set "--public-certificate" to the content of file "--public-certificate-file"
    public_certificate_file = kwargs.get('public_certificate_file')
    if public_certificate_file:
        kwargs['public_certificate'] = public_certificate_file.read()

    # Set "--ca-certificate" to the content of file "--ca-certificate-file"
    ca_certificate_file = kwargs.get('ca_certificate_file')
    if ca_certificate_file:
        kwargs['ca_certificate'] = ca_certificate_file.read()

    # Remove the extram parameters not expected on base method "create-vanity-url".
    kwargs.pop('ca_certificate_file')
    kwargs.pop('private_key_file')
    kwargs.pop('public_certificate_file')

    # Invoke base method "create_analytics_instance"
    ctx.invoke(analytics_cli.create_vanity_url, **kwargs)


@cli_util.copy_params_from_generated_command(analytics_cli.update_vanity_url, params_to_exclude=['ca_certificate', 'private_key', 'public_certificate'])
@analytics_cli.analytics_instance_group.command(name=cli_util.override('analytics.update_vanity_url.command_name', 'update-vanity-url'), help=analytics_cli.update_vanity_url.help)
@cli_util.option('--private-key-file', required=True, type=click.File('r'), help=u"""PEM Private key file for HTTPS connections.""")
@cli_util.option('--public-certificate-file', required=True, type=click.File('r'), help=u"""PEM certificate file for HTTPS connections.""")
@cli_util.option('--ca-certificate-file', required=True, type=click.File('r'), help=u"""PEM CA certificate(s) file for HTTPS connections. This may include multiple PEM certificates.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_vanity_url_extended(ctx, **kwargs):

    # Set "--private-key" to the content of file "--private-key-file"
    private_key_file = kwargs.get('private_key_file')
    if private_key_file:
        kwargs['private_key'] = private_key_file.read()

    # Set "--public-certificate" to the content of file "--public-certificate-file"
    public_certificate_file = kwargs.get('public_certificate_file')
    if public_certificate_file:
        kwargs['public_certificate'] = public_certificate_file.read()

    # Set "--ca-certificate" to the content of file "--ca-certificate-file"
    ca_certificate_file = kwargs.get('ca_certificate_file')
    if ca_certificate_file:
        kwargs['ca_certificate'] = ca_certificate_file.read()

    # Remove the extram parameters not expected on base method "update-vanity-url".
    kwargs.pop('ca_certificate_file')
    kwargs.pop('private_key_file')
    kwargs.pop('public_certificate_file')

    # Invoke base method "create_analytics_instance"
    ctx.invoke(analytics_cli.update_vanity_url, **kwargs)


# Remove commands:
#   change-analytics-instance-network-endpoint-private-endpoint-details
#   change-analytics-instance-network-endpoint-public-endpoint-details
#   create-analytics-instance-private-endpoint-details
#   create-analytics-instance-public-endpoint-details
analytics_cli.analytics_instance_group.commands.pop(analytics_cli.change_analytics_instance_network_endpoint_private_endpoint_details.name)
analytics_cli.analytics_instance_group.commands.pop(analytics_cli.change_analytics_instance_network_endpoint_public_endpoint_details.name)
analytics_cli.analytics_instance_group.commands.pop(analytics_cli.create_analytics_instance_private_endpoint_details.name)
analytics_cli.analytics_instance_group.commands.pop(analytics_cli.create_analytics_instance_public_endpoint_details.name)

# Rename command "change-analytics-instance-network-endpoint" to "change-network-endpoint"
cli_util.rename_command(analytics_cli, analytics_cli.analytics_instance_group, analytics_cli.change_analytics_instance_network_endpoint, "change-network-endpoint")
