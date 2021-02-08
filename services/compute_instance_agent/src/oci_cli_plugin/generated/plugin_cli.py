# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
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
from services.compute_instance_agent.src.oci_cli_compute_instance_agent.generated import instance_agent_service_cli


@click.command(cli_util.override('plugin.plugin_root_group.command_name', 'plugin'), cls=CommandGroupWithAlias, help=cli_util.override('plugin.plugin_root_group.help', """API for the Oracle Cloud Agent software running on compute instances. Oracle Cloud Agent
is a lightweight process that monitors and manages compute instances."""), short_help=cli_util.override('plugin.plugin_root_group.short_help', """Oracle Cloud Agent API"""))
@cli_util.help_option_group
def plugin_root_group():
    pass


@click.command(cli_util.override('plugin.plugin_group.command_name', 'plugin'), cls=CommandGroupWithAlias, help="""The agent plugin""")
@cli_util.help_option_group
def plugin_group():
    pass


instance_agent_service_cli.instance_agent_service_group.add_command(plugin_root_group)
plugin_root_group.add_command(plugin_group)


@plugin_group.command(name=cli_util.override('plugin.get_instance_agent_plugin.command_name', 'get-instance-agent'), help=u"""The API to get information for a plugin. \n[Command Reference](getInstanceAgentPlugin)""")
@cli_util.option('--instanceagent-id', required=True, help=u"""The OCID of the instance.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--plugin-name', required=True, help=u"""The name of the plugin.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'compute_instance_agent', 'class': 'InstanceAgentPlugin'})
@cli_util.wrap_exceptions
def get_instance_agent_plugin(ctx, from_json, instanceagent_id, compartment_id, plugin_name):

    if isinstance(instanceagent_id, six.string_types) and len(instanceagent_id.strip()) == 0:
        raise click.UsageError('Parameter --instanceagent-id cannot be whitespace or empty string')

    if isinstance(plugin_name, six.string_types) and len(plugin_name.strip()) == 0:
        raise click.UsageError('Parameter --plugin-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('compute_instance_agent', 'plugin', ctx)
    result = client.get_instance_agent_plugin(
        instanceagent_id=instanceagent_id,
        compartment_id=compartment_id,
        plugin_name=plugin_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@plugin_group.command(name=cli_util.override('plugin.list_instance_agent_plugins.command_name', 'list-instance-agent'), help=u"""The API to get one or more plugin information. \n[Command Reference](listInstanceAgentPlugins)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--instanceagent-id', required=True, help=u"""The OCID of the instance.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["RUNNING", "STOPPED", "NOT_SUPPORTED", "INVALID"]), help=u"""The plugin status""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for `TIMECREATED` is descending.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The `DISPLAYNAME` sort order is case sensitive.""")
@cli_util.option('--name', help=u"""The plugin name""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'compute_instance_agent', 'class': 'list[InstanceAgentPluginSummary]'})
@cli_util.wrap_exceptions
def list_instance_agent_plugins(ctx, from_json, all_pages, page_size, compartment_id, instanceagent_id, status, page, limit, sort_by, sort_order, name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(instanceagent_id, six.string_types) and len(instanceagent_id.strip()) == 0:
        raise click.UsageError('Parameter --instanceagent-id cannot be whitespace or empty string')

    kwargs = {}
    if status is not None:
        kwargs['status'] = status
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if name is not None:
        kwargs['name'] = name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('compute_instance_agent', 'plugin', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_instance_agent_plugins,
            compartment_id=compartment_id,
            instanceagent_id=instanceagent_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_instance_agent_plugins,
            limit,
            page_size,
            compartment_id=compartment_id,
            instanceagent_id=instanceagent_id,
            **kwargs
        )
    else:
        result = client.list_instance_agent_plugins(
            compartment_id=compartment_id,
            instanceagent_id=instanceagent_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)
