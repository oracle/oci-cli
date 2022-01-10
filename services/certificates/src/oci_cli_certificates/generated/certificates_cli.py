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


@cli.command(cli_util.override('certificates.certificates_root_group.command_name', 'certificates'), cls=CommandGroupWithAlias, help=cli_util.override('certificates.certificates_root_group.help', """API for retrieving certificates."""), short_help=cli_util.override('certificates.certificates_root_group.short_help', """Certificates Service Retrieval API"""))
@cli_util.help_option_group
def certificates_root_group():
    pass


@click.command(cli_util.override('certificates.certificate_bundle_version_summary_group.command_name', 'certificate-bundle-version-summary'), cls=CommandGroupWithAlias, help="""The properties of the certificate bundle. Certificate bundle version summary objects do not include the actual contents of the certificate.""")
@cli_util.help_option_group
def certificate_bundle_version_summary_group():
    pass


@click.command(cli_util.override('certificates.certificate_authority_bundle_group.command_name', 'certificate-authority-bundle'), cls=CommandGroupWithAlias, help="""The contents of the certificate, properties of the certificate (and certificate version), and user-provided contextual metadata for the certificate.""")
@cli_util.help_option_group
def certificate_authority_bundle_group():
    pass


@click.command(cli_util.override('certificates.ca_bundle_group.command_name', 'ca-bundle'), cls=CommandGroupWithAlias, help="""The contents of the CA bundle (root and intermediate certificates), properties of the CA bundle, and user-provided contextual metadata for the CA bundle.""")
@cli_util.help_option_group
def ca_bundle_group():
    pass


@click.command(cli_util.override('certificates.certificate_authority_bundle_version_summary_group.command_name', 'certificate-authority-bundle-version-summary'), cls=CommandGroupWithAlias, help="""The properties of a version of a bundle for a certificate authority (CA). Certificate authority bundle version summary objects do not include the actual contents of the certificate.""")
@cli_util.help_option_group
def certificate_authority_bundle_version_summary_group():
    pass


@click.command(cli_util.override('certificates.certificate_bundle_group.command_name', 'certificate-bundle'), cls=CommandGroupWithAlias, help="""The contents of the certificate, properties of the certificate (and certificate version), and user-provided contextual metadata for the certificate.""")
@cli_util.help_option_group
def certificate_bundle_group():
    pass


certificates_root_group.add_command(certificate_bundle_version_summary_group)
certificates_root_group.add_command(certificate_authority_bundle_group)
certificates_root_group.add_command(ca_bundle_group)
certificates_root_group.add_command(certificate_authority_bundle_version_summary_group)
certificates_root_group.add_command(certificate_bundle_group)


@ca_bundle_group.command(name=cli_util.override('certificates.get_ca_bundle.command_name', 'get'), help=u"""Gets a ca-bundle bundle. \n[Command Reference](getCaBundle)""")
@cli_util.option('--ca-bundle-id', required=True, help=u"""The OCID of the CA bundle.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'certificates', 'class': 'CaBundle'})
@cli_util.wrap_exceptions
def get_ca_bundle(ctx, from_json, ca_bundle_id):

    if isinstance(ca_bundle_id, six.string_types) and len(ca_bundle_id.strip()) == 0:
        raise click.UsageError('Parameter --ca-bundle-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('certificates', 'certificates', ctx)
    result = client.get_ca_bundle(
        ca_bundle_id=ca_bundle_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@certificate_authority_bundle_group.command(name=cli_util.override('certificates.get_certificate_authority_bundle.command_name', 'get'), help=u"""Gets a certificate authority bundle that matches either the specified `stage`, `name`, or `versionNumber` parameter. If none of these parameters are provided, the bundle for the certificate authority version marked as `CURRENT` will be returned. \n[Command Reference](getCertificateAuthorityBundle)""")
@cli_util.option('--certificate-authority-id', required=True, help=u"""The OCID of the certificate authority (CA).""")
@cli_util.option('--version-number', type=click.INT, help=u"""The version number of the certificate authority (CA).""")
@cli_util.option('--certificate-authority-version-name', help=u"""The name of the certificate authority (CA). (This might be referred to as the name of the CA version, as every CA consists of at least one version.) Names are unique across versions of a given CA.""")
@cli_util.option('--stage', type=custom_types.CliCaseInsensitiveChoice(["CURRENT", "PENDING", "LATEST", "PREVIOUS", "DEPRECATED"]), help=u"""The rotation state of the certificate version.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'certificates', 'class': 'CertificateAuthorityBundle'})
@cli_util.wrap_exceptions
def get_certificate_authority_bundle(ctx, from_json, certificate_authority_id, version_number, certificate_authority_version_name, stage):

    if isinstance(certificate_authority_id, six.string_types) and len(certificate_authority_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-authority-id cannot be whitespace or empty string')

    kwargs = {}
    if version_number is not None:
        kwargs['version_number'] = version_number
    if certificate_authority_version_name is not None:
        kwargs['certificate_authority_version_name'] = certificate_authority_version_name
    if stage is not None:
        kwargs['stage'] = stage
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('certificates', 'certificates', ctx)
    result = client.get_certificate_authority_bundle(
        certificate_authority_id=certificate_authority_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@certificate_bundle_group.command(name=cli_util.override('certificates.get_certificate_bundle.command_name', 'get'), help=u"""Gets a certificate bundle that matches either the specified `stage`, `versionName`, or `versionNumber` parameter. If none of these parameters are provided, the bundle for the certificate version marked as `CURRENT` will be returned.

By default, the private key is not included in the query result, and a CertificateBundlePublicOnly is returned. If the private key is needed, use the CertificateBundleTypeQueryParam parameter to get a CertificateBundleWithPrivateKey response. \n[Command Reference](getCertificateBundle)""")
@cli_util.option('--certificate-id', required=True, help=u"""The OCID of the certificate.""")
@cli_util.option('--version-number', type=click.INT, help=u"""The version number of the certificate. The default value is 0, which means that this query parameter is ignored.""")
@cli_util.option('--certificate-version-name', help=u"""The name of the certificate. (This might be referred to as the name of the certificate version, as every certificate consists of at least one version.) Names are unique across versions of a given certificate.""")
@cli_util.option('--stage', type=custom_types.CliCaseInsensitiveChoice(["CURRENT", "PENDING", "LATEST", "PREVIOUS", "DEPRECATED"]), help=u"""The rotation state of the certificate version.""")
@cli_util.option('--certificate-bundle-type', type=custom_types.CliCaseInsensitiveChoice(["CERTIFICATE_CONTENT_PUBLIC_ONLY", "CERTIFICATE_CONTENT_WITH_PRIVATE_KEY"]), help=u"""The type of certificate bundle. By default, the private key fields are not returned. When querying for certificate bundles, to return results with certificate contents, the private key in PEM format, and the private key passphrase, specify the value of this parameter as `CERTIFICATE_CONTENT_WITH_PRIVATE_KEY`.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'certificates', 'class': 'CertificateBundle'})
@cli_util.wrap_exceptions
def get_certificate_bundle(ctx, from_json, certificate_id, version_number, certificate_version_name, stage, certificate_bundle_type):

    if isinstance(certificate_id, six.string_types) and len(certificate_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-id cannot be whitespace or empty string')

    kwargs = {}
    if version_number is not None:
        kwargs['version_number'] = version_number
    if certificate_version_name is not None:
        kwargs['certificate_version_name'] = certificate_version_name
    if stage is not None:
        kwargs['stage'] = stage
    if certificate_bundle_type is not None:
        kwargs['certificate_bundle_type'] = certificate_bundle_type
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('certificates', 'certificates', ctx)
    result = client.get_certificate_bundle(
        certificate_id=certificate_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@certificate_authority_bundle_version_summary_group.command(name=cli_util.override('certificates.list_certificate_authority_bundle_versions.command_name', 'list-certificate-authority-bundle-versions'), help=u"""Lists all certificate authority bundle versions for the specified certificate authority. \n[Command Reference](listCertificateAuthorityBundleVersions)""")
@cli_util.option('--certificate-authority-id', required=True, help=u"""The OCID of the certificate authority (CA).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["VERSION_NUMBER"]), help=u"""The field to sort by. You can specify only one sort order. The default order for `VERSION_NUMBER` is ascending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'certificates', 'class': 'CertificateAuthorityBundleVersionCollection'})
@cli_util.wrap_exceptions
def list_certificate_authority_bundle_versions(ctx, from_json, all_pages, certificate_authority_id, sort_by, sort_order):

    if isinstance(certificate_authority_id, six.string_types) and len(certificate_authority_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-authority-id cannot be whitespace or empty string')

    kwargs = {}
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('certificates', 'certificates', ctx)
    result = client.list_certificate_authority_bundle_versions(
        certificate_authority_id=certificate_authority_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@certificate_bundle_version_summary_group.command(name=cli_util.override('certificates.list_certificate_bundle_versions.command_name', 'list-certificate-bundle-versions'), help=u"""Lists all certificate bundle versions for the specified certificate. \n[Command Reference](listCertificateBundleVersions)""")
@cli_util.option('--certificate-id', required=True, help=u"""The OCID of the certificate.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["VERSION_NUMBER"]), help=u"""The field to sort by. You can specify only one sort order. The default order for `VERSION_NUMBER` is ascending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'certificates', 'class': 'CertificateBundleVersionCollection'})
@cli_util.wrap_exceptions
def list_certificate_bundle_versions(ctx, from_json, all_pages, certificate_id, sort_by, sort_order):

    if isinstance(certificate_id, six.string_types) and len(certificate_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-id cannot be whitespace or empty string')

    kwargs = {}
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('certificates', 'certificates', ctx)
    result = client.list_certificate_bundle_versions(
        certificate_id=certificate_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)
