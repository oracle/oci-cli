# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# Copyright (c) 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


import click
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from services.management_agent.src.oci_cli_management_agent.generated import managementagent_cli


# Group name shortening
# Update version-parameterconflict to  agent-version
@cli_util.copy_params_from_generated_command(managementagent_cli.list_management_agents, params_to_exclude=['version_parameterconflict'])
@managementagent_cli.management_agent_group.command(name=cli_util.override('management_agent.management_agent_group.command_name', 'list'), help=u"""Returns a list of Management Agent.""")
@cli_util.option('--agent-version', help=u"""Filter to return only Management Agents having the particular agent version.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_agent', 'class': 'list[ManagementAgentSummary]'})
@cli_util.wrap_exceptions
def version_parameterconflict_extended(ctx, **kwargs):
    if 'agent_version' in kwargs:
        kwargs['version_parameterconflict'] = kwargs['agent_version']
        kwargs.pop('agent_version')
    ctx.invoke(managementagent_cli.list_management_agents, **kwargs)


# Update management-agent-id to  agent-id
# @management_agent_group.command(name=cli_util.override('management_agent.delete_management_agent.command_name', 'delete'), help=u"""Deletes a Management Agent resource by identifier""")
# @cli_util.option('--management-agent-id', required=True, help=u"""Unique Management Agent identifier""")
@cli_util.copy_params_from_generated_command(managementagent_cli.delete_management_agent, params_to_exclude=['management_agent_id'])
@managementagent_cli.management_agent_group.command(name=cli_util.override('management_agent.delete_management_agent.command_name', 'delete'), help=u"""Deletes a Management Agent resource by identifier""")
@cli_util.option('--agent-id', required=True, help=u"""Unique Management Agent identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_management_agent(ctx, **kwargs):
    if 'agent_id' in kwargs:
        kwargs['management_agent_id'] = kwargs['agent_id']
        kwargs.pop('agent_id')
    ctx.invoke(managementagent_cli.delete_management_agent, **kwargs)


# Update management-agent-id to  agent-id
# @management_agent_group.command(name=cli_util.override('management_agent.get_management_agent.command_name', 'get'), help=u"""Gets complete details of the inventory of a given agent id""")
# @cli_util.option('--management-agent-id', required=True, help=u"""Unique Management Agent identifier""")
@cli_util.copy_params_from_generated_command(managementagent_cli.get_management_agent, params_to_exclude=['management_agent_id'])
@managementagent_cli.management_agent_group.command(name=cli_util.override('management_agent.get_management_agent.command_name', 'get'), help=u"""Gets complete details of the inventory of a given agent id""")
@cli_util.option('--agent-id', required=True, help=u"""Unique Management Agent identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_agent', 'class': 'ManagementAgent'})
@cli_util.wrap_exceptions
def get_management_agent(ctx, **kwargs):
    if 'agent_id' in kwargs:
        kwargs['management_agent_id'] = kwargs['agent_id']
        kwargs.pop('agent_id')
    ctx.invoke(managementagent_cli.get_management_agent, **kwargs)


# Update management-agent-id to  agent-id
# @management_agent_group.command(name=cli_util.override('management_agent.update_management_agent.command_name', 'update'), help=u"""API to update the console managed properties of the Management Agent.""")
# @cli_util.option('--management-agent-id', required=True, help=u"""Unique Management Agent identifier""")
@cli_util.copy_params_from_generated_command(managementagent_cli.update_management_agent, params_to_exclude=['management_agent_id'])
@managementagent_cli.management_agent_group.command(name=cli_util.override('management_agent.update_management_agent.command_name', 'update'), help=u"""API to update the console managed properties of the Management Agent.""")
@cli_util.option('--agent-id', required=True, help=u"""Unique Management Agent identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'management_agent', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'management_agent', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'management_agent', 'class': 'ManagementAgent'})
@cli_util.wrap_exceptions
def update_management_agent(ctx, **kwargs):
    if 'agent_id' in kwargs:
        kwargs['management_agent_id'] = kwargs['agent_id']
        kwargs.pop('agent_id')
    ctx.invoke(managementagent_cli.update_management_agent, **kwargs)


# Update management-agent-install-key-id to install-key
# @management_agent_install_key_group.command(name=cli_util.override('management_agent.update_management_agent_install_key.command_name', 'update'), help=u"""API to update the modifiable properties of the Management Agent install key.""")
# @cli_util.option('--management-agent-install-key-id', required=True, help=u"""Unique Management Agent Install Key identifier""")
#
@cli_util.copy_params_from_generated_command(managementagent_cli.update_management_agent_install_key, params_to_exclude=['management_agent_install_key_id'])
@managementagent_cli.management_agent_install_key_group.command(name=cli_util.override('management_agent.update_management_agent_install_key.command_name', 'update'), help=u"""API to update the modifiable properties of the Management Agent install key.""")
@cli_util.option('--install-key-id', required=True, help=u"""Unique Management Agent Install Key identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_agent', 'class': 'ManagementAgentInstallKey'})
@cli_util.wrap_exceptions
def update_management_agent_install_key(ctx, **kwargs):
    if 'install_key_id' in kwargs:
        kwargs['management_agent_install_key_id'] = kwargs['install_key_id']
        kwargs.pop('install_key_id')
    ctx.invoke(managementagent_cli.update_management_agent_install_key, **kwargs)


# Update management-agent-install-key-id to install-key
# @management_agent_install_key_group.command(name=cli_util.override('management_agent.delete_management_agent_install_key.command_name', 'delete'), help=u"""Deletes a Management Agent install Key resource by identifier""")
# @cli_util.option('--management-agent-install-key-id', required=True, help=u"""Unique Management Agent Install Key identifier""")
#
@cli_util.copy_params_from_generated_command(managementagent_cli.delete_management_agent_install_key, params_to_exclude=['management_agent_install_key_id'])
@managementagent_cli.management_agent_install_key_group.command(name=cli_util.override('management_agent.delete_management_agent_install_key.command_name', 'delete'), help=u"""Deletes a Management Agent install Key resource by identifier""")
@cli_util.option('--install-key-id', required=True, help=u"""Unique Management Agent Install Key identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_management_agent_install_key(ctx, **kwargs):
    if 'install_key_id' in kwargs:
        kwargs['management_agent_install_key_id'] = kwargs['install_key_id']
        kwargs.pop('install_key_id')
    ctx.invoke(managementagent_cli.delete_management_agent_install_key, **kwargs)


# Update management-agent-install-key-id to install-key
# @management_agent_install_key_group.command(name=cli_util.override('management_agent.get_management_agent_install_key.command_name', 'get'), help=u"""Gets complete details of the Agent install Key for a given key id""")
# @cli_util.option('--management-agent-install-key-id', required=True, help=u"""Unique Management Agent Install Key identifier""")
#
@cli_util.copy_params_from_generated_command(managementagent_cli.get_management_agent_install_key, params_to_exclude=['management_agent_install_key_id'])
@managementagent_cli.management_agent_install_key_group.command(name=cli_util.override('management_agent.get_management_agent_install_key.command_name', 'get'), help=u"""Gets complete details of the Agent install Key for a given key id""")
@cli_util.option('--install-key-id', required=True, help=u"""Unique Management Agent Install Key identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_agent', 'class': 'ManagementAgentInstallKey'})
@cli_util.wrap_exceptions
def get_management_agent_install_key(ctx, **kwargs):
    if 'install_key_id' in kwargs:
        kwargs['management_agent_install_key_id'] = kwargs['install_key_id']
        kwargs.pop('install_key_id')
    ctx.invoke(managementagent_cli.get_management_agent_install_key, **kwargs)


# Rename management_agent management_agent   to   management_agent agent
cli_util.rename_command(managementagent_cli, managementagent_cli.management_agent_root_group, managementagent_cli.management_agent_group, "agent")
cli_util.rename_command(managementagent_cli, managementagent_cli.management_agent_root_group, managementagent_cli.management_agent_image_group, "agent-image")
cli_util.rename_command(managementagent_cli, managementagent_cli.management_agent_root_group, managementagent_cli.management_agent_install_key_group, "install-key")

# Rename
#   oci management-agent install-key get-management-agent-install-key-content
#  to
#   oci management-agent install-key get-install-key-content
cli_util.rename_command(managementagent_cli, managementagent_cli.management_agent_install_key_group, managementagent_cli.get_management_agent_install_key_content, "get-install-key-content")

# Rename
#  oci management-agent management-agent-plugin list
# to
#  oci management-agent plugin list
cli_util.rename_command(managementagent_cli, managementagent_cli.management_agent_root_group, managementagent_cli.management_agent_plugin_group, "plugin")
