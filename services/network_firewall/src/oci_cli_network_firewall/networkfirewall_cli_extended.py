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


@cli_util.copy_params_from_generated_command(
    networkfirewall_cli.bulk_upload_tunnel_inspection_rules,
    params_to_exclude=['bulk_upload_tunnel_inspection_rules_details']
)
@networkfirewall_cli.tunnel_inspection_rule_group.command(
    name='bulk-upload',
    help=networkfirewall_cli.bulk_upload_tunnel_inspection_rules.help
)
@cli_util.option(
    '--bulk-upload-tunnel-inspection-rules-details',
    type=custom_types.CLI_COMPLEX_TYPE,
    required=True,
    help=u"""Request Details to bulk import tunnel inspection rules for the Network Firewall Policy resource."""
)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'bulk-upload-tunnel-inspection-rules-details': {
            'module': 'network_firewall', 'class': 'list[CreateTunnelInspectionRuleDetails]'
        }
    }
)
@json_skeleton_utils.get_cli_json_input_option(
    {'bulk-upload-tunnel-inspection-rules-details': {
        'module': 'network_firewall', 'class': 'list[CreateTunnelInspectionRuleDetails]'
    }}
)
@cli_util.wrap_exceptions
def upload_tunnel_inspection_rules_extended(ctx, **kwargs):
    upload_file = cli_util.parse_json_parameter(
        "bulk_upload_tunnel_inspection_rules_details",
        kwargs['bulk_upload_tunnel_inspection_rules_details']
    )
    del kwargs['bulk_upload_tunnel_inspection_rules_details']
    kwargs['bulk_upload_tunnel_inspection_rules_details'] = json.dumps(upload_file)
    ctx.invoke(networkfirewall_cli.bulk_upload_tunnel_inspection_rules, **kwargs)


@cli_util.copy_params_from_generated_command(
    networkfirewall_cli.bulk_upload_nat_rules,
    params_to_exclude=['bulk_upload_nat_rules_details']
)
@networkfirewall_cli.nat_rule_group.command(
    name='bulk-upload',
    help=networkfirewall_cli.bulk_upload_nat_rules.help
)
@cli_util.option(
    '--bulk-upload-nat-rules-details',
    type=custom_types.CLI_COMPLEX_TYPE,
    required=True,
    help=u"""Request Details to bulk import nat rules for the Network Firewall Policy resource."""
)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'bulk-upload-nat-rules-details': {
            'module': 'network_firewall', 'class': 'list[CreateNatRuleDetails]'
        }
    }
)
@json_skeleton_utils.get_cli_json_input_option(
    {'bulk-upload-nat-rules-details': {
        'module': 'network_firewall', 'class': 'list[CreateNatRuleDetails]'
    }}
)
@cli_util.wrap_exceptions
def upload_nat_rules_extended(ctx, **kwargs):
    upload_file = cli_util.parse_json_parameter(
        "bulk_upload_nat_rules_details",
        kwargs['bulk_upload_nat_rules_details']
    )
    del kwargs['bulk_upload_nat_rules_details']
    kwargs['bulk_upload_nat_rules_details'] = json.dumps(upload_file)
    ctx.invoke(networkfirewall_cli.bulk_upload_nat_rules, **kwargs)


@cli_util.copy_params_from_generated_command(
    networkfirewall_cli.create_application,
    params_to_exclude=['name']
)
@networkfirewall_cli.application_group.command(
    name='create',
    help=networkfirewall_cli.create_application.help
)
@cli_util.option(
    '--application-details',
    type=custom_types.CLI_COMPLEX_TYPE,
    required=True,
    help=u"""Type specific request details to create an application for the Network Firewall Policy resource."""
)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'application-details': {
            'module': 'network_firewall', 'class': 'CreateApplicationDetails'
        }
    }
)
@json_skeleton_utils.get_cli_json_input_option(
    {'application-details': {
        'module': 'network_firewall', 'class': 'CreateApplicationDetails'
    }}
)
@cli_util.wrap_exceptions
def create_application_extended(ctx, **kwargs):

    application_details = cli_util.parse_json_parameter(
        "application_details",
        kwargs['application_details']
    )
    del kwargs['application_details']

    application_type = kwargs['type']
    del kwargs['type']

    if not (application_details.get('name') is None):
        kwargs['name'] = application_details['name']
    if not (application_details.get('icmpType') is None):
        kwargs['icmp_type'] = application_details['icmpType']
    if not (application_details.get('icmpCode') is None):
        kwargs['icmp_code'] = application_details['icmpCode']
    if not (application_details.get('type') is None):
        if application_type != application_details.get('type'):
            raise ValueError("type from application-details doesn't match with type provided as parameter")

    if application_type == "ICMP":
        ctx.invoke(networkfirewall_cli.create_application_create_icmp_application_details, **kwargs)
    else:
        ctx.invoke(networkfirewall_cli.create_application_create_icmp_application_details, **kwargs)


@cli_util.copy_params_from_generated_command(
    networkfirewall_cli.update_application,
    params_to_exclude=[]
)
@networkfirewall_cli.application_group.command(
    name='update',
    help=networkfirewall_cli.update_application.help
)
@cli_util.option(
    '--application-details',
    type=custom_types.CLI_COMPLEX_TYPE,
    required=True,
    help=u"""Type specific details to update an application for the Network Firewall Policy resource."""
)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'application-details': {
            'module': 'network_firewall', 'class': 'UpdateApplicationDetails'
        }
    }
)
@json_skeleton_utils.get_cli_json_input_option(
    {'application-details': {
        'module': 'network_firewall', 'class': 'UpdateApplicationDetails'
    }}
)
@cli_util.wrap_exceptions
def update_application_extended(ctx, **kwargs):
    application_details = cli_util.parse_json_parameter(
        "application_details",
        kwargs['application_details']
    )
    del kwargs['application_details']

    application_type = kwargs['type']
    del kwargs['type']

    if not (application_details.get('icmpType') is None):
        kwargs['icmp_type'] = application_details['icmpType']
    if not (application_details.get('icmpCode') is None):
        kwargs['icmp_code'] = application_details['icmpCode']
    if not (application_details.get('type') is None):
        if application_type != application_details.get('type'):
            raise ValueError("type from application-details doesn't match with type provided as parameter")

    if application_type == "ICMP":
        ctx.invoke(networkfirewall_cli.update_application_update_icmp_application_details, **kwargs)
    else:
        ctx.invoke(networkfirewall_cli.update_application_update_icmp6_application_details, **kwargs)


@cli_util.copy_params_from_generated_command(
    networkfirewall_cli.create_service,
    params_to_exclude=['name']
)
@networkfirewall_cli.service_group.command(
    name='create',
    help=networkfirewall_cli.create_service.help
)
@cli_util.option(
    '--service-details',
    type=custom_types.CLI_COMPLEX_TYPE,
    required=True,
    help=u"""Type specific request details to create a service for the Network Firewall Policy resource."""
)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'service-details': {
            'module': 'network_firewall', 'class': 'CreateServiceDetails'
        }
    }
)
@json_skeleton_utils.get_cli_json_input_option(
    {'service-details': {
        'module': 'network_firewall', 'class': 'CreateServiceDetails'
    }}
)
@cli_util.wrap_exceptions
def create_service_extended(ctx, **kwargs):
    service_details = cli_util.parse_json_parameter(
        "service_details",
        kwargs['service_details']
    )
    del kwargs['service_details']

    service_type = kwargs['type']
    del kwargs['type']

    if not (service_details.get('portRanges') is None):
        kwargs['port_ranges'] = service_details['portRanges']
    if not (service_details.get('name') is None):
        kwargs['name'] = service_details['name']
    if not (service_details.get('type') is None):
        if service_details.get('type') != service_type:
            raise ValueError("type from service-details doesn't match with type provided as parameter")

    if service_type == "TCP":
        ctx.invoke(networkfirewall_cli.create_service_create_tcp_service_details, **kwargs)
    else:
        ctx.invoke(networkfirewall_cli.create_service_create_udp_service_details, **kwargs)


@cli_util.copy_params_from_generated_command(
    networkfirewall_cli.update_service,
    params_to_exclude=[]
)
@networkfirewall_cli.service_group.command(
    name='update',
    help=networkfirewall_cli.update_service.help
)
@cli_util.option(
    '--service-details',
    type=custom_types.CLI_COMPLEX_TYPE,
    required=True,
    help=u"""Type specific details to update a service for the Network Firewall Policy resource."""
)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'service-details': {
            'module': 'network_firewall', 'class': 'UpdateServiceDetails'
        }
    }
)
@json_skeleton_utils.get_cli_json_input_option(
    {'service-details': {
        'module': 'network_firewall', 'class': 'UpdateServiceDetails'
    }}
)
@cli_util.wrap_exceptions
def update_service_extended(ctx, **kwargs):
    service_details = cli_util.parse_json_parameter(
        "service_details",
        kwargs['service_details']
    )
    del kwargs['service_details']

    service_type = kwargs['type']
    del kwargs['type']

    if not (service_details.get('portRanges') is None):
        kwargs['port_ranges'] = service_details['portRanges']
    if not (service_details.get('type') is None):
        if service_details.get('type') != service_type:
            raise ValueError("type from service-details doesn't match with type provided as parameter")

    if service_type == "TCP":
        ctx.invoke(networkfirewall_cli.update_service_update_tcp_service_details, **kwargs)
    else:
        ctx.invoke(networkfirewall_cli.update_service_update_udp_service_details, **kwargs)


@cli_util.copy_params_from_generated_command(
    networkfirewall_cli.create_mapped_secret,
    params_to_exclude=['name', 'type']
)
@networkfirewall_cli.mapped_secret_group.command(
    name='create',
    help=networkfirewall_cli.create_mapped_secret.help
)
@cli_util.option(
    '--mapped-secret-details',
    type=custom_types.CLI_COMPLEX_TYPE,
    required=True,
    help=u"""Type specific request details to create a mapped secret for the Network Firewall Policy resource."""
)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'mapped-secret-details': {
            'module': 'network_firewall', 'class': 'CreateMappedSecretDetails'
        }
    }
)
@json_skeleton_utils.get_cli_json_input_option(
    {'mapped-secret-details': {
        'module': 'network_firewall', 'class': 'CreateMappedSecretDetails'
    }}
)
@cli_util.wrap_exceptions
def create_mapped_secret_extended(ctx, **kwargs):
    mapped_secret_details = cli_util.parse_json_parameter(
        "mapped_secret_details",
        kwargs['mapped_secret_details']
    )
    del kwargs['mapped_secret_details']

    secret_source = kwargs['source']
    del kwargs['source']

    if not (mapped_secret_details.get('name') is None):
        kwargs['name'] = mapped_secret_details['name']
    if not (mapped_secret_details.get('type') is None):
        kwargs['type'] = mapped_secret_details['type']
    if not (mapped_secret_details.get('vaultSecretId') is None):
        kwargs['vault_secret_id'] = mapped_secret_details['vaultSecretId']
    if not (mapped_secret_details.get('versionNumber') is None):
        kwargs['version_number'] = mapped_secret_details['versionNumber']
    if mapped_secret_details.get('source') is None:
        if secret_source != mapped_secret_details.get('source'):
            raise ValueError("source from mapped-secret-details doesn't match with source provided as parameter")

    # add condition when more than one source values available
    ctx.invoke(networkfirewall_cli.create_mapped_secret_create_vault_mapped_secret_details, **kwargs)


@cli_util.copy_params_from_generated_command(
    networkfirewall_cli.update_mapped_secret,
    params_to_exclude=['type']
)
@networkfirewall_cli.mapped_secret_group.command(
    name='update',
    help=networkfirewall_cli.update_mapped_secret.help
)
@cli_util.option(
    '--mapped-secret-details',
    type=custom_types.CLI_COMPLEX_TYPE,
    required=True,
    help=u"""Type specific details to update a mapped secret for the Network Firewall Policy resource."""
)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'mapped-secret-details': {
            'module': 'network_firewall', 'class': 'UpdateMappedSecretDetails'
        }
    }
)
@json_skeleton_utils.get_cli_json_input_option(
    {'mapped-secret-details': {
        'module': 'network_firewall', 'class': 'UpdateMappedSecretDetails'
    }}
)
@cli_util.wrap_exceptions
def update_mapped_secret_extended(ctx, **kwargs):
    mapped_secret_details = cli_util.parse_json_parameter(
        "mapped_secret_details",
        kwargs['mapped_secret_details']
    )
    del kwargs['mapped_secret_details']

    secret_source = kwargs['source']
    del kwargs['source']

    if not (mapped_secret_details.get('type') is None):
        kwargs['type'] = mapped_secret_details['type']
    if not (mapped_secret_details.get('vaultSecretId') is None):
        kwargs['vault_secret_id'] = mapped_secret_details['vaultSecretId']
    if not (mapped_secret_details.get('versionNumber') is None):
        kwargs['version_number'] = mapped_secret_details['versionNumber']
    if mapped_secret_details.get('source') is None:
        if secret_source != mapped_secret_details.get('source'):
            raise ValueError("source from mapped-secret-details doesn't match with source provided as parameter")

    # add condition when more than one source values available
    ctx.invoke(networkfirewall_cli.update_mapped_secret_update_vault_mapped_secret_details, **kwargs)


@cli_util.copy_params_from_generated_command(
    networkfirewall_cli.create_decryption_profile,
    params_to_exclude=['name']
)
@networkfirewall_cli.decryption_profile_group.command(
    name='create',
    help=networkfirewall_cli.create_decryption_profile.help
)
@cli_util.option(
    '--decryption-profile-details',
    type=custom_types.CLI_COMPLEX_TYPE,
    required=True,
    help=u"""Type specific request details to create a decryption profile for the Network Firewall Policy resource."""
)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'decryption-profile-details': {
            'module': 'network_firewall', 'class': 'CreateDecryptionProfileDetails'
        }
    }
)
@json_skeleton_utils.get_cli_json_input_option(
    {'decryption-profile-details': {
        'module': 'network_firewall', 'class': 'CreateDecryptionProfileDetails'
    }}
)
@cli_util.wrap_exceptions
def create_decryption_profile_extended(ctx, **kwargs):
    decryption_profile_details = cli_util.parse_json_parameter(
        "decryption_profile_details",
        kwargs['decryption_profile_details']
    )
    del kwargs['decryption_profile_details']

    profile_type = kwargs['type']
    del kwargs['type']

    if not (decryption_profile_details.get('name') is None):
        kwargs['name'] = decryption_profile_details['name']
    if not (decryption_profile_details.get('type') is None):
        if decryption_profile_details.get('type') != profile_type:
            raise ValueError("type from decryption-profile-details doesn't match with type provided as parameter")

    if profile_type == "SSL_FORWARD_PROXY":
        if decryption_profile_details.get('isExpiredCertificateBlocked') is not None:
            kwargs['is_expired_certificate_blocked'] = decryption_profile_details['isExpiredCertificateBlocked']

        if decryption_profile_details.get('isUntrustedIssuerBlocked') is not None:
            kwargs['is_untrusted_issuer_blocked'] = decryption_profile_details['isUntrustedIssuerBlocked']

        if decryption_profile_details.get('isRevocationStatusTimeoutBlocked') is not None:
            kwargs['is_revocation_status_timeout_blocked'] = decryption_profile_details['isRevocationStatusTimeoutBlocked']

        if decryption_profile_details.get('isUnknownRevocationStatusBlocked') is not None:
            kwargs['is_unknown_revocation_status_blocked'] = decryption_profile_details['isUnknownRevocationStatusBlocked']

        if decryption_profile_details.get('areCertificateExtensionsRestricted') is not None:
            kwargs['are_certificate_extensions_restricted'] = decryption_profile_details['areCertificateExtensionsRestricted']

        if decryption_profile_details.get('isAutoIncludeAltName') is not None:
            kwargs['is_auto_include_alt_name'] = decryption_profile_details['isAutoIncludeAltName']

    if decryption_profile_details.get('isUnsupportedVersionBlocked') is not None:
        kwargs['is_unsupported_version_blocked'] = decryption_profile_details['isUnsupportedVersionBlocked']

    if decryption_profile_details.get('isUnsupportedCipherBlocked') is not None:
        kwargs['is_unsupported_cipher_blocked'] = decryption_profile_details['isUnsupportedCipherBlocked']

    if decryption_profile_details.get('isOutOfCapacityBlocked') is not None:
        kwargs['is_out_of_capacity_blocked'] = decryption_profile_details['isOutOfCapacityBlocked']

    if profile_type == "SSL_FORWARD_PROXY":
        ctx.invoke(
            networkfirewall_cli.create_decryption_profile_create_ssl_forward_proxy_profile_details, **kwargs)
    else:
        ctx.invoke(
            networkfirewall_cli.create_decryption_profile_create_ssl_inbound_inspection_profile_details, **kwargs)


@cli_util.copy_params_from_generated_command(
    networkfirewall_cli.update_decryption_profile,
    params_to_exclude=[]
)
@networkfirewall_cli.decryption_profile_group.command(
    name='update',
    help=networkfirewall_cli.update_decryption_profile.help
)
@cli_util.option(
    '--decryption-profile-details',
    type=custom_types.CLI_COMPLEX_TYPE,
    required=True,
    help=u"""Type specific details to update a decryption profile for the Network Firewall Policy resource."""
)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'decryption-profile-details': {
            'module': 'network_firewall', 'class': 'UpdateDecryptionProfileDetails'
        }
    }
)
@json_skeleton_utils.get_cli_json_input_option(
    {'decryption-profile-details': {
        'module': 'network_firewall', 'class': 'UpdateDecryptionProfileDetails'
    }}
)
@cli_util.wrap_exceptions
def update_decryption_profile_extended(ctx, **kwargs):
    decryption_profile_details = cli_util.parse_json_parameter(
        "decryption_profile_details",
        kwargs['decryption_profile_details']
    )
    del kwargs['decryption_profile_details']

    profile_type = kwargs['type']
    del kwargs['type']

    if not (decryption_profile_details.get('type') is None):
        if decryption_profile_details.get('type') != profile_type:
            raise ValueError("type from decryption-profile-details doesn't match with type provided as parameter")

    if profile_type == "SSL_FORWARD_PROXY":
        if decryption_profile_details.get('isExpiredCertificateBlocked') is not None:
            kwargs['is_expired_certificate_blocked'] = decryption_profile_details['isExpiredCertificateBlocked']

        if decryption_profile_details.get('isUntrustedIssuerBlocked') is not None:
            kwargs['is_untrusted_issuer_blocked'] = decryption_profile_details['isUntrustedIssuerBlocked']

        if decryption_profile_details.get('isRevocationStatusTimeoutBlocked') is not None:
            kwargs['is_revocation_status_timeout_blocked'] = decryption_profile_details['isRevocationStatusTimeoutBlocked']

        if decryption_profile_details.get('isUnknownRevocationStatusBlocked') is not None:
            kwargs['is_unknown_revocation_status_blocked'] = decryption_profile_details['isUnknownRevocationStatusBlocked']

        if decryption_profile_details.get('areCertificateExtensionsRestricted') is not None:
            kwargs['are_certificate_extensions_restricted'] = decryption_profile_details['areCertificateExtensionsRestricted']

        if decryption_profile_details.get('isAutoIncludeAltName') is not None:
            kwargs['is_auto_include_alt_name'] = decryption_profile_details['isAutoIncludeAltName']

    if decryption_profile_details.get('isUnsupportedVersionBlocked') is not None:
        kwargs['is_unsupported_version_blocked'] = decryption_profile_details['isUnsupportedVersionBlocked']

    if decryption_profile_details.get('isUnsupportedCipherBlocked') is not None:
        kwargs['is_unsupported_cipher_blocked'] = decryption_profile_details['isUnsupportedCipherBlocked']

    if decryption_profile_details.get('isOutOfCapacityBlocked') is not None:
        kwargs['is_out_of_capacity_blocked'] = decryption_profile_details['isOutOfCapacityBlocked']

    if profile_type == "SSL_FORWARD_PROXY":
        ctx.invoke(networkfirewall_cli.update_decryption_profile_update_ssl_forward_proxy_profile_details, **kwargs)
    else:
        ctx.invoke(
            networkfirewall_cli.update_decryption_profile_update_ssl_inbound_inspection_profile_details, **kwargs)


@cli_util.copy_params_from_generated_command(
    networkfirewall_cli.create_tunnel_inspection_rule,
    params_to_exclude=['name', 'action', 'position']
)
@networkfirewall_cli.tunnel_inspection_rule_group.command(
    name='create',
    help=networkfirewall_cli.create_tunnel_inspection_rule.help
)
@cli_util.option(
    '--tunnel-inspection-rule-details',
    type=custom_types.CLI_COMPLEX_TYPE,
    required=True,
    help=u"""Type specific request details to create a tunnel inspection rule for the Network Firewall Policy resource."""
)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'tunnel-inspection-rule-details': {
            'module': 'network_firewall', 'class': 'CreateTunnelInspectionRuleDetails'
        }
    }
)
@json_skeleton_utils.get_cli_json_input_option(
    {'tunnel-inspection-rule-details': {
        'module': 'network_firewall', 'class': 'CreateTunnelInspectionRuleDetails'
    }}
)
@cli_util.wrap_exceptions
def create_tunnel_inspection_rule_extended(ctx, **kwargs):
    tunnel_inspection_rule_details = cli_util.parse_json_parameter(
        "tunnel_inspection_rule_details",
        kwargs['tunnel_inspection_rule_details']
    )
    del kwargs['tunnel_inspection_rule_details']

    protocol = kwargs['protocol']
    del kwargs['protocol']

    if not (tunnel_inspection_rule_details.get('name') is None):
        kwargs['name'] = tunnel_inspection_rule_details['name']
    if not (tunnel_inspection_rule_details.get('condition') is None):
        kwargs['condition'] = tunnel_inspection_rule_details['condition']
    if not (tunnel_inspection_rule_details.get('action') is None):
        kwargs['action'] = tunnel_inspection_rule_details['action']
    if not (tunnel_inspection_rule_details.get('position') is None):
        kwargs['position'] = tunnel_inspection_rule_details['position']
    if not (tunnel_inspection_rule_details.get('profile') is None):
        kwargs['profile_parameterconflict'] = tunnel_inspection_rule_details['profile']
    if not tunnel_inspection_rule_details.get('protocol') is None:
        if tunnel_inspection_rule_details.get('protocol') != protocol:
            raise ValueError(
                "protocol from tunnel-inspection-rule-details doesn't match with protocol provided as parameter")

    ctx.invoke(networkfirewall_cli.create_tunnel_inspection_rule_create_vxlan_inspection_rule_details, **kwargs)


@cli_util.copy_params_from_generated_command(
    networkfirewall_cli.update_tunnel_inspection_rule,
    params_to_exclude=['action', 'position']
)
@networkfirewall_cli.tunnel_inspection_rule_group.command(
    name='update', help=networkfirewall_cli.update_tunnel_inspection_rule.help
)
@cli_util.option(
    '--tunnel-inspection-rule-details',
    type=custom_types.CLI_COMPLEX_TYPE,
    required=True,
    help=u"""Type specific details to update a tunnel inspection rule for the Network Firewall Policy resource."""
)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'tunnel-inspection-rule-details': {
            'module': 'network_firewall', 'class': 'UpdateTunnelInspectionRuleDetails'
        }
    }
)
@json_skeleton_utils.get_cli_json_input_option(
    {'tunnel-inspection-rule-details': {
        'module': 'network_firewall', 'class': 'UpdateTunnelInspectionRuleDetails'
    }}
)
@cli_util.wrap_exceptions
def update_tunnel_inspection_rule_extended(ctx, **kwargs):
    tunnel_inspection_rule_details = cli_util.parse_json_parameter(
        "tunnel_inspection_rule_details",
        kwargs['tunnel_inspection_rule_details']
    )
    del kwargs['tunnel_inspection_rule_details']

    protocol = kwargs['protocol']
    del kwargs['protocol']

    if not (tunnel_inspection_rule_details.get('condition') is None):
        kwargs['condition'] = tunnel_inspection_rule_details['condition']
    if not (tunnel_inspection_rule_details.get('protocol') is None):
        if protocol != tunnel_inspection_rule_details.get('protocol'):
            raise KeyError("protocol is missing for tunnel inspection rule.")

    if tunnel_inspection_rule_details.get('action') is not None:
        kwargs['action'] = tunnel_inspection_rule_details['action']
    if tunnel_inspection_rule_details.get('position') is not None:
        kwargs['position'] = tunnel_inspection_rule_details['position']
    if tunnel_inspection_rule_details.get('profile') is not None:
        kwargs['profile_parameterconflict'] = tunnel_inspection_rule_details['profile']

    ctx.invoke(networkfirewall_cli.update_tunnel_inspection_rule_update_vxlan_inspection_rule_details, **kwargs)


@cli_util.copy_params_from_generated_command(
    networkfirewall_cli.create_nat_rule,
    params_to_exclude=['name', 'action', 'condition', 'description']
)
@networkfirewall_cli.nat_rule_group.command(
    name='create',
    help=networkfirewall_cli.create_nat_rule.help
)
@cli_util.option(
    '--nat-rule-details',
    type=custom_types.CLI_COMPLEX_TYPE,
    required=True,
    help=u"""Type specific request details to create a nat rule for the Network Firewall Policy resource."""
)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'nat-rule-details': {
            'module': 'network_firewall', 'class': 'CreateNatRuleDetails'
        }
    }
)
@json_skeleton_utils.get_cli_json_input_option(
    {'nat-rule-details': {
        'module': 'network_firewall', 'class': 'CreateNatRuleDetails'
    }}
)
@cli_util.wrap_exceptions
def create_nat_rule_extended(ctx, **kwargs):
    nat_rule_details = cli_util.parse_json_parameter(
        "nat_rule_details",
        kwargs['nat_rule_details']
    )
    del kwargs['nat_rule_details']

    type = kwargs['type']
    del kwargs['type']

    if not (nat_rule_details.get('name') is None):
        kwargs['name'] = nat_rule_details['name']
    if not (nat_rule_details.get('condition') is None):
        kwargs['condition'] = nat_rule_details['condition']
    if not (nat_rule_details.get('action') is None):
        kwargs['action'] = nat_rule_details['action']
    if not (nat_rule_details.get('description') is None):
        kwargs['description'] = nat_rule_details['description']

    if type == "NATV4":
        ctx.invoke(networkfirewall_cli.create_nat_rule_create_nat_v4_rule_details, **kwargs)


@cli_util.copy_params_from_generated_command(
    networkfirewall_cli.update_nat_rule,
    params_to_exclude=['action', 'position', 'condition', 'type']
)
@networkfirewall_cli.nat_rule_group.command(
    name='update', help=networkfirewall_cli.update_nat_rule.help
)
@cli_util.option(
    '--nat-rule-details',
    type=custom_types.CLI_COMPLEX_TYPE,
    required=True,
    help=u"""Type specific details to update a nat rule for the Network Firewall Policy resource."""
)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'nat-rule-details': {
            'module': 'network_firewall', 'class': 'UpdateNatRuleDetails'
        }
    }
)
@json_skeleton_utils.get_cli_json_input_option(
    {'nat-rule-details': {
        'module': 'network_firewall', 'class': 'UpdateNatRuleDetails'
    }}
)
@cli_util.wrap_exceptions
def update_nat_rule_extended(ctx, **kwargs):
    nat_rule_details = cli_util.parse_json_parameter(
        "nat_rule_details",
        kwargs['nat_rule_details']
    )
    del kwargs['nat_rule_details']

    if not (nat_rule_details.get('condition') is None):
        kwargs['condition'] = nat_rule_details['condition']
    if nat_rule_details.get('action') is not None:
        kwargs['action'] = nat_rule_details['action']
    if nat_rule_details.get('position') is not None:
        kwargs['position'] = nat_rule_details['position']

    ctx.invoke(networkfirewall_cli.update_nat_rule_update_nat_v4_rule_details, **kwargs)


networkfirewall_cli.application_group.commands.pop(
    networkfirewall_cli.create_application_create_icmp_application_details.name)
networkfirewall_cli.application_group.commands.pop(
    networkfirewall_cli.create_application_create_icmp6_application_details.name)
networkfirewall_cli.application_group.commands.pop(
    networkfirewall_cli.update_application_update_icmp_application_details.name)
networkfirewall_cli.application_group.commands.pop(
    networkfirewall_cli.update_application_update_icmp6_application_details.name)
networkfirewall_cli.service_group.commands.pop(
    networkfirewall_cli.create_service_create_udp_service_details.name)
networkfirewall_cli.service_group.commands.pop(
    networkfirewall_cli.create_service_create_tcp_service_details.name)
networkfirewall_cli.service_group.commands.pop(
    networkfirewall_cli.update_service_update_tcp_service_details.name)
networkfirewall_cli.service_group.commands.pop(
    networkfirewall_cli.update_service_update_udp_service_details.name)
networkfirewall_cli.mapped_secret_group.commands.pop(
    networkfirewall_cli.create_mapped_secret_create_vault_mapped_secret_details.name)
networkfirewall_cli.mapped_secret_group.commands.pop(
    networkfirewall_cli.update_mapped_secret_update_vault_mapped_secret_details.name)
networkfirewall_cli.decryption_profile_group.commands.pop(
    networkfirewall_cli.create_decryption_profile_create_ssl_inbound_inspection_profile_details.name)
networkfirewall_cli.decryption_profile_group.commands.pop(
    networkfirewall_cli.create_decryption_profile_create_ssl_forward_proxy_profile_details.name)
networkfirewall_cli.decryption_profile_group.commands.pop(
    networkfirewall_cli.update_decryption_profile_update_ssl_inbound_inspection_profile_details.name)
networkfirewall_cli.decryption_profile_group.commands.pop(
    networkfirewall_cli.update_decryption_profile_update_ssl_forward_proxy_profile_details.name)
networkfirewall_cli.tunnel_inspection_rule_group.commands.pop(
    networkfirewall_cli.create_tunnel_inspection_rule_create_vxlan_inspection_rule_details.name)
networkfirewall_cli.tunnel_inspection_rule_group.commands.pop(
    networkfirewall_cli.update_tunnel_inspection_rule_update_vxlan_inspection_rule_details.name)
networkfirewall_cli.nat_rule_group.commands.pop(
    networkfirewall_cli.create_nat_rule_create_nat_v4_rule_details.name)
networkfirewall_cli.nat_rule_group.commands.pop(
    networkfirewall_cli.update_nat_rule_update_nat_v4_rule_details.name)
