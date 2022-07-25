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


@cli.command(cli_util.override('management_agent.management_agent_root_group.command_name', 'management-agent'), cls=CommandGroupWithAlias, help=cli_util.override('management_agent.management_agent_root_group.help', """Use the Management Agent API to manage your infrastructure's management agents, including their plugins and install keys.
For more information, see [Management Agent]."""), short_help=cli_util.override('management_agent.management_agent_root_group.short_help', """Management Agent API"""))
@cli_util.help_option_group
def management_agent_root_group():
    pass


@click.command(cli_util.override('management_agent.management_agent_install_key_group.command_name', 'management-agent-install-key'), cls=CommandGroupWithAlias, help="""The details of the Agent install Key""")
@cli_util.help_option_group
def management_agent_install_key_group():
    pass


@click.command(cli_util.override('management_agent.management_agent_plugin_group.command_name', 'management-agent-plugin'), cls=CommandGroupWithAlias, help="""Summary of the ManagementAgentPlugin.""")
@cli_util.help_option_group
def management_agent_plugin_group():
    pass


@click.command(cli_util.override('management_agent.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('management_agent.management_agent_group.command_name', 'management-agent'), cls=CommandGroupWithAlias, help="""The details of the Management Agent inventory including the associated plugins.""")
@cli_util.help_option_group
def management_agent_group():
    pass


@click.command(cli_util.override('management_agent.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""A log message from the execution of a work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('management_agent.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""A description of workrequest status""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('management_agent.management_agent_image_group.command_name', 'management-agent-image'), cls=CommandGroupWithAlias, help="""Supported Agent downloads""")
@cli_util.help_option_group
def management_agent_image_group():
    pass


management_agent_root_group.add_command(management_agent_install_key_group)
management_agent_root_group.add_command(management_agent_plugin_group)
management_agent_root_group.add_command(work_request_error_group)
management_agent_root_group.add_command(management_agent_group)
management_agent_root_group.add_command(work_request_log_entry_group)
management_agent_root_group.add_command(work_request_group)
management_agent_root_group.add_command(management_agent_image_group)


@management_agent_install_key_group.command(name=cli_util.override('management_agent.create_management_agent_install_key.command_name', 'create'), help=u"""User creates a new install key as part of this API. \n[Command Reference](createManagementAgentInstallKey)""")
@cli_util.option('--display-name', required=True, help=u"""Management Agent install Key Name""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier""")
@cli_util.option('--allowed-key-install-count', type=click.INT, help=u"""Total number of install for this keys""")
@cli_util.option('--time-expires', type=custom_types.CLI_DATETIME, help=u"""date after which key would expire after creation""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--is-unlimited', type=click.BOOL, help=u"""If set to true, the install key has no expiration date or usage limit. Defaults to false""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "TERMINATED", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_agent', 'class': 'ManagementAgentInstallKey'})
@cli_util.wrap_exceptions
def create_management_agent_install_key(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, allowed_key_install_count, time_expires, is_unlimited):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id

    if allowed_key_install_count is not None:
        _details['allowedKeyInstallCount'] = allowed_key_install_count

    if time_expires is not None:
        _details['timeExpires'] = time_expires

    if is_unlimited is not None:
        _details['isUnlimited'] = is_unlimited

    client = cli_util.build_client('management_agent', 'management_agent', ctx)
    result = client.create_management_agent_install_key(
        create_management_agent_install_key_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_management_agent_install_key') and callable(getattr(client, 'get_management_agent_install_key')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_management_agent_install_key(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@management_agent_group.command(name=cli_util.override('management_agent.delete_management_agent.command_name', 'delete'), help=u"""Deletes a Management Agent resource by identifier \n[Command Reference](deleteManagementAgent)""")
@cli_util.option('--management-agent-id', required=True, help=u"""Unique Management Agent identifier""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "TERMINATED", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_management_agent(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, management_agent_id, if_match):

    if isinstance(management_agent_id, six.string_types) and len(management_agent_id.strip()) == 0:
        raise click.UsageError('Parameter --management-agent-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_agent', 'management_agent', ctx)
    result = client.delete_management_agent(
        management_agent_id=management_agent_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_management_agent') and callable(getattr(client, 'get_management_agent')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_management_agent(management_agent_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@management_agent_install_key_group.command(name=cli_util.override('management_agent.delete_management_agent_install_key.command_name', 'delete'), help=u"""Deletes a Management Agent install Key resource by identifier \n[Command Reference](deleteManagementAgentInstallKey)""")
@cli_util.option('--management-agent-install-key-id', required=True, help=u"""Unique Management Agent Install Key identifier""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "TERMINATED", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_management_agent_install_key(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, management_agent_install_key_id, if_match):

    if isinstance(management_agent_install_key_id, six.string_types) and len(management_agent_install_key_id.strip()) == 0:
        raise click.UsageError('Parameter --management-agent-install-key-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_agent', 'management_agent', ctx)
    result = client.delete_management_agent_install_key(
        management_agent_install_key_id=management_agent_install_key_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_management_agent_install_key') and callable(getattr(client, 'get_management_agent_install_key')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_management_agent_install_key(management_agent_install_key_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('management_agent.delete_work_request.command_name', 'delete'), help=u"""Cancel the work request with the given ID. \n[Command Reference](deleteWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_work_request(ctx, from_json, work_request_id, if_match):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_agent', 'management_agent', ctx)
    result = client.delete_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@management_agent_group.command(name=cli_util.override('management_agent.deploy_plugins.command_name', 'deploy-plugins'), help=u"""Deploys Plugins to a given list of agentIds. \n[Command Reference](deployPlugins)""")
@cli_util.option('--plugin-ids', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Plugin Id""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--agent-compartment-id', required=True, help=u"""Management Agent Compartment Identifier""")
@cli_util.option('--agent-ids', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Agent identifiers""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATED", "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'plugin-ids': {'module': 'management_agent', 'class': 'list[string]'}, 'agent-ids': {'module': 'management_agent', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'plugin-ids': {'module': 'management_agent', 'class': 'list[string]'}, 'agent-ids': {'module': 'management_agent', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def deploy_plugins(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, plugin_ids, agent_compartment_id, agent_ids):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['pluginIds'] = cli_util.parse_json_parameter("plugin_ids", plugin_ids)
    _details['agentCompartmentId'] = agent_compartment_id
    _details['agentIds'] = cli_util.parse_json_parameter("agent_ids", agent_ids)

    client = cli_util.build_client('management_agent', 'management_agent', ctx)
    result = client.deploy_plugins(
        deploy_plugins_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@management_agent_group.command(name=cli_util.override('management_agent.get_auto_upgradable_config.command_name', 'get-auto-upgradable-config'), help=u"""Get the AutoUpgradable configuration for all agents in a tenancy. The supplied compartmentId must be a tenancy root. \n[Command Reference](getAutoUpgradableConfig)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to which a request will be scoped.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_agent', 'class': 'AutoUpgradableConfig'})
@cli_util.wrap_exceptions
def get_auto_upgradable_config(ctx, from_json, compartment_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_agent', 'management_agent', ctx)
    result = client.get_auto_upgradable_config(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@management_agent_group.command(name=cli_util.override('management_agent.get_management_agent.command_name', 'get'), help=u"""Gets complete details of the inventory of a given agent id \n[Command Reference](getManagementAgent)""")
@cli_util.option('--management-agent-id', required=True, help=u"""Unique Management Agent identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_agent', 'class': 'ManagementAgent'})
@cli_util.wrap_exceptions
def get_management_agent(ctx, from_json, management_agent_id):

    if isinstance(management_agent_id, six.string_types) and len(management_agent_id.strip()) == 0:
        raise click.UsageError('Parameter --management-agent-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_agent', 'management_agent', ctx)
    result = client.get_management_agent(
        management_agent_id=management_agent_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@management_agent_install_key_group.command(name=cli_util.override('management_agent.get_management_agent_install_key.command_name', 'get'), help=u"""Gets complete details of the Agent install Key for a given key id \n[Command Reference](getManagementAgentInstallKey)""")
@cli_util.option('--management-agent-install-key-id', required=True, help=u"""Unique Management Agent Install Key identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_agent', 'class': 'ManagementAgentInstallKey'})
@cli_util.wrap_exceptions
def get_management_agent_install_key(ctx, from_json, management_agent_install_key_id):

    if isinstance(management_agent_install_key_id, six.string_types) and len(management_agent_install_key_id.strip()) == 0:
        raise click.UsageError('Parameter --management-agent-install-key-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_agent', 'management_agent', ctx)
    result = client.get_management_agent_install_key(
        management_agent_install_key_id=management_agent_install_key_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@management_agent_install_key_group.command(name=cli_util.override('management_agent.get_management_agent_install_key_content.command_name', 'get-management-agent-install-key-content'), help=u"""Returns a file with Management Agent install Key in it \n[Command Reference](getManagementAgentInstallKeyContent)""")
@cli_util.option('--management-agent-install-key-id', required=True, help=u"""Unique Management Agent Install Key identifier""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@cli_util.option('--plugin-name', multiple=True, help=u"""Filter to return input plugin names uncommented in the output.""")
@json_skeleton_utils.get_cli_json_input_option({'plugin-name': {'module': 'management_agent', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'plugin-name': {'module': 'management_agent', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def get_management_agent_install_key_content(ctx, from_json, file, management_agent_install_key_id, plugin_name):

    if isinstance(management_agent_install_key_id, six.string_types) and len(management_agent_install_key_id.strip()) == 0:
        raise click.UsageError('Parameter --management-agent-install-key-id cannot be whitespace or empty string')

    kwargs = {}
    if plugin_name is not None and len(plugin_name) > 0:
        kwargs['plugin_name'] = plugin_name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_agent', 'management_agent', ctx)
    result = client.get_management_agent_install_key_content(
        management_agent_install_key_id=management_agent_install_key_id,
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


@work_request_group.command(name=cli_util.override('management_agent.get_work_request.command_name', 'get'), help=u"""Gets the status of the work request with the given ID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_agent', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_agent', 'management_agent', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@management_agent_group.command(name=cli_util.override('management_agent.list_availability_histories.command_name', 'list-availability-histories'), help=u"""Lists the availability history records of Management Agent \n[Command Reference](listAvailabilityHistories)""")
@cli_util.option('--management-agent-id', required=True, help=u"""Unique Management Agent identifier""")
@cli_util.option('--time-availability-status-ended-greater-than', type=custom_types.CLI_DATETIME, help=u"""Filter to limit the availability history results to that of time after the input time including the boundary record. Defaulted to current date minus one year. The date and time to be given as described in [RFC 3339], section 14.29.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-availability-status-started-less-than', type=custom_types.CLI_DATETIME, help=u"""Filter to limit the availability history results to that of time before the input time including the boundary record Defaulted to current date. The date and time to be given as described in [RFC 3339], section 14.29.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAvailabilityStatusStarted"]), help=u"""The field to sort by. Default order for timeAvailabilityStatusStarted is descending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_agent', 'class': 'list[AvailabilityHistorySummary]'})
@cli_util.wrap_exceptions
def list_availability_histories(ctx, from_json, all_pages, page_size, management_agent_id, time_availability_status_ended_greater_than, time_availability_status_started_less_than, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(management_agent_id, six.string_types) and len(management_agent_id.strip()) == 0:
        raise click.UsageError('Parameter --management-agent-id cannot be whitespace or empty string')

    kwargs = {}
    if time_availability_status_ended_greater_than is not None:
        kwargs['time_availability_status_ended_greater_than'] = time_availability_status_ended_greater_than
    if time_availability_status_started_less_than is not None:
        kwargs['time_availability_status_started_less_than'] = time_availability_status_started_less_than
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_agent', 'management_agent', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_availability_histories,
            management_agent_id=management_agent_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_availability_histories,
            limit,
            page_size,
            management_agent_id=management_agent_id,
            **kwargs
        )
    else:
        result = client.list_availability_histories(
            management_agent_id=management_agent_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@management_agent_image_group.command(name=cli_util.override('management_agent.list_management_agent_images.command_name', 'list'), help=u"""Get supported agent image information \n[Command Reference](listManagementAgentImages)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to which a request will be scoped.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["platformType", "version"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for platformType is descending. Default order for version is descending. If no value is specified platformType is default.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire platform name given.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "TERMINATED", "DELETING", "DELETED", "FAILED"]), help=u"""Filter to return only Management Agents in the particular lifecycle state.""")
@cli_util.option('--install-type', type=custom_types.CliCaseInsensitiveChoice(["AGENT", "GATEWAY"]), help=u"""A filter to return either agents or gateway types depending upon install type selected by user. By default both install type will be returned.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_agent', 'class': 'list[ManagementAgentImageSummary]'})
@cli_util.wrap_exceptions
def list_management_agent_images(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_order, sort_by, name, lifecycle_state, install_type):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if name is not None:
        kwargs['name'] = name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if install_type is not None:
        kwargs['install_type'] = install_type
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_agent', 'management_agent', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_management_agent_images,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_management_agent_images,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_management_agent_images(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@management_agent_install_key_group.command(name=cli_util.override('management_agent.list_management_agent_install_keys.command_name', 'list'), help=u"""Returns a list of Management Agent installed Keys. \n[Command Reference](listManagementAgentInstallKeys)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to which a request will be scoped.""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""if set to true then it fetches resources for all compartments where user has access to else only on the compartment specified.""")
@cli_util.option('--access-level', help=u"""Value of this is always \"ACCESSIBLE\" and any other value is not supported.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "TERMINATED", "DELETING", "DELETED", "FAILED"]), help=u"""Filter to return only Management Agents in the particular lifecycle state.""")
@cli_util.option('--display-name', help=u"""The display name for which the Key needs to be listed.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_agent', 'class': 'list[ManagementAgentInstallKeySummary]'})
@cli_util.wrap_exceptions
def list_management_agent_install_keys(ctx, from_json, all_pages, compartment_id, compartment_id_in_subtree, access_level, lifecycle_state, display_name, page, sort_order, sort_by):

    kwargs = {}
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    if access_level is not None:
        kwargs['access_level'] = access_level
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_agent', 'management_agent', ctx)
    if all_pages:
        result = cli_util.list_call_get_all_results(
            client.list_management_agent_install_keys,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_management_agent_install_keys(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@management_agent_plugin_group.command(name=cli_util.override('management_agent.list_management_agent_plugins.command_name', 'list'), help=u"""Returns a list of managementAgentPlugins. \n[Command Reference](listManagementAgentPlugins)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to which a request will be scoped.""")
@cli_util.option('--display-name', help=u"""Filter to return only Management Agent Plugins having the particular display name.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["displayName"]), help=u"""The field to sort by. Default order for displayName is ascending. If no value is specified displayName is default.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "TERMINATED", "DELETING", "DELETED", "FAILED"]), help=u"""Filter to return only Management Agents in the particular lifecycle state.""")
@cli_util.option('--platform-type', type=custom_types.CliCaseInsensitiveChoice(["LINUX", "WINDOWS", "SOLARIS"]), multiple=True, help=u"""Filter to return only results having the particular platform type.""")
@cli_util.option('--agent-id', help=u"""The ManagementAgentID of the agent from which the Management Agents to be filtered.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_agent', 'class': 'list[ManagementAgentPluginSummary]'})
@cli_util.wrap_exceptions
def list_management_agent_plugins(ctx, from_json, all_pages, page_size, compartment_id, display_name, limit, page, sort_order, sort_by, lifecycle_state, platform_type, agent_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if platform_type is not None and len(platform_type) > 0:
        kwargs['platform_type'] = platform_type
    if agent_id is not None:
        kwargs['agent_id'] = agent_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_agent', 'management_agent', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_management_agent_plugins,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_management_agent_plugins,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_management_agent_plugins(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@management_agent_group.command(name=cli_util.override('management_agent.list_management_agents.command_name', 'list'), help=u"""Returns a list of Management Agents. If no explicit page size limit is specified, it will default to 1000 when compartmentIdInSubtree is true and 5000 otherwise. The response is limited to maximum 1000 records when compartmentIdInSubtree is true. \n[Command Reference](listManagementAgents)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to which a request will be scoped.""")
@cli_util.option('--plugin-name', multiple=True, help=u"""Filter to return only Management Agents having the particular Plugin installed. A special pluginName of 'None' can be provided and this will return only Management Agents having no plugin installed.""")
@cli_util.option('--version-parameterconflict', multiple=True, help=u"""Filter to return only Management Agents having the particular agent version.""")
@cli_util.option('--display-name', help=u"""Filter to return only Management Agents having the particular display name.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "TERMINATED", "DELETING", "DELETED", "FAILED"]), help=u"""Filter to return only Management Agents in the particular lifecycle state.""")
@cli_util.option('--availability-status', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "SILENT", "NOT_AVAILABLE"]), help=u"""Filter to return only Management Agents in the particular availability status.""")
@cli_util.option('--host-id', help=u"""Filter to return only Management Agents having the particular agent host id.""")
@cli_util.option('--platform-type', type=custom_types.CliCaseInsensitiveChoice(["LINUX", "WINDOWS", "SOLARIS"]), multiple=True, help=u"""Filter to return only results having the particular platform type.""")
@cli_util.option('--is-customer-deployed', type=click.BOOL, help=u"""true, if the agent image is manually downloaded and installed. false, if the agent is deployed as a plugin in Oracle Cloud Agent.""")
@cli_util.option('--install-type', type=custom_types.CliCaseInsensitiveChoice(["AGENT", "GATEWAY"]), help=u"""A filter to return either agents or gateway types depending upon install type selected by user. By default both install type will be returned.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName", "host", "availabilityStatus", "platformType", "pluginDisplayNames", "version"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""if set to true then it fetches resources for all compartments where user has access to else only on the compartment specified.""")
@cli_util.option('--access-level', help=u"""When the value is \"ACCESSIBLE\", insufficient permissions for a compartment will filter out resources in that compartment without rejecting the request.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'plugin-name': {'module': 'management_agent', 'class': 'list[string]'}, 'version-parameterconflict': {'module': 'management_agent', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'plugin-name': {'module': 'management_agent', 'class': 'list[string]'}, 'version-parameterconflict': {'module': 'management_agent', 'class': 'list[string]'}}, output_type={'module': 'management_agent', 'class': 'list[ManagementAgentSummary]'})
@cli_util.wrap_exceptions
def list_management_agents(ctx, from_json, all_pages, page_size, compartment_id, plugin_name, version_parameterconflict, display_name, lifecycle_state, availability_status, host_id, platform_type, is_customer_deployed, install_type, limit, page, sort_order, sort_by, compartment_id_in_subtree, access_level):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if plugin_name is not None and len(plugin_name) > 0:
        kwargs['plugin_name'] = plugin_name
    if version_parameterconflict is not None and len(version_parameterconflict) > 0:
        kwargs['version'] = version_parameterconflict
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if availability_status is not None:
        kwargs['availability_status'] = availability_status
    if host_id is not None:
        kwargs['host_id'] = host_id
    if platform_type is not None and len(platform_type) > 0:
        kwargs['platform_type'] = platform_type
    if is_customer_deployed is not None:
        kwargs['is_customer_deployed'] = is_customer_deployed
    if install_type is not None:
        kwargs['install_type'] = install_type
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    if access_level is not None:
        kwargs['access_level'] = access_level
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_agent', 'management_agent', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_management_agents,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_management_agents,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_management_agents(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('management_agent.list_work_request_errors.command_name', 'list'), help=u"""Return a (paginated) list of errors for a given work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timestamp"]), help=u"""The field to sort by. Only one sort order may""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_agent', 'class': 'list[WorkRequestError]'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_agent', 'management_agent', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_errors,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_errors,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_errors(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_log_entry_group.command(name=cli_util.override('management_agent.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Return a (paginated) list of logs for a given work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timestamp"]), help=u"""The field to sort by. Only one sort order may""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_agent', 'class': 'list[WorkRequestLogEntry]'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_agent', 'management_agent', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_logs,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_logs,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_logs(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('management_agent.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to which a request will be scoped.""")
@cli_util.option('--agent-id', help=u"""The ManagementAgentID of the agent from which the Management Agents to be filtered.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["CREATED", "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help=u"""The OperationStatus of the workRequest""")
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["DEPLOY_PLUGIN", "UPGRADE_PLUGIN", "CREATE_UPGRADE_PLUGINS", "AGENTIMAGE_UPGRADE"]), help=u"""The OperationType of the workRequest""")
@cli_util.option('--time-created-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""Filter for items with timeCreated greater or equal to provided value. given `timeCreatedGreaterThanOrEqualTo` to the current time, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending. If no value is specified timeAccepted is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_agent', 'class': 'list[WorkRequestSummary]'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, agent_id, page, limit, status, type, time_created_greater_than_or_equal_to, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if agent_id is not None:
        kwargs['agent_id'] = agent_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if status is not None:
        kwargs['status'] = status
    if type is not None:
        kwargs['type'] = type
    if time_created_greater_than_or_equal_to is not None:
        kwargs['time_created_greater_than_or_equal_to'] = time_created_greater_than_or_equal_to
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_agent', 'management_agent', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@management_agent_group.command(name=cli_util.override('management_agent.set_auto_upgradable_config.command_name', 'set-auto-upgradable-config'), help=u"""Sets the AutoUpgradable configuration for all agents in a tenancy. The supplied compartmentId must be a tenancy root. \n[Command Reference](setAutoUpgradableConfig)""")
@cli_util.option('--compartment-id', required=True, help=u"""Tenancy identifier i.e, Root compartment identifier""")
@cli_util.option('--is-agent-auto-upgradable', required=True, type=click.BOOL, help=u"""true if the agents can be upgraded automatically; false if they must be upgraded manually.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_agent', 'class': 'AutoUpgradableConfig'})
@cli_util.wrap_exceptions
def set_auto_upgradable_config(ctx, from_json, compartment_id, is_agent_auto_upgradable):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['isAgentAutoUpgradable'] = is_agent_auto_upgradable

    client = cli_util.build_client('management_agent', 'management_agent', ctx)
    result = client.set_auto_upgradable_config(
        set_auto_upgradable_config_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@management_agent_group.command(name=cli_util.override('management_agent.summarize_management_agent_counts.command_name', 'summarize-management-agent-counts'), help=u"""Gets count of the inventory of agents for a given compartment id, group by, and isPluginDeployed parameters. Supported groupBy parameters: availabilityStatus, platformType, version \n[Command Reference](summarizeManagementAgentCounts)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to which a request will be scoped.""")
@cli_util.option('--group-by', required=True, type=custom_types.CliCaseInsensitiveChoice(["availabilityStatus", "platformType", "version"]), multiple=True, help=u"""The field by which to group Management Agents. Currently, only one groupBy dimension is supported at a time.""")
@cli_util.option('--has-plugins', type=click.BOOL, help=u"""When set to true then agents that have at least one plugin deployed will be returned. When set to false only agents that have no plugins deployed will be returned.""")
@cli_util.option('--install-type', type=custom_types.CliCaseInsensitiveChoice(["AGENT", "GATEWAY"]), help=u"""A filter to return either agents or gateway types depending upon install type selected by user. By default both install type will be returned.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_agent', 'class': 'ManagementAgentAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_management_agent_counts(ctx, from_json, compartment_id, group_by, has_plugins, install_type, page):

    kwargs = {}
    if has_plugins is not None:
        kwargs['has_plugins'] = has_plugins
    if install_type is not None:
        kwargs['install_type'] = install_type
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_agent', 'management_agent', ctx)
    result = client.summarize_management_agent_counts(
        compartment_id=compartment_id,
        group_by=group_by,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@management_agent_group.command(name=cli_util.override('management_agent.summarize_management_agent_plugin_counts.command_name', 'summarize-management-agent-plugin-counts'), help=u"""Gets count of the inventory of management agent plugins for a given compartment id and group by parameter. Supported groupBy parameter: pluginName \n[Command Reference](summarizeManagementAgentPluginCounts)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to which a request will be scoped.""")
@cli_util.option('--group-by', required=True, type=custom_types.CliCaseInsensitiveChoice(["pluginName"]), help=u"""The field by which to group Management Agent Plugins""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_agent', 'class': 'ManagementAgentPluginAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_management_agent_plugin_counts(ctx, from_json, compartment_id, group_by, page):

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_agent', 'management_agent', ctx)
    result = client.summarize_management_agent_plugin_counts(
        compartment_id=compartment_id,
        group_by=group_by,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@management_agent_group.command(name=cli_util.override('management_agent.update_management_agent.command_name', 'update'), help=u"""API to update the console managed properties of the Management Agent. \n[Command Reference](updateManagementAgent)""")
@cli_util.option('--management-agent-id', required=True, help=u"""Unique Management Agent identifier""")
@cli_util.option('--display-name', help=u"""New displayName of Agent.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "TERMINATED", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'management_agent', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'management_agent', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'management_agent', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'management_agent', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'management_agent', 'class': 'ManagementAgent'})
@cli_util.wrap_exceptions
def update_management_agent(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, management_agent_id, display_name, freeform_tags, defined_tags, if_match):

    if isinstance(management_agent_id, six.string_types) and len(management_agent_id.strip()) == 0:
        raise click.UsageError('Parameter --management-agent-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('management_agent', 'management_agent', ctx)
    result = client.update_management_agent(
        management_agent_id=management_agent_id,
        update_management_agent_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_management_agent') and callable(getattr(client, 'get_management_agent')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_management_agent(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@management_agent_install_key_group.command(name=cli_util.override('management_agent.update_management_agent_install_key.command_name', 'update'), help=u"""API to update the modifiable properties of the Management Agent install key. \n[Command Reference](updateManagementAgentInstallKey)""")
@cli_util.option('--management-agent-install-key-id', required=True, help=u"""Unique Management Agent Install Key identifier""")
@cli_util.option('--is-key-active', type=click.BOOL, help=u"""if set to true the install key state would be set to Active and if false to Inactive""")
@cli_util.option('--display-name', help=u"""New displayName of Agent install key.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "TERMINATED", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_agent', 'class': 'ManagementAgentInstallKey'})
@cli_util.wrap_exceptions
def update_management_agent_install_key(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, management_agent_install_key_id, is_key_active, display_name, if_match):

    if isinstance(management_agent_install_key_id, six.string_types) and len(management_agent_install_key_id.strip()) == 0:
        raise click.UsageError('Parameter --management-agent-install-key-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if is_key_active is not None:
        _details['isKeyActive'] = is_key_active

    if display_name is not None:
        _details['displayName'] = display_name

    client = cli_util.build_client('management_agent', 'management_agent', ctx)
    result = client.update_management_agent_install_key(
        management_agent_install_key_id=management_agent_install_key_id,
        update_management_agent_install_key_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_management_agent_install_key') and callable(getattr(client, 'get_management_agent_install_key')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_management_agent_install_key(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
