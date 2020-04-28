# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
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
from services.limits.src.oci_cli_limits.generated import limits_service_cli


@click.command(cli_util.override('limits.limits_root_group.command_name', 'limits'), cls=CommandGroupWithAlias, help=cli_util.override('limits.limits_root_group.help', """APIs that interact with the resource limits of a specific resource type"""), short_help=cli_util.override('limits.limits_root_group.short_help', """Service limits APIs"""))
@cli_util.help_option_group
def limits_root_group():
    pass


@click.command(cli_util.override('limits.service_group.command_name', 'service'), cls=CommandGroupWithAlias, help="""A specific OCI service supported by resource limits.""")
@cli_util.help_option_group
def service_group():
    pass


@click.command(cli_util.override('limits.limit_value_group.command_name', 'limit-value'), cls=CommandGroupWithAlias, help="""The value of a specific resource limit.""")
@cli_util.help_option_group
def limit_value_group():
    pass


@click.command(cli_util.override('limits.limit_definition_group.command_name', 'limit-definition'), cls=CommandGroupWithAlias, help="""The metadata specific to a resource limit definition.""")
@cli_util.help_option_group
def limit_definition_group():
    pass


@click.command(cli_util.override('limits.resource_availability_group.command_name', 'resource-availability'), cls=CommandGroupWithAlias, help="""The availability of a given resource limit, based on the usage, tenant service limits and quotas set for the tenancy. Note: We cannot guarantee this data for all the limits. In those cases, these fields will be empty.""")
@cli_util.help_option_group
def resource_availability_group():
    pass


limits_service_cli.limits_service_group.add_command(limits_root_group)
limits_root_group.add_command(service_group)
limits_root_group.add_command(limit_value_group)
limits_root_group.add_command(limit_definition_group)
limits_root_group.add_command(resource_availability_group)
# oci limits limits --> oci limits
limits_service_cli.limits_service_group.commands.pop(limits_root_group.name)
limits_service_cli.limits_service_group.add_command(service_group)
limits_service_cli.limits_service_group.add_command(limit_value_group)
limits_service_cli.limits_service_group.add_command(limit_definition_group)
limits_service_cli.limits_service_group.add_command(resource_availability_group)


@resource_availability_group.command(name=cli_util.override('limits.get_resource_availability.command_name', 'get'), help=u"""For a given compartmentId, resource limit name, and scope, returns the following:   - the number of available resources associated with the given limit   - the usage in the selected compartment for the given limit   Note: not all resource limits support this API. If the value is not available, the API will return 404.""")
@cli_util.option('--service-name', required=True, help=u"""The service name of the target quota.""")
@cli_util.option('--limit-name', required=True, help=u"""The limit name for which to fetch the data.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment for which data is being fetched.""")
@cli_util.option('--availability-domain', help=u"""This field is mandatory if the scopeType of the target resource limit is AD. Otherwise, this field should be omitted. If the above requirements are not met, the API will return a 400 - InvalidParameter response.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'limits', 'class': 'ResourceAvailability'})
@cli_util.wrap_exceptions
def get_resource_availability(ctx, from_json, service_name, limit_name, compartment_id, availability_domain):

    if isinstance(service_name, six.string_types) and len(service_name.strip()) == 0:
        raise click.UsageError('Parameter --service-name cannot be whitespace or empty string')

    if isinstance(limit_name, six.string_types) and len(limit_name.strip()) == 0:
        raise click.UsageError('Parameter --limit-name cannot be whitespace or empty string')

    kwargs = {}
    if availability_domain is not None:
        kwargs['availability_domain'] = availability_domain
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('limits', 'limits', ctx)
    result = client.get_resource_availability(
        service_name=service_name,
        limit_name=limit_name,
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@limit_definition_group.command(name=cli_util.override('limits.list_limit_definitions.command_name', 'list'), help=u"""Includes a list of resource limits that are currently supported. If the 'areQuotasSupported' property is true, you can create quota policies on top of this limit at the compartment level.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the parent compartment (remember that the tenancy is simply the root compartment).""")
@cli_util.option('--service-name', help=u"""The target service name.""")
@cli_util.option('--name', help=u"""Optional field, filter for a specific resource limit.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["name", "description"]), help=u"""The field to sort by.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'. By default it will be ascending.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'limits', 'class': 'list[LimitDefinitionSummary]'})
@cli_util.wrap_exceptions
def list_limit_definitions(ctx, from_json, all_pages, page_size, compartment_id, service_name, name, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if service_name is not None:
        kwargs['service_name'] = service_name
    if name is not None:
        kwargs['name'] = name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('limits', 'limits', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_limit_definitions,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_limit_definitions,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_limit_definitions(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@limit_value_group.command(name=cli_util.override('limits.list_limit_values.command_name', 'list'), help=u"""Includes a full list of resource limits belonging to a given service.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the parent compartment (remember that the tenancy is simply the root compartment).""")
@cli_util.option('--service-name', required=True, help=u"""The target service name""")
@cli_util.option('--scope-type', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "REGION", "AD"]), help=u"""Filter entries by scope type.""")
@cli_util.option('--availability-domain', help=u"""Filter entries by availability domain. This implies that only AD-specific values will be returned.""")
@cli_util.option('--name', help=u"""Optional field, can be used to see a specific resource limit value.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["name"]), help=u"""The field to sort by. We will be implicitly sorting by availabilityDomain, as a second level field, if available.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'. By default it will be ascending.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'limits', 'class': 'list[LimitValueSummary]'})
@cli_util.wrap_exceptions
def list_limit_values(ctx, from_json, all_pages, page_size, compartment_id, service_name, scope_type, availability_domain, name, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    if sort_by and not availability_domain and not all_pages:
        raise click.UsageError('You must provide an --availability-domain when doing a --sort-by, unless you specify the --all parameter')

    kwargs = {}
    if scope_type is not None:
        kwargs['scope_type'] = scope_type
    if availability_domain is not None:
        kwargs['availability_domain'] = availability_domain
    if name is not None:
        kwargs['name'] = name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('limits', 'limits', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_limit_values,
            compartment_id=compartment_id,
            service_name=service_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_limit_values,
            limit,
            page_size,
            compartment_id=compartment_id,
            service_name=service_name,
            **kwargs
        )
    else:
        result = client.list_limit_values(
            compartment_id=compartment_id,
            service_name=service_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@service_group.command(name=cli_util.override('limits.list_services.command_name', 'list'), help=u"""Returns the list of supported services. This will include the programmatic service name, along with the friendly service name.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the parent compartment (remember that the tenancy is simply the root compartment).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["name", "description"]), help=u"""The field to sort by.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'. By default it will be ascending.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'limits', 'class': 'list[ServiceSummary]'})
@cli_util.wrap_exceptions
def list_services(ctx, from_json, all_pages, page_size, compartment_id, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('limits', 'limits', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_services,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_services,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_services(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)
