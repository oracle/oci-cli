# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
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


@cli.command(cli_util.override('service_manager_proxy.service_manager_proxy_root_group.command_name', 'service-manager-proxy'), cls=CommandGroupWithAlias, help=cli_util.override('service_manager_proxy.service_manager_proxy_root_group.help', """Use the Service Manager Proxy API to obtain information about SaaS environments provisioned by Service Manager.
You can get information such as service types and service environment URLs."""), short_help=cli_util.override('service_manager_proxy.service_manager_proxy_root_group.short_help', """Service Manager Proxy API"""))
@cli_util.help_option_group
def service_manager_proxy_root_group():
    pass


@click.command(cli_util.override('service_manager_proxy.service_environment_group.command_name', 'service-environment'), cls=CommandGroupWithAlias, help="""Detailed information about a service environment.

**Note:** Service URL formats may vary from the provided example.""")
@cli_util.help_option_group
def service_environment_group():
    pass


service_manager_proxy_root_group.add_command(service_environment_group)


@service_environment_group.command(name=cli_util.override('service_manager_proxy.get_service_environment.command_name', 'get'), help=u"""Get the detailed information for a specific service environment. \n[Command Reference](getServiceEnvironment)""")
@cli_util.option('--service-environment-id', required=True, help=u"""The unique identifier associated with the service environment.

**Note:** Not an [OCID].""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] for the compartment.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_manager_proxy', 'class': 'ServiceEnvironment'})
@cli_util.wrap_exceptions
def get_service_environment(ctx, from_json, service_environment_id, compartment_id):

    if isinstance(service_environment_id, six.string_types) and len(service_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --service-environment-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_manager_proxy', 'service_manager_proxy', ctx)
    result = client.get_service_environment(
        service_environment_id=service_environment_id,
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@service_environment_group.command(name=cli_util.override('service_manager_proxy.list_service_environments.command_name', 'list'), help=u"""List the details of Software as a Service (SaaS) environments provisioned by Service Manager. Information includes the service instance endpoints and service definition details. \n[Command Reference](listServiceEnvironments)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] for the compartment.""")
@cli_util.option('--service-environment-id', help=u"""The unique identifier associated with the service environment.

**Note:** Not an [OCID].""")
@cli_util.option('--service-environment-type', help=u"""The environment's service definition type. For example, \"RGBUOROMS\" is the service definition type for \"Oracle Retail Order Management Cloud Service\".""")
@cli_util.option('--limit', type=click.INT, help=u"""How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["ID"]), help=u"""The field to sort by. Only one sort order may be provided. ID is default ordered as ascending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either `ASC` or `DESC`.""")
@cli_util.option('--display-name', help=u"""The display name of the resource.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_manager_proxy', 'class': 'ServiceEnvironmentCollection'})
@cli_util.wrap_exceptions
def list_service_environments(ctx, from_json, all_pages, page_size, compartment_id, service_environment_id, service_environment_type, limit, page, sort_by, sort_order, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if service_environment_id is not None:
        kwargs['service_environment_id'] = service_environment_id
    if service_environment_type is not None:
        kwargs['service_environment_type'] = service_environment_type
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if display_name is not None:
        kwargs['display_name'] = display_name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_manager_proxy', 'service_manager_proxy', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_service_environments,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_service_environments,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_service_environments(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)
