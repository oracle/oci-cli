# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.certificates_management.src.oci_cli_certificates_management.generated import certificatesmanagement_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci certificates-management association-summary list-associations -> oci certificates-management association-summary list
cli_util.rename_command(certificatesmanagement_cli, certificatesmanagement_cli.association_summary_group, certificatesmanagement_cli.list_associations, "list")


# oci certificates-management ca-bundle-summary list-ca-bundles -> oci certificates-management ca-bundle-summary list
cli_util.rename_command(certificatesmanagement_cli, certificatesmanagement_cli.ca_bundle_summary_group, certificatesmanagement_cli.list_ca_bundles, "list")


# oci certificates-management certificate-authority-summary list-certificate-authorities -> oci certificates-management certificate-authority-summary list
cli_util.rename_command(certificatesmanagement_cli, certificatesmanagement_cli.certificate_authority_summary_group, certificatesmanagement_cli.list_certificate_authorities, "list")


# oci certificates-management certificate-authority-version-summary list-certificate-authority-versions -> oci certificates-management certificate-authority-version-summary list
cli_util.rename_command(certificatesmanagement_cli, certificatesmanagement_cli.certificate_authority_version_summary_group, certificatesmanagement_cli.list_certificate_authority_versions, "list")


# oci certificates-management certificate-summary list-certificates -> oci certificates-management certificate-summary list
cli_util.rename_command(certificatesmanagement_cli, certificatesmanagement_cli.certificate_summary_group, certificatesmanagement_cli.list_certificates, "list")


# oci certificates-management certificate-version-summary list-certificate-versions -> oci certificates-management certificate-version-summary list
cli_util.rename_command(certificatesmanagement_cli, certificatesmanagement_cli.certificate_version_summary_group, certificatesmanagement_cli.list_certificate_versions, "list")


# oci certificates-management certificate cancel-certificate-deletion -> oci certificates-management certificate cancel-deletion
cli_util.rename_command(certificatesmanagement_cli, certificatesmanagement_cli.certificate_group, certificatesmanagement_cli.cancel_certificate_deletion, "cancel-deletion")


# oci certificates-management certificate schedule-certificate-deletion -> oci certificates-management certificate schedule-deletion
cli_util.rename_command(certificatesmanagement_cli, certificatesmanagement_cli.certificate_group, certificatesmanagement_cli.schedule_certificate_deletion, "schedule-deletion")


# oci certificates-management certificate-authority cancel-certificate-authority-deletion -> oci certificates-management certificate-authority cancel-deletion
cli_util.rename_command(certificatesmanagement_cli, certificatesmanagement_cli.certificate_authority_group, certificatesmanagement_cli.cancel_certificate_authority_deletion, "cancel-deletion")


# oci certificates-management certificate-authority schedule-certificate-authority-deletion -> oci certificates-management certificate-authority schedule-deletion
cli_util.rename_command(certificatesmanagement_cli, certificatesmanagement_cli.certificate_authority_group, certificatesmanagement_cli.schedule_certificate_authority_deletion, "schedule-deletion")


# oci certificates-management certificate-authority-version cancel-certificate-authority-version-deletion -> oci certificates-management certificate-authority-version cancel-deletion
cli_util.rename_command(certificatesmanagement_cli, certificatesmanagement_cli.certificate_authority_version_group, certificatesmanagement_cli.cancel_certificate_authority_version_deletion, "cancel-deletion")


# oci certificates-management certificate-authority-version schedule-certificate-authority-version-deletion -> oci certificates-management certificate-authority-version schedule-deletion
cli_util.rename_command(certificatesmanagement_cli, certificatesmanagement_cli.certificate_authority_version_group, certificatesmanagement_cli.schedule_certificate_authority_version_deletion, "schedule-deletion")


# oci certificates-management certificate-version cancel-certificate-version-deletion -> oci certificates-management certificate-version cancel-deletion
cli_util.rename_command(certificatesmanagement_cli, certificatesmanagement_cli.certificate_version_group, certificatesmanagement_cli.cancel_certificate_version_deletion, "cancel-deletion")


# oci certificates-management certificate-version schedule-certificate-version-deletion -> oci certificates-management certificate-version schedule-deletion
cli_util.rename_command(certificatesmanagement_cli, certificatesmanagement_cli.certificate_version_group, certificatesmanagement_cli.schedule_certificate_version_deletion, "schedule-deletion")


# oci certificates-management certificate create-certificate-create-certificate-by-importing-config-details -> oci certificates-management certificate create-by-importing-config
cli_util.rename_command(certificatesmanagement_cli, certificatesmanagement_cli.certificate_group, certificatesmanagement_cli.create_certificate_create_certificate_by_importing_config_details, "create-by-importing-config")


# oci certificates-management certificate create-certificate-create-certificate-issued-by-internal-ca-config-details -> oci certificates-management certificate create-certificate-issued-by-internal-ca
cli_util.rename_command(certificatesmanagement_cli, certificatesmanagement_cli.certificate_group, certificatesmanagement_cli.create_certificate_create_certificate_issued_by_internal_ca_config_details, "create-certificate-issued-by-internal-ca")


# oci certificates-management certificate create-certificate-create-certificate-managed-externally-issued-by-internal-ca-config-details -> oci certificates-management certificate create-certificate-managed-externally-issued-by-internal-ca
cli_util.rename_command(certificatesmanagement_cli, certificatesmanagement_cli.certificate_group, certificatesmanagement_cli.create_certificate_create_certificate_managed_externally_issued_by_internal_ca_config_details, "create-certificate-managed-externally-issued-by-internal-ca")


# oci certificates-management certificate update-certificate-update-certificate-by-importing-config-details -> oci certificates-management certificate update-certificate-by-importing-config-details
cli_util.rename_command(certificatesmanagement_cli, certificatesmanagement_cli.certificate_group, certificatesmanagement_cli.update_certificate_update_certificate_by_importing_config_details, "update-certificate-by-importing-config-details")


# oci certificates-management certificate update-certificate-update-certificate-issued-by-internal-ca-config-details -> oci certificates-management certificate update-certificate-managed-internally
cli_util.rename_command(certificatesmanagement_cli, certificatesmanagement_cli.certificate_group, certificatesmanagement_cli.update_certificate_update_certificate_issued_by_internal_ca_config_details, "update-certificate-managed-internally")


# oci certificates-management certificate update-certificate-update-certificate-managed-externally-issued-by-internal-ca-config-details -> oci certificates-management certificate update-certificate-managed-externally
cli_util.rename_command(certificatesmanagement_cli, certificatesmanagement_cli.certificate_group, certificatesmanagement_cli.update_certificate_update_certificate_managed_externally_issued_by_internal_ca_config_details, "update-certificate-managed-externally")


# oci certificates-management certificate-authority create-certificate-authority-create-root-ca-by-generating-internally-config-details -> oci certificates-management certificate-authority create-root-ca-by-generating-config-details
cli_util.rename_command(certificatesmanagement_cli, certificatesmanagement_cli.certificate_authority_group, certificatesmanagement_cli.create_certificate_authority_create_root_ca_by_generating_internally_config_details, "create-root-ca-by-generating-config-details")


# oci certificates-management certificate-authority create-certificate-authority-create-subordinate-ca-issued-by-internal-ca-config-details -> oci certificates-management certificate-authority create-subordinate-ca-issued-by-internal-ca
cli_util.rename_command(certificatesmanagement_cli, certificatesmanagement_cli.certificate_authority_group, certificatesmanagement_cli.create_certificate_authority_create_subordinate_ca_issued_by_internal_ca_config_details, "create-subordinate-ca-issued-by-internal-ca")


# oci certificates-management certificate-authority update-certificate-authority-update-root-ca-by-generating-internally-config-details -> oci certificates-management certificate-authority update-root-ca-by-generating-config-details
cli_util.rename_command(certificatesmanagement_cli, certificatesmanagement_cli.certificate_authority_group, certificatesmanagement_cli.update_certificate_authority_update_root_ca_by_generating_internally_config_details, "update-root-ca-by-generating-config-details")


# oci certificates-management certificate-authority update-certificate-authority-update-subordinate-ca-issued-by-internal-ca-config-details -> oci certificates-management certificate-authority update-subordinate-ca-issued-by-internal-ca
cli_util.rename_command(certificatesmanagement_cli, certificatesmanagement_cli.certificate_authority_group, certificatesmanagement_cli.update_certificate_authority_update_subordinate_ca_issued_by_internal_ca_config_details, "update-subordinate-ca-issued-by-internal-ca")


# Remove create from oci certificates-management certificate
certificatesmanagement_cli.certificate_group.commands.pop(certificatesmanagement_cli.create_certificate.name)


# Remove create from oci certificates-management certificate-authority
certificatesmanagement_cli.certificate_authority_group.commands.pop(certificatesmanagement_cli.create_certificate_authority.name)


# Remove update from oci certificates-management certificate-authority
certificatesmanagement_cli.certificate_authority_group.commands.pop(certificatesmanagement_cli.update_certificate_authority.name)


# Move commands under 'oci certificates-management association-summary' -> 'oci certificates-management association'
certificatesmanagement_cli.certs_mgmt_root_group.commands.pop(certificatesmanagement_cli.association_summary_group.name)
certificatesmanagement_cli.association_group.add_command(certificatesmanagement_cli.list_associations)


# Move commands under 'oci certificates-management ca-bundle-summary' -> 'oci certificates-management ca-bundle'
certificatesmanagement_cli.certs_mgmt_root_group.commands.pop(certificatesmanagement_cli.ca_bundle_summary_group.name)
certificatesmanagement_cli.ca_bundle_group.add_command(certificatesmanagement_cli.list_ca_bundles)


# Move commands under 'oci certificates-management certificate-authority-summary' -> 'oci certificates-management certificate-authority'
certificatesmanagement_cli.certs_mgmt_root_group.commands.pop(certificatesmanagement_cli.certificate_authority_summary_group.name)
certificatesmanagement_cli.certificate_authority_group.add_command(certificatesmanagement_cli.list_certificate_authorities)


# Move commands under 'oci certificates-management certificate-authority-version-summary' -> 'oci certificates-management certificate-authority-version'
certificatesmanagement_cli.certs_mgmt_root_group.commands.pop(certificatesmanagement_cli.certificate_authority_version_summary_group.name)
certificatesmanagement_cli.certificate_authority_version_group.add_command(certificatesmanagement_cli.list_certificate_authority_versions)


# Move commands under 'oci certificates-management certificate-summary' -> 'oci certificates-management certificate'
certificatesmanagement_cli.certs_mgmt_root_group.commands.pop(certificatesmanagement_cli.certificate_summary_group.name)
certificatesmanagement_cli.certificate_group.add_command(certificatesmanagement_cli.list_certificates)


# Move commands under 'oci certificates-management certificate-version-summary' -> 'oci certificates-management certificate-version'
certificatesmanagement_cli.certs_mgmt_root_group.commands.pop(certificatesmanagement_cli.certificate_version_summary_group.name)
certificatesmanagement_cli.certificate_version_group.add_command(certificatesmanagement_cli.list_certificate_versions)


@cli_util.copy_params_from_generated_command(certificatesmanagement_cli.get_certificate_version, params_to_exclude=['certificate_version_number'])
@certificatesmanagement_cli.certificate_version_group.command(name=certificatesmanagement_cli.get_certificate_version.name, help=certificatesmanagement_cli.get_certificate_version.help)
@cli_util.option('--version-number', required=True, type=click.INT, help=u"""The version number of the certificate. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'certificates_management', 'class': 'CertificateVersion'})
@cli_util.wrap_exceptions
def get_certificate_version_extended(ctx, **kwargs):
    if 'version_number' in kwargs:
        kwargs['certificate_version_number'] = kwargs['version_number']
        kwargs.pop('version_number')

    ctx.invoke(certificatesmanagement_cli.get_certificate_version, **kwargs)


@cli_util.copy_params_from_generated_command(certificatesmanagement_cli.revoke_certificate_version, params_to_exclude=['certificate_version_number'])
@certificatesmanagement_cli.certificate_version_group.command(name=certificatesmanagement_cli.revoke_certificate_version.name, help=certificatesmanagement_cli.revoke_certificate_version.help)
@cli_util.option('--version-number', required=True, type=click.INT, help=u"""The version number of the certificate. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def revoke_certificate_version_extended(ctx, **kwargs):
    if 'version_number' in kwargs:
        kwargs['certificate_version_number'] = kwargs['version_number']
        kwargs.pop('version_number')

    ctx.invoke(certificatesmanagement_cli.revoke_certificate_version, **kwargs)


@cli_util.copy_params_from_generated_command(certificatesmanagement_cli.get_certificate_authority_version, params_to_exclude=['certificate_authority_version_number'])
@certificatesmanagement_cli.certificate_authority_version_group.command(name=certificatesmanagement_cli.get_certificate_authority_version.name, help=certificatesmanagement_cli.get_certificate_authority_version.help)
@cli_util.option('--version-number', required=True, type=click.INT, help=u"""The version number of the certificate authority (CA). [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'certificates_management', 'class': 'CertificateAuthorityVersion'})
@cli_util.wrap_exceptions
def get_certificate_authority_version_extended(ctx, **kwargs):
    if 'version_number' in kwargs:
        kwargs['certificate_authority_version_number'] = kwargs['version_number']
        kwargs.pop('version_number')

    ctx.invoke(certificatesmanagement_cli.get_certificate_authority_version, **kwargs)


@cli_util.copy_params_from_generated_command(certificatesmanagement_cli.revoke_certificate_authority_version, params_to_exclude=['certificate_authority_version_number'])
@certificatesmanagement_cli.certificate_authority_version_group.command(name=certificatesmanagement_cli.revoke_certificate_authority_version.name, help=certificatesmanagement_cli.revoke_certificate_authority_version.help)
@cli_util.option('--version-number', required=True, type=click.INT, help=u"""The version number of the certificate authority (CA). [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def revoke_certificate_authority_version_extended(ctx, **kwargs):
    if 'version_number' in kwargs:
        kwargs['certificate_authority_version_number'] = kwargs['version_number']
        kwargs.pop('version_number')

    ctx.invoke(certificatesmanagement_cli.revoke_certificate_authority_version, **kwargs)


@cli_util.copy_params_from_generated_command(certificatesmanagement_cli.cancel_certificate_authority_version_deletion, params_to_exclude=['certificate_authority_version_number'])
@certificatesmanagement_cli.certificate_authority_version_group.command(name=certificatesmanagement_cli.cancel_certificate_authority_version_deletion.name, help=certificatesmanagement_cli.cancel_certificate_authority_version_deletion.help)
@cli_util.option('--version-number', required=True, type=click.INT, help=u"""The version number of the certificate authority (CA). [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_certificate_authority_version_deletion_extended(ctx, **kwargs):
    if 'version_number' in kwargs:
        kwargs['certificate_authority_version_number'] = kwargs['version_number']
        kwargs.pop('version_number')

    ctx.invoke(certificatesmanagement_cli.cancel_certificate_authority_version_deletion, **kwargs)


@cli_util.copy_params_from_generated_command(certificatesmanagement_cli.schedule_certificate_authority_version_deletion, params_to_exclude=['certificate_authority_version_number'])
@certificatesmanagement_cli.certificate_authority_version_group.command(name=certificatesmanagement_cli.schedule_certificate_authority_version_deletion.name, help=certificatesmanagement_cli.schedule_certificate_authority_version_deletion.help)
@cli_util.option('--version-number', required=True, type=click.INT, help=u"""The version number of the certificate authority (CA). [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def schedule_certificate_authority_version_deletion_extended(ctx, **kwargs):
    if 'version_number' in kwargs:
        kwargs['certificate_authority_version_number'] = kwargs['version_number']
        kwargs.pop('version_number')

    ctx.invoke(certificatesmanagement_cli.schedule_certificate_authority_version_deletion, **kwargs)


@cli_util.copy_params_from_generated_command(certificatesmanagement_cli.cancel_certificate_version_deletion, params_to_exclude=['certificate_version_number'])
@certificatesmanagement_cli.certificate_version_group.command(name=certificatesmanagement_cli.cancel_certificate_version_deletion.name, help=certificatesmanagement_cli.cancel_certificate_version_deletion.help)
@cli_util.option('--version-number', required=True, type=click.INT, help=u"""The version number of the certificate. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_certificate_version_deletion_extended(ctx, **kwargs):
    if 'version_number' in kwargs:
        kwargs['certificate_version_number'] = kwargs['version_number']
        kwargs.pop('version_number')

    ctx.invoke(certificatesmanagement_cli.cancel_certificate_version_deletion, **kwargs)


@cli_util.copy_params_from_generated_command(certificatesmanagement_cli.schedule_certificate_version_deletion, params_to_exclude=['certificate_version_number'])
@certificatesmanagement_cli.certificate_version_group.command(name=certificatesmanagement_cli.schedule_certificate_version_deletion.name, help=certificatesmanagement_cli.schedule_certificate_version_deletion.help)
@cli_util.option('--version-number', required=True, type=click.INT, help=u"""The version number of the certificate. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def schedule_certificate_version_deletion_extended(ctx, **kwargs):
    if 'version_number' in kwargs:
        kwargs['certificate_version_number'] = kwargs['version_number']
        kwargs.pop('version_number')

    ctx.invoke(certificatesmanagement_cli.schedule_certificate_version_deletion, **kwargs)


@cli_util.copy_params_from_generated_command(certificatesmanagement_cli.create_certificate_create_certificate_by_importing_config_details, params_to_exclude=['certificate_config_cert_chain_pem', 'certificate_config_certificate_pem', 'certificate_config_private_key_pem', 'certificate_config_private_key_pem_passphrase', 'certificate_config_version_name'])
@certificatesmanagement_cli.certificate_group.command(name=certificatesmanagement_cli.create_certificate_create_certificate_by_importing_config_details.name, help=certificatesmanagement_cli.create_certificate_create_certificate_by_importing_config_details.help)
@cli_util.option('--cert-chain-pem', required=True, help=u"""The certificate chain (in PEM format) for the imported certificate. [required]""")
@cli_util.option('--certificate-pem', required=True, help=u"""The certificate (in PEM format) for the imported certificate. [required]""")
@cli_util.option('--private-key-pem', required=True, help=u"""The private key (in PEM format) for the imported certificate. [required]""")
@cli_util.option('--private-key-pem-passphrase', help=u"""An optional passphrase for the private key.""")
@cli_util.option('--version-name', help=u"""A name for the certificate. When the value is not null, a name is unique across versions of a given certificate.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'certificate-rules': {'module': 'certificates_management', 'class': 'list[CertificateRule]'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'certificates_management', 'class': 'Certificate'})
@cli_util.wrap_exceptions
def create_certificate_create_certificate_by_importing_config_details_extended(ctx, **kwargs):
    if 'cert_chain_pem' in kwargs:
        kwargs['certificate_config_cert_chain_pem'] = kwargs['cert_chain_pem']
        kwargs.pop('cert_chain_pem')

    if 'certificate_pem' in kwargs:
        kwargs['certificate_config_certificate_pem'] = kwargs['certificate_pem']
        kwargs.pop('certificate_pem')

    if 'private_key_pem' in kwargs:
        kwargs['certificate_config_private_key_pem'] = kwargs['private_key_pem']
        kwargs.pop('private_key_pem')

    if 'private_key_pem_passphrase' in kwargs:
        kwargs['certificate_config_private_key_pem_passphrase'] = kwargs['private_key_pem_passphrase']
        kwargs.pop('private_key_pem_passphrase')

    if 'version_name' in kwargs:
        kwargs['certificate_config_version_name'] = kwargs['version_name']
        kwargs.pop('version_name')

    ctx.invoke(certificatesmanagement_cli.create_certificate_create_certificate_by_importing_config_details, **kwargs)


@cli_util.copy_params_from_generated_command(certificatesmanagement_cli.create_certificate_create_certificate_issued_by_internal_ca_config_details, params_to_exclude=['certificate_config_certificate_profile_type', 'certificate_config_issuer_certificate_authority_id', 'certificate_config_subject', 'certificate_config_key_algorithm', 'certificate_config_signature_algorithm', 'certificate_config_subject_alternative_names', 'certificate_config_validity', 'certificate_config_version_name'])
@certificatesmanagement_cli.certificate_group.command(name=certificatesmanagement_cli.create_certificate_create_certificate_issued_by_internal_ca_config_details.name, help=certificatesmanagement_cli.create_certificate_create_certificate_issued_by_internal_ca_config_details.help)
@cli_util.option('--certificate-profile-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["TLS_SERVER_OR_CLIENT", "TLS_SERVER", "TLS_CLIENT", "TLS_CODE_SIGN"]), help=u"""The name of the profile used to create the certificate, which depends on the type of certificate you need. [required]""")
@cli_util.option('--issuer-certificate-authority-id', required=True, help=u"""The OCID of the private CA. [required]""")
@cli_util.option('--subject', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.
 [required]""")
@cli_util.option('--key-algorithm', type=custom_types.CliCaseInsensitiveChoice(["RSA2048", "RSA4096", "ECDSA_P256", "ECDSA_P384"]), help=u"""The algorithm to use to create key pairs.""")
@cli_util.option('--signature-algorithm', type=custom_types.CliCaseInsensitiveChoice(["SHA256_WITH_RSA", "SHA384_WITH_RSA", "SHA512_WITH_RSA", "SHA256_WITH_ECDSA", "SHA384_WITH_ECDSA", "SHA512_WITH_ECDSA"]), help=u"""The algorithm to use to sign the public key certificate.""")
@cli_util.option('--subject-alternative-names', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of subject alternative names.

This option is a JSON list with items of type CertificateSubjectAlternativeName.  For documentation on CertificateSubjectAlternativeName please see our API reference: https://docs.cloud.oracle.com/api/#/en/certificatesmanagement/20210224/datatypes/CertificateSubjectAlternativeName.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--validity', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--version-name', help=u"""A name for the certificate. When the value is not null, a name is unique across versions of a given certificate.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'certificate-rules': {'module': 'certificates_management', 'class': 'list[CertificateRule]'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'validity': {'module': 'certificates_management', 'class': 'Validity'}, 'subject': {'module': 'certificates_management', 'class': 'CertificateSubject'}, 'subject-alternative-names': {'module': 'certificates_management', 'class': 'list[CertificateSubjectAlternativeName]'}}, output_type={'module': 'certificates_management', 'class': 'Certificate'})
@cli_util.wrap_exceptions
def create_certificate_create_certificate_issued_by_internal_ca_config_details_extended(ctx, **kwargs):
    if 'certificate_profile_type' in kwargs:
        kwargs['certificate_config_certificate_profile_type'] = kwargs['certificate_profile_type']
        kwargs.pop('certificate_profile_type')

    if 'issuer_certificate_authority_id' in kwargs:
        kwargs['certificate_config_issuer_certificate_authority_id'] = kwargs['issuer_certificate_authority_id']
        kwargs.pop('issuer_certificate_authority_id')

    if 'subject' in kwargs:
        kwargs['certificate_config_subject'] = kwargs['subject']
        kwargs.pop('subject')

    if 'key_algorithm' in kwargs:
        kwargs['certificate_config_key_algorithm'] = kwargs['key_algorithm']
        kwargs.pop('key_algorithm')

    if 'signature_algorithm' in kwargs:
        kwargs['certificate_config_signature_algorithm'] = kwargs['signature_algorithm']
        kwargs.pop('signature_algorithm')

    if 'subject_alternative_names' in kwargs:
        kwargs['certificate_config_subject_alternative_names'] = kwargs['subject_alternative_names']
        kwargs.pop('subject_alternative_names')

    if 'validity' in kwargs:
        kwargs['certificate_config_validity'] = kwargs['validity']
        kwargs.pop('validity')

    if 'version_name' in kwargs:
        kwargs['certificate_config_version_name'] = kwargs['version_name']
        kwargs.pop('version_name')

    ctx.invoke(certificatesmanagement_cli.create_certificate_create_certificate_issued_by_internal_ca_config_details, **kwargs)


@cli_util.copy_params_from_generated_command(certificatesmanagement_cli.create_certificate_create_certificate_managed_externally_issued_by_internal_ca_config_details, params_to_exclude=['certificate_config_csr_pem', 'certificate_config_issuer_certificate_authority_id', 'certificate_config_validity', 'certificate_config_version_name'])
@certificatesmanagement_cli.certificate_group.command(name=certificatesmanagement_cli.create_certificate_create_certificate_managed_externally_issued_by_internal_ca_config_details.name, help=certificatesmanagement_cli.create_certificate_create_certificate_managed_externally_issued_by_internal_ca_config_details.help)
@cli_util.option('--csr-pem', required=True, help=u"""The certificate signing request (in PEM format). [required]""")
@cli_util.option('--issuer-certificate-authority-id', required=True, help=u"""The OCID of the private CA. [required]""")
@cli_util.option('--validity', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--version-name', help=u"""A name for the certificate. When the value is not null, a name is unique across versions of a given certificate.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'certificate-rules': {'module': 'certificates_management', 'class': 'list[CertificateRule]'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'validity': {'module': 'certificates_management', 'class': 'Validity'}}, output_type={'module': 'certificates_management', 'class': 'Certificate'})
@cli_util.wrap_exceptions
def create_certificate_create_certificate_managed_externally_issued_by_internal_ca_config_details_extended(ctx, **kwargs):
    if 'csr_pem' in kwargs:
        kwargs['certificate_config_csr_pem'] = kwargs['csr_pem']
        kwargs.pop('csr_pem')

    if 'issuer_certificate_authority_id' in kwargs:
        kwargs['certificate_config_issuer_certificate_authority_id'] = kwargs['issuer_certificate_authority_id']
        kwargs.pop('issuer_certificate_authority_id')

    if 'validity' in kwargs:
        kwargs['certificate_config_validity'] = kwargs['validity']
        kwargs.pop('validity')

    if 'version_name' in kwargs:
        kwargs['certificate_config_version_name'] = kwargs['version_name']
        kwargs.pop('version_name')

    ctx.invoke(certificatesmanagement_cli.create_certificate_create_certificate_managed_externally_issued_by_internal_ca_config_details, **kwargs)


@cli_util.copy_params_from_generated_command(certificatesmanagement_cli.update_certificate_update_certificate_by_importing_config_details, params_to_exclude=['certificate_config_cert_chain_pem', 'certificate_config_certificate_pem', 'certificate_config_private_key_pem', 'certificate_config_private_key_pem_passphrase', 'certificate_config_stage', 'certificate_config_version_name', 'current_version_number'])
@certificatesmanagement_cli.certificate_group.command(name=certificatesmanagement_cli.update_certificate_update_certificate_by_importing_config_details.name, help=certificatesmanagement_cli.update_certificate_update_certificate_by_importing_config_details.help)
@cli_util.option('--cert-chain-pem', required=True, help=u"""The certificate chain (in PEM format) for the imported certificate. [required]""")
@cli_util.option('--certificate-pem', required=True, help=u"""The certificate (in PEM format) for the imported certificate. [required]""")
@cli_util.option('--private-key-pem', required=True, help=u"""The private key (in PEM format) for the imported certificate. [required]""")
@cli_util.option('--private-key-pem-passphrase', help=u"""An optional passphrase for the private key.""")
@cli_util.option('--stage', type=custom_types.CliCaseInsensitiveChoice(["CURRENT", "PENDING"]), help=u"""The rotation state of the certificate. The default is `CURRENT`, meaning that the certificate is currently in use. A certificate version that you mark as `PENDING` is staged and available for use, but you don't yet want to rotate it into current, active use. For example, you might update a certificate and mark its rotation state as `PENDING` if you haven't yet updated the certificate on the target system.""")
@cli_util.option('--version-name', help=u"""A name for the certificate version. When the value is not null, a name is unique across versions of a given certificate.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'certificate-rules': {'module': 'certificates_management', 'class': 'list[CertificateRule]'}}, output_type={'module': 'certificates_management', 'class': 'Certificate'})
@cli_util.wrap_exceptions
def update_certificate_update_certificate_by_importing_config_details_extended(ctx, **kwargs):
    if 'cert_chain_pem' in kwargs:
        kwargs['certificate_config_cert_chain_pem'] = kwargs['cert_chain_pem']
        kwargs.pop('cert_chain_pem')

    if 'certificate_pem' in kwargs:
        kwargs['certificate_config_certificate_pem'] = kwargs['certificate_pem']
        kwargs.pop('certificate_pem')

    if 'private_key_pem' in kwargs:
        kwargs['certificate_config_private_key_pem'] = kwargs['private_key_pem']
        kwargs.pop('private_key_pem')

    if 'private_key_pem_passphrase' in kwargs:
        kwargs['certificate_config_private_key_pem_passphrase'] = kwargs['private_key_pem_passphrase']
        kwargs.pop('private_key_pem_passphrase')

    if 'stage' in kwargs:
        kwargs['certificate_config_stage'] = kwargs['stage']
        kwargs.pop('stage')

    if 'version_name' in kwargs:
        kwargs['certificate_config_version_name'] = kwargs['version_name']
        kwargs.pop('version_name')

    ctx.invoke(certificatesmanagement_cli.update_certificate_update_certificate_by_importing_config_details, **kwargs)


@cli_util.copy_params_from_generated_command(certificatesmanagement_cli.update_certificate_update_certificate_issued_by_internal_ca_config_details, params_to_exclude=['certificate_config_stage', 'certificate_config_validity', 'certificate_config_version_name', 'current_version_number'])
@certificatesmanagement_cli.certificate_group.command(name=certificatesmanagement_cli.update_certificate_update_certificate_issued_by_internal_ca_config_details.name, help=certificatesmanagement_cli.update_certificate_update_certificate_issued_by_internal_ca_config_details.help)
@cli_util.option('--stage', type=custom_types.CliCaseInsensitiveChoice(["CURRENT", "PENDING"]), help=u"""The rotation state of the certificate. The default is `CURRENT`, meaning that the certificate is currently in use. A certificate version that you mark as `PENDING` is staged and available for use, but you don't yet want to rotate it into current, active use. For example, you might update a certificate and mark its rotation state as `PENDING` if you haven't yet updated the certificate on the target system.""")
@cli_util.option('--validity', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--version-name', help=u"""A name for the certificate version. When the value is not null, a name is unique across versions of a given certificate.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'certificate-rules': {'module': 'certificates_management', 'class': 'list[CertificateRule]'}, 'validity': {'module': 'certificates_management', 'class': 'Validity'}}, output_type={'module': 'certificates_management', 'class': 'Certificate'})
@cli_util.wrap_exceptions
def update_certificate_update_certificate_issued_by_internal_ca_config_details_extended(ctx, **kwargs):
    if 'stage' in kwargs:
        kwargs['certificate_config_stage'] = kwargs['stage']
        kwargs.pop('stage')

    if 'validity' in kwargs:
        kwargs['certificate_config_validity'] = kwargs['validity']
        kwargs.pop('validity')

    if 'version_name' in kwargs:
        kwargs['certificate_config_version_name'] = kwargs['version_name']
        kwargs.pop('version_name')

    ctx.invoke(certificatesmanagement_cli.update_certificate_update_certificate_issued_by_internal_ca_config_details, **kwargs)


@cli_util.copy_params_from_generated_command(certificatesmanagement_cli.update_certificate_update_certificate_managed_externally_issued_by_internal_ca_config_details, params_to_exclude=['certificate_config_csr_pem', 'certificate_config_stage', 'certificate_config_validity', 'certificate_config_version_name', 'current_version_number'])
@certificatesmanagement_cli.certificate_group.command(name=certificatesmanagement_cli.update_certificate_update_certificate_managed_externally_issued_by_internal_ca_config_details.name, help=certificatesmanagement_cli.update_certificate_update_certificate_managed_externally_issued_by_internal_ca_config_details.help)
@cli_util.option('--csr-pem', required=True, help=u"""The certificate signing request (in PEM format). [required]""")
@cli_util.option('--stage', type=custom_types.CliCaseInsensitiveChoice(["CURRENT", "PENDING"]), help=u"""The rotation state of the certificate. The default is `CURRENT`, meaning that the certificate is currently in use. A certificate version that you mark as `PENDING` is staged and available for use, but you don't yet want to rotate it into current, active use. For example, you might update a certificate and mark its rotation state as `PENDING` if you haven't yet updated the certificate on the target system.""")
@cli_util.option('--validity', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--version-name', help=u"""A name for the certificate version. When the value is not null, a name is unique across versions of a given certificate.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'certificate-rules': {'module': 'certificates_management', 'class': 'list[CertificateRule]'}, 'validity': {'module': 'certificates_management', 'class': 'Validity'}}, output_type={'module': 'certificates_management', 'class': 'Certificate'})
@cli_util.wrap_exceptions
def update_certificate_update_certificate_managed_externally_issued_by_internal_ca_config_details_extended(ctx, **kwargs):
    if 'csr_pem' in kwargs:
        kwargs['certificate_config_csr_pem'] = kwargs['csr_pem']
        kwargs.pop('csr_pem')

    if 'stage' in kwargs:
        kwargs['certificate_config_stage'] = kwargs['stage']
        kwargs.pop('stage')

    if 'validity' in kwargs:
        kwargs['certificate_config_validity'] = kwargs['validity']
        kwargs.pop('validity')

    if 'version_name' in kwargs:
        kwargs['certificate_config_version_name'] = kwargs['version_name']
        kwargs.pop('version_name')

    ctx.invoke(certificatesmanagement_cli.update_certificate_update_certificate_managed_externally_issued_by_internal_ca_config_details, **kwargs)


@cli_util.copy_params_from_generated_command(certificatesmanagement_cli.create_certificate_authority_create_root_ca_by_generating_internally_config_details, params_to_exclude=['certificate_authority_config_subject', 'certificate_authority_config_signing_algorithm', 'certificate_authority_config_validity', 'certificate_authority_config_version_name'])
@certificatesmanagement_cli.certificate_authority_group.command(name=certificatesmanagement_cli.create_certificate_authority_create_root_ca_by_generating_internally_config_details.name, help=certificatesmanagement_cli.create_certificate_authority_create_root_ca_by_generating_internally_config_details.help)
@cli_util.option('--subject', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.
 [required]""")
@cli_util.option('--signing-algorithm', type=custom_types.CliCaseInsensitiveChoice(["SHA256_WITH_RSA", "SHA384_WITH_RSA", "SHA512_WITH_RSA", "SHA256_WITH_ECDSA", "SHA384_WITH_ECDSA", "SHA512_WITH_ECDSA"]), help=u"""The algorithm used to sign public key certificates that the CA issues.""")
@cli_util.option('--validity', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--version-name', help=u"""The name of the CA version. When the value is not null, a name is unique across versions of a given CA.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'certificate-authority-rules': {'module': 'certificates_management', 'class': 'list[CertificateAuthorityRule]'}, 'certificate-revocation-list-details': {'module': 'certificates_management', 'class': 'CertificateRevocationListDetails'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'validity': {'module': 'certificates_management', 'class': 'Validity'}, 'subject': {'module': 'certificates_management', 'class': 'CertificateSubject'}}, output_type={'module': 'certificates_management', 'class': 'CertificateAuthority'})
@cli_util.wrap_exceptions
def create_certificate_authority_create_root_ca_by_generating_internally_config_details_extended(ctx, **kwargs):
    if 'subject' in kwargs:
        kwargs['certificate_authority_config_subject'] = kwargs['subject']
        kwargs.pop('subject')

    if 'signing_algorithm' in kwargs:
        kwargs['certificate_authority_config_signing_algorithm'] = kwargs['signing_algorithm']
        kwargs.pop('signing_algorithm')

    if 'validity' in kwargs:
        kwargs['certificate_authority_config_validity'] = kwargs['validity']
        kwargs.pop('validity')

    if 'version_name' in kwargs:
        kwargs['certificate_authority_config_version_name'] = kwargs['version_name']
        kwargs.pop('version_name')

    ctx.invoke(certificatesmanagement_cli.create_certificate_authority_create_root_ca_by_generating_internally_config_details, **kwargs)


@cli_util.copy_params_from_generated_command(certificatesmanagement_cli.create_certificate_authority_create_subordinate_ca_issued_by_internal_ca_config_details, params_to_exclude=['certificate_authority_config_issuer_certificate_authority_id', 'certificate_authority_config_signing_algorithm', 'certificate_authority_config_subject', 'certificate_authority_config_validity', 'certificate_authority_config_version_name'])
@certificatesmanagement_cli.certificate_authority_group.command(name=certificatesmanagement_cli.create_certificate_authority_create_subordinate_ca_issued_by_internal_ca_config_details.name, help=certificatesmanagement_cli.create_certificate_authority_create_subordinate_ca_issued_by_internal_ca_config_details.help)
@cli_util.option('--issuer-certificate-authority-id', required=True, help=u"""The OCID of the private CA. [required]""")
@cli_util.option('--signing-algorithm', type=custom_types.CliCaseInsensitiveChoice(["SHA256_WITH_RSA", "SHA384_WITH_RSA", "SHA512_WITH_RSA", "SHA256_WITH_ECDSA", "SHA384_WITH_ECDSA", "SHA512_WITH_ECDSA"]), help=u"""The algorithm used to sign public key certificates that the CA issues.""")
@cli_util.option('--subject', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.
 [required]""")
@cli_util.option('--validity', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--version-name', help=u"""The name of the CA version. When the value is not null, a name is unique across versions of a given CA.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'certificate-authority-rules': {'module': 'certificates_management', 'class': 'list[CertificateAuthorityRule]'}, 'certificate-revocation-list-details': {'module': 'certificates_management', 'class': 'CertificateRevocationListDetails'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'validity': {'module': 'certificates_management', 'class': 'Validity'}, 'subject': {'module': 'certificates_management', 'class': 'CertificateSubject'}}, output_type={'module': 'certificates_management', 'class': 'CertificateAuthority'})
@cli_util.wrap_exceptions
def create_certificate_authority_create_subordinate_ca_issued_by_internal_ca_config_details_extended(ctx, **kwargs):
    if 'issuer_certificate_authority_id' in kwargs:
        kwargs['certificate_authority_config_issuer_certificate_authority_id'] = kwargs['issuer_certificate_authority_id']
        kwargs.pop('issuer_certificate_authority_id')

    if 'signing_algorithm' in kwargs:
        kwargs['certificate_authority_config_signing_algorithm'] = kwargs['signing_algorithm']
        kwargs.pop('signing_algorithm')

    if 'subject' in kwargs:
        kwargs['certificate_authority_config_subject'] = kwargs['subject']
        kwargs.pop('subject')

    if 'validity' in kwargs:
        kwargs['certificate_authority_config_validity'] = kwargs['validity']
        kwargs.pop('validity')

    if 'version_name' in kwargs:
        kwargs['certificate_authority_config_version_name'] = kwargs['version_name']
        kwargs.pop('version_name')

    ctx.invoke(certificatesmanagement_cli.create_certificate_authority_create_subordinate_ca_issued_by_internal_ca_config_details, **kwargs)


@cli_util.copy_params_from_generated_command(certificatesmanagement_cli.update_certificate_authority_update_root_ca_by_generating_internally_config_details, params_to_exclude=['certificate_authority_config_stage', 'certificate_authority_config_validity', 'certificate_authority_config_version_name', 'current_version_number'])
@certificatesmanagement_cli.certificate_authority_group.command(name=certificatesmanagement_cli.update_certificate_authority_update_root_ca_by_generating_internally_config_details.name, help=certificatesmanagement_cli.update_certificate_authority_update_root_ca_by_generating_internally_config_details.help)
@cli_util.option('--stage', type=custom_types.CliCaseInsensitiveChoice(["CURRENT", "PENDING"]), help=u"""The rotation state of the CA. The default is `PENDING`, meaning that the CA is staged and available for use. A CA version that you mark as `CURRENT` is currently in use, but you don't yet want to rotate it into current, active use. For example, you might create or update a CA and mark its rotation state as `PENDING` if you haven't yet updated the certificate on the target system.""")
@cli_util.option('--validity', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--version-name', help=u"""The name of the CA version. When the value is not null, a name is unique across versions of a given CA.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'certificate-revocation-list-details': {'module': 'certificates_management', 'class': 'CertificateRevocationListDetails'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'certificate-authority-rules': {'module': 'certificates_management', 'class': 'list[CertificateAuthorityRule]'}, 'validity': {'module': 'certificates_management', 'class': 'Validity'}}, output_type={'module': 'certificates_management', 'class': 'CertificateAuthority'})
@cli_util.wrap_exceptions
def update_certificate_authority_update_root_ca_by_generating_internally_config_details_extended(ctx, **kwargs):
    if 'stage' in kwargs:
        kwargs['certificate_authority_config_stage'] = kwargs['stage']
        kwargs.pop('stage')

    if 'validity' in kwargs:
        kwargs['certificate_authority_config_validity'] = kwargs['validity']
        kwargs.pop('validity')

    if 'version_name' in kwargs:
        kwargs['certificate_authority_config_version_name'] = kwargs['version_name']
        kwargs.pop('version_name')

    ctx.invoke(certificatesmanagement_cli.update_certificate_authority_update_root_ca_by_generating_internally_config_details, **kwargs)


@cli_util.copy_params_from_generated_command(certificatesmanagement_cli.update_certificate_authority_update_subordinate_ca_issued_by_internal_ca_config_details, params_to_exclude=['certificate_authority_config_stage', 'certificate_authority_config_validity', 'certificate_authority_config_version_name', 'current_version_number'])
@certificatesmanagement_cli.certificate_authority_group.command(name=certificatesmanagement_cli.update_certificate_authority_update_subordinate_ca_issued_by_internal_ca_config_details.name, help=certificatesmanagement_cli.update_certificate_authority_update_subordinate_ca_issued_by_internal_ca_config_details.help)
@cli_util.option('--stage', type=custom_types.CliCaseInsensitiveChoice(["CURRENT", "PENDING"]), help=u"""The rotation state of the CA. The default is `PENDING`, meaning that the CA is staged and available for use. A CA version that you mark as `CURRENT` is currently in use, but you don't yet want to rotate it into current, active use. For example, you might create or update a CA and mark its rotation state as `PENDING` if you haven't yet updated the certificate on the target system.""")
@cli_util.option('--validity', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--version-name', help=u"""The name of the CA version. When the value is not null, a name is unique across versions of a given CA.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'certificate-revocation-list-details': {'module': 'certificates_management', 'class': 'CertificateRevocationListDetails'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'certificate-authority-rules': {'module': 'certificates_management', 'class': 'list[CertificateAuthorityRule]'}, 'validity': {'module': 'certificates_management', 'class': 'Validity'}}, output_type={'module': 'certificates_management', 'class': 'CertificateAuthority'})
@cli_util.wrap_exceptions
def update_certificate_authority_update_subordinate_ca_issued_by_internal_ca_config_details_extended(ctx, **kwargs):
    if 'stage' in kwargs:
        kwargs['certificate_authority_config_stage'] = kwargs['stage']
        kwargs.pop('stage')

    if 'validity' in kwargs:
        kwargs['certificate_authority_config_validity'] = kwargs['validity']
        kwargs.pop('validity')

    if 'version_name' in kwargs:
        kwargs['certificate_authority_config_version_name'] = kwargs['version_name']
        kwargs.pop('version_name')

    ctx.invoke(certificatesmanagement_cli.update_certificate_authority_update_subordinate_ca_issued_by_internal_ca_config_details, **kwargs)


@cli_util.copy_params_from_generated_command(certificatesmanagement_cli.update_certificate, params_to_exclude=['certificate_config'])
@certificatesmanagement_cli.certificate_group.command(name=certificatesmanagement_cli.update_certificate.name, help=certificatesmanagement_cli.update_certificate.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'certificate-config': {'module': 'certificates_management', 'class': 'UpdateCertificateConfigDetails'}, 'freeform-tags': {'module': 'certificates_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'certificates_management', 'class': 'dict(str, dict(str, object))'}, 'certificate-rules': {'module': 'certificates_management', 'class': 'list[CertificateRule]'}}, output_type={'module': 'certificates_management', 'class': 'Certificate'})
@cli_util.wrap_exceptions
def update_certificate_extended(ctx, **kwargs):

    ctx.invoke(certificatesmanagement_cli.update_certificate, **kwargs)
