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
from services.cloud_bridge.src.oci_cli_cloud_bridge.generated import cloud_bridge_service_cli


@click.command(cli_util.override('ocb_agent_svc.ocb_agent_svc_root_group.command_name', 'ocb-agent-svc'), cls=CommandGroupWithAlias, help=cli_util.override('ocb_agent_svc.ocb_agent_svc_root_group.help', """API for Oracle Cloud Bridge service."""), short_help=cli_util.override('ocb_agent_svc.ocb_agent_svc_root_group.short_help', """Oracle Cloud Bridge API"""))
@cli_util.help_option_group
def ocb_agent_svc_root_group():
    pass


@click.command(cli_util.override('ocb_agent_svc.appliance_image_collection_group.command_name', 'appliance-image-collection'), cls=CommandGroupWithAlias, help="""Results of an ApplianceImage search.""")
@cli_util.help_option_group
def appliance_image_collection_group():
    pass


@click.command(cli_util.override('ocb_agent_svc.agent_dependency_collection_group.command_name', 'agent-dependency-collection'), cls=CommandGroupWithAlias, help="""Results of an AgentDependency list. Contains both AgentDependency items and other information, such as metadata.""")
@cli_util.help_option_group
def agent_dependency_collection_group():
    pass


@click.command(cli_util.override('ocb_agent_svc.agent_group.command_name', 'agent'), cls=CommandGroupWithAlias, help="""Description of Agent.""")
@cli_util.help_option_group
def agent_group():
    pass


@click.command(cli_util.override('ocb_agent_svc.environment_group.command_name', 'environment'), cls=CommandGroupWithAlias, help="""Description of the source environment.""")
@cli_util.help_option_group
def environment_group():
    pass


@click.command(cli_util.override('ocb_agent_svc.agent_dependency_group.command_name', 'agent-dependency'), cls=CommandGroupWithAlias, help="""Description of the AgentDependency, which is a sub-resource of the external environment.""")
@cli_util.help_option_group
def agent_dependency_group():
    pass


@click.command(cli_util.override('ocb_agent_svc.plugin_group.command_name', 'plugin'), cls=CommandGroupWithAlias, help="""Description of plugin""")
@cli_util.help_option_group
def plugin_group():
    pass


@click.command(cli_util.override('ocb_agent_svc.environment_collection_group.command_name', 'environment-collection'), cls=CommandGroupWithAlias, help="""Results of an environment search. Contains both EnvironmentSummary items and other information, such as metadata.""")
@cli_util.help_option_group
def environment_collection_group():
    pass


@click.command(cli_util.override('ocb_agent_svc.agent_collection_group.command_name', 'agent-collection'), cls=CommandGroupWithAlias, help="""Displays results of an Agent search. Contains both AgentSummary items and other information, such as metadata.""")
@cli_util.help_option_group
def agent_collection_group():
    pass


cloud_bridge_service_cli.cloud_bridge_service_group.add_command(ocb_agent_svc_root_group)
ocb_agent_svc_root_group.add_command(appliance_image_collection_group)
ocb_agent_svc_root_group.add_command(agent_dependency_collection_group)
ocb_agent_svc_root_group.add_command(agent_group)
ocb_agent_svc_root_group.add_command(environment_group)
ocb_agent_svc_root_group.add_command(agent_dependency_group)
ocb_agent_svc_root_group.add_command(plugin_group)
ocb_agent_svc_root_group.add_command(environment_collection_group)
ocb_agent_svc_root_group.add_command(agent_collection_group)


@environment_group.command(name=cli_util.override('ocb_agent_svc.add_agent_dependency.command_name', 'add'), help=u"""Add a dependency to the environment. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](addAgentDependency)""")
@cli_util.option('--environment-id', required=True, help=u"""Unique environment identifier.""")
@cli_util.option('--agent-dependency-id', required=True, help=u"""The OCID of the agentDependency, which is added to the source environment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_bridge', 'class': 'Environment'})
@cli_util.wrap_exceptions
def add_agent_dependency(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, environment_id, agent_dependency_id, if_match):

    if isinstance(environment_id, six.string_types) and len(environment_id.strip()) == 0:
        raise click.UsageError('Parameter --environment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['agentDependencyId'] = agent_dependency_id

    client = cli_util.build_client('cloud_bridge', 'ocb_agent_svc', ctx)
    result = client.add_agent_dependency(
        environment_id=environment_id,
        add_agent_dependency_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_environment') and callable(getattr(client, 'get_environment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_environment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@agent_group.command(name=cli_util.override('ocb_agent_svc.change_agent_compartment.command_name', 'change-compartment'), help=u"""Moves an Agent resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeAgentCompartment)""")
@cli_util.option('--agent-id', required=True, help=u"""Unique Agent identifier path parameter.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_agent_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, agent_id, compartment_id, if_match):

    if isinstance(agent_id, six.string_types) and len(agent_id.strip()) == 0:
        raise click.UsageError('Parameter --agent-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('cloud_bridge', 'ocb_agent_svc', ctx)
    result = client.change_agent_compartment(
        agent_id=agent_id,
        change_agent_compartment_details=_details,
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


@agent_dependency_group.command(name=cli_util.override('ocb_agent_svc.change_agent_dependency_compartment.command_name', 'change-compartment'), help=u"""Moves a AgentDependency resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeAgentDependencyCompartment)""")
@cli_util.option('--agent-dependency-id', required=True, help=u"""A unique AgentDependency identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_agent_dependency_compartment(ctx, from_json, agent_dependency_id, compartment_id, if_match):

    if isinstance(agent_dependency_id, six.string_types) and len(agent_dependency_id.strip()) == 0:
        raise click.UsageError('Parameter --agent-dependency-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('cloud_bridge', 'ocb_agent_svc', ctx)
    result = client.change_agent_dependency_compartment(
        agent_dependency_id=agent_dependency_id,
        change_agent_dependency_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@environment_group.command(name=cli_util.override('ocb_agent_svc.change_environment_compartment.command_name', 'change-compartment'), help=u"""Moves a source environment resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeEnvironmentCompartment)""")
@cli_util.option('--environment-id', required=True, help=u"""Unique environment identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_environment_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, environment_id, compartment_id, if_match):

    if isinstance(environment_id, six.string_types) and len(environment_id.strip()) == 0:
        raise click.UsageError('Parameter --environment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('cloud_bridge', 'ocb_agent_svc', ctx)
    result = client.change_environment_compartment(
        environment_id=environment_id,
        change_environment_compartment_details=_details,
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


@agent_group.command(name=cli_util.override('ocb_agent_svc.create_agent.command_name', 'create'), help=u"""Creates an Agent. \n[Command Reference](createAgent)""")
@cli_util.option('--display-name', required=True, help=u"""Agent identifier.""")
@cli_util.option('--agent-type', required=True, help=u"""Agent identifier.""")
@cli_util.option('--agent-version', required=True, help=u"""Agent identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment identifier.""")
@cli_util.option('--environment-id', required=True, help=u"""Environment identifier.""")
@cli_util.option('--os-version', required=True, help=u"""OS version.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'cloud_bridge', 'class': 'Agent'})
@cli_util.wrap_exceptions
def create_agent(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, agent_type, agent_version, compartment_id, environment_id, os_version, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['agentType'] = agent_type
    _details['agentVersion'] = agent_version
    _details['compartmentId'] = compartment_id
    _details['environmentId'] = environment_id
    _details['osVersion'] = os_version

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('cloud_bridge', 'ocb_agent_svc', ctx)
    result = client.create_agent(
        create_agent_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_agent') and callable(getattr(client, 'get_agent')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_agent(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@agent_dependency_group.command(name=cli_util.override('ocb_agent_svc.create_agent_dependency.command_name', 'create'), help=u"""Creates an AgentDependency. \n[Command Reference](createAgentDependency)""")
@cli_util.option('--display-name', required=True, help=u"""Display name of the Agent dependency.""")
@cli_util.option('--dependency-name', required=True, help=u"""Name of the dependency type. This should match the whitelisted enum of dependency names.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment identifier.""")
@cli_util.option('--namespace', required=True, help=u"""Object storage namespace associated with the customer's tenancy.""")
@cli_util.option('--bucket', required=True, help=u"""Object storage bucket where the dependency is uploaded.""")
@cli_util.option('--object-name', required=True, help=u"""Name of the dependency object uploaded by the customer.""")
@cli_util.option('--dependency-version', help=u"""Version of the Agent dependency.""")
@cli_util.option('--description', help=u"""Description about the Agent dependency.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--system-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{orcl-cloud: {free-tier-retain: true}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'cloud_bridge', 'class': 'AgentDependency'})
@cli_util.wrap_exceptions
def create_agent_dependency(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, dependency_name, compartment_id, namespace, bucket, object_name, dependency_version, description, freeform_tags, defined_tags, system_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['dependencyName'] = dependency_name
    _details['compartmentId'] = compartment_id
    _details['namespace'] = namespace
    _details['bucket'] = bucket
    _details['objectName'] = object_name

    if dependency_version is not None:
        _details['dependencyVersion'] = dependency_version

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if system_tags is not None:
        _details['systemTags'] = cli_util.parse_json_parameter("system_tags", system_tags)

    client = cli_util.build_client('cloud_bridge', 'ocb_agent_svc', ctx)
    result = client.create_agent_dependency(
        create_agent_dependency_details=_details,
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


@environment_group.command(name=cli_util.override('ocb_agent_svc.create_environment.command_name', 'create'), help=u"""Creates a source environment. \n[Command Reference](createEnvironment)""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment identifier.""")
@cli_util.option('--display-name', help=u"""Environment identifier.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'cloud_bridge', 'class': 'Environment'})
@cli_util.wrap_exceptions
def create_environment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('cloud_bridge', 'ocb_agent_svc', ctx)
    result = client.create_environment(
        create_environment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_environment') and callable(getattr(client, 'get_environment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_environment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@agent_group.command(name=cli_util.override('ocb_agent_svc.delete_agent.command_name', 'delete'), help=u"""Deletes an Agent resource identified by an identifier. \n[Command Reference](deleteAgent)""")
@cli_util.option('--agent-id', required=True, help=u"""Unique Agent identifier path parameter.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_agent(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, agent_id, if_match):

    if isinstance(agent_id, six.string_types) and len(agent_id.strip()) == 0:
        raise click.UsageError('Parameter --agent-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_bridge', 'ocb_agent_svc', ctx)
    result = client.delete_agent(
        agent_id=agent_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_agent') and callable(getattr(client, 'get_agent')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_agent(agent_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@agent_dependency_group.command(name=cli_util.override('ocb_agent_svc.delete_agent_dependency.command_name', 'delete'), help=u"""Deletes the AgentDependency resource based on an identifier. \n[Command Reference](deleteAgentDependency)""")
@cli_util.option('--agent-dependency-id', required=True, help=u"""A unique AgentDependency identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_agent_dependency(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, agent_dependency_id, if_match):

    if isinstance(agent_dependency_id, six.string_types) and len(agent_dependency_id.strip()) == 0:
        raise click.UsageError('Parameter --agent-dependency-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_bridge', 'ocb_agent_svc', ctx)
    result = client.delete_agent_dependency(
        agent_dependency_id=agent_dependency_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_agent_dependency') and callable(getattr(client, 'get_agent_dependency')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_agent_dependency(agent_dependency_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@environment_group.command(name=cli_util.override('ocb_agent_svc.delete_environment.command_name', 'delete'), help=u"""Deletes a the source environment resource identified by an identifier. \n[Command Reference](deleteEnvironment)""")
@cli_util.option('--environment-id', required=True, help=u"""Unique environment identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_environment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, environment_id, if_match):

    if isinstance(environment_id, six.string_types) and len(environment_id.strip()) == 0:
        raise click.UsageError('Parameter --environment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_bridge', 'ocb_agent_svc', ctx)
    result = client.delete_environment(
        environment_id=environment_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_environment') and callable(getattr(client, 'get_environment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_environment(environment_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@agent_group.command(name=cli_util.override('ocb_agent_svc.get_agent.command_name', 'get'), help=u"""Gets an Agent by identifier. \n[Command Reference](getAgent)""")
@cli_util.option('--agent-id', required=True, help=u"""Unique Agent identifier path parameter.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_bridge', 'class': 'Agent'})
@cli_util.wrap_exceptions
def get_agent(ctx, from_json, agent_id):

    if isinstance(agent_id, six.string_types) and len(agent_id.strip()) == 0:
        raise click.UsageError('Parameter --agent-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_bridge', 'ocb_agent_svc', ctx)
    result = client.get_agent(
        agent_id=agent_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@agent_dependency_group.command(name=cli_util.override('ocb_agent_svc.get_agent_dependency.command_name', 'get'), help=u"""Gets an AgentDependency by identifier. \n[Command Reference](getAgentDependency)""")
@cli_util.option('--agent-dependency-id', required=True, help=u"""A unique AgentDependency identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_bridge', 'class': 'AgentDependency'})
@cli_util.wrap_exceptions
def get_agent_dependency(ctx, from_json, agent_dependency_id):

    if isinstance(agent_dependency_id, six.string_types) and len(agent_dependency_id.strip()) == 0:
        raise click.UsageError('Parameter --agent-dependency-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_bridge', 'ocb_agent_svc', ctx)
    result = client.get_agent_dependency(
        agent_dependency_id=agent_dependency_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@environment_group.command(name=cli_util.override('ocb_agent_svc.get_environment.command_name', 'get'), help=u"""Gets a source environment by identifier. \n[Command Reference](getEnvironment)""")
@cli_util.option('--environment-id', required=True, help=u"""Unique environment identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_bridge', 'class': 'Environment'})
@cli_util.wrap_exceptions
def get_environment(ctx, from_json, environment_id):

    if isinstance(environment_id, six.string_types) and len(environment_id.strip()) == 0:
        raise click.UsageError('Parameter --environment-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_bridge', 'ocb_agent_svc', ctx)
    result = client.get_environment(
        environment_id=environment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@plugin_group.command(name=cli_util.override('ocb_agent_svc.get_plugin.command_name', 'get'), help=u"""Gets a plugin by identifier. \n[Command Reference](getPlugin)""")
@cli_util.option('--agent-id', required=True, help=u"""Unique Agent identifier path parameter.""")
@cli_util.option('--plugin-name', required=True, help=u"""Unique plugin identifier path parameter.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_bridge', 'class': 'Plugin'})
@cli_util.wrap_exceptions
def get_plugin(ctx, from_json, agent_id, plugin_name):

    if isinstance(agent_id, six.string_types) and len(agent_id.strip()) == 0:
        raise click.UsageError('Parameter --agent-id cannot be whitespace or empty string')

    if isinstance(plugin_name, six.string_types) and len(plugin_name.strip()) == 0:
        raise click.UsageError('Parameter --plugin-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_bridge', 'ocb_agent_svc', ctx)
    result = client.get_plugin(
        agent_id=agent_id,
        plugin_name=plugin_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@agent_dependency_collection_group.command(name=cli_util.override('ocb_agent_svc.list_agent_dependencies.command_name', 'list-agent-dependencies'), help=u"""Returns a list of AgentDependencies such as AgentDependencyCollection. \n[Command Reference](listAgentDependencies)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--agent-id', help=u"""A filter to return only resources that match the given Agent ID.""")
@cli_util.option('--environment-id', help=u"""A filter to return only resources that match the given environment ID.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources their lifecycleState matches the given lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "timeUpdated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_bridge', 'class': 'AgentDependencyCollection'})
@cli_util.wrap_exceptions
def list_agent_dependencies(ctx, from_json, all_pages, page_size, compartment_id, agent_id, environment_id, lifecycle_state, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if agent_id is not None:
        kwargs['agent_id'] = agent_id
    if environment_id is not None:
        kwargs['environment_id'] = environment_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
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
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_bridge', 'ocb_agent_svc', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_agent_dependencies,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_agent_dependencies,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_agent_dependencies(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@agent_collection_group.command(name=cli_util.override('ocb_agent_svc.list_agents.command_name', 'list-agents'), help=u"""Returns a list of Agents. \n[Command Reference](listAgents)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--environment-id', help=u"""A filter to return only resources that match the given environment ID.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETED", "FAILED"]), help=u"""A filter to return only resources their lifecycleState matches the given lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--agent-id', help=u"""A filter to return only resources that match the given Agent ID.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "timeUpdated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_bridge', 'class': 'AgentCollection'})
@cli_util.wrap_exceptions
def list_agents(ctx, from_json, all_pages, page_size, compartment_id, environment_id, lifecycle_state, display_name, agent_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if environment_id is not None:
        kwargs['environment_id'] = environment_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if agent_id is not None:
        kwargs['agent_id'] = agent_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_bridge', 'ocb_agent_svc', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_agents,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_agents,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_agents(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@appliance_image_collection_group.command(name=cli_util.override('ocb_agent_svc.list_appliance_images.command_name', 'list-appliance-images'), help=u"""Returns a list of Appliance Images. \n[Command Reference](listApplianceImages)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "timeUpdated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_bridge', 'class': 'ApplianceImageCollection'})
@cli_util.wrap_exceptions
def list_appliance_images(ctx, from_json, all_pages, page_size, compartment_id, display_name, limit, page, sort_order, sort_by):

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
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_bridge', 'ocb_agent_svc', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_appliance_images,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_appliance_images,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_appliance_images(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@environment_collection_group.command(name=cli_util.override('ocb_agent_svc.list_environments.command_name', 'list-environments'), help=u"""Returns a list of source environments. \n[Command Reference](listEnvironments)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources where their lifecycleState matches the given lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--environment-id', help=u"""A filter to return only resources that match the given environment ID.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "timeUpdated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_bridge', 'class': 'EnvironmentCollection'})
@cli_util.wrap_exceptions
def list_environments(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, display_name, environment_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if environment_id is not None:
        kwargs['environment_id'] = environment_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_bridge', 'ocb_agent_svc', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_environments,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_environments,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_environments(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@environment_group.command(name=cli_util.override('ocb_agent_svc.remove_agent_dependency.command_name', 'remove'), help=u"""Adds a dependency to the source environment. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](removeAgentDependency)""")
@cli_util.option('--environment-id', required=True, help=u"""Unique environment identifier.""")
@cli_util.option('--agent-dependency-id', required=True, help=u"""The OCID of the agentDependency that should be removed from the source environment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_bridge', 'class': 'Environment'})
@cli_util.wrap_exceptions
def remove_agent_dependency(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, environment_id, agent_dependency_id, if_match):

    if isinstance(environment_id, six.string_types) and len(environment_id.strip()) == 0:
        raise click.UsageError('Parameter --environment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['agentDependencyId'] = agent_dependency_id

    client = cli_util.build_client('cloud_bridge', 'ocb_agent_svc', ctx)
    result = client.remove_agent_dependency(
        environment_id=environment_id,
        remove_agent_dependency_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_environment') and callable(getattr(client, 'get_environment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_environment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@agent_group.command(name=cli_util.override('ocb_agent_svc.update_agent.command_name', 'update'), help=u"""Updates the Agent. \n[Command Reference](updateAgent)""")
@cli_util.option('--agent-id', required=True, help=u"""Unique Agent identifier path parameter.""")
@cli_util.option('--display-name', help=u"""Agent identifier.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'cloud_bridge', 'class': 'Agent'})
@cli_util.wrap_exceptions
def update_agent(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, agent_id, display_name, freeform_tags, defined_tags, if_match):

    if isinstance(agent_id, six.string_types) and len(agent_id.strip()) == 0:
        raise click.UsageError('Parameter --agent-id cannot be whitespace or empty string')
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

    client = cli_util.build_client('cloud_bridge', 'ocb_agent_svc', ctx)
    result = client.update_agent(
        agent_id=agent_id,
        update_agent_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_agent') and callable(getattr(client, 'get_agent')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_agent(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@agent_dependency_group.command(name=cli_util.override('ocb_agent_svc.update_agent_dependency.command_name', 'update'), help=u"""Updates the AgentDependency. \n[Command Reference](updateAgentDependency)""")
@cli_util.option('--agent-dependency-id', required=True, help=u"""A unique AgentDependency identifier.""")
@cli_util.option('--display-name', help=u"""Display name of the Agent dependency.""")
@cli_util.option('--dependency-name', help=u"""Name of the dependency type. This should match the whitelisted enum of dependency names.""")
@cli_util.option('--dependency-version', help=u"""Version of the Agent dependency.""")
@cli_util.option('--description', help=u"""Description about the Agent dependency.""")
@cli_util.option('--namespace', help=u"""Object storage namespace associated with the customer's tenancy.""")
@cli_util.option('--bucket', help=u"""Object storage bucket where the dependency is uploaded.""")
@cli_util.option('--object-name', help=u"""Name of the dependency object uploaded by the customer.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--system-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{orcl-cloud: {free-tier-retain: true}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_agent_dependency(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, agent_dependency_id, display_name, dependency_name, dependency_version, description, namespace, bucket, object_name, freeform_tags, defined_tags, system_tags, if_match):

    if isinstance(agent_dependency_id, six.string_types) and len(agent_dependency_id.strip()) == 0:
        raise click.UsageError('Parameter --agent-dependency-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or system_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and system-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if dependency_name is not None:
        _details['dependencyName'] = dependency_name

    if dependency_version is not None:
        _details['dependencyVersion'] = dependency_version

    if description is not None:
        _details['description'] = description

    if namespace is not None:
        _details['namespace'] = namespace

    if bucket is not None:
        _details['bucket'] = bucket

    if object_name is not None:
        _details['objectName'] = object_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if system_tags is not None:
        _details['systemTags'] = cli_util.parse_json_parameter("system_tags", system_tags)

    client = cli_util.build_client('cloud_bridge', 'ocb_agent_svc', ctx)
    result = client.update_agent_dependency(
        agent_dependency_id=agent_dependency_id,
        update_agent_dependency_details=_details,
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


@environment_group.command(name=cli_util.override('ocb_agent_svc.update_environment.command_name', 'update'), help=u"""Updates the source environment. \n[Command Reference](updateEnvironment)""")
@cli_util.option('--environment-id', required=True, help=u"""Unique environment identifier.""")
@cli_util.option('--display-name', help=u"""Environment identifier.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'cloud_bridge', 'class': 'Environment'})
@cli_util.wrap_exceptions
def update_environment(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, environment_id, display_name, freeform_tags, defined_tags, if_match):

    if isinstance(environment_id, six.string_types) and len(environment_id.strip()) == 0:
        raise click.UsageError('Parameter --environment-id cannot be whitespace or empty string')
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

    client = cli_util.build_client('cloud_bridge', 'ocb_agent_svc', ctx)
    result = client.update_environment(
        environment_id=environment_id,
        update_environment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_environment') and callable(getattr(client, 'get_environment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_environment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@plugin_group.command(name=cli_util.override('ocb_agent_svc.update_plugin.command_name', 'update'), help=u"""Updates the plugin. \n[Command Reference](updatePlugin)""")
@cli_util.option('--agent-id', required=True, help=u"""Unique Agent identifier path parameter.""")
@cli_util.option('--plugin-name', required=True, help=u"""Unique plugin identifier path parameter.""")
@cli_util.option('--desired-state', help=u"""State to which the customer wants the plugin to move to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["UPDATING", "ACTIVE", "INACTIVE", "NEEDS_ATTENTION", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_bridge', 'class': 'Plugin'})
@cli_util.wrap_exceptions
def update_plugin(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, agent_id, plugin_name, desired_state, if_match):

    if isinstance(agent_id, six.string_types) and len(agent_id.strip()) == 0:
        raise click.UsageError('Parameter --agent-id cannot be whitespace or empty string')

    if isinstance(plugin_name, six.string_types) and len(plugin_name.strip()) == 0:
        raise click.UsageError('Parameter --plugin-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if desired_state is not None:
        _details['desiredState'] = desired_state

    client = cli_util.build_client('cloud_bridge', 'ocb_agent_svc', ctx)
    result = client.update_plugin(
        agent_id=agent_id,
        plugin_name=plugin_name,
        update_plugin_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_plugin') and callable(getattr(client, 'get_plugin')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_plugin(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
