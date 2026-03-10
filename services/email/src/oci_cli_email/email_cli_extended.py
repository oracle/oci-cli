# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.email.src.oci_cli_email.generated import email_cli
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
import click

email_cli.email_root_group.help = "Email Delivery Service CLI"


# oci email work-request-error-collection list-work-request-errors -> oci email work-request-error-collection list
cli_util.rename_command(email_cli, email_cli.work_request_error_collection_group, email_cli.list_work_request_errors, "list")


# oci email work-request-log-entry-collection -> oci email work-request-log
cli_util.rename_command(email_cli, email_cli.email_root_group, email_cli.work_request_log_entry_collection_group, "work-request-log")


# oci email work-request-log-entry-collection list-work-request-logs -> oci email work-request-log-entry-collection work-request-log-entry-collectionlist
cli_util.rename_command(email_cli, email_cli.work_request_log_entry_collection_group, email_cli.list_work_request_logs, "list")


# oci email email-domain -> oci email domain
cli_util.rename_command(email_cli, email_cli.email_root_group, email_cli.email_domain_group, "domain")


# oci email work-request-summary-collection list-work-requests -> oci email work-request
email_cli.work_request_summary_collection_group.commands.pop(email_cli.list_work_requests.name)
cli_util.rename_command(email_cli, email_cli.work_request_group, email_cli.list_work_requests, "list")
email_cli.email_root_group.commands.pop(email_cli.work_request_summary_collection_group.name)


# oci email work-request-error-collection -> oci email work-request-error
cli_util.rename_command(email_cli, email_cli.email_root_group, email_cli.work_request_error_collection_group, "work-request-error")

# oci email email-outbound-ip-collection -> oci email email-outbound-ip
cli_util.rename_command(email_cli, email_cli.email_root_group, email_cli.email_outbound_ip_collection_group, "email-outbound-ip")


# oci email email-outbound-ip-collection list-email-outbound-ips -> oci email email-outbound-ip-collection list
cli_util.rename_command(email_cli, email_cli.email_outbound_ip_collection_group, email_cli.list_email_outbound_ips, "list")


# oci email email-ip-pool-collection list-email-ip-pools -> oci email email-ip-pool-collection list
cli_util.rename_command(email_cli, email_cli.email_ip_pool_collection_group, email_cli.list_email_ip_pools, "list")


# Move commands under 'oci email email-ip-pool-collection' -> 'oci email email-ip-pool'
email_cli.email_root_group.commands.pop(email_cli.email_ip_pool_collection_group.name)
email_cli.email_ip_pool_group.add_command(email_cli.list_email_ip_pools)


@cli_util.copy_params_from_generated_command(email_cli.create_email_ip_pool, params_to_exclude=['last_ip_drain_period_in_hours'])
@email_cli.email_ip_pool_group.command(name=email_cli.create_email_ip_pool.name, help=email_cli.create_email_ip_pool.help)
@cli_util.option('--last-ip-drain-period', type=click.INT, help=u"""Last IP will be unassigned from the IP Pool after the period of time (in hours) specified by this parameter. Default is 24 hours.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'outbound-ips': {'module': 'email', 'class': 'list[string]'}, 'freeform-tags': {'module': 'email', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'email', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'email', 'class': 'EmailIpPool'})
@cli_util.wrap_exceptions
def create_email_ip_pool_extended(ctx, **kwargs):

    if 'last_ip_drain_period' in kwargs:
        kwargs['last_ip_drain_period_in_hours'] = kwargs['last_ip_drain_period']
        kwargs.pop('last_ip_drain_period')

    ctx.invoke(email_cli.create_email_ip_pool, **kwargs)


@cli_util.copy_params_from_generated_command(email_cli.update_email_ip_pool, params_to_exclude=['last_ip_drain_period_in_hours'])
@email_cli.email_ip_pool_group.command(name=email_cli.update_email_ip_pool.name, help=email_cli.update_email_ip_pool.help)
@cli_util.option('--last-ip-drain-period', type=click.INT, help=u"""Last IP will be unassigned from the IP Pool after the period of time (in hours) specified by this parameter. Default is 24 hours.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'email', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'email', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_email_ip_pool_extended(ctx, **kwargs):

    if 'last_ip_drain_period' in kwargs:
        kwargs['last_ip_drain_period_in_hours'] = kwargs['last_ip_drain_period']
        kwargs.pop('last_ip_drain_period')

    ctx.invoke(email_cli.update_email_ip_pool, **kwargs)
