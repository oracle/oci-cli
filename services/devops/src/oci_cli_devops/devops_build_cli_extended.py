# Copyright (c) 2016, 2023, Oracle and/or its affiliates.
#
# This software is dual-licensed to you under the Universal Permissive License
# (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl and Apache License
# 2.0 as shown at https://www.apache.org/licenses/LICENSE-2.0. You may choose
# either license.
#
# If you elect to accept the software under the Apache License, Version 2.0,
# the following applies:
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# coding: utf-8
from services.devops.src.oci_cli_devops.generated import devops_cli
from oci_cli import cli_util
import click  # noqa: F401
import json  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401

# BUILD PIPELINE
# oci devops build-pipeline-collection list-build-pipelines -> oci devops build-pipeline-collection list
cli_util.rename_command(devops_cli, devops_cli.build_pipeline_collection_group, devops_cli.list_build_pipelines, "list")
# Move commands under 'oci devops build-pipeline-collection' -> 'oci devops build-pipeline'
devops_cli.devops_root_group.commands.pop(devops_cli.build_pipeline_collection_group.name)
devops_cli.build_pipeline_group.add_command(devops_cli.list_build_pipelines)


# BUILD EXECUTION
# oci devops build-execution-summary list-build-executions -> oci devops build-execution-summary list
cli_util.rename_command(devops_cli, devops_cli.build_run_summary_group, devops_cli.list_build_runs, "list")
# Move commands under 'oci devops build-execution-summary' -> 'oci devops build-execution'
devops_cli.devops_root_group.commands.pop(devops_cli.build_run_summary_group.name)
devops_cli.build_run_group.add_command(devops_cli.list_build_runs)


# BUILD PIPELINE STAGE
# oci devops build-pipeline-stage-summary list-build-pipeline-stages -> oci devops build-pipeline-stage-summary list
cli_util.rename_command(devops_cli, devops_cli.build_pipeline_stage_summary_group, devops_cli.list_build_pipeline_stages, "list")
# Move commands under 'oci devops build-pipeline-stage-summary' -> 'oci devops build-pipeline-stage'
devops_cli.devops_root_group.commands.pop(devops_cli.build_pipeline_stage_summary_group.name)
devops_cli.build_pipeline_stage_group.add_command(devops_cli.list_build_pipeline_stages)
# Rename build-pipeline-stage create commands
cli_util.rename_command(devops_cli, devops_cli.build_pipeline_stage_group, devops_cli.create_build_pipeline_stage_create_build_stage_details, "create-build-stage")
cli_util.rename_command(devops_cli, devops_cli.build_pipeline_stage_group, devops_cli.create_build_pipeline_stage_create_wait_stage_details, "create-wait-stage")
cli_util.rename_command(devops_cli, devops_cli.build_pipeline_stage_group, devops_cli.create_build_pipeline_stage_create_deliver_artifact_stage_details, "create-deliver-artifact-stage")
cli_util.rename_command(devops_cli, devops_cli.build_pipeline_stage_group, devops_cli.create_build_pipeline_stage_create_trigger_deployment_stage_details, "create-trigger-deployment-stage")
# Rename build-pipeline-stage update commands
cli_util.rename_command(devops_cli, devops_cli.build_pipeline_stage_group, devops_cli.update_build_pipeline_stage_update_build_stage_details, "update-build-stage")
cli_util.rename_command(devops_cli, devops_cli.build_pipeline_stage_group, devops_cli.update_build_pipeline_stage_update_wait_stage_details, "update-wait-stage")
cli_util.rename_command(devops_cli, devops_cli.build_pipeline_stage_group, devops_cli.update_build_pipeline_stage_update_deliver_artifact_stage_details, "update-deliver-artifact-stage")
cli_util.rename_command(devops_cli, devops_cli.build_pipeline_stage_group, devops_cli.update_build_pipeline_stage_update_trigger_deployment_stage_details, "update-trigger-deployment-stage")
# Remove oci devops build-pipeline-stage create
devops_cli.build_pipeline_stage_group.commands.pop(devops_cli.create_build_pipeline_stage.name)
# Remove oci devops build-pipeline-stage update
devops_cli.build_pipeline_stage_group.commands.pop(devops_cli.update_build_pipeline_stage.name)


# CONNECTION
# oci devops connection-collection list-connections -> oci devops connection-collection list
cli_util.rename_command(devops_cli, devops_cli.connection_collection_group, devops_cli.list_connections, "list")
# Move commands under 'oci devops connection-collection' -> 'oci devops connection'
devops_cli.devops_root_group.commands.pop(devops_cli.connection_collection_group.name)
devops_cli.connection_group.add_command(devops_cli.list_connections)
# Rename connection create commands
cli_util.rename_command(devops_cli, devops_cli.connection_group, devops_cli.create_connection_create_github_access_token_connection_details, "create-github-connection")
cli_util.rename_command(devops_cli, devops_cli.connection_group, devops_cli.create_connection_create_gitlab_access_token_connection_details, "create-gitlab-connection")
# Rename connection update commands
cli_util.rename_command(devops_cli, devops_cli.connection_group, devops_cli.update_connection_update_github_access_token_connection_details, "update-github-connection")
cli_util.rename_command(devops_cli, devops_cli.connection_group, devops_cli.update_connection_update_gitlab_access_token_connection_details, "update-gitlab-connection")
# Remove oci devops connection create
devops_cli.connection_group.commands.pop(devops_cli.create_connection.name)
# Remove oci devops connection update
devops_cli.connection_group.commands.pop(devops_cli.update_connection.name)


# TRIGGER
# oci devops trigger-collection list-triggers -> oci devops trigger-collection list
cli_util.rename_command(devops_cli, devops_cli.trigger_collection_group, devops_cli.list_triggers, "list")
# Move commands under 'oci devops trigger-collection' -> 'oci devops trigger'
devops_cli.devops_root_group.commands.pop(devops_cli.trigger_collection_group.name)
devops_cli.trigger_group.add_command(devops_cli.list_triggers)
# Rename trigger create commands
cli_util.rename_command(devops_cli, devops_cli.trigger_group, devops_cli.create_trigger_create_devops_code_repository_trigger_details, "create-devops-code-repo-trigger")
cli_util.rename_command(devops_cli, devops_cli.trigger_group, devops_cli.create_trigger_create_github_trigger_details, "create-github-trigger")
cli_util.rename_command(devops_cli, devops_cli.trigger_group, devops_cli.create_trigger_create_gitlab_trigger_details, "create-gitlab-trigger")
# Rename trigger update commands
cli_util.rename_command(devops_cli, devops_cli.trigger_group, devops_cli.update_trigger_update_devops_code_repository_trigger_details, "update-devops-code-repo-trigger")
cli_util.rename_command(devops_cli, devops_cli.trigger_group, devops_cli.update_trigger_update_github_trigger_details, "update-github-trigger")
cli_util.rename_command(devops_cli, devops_cli.trigger_group, devops_cli.update_trigger_update_gitlab_trigger_details, "update-gitlab-trigger")
# Remove oci devops trigger create
devops_cli.trigger_group.commands.pop(devops_cli.create_trigger.name)
# Remove oci devops trigger update
devops_cli.trigger_group.commands.pop(devops_cli.update_trigger.name)


@cli_util.copy_params_from_generated_command(
    devops_cli.get_build_pipeline_stage, params_to_exclude=['build_pipeline_stage_id'])
@devops_cli.build_pipeline_stage_group.command(
    name=cli_util.override('build_pipeline_stage.get_build_pipeline_stage.command_name', 'get'),
    help=devops_cli.get_build_pipeline_stage.help)
@cli_util.option('--stage-id', required=True, help=u"""Unique stage identifier.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'BuildPipelineStage'})
@cli_util.wrap_exceptions
def get_build_pipeline_stage_extended(ctx, **kwargs):
    if 'stage_id' in kwargs:
        kwargs['build_pipeline_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')
    ctx.invoke(devops_cli.get_build_pipeline_stage, **kwargs)


@cli_util.copy_params_from_generated_command(
    devops_cli.delete_build_pipeline_stage, params_to_exclude=['build_pipeline_stage_id'])
@devops_cli.build_pipeline_stage_group.command(
    name=cli_util.override('build_pipeline_stage.delete_build_pipeline_stage.command_name', 'delete'),
    help=devops_cli.delete_build_pipeline_stage.help)
@cli_util.option('--stage-id', required=True, help=u"""Unique stage identifier.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_build_pipeline_stage_extended(ctx, **kwargs):
    if 'stage_id' in kwargs:
        kwargs['build_pipeline_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')
    ctx.invoke(devops_cli.delete_build_pipeline_stage, **kwargs)


@cli_util.copy_params_from_generated_command(
    devops_cli.create_build_pipeline_stage_create_wait_stage_details,
    params_to_exclude=['build_pipeline_stage_predecessor_collection'])
@devops_cli.build_pipeline_stage_group.command(
    name=cli_util.override(
        'build_pipeline_stage.create_build_pipeline_stage_create_wait_stage_details.command_name', 'create-wait-stage'),
    help=devops_cli.create_build_pipeline_stage_create_wait_stage_details.help)
@cli_util.option('--stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'},
        'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'},
        'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'},
        'wait-criteria': {'module': 'devops', 'class': 'CreateWaitCriteriaDetails'}},
    output_type={'module': 'devops', 'class': 'BuildPipelineStage'})
@cli_util.wrap_exceptions
def create_build_pipeline_stage_create_wait_stage_details_extended(ctx, **kwargs):
    if 'stage_predecessor_collection' in kwargs:
        kwargs['build_pipeline_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')
    ctx.invoke(devops_cli.create_build_pipeline_stage_create_wait_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(
    devops_cli.create_build_pipeline_stage_create_build_stage_details,
    params_to_exclude=['build_pipeline_stage_predecessor_collection', 'private_access_config', 'build_runner_shape_config'])
@devops_cli.build_pipeline_stage_group.command(
    name=cli_util.override(
        'build_pipeline_stage.create_build_pipeline_stage_create_build_stage_details.command_name', 'create-build-stage'),
    help=devops_cli.create_build_pipeline_stage_create_build_stage_details.help)
@cli_util.option('--stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--network-channel', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--build-runner-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'},
        'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'},
        'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'},
        'build-source-collection': {'module': 'devops', 'class': 'BuildSourceCollection'},
        'network-channel': {'module': 'devops', 'class': 'NetworkChannel'}
    },
    output_type={'module': 'devops', 'class': 'BuildPipelineStage'})
@cli_util.wrap_exceptions
def create_build_pipeline_stage_create_build_stage_details_extended(ctx, **kwargs):
    if 'network_channel' in kwargs:
        kwargs['private_access_config'] = kwargs['network_channel']
        kwargs.pop('network_channel')
    if 'build_runner_config' in kwargs:
        kwargs['build_runner_shape_config'] = kwargs['build_runner_config']
        kwargs.pop('build_runner_config')
    if 'stage_predecessor_collection' in kwargs:
        kwargs['build_pipeline_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')
    ctx.invoke(devops_cli.create_build_pipeline_stage_create_build_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(
    devops_cli.create_build_pipeline_stage_create_deliver_artifact_stage_details,
    params_to_exclude=['build_pipeline_stage_predecessor_collection'])
@devops_cli.build_pipeline_stage_group.command(
    name=cli_util.override(
        'build_pipeline_stage.create_build_pipeline_stage_create_deliver_artifact_stage_details.command_name',
        'create-deliver-artifact-stage'),
    help=devops_cli.create_build_pipeline_stage_create_deliver_artifact_stage_details.help)
@cli_util.option('--stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'},
        'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'},
        'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'},
        'deliver-artifact-collection': {'module': 'devops', 'class': 'DeliverArtifactCollection'}},
    output_type={'module': 'devops', 'class': 'BuildPipelineStage'})
@cli_util.wrap_exceptions
def create_build_pipeline_stage_create_deliver_artifact_stage_details_extended(ctx, **kwargs):
    if 'stage_predecessor_collection' in kwargs:
        kwargs['build_pipeline_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')
    ctx.invoke(devops_cli.create_build_pipeline_stage_create_deliver_artifact_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(
    devops_cli.create_build_pipeline_stage_create_trigger_deployment_stage_details,
    params_to_exclude=['build_pipeline_stage_predecessor_collection'])
@devops_cli.build_pipeline_stage_group.command(
    name=cli_util.override(
        'build_pipeline_stage.create_build_pipeline_stage_create_trigger_deployment_stage_details.command_name',
        'create-trigger-deployment-stage'),
    help=devops_cli.create_build_pipeline_stage_create_trigger_deployment_stage_details.help)
@cli_util.option('--stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'},
        'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'},
        'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}},
    output_type={'module': 'devops', 'class': 'BuildPipelineStage'})
@cli_util.wrap_exceptions
def create_build_pipeline_stage_create_trigger_deployment_stage_details_extended(ctx, **kwargs):
    if 'stage_predecessor_collection' in kwargs:
        kwargs['build_pipeline_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')
    ctx.invoke(devops_cli.create_build_pipeline_stage_create_trigger_deployment_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(
    devops_cli.update_build_pipeline_stage_update_wait_stage_details,
    params_to_exclude=['build_pipeline_stage_id', 'build_pipeline_stage_predecessor_collection'])
@devops_cli.build_pipeline_stage_group.command(
    name=cli_util.override(
        'build_pipeline_stage.update_build_pipeline_stage_update_wait_stage_details.command_name', 'update-wait-stage'),
    help=devops_cli.update_build_pipeline_stage_update_wait_stage_details.help)
@cli_util.option('--stage-id', required=True, help=u"""Unique stage identifier.""")
@cli_util.option('--stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'},
        'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'},
        'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'},
        'wait-criteria': {'module': 'devops', 'class': 'UpdateWaitCriteriaDetails'}},
    output_type={'module': 'devops', 'class': 'BuildPipelineStage'})
@cli_util.wrap_exceptions
def update_build_pipeline_stage_update_wait_stage_details_extended(ctx, **kwargs):
    if 'stage_id' in kwargs:
        kwargs['build_pipeline_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')
    if 'stage_predecessor_collection' in kwargs:
        kwargs['build_pipeline_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')
    ctx.invoke(devops_cli.update_build_pipeline_stage_update_wait_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(
    devops_cli.update_build_pipeline_stage_update_build_stage_details,
    params_to_exclude=['build_pipeline_stage_id', 'build_pipeline_stage_predecessor_collection', 'private_access_config', 'build_runner_shape_config'])
@devops_cli.build_pipeline_stage_group.command(
    name=cli_util.override(
        'build_pipeline_stage.update_build_pipeline_stage_update_build_stage_details.command_name', 'update-build-stage'),
    help=devops_cli.update_build_pipeline_stage_update_build_stage_details.help)
@cli_util.option('--stage-id', required=True, help=u"""Unique stage identifier.""")
@cli_util.option('--stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--network-channel', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--build-runner-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'},
        'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'},
        'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'},
        'build-source-collection': {'module': 'devops', 'class': 'BuildSourceCollection'},
        'network-channel': {'module': 'devops', 'class': 'NetworkChannel'}
    },
    output_type={'module': 'devops', 'class': 'BuildPipelineStage'})
@cli_util.wrap_exceptions
def update_build_pipeline_stage_update_build_stage_details_extended(ctx, **kwargs):
    if 'stage_id' in kwargs:
        kwargs['build_pipeline_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')
    if 'network_channel' in kwargs:
        kwargs['private_access_config'] = kwargs['network_channel']
        kwargs.pop('network_channel')
    if 'build_runner_config' in kwargs:
        kwargs['build_runner_shape_config'] = kwargs['build_runner_config']
        kwargs.pop('build_runner_config')
    if 'stage_predecessor_collection' in kwargs:
        kwargs['build_pipeline_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')
    ctx.invoke(devops_cli.update_build_pipeline_stage_update_build_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(
    devops_cli.update_build_pipeline_stage_update_deliver_artifact_stage_details,
    params_to_exclude=['build_pipeline_stage_id', 'build_pipeline_stage_predecessor_collection'])
@devops_cli.build_pipeline_stage_group.command(
    name=cli_util.override(
        'build_pipeline_stage.update_build_pipeline_stage_update_deliver_artifact_stage_details.command_name',
        'update-deliver-artifact-stage'),
    help=devops_cli.update_build_pipeline_stage_update_deliver_artifact_stage_details.help)
@cli_util.option('--stage-id', required=True, help=u"""Unique stage identifier.""")
@cli_util.option('--stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'},
        'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'},
        'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'},
        'deliver-artifact-collection': {'module': 'devops', 'class': 'DeliverArtifactCollection'}},
    output_type={'module': 'devops', 'class': 'BuildPipelineStage'})
@cli_util.wrap_exceptions
def update_build_pipeline_stage_update_deliver_artifact_stage_details_extended(ctx, **kwargs):
    if 'stage_id' in kwargs:
        kwargs['build_pipeline_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')
    if 'stage_predecessor_collection' in kwargs:
        kwargs['build_pipeline_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')
    ctx.invoke(devops_cli.update_build_pipeline_stage_update_deliver_artifact_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(
    devops_cli.update_build_pipeline_stage_update_trigger_deployment_stage_details,
    params_to_exclude=['build_pipeline_stage_id', 'build_pipeline_stage_predecessor_collection'])
@devops_cli.build_pipeline_stage_group.command(
    name=cli_util.override(
        'build_pipeline_stage.update_build_pipeline_stage_update_trigger_deployment_stage_details.command_name',
        'update-trigger-deployment-stage'),
    help=devops_cli.update_build_pipeline_stage_update_trigger_deployment_stage_details.help)
@cli_util.option('--stage-id', required=True, help=u"""Unique stage identifier.""")
@cli_util.option('--stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'},
        'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'},
        'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}},
    output_type={'module': 'devops', 'class': 'BuildPipelineStage'})
@cli_util.wrap_exceptions
def update_build_pipeline_stage_update_trigger_deployment_stage_details_extended(ctx, **kwargs):
    if 'stage_id' in kwargs:
        kwargs['build_pipeline_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')
    if 'stage_predecessor_collection' in kwargs:
        kwargs['build_pipeline_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')
    ctx.invoke(devops_cli.update_build_pipeline_stage_update_trigger_deployment_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_connection_create_gitlab_access_token_connection_details, params_to_exclude=['access_token'])
@devops_cli.connection_group.command(name=cli_util.override('connection.create_connection_create_gitlab_access_token_connection_details.command_name', 'create-gitlab-connection'), help=devops_cli.create_connection_create_gitlab_access_token_connection_details.help)
@cli_util.option('--personal-access-token', required=True, help=u"""OCID of personal access token saved in secret store""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection_create_gitlab_access_token_connection_details_extended(ctx, **kwargs):
    if 'personal_access_token' in kwargs:
        kwargs['access_token'] = kwargs['personal_access_token']
        kwargs.pop('personal_access_token')
    ctx.invoke(devops_cli.create_connection_create_gitlab_access_token_connection_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_connection_update_gitlab_access_token_connection_details, params_to_exclude=['access_token'])
@devops_cli.connection_group.command(name=cli_util.override('connection.update_connection_update_gitlab_access_token_connection_details.command_name', 'update-gitlab-connection'), help=devops_cli.update_connection_update_gitlab_access_token_connection_details.help)
@cli_util.option('--personal-access-token', help=u"""OCID of personal access token saved in secret store""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Connection'})
@cli_util.wrap_exceptions
def update_connection_update_gitlab_access_token_connection_details_extended(ctx, **kwargs):
    if 'personal_access_token' in kwargs:
        kwargs['access_token'] = kwargs['personal_access_token']
        kwargs.pop('personal_access_token')
    ctx.invoke(devops_cli.update_connection_update_gitlab_access_token_connection_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_connection_create_github_access_token_connection_details, params_to_exclude=['access_token'])
@devops_cli.connection_group.command(name=cli_util.override('connection.create_connection_create_github_access_token_connection_details.command_name', 'create-github-connection'), help=devops_cli.create_connection_create_github_access_token_connection_details.help)
@cli_util.option('--personal-access-token', required=True, help=u"""OCID of personal access token saved in secret store""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection_create_github_access_token_connection_details_extended(ctx, **kwargs):
    if 'personal_access_token' in kwargs:
        kwargs['access_token'] = kwargs['personal_access_token']
        kwargs.pop('personal_access_token')
    ctx.invoke(devops_cli.create_connection_create_github_access_token_connection_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_connection_update_github_access_token_connection_details, params_to_exclude=['access_token'])
@devops_cli.connection_group.command(name=cli_util.override('connection.update_connection_update_github_access_token_connection_details.command_name', 'update-github-connection'), help=devops_cli.update_connection_update_github_access_token_connection_details.help)
@cli_util.option('--personal-access-token', help=u"""OCID of personal access token saved in secret store""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Connection'})
@cli_util.wrap_exceptions
def update_connection_update_github_access_token_connection_details_extended(ctx, **kwargs):
    if 'personal_access_token' in kwargs:
        kwargs['access_token'] = kwargs['personal_access_token']
        kwargs.pop('personal_access_token')
    ctx.invoke(devops_cli.update_connection_update_github_access_token_connection_details, **kwargs)


# oci devops deploy-stage create-deploy-stage-create-compute-instance-group-blue-green-deploy-stage-details -> oci devops deploy-stage create-deploy-compute-instance-group-blue-green-stage
cli_util.rename_command(devops_cli, devops_cli.deploy_stage_group, devops_cli.create_deploy_stage_create_compute_instance_group_blue_green_deploy_stage_details, "create-deploy-compute-instance-group-blue-green-stage")


# oci devops deploy-stage create-deploy-stage-create-compute-instance-group-blue-green-traffic-shift-deploy-stage-details -> oci devops deploy-stage create-compute-instance-group-blue-green-traffic-shift-stage
cli_util.rename_command(devops_cli, devops_cli.deploy_stage_group, devops_cli.create_deploy_stage_create_compute_instance_group_blue_green_traffic_shift_deploy_stage_details, "create-compute-instance-group-blue-green-traffic-shift-stage")


# oci devops deploy-stage create-deploy-stage-create-compute-instance-group-canary-approval-deploy-stage-details -> oci devops deploy-stage create-compute-instance-group-canary-approval-stage
cli_util.rename_command(devops_cli, devops_cli.deploy_stage_group, devops_cli.create_deploy_stage_create_compute_instance_group_canary_approval_deploy_stage_details, "create-compute-instance-group-canary-approval-stage")


# oci devops deploy-stage create-deploy-stage-create-compute-instance-group-canary-deploy-stage-details -> oci devops deploy-stage create-deploy-compute-instance-group-canary-stage
cli_util.rename_command(devops_cli, devops_cli.deploy_stage_group, devops_cli.create_deploy_stage_create_compute_instance_group_canary_deploy_stage_details, "create-deploy-compute-instance-group-canary-stage")


# oci devops deploy-stage create-deploy-stage-create-compute-instance-group-canary-traffic-shift-deploy-stage-details -> oci devops deploy-stage create-compute-instance-group-canary-traffic-shift-stage
cli_util.rename_command(devops_cli, devops_cli.deploy_stage_group, devops_cli.create_deploy_stage_create_compute_instance_group_canary_traffic_shift_deploy_stage_details, "create-compute-instance-group-canary-traffic-shift-stage")


# oci devops deploy-stage create-deploy-stage-create-oke-blue-green-deploy-stage-details -> oci devops deploy-stage create-deploy-oke-blue-green-stage
cli_util.rename_command(devops_cli, devops_cli.deploy_stage_group, devops_cli.create_deploy_stage_create_oke_blue_green_deploy_stage_details, "create-deploy-oke-blue-green-stage")


# oci devops deploy-stage create-deploy-stage-create-oke-blue-green-traffic-shift-deploy-stage-details -> oci devops deploy-stage create-oke-blue-green-traffic-shift-stage
cli_util.rename_command(devops_cli, devops_cli.deploy_stage_group, devops_cli.create_deploy_stage_create_oke_blue_green_traffic_shift_deploy_stage_details, "create-oke-blue-green-traffic-shift-stage")


# oci devops deploy-stage create-deploy-stage-create-oke-canary-approval-deploy-stage-details -> oci devops deploy-stage create-oke-canary-approval-stage
cli_util.rename_command(devops_cli, devops_cli.deploy_stage_group, devops_cli.create_deploy_stage_create_oke_canary_approval_deploy_stage_details, "create-oke-canary-approval-stage")


# oci devops deploy-stage create-deploy-stage-create-oke-canary-deploy-stage-details -> oci devops deploy-stage create-deploy-oke-canary-stage
cli_util.rename_command(devops_cli, devops_cli.deploy_stage_group, devops_cli.create_deploy_stage_create_oke_canary_deploy_stage_details, "create-deploy-oke-canary-stage")


# oci devops deploy-stage create-deploy-stage-create-oke-canary-traffic-shift-deploy-stage-details -> oci devops deploy-stage create-oke-canary-traffic-shift-stage
cli_util.rename_command(devops_cli, devops_cli.deploy_stage_group, devops_cli.create_deploy_stage_create_oke_canary_traffic_shift_deploy_stage_details, "create-oke-canary-traffic-shift-stage")


# oci devops deploy-stage update-deploy-stage-update-compute-instance-group-blue-green-deploy-stage-details -> oci devops deploy-stage update-deploy-compute-instance-group-blue-green-stage
cli_util.rename_command(devops_cli, devops_cli.deploy_stage_group, devops_cli.update_deploy_stage_update_compute_instance_group_blue_green_deploy_stage_details, "update-deploy-compute-instance-group-blue-green-stage")


# oci devops deploy-stage update-deploy-stage-update-compute-instance-group-blue-green-traffic-shift-deploy-stage-details -> oci devops deploy-stage update-compute-instance-group-blue-green-traffic-shift-stage
cli_util.rename_command(devops_cli, devops_cli.deploy_stage_group, devops_cli.update_deploy_stage_update_compute_instance_group_blue_green_traffic_shift_deploy_stage_details, "update-compute-instance-group-blue-green-traffic-shift-stage")


# oci devops deploy-stage update-deploy-stage-update-compute-instance-group-canary-approval-deploy-stage-details -> oci devops deploy-stage update-compute-instance-group-canary-approval-stage
cli_util.rename_command(devops_cli, devops_cli.deploy_stage_group, devops_cli.update_deploy_stage_update_compute_instance_group_canary_approval_deploy_stage_details, "update-compute-instance-group-canary-approval-stage")


# oci devops deploy-stage update-deploy-stage-update-compute-instance-group-canary-deploy-stage-details -> oci devops deploy-stage update-deploy-compute-instance-group-canary-stage
cli_util.rename_command(devops_cli, devops_cli.deploy_stage_group, devops_cli.update_deploy_stage_update_compute_instance_group_canary_deploy_stage_details, "update-deploy-compute-instance-group-canary-stage")


# oci devops deploy-stage update-deploy-stage-update-compute-instance-group-canary-traffic-shift-deploy-stage-details -> oci devops deploy-stage update-compute-instance-group-canary-traffic-shift-stage
cli_util.rename_command(devops_cli, devops_cli.deploy_stage_group, devops_cli.update_deploy_stage_update_compute_instance_group_canary_traffic_shift_deploy_stage_details, "update-compute-instance-group-canary-traffic-shift-stage")


# oci devops deploy-stage update-deploy-stage-update-oke-blue-green-deploy-stage-details -> oci devops deploy-stage update-deploy-oke-blue-green-stage
cli_util.rename_command(devops_cli, devops_cli.deploy_stage_group, devops_cli.update_deploy_stage_update_oke_blue_green_deploy_stage_details, "update-deploy-oke-blue-green-stage")


# oci devops deploy-stage update-deploy-stage-update-oke-blue-green-traffic-shift-deploy-stage-details -> oci devops deploy-stage update-oke-blue-green-traffic-shift-stage
cli_util.rename_command(devops_cli, devops_cli.deploy_stage_group, devops_cli.update_deploy_stage_update_oke_blue_green_traffic_shift_deploy_stage_details, "update-oke-blue-green-traffic-shift-stage")


# oci devops deploy-stage update-deploy-stage-update-oke-canary-approval-deploy-stage-details -> oci devops deploy-stage update-oke-canary-approval-stage
cli_util.rename_command(devops_cli, devops_cli.deploy_stage_group, devops_cli.update_deploy_stage_update_oke_canary_approval_deploy_stage_details, "update-oke-canary-approval-stage")


# oci devops deploy-stage update-deploy-stage-update-oke-canary-deploy-stage-details -> oci devops deploy-stage update-deploy-oke-canary-stage
cli_util.rename_command(devops_cli, devops_cli.deploy_stage_group, devops_cli.update_deploy_stage_update_oke_canary_deploy_stage_details, "update-deploy-oke-canary-stage")


# oci devops deploy-stage update-deploy-stage-update-oke-canary-traffic-shift-deploy-stage-details -> oci devops deploy-stage update-oke-canary-traffic-shift-stage
cli_util.rename_command(devops_cli, devops_cli.deploy_stage_group, devops_cli.update_deploy_stage_update_oke_canary_traffic_shift_deploy_stage_details, "update-oke-canary-traffic-shift-stage")


# oci devops deployment create-deployment-create-single-deploy-stage-redeployment-details -> oci devops deployment create-single-stage-redeployment
cli_util.rename_command(devops_cli, devops_cli.deployment_group, devops_cli.create_deployment_create_single_deploy_stage_redeployment_details, "create-single-stage-redeployment")


# oci devops deployment update-deployment-update-single-deploy-stage-redeployment-details -> oci devops deployment update-single-stage-redeployment
cli_util.rename_command(devops_cli, devops_cli.deployment_group, devops_cli.update_deployment_update_single_deploy_stage_redeployment_details, "update-single-stage-redeployment")


@cli_util.copy_params_from_generated_command(devops_cli.create_deploy_stage_create_compute_instance_group_blue_green_deploy_stage_details, params_to_exclude=['deploy_environment_id_a', 'deploy_environment_id_b', 'deploy_pipeline_id', 'deploy_stage_predecessor_collection', 'deployment_spec_deploy_artifact_id', 'deploy_artifact_ids'])
@devops_cli.deploy_stage_group.command(name=devops_cli.create_deploy_stage_create_compute_instance_group_blue_green_deploy_stage_details.name, help=devops_cli.create_deploy_stage_create_compute_instance_group_blue_green_deploy_stage_details.help)
@cli_util.option('--environment-id-a', required=True, help=u"""First compute instance group environment OCID for deployment. [required]""")
@cli_util.option('--environment-id-b', required=True, help=u"""Second compute instance group environment OCID for deployment. [required]""")
@cli_util.option('--pipeline-id', required=True, help=u"""The OCID of a pipeline. [required]""")
@cli_util.option('--stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.
 [required]""")
@cli_util.option('--deployment-spec-artifact-id', required=True, help=u"""The OCID of the artifact that contains the deployment specification. [required]""")
@cli_util.option('--artifact-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of file artifact OCIDs to deploy.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollout-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupRolloutPolicy'}, 'failure-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupFailurePolicy'}, 'test-load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}, 'production-load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_compute_instance_group_blue_green_deploy_stage_details_extended(ctx, **kwargs):
    if 'environment_id_a' in kwargs:
        kwargs['deploy_environment_id_a'] = kwargs['environment_id_a']
        kwargs.pop('environment_id_a')

    if 'environment_id_b' in kwargs:
        kwargs['deploy_environment_id_b'] = kwargs['environment_id_b']
        kwargs.pop('environment_id_b')

    if 'pipeline_id' in kwargs:
        kwargs['deploy_pipeline_id'] = kwargs['pipeline_id']
        kwargs.pop('pipeline_id')

    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')

    if 'deployment_spec_artifact_id' in kwargs:
        kwargs['deployment_spec_deploy_artifact_id'] = kwargs['deployment_spec_artifact_id']
        kwargs.pop('deployment_spec_artifact_id')

    if 'artifact_ids' in kwargs:
        kwargs['deploy_artifact_ids'] = kwargs['artifact_ids']
        kwargs.pop('artifact_ids')

    ctx.invoke(devops_cli.create_deploy_stage_create_compute_instance_group_blue_green_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_deploy_stage_create_compute_instance_group_blue_green_traffic_shift_deploy_stage_details, params_to_exclude=['compute_instance_group_blue_green_deployment_deploy_stage_id', 'deploy_pipeline_id', 'deploy_stage_predecessor_collection'])
@devops_cli.deploy_stage_group.command(name=devops_cli.create_deploy_stage_create_compute_instance_group_blue_green_traffic_shift_deploy_stage_details.name, help=devops_cli.create_deploy_stage_create_compute_instance_group_blue_green_traffic_shift_deploy_stage_details.help)
@cli_util.option('--compute-instance-group-blue-green-stage-id', required=True, help=u"""The OCID of the upstream compute instance group blue-green deployment stage in this pipeline. [required]""")
@cli_util.option('--pipeline-id', required=True, help=u"""The OCID of a pipeline. [required]""")
@cli_util.option('--stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.
 [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_compute_instance_group_blue_green_traffic_shift_deploy_stage_details_extended(ctx, **kwargs):
    if 'compute_instance_group_blue_green_stage_id' in kwargs:
        kwargs['compute_instance_group_blue_green_deployment_deploy_stage_id'] = kwargs['compute_instance_group_blue_green_stage_id']
        kwargs.pop('compute_instance_group_blue_green_stage_id')

    if 'pipeline_id' in kwargs:
        kwargs['deploy_pipeline_id'] = kwargs['pipeline_id']
        kwargs.pop('pipeline_id')

    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')

    ctx.invoke(devops_cli.create_deploy_stage_create_compute_instance_group_blue_green_traffic_shift_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_deploy_stage_create_compute_instance_group_canary_approval_deploy_stage_details, params_to_exclude=['compute_instance_group_canary_traffic_shift_deploy_stage_id', 'deploy_pipeline_id', 'deploy_stage_predecessor_collection'])
@devops_cli.deploy_stage_group.command(name=devops_cli.create_deploy_stage_create_compute_instance_group_canary_approval_deploy_stage_details.name, help=devops_cli.create_deploy_stage_create_compute_instance_group_canary_approval_deploy_stage_details.help)
@cli_util.option('--compute-instance-group-canary-traffic-shift-stage-id', required=True, help=u"""A compute instance group canary traffic shift stage OCID for load balancer. [required]""")
@cli_util.option('--pipeline-id', required=True, help=u"""The OCID of a pipeline. [required]""")
@cli_util.option('--stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.
 [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'approval-policy': {'module': 'devops', 'class': 'ApprovalPolicy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_compute_instance_group_canary_approval_deploy_stage_details_extended(ctx, **kwargs):
    if 'compute_instance_group_canary_traffic_shift_stage_id' in kwargs:
        kwargs['compute_instance_group_canary_traffic_shift_deploy_stage_id'] = kwargs['compute_instance_group_canary_traffic_shift_stage_id']
        kwargs.pop('compute_instance_group_canary_traffic_shift_stage_id')

    if 'pipeline_id' in kwargs:
        kwargs['deploy_pipeline_id'] = kwargs['pipeline_id']
        kwargs.pop('pipeline_id')

    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')

    ctx.invoke(devops_cli.create_deploy_stage_create_compute_instance_group_canary_approval_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_deploy_stage_create_compute_instance_group_canary_deploy_stage_details, params_to_exclude=['compute_instance_group_deploy_environment_id', 'deploy_pipeline_id', 'deploy_stage_predecessor_collection', 'deployment_spec_deploy_artifact_id', 'deploy_artifact_ids'])
@devops_cli.deploy_stage_group.command(name=devops_cli.create_deploy_stage_create_compute_instance_group_canary_deploy_stage_details.name, help=devops_cli.create_deploy_stage_create_compute_instance_group_canary_deploy_stage_details.help)
@cli_util.option('--compute-instance-group-environment-id', required=True, help=u"""A compute instance group environment OCID for canary deployment. [required]""")
@cli_util.option('--pipeline-id', required=True, help=u"""The OCID of a pipeline. [required]""")
@cli_util.option('--stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.
 [required]""")
@cli_util.option('--deployment-spec-artifact-id', required=True, help=u"""The OCID of the artifact that contains the deployment specification. [required]""")
@cli_util.option('--artifact-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of file artifact OCIDs to deploy.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollout-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupRolloutPolicy'}, 'test-load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}, 'production-load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_compute_instance_group_canary_deploy_stage_details_extended(ctx, **kwargs):
    if 'compute_instance_group_environment_id' in kwargs:
        kwargs['compute_instance_group_deploy_environment_id'] = kwargs['compute_instance_group_environment_id']
        kwargs.pop('compute_instance_group_environment_id')

    if 'pipeline_id' in kwargs:
        kwargs['deploy_pipeline_id'] = kwargs['pipeline_id']
        kwargs.pop('pipeline_id')

    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')

    if 'deployment_spec_artifact_id' in kwargs:
        kwargs['deployment_spec_deploy_artifact_id'] = kwargs['deployment_spec_artifact_id']
        kwargs.pop('deployment_spec_artifact_id')

    if 'artifact_ids' in kwargs:
        kwargs['deploy_artifact_ids'] = kwargs['artifact_ids']
        kwargs.pop('artifact_ids')

    ctx.invoke(devops_cli.create_deploy_stage_create_compute_instance_group_canary_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_deploy_stage_create_compute_instance_group_canary_traffic_shift_deploy_stage_details, params_to_exclude=['compute_instance_group_canary_deploy_stage_id', 'deploy_pipeline_id', 'deploy_stage_predecessor_collection'])
@devops_cli.deploy_stage_group.command(name=devops_cli.create_deploy_stage_create_compute_instance_group_canary_traffic_shift_deploy_stage_details.name, help=devops_cli.create_deploy_stage_create_compute_instance_group_canary_traffic_shift_deploy_stage_details.help)
@cli_util.option('--compute-instance-group-canary-stage-id', required=True, help=u"""A compute instance group canary stage OCID for load balancer. [required]""")
@cli_util.option('--pipeline-id', required=True, help=u"""The OCID of a pipeline. [required]""")
@cli_util.option('--stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.
 [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'rollout-policy': {'module': 'devops', 'class': 'LoadBalancerTrafficShiftRolloutPolicy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_compute_instance_group_canary_traffic_shift_deploy_stage_details_extended(ctx, **kwargs):
    if 'compute_instance_group_canary_stage_id' in kwargs:
        kwargs['compute_instance_group_canary_deploy_stage_id'] = kwargs['compute_instance_group_canary_stage_id']
        kwargs.pop('compute_instance_group_canary_stage_id')

    if 'pipeline_id' in kwargs:
        kwargs['deploy_pipeline_id'] = kwargs['pipeline_id']
        kwargs.pop('pipeline_id')

    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')

    ctx.invoke(devops_cli.create_deploy_stage_create_compute_instance_group_canary_traffic_shift_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_deploy_stage_create_oke_blue_green_deploy_stage_details, params_to_exclude=['deploy_pipeline_id', 'deploy_stage_predecessor_collection', 'kubernetes_manifest_deploy_artifact_ids', 'oke_cluster_deploy_environment_id'])
@devops_cli.deploy_stage_group.command(name=devops_cli.create_deploy_stage_create_oke_blue_green_deploy_stage_details.name, help=devops_cli.create_deploy_stage_create_oke_blue_green_deploy_stage_details.help)
@cli_util.option('--pipeline-id', required=True, help=u"""The OCID of a pipeline. [required]""")
@cli_util.option('--stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.
 [required]""")
@cli_util.option('--kubernetes-manifest-artifact-ids', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Kubernetes manifest artifact OCIDs.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.
 [required]""")
@cli_util.option('--oke-cluster-environment-id', required=True, help=u"""Kubernetes cluster environment OCID for deployment. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'kubernetes-manifest-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'blue-green-strategy': {'module': 'devops', 'class': 'OkeBlueGreenStrategy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_oke_blue_green_deploy_stage_details_extended(ctx, **kwargs):
    if 'pipeline_id' in kwargs:
        kwargs['deploy_pipeline_id'] = kwargs['pipeline_id']
        kwargs.pop('pipeline_id')

    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')

    if 'kubernetes_manifest_artifact_ids' in kwargs:
        kwargs['kubernetes_manifest_deploy_artifact_ids'] = kwargs['kubernetes_manifest_artifact_ids']
        kwargs.pop('kubernetes_manifest_artifact_ids')

    if 'oke_cluster_environment_id' in kwargs:
        kwargs['oke_cluster_deploy_environment_id'] = kwargs['oke_cluster_environment_id']
        kwargs.pop('oke_cluster_environment_id')

    ctx.invoke(devops_cli.create_deploy_stage_create_oke_blue_green_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_deploy_stage_create_oke_blue_green_traffic_shift_deploy_stage_details, params_to_exclude=['deploy_pipeline_id', 'deploy_stage_predecessor_collection', 'oke_blue_green_deploy_stage_id'])
@devops_cli.deploy_stage_group.command(name=devops_cli.create_deploy_stage_create_oke_blue_green_traffic_shift_deploy_stage_details.name, help=devops_cli.create_deploy_stage_create_oke_blue_green_traffic_shift_deploy_stage_details.help)
@cli_util.option('--pipeline-id', required=True, help=u"""The OCID of a pipeline. [required]""")
@cli_util.option('--stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.
 [required]""")
@cli_util.option('--oke-blue-green-stage-id', required=True, help=u"""The OCID of the upstream OKE blue-green deployment stage in this pipeline. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_oke_blue_green_traffic_shift_deploy_stage_details_extended(ctx, **kwargs):
    if 'pipeline_id' in kwargs:
        kwargs['deploy_pipeline_id'] = kwargs['pipeline_id']
        kwargs.pop('pipeline_id')

    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')

    if 'oke_blue_green_stage_id' in kwargs:
        kwargs['oke_blue_green_deploy_stage_id'] = kwargs['oke_blue_green_stage_id']
        kwargs.pop('oke_blue_green_stage_id')

    ctx.invoke(devops_cli.create_deploy_stage_create_oke_blue_green_traffic_shift_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_deploy_stage_create_oke_canary_approval_deploy_stage_details, params_to_exclude=['deploy_pipeline_id', 'deploy_stage_predecessor_collection', 'oke_canary_traffic_shift_deploy_stage_id'])
@devops_cli.deploy_stage_group.command(name=devops_cli.create_deploy_stage_create_oke_canary_approval_deploy_stage_details.name, help=devops_cli.create_deploy_stage_create_oke_canary_approval_deploy_stage_details.help)
@cli_util.option('--pipeline-id', required=True, help=u"""The OCID of a pipeline. [required]""")
@cli_util.option('--stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.
 [required]""")
@cli_util.option('--oke-canary-traffic-shift-stage-id', required=True, help=u"""The OCID of an upstream OKE canary deployment traffic shift stage in this pipeline. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'approval-policy': {'module': 'devops', 'class': 'ApprovalPolicy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_oke_canary_approval_deploy_stage_details_extended(ctx, **kwargs):
    if 'pipeline_id' in kwargs:
        kwargs['deploy_pipeline_id'] = kwargs['pipeline_id']
        kwargs.pop('pipeline_id')

    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')

    if 'oke_canary_traffic_shift_stage_id' in kwargs:
        kwargs['oke_canary_traffic_shift_deploy_stage_id'] = kwargs['oke_canary_traffic_shift_stage_id']
        kwargs.pop('oke_canary_traffic_shift_stage_id')

    ctx.invoke(devops_cli.create_deploy_stage_create_oke_canary_approval_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_deploy_stage_create_oke_canary_deploy_stage_details, params_to_exclude=['deploy_pipeline_id', 'deploy_stage_predecessor_collection', 'kubernetes_manifest_deploy_artifact_ids', 'oke_cluster_deploy_environment_id'])
@devops_cli.deploy_stage_group.command(name=devops_cli.create_deploy_stage_create_oke_canary_deploy_stage_details.name, help=devops_cli.create_deploy_stage_create_oke_canary_deploy_stage_details.help)
@cli_util.option('--pipeline-id', required=True, help=u"""The OCID of a pipeline. [required]""")
@cli_util.option('--stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.
 [required]""")
@cli_util.option('--kubernetes-manifest-artifact-ids', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Kubernetes manifest artifact OCIDs.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.
 [required]""")
@cli_util.option('--oke-cluster-environment-id', required=True, help=u"""Kubernetes cluster environment OCID for deployment. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'kubernetes-manifest-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'canary-strategy': {'module': 'devops', 'class': 'OkeCanaryStrategy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_oke_canary_deploy_stage_details_extended(ctx, **kwargs):
    if 'pipeline_id' in kwargs:
        kwargs['deploy_pipeline_id'] = kwargs['pipeline_id']
        kwargs.pop('pipeline_id')

    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')

    if 'kubernetes_manifest_artifact_ids' in kwargs:
        kwargs['kubernetes_manifest_deploy_artifact_ids'] = kwargs['kubernetes_manifest_artifact_ids']
        kwargs.pop('kubernetes_manifest_artifact_ids')

    if 'oke_cluster_environment_id' in kwargs:
        kwargs['oke_cluster_deploy_environment_id'] = kwargs['oke_cluster_environment_id']
        kwargs.pop('oke_cluster_environment_id')

    ctx.invoke(devops_cli.create_deploy_stage_create_oke_canary_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_deploy_stage_create_oke_canary_traffic_shift_deploy_stage_details, params_to_exclude=['deploy_pipeline_id', 'deploy_stage_predecessor_collection', 'oke_canary_deploy_stage_id'])
@devops_cli.deploy_stage_group.command(name=devops_cli.create_deploy_stage_create_oke_canary_traffic_shift_deploy_stage_details.name, help=devops_cli.create_deploy_stage_create_oke_canary_traffic_shift_deploy_stage_details.help)
@cli_util.option('--pipeline-id', required=True, help=u"""The OCID of a pipeline. [required]""")
@cli_util.option('--stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.
 [required]""")
@cli_util.option('--oke-canary-stage-id', required=True, help=u"""The OCID of an upstream OKE canary deployment stage in this pipeline. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'rollout-policy': {'module': 'devops', 'class': 'LoadBalancerTrafficShiftRolloutPolicy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_oke_canary_traffic_shift_deploy_stage_details_extended(ctx, **kwargs):
    if 'pipeline_id' in kwargs:
        kwargs['deploy_pipeline_id'] = kwargs['pipeline_id']
        kwargs.pop('pipeline_id')

    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')

    if 'oke_canary_stage_id' in kwargs:
        kwargs['oke_canary_deploy_stage_id'] = kwargs['oke_canary_stage_id']
        kwargs.pop('oke_canary_stage_id')

    ctx.invoke(devops_cli.create_deploy_stage_create_oke_canary_traffic_shift_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_stage_update_compute_instance_group_blue_green_deploy_stage_details, params_to_exclude=['deploy_stage_id', 'deploy_artifact_ids', 'deploy_stage_predecessor_collection', 'deployment_spec_deploy_artifact_id'])
@devops_cli.deploy_stage_group.command(name=devops_cli.update_deploy_stage_update_compute_instance_group_blue_green_deploy_stage_details.name, help=devops_cli.update_deploy_stage_update_compute_instance_group_blue_green_deploy_stage_details.help)
@cli_util.option('--stage-id', required=True, help=u"""Unique stage identifier. [required]""")
@cli_util.option('--artifact-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of file artifact OCIDs to deploy.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--deployment-spec-artifact-id', help=u"""The OCID of the artifact that contains the deployment specification.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollout-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupRolloutPolicy'}, 'failure-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupFailurePolicy'}, 'test-load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_compute_instance_group_blue_green_deploy_stage_details_extended(ctx, **kwargs):
    if 'stage_id' in kwargs:
        kwargs['deploy_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')

    if 'artifact_ids' in kwargs:
        kwargs['deploy_artifact_ids'] = kwargs['artifact_ids']
        kwargs.pop('artifact_ids')

    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')

    if 'deployment_spec_artifact_id' in kwargs:
        kwargs['deployment_spec_deploy_artifact_id'] = kwargs['deployment_spec_artifact_id']
        kwargs.pop('deployment_spec_artifact_id')

    ctx.invoke(devops_cli.update_deploy_stage_update_compute_instance_group_blue_green_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_stage_update_compute_instance_group_blue_green_traffic_shift_deploy_stage_details, params_to_exclude=['deploy_stage_id', 'deploy_stage_predecessor_collection'])
@devops_cli.deploy_stage_group.command(name=devops_cli.update_deploy_stage_update_compute_instance_group_blue_green_traffic_shift_deploy_stage_details.name, help=devops_cli.update_deploy_stage_update_compute_instance_group_blue_green_traffic_shift_deploy_stage_details.help)
@cli_util.option('--stage-id', required=True, help=u"""Unique stage identifier. [required]""")
@cli_util.option('--stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_compute_instance_group_blue_green_traffic_shift_deploy_stage_details_extended(ctx, **kwargs):
    if 'stage_id' in kwargs:
        kwargs['deploy_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')

    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')

    ctx.invoke(devops_cli.update_deploy_stage_update_compute_instance_group_blue_green_traffic_shift_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_stage_update_compute_instance_group_canary_approval_deploy_stage_details, params_to_exclude=['deploy_stage_id', 'compute_instance_group_canary_traffic_shift_deploy_stage_id', 'deploy_stage_predecessor_collection'])
@devops_cli.deploy_stage_group.command(name=devops_cli.update_deploy_stage_update_compute_instance_group_canary_approval_deploy_stage_details.name, help=devops_cli.update_deploy_stage_update_compute_instance_group_canary_approval_deploy_stage_details.help)
@cli_util.option('--stage-id', help=u"""Unique stage identifier. [required]""")
@cli_util.option('--stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'approval-policy': {'module': 'devops', 'class': 'ApprovalPolicy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_compute_instance_group_canary_approval_deploy_stage_details_extended(ctx, **kwargs):
    if 'stage_id' in kwargs:
        kwargs['deploy_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')

    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')

    ctx.invoke(devops_cli.update_deploy_stage_update_compute_instance_group_canary_approval_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_stage_update_compute_instance_group_canary_deploy_stage_details, params_to_exclude=['deploy_stage_id', 'deploy_artifact_ids', 'deploy_stage_predecessor_collection', 'deployment_spec_deploy_artifact_id'])
@devops_cli.deploy_stage_group.command(name=devops_cli.update_deploy_stage_update_compute_instance_group_canary_deploy_stage_details.name, help=devops_cli.update_deploy_stage_update_compute_instance_group_canary_deploy_stage_details.help)
@cli_util.option('--stage-id', required=True, help=u"""Unique stage identifier. [required]""")
@cli_util.option('--artifact-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of file artifact OCIDs to deploy.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--deployment-spec-artifact-id', help=u"""The OCID of the artifact that contains the deployment specification.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollout-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupRolloutPolicy'}, 'test-load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_compute_instance_group_canary_deploy_stage_details_extended(ctx, **kwargs):
    if 'stage_id' in kwargs:
        kwargs['deploy_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')

    if 'artifact_ids' in kwargs:
        kwargs['deploy_artifact_ids'] = kwargs['artifact_ids']
        kwargs.pop('artifact_ids')

    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')

    if 'deployment_spec_artifact_id' in kwargs:
        kwargs['deployment_spec_deploy_artifact_id'] = kwargs['deployment_spec_artifact_id']
        kwargs.pop('deployment_spec_artifact_id')

    ctx.invoke(devops_cli.update_deploy_stage_update_compute_instance_group_canary_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_stage_update_compute_instance_group_canary_traffic_shift_deploy_stage_details, params_to_exclude=['deploy_stage_id', 'deploy_stage_predecessor_collection'])
@devops_cli.deploy_stage_group.command(name=devops_cli.update_deploy_stage_update_compute_instance_group_canary_traffic_shift_deploy_stage_details.name, help=devops_cli.update_deploy_stage_update_compute_instance_group_canary_traffic_shift_deploy_stage_details.help)
@cli_util.option('--stage-id', required=True, help=u"""Unique stage identifier. [required]""")
@cli_util.option('--stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'rollout-policy': {'module': 'devops', 'class': 'LoadBalancerTrafficShiftRolloutPolicy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_compute_instance_group_canary_traffic_shift_deploy_stage_details_extended(ctx, **kwargs):
    if 'stage_id' in kwargs:
        kwargs['deploy_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')

    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')

    ctx.invoke(devops_cli.update_deploy_stage_update_compute_instance_group_canary_traffic_shift_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_stage_update_oke_blue_green_deploy_stage_details, params_to_exclude=['deploy_stage_id', 'deploy_stage_predecessor_collection', 'kubernetes_manifest_deploy_artifact_ids'])
@devops_cli.deploy_stage_group.command(name=devops_cli.update_deploy_stage_update_oke_blue_green_deploy_stage_details.name, help=devops_cli.update_deploy_stage_update_oke_blue_green_deploy_stage_details.help)
@cli_util.option('--stage-id', required=True, help=u"""Unique stage identifier. [required]""")
@cli_util.option('--stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--kubernetes-manifest-artifact-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Kubernetes manifest artifact OCIDs, the manifests should not include any job resource.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'kubernetes-manifest-artifact-ids': {'module': 'devops', 'class': 'list[string]'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_oke_blue_green_deploy_stage_details_extended(ctx, **kwargs):
    if 'stage_id' in kwargs:
        kwargs['deploy_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')

    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')

    if 'kubernetes_manifest_artifact_ids' in kwargs:
        kwargs['kubernetes_manifest_deploy_artifact_ids'] = kwargs['kubernetes_manifest_artifact_ids']
        kwargs.pop('kubernetes_manifest_artifact_ids')

    ctx.invoke(devops_cli.update_deploy_stage_update_oke_blue_green_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_stage_update_oke_blue_green_traffic_shift_deploy_stage_details, params_to_exclude=['deploy_stage_id', 'deploy_stage_predecessor_collection'])
@devops_cli.deploy_stage_group.command(name=devops_cli.update_deploy_stage_update_oke_blue_green_traffic_shift_deploy_stage_details.name, help=devops_cli.update_deploy_stage_update_oke_blue_green_traffic_shift_deploy_stage_details.help)
@cli_util.option('--stage-id', required=True, help=u"""Unique stage identifier. [required]""")
@cli_util.option('--stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_oke_blue_green_traffic_shift_deploy_stage_details_extended(ctx, **kwargs):
    if 'stage_id' in kwargs:
        kwargs['deploy_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')

    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')

    ctx.invoke(devops_cli.update_deploy_stage_update_oke_blue_green_traffic_shift_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_stage_update_oke_canary_approval_deploy_stage_details, params_to_exclude=['deploy_stage_id', 'deploy_stage_predecessor_collection'])
@devops_cli.deploy_stage_group.command(name=devops_cli.update_deploy_stage_update_oke_canary_approval_deploy_stage_details.name, help=devops_cli.update_deploy_stage_update_oke_canary_approval_deploy_stage_details.help)
@cli_util.option('--stage-id', required=True, help=u"""Unique stage identifier. [required]""")
@cli_util.option('--stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'approval-policy': {'module': 'devops', 'class': 'ApprovalPolicy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_oke_canary_approval_deploy_stage_details_extended(ctx, **kwargs):
    if 'stage_id' in kwargs:
        kwargs['deploy_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')

    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')

    ctx.invoke(devops_cli.update_deploy_stage_update_oke_canary_approval_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_stage_update_oke_canary_deploy_stage_details, params_to_exclude=['deploy_stage_id', 'deploy_stage_predecessor_collection', 'kubernetes_manifest_deploy_artifact_ids'])
@devops_cli.deploy_stage_group.command(name=devops_cli.update_deploy_stage_update_oke_canary_deploy_stage_details.name, help=devops_cli.update_deploy_stage_update_oke_canary_deploy_stage_details.help)
@cli_util.option('--stage-id', required=True, help=u"""Unique stage identifier. [required]""")
@cli_util.option('--stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--kubernetes-manifest-artifact-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Kubernetes manifest artifact OCIDs.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'kubernetes-manifest-artifact-ids': {'module': 'devops', 'class': 'list[string]'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_oke_canary_deploy_stage_details_extended(ctx, **kwargs):
    if 'stage_id' in kwargs:
        kwargs['deploy_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')

    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')

    if 'kubernetes_manifest_artifact_ids' in kwargs:
        kwargs['kubernetes_manifest_deploy_artifact_ids'] = kwargs['kubernetes_manifest_artifact_ids']
        kwargs.pop('kubernetes_manifest_artifact_ids')

    ctx.invoke(devops_cli.update_deploy_stage_update_oke_canary_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_stage_update_oke_canary_traffic_shift_deploy_stage_details, params_to_exclude=['deploy_stage_id', 'deploy_stage_predecessor_collection'])
@devops_cli.deploy_stage_group.command(name=devops_cli.update_deploy_stage_update_oke_canary_traffic_shift_deploy_stage_details.name, help=devops_cli.update_deploy_stage_update_oke_canary_traffic_shift_deploy_stage_details.help)
@cli_util.option('--stage-id', required=True, help=u"""Unique stage identifier. [required]""")
@cli_util.option('--stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'rollout-policy': {'module': 'devops', 'class': 'LoadBalancerTrafficShiftRolloutPolicy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_oke_canary_traffic_shift_deploy_stage_details_extended(ctx, **kwargs):
    if 'stage_id' in kwargs:
        kwargs['deploy_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')

    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')

    ctx.invoke(devops_cli.update_deploy_stage_update_oke_canary_traffic_shift_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_deployment_create_single_deploy_stage_redeployment_details, params_to_exclude=['deploy_pipeline_id', 'deploy_stage_id'])
@devops_cli.deployment_group.command(name=devops_cli.create_deployment_create_single_deploy_stage_redeployment_details.name, help=devops_cli.create_deployment_create_single_deploy_stage_redeployment_details.help)
@cli_util.option('--pipeline-id', required=True, help=u"""The OCID of a pipeline. [required]""")
@cli_util.option('--stage-id', required=True, help=u"""Specifies the OCID of the stage to be redeployed.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Deployment'})
@cli_util.wrap_exceptions
def create_deployment_create_single_deploy_stage_redeployment_details_extended(ctx, **kwargs):
    if 'pipeline_id' in kwargs:
        kwargs['deploy_pipeline_id'] = kwargs['pipeline_id']
        kwargs.pop('pipeline_id')

    if 'stage_id' in kwargs:
        kwargs['deploy_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')

    ctx.invoke(devops_cli.create_deployment_create_single_deploy_stage_redeployment_details, **kwargs)


# oci devops connection create-connection-create-bitbucket-cloud-app-password-connection-details -> oci devops connection create-bitbucket-cloud-connection
cli_util.rename_command(devops_cli, devops_cli.connection_group, devops_cli.create_connection_create_bitbucket_cloud_app_password_connection_details, "create-bitbucket-cloud-connection")


# oci devops connection update-connection-update-bitbucket-cloud-app-password-connection-details -> oci devops connection update-bitbucket-cloud-connection
cli_util.rename_command(devops_cli, devops_cli.connection_group, devops_cli.update_connection_update_bitbucket_cloud_app_password_connection_details, "update-bitbucket-cloud-connection")


# oci devops trigger create-trigger-create-bitbucket-cloud-trigger-details -> oci devops trigger create-bitbucket-cloud-trigger
cli_util.rename_command(devops_cli, devops_cli.trigger_group, devops_cli.create_trigger_create_bitbucket_cloud_trigger_details, "create-bitbucket-cloud-trigger")


# oci devops trigger update-trigger-update-bitbucket-cloud-trigger-details -> oci devops trigger update-bitbucket-cloud-trigger
cli_util.rename_command(devops_cli, devops_cli.trigger_group, devops_cli.update_trigger_update_bitbucket_cloud_trigger_details, "update-bitbucket-cloud-trigger")


@cli_util.copy_params_from_generated_command(devops_cli.create_connection_create_bitbucket_cloud_app_password_connection_details, params_to_exclude=['username'])
@devops_cli.connection_group.command(name=devops_cli.create_connection_create_bitbucket_cloud_app_password_connection_details.name, help=devops_cli.create_connection_create_bitbucket_cloud_app_password_connection_details.help)
@cli_util.option('--bitbucket-cloud-username', required=True, help=u"""Public Bitbucket Cloud Username in plain text(not more than 30 characters) [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection_create_bitbucket_cloud_app_password_connection_details_extended(ctx, **kwargs):
    if 'bitbucket_cloud_username' in kwargs:
        kwargs['username'] = kwargs['bitbucket_cloud_username']
        kwargs.pop('bitbucket_cloud_username')

    ctx.invoke(devops_cli.create_connection_create_bitbucket_cloud_app_password_connection_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_connection_update_bitbucket_cloud_app_password_connection_details, params_to_exclude=['username'])
@devops_cli.connection_group.command(name=devops_cli.update_connection_update_bitbucket_cloud_app_password_connection_details.name, help=devops_cli.update_connection_update_bitbucket_cloud_app_password_connection_details.help)
@cli_util.option('--bitbucket-cloud-username', help=u"""Public Bitbucket Cloud Username in plain text(not more than 30 characters)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Connection'})
@cli_util.wrap_exceptions
def update_connection_update_bitbucket_cloud_app_password_connection_details_extended(ctx, **kwargs):
    if 'bitbucket_cloud_username' in kwargs:
        kwargs['username'] = kwargs['bitbucket_cloud_username']
        kwargs.pop('bitbucket_cloud_username')

    ctx.invoke(devops_cli.update_connection_update_bitbucket_cloud_app_password_connection_details, **kwargs)


# oci devops connection create-connection-create-bitbucket-server-access-token-connection-details -> oci devops connection create-bitbucket-server-connection
cli_util.rename_command(devops_cli, devops_cli.connection_group, devops_cli.create_connection_create_bitbucket_server_access_token_connection_details, "create-bitbucket-server-connection")


# oci devops connection create-connection-create-gitlab-server-access-token-connection-details -> oci devops connection create-gitlab-server-connection
cli_util.rename_command(devops_cli, devops_cli.connection_group, devops_cli.create_connection_create_gitlab_server_access_token_connection_details, "create-gitlab-server-connection")


# oci devops connection update-connection-update-bitbucket-server-access-token-connection-details -> oci devops connection update-bitbucket-server-connection
cli_util.rename_command(devops_cli, devops_cli.connection_group, devops_cli.update_connection_update_bitbucket_server_access_token_connection_details, "update-bitbucket-server-connection")


# oci devops connection update-connection-update-gitlab-server-access-token-connection-details -> oci devops connection update-gitlab-server-connection
cli_util.rename_command(devops_cli, devops_cli.connection_group, devops_cli.update_connection_update_gitlab_server_access_token_connection_details, "update-gitlab-server-connection")


# oci devops trigger create-trigger-create-bitbucket-server-trigger-details -> oci devops trigger create-bitbucket-server-trigger
cli_util.rename_command(devops_cli, devops_cli.trigger_group, devops_cli.create_trigger_create_bitbucket_server_trigger_details, "create-bitbucket-server-trigger")


# oci devops trigger create-trigger-create-gitlab-server-trigger-details -> oci devops trigger create-gitlab-server-trigger
cli_util.rename_command(devops_cli, devops_cli.trigger_group, devops_cli.create_trigger_create_gitlab_server_trigger_details, "create-gitlab-server-trigger")


# oci devops trigger update-trigger-update-bitbucket-server-trigger-details -> oci devops trigger update-bitbucket-server-trigger
cli_util.rename_command(devops_cli, devops_cli.trigger_group, devops_cli.update_trigger_update_bitbucket_server_trigger_details, "update-bitbucket-server-trigger")


# oci devops trigger update-trigger-update-gitlab-server-trigger-details -> oci devops trigger update-gitlab-server-trigger
cli_util.rename_command(devops_cli, devops_cli.trigger_group, devops_cli.update_trigger_update_gitlab_server_trigger_details, "update-gitlab-server-trigger")


@cli_util.copy_params_from_generated_command(devops_cli.create_connection_create_bitbucket_server_access_token_connection_details, params_to_exclude=['access_token'])
@devops_cli.connection_group.command(name=devops_cli.create_connection_create_bitbucket_server_access_token_connection_details.name, help=devops_cli.create_connection_create_bitbucket_server_access_token_connection_details.help)
@cli_util.option('--personal-access-token', required=True, help=u"""The OCID of personal access token saved in secret store. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'tls-verify-config': {'module': 'devops', 'class': 'TlsVerifyConfig'}}, output_type={'module': 'devops', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection_create_bitbucket_server_access_token_connection_details_extended(ctx, **kwargs):

    if 'personal_access_token' in kwargs:
        kwargs['access_token'] = kwargs['personal_access_token']
        kwargs.pop('personal_access_token')

    ctx.invoke(devops_cli.create_connection_create_bitbucket_server_access_token_connection_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_connection_create_gitlab_server_access_token_connection_details, params_to_exclude=['access_token'])
@devops_cli.connection_group.command(name=devops_cli.create_connection_create_gitlab_server_access_token_connection_details.name, help=devops_cli.create_connection_create_gitlab_server_access_token_connection_details.help)
@cli_util.option('--personal-access-token', required=True, help=u"""The OCID of personal access token saved in secret store. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'tls-verify-config': {'module': 'devops', 'class': 'TlsVerifyConfig'}}, output_type={'module': 'devops', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection_create_gitlab_server_access_token_connection_details_extended(ctx, **kwargs):

    if 'personal_access_token' in kwargs:
        kwargs['access_token'] = kwargs['personal_access_token']
        kwargs.pop('personal_access_token')

    ctx.invoke(devops_cli.create_connection_create_gitlab_server_access_token_connection_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_connection_update_bitbucket_server_access_token_connection_details, params_to_exclude=['access_token'])
@devops_cli.connection_group.command(name=devops_cli.update_connection_update_bitbucket_server_access_token_connection_details.name, help=devops_cli.update_connection_update_bitbucket_server_access_token_connection_details.help)
@cli_util.option('--personal-access-token', help=u"""OCID of personal access token saved in secret store""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'tls-verify-config': {'module': 'devops', 'class': 'TlsVerifyConfig'}}, output_type={'module': 'devops', 'class': 'Connection'})
@cli_util.wrap_exceptions
def update_connection_update_bitbucket_server_access_token_connection_details_extended(ctx, **kwargs):

    if 'personal_access_token' in kwargs:
        kwargs['access_token'] = kwargs['personal_access_token']
        kwargs.pop('personal_access_token')

    ctx.invoke(devops_cli.update_connection_update_bitbucket_server_access_token_connection_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_connection_update_gitlab_server_access_token_connection_details, params_to_exclude=['access_token'])
@devops_cli.connection_group.command(name=devops_cli.update_connection_update_gitlab_server_access_token_connection_details.name, help=devops_cli.update_connection_update_gitlab_server_access_token_connection_details.help)
@cli_util.option('--personal-access-token', help=u"""The OCID of personal access token saved in secret store.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'tls-verify-config': {'module': 'devops', 'class': 'TlsVerifyConfig'}}, output_type={'module': 'devops', 'class': 'Connection'})
@cli_util.wrap_exceptions
def update_connection_update_gitlab_server_access_token_connection_details_extended(ctx, **kwargs):

    if 'personal_access_token' in kwargs:
        kwargs['access_token'] = kwargs['personal_access_token']
        kwargs.pop('personal_access_token')

    ctx.invoke(devops_cli.update_connection_update_gitlab_server_access_token_connection_details, **kwargs)


# oci devops code-search-result-collection -> oci devops code-search
# cli_util.rename_command(devops_cli, devops_cli.devops_root_group, devops_cli.code_search_result_collection_group, "code-search")


# oci devops code-search-result-collection list-code-search-results -> oci devops code-search-result-collection list-results
# cli_util.rename_command(devops_cli, devops_cli.code_search_result_collection_group, devops_cli.list_code_search_results, "list-results")


# @cli_util.copy_params_from_generated_command(devops_cli.list_code_search_results, params_to_exclude=['query_parameterconflict'])
# @devops_cli.code_search_result_collection_group.command(name=devops_cli.list_code_search_results.name, help=devops_cli.list_code_search_results.help)
# @cli_util.option('--search-query', required=True, help=u"""Search query provided by the user as per the search query syntax.   Example:     Workflow AdminServiceApiConfiguration retryConfig  -  Search for files with occurrence of all of these keywords.     hello AND world  -  Search for files that has both 'hello' and 'world'.     hello OR world  -  Search for  files that has 'hello' or 'world' or both.     hello NOT world  -  Search for files that has 'hello' but not 'world'.     "hello world"  -  Search for files that has words 'hello' and 'world' in same order.     project:project1 repo:repo1 wfaas  -  Search in repository 'repo1' in project 'project1' for keyword 'wfaas'.     hello path:readme.md  -  Search for files that contain word 'hello' and the file path matches 'readme.md'.     hello ext:c  -  Search for files that has 'hello' within files with the '.c' extension. [required]""")
# @click.pass_context
# @json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'CodeSearchResultCollection'})
# @cli_util.wrap_exceptions
# def list_code_search_results_extended(ctx, **kwargs):
#
#     if 'search_query' in kwargs:
#         kwargs['query_parameterconflict'] = kwargs['search_query']
#         kwargs.pop('search_query')
#
#     ctx.invoke(devops_cli.list_code_search_results, **kwargs)


# oci devops deploy-artifact create-deploy-artifact-helm-command-spec-artifact-source -> oci devops deploy-artifact create-helm-command-spec-source
cli_util.rename_command(devops_cli, devops_cli.deploy_artifact_group, devops_cli.create_deploy_artifact_helm_command_spec_artifact_source, "create-helm-command-spec")


# oci devops deploy-artifact update-deploy-artifact-helm-command-spec-artifact-source -> oci devops deploy-artifact update-helm-command-spec-source
cli_util.rename_command(devops_cli, devops_cli.deploy_artifact_group, devops_cli.update_deploy_artifact_helm_command_spec_artifact_source, "update-helm-command-spec")


@cli_util.copy_params_from_generated_command(devops_cli.create_deploy_artifact_helm_command_spec_artifact_source, params_to_exclude=['deploy_artifact_source_base64_encoded_content', 'deploy_artifact_source_helm_artifact_source_type'])
@devops_cli.deploy_artifact_group.command(name=devops_cli.create_deploy_artifact_helm_command_spec_artifact_source.name, help=devops_cli.create_deploy_artifact_helm_command_spec_artifact_source.help)
@cli_util.option('--base64-encoded-content', required=True, help=u"""The Helm commands to be executed, base 64 encoded""")
@cli_util.option('--helm-artifact-source', required=True, type=custom_types.CliCaseInsensitiveChoice(["INLINE"]), help=u"""Type of source for the helm artifact""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployArtifact'})
@cli_util.wrap_exceptions
def create_deploy_artifact_helm_command_spec_artifact_source_extended(ctx, **kwargs):
    if 'base64_encoded_content' in kwargs:
        kwargs['deploy_artifact_source_base64_encoded_content'] = kwargs['base64_encoded_content']
        kwargs.pop('base64_encoded_content')
    if 'helm_artifact_source' in kwargs:
        kwargs['deploy_artifact_source_helm_artifact_source_type'] = kwargs['helm_artifact_source']
        kwargs.pop('helm_artifact_source')
    ctx.invoke(devops_cli.create_deploy_artifact_helm_command_spec_artifact_source, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_artifact_helm_command_spec_artifact_source, params_to_exclude=['deploy_artifact_source_base64_encoded_content', 'deploy_artifact_source_helm_artifact_source_type'])
@devops_cli.deploy_artifact_group.command(name=devops_cli.update_deploy_artifact_helm_command_spec_artifact_source.name, help=devops_cli.update_deploy_artifact_helm_command_spec_artifact_source.help)
@cli_util.option('--base64-encoded-content', required=True, help=u"""The Helm commands to be executed, base 64 encoded""")
@cli_util.option('--helm-artifact-source', required=True, type=custom_types.CliCaseInsensitiveChoice(["INLINE"]), help=u"""Type of source for the helm artifact""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployArtifact'})
@cli_util.wrap_exceptions
def update_deploy_artifact_helm_command_spec_artifact_source_extended(ctx, **kwargs):
    if 'base64_encoded_content' in kwargs:
        kwargs['deploy_artifact_source_base64_encoded_content'] = kwargs['base64_encoded_content']
        kwargs.pop('base64_encoded_content')
    if 'helm_artifact_source' in kwargs:
        kwargs['deploy_artifact_source_helm_artifact_source_type'] = kwargs['helm_artifact_source']
        kwargs.pop('helm_artifact_source')
    ctx.invoke(devops_cli.update_deploy_artifact_helm_command_spec_artifact_source, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_deploy_stage_create_oke_helm_chart_deploy_stage_details, params_to_exclude=['is_uninstall_on_stage_delete'])
@devops_cli.deploy_stage_group.command(name=devops_cli.create_deploy_stage_create_oke_helm_chart_deploy_stage_details.name, help=devops_cli.create_deploy_stage_create_oke_helm_chart_deploy_stage_details.help)
@cli_util.option('--uninstall-on-stage-delete', type=click.BOOL, help=u"""Uninstall the Helm chart release on deleting the stage.""")
@click.pass_context
@cli_util.wrap_exceptions
def create_deploy_stage_create_oke_helm_chart_deploy_stage_details_extended(ctx, **kwargs):

    if 'uninstall_on_stage_delete' in kwargs:
        kwargs['is_uninstall_on_stage_delete'] = kwargs['uninstall_on_stage_delete']
        kwargs.pop('uninstall_on_stage_delete')

    ctx.invoke(devops_cli.create_deploy_stage_create_oke_helm_chart_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_stage_update_oke_helm_chart_deploy_stage_details, params_to_exclude=['is_uninstall_on_stage_delete'])
@devops_cli.deploy_stage_group.command(name=devops_cli.update_deploy_stage_update_oke_helm_chart_deploy_stage_details.name, help=devops_cli.update_deploy_stage_update_oke_helm_chart_deploy_stage_details.help)
@cli_util.option('--uninstall-on-stage-delete', type=click.BOOL, help=u"""Uninstall the Helm chart release on deleting the stage.""")
@click.pass_context
@cli_util.wrap_exceptions
def update_deploy_stage_update_oke_helm_chart_deploy_stage_details_extended(ctx, **kwargs):

    if 'uninstall_on_stage_delete' in kwargs:
        kwargs['is_uninstall_on_stage_delete'] = kwargs['uninstall_on_stage_delete']
        kwargs.pop('uninstall_on_stage_delete')

    ctx.invoke(devops_cli.update_deploy_stage_update_oke_helm_chart_deploy_stage_details, **kwargs)
