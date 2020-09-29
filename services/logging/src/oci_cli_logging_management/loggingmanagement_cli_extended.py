# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


import click

from services.logging.src.oci_cli_logging_management.generated import loggingmanagement_cli
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types

# Override the name of the service for top-level index
loggingmanagement_cli.logging_root_group.short_help = "Logging Management"

##################################
# rename commands
##################################

# from
#   oci logging log change_log_log_group
# to
#   oci logging log change_log_group
cli_util.rename_command(loggingmanagement_cli, loggingmanagement_cli.log_group, loggingmanagement_cli.change_log_log_group, "change-log-group")

# from
#   oci logging unified-agent-configuration
# to
#   oci logging agent-configuration
cli_util.rename_command(loggingmanagement_cli, loggingmanagement_cli.logging_root_group, loggingmanagement_cli.unified_agent_configuration_group, "agent-configuration")

#  remove sub-command longer than 25 chars
loggingmanagement_cli.unified_agent_configuration_group.commands.pop(loggingmanagement_cli.create_unified_agent_configuration_unified_agent_logging_configuration.name)
loggingmanagement_cli.unified_agent_configuration_group.commands.pop(loggingmanagement_cli.update_unified_agent_configuration_unified_agent_logging_configuration.name)


##################################
# rename parameters
##################################

# Shorten parameters longer than 25 chars: --is-compartment-id-in-subtree to --compartmentidinsubtree
# from
#   oci logging log-group list ... --is_compartment_id_in_subtree ...
# to
#   oci logging log-group list ... --compartmentidinsubtree ...
@cli_util.copy_params_from_generated_command(loggingmanagement_cli.list_log_groups, params_to_exclude=['is_compartment_id_in_subtree'])
@cli_util.option('--compartmentidinsubtree', type=click.BOOL, help=u"""Specifies whether or not nested compartments should be traversed. Defaults to false.""")
@loggingmanagement_cli.log_group_group.command(name=cli_util.override('logging.list_log_groups.command_name', 'list'), help=loggingmanagement_cli.list_log_groups.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'logging', 'class': 'list[LogGroupSummary]'})
@cli_util.wrap_exceptions
def list_log_groups_extended(ctx, **kwargs):
    if 'compartmentidinsubtree' in kwargs:
        kwargs['is_compartment_id_in_subtree'] = kwargs['compartmentidinsubtree']
        kwargs.pop('compartmentidinsubtree')

    ctx.invoke(loggingmanagement_cli.list_log_groups, **kwargs)


# Fix the parameters that conflict with internal CLI parameters
# The conflict parameters are end with -parameterconflict
# from
#   oci logging log-saved-search create ... --query-parameterconflict ...
# to
#   oci logging log-saved-search create ... --log-query ...
@cli_util.copy_params_from_generated_command(loggingmanagement_cli.create_log_saved_search, params_to_exclude=['query_parameterconflict'])
@cli_util.option('--log-query', required=True, help=u"""The search query that is saved.""")
@loggingmanagement_cli.log_saved_search_group.command(name=cli_util.override('logging.create_log_saved_search.command_name', 'create'), help=loggingmanagement_cli.create_log_saved_search.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'logging', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'logging', 'class': 'dict(str, string)'}}, output_type={'module': 'logging', 'class': 'LogSavedSearch'})
@cli_util.wrap_exceptions
def create_log_saved_search_extended(ctx, **kwargs):
    if 'log_query' in kwargs:
        kwargs['query_parameterconflict'] = kwargs['log_query']
        kwargs.pop('log_query')

    ctx.invoke(loggingmanagement_cli.create_log_saved_search, **kwargs)


# Fix the parameters that conflict with internal CLI parameters
# The conflict parameters are end with -parameterconflict
# from
#   oci logging log-saved-search update ... --query-parameterconflict ...
# to
#   oci logging log-saved-search update ... --log-query ...
@cli_util.copy_params_from_generated_command(loggingmanagement_cli.update_log_saved_search, params_to_exclude=['query_parameterconflict'])
@cli_util.option('--log-query', help=u"""The search query that is saved.""")
@loggingmanagement_cli.log_saved_search_group.command(name=cli_util.override('logging.update_log_saved_search.command_name', 'update'), help=loggingmanagement_cli.update_log_saved_search.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'logging', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'logging', 'class': 'dict(str, string)'}}, output_type={'module': 'logging', 'class': 'LogSavedSearch'})
@cli_util.wrap_exceptions
def update_log_saved_search_extended(ctx, **kwargs):
    if 'log_query' in kwargs:
        kwargs['query_parameterconflict'] = kwargs['log_query']
        kwargs.pop('log_query')

    ctx.invoke(loggingmanagement_cli.update_log_saved_search, **kwargs)


# Shorten parameters longer than 25 chars: --unified-agent-configuration-id to --unified-agent-configuration-id
# from
#   oci logging agent-configuration change-compartment --unified-agent-configuration-id ...
# to
#   oci logging agent-configuration change-compartment --config-id ...
@cli_util.copy_params_from_generated_command(loggingmanagement_cli.change_unified_agent_configuration_compartment, params_to_exclude=['unified_agent_configuration_id'])
@cli_util.option('--config-id', required=True, help=u"""The OCID of the unified agent configuration.""")
@loggingmanagement_cli.unified_agent_configuration_group.command(name=cli_util.override('logging.change_unified_agent_configuration_compartment.command_name', 'change-compartment'), help=loggingmanagement_cli.change_unified_agent_configuration_compartment.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_unified_agent_configuration_compartment_extended(ctx, **kwargs):
    if 'config_id' in kwargs:
        kwargs['unified_agent_configuration_id'] = kwargs['config_id']
        kwargs.pop('config_id')

    ctx.invoke(loggingmanagement_cli.change_unified_agent_configuration_compartment, **kwargs)


# Shorten parameters longer than 25 chars: --unified-agent-configuration-id to --unified-agent-configuration-id
# from
#   oci logging agent-configuration delete --unified-agent-configuration-id ...
# to
#   oci logging agent-configuration delete --config-id
@cli_util.copy_params_from_generated_command(loggingmanagement_cli.delete_unified_agent_configuration, params_to_exclude=['unified_agent_configuration_id'])
@cli_util.option('--config-id', required=True, help=u"""The OCID of the unified agent configuration.""")
@loggingmanagement_cli.unified_agent_configuration_group.command(name=cli_util.override('logging.delete_unified_agent_configuration.command_name', 'delete'), help=loggingmanagement_cli.delete_unified_agent_configuration.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_unified_agent_configuration_extended(ctx, **kwargs):
    if 'config_id' in kwargs:
        kwargs['unified_agent_configuration_id'] = kwargs['config_id']
        kwargs.pop('config_id')

    ctx.invoke(loggingmanagement_cli.delete_unified_agent_configuration, **kwargs)


# Shorten parameters longer than 25 chars: --unified-agent-configuration-id to --unified-agent-configuration-id
# from
#   oci logging agent-configuration get --unified-agent-configuration-id ...
# to
#   oci logging agent-configuration get --config-id
@cli_util.copy_params_from_generated_command(loggingmanagement_cli.get_unified_agent_configuration, params_to_exclude=['unified_agent_configuration_id'])
@cli_util.option('--config-id', required=True, help=u"""The OCID of the unified agent configuration.""")
@loggingmanagement_cli.unified_agent_configuration_group.command(name=cli_util.override('logging.get_unified_agent_configuration.command_name', 'get'), help=loggingmanagement_cli.get_unified_agent_configuration.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'logging', 'class': 'UnifiedAgentConfiguration'})
@cli_util.wrap_exceptions
def get_unified_agent_configuration_extended(ctx, **kwargs):
    if 'config_id' in kwargs:
        kwargs['unified_agent_configuration_id'] = kwargs['config_id']
        kwargs.pop('config_id')

    ctx.invoke(loggingmanagement_cli.get_unified_agent_configuration, **kwargs)


# Shorten parameters longer than 25 chars: --unified-agent-configuration-id to --unified-agent-configuration-id
# from
#   oci logging agent-configuration update --unified-agent-configuration-id ...
# to
#   oci logging agent-configuration update --config-id
@cli_util.copy_params_from_generated_command(loggingmanagement_cli.update_unified_agent_configuration, params_to_exclude=['unified_agent_configuration_id'])
@cli_util.option('--config-id', required=True, help=u"""The OCID of the unified agent configuration.""")
@loggingmanagement_cli.unified_agent_configuration_group.command(name=cli_util.override('logging.update_unified_agent_configuration.command_name', 'update'), help=loggingmanagement_cli.update_unified_agent_configuration.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'logging', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'logging', 'class': 'dict(str, string)'}, 'service-configuration': {'module': 'logging', 'class': 'UnifiedAgentServiceConfigurationDetails'}, 'group-association': {'module': 'logging', 'class': 'GroupAssociationDetails'}})
@cli_util.wrap_exceptions
def update_unified_agent_configuration_extended(ctx, **kwargs):
    if 'config_id' in kwargs:
        kwargs['unified_agent_configuration_id'] = kwargs['config_id']
        kwargs.pop('config_id')

    ctx.invoke(loggingmanagement_cli.update_unified_agent_configuration, **kwargs)


# Shorten parameters longer than 25 chars: --unified-agent-configuration-id to --unified-agent-configuration-id
# from
#   oci logging agent-configuration create-unified-agent-configuration-unified-agent-logging-configuration --service-configuration-destination, --service-configuration-sources ...
# to
#   oci logging agent-configuration create-log-configuration --config-destination, --config-sources ...
@cli_util.copy_params_from_generated_command(loggingmanagement_cli.create_unified_agent_configuration_unified_agent_logging_configuration, params_to_exclude=['service_configuration_destination', 'service_configuration_sources'])
@cli_util.option('--service-conf-destination', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--service-conf-sources', type=custom_types.CLI_COMPLEX_TYPE, help=u"""
This option is a JSON list with items of type UnifiedAgentLoggingSource.  For documentation on UnifiedAgentLoggingSource please see our API reference: https://docs.cloud.oracle.com/api/#/en/loggingmanagement/20200531/datatypes/UnifiedAgentLoggingSource.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@loggingmanagement_cli.unified_agent_configuration_group.command(name=cli_util.override('logging.create_unified_agent_configuration_unified_agent_logging_configuration.command_name', 'create-log-configuration'), help=loggingmanagement_cli.create_unified_agent_configuration_unified_agent_logging_configuration.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'logging', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'logging', 'class': 'dict(str, string)'}, 'group-association': {'module': 'logging', 'class': 'GroupAssociationDetails'}, 'service-conf-sources': {'module': 'logging', 'class': 'list[UnifiedAgentLoggingSource]'}, 'service-conf-destination': {'module': 'logging', 'class': 'UnifiedAgentLoggingDestination'}})
@cli_util.wrap_exceptions
def create_unified_agent_configuration_unified_agent_logging_configuration_extended(ctx, **kwargs):
    if 'service_conf_destination' in kwargs:
        kwargs['service_configuration_destination'] = kwargs['service_conf_destination']
        kwargs.pop('service_conf_destination')
    if 'service_conf_sources' in kwargs:
        kwargs['service_configuration_sources'] = kwargs['service_conf_sources']
        kwargs.pop('service_conf_sources')

    ctx.invoke(loggingmanagement_cli.create_unified_agent_configuration_unified_agent_logging_configuration, **kwargs)


# Shorten parameters longer than 25 chars: --unified-agent-configuration-id to --unified-agent-configuration-id
# from
#   oci logging agent-configuration update-unified-agent-configuration-unified-agent-logging-configuration --service-configuration-destination, --service-configuration-sources --unified-agent-configuration-id ...
# to
#   oci logging agent-configuration update-log-configuration --config-destination, --config-sources --config-id ...
@cli_util.copy_params_from_generated_command(loggingmanagement_cli.update_unified_agent_configuration_unified_agent_logging_configuration, params_to_exclude=['service_configuration_destination', 'service_configuration_sources', 'unified_agent_configuration_id'])
@cli_util.option('--service-conf-destination', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--service-conf-sources', type=custom_types.CLI_COMPLEX_TYPE, help=u"""
This option is a JSON list with items of type UnifiedAgentLoggingSource.  For documentation on UnifiedAgentLoggingSource please see our API reference: https://docs.cloud.oracle.com/api/#/en/loggingmanagement/20200531/datatypes/UnifiedAgentLoggingSource.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--config-id', required=True, help=u"""The OCID of the unified agent configuration.""")
@loggingmanagement_cli.unified_agent_configuration_group.command(name=cli_util.override('logging.update_unified_agent_configuration_unified_agent_logging_configuration.command_name', 'update-log-configuration'), help=loggingmanagement_cli.update_unified_agent_configuration_unified_agent_logging_configuration.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'logging', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'logging', 'class': 'dict(str, string)'}, 'group-association': {'module': 'logging', 'class': 'GroupAssociationDetails'}, 'service-conf-sources': {'module': 'logging', 'class': 'list[UnifiedAgentLoggingSource]'}, 'service-conf-destination': {'module': 'logging', 'class': 'UnifiedAgentLoggingDestination'}})
@cli_util.wrap_exceptions
def update_unified_agent_configuration_unified_agent_logging_configuration_extended(ctx, **kwargs):
    if 'service_conf_destination' in kwargs:
        kwargs['service_configuration_destination'] = kwargs['service_conf_destination']
        kwargs.pop('service_conf_destination')

    if 'service_conf_sources' in kwargs:
        kwargs['service_configuration_sources'] = kwargs['service_conf_sources']
        kwargs.pop('service_conf_sources')

    if 'config_id' in kwargs:
        kwargs['unified_agent_configuration_id'] = kwargs['config_id']
        kwargs.pop('config_id')

    ctx.invoke(loggingmanagement_cli.update_unified_agent_configuration_unified_agent_logging_configuration, **kwargs)


# Shorten parameters longer than 25 chars: --is-compartment-id-in-subtree to --compartmentidinsubtree
# from
#   oci logging unified-agent-configuration list ... --is-compartment-id-in-subtree ...
# to
#   oci logging unified-agent-configuration list ... --compartmentidinsubtree ...
@cli_util.copy_params_from_generated_command(loggingmanagement_cli.list_unified_agent_configurations, params_to_exclude=['is_compartment_id_in_subtree'])
@cli_util.option('--compartmentidinsubtree', type=click.BOOL, help=u"""Specifies whether or not nested compartments should be traversed. Defaults to false.""")
@loggingmanagement_cli.unified_agent_configuration_group.command(name=cli_util.override('logging.list_unified_agent_configurations.command_name', 'list'), help=loggingmanagement_cli.list_unified_agent_configurations.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'logging', 'class': 'UnifiedAgentConfigurationCollection'})
@cli_util.wrap_exceptions
def list_unified_agent_configurations_extended(ctx, **kwargs):
    if 'compartmentidinsubtree' in kwargs:
        kwargs['is_compartment_id_in_subtree'] = kwargs['compartmentidinsubtree']
        kwargs.pop('compartmentidinsubtree')

    ctx.invoke(loggingmanagement_cli.list_unified_agent_configurations, **kwargs)
