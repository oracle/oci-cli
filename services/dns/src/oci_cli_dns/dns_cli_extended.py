# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci_cli import cli_util
from oci_cli.cli_util import option

from oci_cli.aliasing import CommandGroupWithAlias
from services.dns.src.oci_cli_dns.generated import dns_cli
from oci_cli import json_skeleton_utils
from oci_cli import custom_types
import click


@dns_cli.dns_root_group.command('record', cls=CommandGroupWithAlias, help="""A DNS record.""")
@cli_util.help_option_group
def record():
    pass


@record.command('rrset', cls=CommandGroupWithAlias, help=dns_cli.rr_set_group.help)
@cli_util.help_option_group
def rrset():
    pass


@record.command('domain', cls=CommandGroupWithAlias, help="""A collection of DNS records for the same domain.""")
@cli_util.help_option_group
def domain():
    pass


@record.command('zone', cls=CommandGroupWithAlias, help="""A collection of DNS records for the same zone.""")
@cli_util.help_option_group
def zone():
    pass


# specify that compartment_id is required for create zone
@cli_util.copy_params_from_generated_command(dns_cli.create_zone_create_zone_details, params_to_exclude=['compartment_id', 'zone_type'])
@dns_cli.zone_group.command(name=cli_util.override('create_zone_create_zone_details.command_name', 'create'), help=dns_cli.create_zone_create_zone_details.help)
@option('--compartment-id', required=True, help="""The OCID of the compartment the resource belongs to.""")
@option('--zone-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["PRIMARY", "SECONDARY"]), help=u"""The type of the zone. Must be either `PRIMARY` or `SECONDARY`.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}, 'external-masters': {'module': 'dns', 'class': 'list[ExternalMaster]'}}, output_type={'module': 'dns', 'class': 'Zone'})
@cli_util.wrap_exceptions
def create_zone(ctx, **kwargs):
    ctx.invoke(dns_cli.create_zone_create_zone_details, **kwargs)


# specify that compartment_id and dynect-migration-details are required for migrate zone
@cli_util.copy_params_from_generated_command(dns_cli.create_zone_create_migrated_dynect_zone_details, params_to_exclude=['compartment_id', 'dynect_migration_details'])
@dns_cli.zone_group.command(name=cli_util.override('create_zone_create_migrated_dynect_zone_details.command_name', 'migrate-from-dynect'), help="""Migrates a zone from DynECT into a specific compartment in OCI.""")
@option('--compartment-id', required=True, help="""The OCID of the compartment the resource belongs to.""")
@option('--dynect-migration-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}, 'dynect-migration-details': {'module': 'dns', 'class': 'DynectMigrationDetails'}}, output_type={'module': 'dns', 'class': 'Zone'})
@cli_util.wrap_exceptions
def migrate_zone_from_dynect(ctx, **kwargs):
    ctx.invoke(dns_cli.create_zone_create_migrated_dynect_zone_details, **kwargs)


dns_cli.zone_group.commands.pop(dns_cli.create_zone.name)
dns_cli.zone_group.commands.pop(dns_cli.create_zone_create_migrated_dynect_zone_details.name)
dns_cli.zone_group.commands.pop(dns_cli.create_zone_create_zone_details.name)
dns_cli.zone_group.add_command(create_zone)
dns_cli.zone_group.add_command(migrate_zone_from_dynect)

dns_cli.dns_root_group.commands.pop(dns_cli.rr_set_group.name)
dns_cli.dns_root_group.commands.pop(dns_cli.record_collection_group.name)
dns_cli.dns_root_group.commands.pop(dns_cli.records_group.name)
dns_cli.dns_root_group.commands.pop(dns_cli.zones_group.name)

dns_cli.zone_group.add_command(dns_cli.get_zone)
dns_cli.zone_group.add_command(dns_cli.list_zones)

# zone records
cli_util.rename_command(dns_cli, zone, dns_cli.get_zone_records, "get")
cli_util.rename_command(dns_cli, zone, dns_cli.patch_zone_records, "patch")
cli_util.rename_command(dns_cli, zone, dns_cli.update_zone_records, "update")

# domain records
cli_util.rename_command(dns_cli, domain, dns_cli.patch_domain_records, "patch")
cli_util.rename_command(dns_cli, domain, dns_cli.update_domain_records, "update")
cli_util.rename_command(dns_cli, domain, dns_cli.get_domain_records, "get")
cli_util.rename_command(dns_cli, domain, dns_cli.delete_domain_records, "delete")

# rrset
cli_util.rename_command(dns_cli, rrset, dns_cli.update_rr_set, "update")
rrset.add_command(dns_cli.get_rr_set)
rrset.add_command(dns_cli.patch_rr_set)
rrset.add_command(dns_cli.delete_rr_set)
