# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .. import cli_util
from ..cli_util import option

from ..aliasing import CommandGroupWithAlias
from ..generated import dns_cli
from .. import json_skeleton_utils
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
@cli_util.copy_params_from_generated_command(dns_cli.create_zone, params_to_exclude=['compartment_id'])
@dns_cli.zone_group.command(name=cli_util.override('create_zone.command_name', 'create'), help="""Creates a new zone in the specified compartment. The `compartmentId` query parameter is required if the `Content-Type` header for the request is `text/dns`.""")
@option('--compartment-id', required=True, help="""The OCID of the compartment the resource belongs to.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'external-masters': {'module': 'dns', 'class': 'list[ExternalMaster]'}}, output_type={'module': 'dns', 'class': 'Zone'})
@cli_util.wrap_exceptions
def create_zone(ctx, **kwargs):
    ctx.invoke(dns_cli.create_zone, **kwargs)


dns_cli.dns_root_group.commands.pop(dns_cli.rr_set_group.name)
dns_cli.dns_root_group.commands.pop(dns_cli.record_collection_group.name)
dns_cli.dns_root_group.commands.pop(dns_cli.records_group.name)
dns_cli.dns_root_group.commands.pop(dns_cli.zones_group.name)

dns_cli.zone_group.add_command(dns_cli.get_zone)
dns_cli.zone_group.add_command(dns_cli.list_zones)

# zone records
zone.add_command(dns_cli.get_zone_records)
zone.add_command(dns_cli.patch_zone_records)
zone.add_command(dns_cli.update_zone_records)

# domain records
domain.add_command(dns_cli.patch_domain_records)
domain.add_command(dns_cli.update_domain_records)
domain.add_command(dns_cli.get_domain_records)
domain.add_command(dns_cli.delete_domain_records)

# rrset
rrset.add_command(dns_cli.update_rr_set)
rrset.add_command(dns_cli.get_rr_set)
rrset.add_command(dns_cli.patch_rr_set)
rrset.add_command(dns_cli.delete_rr_set)
