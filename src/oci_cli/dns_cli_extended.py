# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from . import cli_util

from .aliasing import CommandGroupWithAlias
from .generated import dns_cli


@dns_cli.dns_group.command('record', cls=CommandGroupWithAlias, help="""A DNS record.""")
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
cli_util.update_param_help(dns_cli.create_zone, 'compartment_id', ' [required]', append=True)
cli_util.get_param(dns_cli.create_zone, 'compartment_id').callback = cli_util.handle_required_param

dns_cli.dns_group.add_command(dns_cli.zone_group)
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
