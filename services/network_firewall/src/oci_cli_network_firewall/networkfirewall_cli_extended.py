# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.
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

import click

from services.network_firewall.src.oci_cli_network_firewall.generated import networkfirewall_cli
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types
import json


@cli_util.copy_params_from_generated_command(
    networkfirewall_cli.bulk_upload_applications,
    params_to_exclude=['bulk_upload_applications_details']
)
@networkfirewall_cli.application_group.command(
    name='bulk-upload',
    help=networkfirewall_cli.bulk_upload_applications.help
)
@cli_util.option(
    '--bulk-upload-applications-details',
    required=True,
    type=custom_types.CLI_COMPLEX_TYPE,
    help=u"""Request Details to bulk import applications for the Network Firewall Policy Resource."""
)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'bulk-upload-applications-details': {
            'module': 'network_firewall', 'class': 'list[CreateApplicationDetails]'
        }
    }
)
@json_skeleton_utils.get_cli_json_input_option(
    {'bulk-upload-applications-details': {
        'module': 'network_firewall', 'class': 'list[CreateAddressListDetails]'
    }}
)
@cli_util.wrap_exceptions
def upload_applications_extended(ctx, **kwargs):
    upload_file = cli_util.parse_json_parameter(
        "bulk_upload_applications_details",
        kwargs['bulk_upload_applications_details']
    )
    del kwargs['bulk_upload_applications_details']
    kwargs['bulk_upload_applications_details'] = json.dumps(upload_file)
    ctx.invoke(networkfirewall_cli.bulk_upload_applications, **kwargs)


@cli_util.copy_params_from_generated_command(
    networkfirewall_cli.bulk_upload_application_groups,
    params_to_exclude=['bulk_upload_application_groups_details']
)
@networkfirewall_cli.application_group_group.command(
    name='bulk-upload',
    help=networkfirewall_cli.bulk_upload_application_groups.help
)
@cli_util.option(
    '--bulk-upload-application-groups-details',
    required=True,
    type=custom_types.CLI_COMPLEX_TYPE,
    help=u"""Request Details to bulk import the application groups for the Network Firewall Policy resource."""
)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'bulk-upload-application-groups-details': {
            'module': 'network_firewall', 'class': 'list[CreateApplicationGroupDetails]'
        }
    }
)
@json_skeleton_utils.get_cli_json_input_option(
    {'bulk-upload-application-groups-details': {
        'module': 'network_firewall', 'class': 'list[CreateApplicationGroupDetails]'
    }}
)
@cli_util.wrap_exceptions
def upload_application_groups_extended(ctx, **kwargs):
    upload_file = cli_util.parse_json_parameter(
        "bulk_upload_application_groups_details",
        kwargs['bulk_upload_application_groups_details']
    )
    del kwargs['bulk_upload_application_groups_details']
    kwargs['bulk_upload_application_groups_details'] = json.dumps(upload_file)
    ctx.invoke(networkfirewall_cli.bulk_upload_application_groups, **kwargs)


@cli_util.copy_params_from_generated_command(
    networkfirewall_cli.bulk_upload_address_lists,
    params_to_exclude=['bulk_upload_address_lists_details']
)
@networkfirewall_cli.address_list_group.command(
    name='bulk-upload',
    help=networkfirewall_cli.bulk_upload_address_lists.help
)
@cli_util.option(
    '--bulk-upload-address-lists-details',
    required=True,
    type=custom_types.CLI_COMPLEX_TYPE,
    help=u"""Request Details to bulk import the address lists for the Network Firewall Policy resource."""
)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'bulk-upload-address-lists-details': {
            'module': 'network_firewall', 'class': 'list[CreateAddressListDetails]'
        }
    }
)
@json_skeleton_utils.get_cli_json_input_option(
    {'bulk-upload-address-lists-details': {
        'module': 'network_firewall', 'class': 'list[CreateAddressListDetails]'
    }}
)
@cli_util.wrap_exceptions
def upload_address_lists_extended(ctx, **kwargs):
    upload_file = cli_util.parse_json_parameter(
        "bulk_upload_address_lists_details",
        kwargs['bulk_upload_address_lists_details']
    )
    del kwargs['bulk_upload_address_lists_details']
    kwargs['bulk_upload_address_lists_details'] = json.dumps(upload_file)
    ctx.invoke(networkfirewall_cli.bulk_upload_address_lists, **kwargs)


@cli_util.copy_params_from_generated_command(
    networkfirewall_cli.bulk_upload_service_lists,
    params_to_exclude=['bulk_upload_service_lists_details']
)
@networkfirewall_cli.service_list_group.command(
    name='bulk-upload',
    help=networkfirewall_cli.bulk_upload_service_lists.help
)
@cli_util.option(
    '--bulk-upload-service-lists-details',
    required=True,
    type=custom_types.CLI_COMPLEX_TYPE,
    help=u"""Request Details to bulk import the service lists for the Network Firewall Policy resource."""
)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'bulk-upload-service-lists-details': {
            'module': 'network_firewall', 'class': 'list[CreateServiceListDetails]'
        }
    }
)
@json_skeleton_utils.get_cli_json_input_option(
    {'bulk-upload-service-lists-details': {
        'module': 'network_firewall', 'class': 'list[CreateServiceListDetails]'
    }}
)
@cli_util.wrap_exceptions
def upload_service_lists_extended(ctx, **kwargs):
    upload_file = cli_util.parse_json_parameter(
        "bulk_upload_service_lists_details",
        kwargs['bulk_upload_service_lists_details']
    )
    del kwargs['bulk_upload_service_lists_details']
    kwargs['bulk_upload_service_lists_details'] = json.dumps(upload_file)
    ctx.invoke(networkfirewall_cli.bulk_upload_service_lists, **kwargs)


@cli_util.copy_params_from_generated_command(
    networkfirewall_cli.bulk_upload_services,
    params_to_exclude=['bulk_upload_services_details']
)
@networkfirewall_cli.service_group.command(
    name='bulk-upload',
    help=networkfirewall_cli.bulk_upload_services.help
)
@cli_util.option(
    '--bulk-upload-services-details',
    required=True,
    type=custom_types.CLI_COMPLEX_TYPE,
    help=u"""Request Details to bulk import the services for the Network Firewall Policy resource."""
)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'bulk-upload-services-details': {
            'module': 'network_firewall', 'class': 'list[CreateServiceDetails]'
        }
    }
)
@json_skeleton_utils.get_cli_json_input_option(
    {'bulk-upload-services-details': {
        'module': 'network_firewall', 'class': 'list[CreateServiceDetails]'
    }}
)
@cli_util.wrap_exceptions
def upload_services_extended(ctx, **kwargs):
    upload_file = cli_util.parse_json_parameter(
        "bulk_upload_services_details",
        kwargs['bulk_upload_services_details']
    )
    del kwargs['bulk_upload_services_details']
    kwargs['bulk_upload_services_details'] = json.dumps(upload_file)
    ctx.invoke(networkfirewall_cli.bulk_upload_services, **kwargs)


@cli_util.copy_params_from_generated_command(
    networkfirewall_cli.bulk_upload_security_rules,
    params_to_exclude=['bulk_upload_security_rules_details']
)
@networkfirewall_cli.security_rule_group.command(
    name='bulk-upload',
    help=networkfirewall_cli.bulk_upload_security_rules.help
)
@cli_util.option(
    '--bulk-upload-security-rules-details',
    required=True,
    type=custom_types.CLI_COMPLEX_TYPE,
    help=u"""Request Details to bulk import the security rules for the Network Firewall Policy resource."""
)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'bulk-upload-security-rules-details': {
            'module': 'network_firewall', 'class': 'list[CreateSecurityRuleDetails]'
        }
    }
)
@json_skeleton_utils.get_cli_json_input_option(
    {'bulk-upload-security-rules-details': {
        'module': 'network_firewall', 'class': 'list[CreateSecurityRuleDetails]'
    }}
)
@cli_util.wrap_exceptions
def upload_security_rules_extended(ctx, **kwargs):
    upload_file = cli_util.parse_json_parameter(
        "bulk_upload_security_rules_details",
        kwargs['bulk_upload_security_rules_details']
    )
    del kwargs['bulk_upload_security_rules_details']
    kwargs['bulk_upload_security_rules_details'] = json.dumps(upload_file)
    ctx.invoke(networkfirewall_cli.bulk_upload_security_rules, **kwargs)


@cli_util.copy_params_from_generated_command(
    networkfirewall_cli.bulk_upload_decryption_rules,
    params_to_exclude=['bulk_upload_decryption_rules_details']
)
@networkfirewall_cli.decryption_rule_group.command(
    name='bulk-upload',
    help=networkfirewall_cli.bulk_upload_decryption_rules.help
)
@cli_util.option(
    '--bulk-upload-decryption-rules-details',
    required=True,
    type=custom_types.CLI_COMPLEX_TYPE,
    help=u"""Request Details to bulk import the decryption rules for the Network Firewall Policy resource."""
)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'bulk-upload-decryption-rules-details': {
            'module': 'network_firewall', 'class': 'list[CreateDecryptionRuleDetails]'
        }
    }
)
@json_skeleton_utils.get_cli_json_input_option(
    {'bulk-upload-decryption-rules-details': {
        'module': 'network_firewall', 'class': 'list[CreateDecryptionRuleDetails]'
    }}
)
@cli_util.wrap_exceptions
def upload_decryption_rules_extended(ctx, **kwargs):
    upload_file = cli_util.parse_json_parameter(
        "bulk_upload_decryption_rules_details",
        kwargs['bulk_upload_decryption_rules_details']
    )
    del kwargs['bulk_upload_decryption_rules_details']
    kwargs['bulk_upload_decryption_rules_details'] = json.dumps(upload_file)
    ctx.invoke(networkfirewall_cli.bulk_upload_decryption_rules, **kwargs)


@cli_util.copy_params_from_generated_command(
    networkfirewall_cli.bulk_upload_mapped_secrets,
    params_to_exclude=['bulk_upload_mapped_secrets_details']
)
@networkfirewall_cli.mapped_secret_group.command(
    name='bulk-upload',
    help=networkfirewall_cli.bulk_upload_mapped_secrets.help
)
@cli_util.option(
    '--bulk-upload-mapped-secrets-details',
    required=True,
    type=custom_types.CLI_COMPLEX_TYPE,
    help=u"""Request Details to bulk import the mapped secrets for the Network Firewall Policy resource."""
)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'bulk-upload-mapped-secrets-details': {
            'module': 'network_firewall', 'class': 'list[CreateMappedSecretDetails]'
        }
    }
)
@json_skeleton_utils.get_cli_json_input_option(
    {'bulk-upload-mapped-secrets-details': {
        'module': 'network_firewall', 'class': 'list[CreateMappedSecretDetails]'
    }}
)
@cli_util.wrap_exceptions
def upload_mapped_secrets_extended(ctx, **kwargs):
    upload_file = cli_util.parse_json_parameter(
        "bulk_upload_mapped_secrets_details",
        kwargs['bulk_upload_mapped_secrets_details']
    )
    del kwargs['bulk_upload_mapped_secrets_details']
    kwargs['bulk_upload_mapped_secrets_details'] = json.dumps(upload_file)
    ctx.invoke(networkfirewall_cli.bulk_upload_mapped_secrets, **kwargs)


@cli_util.copy_params_from_generated_command(
    networkfirewall_cli.bulk_upload_decryption_profiles,
    params_to_exclude=['bulk_upload_decryption_profiles_details']
)
@networkfirewall_cli.decryption_profile_group.command(
    name='bulk-upload',
    help=networkfirewall_cli.bulk_upload_decryption_profiles.help
)
@cli_util.option(
    '--bulk-upload-decryption-profiles-details',
    required=True,
    type=custom_types.CLI_COMPLEX_TYPE,
    help=u"""Request Details to bulk import decryption profiles for the Network Firewall Policy resource."""
)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'bulk-upload-decryption-profiles-details': {
            'module': 'network_firewall', 'class': 'list[CreateDecryptionProfileDetails]'
        }})
@json_skeleton_utils.get_cli_json_input_option(
    {'bulk-upload-decryption-profiles-details': {
        'module': 'network_firewall', 'class': 'list[CreateDecryptionProfileDetails]'
    }}
)
@cli_util.wrap_exceptions
def upload_decryption_profiles_extended(ctx, **kwargs):
    upload_file = cli_util.parse_json_parameter(
        "bulk_upload_decryption_profiles_details",
        kwargs['bulk_upload_decryption_profiles_details']
    )
    del kwargs['bulk_upload_decryption_profiles_details']
    kwargs['bulk_upload_decryption_profiles_details'] = json.dumps(upload_file)
    ctx.invoke(networkfirewall_cli.bulk_upload_decryption_profiles, **kwargs)


@cli_util.copy_params_from_generated_command(
    networkfirewall_cli.bulk_upload_url_lists,
    params_to_exclude=['bulk_upload_url_lists_details']
)
@networkfirewall_cli.url_list_group.command(
    name='bulk-upload',
    help=networkfirewall_cli.bulk_upload_url_lists.help
)
@cli_util.option(
    '--bulk-upload-url-lists-details',
    type=custom_types.CLI_COMPLEX_TYPE,
    required=True,
    help=u"""Request Details to bulk import URL lists for the Network Firewall Policy resource."""
)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'bulk-upload-url-lists-details': {
            'module': 'network_firewall', 'class': 'list[CreateURLListDetails]'
        }
    }
)
@json_skeleton_utils.get_cli_json_input_option(
    {'bulk-upload-url-lists-details': {
        'module': 'network_firewall', 'class': 'list[CreateURLListDetails]'
    }}
)
@cli_util.wrap_exceptions
def upload_url_lists_extended(ctx, **kwargs):
    upload_file = cli_util.parse_json_parameter(
        "bulk_upload_url_lists_details",
        kwargs['bulk_upload_url_lists_details']
    )
    del kwargs['bulk_upload_url_lists_details']
    kwargs['bulk_upload_url_lists_details'] = json.dumps(upload_file)
    ctx.invoke(networkfirewall_cli.bulk_upload_url_lists, **kwargs)
