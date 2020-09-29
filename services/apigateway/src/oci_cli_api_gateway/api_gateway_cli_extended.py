# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click

from oci_cli import cli_util, json_skeleton_utils
from services.apigateway.src.oci_cli_api_gateway.generated import apigateway_cli

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
