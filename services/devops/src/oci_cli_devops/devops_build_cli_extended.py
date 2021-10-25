# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

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
    params_to_exclude=['build_pipeline_stage_predecessor_collection'])
@devops_cli.build_pipeline_stage_group.command(
    name=cli_util.override(
        'build_pipeline_stage.create_build_pipeline_stage_create_build_stage_details.command_name', 'create-build-stage'),
    help=devops_cli.create_build_pipeline_stage_create_build_stage_details.help)
@cli_util.option('--stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'},
        'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'},
        'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'},
        'build-source-collection': {'module': 'devops', 'class': 'BuildSourceCollection'}},
    output_type={'module': 'devops', 'class': 'BuildPipelineStage'})
@cli_util.wrap_exceptions
def create_build_pipeline_stage_create_build_stage_details_extended(ctx, **kwargs):
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
    params_to_exclude=['build_pipeline_stage_id', 'build_pipeline_stage_predecessor_collection'])
@devops_cli.build_pipeline_stage_group.command(
    name=cli_util.override(
        'build_pipeline_stage.update_build_pipeline_stage_update_build_stage_details.command_name', 'update-build-stage'),
    help=devops_cli.update_build_pipeline_stage_update_build_stage_details.help)
@cli_util.option('--stage-id', required=True, help=u"""Unique stage identifier.""")
@cli_util.option('--stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'},
        'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'},
        'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'},
        'build-source-collection': {'module': 'devops', 'class': 'BuildSourceCollection'}},
    output_type={'module': 'devops', 'class': 'BuildPipelineStage'})
@cli_util.wrap_exceptions
def update_build_pipeline_stage_update_build_stage_details_extended(ctx, **kwargs):
    if 'stage_id' in kwargs:
        kwargs['build_pipeline_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')
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
