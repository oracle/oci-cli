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
from services.osp_gateway.src.oci_cli_osp_gateway.generated import osp_gateway_service_cli


@click.command(cli_util.override('invoice_service.invoice_service_root_group.command_name', 'invoice-service'), cls=CommandGroupWithAlias, help=cli_util.override('invoice_service.invoice_service_root_group.help', """This site describes all the Rest endpoints of OSP Gateway."""), short_help=cli_util.override('invoice_service.invoice_service_root_group.short_help', """OSP Gateway API"""))
@cli_util.help_option_group
def invoice_service_root_group():
    pass


@click.command(cli_util.override('invoice_service.invoice_group.command_name', 'invoice'), cls=CommandGroupWithAlias, help="""Invoice details""")
@cli_util.help_option_group
def invoice_group():
    pass


osp_gateway_service_cli.osp_gateway_service_group.add_command(invoice_service_root_group)
invoice_service_root_group.add_command(invoice_group)


@invoice_group.command(name=cli_util.override('invoice_service.download_pdf_content.command_name', 'download-pdf-content'), help=u"""Returns an invoice in pdf format \n[Command Reference](downloadPdfContent)""")
@cli_util.option('--osp-home-region', required=True, help=u"""The home region's public name of the logged in user.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--internal-invoice-id', required=True, help=u"""The identifier of the invoice.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def download_pdf_content(ctx, from_json, file, osp_home_region, compartment_id, internal_invoice_id):

    if isinstance(internal_invoice_id, six.string_types) and len(internal_invoice_id.strip()) == 0:
        raise click.UsageError('Parameter --internal-invoice-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('osp_gateway', 'invoice_service', ctx)
    result = client.download_pdf_content(
        osp_home_region=osp_home_region,
        compartment_id=compartment_id,
        internal_invoice_id=internal_invoice_id,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@invoice_group.command(name=cli_util.override('invoice_service.get_invoice.command_name', 'get'), help=u"""Returns an invoice by invoice id \n[Command Reference](getInvoice)""")
@cli_util.option('--osp-home-region', required=True, help=u"""The home region's public name of the logged in user.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--internal-invoice-id', required=True, help=u"""The identifier of the invoice.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'osp_gateway', 'class': 'Invoice'})
@cli_util.wrap_exceptions
def get_invoice(ctx, from_json, osp_home_region, compartment_id, internal_invoice_id):

    if isinstance(internal_invoice_id, six.string_types) and len(internal_invoice_id.strip()) == 0:
        raise click.UsageError('Parameter --internal-invoice-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('osp_gateway', 'invoice_service', ctx)
    result = client.get_invoice(
        osp_home_region=osp_home_region,
        compartment_id=compartment_id,
        internal_invoice_id=internal_invoice_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@invoice_group.command(name=cli_util.override('invoice_service.list_invoice_lines.command_name', 'list-invoice-lines'), help=u"""Returns the invoice product list by invoice id \n[Command Reference](listInvoiceLines)""")
@cli_util.option('--osp-home-region', required=True, help=u"""The home region's public name of the logged in user.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--internal-invoice-id', required=True, help=u"""The identifier of the invoice.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the opc-next-page response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'osp_gateway', 'class': 'InvoiceLineCollection'})
@cli_util.wrap_exceptions
def list_invoice_lines(ctx, from_json, all_pages, page_size, osp_home_region, compartment_id, internal_invoice_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(internal_invoice_id, six.string_types) and len(internal_invoice_id.strip()) == 0:
        raise click.UsageError('Parameter --internal-invoice-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('osp_gateway', 'invoice_service', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_invoice_lines,
            osp_home_region=osp_home_region,
            compartment_id=compartment_id,
            internal_invoice_id=internal_invoice_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_invoice_lines,
            limit,
            page_size,
            osp_home_region=osp_home_region,
            compartment_id=compartment_id,
            internal_invoice_id=internal_invoice_id,
            **kwargs
        )
    else:
        result = client.list_invoice_lines(
            osp_home_region=osp_home_region,
            compartment_id=compartment_id,
            internal_invoice_id=internal_invoice_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@invoice_group.command(name=cli_util.override('invoice_service.list_invoices.command_name', 'list'), help=u"""Returns a list of invoices \n[Command Reference](listInvoices)""")
@cli_util.option('--osp-home-region', required=True, help=u"""The home region's public name of the logged in user.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--invoice-id', help=u"""The invoice query param (not unique).""")
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["HARDWARE", "SUBSCRIPTION", "SUPPORT", "LICENSE", "EDUCATION", "CONSULTING", "SERVICE", "USAGE"]), multiple=True, help=u"""A filter to only return resources that match the given type exactly.""")
@cli_util.option('--search-text', help=u"""A filter to only return resources that match the given value. Looking for partial matches in the following fileds: Invoice No., Reference No. (plan number), Payment Ref, Total Amount(plan number), Balance Due(plan number) and Party/Customer Name""")
@cli_util.option('--time-invoice-start', type=custom_types.CLI_DATETIME, help=u"""description: Start time (UTC) of the target invoice date range for which to fetch invoice data (inclusive).""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-invoice-end', type=custom_types.CLI_DATETIME, help=u"""description: End time (UTC) of the target invoice date range for which to fetch invoice data (exclusive).""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-payment-start', type=custom_types.CLI_DATETIME, help=u"""description: Start time (UTC) of the target payment date range for which to fetch invoice data (inclusive).""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-payment-end', type=custom_types.CLI_DATETIME, help=u"""description: End time (UTC) of the target payment date range for which to fetch invoice data (exclusive).""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["OPEN", "PAST_DUE", "PAYMENT_SUBMITTED", "CLOSED"]), multiple=True, help=u"""A filter to only return resources that match one of the status elements.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the opc-next-page response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["INVOICE_NO", "REF_NO", "STATUS", "TYPE", "INVOICE_DATE", "DUE_DATE", "PAYM_REF", "TOTAL_AMOUNT", "BALANCE_DUE"]), help=u"""The field to sort by. Only one field can be selected for sorting.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use (ascending or descending).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'osp_gateway', 'class': 'InvoiceCollection'})
@cli_util.wrap_exceptions
def list_invoices(ctx, from_json, all_pages, page_size, osp_home_region, compartment_id, invoice_id, type, search_text, time_invoice_start, time_invoice_end, time_payment_start, time_payment_end, status, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if invoice_id is not None:
        kwargs['invoice_id'] = invoice_id
    if type is not None and len(type) > 0:
        kwargs['type'] = type
    if search_text is not None:
        kwargs['search_text'] = search_text
    if time_invoice_start is not None:
        kwargs['time_invoice_start'] = time_invoice_start
    if time_invoice_end is not None:
        kwargs['time_invoice_end'] = time_invoice_end
    if time_payment_start is not None:
        kwargs['time_payment_start'] = time_payment_start
    if time_payment_end is not None:
        kwargs['time_payment_end'] = time_payment_end
    if status is not None and len(status) > 0:
        kwargs['status'] = status
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('osp_gateway', 'invoice_service', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_invoices,
            osp_home_region=osp_home_region,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_invoices,
            limit,
            page_size,
            osp_home_region=osp_home_region,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_invoices(
            osp_home_region=osp_home_region,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@invoice_group.command(name=cli_util.override('invoice_service.pay_invoice.command_name', 'pay'), help=u"""Pay an invoice \n[Command Reference](payInvoice)""")
@cli_util.option('--osp-home-region', required=True, help=u"""The home region's public name of the logged in user.""")
@cli_util.option('--internal-invoice-id', required=True, help=u"""The identifier of the invoice.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--email', required=True, help=u"""User email""")
@cli_util.option('--language-code', help=u"""Language code""")
@cli_util.option('--return-url', help=u"""Callback URL""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'osp_gateway', 'class': 'PayInvoiceReceipt'})
@cli_util.wrap_exceptions
def pay_invoice(ctx, from_json, osp_home_region, internal_invoice_id, compartment_id, email, language_code, return_url, if_match):

    if isinstance(internal_invoice_id, six.string_types) and len(internal_invoice_id.strip()) == 0:
        raise click.UsageError('Parameter --internal-invoice-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['email'] = email

    if language_code is not None:
        _details['languageCode'] = language_code

    if return_url is not None:
        _details['returnUrl'] = return_url

    client = cli_util.build_client('osp_gateway', 'invoice_service', ctx)
    result = client.pay_invoice(
        osp_home_region=osp_home_region,
        internal_invoice_id=internal_invoice_id,
        compartment_id=compartment_id,
        pay_invoice_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
