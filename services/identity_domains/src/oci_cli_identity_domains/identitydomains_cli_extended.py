# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click
from services.identity_domains.src.oci_cli_identity_domains.generated import identitydomains_cli
from oci_cli import json_skeleton_utils  # noqa: F401
from oci_cli import cli_util
from oci_cli import custom_types  # noqa: F401


cli_util.SERVICES_REQUIRING_ENDPOINTS.append('identity_domains')


@cli_util.copy_params_from_generated_command(identitydomains_cli.create_user, params_to_exclude=['urnietfparamsscimschemasextensionenterprise2_0_user', 'urnietfparamsscimschemasoracleidcsextension_oci_tags', 'urnietfparamsscimschemasoracleidcsextensionadaptive_user', 'urnietfparamsscimschemasoracleidcsextensioncapabilities_user', 'urnietfparamsscimschemasoracleidcsextensiondb_credentials_user', 'urnietfparamsscimschemasoracleidcsextensiondb_user_user', 'urnietfparamsscimschemasoracleidcsextensionkerberos_user_user', 'urnietfparamsscimschemasoracleidcsextensionmfa_user', 'urnietfparamsscimschemasoracleidcsextensionpassword_state_user', 'urnietfparamsscimschemasoracleidcsextensionpasswordless_user', 'urnietfparamsscimschemasoracleidcsextensionposix_user', 'urnietfparamsscimschemasoracleidcsextensionsecurity_questions_user', 'urnietfparamsscimschemasoracleidcsextensionself_change_user', 'urnietfparamsscimschemasoracleidcsextensionself_registration_user', 'urnietfparamsscimschemasoracleidcsextensionsff_user', 'urnietfparamsscimschemasoracleidcsextensionsocial_account_user', 'urnietfparamsscimschemasoracleidcsextensionterms_of_use_user', 'urnietfparamsscimschemasoracleidcsextensionuser_credentials_user', 'urnietfparamsscimschemasoracleidcsextensionuser_state_user', 'urnietfparamsscimschemasoracleidcsextensionuser_user'])
@identitydomains_cli.user_group.command(name=identitydomains_cli.create_user.name, help=identitydomains_cli.create_user.help)
@cli_util.option('--ext-enterprise-20-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-oci-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-adaptive-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-capabilities-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-db-credentials-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-db-user-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-kerberos-user-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-mfa-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-password-state-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-passwordless-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-posix-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-security-questions-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-self-change-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-self-registration-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-sff-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-social-account-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-terms-of-use-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-user-credentials-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-user-state-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-user-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'schemas': {'module': 'identity_domains', 'class': 'list[string]'}, 'meta': {'module': 'identity_domains', 'class': 'Meta'}, 'idcs-created-by': {'module': 'identity_domains', 'class': 'IdcsCreatedBy'}, 'idcs-last-modified-by': {'module': 'identity_domains', 'class': 'IdcsLastModifiedBy'}, 'tags': {'module': 'identity_domains', 'class': 'list[Tags]'}, 'name': {'module': 'identity_domains', 'class': 'UserName'}, 'emails': {'module': 'identity_domains', 'class': 'list[UserEmails]'}, 'phone-numbers': {'module': 'identity_domains', 'class': 'list[UserPhoneNumbers]'}, 'ims': {'module': 'identity_domains', 'class': 'list[UserIms]'}, 'photos': {'module': 'identity_domains', 'class': 'list[UserPhotos]'}, 'addresses': {'module': 'identity_domains', 'class': 'list[Addresses]'}, 'groups': {'module': 'identity_domains', 'class': 'list[UserGroups]'}, 'entitlements': {'module': 'identity_domains', 'class': 'list[UserEntitlements]'}, 'roles': {'module': 'identity_domains', 'class': 'list[UserRoles]'}, 'x509-certificates': {'module': 'identity_domains', 'class': 'list[UserX509Certificates]'}, 'urnietfparamsscimschemasextensionenterprise2-0-user': {'module': 'identity_domains', 'class': 'ExtensionEnterprise20User'}, 'urnietfparamsscimschemasoracleidcsextensionuser-user': {'module': 'identity_domains', 'class': 'ExtensionUserUser'}, 'urnietfparamsscimschemasoracleidcsextensionpassword-state-user': {'module': 'identity_domains', 'class': 'ExtensionPasswordStateUser'}, 'urnietfparamsscimschemasoracleidcsextensionuser-state-user': {'module': 'identity_domains', 'class': 'ExtensionUserStateUser'}, 'urnietfparamsscimschemasoracleidcsextensionposix-user': {'module': 'identity_domains', 'class': 'ExtensionPosixUser'}, 'urnietfparamsscimschemasoracleidcsextensionkerberos-user-user': {'module': 'identity_domains', 'class': 'ExtensionKerberosUserUser'}, 'urnietfparamsscimschemasoracleidcsextensionmfa-user': {'module': 'identity_domains', 'class': 'ExtensionMfaUser'}, 'urnietfparamsscimschemasoracleidcsextensionadaptive-user': {'module': 'identity_domains', 'class': 'ExtensionAdaptiveUser'}, 'urnietfparamsscimschemasoracleidcsextensionsff-user': {'module': 'identity_domains', 'class': 'ExtensionSffUser'}, 'urnietfparamsscimschemasoracleidcsextensionsecurity-questions-user': {'module': 'identity_domains', 'class': 'ExtensionSecurityQuestionsUser'}, 'urnietfparamsscimschemasoracleidcsextensionself-registration-user': {'module': 'identity_domains', 'class': 'ExtensionSelfRegistrationUser'}, 'urnietfparamsscimschemasoracleidcsextensionsocial-account-user': {'module': 'identity_domains', 'class': 'ExtensionSocialAccountUser'}, 'urnietfparamsscimschemasoracleidcsextensiondb-user-user': {'module': 'identity_domains', 'class': 'ExtensionDbUserUser'}, 'urnietfparamsscimschemasoracleidcsextensionterms-of-use-user': {'module': 'identity_domains', 'class': 'ExtensionTermsOfUseUser'}, 'urnietfparamsscimschemasoracleidcsextensionpasswordless-user': {'module': 'identity_domains', 'class': 'ExtensionPasswordlessUser'}, 'urnietfparamsscimschemasoracleidcsextension-oci-tags': {'module': 'identity_domains', 'class': 'ExtensionOCITags'}, 'urnietfparamsscimschemasoracleidcsextensionuser-credentials-user': {'module': 'identity_domains', 'class': 'ExtensionUserCredentialsUser'}, 'urnietfparamsscimschemasoracleidcsextensioncapabilities-user': {'module': 'identity_domains', 'class': 'ExtensionCapabilitiesUser'}, 'urnietfparamsscimschemasoracleidcsextensiondb-credentials-user': {'module': 'identity_domains', 'class': 'ExtensionDbCredentialsUser'}, 'urnietfparamsscimschemasoracleidcsextensionself-change-user': {'module': 'identity_domains', 'class': 'ExtensionSelfChangeUser'}}, output_type={'module': 'identity_domains', 'class': 'User'})
@cli_util.wrap_exceptions
def create_user_extended(ctx, **kwargs):

    if 'ext_enterprise_20_user' in kwargs:
        kwargs['urnietfparamsscimschemasextensionenterprise2_0_user'] = kwargs['ext_enterprise_20_user']
        kwargs.pop('ext_enterprise_20_user')

    if 'ext_oci_tags' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextension_oci_tags'] = kwargs['ext_oci_tags']
        kwargs.pop('ext_oci_tags')

    if 'ext_adaptive_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionadaptive_user'] = kwargs['ext_adaptive_user']
        kwargs.pop('ext_adaptive_user')

    if 'ext_capabilities_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensioncapabilities_user'] = kwargs['ext_capabilities_user']
        kwargs.pop('ext_capabilities_user')

    if 'ext_db_credentials_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensiondb_credentials_user'] = kwargs['ext_db_credentials_user']
        kwargs.pop('ext_db_credentials_user')

    if 'ext_db_user_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensiondb_user_user'] = kwargs['ext_db_user_user']
        kwargs.pop('ext_db_user_user')

    if 'ext_kerberos_user_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionkerberos_user_user'] = kwargs['ext_kerberos_user_user']
        kwargs.pop('ext_kerberos_user_user')

    if 'ext_mfa_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionmfa_user'] = kwargs['ext_mfa_user']
        kwargs.pop('ext_mfa_user')

    if 'ext_password_state_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionpassword_state_user'] = kwargs['ext_password_state_user']
        kwargs.pop('ext_password_state_user')

    if 'ext_passwordless_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionpasswordless_user'] = kwargs['ext_passwordless_user']
        kwargs.pop('ext_passwordless_user')

    if 'ext_posix_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionposix_user'] = kwargs['ext_posix_user']
        kwargs.pop('ext_posix_user')

    if 'ext_security_questions_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionsecurity_questions_user'] = kwargs['ext_security_questions_user']
        kwargs.pop('ext_security_questions_user')

    if 'ext_self_change_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionself_change_user'] = kwargs['ext_self_change_user']
        kwargs.pop('ext_self_change_user')

    if 'ext_self_registration_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionself_registration_user'] = kwargs['ext_self_registration_user']
        kwargs.pop('ext_self_registration_user')

    if 'ext_sff_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionsff_user'] = kwargs['ext_sff_user']
        kwargs.pop('ext_sff_user')

    if 'ext_social_account_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionsocial_account_user'] = kwargs['ext_social_account_user']
        kwargs.pop('ext_social_account_user')

    if 'ext_terms_of_use_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionterms_of_use_user'] = kwargs['ext_terms_of_use_user']
        kwargs.pop('ext_terms_of_use_user')

    if 'ext_user_credentials_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionuser_credentials_user'] = kwargs['ext_user_credentials_user']
        kwargs.pop('ext_user_credentials_user')

    if 'ext_user_state_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionuser_state_user'] = kwargs['ext_user_state_user']
        kwargs.pop('ext_user_state_user')

    if 'ext_user_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionuser_user'] = kwargs['ext_user_user']
        kwargs.pop('ext_user_user')

    ctx.invoke(identitydomains_cli.create_user, **kwargs)


@cli_util.copy_params_from_generated_command(identitydomains_cli.put_user, params_to_exclude=['urnietfparamsscimschemasextensionenterprise2_0_user', 'urnietfparamsscimschemasoracleidcsextension_oci_tags', 'urnietfparamsscimschemasoracleidcsextensionadaptive_user', 'urnietfparamsscimschemasoracleidcsextensioncapabilities_user', 'urnietfparamsscimschemasoracleidcsextensiondb_credentials_user', 'urnietfparamsscimschemasoracleidcsextensiondb_user_user', 'urnietfparamsscimschemasoracleidcsextensionkerberos_user_user', 'urnietfparamsscimschemasoracleidcsextensionmfa_user', 'urnietfparamsscimschemasoracleidcsextensionpassword_state_user', 'urnietfparamsscimschemasoracleidcsextensionpasswordless_user', 'urnietfparamsscimschemasoracleidcsextensionposix_user', 'urnietfparamsscimschemasoracleidcsextensionsecurity_questions_user', 'urnietfparamsscimschemasoracleidcsextensionself_change_user', 'urnietfparamsscimschemasoracleidcsextensionself_registration_user', 'urnietfparamsscimschemasoracleidcsextensionsff_user', 'urnietfparamsscimschemasoracleidcsextensionsocial_account_user', 'urnietfparamsscimschemasoracleidcsextensionterms_of_use_user', 'urnietfparamsscimschemasoracleidcsextensionuser_credentials_user', 'urnietfparamsscimschemasoracleidcsextensionuser_state_user', 'urnietfparamsscimschemasoracleidcsextensionuser_user'])
@identitydomains_cli.user_group.command(name=identitydomains_cli.put_user.name, help=identitydomains_cli.put_user.help)
@cli_util.option('--ext-enterprise-20-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-oci-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-adaptive-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-capabilities-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-db-credentials-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-db-user-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-kerberos-user-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-mfa-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-password-state-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-passwordless-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-posix-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-security-questions-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-self-change-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-self-registration-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-sff-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-social-account-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-terms-of-use-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-user-credentials-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-user-state-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-user-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'schemas': {'module': 'identity_domains', 'class': 'list[string]'}, 'meta': {'module': 'identity_domains', 'class': 'Meta'}, 'idcs-created-by': {'module': 'identity_domains', 'class': 'IdcsCreatedBy'}, 'idcs-last-modified-by': {'module': 'identity_domains', 'class': 'IdcsLastModifiedBy'}, 'tags': {'module': 'identity_domains', 'class': 'list[Tags]'}, 'name': {'module': 'identity_domains', 'class': 'UserName'}, 'emails': {'module': 'identity_domains', 'class': 'list[UserEmails]'}, 'phone-numbers': {'module': 'identity_domains', 'class': 'list[UserPhoneNumbers]'}, 'ims': {'module': 'identity_domains', 'class': 'list[UserIms]'}, 'photos': {'module': 'identity_domains', 'class': 'list[UserPhotos]'}, 'addresses': {'module': 'identity_domains', 'class': 'list[Addresses]'}, 'groups': {'module': 'identity_domains', 'class': 'list[UserGroups]'}, 'entitlements': {'module': 'identity_domains', 'class': 'list[UserEntitlements]'}, 'roles': {'module': 'identity_domains', 'class': 'list[UserRoles]'}, 'x509-certificates': {'module': 'identity_domains', 'class': 'list[UserX509Certificates]'}, 'urnietfparamsscimschemasextensionenterprise2-0-user': {'module': 'identity_domains', 'class': 'ExtensionEnterprise20User'}, 'urnietfparamsscimschemasoracleidcsextensionuser-user': {'module': 'identity_domains', 'class': 'ExtensionUserUser'}, 'urnietfparamsscimschemasoracleidcsextensionpassword-state-user': {'module': 'identity_domains', 'class': 'ExtensionPasswordStateUser'}, 'urnietfparamsscimschemasoracleidcsextensionuser-state-user': {'module': 'identity_domains', 'class': 'ExtensionUserStateUser'}, 'urnietfparamsscimschemasoracleidcsextensionposix-user': {'module': 'identity_domains', 'class': 'ExtensionPosixUser'}, 'urnietfparamsscimschemasoracleidcsextensionkerberos-user-user': {'module': 'identity_domains', 'class': 'ExtensionKerberosUserUser'}, 'urnietfparamsscimschemasoracleidcsextensionmfa-user': {'module': 'identity_domains', 'class': 'ExtensionMfaUser'}, 'urnietfparamsscimschemasoracleidcsextensionadaptive-user': {'module': 'identity_domains', 'class': 'ExtensionAdaptiveUser'}, 'urnietfparamsscimschemasoracleidcsextensionsff-user': {'module': 'identity_domains', 'class': 'ExtensionSffUser'}, 'urnietfparamsscimschemasoracleidcsextensionsecurity-questions-user': {'module': 'identity_domains', 'class': 'ExtensionSecurityQuestionsUser'}, 'urnietfparamsscimschemasoracleidcsextensionself-registration-user': {'module': 'identity_domains', 'class': 'ExtensionSelfRegistrationUser'}, 'urnietfparamsscimschemasoracleidcsextensionsocial-account-user': {'module': 'identity_domains', 'class': 'ExtensionSocialAccountUser'}, 'urnietfparamsscimschemasoracleidcsextensiondb-user-user': {'module': 'identity_domains', 'class': 'ExtensionDbUserUser'}, 'urnietfparamsscimschemasoracleidcsextensionterms-of-use-user': {'module': 'identity_domains', 'class': 'ExtensionTermsOfUseUser'}, 'urnietfparamsscimschemasoracleidcsextensionpasswordless-user': {'module': 'identity_domains', 'class': 'ExtensionPasswordlessUser'}, 'urnietfparamsscimschemasoracleidcsextension-oci-tags': {'module': 'identity_domains', 'class': 'ExtensionOCITags'}, 'urnietfparamsscimschemasoracleidcsextensionuser-credentials-user': {'module': 'identity_domains', 'class': 'ExtensionUserCredentialsUser'}, 'urnietfparamsscimschemasoracleidcsextensioncapabilities-user': {'module': 'identity_domains', 'class': 'ExtensionCapabilitiesUser'}, 'urnietfparamsscimschemasoracleidcsextensiondb-credentials-user': {'module': 'identity_domains', 'class': 'ExtensionDbCredentialsUser'}, 'urnietfparamsscimschemasoracleidcsextensionself-change-user': {'module': 'identity_domains', 'class': 'ExtensionSelfChangeUser'}}, output_type={'module': 'identity_domains', 'class': 'User'})
@cli_util.wrap_exceptions
def put_user_extended(ctx, **kwargs):

    if 'ext_enterprise_20_user' in kwargs:
        kwargs['urnietfparamsscimschemasextensionenterprise2_0_user'] = kwargs['ext_enterprise_20_user']
        kwargs.pop('ext_enterprise_20_user')

    if 'ext_oci_tags' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextension_oci_tags'] = kwargs['ext_oci_tags']
        kwargs.pop('ext_oci_tags')

    if 'ext_adaptive_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionadaptive_user'] = kwargs['ext_adaptive_user']
        kwargs.pop('ext_adaptive_user')

    if 'ext_capabilities_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensioncapabilities_user'] = kwargs['ext_capabilities_user']
        kwargs.pop('ext_capabilities_user')

    if 'ext_db_credentials_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensiondb_credentials_user'] = kwargs['ext_db_credentials_user']
        kwargs.pop('ext_db_credentials_user')

    if 'ext_db_user_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensiondb_user_user'] = kwargs['ext_db_user_user']
        kwargs.pop('ext_db_user_user')

    if 'ext_kerberos_user_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionkerberos_user_user'] = kwargs['ext_kerberos_user_user']
        kwargs.pop('ext_kerberos_user_user')

    if 'ext_mfa_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionmfa_user'] = kwargs['ext_mfa_user']
        kwargs.pop('ext_mfa_user')

    if 'ext_password_state_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionpassword_state_user'] = kwargs['ext_password_state_user']
        kwargs.pop('ext_password_state_user')

    if 'ext_passwordless_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionpasswordless_user'] = kwargs['ext_passwordless_user']
        kwargs.pop('ext_passwordless_user')

    if 'ext_posix_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionposix_user'] = kwargs['ext_posix_user']
        kwargs.pop('ext_posix_user')

    if 'ext_security_questions_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionsecurity_questions_user'] = kwargs['ext_security_questions_user']
        kwargs.pop('ext_security_questions_user')

    if 'ext_self_change_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionself_change_user'] = kwargs['ext_self_change_user']
        kwargs.pop('ext_self_change_user')

    if 'ext_self_registration_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionself_registration_user'] = kwargs['ext_self_registration_user']
        kwargs.pop('ext_self_registration_user')

    if 'ext_sff_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionsff_user'] = kwargs['ext_sff_user']
        kwargs.pop('ext_sff_user')

    if 'ext_social_account_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionsocial_account_user'] = kwargs['ext_social_account_user']
        kwargs.pop('ext_social_account_user')

    if 'ext_terms_of_use_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionterms_of_use_user'] = kwargs['ext_terms_of_use_user']
        kwargs.pop('ext_terms_of_use_user')

    if 'ext_user_credentials_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionuser_credentials_user'] = kwargs['ext_user_credentials_user']
        kwargs.pop('ext_user_credentials_user')

    if 'ext_user_state_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionuser_state_user'] = kwargs['ext_user_state_user']
        kwargs.pop('ext_user_state_user')

    if 'ext_user_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionuser_user'] = kwargs['ext_user_user']
        kwargs.pop('ext_user_user')

    ctx.invoke(identitydomains_cli.put_user, **kwargs)


@cli_util.copy_params_from_generated_command(identitydomains_cli.create_me, params_to_exclude=['urnietfparamsscimschemasoracleidcsextensionme_user', 'urnietfparamsscimschemasextensionenterprise2_0_user', 'urnietfparamsscimschemasoracleidcsextensionuser_user', 'urnietfparamsscimschemasoracleidcsextensionpassword_state_user', 'urnietfparamsscimschemasoracleidcsextensionuser_state_user', 'urnietfparamsscimschemasoracleidcsextensionposix_user', 'urnietfparamsscimschemasoracleidcsextensionmfa_user', 'urnietfparamsscimschemasoracleidcsextensionsecurity_questions_user', 'urnietfparamsscimschemasoracleidcsextensionself_registration_user', 'urnietfparamsscimschemasoracleidcsextensionterms_of_use_user', 'urnietfparamsscimschemasoracleidcsextension_oci_tags', 'urnietfparamsscimschemasoracleidcsextensionuser_credentials_user', 'urnietfparamsscimschemasoracleidcsextensioncapabilities_user', 'urnietfparamsscimschemasoracleidcsextensiondb_credentials_user'])
@identitydomains_cli.me_group.command(name=identitydomains_cli.create_me.name, help=identitydomains_cli.create_me.help)
@cli_util.option('--ext-me-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-enterprise-20-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-user-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-password-state-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-user-state-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-posix-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-mfa-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-security-questions-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-self-registration-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-terms-of-use-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-oci-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-user-credentials-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-capabilities-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-db-credentials-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'schemas': {'module': 'identity_domains', 'class': 'list[string]'}, 'meta': {'module': 'identity_domains', 'class': 'Meta'}, 'idcs-created-by': {'module': 'identity_domains', 'class': 'IdcsCreatedBy'}, 'idcs-last-modified-by': {'module': 'identity_domains', 'class': 'IdcsLastModifiedBy'}, 'tags': {'module': 'identity_domains', 'class': 'list[Tags]'}, 'name': {'module': 'identity_domains', 'class': 'MeName'}, 'emails': {'module': 'identity_domains', 'class': 'list[MeEmails]'}, 'phone-numbers': {'module': 'identity_domains', 'class': 'list[MePhoneNumbers]'}, 'ims': {'module': 'identity_domains', 'class': 'list[MeIms]'}, 'photos': {'module': 'identity_domains', 'class': 'list[MePhotos]'}, 'addresses': {'module': 'identity_domains', 'class': 'list[Addresses]'}, 'groups': {'module': 'identity_domains', 'class': 'list[MeGroups]'}, 'entitlements': {'module': 'identity_domains', 'class': 'list[MeEntitlements]'}, 'roles': {'module': 'identity_domains', 'class': 'list[MeRoles]'}, 'x509-certificates': {'module': 'identity_domains', 'class': 'list[MeX509Certificates]'}, 'urnietfparamsscimschemasextensionenterprise2-0-user': {'module': 'identity_domains', 'class': 'ExtensionEnterprise20User'}, 'urnietfparamsscimschemasoracleidcsextensionuser-user': {'module': 'identity_domains', 'class': 'ExtensionUserUser'}, 'urnietfparamsscimschemasoracleidcsextensionpassword-state-user': {'module': 'identity_domains', 'class': 'ExtensionPasswordStateUser'}, 'urnietfparamsscimschemasoracleidcsextensionuser-state-user': {'module': 'identity_domains', 'class': 'ExtensionUserStateUser'}, 'urnietfparamsscimschemasoracleidcsextensionme-user': {'module': 'identity_domains', 'class': 'ExtensionMeUser'}, 'urnietfparamsscimschemasoracleidcsextensionposix-user': {'module': 'identity_domains', 'class': 'ExtensionPosixUser'}, 'urnietfparamsscimschemasoracleidcsextensionmfa-user': {'module': 'identity_domains', 'class': 'ExtensionMfaUser'}, 'urnietfparamsscimschemasoracleidcsextensionsecurity-questions-user': {'module': 'identity_domains', 'class': 'ExtensionSecurityQuestionsUser'}, 'urnietfparamsscimschemasoracleidcsextensionself-registration-user': {'module': 'identity_domains', 'class': 'ExtensionSelfRegistrationUser'}, 'urnietfparamsscimschemasoracleidcsextensionterms-of-use-user': {'module': 'identity_domains', 'class': 'ExtensionTermsOfUseUser'}, 'urnietfparamsscimschemasoracleidcsextension-oci-tags': {'module': 'identity_domains', 'class': 'ExtensionOCITags'}, 'urnietfparamsscimschemasoracleidcsextensionuser-credentials-user': {'module': 'identity_domains', 'class': 'ExtensionUserCredentialsUser'}, 'urnietfparamsscimschemasoracleidcsextensioncapabilities-user': {'module': 'identity_domains', 'class': 'ExtensionCapabilitiesUser'}, 'urnietfparamsscimschemasoracleidcsextensiondb-credentials-user': {'module': 'identity_domains', 'class': 'ExtensionDbCredentialsUser'}}, output_type={'module': 'identity_domains', 'class': 'Me'})
@cli_util.wrap_exceptions
def create_me_extended(ctx, **kwargs):

    if 'ext_me_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionme_user'] = kwargs['ext_me_user']
        kwargs.pop('ext_me_user')

    if 'ext_enterprise_20_user' in kwargs:
        kwargs['urnietfparamsscimschemasextensionenterprise2_0_user'] = kwargs['ext_enterprise_20_user']
        kwargs.pop('ext_enterprise_20_user')

    if 'ext_user_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionuser_user'] = kwargs['ext_user_user']
        kwargs.pop('ext_user_user')

    if 'ext_password_state_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionpassword_state_user'] = kwargs['ext_password_state_user']
        kwargs.pop('ext_password_state_user')

    if 'ext_user_state_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionuser_state_user'] = kwargs['ext_user_state_user']
        kwargs.pop('ext_user_state_user')

    if 'ext_posix_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionposix_user'] = kwargs['ext_posix_user']
        kwargs.pop('ext_posix_user')

    if 'ext_mfa_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionmfa_user'] = kwargs['ext_mfa_user']
        kwargs.pop('ext_mfa_user')

    if 'ext_security_questions_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionsecurity_questions_user'] = kwargs['ext_security_questions_user']
        kwargs.pop('ext_security_questions_user')

    if 'ext_self_registration_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionself_registration_user'] = kwargs['ext_self_registration_user']
        kwargs.pop('ext_self_registration_user')

    if 'ext_terms_of_use_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionterms_of_use_user'] = kwargs['ext_terms_of_use_user']
        kwargs.pop('ext_terms_of_use_user')

    if 'ext_oci_tags' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextension_oci_tags'] = kwargs['ext_oci_tags']
        kwargs.pop('ext_oci_tags')

    if 'ext_user_credentials_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionuser_credentials_user'] = kwargs['ext_user_credentials_user']
        kwargs.pop('ext_user_credentials_user')

    if 'ext_capabilities_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensioncapabilities_user'] = kwargs['ext_capabilities_user']
        kwargs.pop('ext_capabilities_user')

    if 'ext_db_credentials_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensiondb_credentials_user'] = kwargs['ext_db_credentials_user']
        kwargs.pop('ext_db_credentials_user')

    ctx.invoke(identitydomains_cli.create_me, **kwargs)


@cli_util.copy_params_from_generated_command(identitydomains_cli.put_me, params_to_exclude=['urnietfparamsscimschemasoracleidcsextensionme_user', 'urnietfparamsscimschemasextensionenterprise2_0_user', 'urnietfparamsscimschemasoracleidcsextensionuser_user', 'urnietfparamsscimschemasoracleidcsextensionpassword_state_user', 'urnietfparamsscimschemasoracleidcsextensionuser_state_user', 'urnietfparamsscimschemasoracleidcsextensionposix_user', 'urnietfparamsscimschemasoracleidcsextensionmfa_user', 'urnietfparamsscimschemasoracleidcsextensionsecurity_questions_user', 'urnietfparamsscimschemasoracleidcsextensionself_registration_user', 'urnietfparamsscimschemasoracleidcsextensionterms_of_use_user', 'urnietfparamsscimschemasoracleidcsextension_oci_tags', 'urnietfparamsscimschemasoracleidcsextensionuser_credentials_user', 'urnietfparamsscimschemasoracleidcsextensioncapabilities_user', 'urnietfparamsscimschemasoracleidcsextensiondb_credentials_user'])
@identitydomains_cli.me_group.command(name=identitydomains_cli.put_me.name, help=identitydomains_cli.put_me.help)
@cli_util.option('--ext-me-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-enterprise-20-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-user-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-password-state-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-user-state-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-posix-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-mfa-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-security-questions-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-self-registration-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-terms-of-use-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-oci-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-user-credentials-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-capabilities-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-db-credentials-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'schemas': {'module': 'identity_domains', 'class': 'list[string]'}, 'meta': {'module': 'identity_domains', 'class': 'Meta'}, 'idcs-created-by': {'module': 'identity_domains', 'class': 'IdcsCreatedBy'}, 'idcs-last-modified-by': {'module': 'identity_domains', 'class': 'IdcsLastModifiedBy'}, 'tags': {'module': 'identity_domains', 'class': 'list[Tags]'}, 'name': {'module': 'identity_domains', 'class': 'MeName'}, 'emails': {'module': 'identity_domains', 'class': 'list[MeEmails]'}, 'phone-numbers': {'module': 'identity_domains', 'class': 'list[MePhoneNumbers]'}, 'ims': {'module': 'identity_domains', 'class': 'list[MeIms]'}, 'photos': {'module': 'identity_domains', 'class': 'list[MePhotos]'}, 'addresses': {'module': 'identity_domains', 'class': 'list[Addresses]'}, 'groups': {'module': 'identity_domains', 'class': 'list[MeGroups]'}, 'entitlements': {'module': 'identity_domains', 'class': 'list[MeEntitlements]'}, 'roles': {'module': 'identity_domains', 'class': 'list[MeRoles]'}, 'x509-certificates': {'module': 'identity_domains', 'class': 'list[MeX509Certificates]'}, 'urnietfparamsscimschemasextensionenterprise2-0-user': {'module': 'identity_domains', 'class': 'ExtensionEnterprise20User'}, 'urnietfparamsscimschemasoracleidcsextensionuser-user': {'module': 'identity_domains', 'class': 'ExtensionUserUser'}, 'urnietfparamsscimschemasoracleidcsextensionpassword-state-user': {'module': 'identity_domains', 'class': 'ExtensionPasswordStateUser'}, 'urnietfparamsscimschemasoracleidcsextensionuser-state-user': {'module': 'identity_domains', 'class': 'ExtensionUserStateUser'}, 'urnietfparamsscimschemasoracleidcsextensionme-user': {'module': 'identity_domains', 'class': 'ExtensionMeUser'}, 'urnietfparamsscimschemasoracleidcsextensionposix-user': {'module': 'identity_domains', 'class': 'ExtensionPosixUser'}, 'urnietfparamsscimschemasoracleidcsextensionmfa-user': {'module': 'identity_domains', 'class': 'ExtensionMfaUser'}, 'urnietfparamsscimschemasoracleidcsextensionsecurity-questions-user': {'module': 'identity_domains', 'class': 'ExtensionSecurityQuestionsUser'}, 'urnietfparamsscimschemasoracleidcsextensionself-registration-user': {'module': 'identity_domains', 'class': 'ExtensionSelfRegistrationUser'}, 'urnietfparamsscimschemasoracleidcsextensionterms-of-use-user': {'module': 'identity_domains', 'class': 'ExtensionTermsOfUseUser'}, 'urnietfparamsscimschemasoracleidcsextension-oci-tags': {'module': 'identity_domains', 'class': 'ExtensionOCITags'}, 'urnietfparamsscimschemasoracleidcsextensionuser-credentials-user': {'module': 'identity_domains', 'class': 'ExtensionUserCredentialsUser'}, 'urnietfparamsscimschemasoracleidcsextensioncapabilities-user': {'module': 'identity_domains', 'class': 'ExtensionCapabilitiesUser'}, 'urnietfparamsscimschemasoracleidcsextensiondb-credentials-user': {'module': 'identity_domains', 'class': 'ExtensionDbCredentialsUser'}}, output_type={'module': 'identity_domains', 'class': 'Me'})
@cli_util.wrap_exceptions
def put_me_extended(ctx, **kwargs):

    if 'ext_me_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionme_user'] = kwargs['ext_me_user']
        kwargs.pop('ext_me_user')

    if 'ext_enterprise_20_user' in kwargs:
        kwargs['urnietfparamsscimschemasextensionenterprise2_0_user'] = kwargs['ext_enterprise_20_user']
        kwargs.pop('ext_enterprise_20_user')

    if 'ext_user_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionuser_user'] = kwargs['ext_user_user']
        kwargs.pop('ext_user_user')

    if 'ext_password_state_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionpassword_state_user'] = kwargs['ext_password_state_user']
        kwargs.pop('ext_password_state_user')

    if 'ext_user_state_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionuser_state_user'] = kwargs['ext_user_state_user']
        kwargs.pop('ext_user_state_user')

    if 'ext_posix_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionposix_user'] = kwargs['ext_posix_user']
        kwargs.pop('ext_posix_user')

    if 'ext_mfa_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionmfa_user'] = kwargs['ext_mfa_user']
        kwargs.pop('ext_mfa_user')

    if 'ext_security_questions_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionsecurity_questions_user'] = kwargs['ext_security_questions_user']
        kwargs.pop('ext_security_questions_user')

    if 'ext_self_registration_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionself_registration_user'] = kwargs['ext_self_registration_user']
        kwargs.pop('ext_self_registration_user')

    if 'ext_terms_of_use_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionterms_of_use_user'] = kwargs['ext_terms_of_use_user']
        kwargs.pop('ext_terms_of_use_user')

    if 'ext_oci_tags' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextension_oci_tags'] = kwargs['ext_oci_tags']
        kwargs.pop('ext_oci_tags')

    if 'ext_user_credentials_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionuser_credentials_user'] = kwargs['ext_user_credentials_user']
        kwargs.pop('ext_user_credentials_user')

    if 'ext_capabilities_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensioncapabilities_user'] = kwargs['ext_capabilities_user']
        kwargs.pop('ext_capabilities_user')

    if 'ext_db_credentials_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensiondb_credentials_user'] = kwargs['ext_db_credentials_user']
        kwargs.pop('ext_db_credentials_user')

    ctx.invoke(identitydomains_cli.put_me, **kwargs)


@cli_util.copy_params_from_generated_command(identitydomains_cli.create_group, params_to_exclude=['urnietfparamsscimschemasoracleidcsextensiondbcs_group', 'urnietfparamsscimschemasoracleidcsextensiondynamic_group', 'urnietfparamsscimschemasoracleidcsextensiongroup_group', 'urnietfparamsscimschemasoracleidcsextensionposix_group', 'urnietfparamsscimschemasoracleidcsextensionrequestable_group', 'urnietfparamsscimschemasoracleidcsextension_oci_tags'])
@identitydomains_cli.group_group.command(name=identitydomains_cli.create_group.name, help=identitydomains_cli.create_group.help)
@cli_util.option('--ext-oci-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-dbcs-group', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-dynamic-group', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-group-group', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-posix-group', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-requestable-group', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'schemas': {'module': 'identity_domains', 'class': 'list[string]'}, 'meta': {'module': 'identity_domains', 'class': 'Meta'}, 'idcs-created-by': {'module': 'identity_domains', 'class': 'IdcsCreatedBy'}, 'idcs-last-modified-by': {'module': 'identity_domains', 'class': 'IdcsLastModifiedBy'}, 'tags': {'module': 'identity_domains', 'class': 'list[Tags]'}, 'members': {'module': 'identity_domains', 'class': 'list[GroupMembers]'}, 'urnietfparamsscimschemasoracleidcsextensiongroup-group': {'module': 'identity_domains', 'class': 'ExtensionGroupGroup'}, 'urnietfparamsscimschemasoracleidcsextensionposix-group': {'module': 'identity_domains', 'class': 'ExtensionPosixGroup'}, 'urnietfparamsscimschemasoracleidcsextensionrequestable-group': {'module': 'identity_domains', 'class': 'ExtensionRequestableGroup'}, 'urnietfparamsscimschemasoracleidcsextensiondbcs-group': {'module': 'identity_domains', 'class': 'ExtensionDbcsGroup'}, 'urnietfparamsscimschemasoracleidcsextensiondynamic-group': {'module': 'identity_domains', 'class': 'ExtensionDynamicGroup'}, 'urnietfparamsscimschemasoracleidcsextension-oci-tags': {'module': 'identity_domains', 'class': 'ExtensionOCITags'}}, output_type={'module': 'identity_domains', 'class': 'Group'})
@cli_util.wrap_exceptions
def create_group_extended(ctx, **kwargs):

    if 'ext_oci_tags' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextension_oci_tags'] = kwargs['ext_oci_tags']
        kwargs.pop('ext_oci_tags')

    if 'ext_dbcs_group' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensiondbcs_group'] = kwargs['ext_dbcs_group']
        kwargs.pop('ext_dbcs_group')

    if 'ext_dynamic_group' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensiondynamic_group'] = kwargs['ext_dynamic_group']
        kwargs.pop('ext_dynamic_group')

    if 'ext_group_group' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensiongroup_group'] = kwargs['ext_group_group']
        kwargs.pop('ext_group_group')

    if 'ext_posix_group' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionposix_group'] = kwargs['ext_posix_group']
        kwargs.pop('ext_posix_group')

    if 'ext_requestable_group' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionrequestable_group'] = kwargs['ext_requestable_group']
        kwargs.pop('ext_requestable_group')

    ctx.invoke(identitydomains_cli.create_group, **kwargs)


@cli_util.copy_params_from_generated_command(identitydomains_cli.put_group, params_to_exclude=['urnietfparamsscimschemasoracleidcsextensiondbcs_group', 'urnietfparamsscimschemasoracleidcsextensiondynamic_group', 'urnietfparamsscimschemasoracleidcsextensiongroup_group', 'urnietfparamsscimschemasoracleidcsextensionposix_group', 'urnietfparamsscimschemasoracleidcsextensionrequestable_group', 'urnietfparamsscimschemasoracleidcsextension_oci_tags'])
@identitydomains_cli.group_group.command(name=identitydomains_cli.put_group.name, help=identitydomains_cli.put_group.help)
@cli_util.option('--ext-oci-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-dbcs-group', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-dynamic-group', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-group-group', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-posix-group', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-requestable-group', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'schemas': {'module': 'identity_domains', 'class': 'list[string]'}, 'meta': {'module': 'identity_domains', 'class': 'Meta'}, 'idcs-created-by': {'module': 'identity_domains', 'class': 'IdcsCreatedBy'}, 'idcs-last-modified-by': {'module': 'identity_domains', 'class': 'IdcsLastModifiedBy'}, 'tags': {'module': 'identity_domains', 'class': 'list[Tags]'}, 'members': {'module': 'identity_domains', 'class': 'list[GroupMembers]'}, 'urnietfparamsscimschemasoracleidcsextensiongroup-group': {'module': 'identity_domains', 'class': 'ExtensionGroupGroup'}, 'urnietfparamsscimschemasoracleidcsextensionposix-group': {'module': 'identity_domains', 'class': 'ExtensionPosixGroup'}, 'urnietfparamsscimschemasoracleidcsextensionrequestable-group': {'module': 'identity_domains', 'class': 'ExtensionRequestableGroup'}, 'urnietfparamsscimschemasoracleidcsextensiondbcs-group': {'module': 'identity_domains', 'class': 'ExtensionDbcsGroup'}, 'urnietfparamsscimschemasoracleidcsextensiondynamic-group': {'module': 'identity_domains', 'class': 'ExtensionDynamicGroup'}, 'urnietfparamsscimschemasoracleidcsextension-oci-tags': {'module': 'identity_domains', 'class': 'ExtensionOCITags'}}, output_type={'module': 'identity_domains', 'class': 'Group'})
@cli_util.wrap_exceptions
def put_group_extended(ctx, **kwargs):

    if 'ext_oci_tags' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextension_oci_tags'] = kwargs['ext_oci_tags']
        kwargs.pop('ext_oci_tags')

    if 'ext_dbcs_group' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensiondbcs_group'] = kwargs['ext_dbcs_group']
        kwargs.pop('ext_dbcs_group')

    if 'ext_dynamic_group' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensiondynamic_group'] = kwargs['ext_dynamic_group']
        kwargs.pop('ext_dynamic_group')

    if 'ext_group_group' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensiongroup_group'] = kwargs['ext_group_group']
        kwargs.pop('ext_group_group')

    if 'ext_posix_group' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionposix_group'] = kwargs['ext_posix_group']
        kwargs.pop('ext_posix_group')

    if 'ext_requestable_group' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionrequestable_group'] = kwargs['ext_requestable_group']
        kwargs.pop('ext_requestable_group')

    ctx.invoke(identitydomains_cli.put_group, **kwargs)


@cli_util.copy_params_from_generated_command(identitydomains_cli.create_identity_provider, params_to_exclude=['urnietfparamsscimschemasoracleidcsextensionsocial_identity_provider', 'urnietfparamsscimschemasoracleidcsextensionx509_identity_provider'])
@identitydomains_cli.identity_provider_group.command(name=identitydomains_cli.create_identity_provider.name, help=identitydomains_cli.create_identity_provider.help)
@cli_util.option('--ext-social-identity-provider', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-x509-identity-provider', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'schemas': {'module': 'identity_domains', 'class': 'list[string]'}, 'meta': {'module': 'identity_domains', 'class': 'Meta'}, 'idcs-created-by': {'module': 'identity_domains', 'class': 'IdcsCreatedBy'}, 'idcs-last-modified-by': {'module': 'identity_domains', 'class': 'IdcsLastModifiedBy'}, 'tags': {'module': 'identity_domains', 'class': 'list[Tags]'}, 'jit-user-prov-group-mappings': {'module': 'identity_domains', 'class': 'list[IdentityProviderJitUserProvGroupMappings]'}, 'requested-authentication-context': {'module': 'identity_domains', 'class': 'list[string]'}, 'jit-user-prov-attributes': {'module': 'identity_domains', 'class': 'IdentityProviderJitUserProvAttributes'}, 'jit-user-prov-assigned-groups': {'module': 'identity_domains', 'class': 'list[IdentityProviderJitUserProvAssignedGroups]'}, 'correlation-policy': {'module': 'identity_domains', 'class': 'IdentityProviderCorrelationPolicy'}, 'urnietfparamsscimschemasoracleidcsextensionsocial-identity-provider': {'module': 'identity_domains', 'class': 'ExtensionSocialIdentityProvider'}, 'urnietfparamsscimschemasoracleidcsextensionx509-identity-provider': {'module': 'identity_domains', 'class': 'ExtensionX509IdentityProvider'}}, output_type={'module': 'identity_domains', 'class': 'IdentityProvider'})
@cli_util.wrap_exceptions
def create_identity_provider_extended(ctx, **kwargs):

    if 'ext_social_identity_provider' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionsocial_identity_provider'] = kwargs['ext_social_identity_provider']
        kwargs.pop('ext_social_identity_provider')

    if 'ext_x509_identity_provider' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionx509_identity_provider'] = kwargs['ext_x509_identity_provider']
        kwargs.pop('ext_x509_identity_provider')

    ctx.invoke(identitydomains_cli.create_identity_provider, **kwargs)


@cli_util.copy_params_from_generated_command(identitydomains_cli.put_identity_provider, params_to_exclude=['urnietfparamsscimschemasoracleidcsextensionsocial_identity_provider', 'urnietfparamsscimschemasoracleidcsextensionx509_identity_provider'])
@identitydomains_cli.identity_provider_group.command(name=identitydomains_cli.put_identity_provider.name, help=identitydomains_cli.put_identity_provider.help)
@cli_util.option('--ext-social-identity-provider', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-x509-identity-provider', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'schemas': {'module': 'identity_domains', 'class': 'list[string]'}, 'meta': {'module': 'identity_domains', 'class': 'Meta'}, 'idcs-created-by': {'module': 'identity_domains', 'class': 'IdcsCreatedBy'}, 'idcs-last-modified-by': {'module': 'identity_domains', 'class': 'IdcsLastModifiedBy'}, 'tags': {'module': 'identity_domains', 'class': 'list[Tags]'}, 'jit-user-prov-group-mappings': {'module': 'identity_domains', 'class': 'list[IdentityProviderJitUserProvGroupMappings]'}, 'requested-authentication-context': {'module': 'identity_domains', 'class': 'list[string]'}, 'jit-user-prov-attributes': {'module': 'identity_domains', 'class': 'IdentityProviderJitUserProvAttributes'}, 'jit-user-prov-assigned-groups': {'module': 'identity_domains', 'class': 'list[IdentityProviderJitUserProvAssignedGroups]'}, 'correlation-policy': {'module': 'identity_domains', 'class': 'IdentityProviderCorrelationPolicy'}, 'urnietfparamsscimschemasoracleidcsextensionsocial-identity-provider': {'module': 'identity_domains', 'class': 'ExtensionSocialIdentityProvider'}, 'urnietfparamsscimschemasoracleidcsextensionx509-identity-provider': {'module': 'identity_domains', 'class': 'ExtensionX509IdentityProvider'}}, output_type={'module': 'identity_domains', 'class': 'IdentityProvider'})
@cli_util.wrap_exceptions
def put_identity_provider_extended(ctx, **kwargs):

    if 'ext_social_identity_provider' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionsocial_identity_provider'] = kwargs['ext_social_identity_provider']
        kwargs.pop('ext_social_identity_provider')

    if 'ext_x509_identity_provider' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionx509_identity_provider'] = kwargs['ext_x509_identity_provider']
        kwargs.pop('ext_x509_identity_provider')

    ctx.invoke(identitydomains_cli.put_identity_provider, **kwargs)


@cli_util.copy_params_from_generated_command(identitydomains_cli.create_dynamic_resource_group, params_to_exclude=['urnietfparamsscimschemasoracleidcsextension_oci_tags'])
@identitydomains_cli.dynamic_resource_group_group.command(name=identitydomains_cli.create_dynamic_resource_group.name, help=identitydomains_cli.create_dynamic_resource_group.help)
@cli_util.option('--ext-oci-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'schemas': {'module': 'identity_domains', 'class': 'list[string]'}, 'meta': {'module': 'identity_domains', 'class': 'Meta'}, 'idcs-created-by': {'module': 'identity_domains', 'class': 'IdcsCreatedBy'}, 'idcs-last-modified-by': {'module': 'identity_domains', 'class': 'IdcsLastModifiedBy'}, 'tags': {'module': 'identity_domains', 'class': 'list[Tags]'}, 'grants': {'module': 'identity_domains', 'class': 'list[DynamicResourceGroupGrants]'}, 'dynamic-group-app-roles': {'module': 'identity_domains', 'class': 'list[DynamicResourceGroupDynamicGroupAppRoles]'}, 'urnietfparamsscimschemasoracleidcsextension-oci-tags': {'module': 'identity_domains', 'class': 'ExtensionOCITags'}}, output_type={'module': 'identity_domains', 'class': 'DynamicResourceGroup'})
@cli_util.wrap_exceptions
def create_dynamic_resource_group_extended(ctx, **kwargs):

    if 'ext_oci_tags' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextension_oci_tags'] = kwargs['ext_oci_tags']
        kwargs.pop('ext_oci_tags')

    ctx.invoke(identitydomains_cli.create_dynamic_resource_group, **kwargs)


@cli_util.copy_params_from_generated_command(identitydomains_cli.put_dynamic_resource_group, params_to_exclude=['urnietfparamsscimschemasoracleidcsextension_oci_tags'])
@identitydomains_cli.dynamic_resource_group_group.command(name=identitydomains_cli.put_dynamic_resource_group.name, help=identitydomains_cli.put_dynamic_resource_group.help)
@cli_util.option('--ext-oci-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'schemas': {'module': 'identity_domains', 'class': 'list[string]'}, 'meta': {'module': 'identity_domains', 'class': 'Meta'}, 'idcs-created-by': {'module': 'identity_domains', 'class': 'IdcsCreatedBy'}, 'idcs-last-modified-by': {'module': 'identity_domains', 'class': 'IdcsLastModifiedBy'}, 'tags': {'module': 'identity_domains', 'class': 'list[Tags]'}, 'grants': {'module': 'identity_domains', 'class': 'list[DynamicResourceGroupGrants]'}, 'dynamic-group-app-roles': {'module': 'identity_domains', 'class': 'list[DynamicResourceGroupDynamicGroupAppRoles]'}, 'urnietfparamsscimschemasoracleidcsextension-oci-tags': {'module': 'identity_domains', 'class': 'ExtensionOCITags'}}, output_type={'module': 'identity_domains', 'class': 'DynamicResourceGroup'})
@cli_util.wrap_exceptions
def put_dynamic_resource_group_extended(ctx, **kwargs):

    if 'ext_oci_tags' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextension_oci_tags'] = kwargs['ext_oci_tags']
        kwargs.pop('ext_oci_tags')

    ctx.invoke(identitydomains_cli.put_dynamic_resource_group, **kwargs)


@cli_util.copy_params_from_generated_command(identitydomains_cli.put_authentication_factor_setting, params_to_exclude=['urnietfparamsscimschemasoracleidcsextensionthird_party_authentication_factor_settings', 'urnietfparamsscimschemasoracleidcsextensionfido_authentication_factor_settings'])
@identitydomains_cli.authentication_factor_setting_group.command(name=identitydomains_cli.put_authentication_factor_setting.name, help=identitydomains_cli.put_authentication_factor_setting.help)
@cli_util.option('--ext-third-party-authentication-factor-settings', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-fido-authentication-factor-settings', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'schemas': {'module': 'identity_domains', 'class': 'list[string]'}, 'meta': {'module': 'identity_domains', 'class': 'Meta'}, 'idcs-created-by': {'module': 'identity_domains', 'class': 'IdcsCreatedBy'}, 'idcs-last-modified-by': {'module': 'identity_domains', 'class': 'IdcsLastModifiedBy'}, 'tags': {'module': 'identity_domains', 'class': 'list[Tags]'}, 'email-settings': {'module': 'identity_domains', 'class': 'AuthenticationFactorSettingsEmailSettings'}, 'third-party-factor': {'module': 'identity_domains', 'class': 'AuthenticationFactorSettingsThirdPartyFactor'}, 'notification-settings': {'module': 'identity_domains', 'class': 'AuthenticationFactorSettingsNotificationSettings'}, 'identity-store-settings': {'module': 'identity_domains', 'class': 'AuthenticationFactorSettingsIdentityStoreSettings'}, 'bypass-code-settings': {'module': 'identity_domains', 'class': 'AuthenticationFactorSettingsBypassCodeSettings'}, 'client-app-settings': {'module': 'identity_domains', 'class': 'AuthenticationFactorSettingsClientAppSettings'}, 'endpoint-restrictions': {'module': 'identity_domains', 'class': 'AuthenticationFactorSettingsEndpointRestrictions'}, 'compliance-policy': {'module': 'identity_domains', 'class': 'list[AuthenticationFactorSettingsCompliancePolicy]'}, 'totp-settings': {'module': 'identity_domains', 'class': 'AuthenticationFactorSettingsTotpSettings'}, 'urnietfparamsscimschemasoracleidcsextensionthird-party-authentication-factor-settings': {'module': 'identity_domains', 'class': 'ExtensionThirdPartyAuthenticationFactorSettings'}, 'urnietfparamsscimschemasoracleidcsextensionfido-authentication-factor-settings': {'module': 'identity_domains', 'class': 'ExtensionFidoAuthenticationFactorSettings'}}, output_type={'module': 'identity_domains', 'class': 'AuthenticationFactorSetting'})
@cli_util.wrap_exceptions
def put_authentication_factor_setting_extended(ctx, **kwargs):

    if 'ext_third_party_authentication_factor_settings' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionthird_party_authentication_factor_settings'] = kwargs['ext_third_party_authentication_factor_settings']
        kwargs.pop('ext_third_party_authentication_factor_settings')

    if 'ext_fido_authentication_factor_settings' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionfido_authentication_factor_settings'] = kwargs['ext_fido_authentication_factor_settings']
        kwargs.pop('ext_fido_authentication_factor_settings')

    ctx.invoke(identitydomains_cli.put_authentication_factor_setting, **kwargs)


@cli_util.copy_params_from_generated_command(identitydomains_cli.create_app, params_to_exclude=['urnietfparamsscimschemasoracleidcsextensionform_fill_app_template_app_template', 'urnietfparamsscimschemasoracleidcsextension_oci_tags', 'urnietfparamsscimschemasoracleidcsextensiondbcs_app', 'urnietfparamsscimschemasoracleidcsextensionenterprise_app_app', 'urnietfparamsscimschemasoracleidcsextensionform_fill_app_app', 'urnietfparamsscimschemasoracleidcsextensionkerberos_realm_app', 'urnietfparamsscimschemasoracleidcsextensionmanagedapp_app', 'urnietfparamsscimschemasoracleidcsextensionmulticloud_service_app_app', 'urnietfparamsscimschemasoracleidcsextensionopc_service_app', 'urnietfparamsscimschemasoracleidcsextensionradius_app_app', 'urnietfparamsscimschemasoracleidcsextensionrequestable_app', 'urnietfparamsscimschemasoracleidcsextensionsaml_service_provider_app', 'urnietfparamsscimschemasoracleidcsextensionweb_tier_policy_app'])
@identitydomains_cli.app_group.command(name=identitydomains_cli.create_app.name, help=identitydomains_cli.create_app.help)
@cli_util.option('--ext-form-fill-app-template-app-template', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-oci-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-dbcs-app', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-enterprise-app-app', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-form-fill-app-app', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-kerberos-realm-app', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-managedapp-app', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-multicloud-service-app-app', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-opc-service-app', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-radius-app-app', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-requestable-app', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-saml-service-provider-app', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-web-tier-policy-app', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'schemas': {'module': 'identity_domains', 'class': 'list[string]'}, 'meta': {'module': 'identity_domains', 'class': 'Meta'}, 'idcs-created-by': {'module': 'identity_domains', 'class': 'IdcsCreatedBy'}, 'idcs-last-modified-by': {'module': 'identity_domains', 'class': 'IdcsLastModifiedBy'}, 'tags': {'module': 'identity_domains', 'class': 'list[Tags]'}, 'delegated-service-names': {'module': 'identity_domains', 'class': 'list[string]'}, 'redirect-uris': {'module': 'identity_domains', 'class': 'list[string]'}, 'post-logout-redirect-uris': {'module': 'identity_domains', 'class': 'list[string]'}, 'allowed-grants': {'module': 'identity_domains', 'class': 'list[string]'}, 'secondary-audiences': {'module': 'identity_domains', 'class': 'list[string]'}, 'radius-policy': {'module': 'identity_domains', 'class': 'AppRadiusPolicy'}, 'apps-network-perimeters': {'module': 'identity_domains', 'class': 'list[AppAppsNetworkPerimeters]'}, 'cloud-control-properties': {'module': 'identity_domains', 'class': 'list[AppCloudControlProperties]'}, 'editable-attributes': {'module': 'identity_domains', 'class': 'list[AppEditableAttributes]'}, 'terms-of-use': {'module': 'identity_domains', 'class': 'AppTermsOfUse'}, 'protectable-secondary-audiences': {'module': 'identity_domains', 'class': 'list[AppProtectableSecondaryAudiences]'}, 'idp-policy': {'module': 'identity_domains', 'class': 'AppIdpPolicy'}, 'allowed-tags': {'module': 'identity_domains', 'class': 'list[AppAllowedTags]'}, 'app-signon-policy': {'module': 'identity_domains', 'class': 'AppAppSignonPolicy'}, 'trust-policies': {'module': 'identity_domains', 'class': 'list[AppTrustPolicies]'}, 'signon-policy': {'module': 'identity_domains', 'class': 'AppSignonPolicy'}, 'identity-providers': {'module': 'identity_domains', 'class': 'list[AppIdentityProviders]'}, 'accounts': {'module': 'identity_domains', 'class': 'list[AppAccounts]'}, 'grants': {'module': 'identity_domains', 'class': 'list[AppGrants]'}, 'service-params': {'module': 'identity_domains', 'class': 'list[AppServiceParams]'}, 'attr-rendering-metadata': {'module': 'identity_domains', 'class': 'list[AppAttrRenderingMetadata]'}, 'based-on-template': {'module': 'identity_domains', 'class': 'AppBasedOnTemplate'}, 'granted-app-roles': {'module': 'identity_domains', 'class': 'list[AppGrantedAppRoles]'}, 'saml-service-provider': {'module': 'identity_domains', 'class': 'AppSamlServiceProvider'}, 'allowed-scopes': {'module': 'identity_domains', 'class': 'list[AppAllowedScopes]'}, 'certificates': {'module': 'identity_domains', 'class': 'list[AppCertificates]'}, 'alias-apps': {'module': 'identity_domains', 'class': 'list[AppAliasApps]'}, 'as-opc-service': {'module': 'identity_domains', 'class': 'AppAsOPCService'}, 'admin-roles': {'module': 'identity_domains', 'class': 'list[AppAdminRoles]'}, 'user-roles': {'module': 'identity_domains', 'class': 'list[AppUserRoles]'}, 'scopes': {'module': 'identity_domains', 'class': 'list[AppScopes]'}, 'urnietfparamsscimschemasoracleidcsextensionradius-app-app': {'module': 'identity_domains', 'class': 'AppExtensionRadiusAppApp'}, 'urnietfparamsscimschemasoracleidcsextensionsaml-service-provider-app': {'module': 'identity_domains', 'class': 'AppExtensionSamlServiceProviderApp'}, 'urnietfparamsscimschemasoracleidcsextensionweb-tier-policy-app': {'module': 'identity_domains', 'class': 'AppExtensionWebTierPolicyApp'}, 'urnietfparamsscimschemasoracleidcsextensionmanagedapp-app': {'module': 'identity_domains', 'class': 'AppExtensionManagedappApp'}, 'urnietfparamsscimschemasoracleidcsextensionform-fill-app-template-app-template': {'module': 'identity_domains', 'class': 'AppExtensionFormFillAppTemplateAppTemplate'}, 'urnietfparamsscimschemasoracleidcsextensionopc-service-app': {'module': 'identity_domains', 'class': 'AppExtensionOpcServiceApp'}, 'urnietfparamsscimschemasoracleidcsextensionkerberos-realm-app': {'module': 'identity_domains', 'class': 'AppExtensionKerberosRealmApp'}, 'urnietfparamsscimschemasoracleidcsextensionrequestable-app': {'module': 'identity_domains', 'class': 'AppExtensionRequestableApp'}, 'urnietfparamsscimschemasoracleidcsextensionform-fill-app-app': {'module': 'identity_domains', 'class': 'AppExtensionFormFillAppApp'}, 'urnietfparamsscimschemasoracleidcsextensiondbcs-app': {'module': 'identity_domains', 'class': 'AppExtensionDbcsApp'}, 'urnietfparamsscimschemasoracleidcsextensionenterprise-app-app': {'module': 'identity_domains', 'class': 'AppExtensionEnterpriseAppApp'}, 'urnietfparamsscimschemasoracleidcsextension-oci-tags': {'module': 'identity_domains', 'class': 'ExtensionOCITags'}, 'urnietfparamsscimschemasoracleidcsextensionmulticloud-service-app-app': {'module': 'identity_domains', 'class': 'AppExtensionMulticloudServiceAppApp'}}, output_type={'module': 'identity_domains', 'class': 'App'})
@cli_util.wrap_exceptions
def create_app_extended(ctx, **kwargs):

    if 'ext_form_fill_app_template_app_template' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionform_fill_app_template_app_template'] = kwargs['ext_form_fill_app_template_app_template']
        kwargs.pop('ext_form_fill_app_template_app_template')
    if 'ext_oci_tags' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextension_oci_tags'] = kwargs['ext_oci_tags']
        kwargs.pop('ext_oci_tags')
    if 'ext_dbcs_app' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensiondbcs_app'] = kwargs['ext_dbcs_app']
        kwargs.pop('ext_dbcs_app')
    if 'ext_enterprise_app_app' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionenterprise_app_app'] = kwargs['ext_enterprise_app_app']
        kwargs.pop('ext_enterprise_app_app')
    if 'ext_form_fill_app_app' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionform_fill_app_app'] = kwargs['ext_form_fill_app_app']
        kwargs.pop('ext_form_fill_app_app')
    if 'ext_kerberos_realm_app' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionkerberos_realm_app'] = kwargs['ext_kerberos_realm_app']
        kwargs.pop('ext_kerberos_realm_app')
    if 'ext_managedapp_app' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionmanagedapp_app'] = kwargs['ext_managedapp_app']
        kwargs.pop('ext_managedapp_app')
    if 'ext_multicloud_service_app_app' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionmulticloud_service_app_app'] = kwargs['ext_multicloud_service_app_app']
        kwargs.pop('ext_multicloud_service_app_app')
    if 'ext_opc_service_app' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionopc_service_app'] = kwargs['ext_opc_service_app']
        kwargs.pop('ext_opc_service_app')
    if 'ext_radius_app_app' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionradius_app_app'] = kwargs['ext_radius_app_app']
        kwargs.pop('ext_radius_app_app')
    if 'ext_requestable_app' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionrequestable_app'] = kwargs['ext_requestable_app']
        kwargs.pop('ext_requestable_app')
    if 'ext_saml_service_provider_app' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionsaml_service_provider_app'] = kwargs['ext_saml_service_provider_app']
        kwargs.pop('ext_saml_service_provider_app')
    if 'ext_web_tier_policy_app' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionweb_tier_policy_app'] = kwargs['ext_web_tier_policy_app']
        kwargs.pop('ext_web_tier_policy_app')

    ctx.invoke(identitydomains_cli.create_app, **kwargs)


@cli_util.copy_params_from_generated_command(identitydomains_cli.put_app, params_to_exclude=['urnietfparamsscimschemasoracleidcsextensionform_fill_app_template_app_template', 'urnietfparamsscimschemasoracleidcsextension_oci_tags', 'urnietfparamsscimschemasoracleidcsextensiondbcs_app', 'urnietfparamsscimschemasoracleidcsextensionenterprise_app_app', 'urnietfparamsscimschemasoracleidcsextensionform_fill_app_app', 'urnietfparamsscimschemasoracleidcsextensionkerberos_realm_app', 'urnietfparamsscimschemasoracleidcsextensionmanagedapp_app', 'urnietfparamsscimschemasoracleidcsextensionmulticloud_service_app_app', 'urnietfparamsscimschemasoracleidcsextensionopc_service_app', 'urnietfparamsscimschemasoracleidcsextensionradius_app_app', 'urnietfparamsscimschemasoracleidcsextensionrequestable_app', 'urnietfparamsscimschemasoracleidcsextensionsaml_service_provider_app', 'urnietfparamsscimschemasoracleidcsextensionweb_tier_policy_app'])
@identitydomains_cli.app_group.command(name=identitydomains_cli.put_app.name, help=identitydomains_cli.put_app.help)
@cli_util.option('--ext-form-fill-app-template-app-template', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-oci-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-dbcs-app', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-enterprise-app-app', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-form-fill-app-app', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-kerberos-realm-app', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-managedapp-app', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-multicloud-service-app-app', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-opc-service-app', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-radius-app-app', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-requestable-app', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-saml-service-provider-app', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ext-web-tier-policy-app', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'schemas': {'module': 'identity_domains', 'class': 'list[string]'}, 'meta': {'module': 'identity_domains', 'class': 'Meta'}, 'idcs-created-by': {'module': 'identity_domains', 'class': 'IdcsCreatedBy'}, 'idcs-last-modified-by': {'module': 'identity_domains', 'class': 'IdcsLastModifiedBy'}, 'tags': {'module': 'identity_domains', 'class': 'list[Tags]'}, 'delegated-service-names': {'module': 'identity_domains', 'class': 'list[string]'}, 'redirect-uris': {'module': 'identity_domains', 'class': 'list[string]'}, 'post-logout-redirect-uris': {'module': 'identity_domains', 'class': 'list[string]'}, 'allowed-grants': {'module': 'identity_domains', 'class': 'list[string]'}, 'secondary-audiences': {'module': 'identity_domains', 'class': 'list[string]'}, 'radius-policy': {'module': 'identity_domains', 'class': 'AppRadiusPolicy'}, 'apps-network-perimeters': {'module': 'identity_domains', 'class': 'list[AppAppsNetworkPerimeters]'}, 'cloud-control-properties': {'module': 'identity_domains', 'class': 'list[AppCloudControlProperties]'}, 'editable-attributes': {'module': 'identity_domains', 'class': 'list[AppEditableAttributes]'}, 'terms-of-use': {'module': 'identity_domains', 'class': 'AppTermsOfUse'}, 'protectable-secondary-audiences': {'module': 'identity_domains', 'class': 'list[AppProtectableSecondaryAudiences]'}, 'idp-policy': {'module': 'identity_domains', 'class': 'AppIdpPolicy'}, 'allowed-tags': {'module': 'identity_domains', 'class': 'list[AppAllowedTags]'}, 'app-signon-policy': {'module': 'identity_domains', 'class': 'AppAppSignonPolicy'}, 'trust-policies': {'module': 'identity_domains', 'class': 'list[AppTrustPolicies]'}, 'signon-policy': {'module': 'identity_domains', 'class': 'AppSignonPolicy'}, 'identity-providers': {'module': 'identity_domains', 'class': 'list[AppIdentityProviders]'}, 'accounts': {'module': 'identity_domains', 'class': 'list[AppAccounts]'}, 'grants': {'module': 'identity_domains', 'class': 'list[AppGrants]'}, 'service-params': {'module': 'identity_domains', 'class': 'list[AppServiceParams]'}, 'attr-rendering-metadata': {'module': 'identity_domains', 'class': 'list[AppAttrRenderingMetadata]'}, 'based-on-template': {'module': 'identity_domains', 'class': 'AppBasedOnTemplate'}, 'granted-app-roles': {'module': 'identity_domains', 'class': 'list[AppGrantedAppRoles]'}, 'saml-service-provider': {'module': 'identity_domains', 'class': 'AppSamlServiceProvider'}, 'allowed-scopes': {'module': 'identity_domains', 'class': 'list[AppAllowedScopes]'}, 'certificates': {'module': 'identity_domains', 'class': 'list[AppCertificates]'}, 'alias-apps': {'module': 'identity_domains', 'class': 'list[AppAliasApps]'}, 'as-opc-service': {'module': 'identity_domains', 'class': 'AppAsOPCService'}, 'admin-roles': {'module': 'identity_domains', 'class': 'list[AppAdminRoles]'}, 'user-roles': {'module': 'identity_domains', 'class': 'list[AppUserRoles]'}, 'scopes': {'module': 'identity_domains', 'class': 'list[AppScopes]'}, 'urnietfparamsscimschemasoracleidcsextensionradius-app-app': {'module': 'identity_domains', 'class': 'AppExtensionRadiusAppApp'}, 'urnietfparamsscimschemasoracleidcsextensionsaml-service-provider-app': {'module': 'identity_domains', 'class': 'AppExtensionSamlServiceProviderApp'}, 'urnietfparamsscimschemasoracleidcsextensionweb-tier-policy-app': {'module': 'identity_domains', 'class': 'AppExtensionWebTierPolicyApp'}, 'urnietfparamsscimschemasoracleidcsextensionmanagedapp-app': {'module': 'identity_domains', 'class': 'AppExtensionManagedappApp'}, 'urnietfparamsscimschemasoracleidcsextensionform-fill-app-template-app-template': {'module': 'identity_domains', 'class': 'AppExtensionFormFillAppTemplateAppTemplate'}, 'urnietfparamsscimschemasoracleidcsextensionopc-service-app': {'module': 'identity_domains', 'class': 'AppExtensionOpcServiceApp'}, 'urnietfparamsscimschemasoracleidcsextensionkerberos-realm-app': {'module': 'identity_domains', 'class': 'AppExtensionKerberosRealmApp'}, 'urnietfparamsscimschemasoracleidcsextensionrequestable-app': {'module': 'identity_domains', 'class': 'AppExtensionRequestableApp'}, 'urnietfparamsscimschemasoracleidcsextensionform-fill-app-app': {'module': 'identity_domains', 'class': 'AppExtensionFormFillAppApp'}, 'urnietfparamsscimschemasoracleidcsextensiondbcs-app': {'module': 'identity_domains', 'class': 'AppExtensionDbcsApp'}, 'urnietfparamsscimschemasoracleidcsextensionenterprise-app-app': {'module': 'identity_domains', 'class': 'AppExtensionEnterpriseAppApp'}, 'urnietfparamsscimschemasoracleidcsextension-oci-tags': {'module': 'identity_domains', 'class': 'ExtensionOCITags'}, 'urnietfparamsscimschemasoracleidcsextensionmulticloud-service-app-app': {'module': 'identity_domains', 'class': 'AppExtensionMulticloudServiceAppApp'}}, output_type={'module': 'identity_domains', 'class': 'App'})
@cli_util.wrap_exceptions
def put_app_extended(ctx, **kwargs):

    if 'ext_form_fill_app_template_app_template' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionform_fill_app_template_app_template'] = kwargs['ext_form_fill_app_template_app_template']
        kwargs.pop('ext_form_fill_app_template_app_template')
    if 'ext_oci_tags' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextension_oci_tags'] = kwargs['ext_oci_tags']
        kwargs.pop('ext_oci_tags')
    if 'ext_dbcs_app' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensiondbcs_app'] = kwargs['ext_dbcs_app']
        kwargs.pop('ext_dbcs_app')
    if 'ext_enterprise_app_app' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionenterprise_app_app'] = kwargs['ext_enterprise_app_app']
        kwargs.pop('ext_enterprise_app_app')
    if 'ext_form_fill_app_app' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionform_fill_app_app'] = kwargs['ext_form_fill_app_app']
        kwargs.pop('ext_form_fill_app_app')
    if 'ext_kerberos_realm_app' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionkerberos_realm_app'] = kwargs['ext_kerberos_realm_app']
        kwargs.pop('ext_kerberos_realm_app')
    if 'ext_managedapp_app' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionmanagedapp_app'] = kwargs['ext_managedapp_app']
        kwargs.pop('ext_managedapp_app')
    if 'ext_multicloud_service_app_app' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionmulticloud_service_app_app'] = kwargs['ext_multicloud_service_app_app']
        kwargs.pop('ext_multicloud_service_app_app')
    if 'ext_opc_service_app' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionopc_service_app'] = kwargs['ext_opc_service_app']
        kwargs.pop('ext_opc_service_app')
    if 'ext_radius_app_app' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionradius_app_app'] = kwargs['ext_radius_app_app']
        kwargs.pop('ext_radius_app_app')
    if 'ext_requestable_app' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionrequestable_app'] = kwargs['ext_requestable_app']
        kwargs.pop('ext_requestable_app')
    if 'ext_saml_service_provider_app' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionsaml_service_provider_app'] = kwargs['ext_saml_service_provider_app']
        kwargs.pop('ext_saml_service_provider_app')
    if 'ext_web_tier_policy_app' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionweb_tier_policy_app'] = kwargs['ext_web_tier_policy_app']
        kwargs.pop('ext_web_tier_policy_app')

    ctx.invoke(identitydomains_cli.put_app, **kwargs)


@cli_util.copy_params_from_generated_command(identitydomains_cli.create_api_key, params_to_exclude=['urnietfparamsscimschemasoracleidcsextensionself_change_user'])
@identitydomains_cli.api_key_group.command(name=identitydomains_cli.create_api_key.name, help=identitydomains_cli.create_api_key.help)
@cli_util.option('--ext-self-change-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'schemas': {'module': 'identity_domains', 'class': 'list[string]'}, 'meta': {'module': 'identity_domains', 'class': 'Meta'}, 'idcs-created-by': {'module': 'identity_domains', 'class': 'IdcsCreatedBy'}, 'idcs-last-modified-by': {'module': 'identity_domains', 'class': 'IdcsLastModifiedBy'}, 'tags': {'module': 'identity_domains', 'class': 'list[Tags]'}, 'user': {'module': 'identity_domains', 'class': 'ApiKeyUser'}, 'urnietfparamsscimschemasoracleidcsextensionself-change-user': {'module': 'identity_domains', 'class': 'ExtensionSelfChangeUser'}}, output_type={'module': 'identity_domains', 'class': 'ApiKey'})
@cli_util.wrap_exceptions
def create_api_key_extended(ctx, **kwargs):

    if 'ext_self_change_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionself_change_user'] = kwargs['ext_self_change_user']
        kwargs.pop('ext_self_change_user')

    ctx.invoke(identitydomains_cli.create_api_key, **kwargs)


@cli_util.copy_params_from_generated_command(identitydomains_cli.create_auth_token, params_to_exclude=['urnietfparamsscimschemasoracleidcsextensionself_change_user'])
@identitydomains_cli.auth_token_group.command(name=identitydomains_cli.create_auth_token.name, help=identitydomains_cli.create_auth_token.help)
@cli_util.option('--ext-self-change-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'schemas': {'module': 'identity_domains', 'class': 'list[string]'}, 'meta': {'module': 'identity_domains', 'class': 'Meta'}, 'idcs-created-by': {'module': 'identity_domains', 'class': 'IdcsCreatedBy'}, 'idcs-last-modified-by': {'module': 'identity_domains', 'class': 'IdcsLastModifiedBy'}, 'tags': {'module': 'identity_domains', 'class': 'list[Tags]'}, 'user': {'module': 'identity_domains', 'class': 'AuthTokenUser'}, 'urnietfparamsscimschemasoracleidcsextensionself-change-user': {'module': 'identity_domains', 'class': 'ExtensionSelfChangeUser'}}, output_type={'module': 'identity_domains', 'class': 'AuthToken'})
@cli_util.wrap_exceptions
def create_auth_token_extended(ctx, **kwargs):

    if 'ext_self_change_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionself_change_user'] = kwargs['ext_self_change_user']
        kwargs.pop('ext_self_change_user')

    ctx.invoke(identitydomains_cli.create_auth_token, **kwargs)


@cli_util.copy_params_from_generated_command(identitydomains_cli.create_customer_secret_key, params_to_exclude=['urnietfparamsscimschemasoracleidcsextensionself_change_user'])
@identitydomains_cli.customer_secret_key_group.command(name=identitydomains_cli.create_customer_secret_key.name, help=identitydomains_cli.create_customer_secret_key.help)
@cli_util.option('--ext-self-change-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'schemas': {'module': 'identity_domains', 'class': 'list[string]'}, 'meta': {'module': 'identity_domains', 'class': 'Meta'}, 'idcs-created-by': {'module': 'identity_domains', 'class': 'IdcsCreatedBy'}, 'idcs-last-modified-by': {'module': 'identity_domains', 'class': 'IdcsLastModifiedBy'}, 'tags': {'module': 'identity_domains', 'class': 'list[Tags]'}, 'user': {'module': 'identity_domains', 'class': 'CustomerSecretKeyUser'}, 'urnietfparamsscimschemasoracleidcsextensionself-change-user': {'module': 'identity_domains', 'class': 'ExtensionSelfChangeUser'}}, output_type={'module': 'identity_domains', 'class': 'CustomerSecretKey'})
@cli_util.wrap_exceptions
def create_customer_secret_key_extended(ctx, **kwargs):

    if 'ext_self_change_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionself_change_user'] = kwargs['ext_self_change_user']
        kwargs.pop('ext_self_change_user')

    ctx.invoke(identitydomains_cli.create_customer_secret_key, **kwargs)


@cli_util.copy_params_from_generated_command(identitydomains_cli.create_o_auth2_client_credential, params_to_exclude=['urnietfparamsscimschemasoracleidcsextensionself_change_user'])
@identitydomains_cli.o_auth2_client_credential_group.command(name=identitydomains_cli.create_o_auth2_client_credential.name, help=identitydomains_cli.create_o_auth2_client_credential.help)
@cli_util.option('--ext-self-change-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'schemas': {'module': 'identity_domains', 'class': 'list[string]'}, 'meta': {'module': 'identity_domains', 'class': 'Meta'}, 'idcs-created-by': {'module': 'identity_domains', 'class': 'IdcsCreatedBy'}, 'idcs-last-modified-by': {'module': 'identity_domains', 'class': 'IdcsLastModifiedBy'}, 'tags': {'module': 'identity_domains', 'class': 'list[Tags]'}, 'scopes': {'module': 'identity_domains', 'class': 'list[OAuth2ClientCredentialScopes]'}, 'user': {'module': 'identity_domains', 'class': 'OAuth2ClientCredentialUser'}, 'urnietfparamsscimschemasoracleidcsextensionself-change-user': {'module': 'identity_domains', 'class': 'ExtensionSelfChangeUser'}}, output_type={'module': 'identity_domains', 'class': 'OAuth2ClientCredential'})
@cli_util.wrap_exceptions
def create_o_auth2_client_credential_extended(ctx, **kwargs):

    if 'ext_self_change_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionself_change_user'] = kwargs['ext_self_change_user']
        kwargs.pop('ext_self_change_user')

    ctx.invoke(identitydomains_cli.create_o_auth2_client_credential, **kwargs)


@cli_util.copy_params_from_generated_command(identitydomains_cli.create_smtp_credential, params_to_exclude=['urnietfparamsscimschemasoracleidcsextensionself_change_user'])
@identitydomains_cli.smtp_credential_group.command(name=identitydomains_cli.create_smtp_credential.name, help=identitydomains_cli.create_smtp_credential.help)
@cli_util.option('--ext-self-change-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'schemas': {'module': 'identity_domains', 'class': 'list[string]'}, 'meta': {'module': 'identity_domains', 'class': 'Meta'}, 'idcs-created-by': {'module': 'identity_domains', 'class': 'IdcsCreatedBy'}, 'idcs-last-modified-by': {'module': 'identity_domains', 'class': 'IdcsLastModifiedBy'}, 'tags': {'module': 'identity_domains', 'class': 'list[Tags]'}, 'user': {'module': 'identity_domains', 'class': 'SmtpCredentialUser'}, 'urnietfparamsscimschemasoracleidcsextensionself-change-user': {'module': 'identity_domains', 'class': 'ExtensionSelfChangeUser'}}, output_type={'module': 'identity_domains', 'class': 'SmtpCredential'})
@cli_util.wrap_exceptions
def create_smtp_credential_extended(ctx, **kwargs):

    if 'ext_self_change_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionself_change_user'] = kwargs['ext_self_change_user']
        kwargs.pop('ext_self_change_user')

    ctx.invoke(identitydomains_cli.create_smtp_credential, **kwargs)


@cli_util.copy_params_from_generated_command(identitydomains_cli.put_user_capabilities_changer, params_to_exclude=['urnietfparamsscimschemasoracleidcsextensionself_change_user'])
@identitydomains_cli.user_capabilities_changer_group.command(name=identitydomains_cli.put_user_capabilities_changer.name, help=identitydomains_cli.put_user_capabilities_changer.help)
@cli_util.option('--ext-self-change-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'schemas': {'module': 'identity_domains', 'class': 'list[string]'}, 'meta': {'module': 'identity_domains', 'class': 'Meta'}, 'idcs-created-by': {'module': 'identity_domains', 'class': 'IdcsCreatedBy'}, 'idcs-last-modified-by': {'module': 'identity_domains', 'class': 'IdcsLastModifiedBy'}, 'tags': {'module': 'identity_domains', 'class': 'list[Tags]'}, 'urnietfparamsscimschemasoracleidcsextensionself-change-user': {'module': 'identity_domains', 'class': 'ExtensionSelfChangeUser'}}, output_type={'module': 'identity_domains', 'class': 'UserCapabilitiesChanger'})
@cli_util.wrap_exceptions
def put_user_capabilities_changer_extended(ctx, **kwargs):

    if 'ext_self_change_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionself_change_user'] = kwargs['ext_self_change_user']
        kwargs.pop('ext_self_change_user')

    ctx.invoke(identitydomains_cli.put_user_capabilities_changer, **kwargs)


@cli_util.copy_params_from_generated_command(identitydomains_cli.create_user_db_credential, params_to_exclude=['urnietfparamsscimschemasoracleidcsextensionself_change_user'])
@identitydomains_cli.user_db_credential_group.command(name=identitydomains_cli.create_user_db_credential.name, help=identitydomains_cli.create_user_db_credential.help)
@cli_util.option('--ext-self-change-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'schemas': {'module': 'identity_domains', 'class': 'list[string]'}, 'meta': {'module': 'identity_domains', 'class': 'Meta'}, 'idcs-created-by': {'module': 'identity_domains', 'class': 'IdcsCreatedBy'}, 'idcs-last-modified-by': {'module': 'identity_domains', 'class': 'IdcsLastModifiedBy'}, 'tags': {'module': 'identity_domains', 'class': 'list[Tags]'}, 'user': {'module': 'identity_domains', 'class': 'UserDbCredentialsUser'}, 'urnietfparamsscimschemasoracleidcsextensionself-change-user': {'module': 'identity_domains', 'class': 'ExtensionSelfChangeUser'}}, output_type={'module': 'identity_domains', 'class': 'UserDbCredential'})
@cli_util.wrap_exceptions
def create_user_db_credential_extended(ctx, **kwargs):

    if 'ext_self_change_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionself_change_user'] = kwargs['ext_self_change_user']
        kwargs.pop('ext_self_change_user')

    ctx.invoke(identitydomains_cli.create_user_db_credential, **kwargs)


@cli_util.copy_params_from_generated_command(identitydomains_cli.put_user_password_changer, params_to_exclude=['urnietfparamsscimschemasoracleidcsextensionself_change_user'])
@identitydomains_cli.user_password_changer_group.command(name=identitydomains_cli.put_user_password_changer.name, help=identitydomains_cli.put_user_password_changer.help)
@cli_util.option('--ext-self-change-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'schemas': {'module': 'identity_domains', 'class': 'list[string]'}, 'meta': {'module': 'identity_domains', 'class': 'Meta'}, 'idcs-created-by': {'module': 'identity_domains', 'class': 'IdcsCreatedBy'}, 'idcs-last-modified-by': {'module': 'identity_domains', 'class': 'IdcsLastModifiedBy'}, 'tags': {'module': 'identity_domains', 'class': 'list[Tags]'}, 'urnietfparamsscimschemasoracleidcsextensionself-change-user': {'module': 'identity_domains', 'class': 'ExtensionSelfChangeUser'}}, output_type={'module': 'identity_domains', 'class': 'UserPasswordChanger'})
@cli_util.wrap_exceptions
def put_user_password_changer_extended(ctx, **kwargs):

    if 'ext_self_change_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionself_change_user'] = kwargs['ext_self_change_user']
        kwargs.pop('ext_self_change_user')

    ctx.invoke(identitydomains_cli.put_user_password_changer, **kwargs)


@cli_util.copy_params_from_generated_command(identitydomains_cli.put_user_password_resetter, params_to_exclude=['urnietfparamsscimschemasoracleidcsextensionself_change_user'])
@identitydomains_cli.user_password_resetter_group.command(name=identitydomains_cli.put_user_password_resetter.name, help=identitydomains_cli.put_user_password_resetter.help)
@cli_util.option('--ext-self-change-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'schemas': {'module': 'identity_domains', 'class': 'list[string]'}, 'meta': {'module': 'identity_domains', 'class': 'Meta'}, 'idcs-created-by': {'module': 'identity_domains', 'class': 'IdcsCreatedBy'}, 'idcs-last-modified-by': {'module': 'identity_domains', 'class': 'IdcsLastModifiedBy'}, 'tags': {'module': 'identity_domains', 'class': 'list[Tags]'}, 'user-token': {'module': 'identity_domains', 'class': 'UserPasswordResetterUserToken'}, 'urnietfparamsscimschemasoracleidcsextensionself-change-user': {'module': 'identity_domains', 'class': 'ExtensionSelfChangeUser'}}, output_type={'module': 'identity_domains', 'class': 'UserPasswordResetter'})
@cli_util.wrap_exceptions
def put_user_password_resetter_extended(ctx, **kwargs):

    if 'ext_self_change_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionself_change_user'] = kwargs['ext_self_change_user']
        kwargs.pop('ext_self_change_user')

    ctx.invoke(identitydomains_cli.put_user_password_resetter, **kwargs)


@cli_util.copy_params_from_generated_command(identitydomains_cli.put_user_status_changer, params_to_exclude=['urnietfparamsscimschemasoracleidcsextensionself_change_user'])
@identitydomains_cli.user_status_changer_group.command(name=identitydomains_cli.put_user_status_changer.name, help=identitydomains_cli.put_user_status_changer.help)
@cli_util.option('--ext-self-change-user', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'schemas': {'module': 'identity_domains', 'class': 'list[string]'}, 'meta': {'module': 'identity_domains', 'class': 'Meta'}, 'idcs-created-by': {'module': 'identity_domains', 'class': 'IdcsCreatedBy'}, 'idcs-last-modified-by': {'module': 'identity_domains', 'class': 'IdcsLastModifiedBy'}, 'tags': {'module': 'identity_domains', 'class': 'list[Tags]'}, 'urnietfparamsscimschemasoracleidcsextensionself-change-user': {'module': 'identity_domains', 'class': 'ExtensionSelfChangeUser'}}, output_type={'module': 'identity_domains', 'class': 'UserStatusChanger'})
@cli_util.wrap_exceptions
def put_user_status_changer_extended(ctx, **kwargs):

    if 'ext_self_change_user' in kwargs:
        kwargs['urnietfparamsscimschemasoracleidcsextensionself_change_user'] = kwargs['ext_self_change_user']
        kwargs.pop('ext_self_change_user')

    ctx.invoke(identitydomains_cli.put_user_status_changer, **kwargs)


# Using list_call_get_up_to_limit_multiple_keys and list_call_get_all_results_multiple_keys
@cli_util.copy_params_from_generated_command(identitydomains_cli.list_apps)
@identitydomains_cli.apps_group.command(name=cli_util.override('list_apps.command_name', 'list'), help=identitydomains_cli.list_apps.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity_domains', 'class': 'Apps'})
@cli_util.wrap_exceptions
def list_apps_extended(ctx, from_json, all_pages, page_size, filter, sort_by, sort_order, start_index, count, attributes, attribute_sets, authorization, resource_type_schema_version, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if filter is not None:
        kwargs['filter'] = filter
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if start_index is not None:
        kwargs['start_index'] = start_index
    if count is not None:
        kwargs['count'] = count
    if attributes is not None:
        kwargs['attributes'] = attributes
    if attribute_sets is not None and len(attribute_sets) > 0:
        kwargs['attribute_sets'] = attribute_sets
    if authorization is not None:
        kwargs['authorization'] = authorization
    if resource_type_schema_version is not None:
        kwargs['resource_type_schema_version'] = resource_type_schema_version
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    client = cli_util.build_client('identity_domains', 'identity_domains', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results_multiple_keys(
            client.list_apps,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit_multiple_keys(
            client.list_apps,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_apps(
            **kwargs
        )
    cli_util.render_response(result, ctx)


# Using list_call_get_up_to_limit_multiple_keys and list_call_get_all_results_multiple_keys
@cli_util.copy_params_from_generated_command(identitydomains_cli.list_groups)
@identitydomains_cli.groups_group.command(name=cli_util.override('list_groups.command_name', 'list'), help=identitydomains_cli.list_groups.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity_domains', 'class': 'Groups'})
@cli_util.wrap_exceptions
def list_groups_extended(ctx, from_json, all_pages, page_size, filter, sort_by, sort_order, start_index, count, attributes, attribute_sets, authorization, resource_type_schema_version, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if filter is not None:
        kwargs['filter'] = filter
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if start_index is not None:
        kwargs['start_index'] = start_index
    if count is not None:
        kwargs['count'] = count
    if attributes is not None:
        kwargs['attributes'] = attributes
    if attribute_sets is not None and len(attribute_sets) > 0:
        kwargs['attribute_sets'] = attribute_sets
    if authorization is not None:
        kwargs['authorization'] = authorization
    if resource_type_schema_version is not None:
        kwargs['resource_type_schema_version'] = resource_type_schema_version
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    client = cli_util.build_client('identity_domains', 'identity_domains', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results_multiple_keys(
            client.list_groups,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit_multiple_keys(
            client.list_groups,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_groups(
            **kwargs
        )
    cli_util.render_response(result, ctx)


# Using list_call_get_up_to_limit_multiple_keys and list_call_get_all_results_multiple_keys
@cli_util.copy_params_from_generated_command(identitydomains_cli.list_users)
@identitydomains_cli.users_group.command(name=cli_util.override('list_users.command_name', 'list'), help=identitydomains_cli.list_users.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity_domains', 'class': 'Users'})
@cli_util.wrap_exceptions
def list_users_extended(ctx, from_json, all_pages, page_size, filter, sort_by, sort_order, start_index, count, attributes, attribute_sets, authorization, resource_type_schema_version, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if filter is not None:
        kwargs['filter'] = filter
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if start_index is not None:
        kwargs['start_index'] = start_index
    if count is not None:
        kwargs['count'] = count
    if attributes is not None:
        kwargs['attributes'] = attributes
    if attribute_sets is not None and len(attribute_sets) > 0:
        kwargs['attribute_sets'] = attribute_sets
    if authorization is not None:
        kwargs['authorization'] = authorization
    if resource_type_schema_version is not None:
        kwargs['resource_type_schema_version'] = resource_type_schema_version
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    client = cli_util.build_client('identity_domains', 'identity_domains', ctx)

    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results_multiple_keys(
            client.list_users,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit_multiple_keys(
            client.list_users,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_users(
            **kwargs
        )
    cli_util.render_response(result, ctx)
