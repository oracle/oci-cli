# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.certificates.src.oci_cli_certificates.generated import certificates_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci certificates certificate-authority-bundle-version-summary list-certificate-authority-bundle-versions -> oci certificates certificate-authority-bundle-version-summary list
cli_util.rename_command(certificates_cli, certificates_cli.certificate_authority_bundle_version_summary_group, certificates_cli.list_certificate_authority_bundle_versions, "list")


# oci certificates certificate-bundle-version-summary list-certificate-bundle-versions -> oci certificates certificate-bundle-version-summary list
cli_util.rename_command(certificates_cli, certificates_cli.certificate_bundle_version_summary_group, certificates_cli.list_certificate_bundle_versions, "list")


# oci certificates certificate-authority-bundle-version-summary -> oci certificates certificate-authority-bundle-version
cli_util.rename_command(certificates_cli, certificates_cli.certificates_root_group, certificates_cli.certificate_authority_bundle_version_summary_group, "certificate-authority-bundle-version")


# oci certificates certificate-bundle-version-summary -> oci certificates certificate-bundle-version
cli_util.rename_command(certificates_cli, certificates_cli.certificates_root_group, certificates_cli.certificate_bundle_version_summary_group, "certificate-bundle-version")


@cli_util.copy_params_from_generated_command(certificates_cli.get_certificate_authority_bundle, params_to_exclude=['certificate_authority_version_name'])
@certificates_cli.certificate_authority_bundle_group.command(name=certificates_cli.get_certificate_authority_bundle.name, help=certificates_cli.get_certificate_authority_bundle.help)
@cli_util.option('--version-name', help=u"""The name of the certificate authority (CA). (This might be referred to as the name of the CA version, as every CA consists of at least one version.) Names are unique across versions of a given CA.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'certificates', 'class': 'CertificateAuthorityBundle'})
@cli_util.wrap_exceptions
def get_certificate_authority_bundle_extended(ctx, **kwargs):
    if 'version_name' in kwargs:
        kwargs['certificate_authority_version_name'] = kwargs['version_name']
        kwargs.pop('version_name')

    ctx.invoke(certificates_cli.get_certificate_authority_bundle, **kwargs)


@cli_util.copy_params_from_generated_command(certificates_cli.get_certificate_bundle, params_to_exclude=['certificate_bundle_type', 'certificate_version_name'])
@certificates_cli.certificate_bundle_group.command(name=certificates_cli.get_certificate_bundle.name, help=certificates_cli.get_certificate_bundle.help)
@cli_util.option('--bundle-type', type=custom_types.CliCaseInsensitiveChoice(["CERTIFICATE_CONTENT_PUBLIC_ONLY", "CERTIFICATE_CONTENT_WITH_PRIVATE_KEY"]), help=u"""The type of certificate bundle. By default, the private key fields are not returned. When querying for certificate bundles, to return results with certificate contents, the private key in PEM format, and the private key passphrase, specify the value of this parameter as `CERTIFICATE_CONTENT_WITH_PRIVATE_KEY`.""")
@cli_util.option('--version-name', help=u"""The name of the certificate. (This might be referred to as the name of the certificate version, as every certificate consists of at least one version.) Names are unique across versions of a given certificate.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'certificates', 'class': 'CertificateBundle'})
@cli_util.wrap_exceptions
def get_certificate_bundle_extended(ctx, **kwargs):
    if 'bundle_type' in kwargs:
        kwargs['certificate_bundle_type'] = kwargs['bundle_type']
        kwargs.pop('bundle_type')

    if 'version_name' in kwargs:
        kwargs['certificate_version_name'] = kwargs['version_name']
        kwargs.pop('version_name')

    ctx.invoke(certificates_cli.get_certificate_bundle, **kwargs)
