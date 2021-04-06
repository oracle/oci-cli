# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click

from oci_cli import cli_util, json_skeleton_utils
from oci_cli.aliasing import CommandGroupWithAlias
from services.apigateway.src.oci_cli_api_gateway.generated import apigateway_cli
from services.apigateway.src.oci_cli_apigateway.generated import api_gateway_service_cli


# #### Api resource #### #

# new groups rather than rename for future modifications (adding commands manualy)

# Changes from this:
# oci api-gateway api-specification get-api-deployment-specification --api-id, -? | -h | --help
# oci api-gateway api-validations get --api-id, -? | -h | --help
# oci api-gateway api get-api-content --api-id, --file, -? | -h | --help

# to this
# oci api-gateway api deployment-specification get --api-id, -? | -h | --help
# oci api-gateway api validations get --api-id, -? | -h | --help
# oci api-gateway api content get --api-id, --file, -? | -h | --help


@apigateway_cli.api_group.command('validations', cls=CommandGroupWithAlias,
                                  help=apigateway_cli.api_validations_group.help)
@cli_util.help_option_group
def validations_group():
    pass


api_gateway_service_cli.api_gateway_service_group.commands.pop(apigateway_cli.api_validations_group.name)
cli_util.rename_command(apigateway_cli, validations_group, apigateway_cli.get_api_validations, "get")


@apigateway_cli.api_group.command('content', cls=CommandGroupWithAlias, help="""The raw API content""")
@cli_util.help_option_group
def content_group():
    pass


api_gateway_service_cli.api_gateway_service_group.commands['api'].commands.pop(
    apigateway_cli.api_gateway_root_group.commands['api'].commands['get-api-content'].name)
cli_util.rename_command(apigateway_cli, content_group, apigateway_cli.get_api_content, "get")


@apigateway_cli.api_group.command('deployment-specification', cls=CommandGroupWithAlias,
                                  help="""API Deployment specification generated from API""")
@cli_util.help_option_group
def deployment_specification_group():
    pass


api_gateway_service_cli.api_gateway_service_group.commands.pop(apigateway_cli.api_specification_group.name)
cli_util.rename_command(apigateway_cli, deployment_specification_group, apigateway_cli.get_api_deployment_specification,
                        "get")

# Changes from
# oci api-gateway sdk-language-type-summary list-sdk-language-types
# to
# oci api-gateway sdk-language-type list

cli_util.rename_command(apigateway_cli, api_gateway_service_cli.api_gateway_service_group,
                        api_gateway_service_cli.api_gateway_service_group.commands['sdk-language-type-summary'],
                        "sdk-language-type")
cli_util.rename_command(apigateway_cli, apigateway_cli.sdk_language_type_summary_group,
                        apigateway_cli.list_sdk_language_types, "list")

# Certificates  #

key_mapping = {
    'private_key_file': 'private_key',
    'certificate_file': 'certificate',
    'intermediate_certificates_file': 'intermediate_certificates',
}


@cli_util.copy_params_from_generated_command(
    apigateway_cli.create_certificate,
    params_to_exclude=list(key_mapping.values())
)
@apigateway_cli.certificate_group.command(
    name=cli_util.override('certificate.command_name', 'create'),
    help=apigateway_cli.create_certificate.help
)
@cli_util.option('--private-key-file', type=click.File('r'),
                 help="""Location of the file containing the private key
                associated with the certificate in pem format.""",
                 required=True
                 )
@cli_util.option('--certificate-file', type=click.File('r'),
                 help="""
                 Location of the file containing the leaf certificate
                 in pem format.""",
                 required=True)
@cli_util.option('--intermediate-certificates-file', type=click.File('r'),
                 help="""Location of file containing the intermediate
                 certificate data associated with the certificate in pem
                 format.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'freeform-tags': {
            'module': 'apigateway',
            'class': 'dict(str, string)'
        },
        'defined-tags': {
            'module': 'apigateway',
            'class': 'dict(str, dict(str, object))'
        }
    }, output_type={'module': 'apigateway', 'class': 'Certificate'}
)
@cli_util.wrap_exceptions
def create_certificate(ctx, **kwargs):
    for key in key_mapping.keys():
        if kwargs.get(key):
            kwargs[key_mapping[key]] = kwargs.get(key).read()
        del kwargs[key]
    ctx.invoke(apigateway_cli.create_certificate, **kwargs)
