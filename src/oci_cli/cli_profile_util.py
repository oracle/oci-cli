# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.
#
# This software is dual-licensed to you under the Universal Permissive License
# (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl and Apache License
# 2.0 as shown at https://www.apache.org/licenses/LICENSE-2.0. You may choose
# either license.
#
# If you elect to accept the software under the Apache License, Version 2.0,
# the following applies:
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import configparser
import os

from oci import config as oci_config
from oci.config import DEFAULT_PROFILE

from oci_cli import cli_constants


AUTH_TYPE_UNKNOWN = 'unknown'

FINDING_SEVERITY_ERROR = 'error'
FINDING_SEVERITY_WARNING = 'warning'
FINDING_SEVERITY_INFO = 'info'


class ProfileConfigError(Exception):
    pass


def load_config(config_file):
    resolved_config_file = oci_config._get_config_path_with_fallback(config_file)
    parser = configparser.ConfigParser(interpolation=None)

    try:
        read_files = parser.read(resolved_config_file)
    except configparser.Error as error:
        raise ProfileConfigError(
            "Could not read config file {}: {}".format(resolved_config_file, error)
        )

    if not read_files:
        raise ProfileConfigError("Config file not found: {}".format(resolved_config_file))

    return parser, resolved_config_file


def list_profiles(config_file, active_profile=None):
    config, expanded_config_file = load_config(config_file)
    return [
        inspect_profile_from_config(
            config,
            expanded_config_file,
            profile_name,
            active_profile=active_profile
        )
        for profile_name in list_profile_names(config)
    ]


def get_current_profile(config_file, active_profile):
    config, expanded_config_file = load_config(config_file)

    if not profile_exists(config, active_profile):
        raise ProfileConfigError(
            "Profile {} not found in config file {}".format(active_profile, expanded_config_file)
        )

    return inspect_profile_from_config(
        config,
        expanded_config_file,
        active_profile,
        active_profile=active_profile
    )


def diagnose_profile(config_file, active_profile, region=None, auth=None, env=None):
    if env is None:
        env = os.environ
    config, expanded_config_file = load_config(config_file)
    findings = []

    if is_config_fallback_used(config_file, expanded_config_file):
        add_finding(
            findings,
            FINDING_SEVERITY_INFO,
            'config_path_fallback_used',
            'Using fallback config path {} because the default config path was not used.'.format(expanded_config_file),
            path=expanded_config_file
        )

    if not profile_exists(config, active_profile):
        add_finding(
            findings,
            FINDING_SEVERITY_ERROR,
            'missing_profile',
            "Profile '{}' does not exist in config file {}.".format(active_profile, expanded_config_file)
        )
        return build_diagnosis(
            active_profile,
            expanded_config_file,
            AUTH_TYPE_UNKNOWN,
            get_effective_auth_type(auth, env),
            None,
            get_effective_region(region, None, env),
            findings
        )

    profile = inspect_profile_from_config(config, expanded_config_file, active_profile, active_profile=active_profile)
    values = get_profile_values(config, active_profile)
    effective_auth_type = get_effective_auth_type(auth, env)
    effective_region = get_effective_region(region, profile['region'], env)

    add_unknown_auth_type_finding(findings, profile)
    add_missing_required_field_findings(findings, profile, values, effective_auth_type, effective_region)
    add_missing_credential_file_findings(findings, profile)
    add_ambiguous_auth_findings(findings, profile, values)
    add_region_override_finding(findings, profile, region, effective_region, env)
    add_auth_override_finding(findings, profile, auth, effective_auth_type, env)

    return build_diagnosis(
        profile['name'],
        profile['config_file'],
        profile['inferred_auth_type'],
        effective_auth_type,
        profile['region'],
        effective_region,
        findings,
        profile=profile
    )


def list_profile_names(config):
    profile_names = []
    if config.defaults():
        profile_names.append(DEFAULT_PROFILE)
    profile_names.extend(config.sections())
    return profile_names


def profile_exists(config, profile_name):
    if profile_name == DEFAULT_PROFILE:
        return bool(config.defaults())
    return config.has_section(profile_name)


def inspect_profile_from_config(config, expanded_config_file, profile_name, active_profile=None):
    values = get_profile_values(config, profile_name)
    inferred_auth_type = infer_auth_type(values)

    key_file_info = get_file_info(values, 'key_file')
    security_token_file_info = get_file_info(values, 'security_token_file')
    delegation_token_file_info = get_file_info(values, 'delegation_token_file')

    return {
        'name': profile_name,
        'is_active': active_profile == profile_name,
        'config_file': expanded_config_file,
        'region': values.get('region'),
        'tenancy': values.get('tenancy'),
        'user': values.get('user'),
        'fingerprint': values.get('fingerprint'),
        'inferred_auth_type': inferred_auth_type,
        'key_file': key_file_info,
        'security_token_file': security_token_file_info,
        'delegation_token_file': delegation_token_file_info
    }


def get_profile_values(config, profile_name):
    if profile_name == DEFAULT_PROFILE:
        items = config.defaults().items()
    else:
        items = config[profile_name].items()

    return {
        key: value
        for key, value in items
        if key not in ('pass_phrase', 'passphrase')
    }


def infer_auth_type(values):
    if values.get('security_token_file'):
        return cli_constants.OCI_CLI_AUTH_SESSION_TOKEN
    if values.get('delegation_token_file'):
        return cli_constants.OCI_CLI_AUTH_INSTANCE_OBO_USER
    if values.get('key_file') or values.get('fingerprint') or values.get('user'):
        return cli_constants.OCI_CLI_AUTH_API_KEY
    return AUTH_TYPE_UNKNOWN


def get_file_info(profile_values, file_config_key):
    configured_path = profile_values.get(file_config_key)
    if not configured_path:
        return {
            'path': None,
            'expanded_path': None,
            'exists': None
        }

    expanded_path = expand_user_path(configured_path)
    return {
        'path': configured_path,
        'expanded_path': expanded_path,
        'exists': os.path.isfile(expanded_path)
    }


def expand_user_path(path):
    return os.path.expanduser(path)


def is_config_fallback_used(config_file, expanded_config_file):
    requested_path = os.path.abspath(os.path.expanduser(config_file))
    default_path = os.path.abspath(os.path.expanduser(oci_config.DEFAULT_LOCATION))
    fallback_path = os.path.abspath(os.path.expanduser(oci_config.FALLBACK_DEFAULT_LOCATION))
    resolved_path = os.path.abspath(os.path.expanduser(expanded_config_file))
    return requested_path == default_path and resolved_path == fallback_path


def get_effective_auth_type(auth, env):
    if auth:
        return auth
    env_auth = env.get(cli_constants.OCI_CLI_AUTH_ENV_VAR)
    if env_auth:
        return env_auth
    return cli_constants.OCI_CLI_AUTH_API_KEY


def get_effective_region(region, profile_region, env):
    if region:
        return region
    env_region = env.get(cli_constants.OCI_CLI_REGION_ENV_VAR)
    if env_region:
        return env_region
    return profile_region


def add_missing_credential_file_findings(findings, profile):
    for field_name in ['key_file', 'security_token_file', 'delegation_token_file']:
        file_info = profile[field_name]
        if not file_info.get('path'):
            continue
        if not file_info.get('exists'):
            add_finding(
                findings,
                FINDING_SEVERITY_ERROR,
                'missing_credential_file',
                "Profile '{}' references {} that does not exist: {}".format(
                    profile['name'],
                    field_name,
                    file_info.get('expanded_path')
                ),
                field=field_name,
                path=file_info.get('expanded_path')
            )


def add_unknown_auth_type_finding(findings, profile):
    if profile['inferred_auth_type'] == AUTH_TYPE_UNKNOWN:
        add_finding(
            findings,
            FINDING_SEVERITY_ERROR,
            'unknown_auth_type',
            "Profile '{}' does not have enough local fields to infer auth type.".format(profile['name'])
        )


def add_missing_required_field_findings(findings, profile, values, effective_auth_type, effective_region):
    if effective_auth_type == cli_constants.OCI_CLI_AUTH_API_KEY:
        required_fields = ['user', 'tenancy', 'fingerprint', 'key_file']
    elif effective_auth_type == cli_constants.OCI_CLI_AUTH_SESSION_TOKEN:
        required_fields = ['key_file', 'security_token_file']
    elif effective_auth_type == cli_constants.OCI_CLI_AUTH_INSTANCE_OBO_USER:
        required_fields = ['delegation_token_file']
    else:
        required_fields = []

    for field_name in required_fields:
        if not values.get(field_name):
            add_finding(
                findings,
                FINDING_SEVERITY_ERROR,
                'missing_required_field',
                "Profile '{}' is missing required field '{}' for auth type '{}'.".format(profile['name'], field_name, effective_auth_type),
                field=field_name
            )

    if not effective_region:
        add_finding(
            findings,
            FINDING_SEVERITY_ERROR,
            'region_missing',
            "Profile '{}' has no region and {} is not set.".format(profile['name'], cli_constants.OCI_CLI_REGION_ENV_VAR),
            field='region'
        )


def add_ambiguous_auth_findings(findings, profile, values):
    token_fields = [field_name for field_name in ['security_token_file', 'delegation_token_file'] if values.get(field_name)]
    api_key_only_fields = [field_name for field_name in ['user', 'fingerprint'] if values.get(field_name)]

    if len(token_fields) > 1:
        add_finding(
            findings,
            FINDING_SEVERITY_WARNING,
            'ambiguous_auth_config',
            "Profile '{}' has multiple token auth fields configured: {}.".format(profile['name'], ', '.join(token_fields)),
            field=','.join(token_fields)
        )

    if token_fields and api_key_only_fields:
        add_finding(
            findings,
            FINDING_SEVERITY_WARNING,
            'ambiguous_auth_config',
            "Profile '{}' mixes token auth fields with API-key-only fields: {}.".format(
                profile['name'],
                ', '.join(token_fields + api_key_only_fields)
            ),
            field=','.join(token_fields + api_key_only_fields)
        )


def add_region_override_finding(findings, profile, region, effective_region, env):
    if region:
        return

    env_region = env.get(cli_constants.OCI_CLI_REGION_ENV_VAR)
    if env_region and profile['region'] and env_region == effective_region and env_region != profile['region']:
        add_finding(
            findings,
            FINDING_SEVERITY_INFO,
            'region_overridden_by_env',
            "{} overrides profile region '{}' with '{}'.".format(cli_constants.OCI_CLI_REGION_ENV_VAR, profile['region'], env_region),
            field='region'
        )


def add_auth_override_finding(findings, profile, auth, effective_auth_type, env):
    if auth:
        return

    env_auth = env.get(cli_constants.OCI_CLI_AUTH_ENV_VAR)
    if (
        env_auth
        and env_auth == effective_auth_type
        and profile['inferred_auth_type'] != AUTH_TYPE_UNKNOWN
        and env_auth != profile['inferred_auth_type']
    ):
        add_finding(
            findings,
            FINDING_SEVERITY_WARNING,
            'auth_overridden_by_env',
            "{} overrides inferred profile auth type '{}' with '{}'.".format(
                cli_constants.OCI_CLI_AUTH_ENV_VAR,
                profile['inferred_auth_type'],
                env_auth
            ),
            field='auth'
        )


def build_diagnosis(
    profile_name,
    config_file,
    inferred_auth_type,
    effective_auth_type,
    profile_region,
    effective_region,
    findings,
    profile=None
):
    data = {
        'status': get_diagnosis_status(findings),
        'profile': profile_name,
        'active': profile['is_active'] if profile else False,
        'config-file': config_file,
        'region': profile_region,
        'effective-region': effective_region,
        'auth-type': inferred_auth_type,
        'effective-auth-type': effective_auth_type,
        'findings': findings
    }

    if profile:
        data.update({
            'tenancy': profile['tenancy'],
            'user': profile['user'],
            'fingerprint': profile['fingerprint'],
            'key-file-status': get_diagnose_file_status(profile['key_file']),
            'security-token-file-status': get_diagnose_file_status(profile['security_token_file']),
            'delegation-token-file-status': get_diagnose_file_status(profile['delegation_token_file'])
        })
    return data


def get_diagnosis_status(findings):
    severities = [finding['severity'] for finding in findings]
    if FINDING_SEVERITY_ERROR in severities:
        return 'error'
    if FINDING_SEVERITY_WARNING in severities:
        return 'warning'
    return 'ok'


def get_diagnose_file_status(file_info):
    if not file_info.get('path'):
        return 'not_configured'
    if not file_info.get('exists'):
        return 'missing'
    return 'present'


def add_finding(findings, severity, code, message, field=None, path=None):
    finding = {
        'severity': severity,
        'code': code,
        'message': message
    }
    if field:
        finding['field'] = field
    if path:
        finding['path'] = path
    findings.append(finding)
