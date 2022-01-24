# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.osub_subscription.src.oci_cli_osub_subscription.generated import osub_subscription_service_cli


@click.command(cli_util.override('subscription.subscription_root_group.command_name', 'subscription'), cls=CommandGroupWithAlias, help=cli_util.override('subscription.subscription_root_group.help', """Set of APIs that return the Subscription Details, Commitment and Effective Rate Card Details"""), short_help=cli_util.override('subscription.subscription_root_group.short_help', """OneSubscription API Subscription, Commitment and and Rate Card Details"""))
@cli_util.help_option_group
def subscription_root_group():
    pass


@click.command(cli_util.override('subscription.subscription_group.command_name', 'subscription'), cls=CommandGroupWithAlias, help="""Subscription summary""")
@cli_util.help_option_group
def subscription_group():
    pass


osub_subscription_service_cli.osub_subscription_service_group.add_command(subscription_root_group)
subscription_root_group.add_command(subscription_group)


@subscription_group.command(name=cli_util.override('subscription.list_subscriptions.command_name', 'list'), help=u"""This list API returns all subscriptions for a given plan number or subscription id or buyer email and provides additional parameters to include ratecard and commitment details. This API expects exactly one of the above mentioned parameters as input. If more than one parameters are provided the API will throw a 400 - invalid parameters exception and if no parameters are provided it will throw a 400 - missing parameter exception \n[Command Reference](listSubscriptions)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--plan-number', help=u"""The Plan Number""")
@cli_util.option('--subscription-id', help=u"""Line level Subscription Id""")
@cli_util.option('--buyer-email', help=u"""Buyer Email Id""")
@cli_util.option('--is-commit-info-required', type=click.BOOL, help=u"""Boolean value to decide whether commitment services will be shown""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call. Default: (`50`)

Example: `500`""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "TIMESTART"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`).""")
@cli_util.option('--x-one-gateway-subscription-id', help=u"""This header is meant to be used only for internal purposes and will be ignored on any public request. The purpose of this header is to help on Gateway to API calls identification.""")
@cli_util.option('--x-one-origin-region', help=u"""The OCI home region name in case home region is not us-ashburn-1 (IAD), e.g. ap-mumbai-1, us-phoenix-1 etc.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'osub_subscription', 'class': 'list[SubscriptionSummary]'})
@cli_util.wrap_exceptions
def list_subscriptions(ctx, from_json, all_pages, page_size, compartment_id, plan_number, subscription_id, buyer_email, is_commit_info_required, limit, page, sort_order, sort_by, x_one_gateway_subscription_id, x_one_origin_region):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if plan_number is not None:
        kwargs['plan_number'] = plan_number
    if subscription_id is not None:
        kwargs['subscription_id'] = subscription_id
    if buyer_email is not None:
        kwargs['buyer_email'] = buyer_email
    if is_commit_info_required is not None:
        kwargs['is_commit_info_required'] = is_commit_info_required
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if x_one_gateway_subscription_id is not None:
        kwargs['x_one_gateway_subscription_id'] = x_one_gateway_subscription_id
    if x_one_origin_region is not None:
        kwargs['x_one_origin_region'] = x_one_origin_region
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('osub_subscription', 'subscription', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_subscriptions,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_subscriptions,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_subscriptions(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)
