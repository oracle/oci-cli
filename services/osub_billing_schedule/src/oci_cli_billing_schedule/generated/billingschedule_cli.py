# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('osub_billing_schedule.osub_billing_schedule_root_group.command_name', 'osub-billing-schedule'), cls=CommandGroupWithAlias, help=cli_util.override('osub_billing_schedule.osub_billing_schedule_root_group.help', """OneSubscription API for Billing Schedule information"""), short_help=cli_util.override('osub_billing_schedule.osub_billing_schedule_root_group.short_help', """OneSubscription API Billing Schedule"""))
@cli_util.help_option_group
def osub_billing_schedule_root_group():
    pass


@click.command(cli_util.override('osub_billing_schedule.billing_schedule_summary_group.command_name', 'billing-schedule-summary'), cls=CommandGroupWithAlias, help="""Billing schedule details related to Subscription Id""")
@cli_util.help_option_group
def billing_schedule_summary_group():
    pass


osub_billing_schedule_root_group.add_command(billing_schedule_summary_group)


@billing_schedule_summary_group.command(name=cli_util.override('osub_billing_schedule.list_billing_schedules.command_name', 'list-billing-schedules'), help=u"""This list API returns all billing schedules for given subscription id and for a particular Subscribed Service if provided \n[Command Reference](listBillingSchedules)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--subscription-id', required=True, help=u"""This param is used to get only the billing schedules for a particular Subscription Id""")
@cli_util.option('--subscribed-service-id', help=u"""This param is used to get only the billing schedules for a particular Subscribed Service""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call. Default: (`50`)

Example: '500'""")
@cli_util.option('--page', help=u"""The value of the 'opc-next-page' response header from the previous \"List\" call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending ('ASC') or descending ('DESC').""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["ORDERNUMBER", "TIMEINVOICING"]), help=u"""The field to sort by. You can provide one sort order ('sortOrder').""")
@cli_util.option('--x-one-origin-region', help=u"""The OCI home region name in case home region is not us-ashburn-1 (IAD), e.g. ap-mumbai-1, us-phoenix-1 etc.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'osub_billing_schedule', 'class': 'list[BillingScheduleSummary]'})
@cli_util.wrap_exceptions
def list_billing_schedules(ctx, from_json, all_pages, page_size, compartment_id, subscription_id, subscribed_service_id, limit, page, sort_order, sort_by, x_one_origin_region):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if subscribed_service_id is not None:
        kwargs['subscribed_service_id'] = subscribed_service_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if x_one_origin_region is not None:
        kwargs['x_one_origin_region'] = x_one_origin_region
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('osub_billing_schedule', 'billing_schedule', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_billing_schedules,
            compartment_id=compartment_id,
            subscription_id=subscription_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_billing_schedules,
            limit,
            page_size,
            compartment_id=compartment_id,
            subscription_id=subscription_id,
            **kwargs
        )
    else:
        result = client.list_billing_schedules(
            compartment_id=compartment_id,
            subscription_id=subscription_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)
