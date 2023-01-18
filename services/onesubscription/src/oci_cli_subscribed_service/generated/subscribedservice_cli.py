# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
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
from services.onesubscription.src.oci_cli_onesubscription.generated import onesubscription_service_cli


@click.command(cli_util.override('subscribed_service.subscribed_service_root_group.command_name', 'subscribed-service'), cls=CommandGroupWithAlias, help=cli_util.override('subscribed_service.subscribed_service_root_group.help', """OneSubscription APIs"""), short_help=cli_util.override('subscribed_service.subscribed_service_root_group.short_help', """OneSubscription APIs"""))
@cli_util.help_option_group
def subscribed_service_root_group():
    pass


@click.command(cli_util.override('subscribed_service.subscribed_service_group.command_name', 'subscribed-service'), cls=CommandGroupWithAlias, help="""Subscribed service contract details""")
@cli_util.help_option_group
def subscribed_service_group():
    pass


onesubscription_service_cli.onesubscription_service_group.add_command(subscribed_service_root_group)
subscribed_service_root_group.add_command(subscribed_service_group)


@subscribed_service_group.command(name=cli_util.override('subscribed_service.get_subscribed_service.command_name', 'get'), help=u"""This API returns the subscribed service details corresponding to the id provided \n[Command Reference](getSubscribedService)""")
@cli_util.option('--subscribed-service-id', required=True, help=u"""The Subscribed Service Id""")
@cli_util.option('--fields', multiple=True, help=u"""Partial response refers to an optimization technique offered by the RESTful web APIs to return only the information (fields) required by the client. In this mechanism, the client sends the required field names as the query parameters for an API to the server, and the server trims down the default response content by removing the fields that are not required by the client. The parameter used to control what fields to return should be a query string parameter called \"fields\" of type array, and usecollectionFormat""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'onesubscription', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'onesubscription', 'class': 'list[string]'}}, output_type={'module': 'onesubscription', 'class': 'SubscribedService'})
@cli_util.wrap_exceptions
def get_subscribed_service(ctx, from_json, subscribed_service_id, fields):

    if isinstance(subscribed_service_id, six.string_types) and len(subscribed_service_id.strip()) == 0:
        raise click.UsageError('Parameter --subscribed-service-id cannot be whitespace or empty string')

    kwargs = {}
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('onesubscription', 'subscribed_service', ctx)
    result = client.get_subscribed_service(
        subscribed_service_id=subscribed_service_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@subscribed_service_group.command(name=cli_util.override('subscribed_service.list_subscribed_services.command_name', 'list'), help=u"""This list API returns all subscribed services for given Subscription ID \n[Command Reference](listSubscribedServices)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the root compartment.""")
@cli_util.option('--subscription-id', required=True, help=u"""Line level Subscription Id""")
@cli_util.option('--order-line-id', type=click.INT, help=u"""Order Line identifier at subscribed service level . This identifier is originated in Order Management module. Default is null.""")
@cli_util.option('--status', help=u"""This param is used to filter subscribed services based on its status""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call. Default: (`50`)

Example: '500'""")
@cli_util.option('--page', help=u"""The value of the 'opc-next-page' response header from the previous \"List\" call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending ('ASC') or descending ('DESC').""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["ORDERNUMBER", "TIMEINVOICING"]), help=u"""The field to sort by. You can provide one sort order ('sortOrder').""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'onesubscription', 'class': 'list[SubscribedServiceSummary]'})
@cli_util.wrap_exceptions
def list_subscribed_services(ctx, from_json, all_pages, page_size, compartment_id, subscription_id, order_line_id, status, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if order_line_id is not None:
        kwargs['order_line_id'] = order_line_id
    if status is not None:
        kwargs['status'] = status
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('onesubscription', 'subscribed_service', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_subscribed_services,
            compartment_id=compartment_id,
            subscription_id=subscription_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_subscribed_services,
            limit,
            page_size,
            compartment_id=compartment_id,
            subscription_id=subscription_id,
            **kwargs
        )
    else:
        result = client.list_subscribed_services(
            compartment_id=compartment_id,
            subscription_id=subscription_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)
