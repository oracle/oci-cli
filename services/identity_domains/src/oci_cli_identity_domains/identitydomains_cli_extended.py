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


@cli_util.copy_params_from_generated_command(identitydomains_cli.create_group, params_to_exclude=['urnietfparamsscimschemasoracleidcsextensiondbcs_group', 'urnietfparamsscimschemasoracleidcsextensiondynamic_group', 'urnietfparamsscimschemasoracleidcsextensiongroup_group', 'urnietfparamsscimschemasoracleidcsextensionposix_group', 'urnietfparamsscimschemasoracleidcsextensionrequestable_group'])
@identitydomains_cli.group_group.command(name=identitydomains_cli.create_group.name, help=identitydomains_cli.create_group.help)
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


@cli_util.copy_params_from_generated_command(identitydomains_cli.put_group, params_to_exclude=['urnietfparamsscimschemasoracleidcsextensiondbcs_group', 'urnietfparamsscimschemasoracleidcsextensiondynamic_group', 'urnietfparamsscimschemasoracleidcsextensiongroup_group', 'urnietfparamsscimschemasoracleidcsextensionposix_group', 'urnietfparamsscimschemasoracleidcsextensionrequestable_group'])
@identitydomains_cli.group_group.command(name=identitydomains_cli.put_group.name, help=identitydomains_cli.put_group.help)
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
