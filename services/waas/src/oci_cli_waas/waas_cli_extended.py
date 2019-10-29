# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import click
from services.waas.src.oci_cli_waas.generated import waas_cli
from .generated import waas_service_cli
from oci_cli import cli_util
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils
from oci_cli.aliasing import CommandGroupWithAlias

from oci_cli.cli_root import cli

cli.commands.pop(waas_service_cli.waas_service_group.name)
cli.add_command(waas_cli.waas_root_group)

# oci waas purge-cache purge-cache --waas-policy-id, --resources
# to
# oci waas purge-cache --waas-policy-id, --resources
waas_cli.waas_root_group.commands.pop(waas_cli.purge_cache_group.name)
waas_cli.waas_root_group.add_command(waas_cli.purge_cache)

# oci waas custom-protection-rule update-waas-policy --update-custom-protection-rules-details, --waas-policy-id
# to
# oci waas custom-protection-rule update-setting --custom-protection-rules-details, --waas-policy-id
# waas_cli.waas_root_group.commands.pop(waas_cli.custom_protection_rule_setting_group.name)

waas_cli.custom_protection_rule_group.commands.pop(waas_cli.update_waas_policy_custom_protection_rules.name)


@cli_util.copy_params_from_generated_command(waas_cli.update_waas_policy_custom_protection_rules, params_to_exclude=['update_custom_protection_rules_details'])
@waas_cli.custom_protection_rule_group.command(name=cli_util.override('update_waas_policy_custom_protection_rules.command_name', 'update-setting'), help=waas_cli.update_waas_policy_custom_protection_rules.help)
@cli_util.option('--custom-protection-rules-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-protection-rules-details': {'module': 'waas', 'class': 'list[CustomProtectionRuleSetting]'}})
@cli_util.wrap_exceptions
def update_waas_policy_custom_protection_rules_extended(ctx, **kwargs):
    if 'custom_protection_rules_details' in kwargs:
        kwargs['update_custom_protection_rules_details'] = kwargs['custom_protection_rules_details']
        kwargs.pop('custom_protection_rules_details')
    ctx.invoke(waas_cli.update_waas_policy_custom_protection_rules, **kwargs)


# Adds commands to support Backward incompatible changes introduced by DEXREQ-829
# Update oci waas custom-protection-rule list-waas-policy to
# oci waas waas-policy custom-protection-rule list
@click.command(cli_util.override('waas.waas_policy_custom_protection_rule_group.command_name', 'waas-policy-custom-protection-rule'), cls=CommandGroupWithAlias, help="""Summary information about a Custom Protection rule.""")
@cli_util.help_option_group
# Create Dummy group
def waas_policy_custom_protection_rule_group():
    pass


waas_cli.custom_protection_rule_group.commands.pop(waas_cli.list_waas_policy_custom_protection_rules.name)
waas_policy_custom_protection_rule_group.add_command(waas_cli.list_waas_policy_custom_protection_rules)
cli_util.rename_command(waas_cli, waas_policy_custom_protection_rule_group, waas_cli.list_waas_policy_custom_protection_rules, 'list')
waas_cli.waas_policy_group.add_command(waas_policy_custom_protection_rule_group)
cli_util.rename_command(waas_cli, waas_cli.waas_policy_group, waas_policy_custom_protection_rule_group, "custom-protection-rule")


# Rename caching-rules to caching-rule
cli_util.rename_command(cli, waas_cli.waas_root_group, waas_cli.caching_rules_group, 'caching-rule')


# Add update-address-list to certificate group
# This is to address backward in-compatible changes introduced by DEXREQ-829
@cli_util.copy_params_from_generated_command(waas_cli.update_address_list)
@waas_cli.certificate_group.command(name=cli_util.override('waas.certificate_group.update_address_list.command_name', 'update-address-list'), help="**Deprecated**, use oci waas address-list update command " + waas_cli.update_address_list.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'addresses': {'module': 'waas', 'class': 'list[string]'}, 'freeform-tags': {'module': 'waas', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waas', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'waas', 'class': 'AddressList'})
@cli_util.wrap_exceptions
def update_address_list_extended(ctx, **kwargs):
    ctx.invoke(waas_cli.update_address_list, **kwargs)
