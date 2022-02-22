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
from services.data_connectivity.src.oci_cli_data_connectivity.generated import data_connectivity_service_cli


@click.command(cli_util.override('network_validation.network_validation_root_group.command_name', 'network-validation'), cls=CommandGroupWithAlias, help=cli_util.override('network_validation.network_validation_root_group.help', """Use the DCMS APIs to perform Metadata/Data operations."""), short_help=cli_util.override('network_validation.network_validation_root_group.short_help', """Data Connectivity Management API"""))
@cli_util.help_option_group
def network_validation_root_group():
    pass


@click.command(cli_util.override('network_validation.test_network_connectivity_group.command_name', 'test-network-connectivity'), cls=CommandGroupWithAlias, help="""The network validation response.""")
@cli_util.help_option_group
def test_network_connectivity_group():
    pass


data_connectivity_service_cli.data_connectivity_service_group.add_command(network_validation_root_group)
network_validation_root_group.add_command(test_network_connectivity_group)


@test_network_connectivity_group.command(name=cli_util.override('network_validation.get_network_connectivity_status_collection.command_name', 'get-network-connectivity-status-collection'), help=u"""This api is used to get Network Connectivity Status for all the Data Assets attatched to the provided Private endpoint. \n[Command Reference](getNetworkConnectivityStatusCollection)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry Ocid.""")
@cli_util.option('--endpoint-key', required=True, help=u"""The endpoint key.""")
@cli_util.option('--page', help=u"""For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""Sets the maximum number of results per page, or items to return in a paginated `List` call. See [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "timeCreated", "displayName"]), help=u"""Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_connectivity', 'class': 'NetworkConnectivityStatusCollection'})
@cli_util.wrap_exceptions
def get_network_connectivity_status_collection(ctx, from_json, registry_id, endpoint_key, page, limit, sort_by, sort_order):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(endpoint_key, six.string_types) and len(endpoint_key.strip()) == 0:
        raise click.UsageError('Parameter --endpoint-key cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'network_validation', ctx)
    result = client.get_network_connectivity_status_collection(
        registry_id=registry_id,
        endpoint_key=endpoint_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)
