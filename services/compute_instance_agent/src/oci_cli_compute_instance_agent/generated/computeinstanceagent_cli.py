# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
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


@cli.command(cli_util.override('instance_agent.instance_agent_root_group.command_name', 'instance-agent'), cls=CommandGroupWithAlias, help=cli_util.override('instance_agent.instance_agent_root_group.help', """Instance Agent Service API"""), short_help=cli_util.override('instance_agent.instance_agent_root_group.short_help', """InstanceAgentService API"""))
@cli_util.help_option_group
def instance_agent_root_group():
    pass


@click.command(cli_util.override('instance_agent.instance_agent_command_group.command_name', 'instance-agent-command'), cls=CommandGroupWithAlias, help="""The command payload.""")
@cli_util.help_option_group
def instance_agent_command_group():
    pass


@click.command(cli_util.override('instance_agent.instance_agent_command_execution_group.command_name', 'instance-agent-command-execution'), cls=CommandGroupWithAlias, help="""A command's execution summary.""")
@cli_util.help_option_group
def instance_agent_command_execution_group():
    pass


instance_agent_root_group.add_command(instance_agent_command_group)
instance_agent_root_group.add_command(instance_agent_command_execution_group)


@instance_agent_command_group.command(name=cli_util.override('instance_agent.cancel_instance_agent_command.command_name', 'cancel'), help=u"""Cancel a command. Cancel is best effort attempt. If the commmand has already completed it will skip cancel. \n[Command Reference](cancelInstanceAgentCommand)""")
@cli_util.option('--instance-agent-command-id', required=True, help=u"""The OCID of the command.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_instance_agent_command(ctx, from_json, instance_agent_command_id, if_match):

    if isinstance(instance_agent_command_id, six.string_types) and len(instance_agent_command_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-agent-command-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('compute_instance_agent', 'compute_instance_agent', ctx)
    result = client.cancel_instance_agent_command(
        instance_agent_command_id=instance_agent_command_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@instance_agent_command_group.command(name=cli_util.override('instance_agent.create_instance_agent_command.command_name', 'create'), help=u"""Create command for one or more managed instances \n[Command Reference](createInstanceAgentCommand)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment you want to create the command.""")
@cli_util.option('--execution-time-out-in-seconds', required=True, type=click.INT, help=u"""Command execution time limit. Zero means no timeout.""")
@cli_util.option('--target', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--content', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name for the command. It does not have to be unique. Avoid entering confidential information. Example: `Database Backup Command`""")
@json_skeleton_utils.get_cli_json_input_option({'target': {'module': 'compute_instance_agent', 'class': 'InstanceAgentCommandTarget'}, 'content': {'module': 'compute_instance_agent', 'class': 'InstanceAgentCommandContent'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'target': {'module': 'compute_instance_agent', 'class': 'InstanceAgentCommandTarget'}, 'content': {'module': 'compute_instance_agent', 'class': 'InstanceAgentCommandContent'}}, output_type={'module': 'compute_instance_agent', 'class': 'InstanceAgentCommand'})
@cli_util.wrap_exceptions
def create_instance_agent_command(ctx, from_json, compartment_id, execution_time_out_in_seconds, target, content, display_name):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['executionTimeOutInSeconds'] = execution_time_out_in_seconds
    _details['target'] = cli_util.parse_json_parameter("target", target)
    _details['content'] = cli_util.parse_json_parameter("content", content)

    if display_name is not None:
        _details['displayName'] = display_name

    client = cli_util.build_client('compute_instance_agent', 'compute_instance_agent', ctx)
    result = client.create_instance_agent_command(
        create_instance_agent_command_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@instance_agent_command_group.command(name=cli_util.override('instance_agent.get_instance_agent_command.command_name', 'get'), help=u"""Gets information about the specified instance agent commandId. \n[Command Reference](getInstanceAgentCommand)""")
@cli_util.option('--instance-agent-command-id', required=True, help=u"""The OCID of the command.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'compute_instance_agent', 'class': 'InstanceAgentCommand'})
@cli_util.wrap_exceptions
def get_instance_agent_command(ctx, from_json, instance_agent_command_id):

    if isinstance(instance_agent_command_id, six.string_types) and len(instance_agent_command_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-agent-command-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('compute_instance_agent', 'compute_instance_agent', ctx)
    result = client.get_instance_agent_command(
        instance_agent_command_id=instance_agent_command_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@instance_agent_command_execution_group.command(name=cli_util.override('instance_agent.get_instance_agent_command_execution.command_name', 'get'), help=u"""Gets information about the status of specified instance agent commandId for the given instanceId. \n[Command Reference](getInstanceAgentCommandExecution)""")
@cli_util.option('--instance-agent-command-id', required=True, help=u"""The OCID of the command.""")
@cli_util.option('--instance-id', required=True, help=u"""The OCID of the instance.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'compute_instance_agent', 'class': 'InstanceAgentCommandExecution'})
@cli_util.wrap_exceptions
def get_instance_agent_command_execution(ctx, from_json, instance_agent_command_id, instance_id):

    if isinstance(instance_agent_command_id, six.string_types) and len(instance_agent_command_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-agent-command-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('compute_instance_agent', 'compute_instance_agent', ctx)
    result = client.get_instance_agent_command_execution(
        instance_agent_command_id=instance_agent_command_id,
        instance_id=instance_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@instance_agent_command_execution_group.command(name=cli_util.override('instance_agent.list_instance_agent_command_executions.command_name', 'list'), help=u"""List all executions of a command, i.e return command execution results from all targeted instances batch by batch. \n[Command Reference](listInstanceAgentCommandExecutions)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--instance-id', required=True, help=u"""The OCID of the instance.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "TIMED_OUT", "CANCELED"]), help=u"""A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'compute_instance_agent', 'class': 'list[InstanceAgentCommandExecutionSummary]'})
@cli_util.wrap_exceptions
def list_instance_agent_command_executions(ctx, from_json, all_pages, page_size, compartment_id, instance_id, page, limit, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('compute_instance_agent', 'compute_instance_agent', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_instance_agent_command_executions,
            compartment_id=compartment_id,
            instance_id=instance_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_instance_agent_command_executions,
            limit,
            page_size,
            compartment_id=compartment_id,
            instance_id=instance_id,
            **kwargs
        )
    else:
        result = client.list_instance_agent_command_executions(
            compartment_id=compartment_id,
            instance_id=instance_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@instance_agent_command_group.command(name=cli_util.override('instance_agent.list_instance_agent_commands.command_name', 'list'), help=u"""List Instance agent commands issued with the specified filter. Additonally you can filter commands sent to a particular InstanceId \n[Command Reference](listInstanceAgentCommands)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'compute_instance_agent', 'class': 'list[InstanceAgentCommandSummary]'})
@cli_util.wrap_exceptions
def list_instance_agent_commands(ctx, from_json, all_pages, page_size, compartment_id, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

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
    client = cli_util.build_client('compute_instance_agent', 'compute_instance_agent', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_instance_agent_commands,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_instance_agent_commands,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_instance_agent_commands(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)
