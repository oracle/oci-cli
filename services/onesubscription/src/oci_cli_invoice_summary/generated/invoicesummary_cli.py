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


@click.command(cli_util.override('invoice_summary.invoice_summary_root_group.command_name', 'invoice-summary'), cls=CommandGroupWithAlias, help=cli_util.override('invoice_summary.invoice_summary_root_group.help', """OneSubscription APIs"""), short_help=cli_util.override('invoice_summary.invoice_summary_root_group.short_help', """OneSubscription APIs"""))
@cli_util.help_option_group
def invoice_summary_root_group():
    pass


@click.command(cli_util.override('invoice_summary.invoiceline_computed_usage_group.command_name', 'invoiceline-computed-usage'), cls=CommandGroupWithAlias, help="""Computed Usage Summary object""")
@cli_util.help_option_group
def invoiceline_computed_usage_group():
    pass


@click.command(cli_util.override('invoice_summary.invoice_group.command_name', 'invoice'), cls=CommandGroupWithAlias, help="""Invoice details""")
@cli_util.help_option_group
def invoice_group():
    pass


onesubscription_service_cli.onesubscription_service_group.add_command(invoice_summary_root_group)
invoice_summary_root_group.add_command(invoiceline_computed_usage_group)
invoice_summary_root_group.add_command(invoice_group)


@invoiceline_computed_usage_group.command(name=cli_util.override('invoice_summary.list_invoiceline_computed_usages.command_name', 'list'), help=u"""This is a collection API which returns a list of Invoiced Computed Usages for given Invoiceline id. \n[Command Reference](listInvoicelineComputedUsages)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the root compartment.""")
@cli_util.option('--invoice-line-id', required=True, help=u"""Invoice Line Identifier - Primary Key SPM""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending ('ASC') or descending ('DESC').""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "meteredOnDate"]), help=u"""The field to sort by Invoiced Computed Usages. You can provide one sort order (`sortOrder`).""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call. Default: (`50`)

Example: '500'""")
@cli_util.option('--page', help=u"""The value of the 'opc-next-page' response header from the previous \"List\" call.""")
@cli_util.option('--fields', multiple=True, help=u"""Partial response refers to an optimization technique offered by the RESTful web APIs to return only the information (fields) required by the client. This parameter is used to control what fields to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'onesubscription', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'onesubscription', 'class': 'list[string]'}}, output_type={'module': 'onesubscription', 'class': 'list[InvoicelineComputedUsageSummary]'})
@cli_util.wrap_exceptions
def list_invoiceline_computed_usages(ctx, from_json, all_pages, page_size, compartment_id, invoice_line_id, sort_order, sort_by, limit, page, fields):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('onesubscription', 'invoice_summary', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_invoiceline_computed_usages,
            compartment_id=compartment_id,
            invoice_line_id=invoice_line_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_invoiceline_computed_usages,
            limit,
            page_size,
            compartment_id=compartment_id,
            invoice_line_id=invoice_line_id,
            **kwargs
        )
    else:
        result = client.list_invoiceline_computed_usages(
            compartment_id=compartment_id,
            invoice_line_id=invoice_line_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@invoice_group.command(name=cli_util.override('invoice_summary.list_invoices.command_name', 'list'), help=u"""This is a collection API which returns a list of Invoices for given filters. \n[Command Reference](listInvoices)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the root compartment.""")
@cli_util.option('--ar-customer-transaction-id', required=True, help=u"""AR Unique identifier for an invoice .""")
@cli_util.option('--time-from', type=custom_types.CLI_DATETIME, help=u"""Initial date to filter Invoice data in SPM.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-to', type=custom_types.CLI_DATETIME, help=u"""Final date to filter Invoice data in SPM.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending ('ASC') or descending ('DESC').""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["ORDERNUMBER", "TIMEINVOICING"]), help=u"""The field to sort by. You can provide one sort order ('sortOrder').""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call. Default: (`50`)

Example: '500'""")
@cli_util.option('--page', help=u"""The value of the 'opc-next-page' response header from the previous \"List\" call.""")
@cli_util.option('--fields', multiple=True, help=u"""Partial response refers to an optimization technique offered by the RESTful web APIs to return only the information (fields) required by the client. This parameter is used to control what fields to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'onesubscription', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'onesubscription', 'class': 'list[string]'}}, output_type={'module': 'onesubscription', 'class': 'list[InvoiceSummary]'})
@cli_util.wrap_exceptions
def list_invoices(ctx, from_json, all_pages, page_size, compartment_id, ar_customer_transaction_id, time_from, time_to, sort_order, sort_by, limit, page, fields):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if time_from is not None:
        kwargs['time_from'] = time_from
    if time_to is not None:
        kwargs['time_to'] = time_to
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('onesubscription', 'invoice_summary', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_invoices,
            compartment_id=compartment_id,
            ar_customer_transaction_id=ar_customer_transaction_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_invoices,
            limit,
            page_size,
            compartment_id=compartment_id,
            ar_customer_transaction_id=ar_customer_transaction_id,
            **kwargs
        )
    else:
        result = client.list_invoices(
            compartment_id=compartment_id,
            ar_customer_transaction_id=ar_customer_transaction_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)
