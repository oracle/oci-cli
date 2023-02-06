# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.devops.src.oci_cli_devops.generated import devops_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci devops deploy-artifact deploy-artifact-summary list-deploy-artifacts -> oci devops deploy-artifact deploy-artifact-summary list
cli_util.rename_command(devops_cli, devops_cli.deploy_artifact_summary_group, devops_cli.list_deploy_artifacts, "list")

# oci devops deploy-artifact create-deploy-artifact-helm-repository-deploy-artifact-source -> oci devops deploy-artifact create-helm-repository-artifact
cli_util.rename_command(devops_cli, devops_cli.deploy_artifact_group, devops_cli.create_deploy_artifact_helm_repository_deploy_artifact_source, "create-helm-repository-artifact")


# oci devops deploy-artifact update-deploy-artifact-helm-repository-deploy-artifact-source -> oci devops deploy-artifact update-helm-repository-artifact
cli_util.rename_command(devops_cli, devops_cli.deploy_artifact_group, devops_cli.update_deploy_artifact_helm_repository_deploy_artifact_source, "update-helm-repository-artifact")


# oci devops deploy-stage create-deploy-stage-create-oke-helm-chart-deploy-stage-details -> oci devops deploy-stage create-oke-helm-chart-stage
cli_util.rename_command(devops_cli, devops_cli.deploy_stage_group, devops_cli.create_deploy_stage_create_oke_helm_chart_deploy_stage_details, "create-oke-helm-chart-stage")


# oci devops deploy-stage update-deploy-stage-update-oke-helm-chart-deploy-stage-details -> oci devops deploy-stage update-oke-helm-chart-stage
cli_util.rename_command(devops_cli, devops_cli.deploy_stage_group, devops_cli.update_deploy_stage_update_oke_helm_chart_deploy_stage_details, "update-oke-helm-chart-stage")


# Move commands under 'oci devops deploy-artifact deploy-artifact-summary' -> 'oci devops deploy-artifact'
devops_cli.devops_root_group.commands.pop(devops_cli.deploy_artifact_summary_group.name)
devops_cli.deploy_artifact_group.add_command(devops_cli.list_deploy_artifacts)


# Remove oci devops deploy-artifact create
devops_cli.deploy_artifact_group.commands.pop(devops_cli.create_deploy_artifact.name)

devops_cli.deploy_artifact_group.commands.pop(devops_cli.update_deploy_artifact.name)
devops_cli.deploy_artifact_group.commands.pop(devops_cli.create_deploy_artifact_generic_deploy_artifact_source.name)
devops_cli.deploy_artifact_group.commands.pop(devops_cli.create_deploy_artifact_inline_deploy_artifact_source.name)
devops_cli.deploy_artifact_group.commands.pop(devops_cli.create_deploy_artifact_ocir_deploy_artifact_source.name)
devops_cli.deploy_artifact_group.commands.pop(devops_cli.create_deploy_artifact_helm_repository_deploy_artifact_source.name)
devops_cli.deploy_artifact_group.commands.pop(devops_cli.update_deploy_artifact_generic_deploy_artifact_source.name)
devops_cli.deploy_artifact_group.commands.pop(devops_cli.update_deploy_artifact_inline_deploy_artifact_source.name)
devops_cli.deploy_artifact_group.commands.pop(devops_cli.update_deploy_artifact_ocir_deploy_artifact_source.name)
devops_cli.deploy_artifact_group.commands.pop(devops_cli.update_deploy_artifact_helm_repository_deploy_artifact_source.name)
devops_cli.deploy_artifact_group.commands.pop(devops_cli.get_deploy_artifact.name)
devops_cli.deploy_artifact_group.commands.pop(devops_cli.delete_deploy_artifact.name)
devops_cli.deploy_environment_group.commands.pop(devops_cli.update_deploy_environment.name)
devops_cli.deploy_environment_group.commands.pop(devops_cli.update_deploy_environment_update_compute_instance_group_deploy_environment_details.name)
devops_cli.deploy_environment_group.commands.pop(devops_cli.delete_deploy_environment.name)
devops_cli.deploy_environment_group.commands.pop(devops_cli.get_deploy_environment.name)
devops_cli.deploy_environment_group.commands.pop(devops_cli.update_deploy_environment_update_function_deploy_environment_details.name)
devops_cli.deploy_environment_group.commands.pop(devops_cli.update_deploy_environment_update_oke_cluster_deploy_environment_details.name)
devops_cli.deploy_pipeline_group.commands.pop(devops_cli.create_deploy_pipeline.name)
devops_cli.deploy_pipeline_group.commands.pop(devops_cli.delete_deploy_pipeline.name)
devops_cli.deploy_pipeline_group.commands.pop(devops_cli.get_deploy_pipeline.name)
devops_cli.deploy_pipeline_group.commands.pop(devops_cli.update_deploy_pipeline.name)
devops_cli.deploy_stage_group.commands.pop(devops_cli.update_deploy_stage.name)
devops_cli.deploy_stage_group.commands.pop(devops_cli.create_deploy_stage_create_compute_instance_group_deploy_stage_details.name)
devops_cli.deploy_stage_group.commands.pop(devops_cli.delete_deploy_stage.name)
devops_cli.deploy_stage_group.commands.pop(devops_cli.create_deploy_stage_create_oke_deploy_stage_details.name)
devops_cli.deploy_stage_group.commands.pop(devops_cli.create_deploy_stage_create_oke_helm_chart_deploy_stage_details.name)
devops_cli.deploy_stage_group.commands.pop(devops_cli.create_deploy_stage_create_function_deploy_stage_details.name)
devops_cli.deploy_stage_group.commands.pop(devops_cli.create_deploy_stage_create_invoke_function_deploy_stage_details.name)
devops_cli.deploy_stage_group.commands.pop(devops_cli.create_deploy_stage_create_load_balancer_traffic_shift_deploy_stage_details.name)
devops_cli.deploy_stage_group.commands.pop(devops_cli.create_deploy_stage_create_manual_approval_deploy_stage_details.name)
devops_cli.deploy_stage_group.commands.pop(devops_cli.create_deploy_stage_create_wait_deploy_stage_details.name)
devops_cli.deploy_stage_group.commands.pop(devops_cli.get_deploy_stage.name)
devops_cli.deploy_stage_group.commands.pop(devops_cli.update_deploy_stage_update_compute_instance_group_deploy_stage_details.name)
devops_cli.deploy_stage_group.commands.pop(devops_cli.update_deploy_stage_update_function_deploy_stage_details.name)
devops_cli.deploy_stage_group.commands.pop(devops_cli.update_deploy_stage_update_invoke_function_deploy_stage_details.name)
devops_cli.deploy_stage_group.commands.pop(devops_cli.update_deploy_stage_update_load_balancer_traffic_shift_deploy_stage_details.name)
devops_cli.deploy_stage_group.commands.pop(devops_cli.update_deploy_stage_update_manual_approval_deploy_stage_details.name)
devops_cli.deploy_stage_group.commands.pop(devops_cli.update_deploy_stage_update_oke_deploy_stage_details.name)
devops_cli.deploy_stage_group.commands.pop(devops_cli.update_deploy_stage_update_oke_helm_chart_deploy_stage_details.name)
devops_cli.deploy_stage_group.commands.pop(devops_cli.update_deploy_stage_update_wait_deploy_stage_details.name)
devops_cli.deployment_group.commands.pop(devops_cli.create_deployment_create_deploy_pipeline_deployment_details.name)
devops_cli.deployment_group.commands.pop(devops_cli.approve_deployment.name)
devops_cli.deployment_group.commands.pop(devops_cli.create_deployment_create_deploy_pipeline_redeployment_details.name)
devops_cli.deployment_group.commands.pop(devops_cli.create_deployment_create_single_deploy_stage_deployment_details.name)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_artifact, params_to_exclude=['deploy_artifact_id', 'deploy_artifact_type', 'deploy_artifact_source'])
@devops_cli.deploy_artifact_group.command(name=cli_util.override('deploy_artifact.update_deploy_artifact.command_name', 'update'), help=devops_cli.update_deploy_artifact.help)
@cli_util.option('--artifact-id', required=True, help=u"""unique Artifact identifier""")
@cli_util.option('--artifact-type', type=custom_types.CliCaseInsensitiveChoice(["COMMAND_SPEC", "DEPLOYMENT_SPEC", "JOB_SPEC", "KUBERNETES_MANIFEST", "GENERIC_FILE", "DOCKER_IMAGE"]), help=u"""Type of the DeployArtifact""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'artifact-parameters': {'module': 'devops', 'class': 'DeployArtifactParameterCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployArtifact'})
@cli_util.wrap_exceptions
def update_deploy_artifact_extended(ctx, **kwargs):
    if 'artifact_id' in kwargs:
        kwargs['deploy_artifact_id'] = kwargs['artifact_id']
        kwargs.pop('artifact_id')
    if 'artifact_type' in kwargs:
        kwargs['deploy_artifact_type'] = kwargs['artifact_type']
        kwargs.pop('artifact_type')
    ctx.invoke(devops_cli.update_deploy_artifact, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_deploy_artifact_generic_deploy_artifact_source, params_to_exclude=['deploy_artifact_source_repository_id', 'deploy_artifact_source_deploy_artifact_path', 'deploy_artifact_source_deploy_artifact_version', 'deploy_artifact_type'])
@devops_cli.deploy_artifact_group.command(name=cli_util.override('deploy_artifact.create_deploy_artifact_generic_deploy_artifact_source.command_name', 'create-generic-artifact'), help=devops_cli.create_deploy_artifact_generic_deploy_artifact_source.help)
@cli_util.option('--repository-id', required=True, help=u"""Specifies the repository id""")
@cli_util.option('--artifact-path', required=True, help=u"""Specifies the artifact path in the repository""")
@cli_util.option('--artifact-version', required=True, help=u"""Users should be able to set this as a pipeline parameter for example ${appVersion}""")
@cli_util.option('--artifact-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["COMMAND_SPEC", "DEPLOYMENT_SPEC", "JOB_SPEC", "KUBERNETES_MANIFEST", "GENERIC_FILE", "DOCKER_IMAGE"]), help=u"""Type of the DeployArtifact""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'artifact-parameters': {'module': 'devops', 'class': 'DeployArtifactParameterCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployArtifact'})
@cli_util.wrap_exceptions
def create_deploy_artifact_generic_deploy_artifact_source_extended(ctx, **kwargs):
    if 'repository_id' in kwargs:
        kwargs['deploy_artifact_source_repository_id'] = kwargs['repository_id']
        kwargs.pop('repository_id')
    if 'artifact_path' in kwargs:
        kwargs['deploy_artifact_source_deploy_artifact_path'] = kwargs['artifact_path']
        kwargs.pop('artifact_path')
    if 'artifact_version' in kwargs:
        kwargs['deploy_artifact_source_deploy_artifact_version'] = kwargs['artifact_version']
        kwargs.pop('artifact_version')
    if 'artifact_type' in kwargs:
        kwargs['deploy_artifact_type'] = kwargs['artifact_type']
        kwargs.pop('artifact_type')
    ctx.invoke(devops_cli.create_deploy_artifact_generic_deploy_artifact_source, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_deploy_artifact_inline_deploy_artifact_source, params_to_exclude=['deploy_artifact_source_base64_encoded_content', 'deploy_artifact_type'])
@devops_cli.deploy_artifact_group.command(name=cli_util.override('deploy_artifact.create_deploy_artifact_inline_deploy_artifact_source.command_name', 'create-inline-artifact'), help=devops_cli.create_deploy_artifact_inline_deploy_artifact_source.help)
@cli_util.option('--artifact-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["COMMAND_SPEC", "DEPLOYMENT_SPEC", "JOB_SPEC", "KUBERNETES_MANIFEST", "GENERIC_FILE", "DOCKER_IMAGE"]), help=u"""Type of the DeployArtifact""")
@cli_util.option('--base64-encoded-content', required=True, help=u"""base64 Encoded String""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'artifact-parameters': {'module': 'devops', 'class': 'DeployArtifactParameterCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployArtifact'})
@cli_util.wrap_exceptions
def create_deploy_artifact_inline_deploy_artifact_source_extended(ctx, **kwargs):
    if 'artifact_type' in kwargs:
        kwargs['deploy_artifact_type'] = kwargs['artifact_type']
        kwargs.pop('artifact_type')
    if 'base64_encoded_content' in kwargs:
        kwargs['deploy_artifact_source_base64_encoded_content'] = kwargs['base64_encoded_content']
        kwargs.pop('base64_encoded_content')
    ctx.invoke(devops_cli.create_deploy_artifact_inline_deploy_artifact_source, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_deploy_artifact_ocir_deploy_artifact_source, params_to_exclude=['deploy_artifact_source_image_uri', 'deploy_artifact_source_image_digest', 'deploy_artifact_type'])
@devops_cli.deploy_artifact_group.command(name=cli_util.override('deploy_artifact.create_deploy_artifact_ocir_deploy_artifact_source.command_name', 'create-ocir-artifact'), help=devops_cli.create_deploy_artifact_ocir_deploy_artifact_source.help)
@cli_util.option('--source-image-uri', required=True, help=u"""base64 Encoded String""")
@cli_util.option('--image-digest', help=u"""Specifies image digest for the version of the image""")
@cli_util.option('--artifact-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["DEPLOYMENT_SPEC", "JOB_SPEC", "KUBERNETES_MANIFEST", "GENERIC_FILE", "DOCKER_IMAGE"]), help=u"""Type of the DeployArtifact""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'artifact-parameters': {'module': 'devops', 'class': 'DeployArtifactParameterCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployArtifact'})
@cli_util.wrap_exceptions
def create_deploy_artifact_ocir_deploy_artifact_source_extended(ctx, **kwargs):
    if 'source_image_uri' in kwargs:
        kwargs['deploy_artifact_source_image_uri'] = kwargs['source_image_uri']
        kwargs.pop('source_image_uri')
    if 'image_digest' in kwargs:
        kwargs['deploy_artifact_source_image_digest'] = kwargs['image_digest']
        kwargs.pop('image_digest')
    if 'artifact_type' in kwargs:
        kwargs['deploy_artifact_type'] = kwargs['artifact_type']
        kwargs.pop('artifact_type')
    ctx.invoke(devops_cli.create_deploy_artifact_ocir_deploy_artifact_source, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_deploy_artifact_helm_repository_deploy_artifact_source, params_to_exclude=['deploy_artifact_source_chart_url', 'deploy_artifact_source_deploy_artifact_version', 'deploy_artifact_type', 'deploy_artifact_source_helm_verification_key_source'])
@devops_cli.deploy_artifact_group.command(name=cli_util.override('devops_cli.create_deploy_artifact_helm_repository_deploy_artifact_source.name', 'create-helm-repository-artifact'), help=devops_cli.create_deploy_artifact_helm_repository_deploy_artifact_source.help)
@cli_util.option('--artifact-type', required=True, help="""Type of the deployment artifact. [required]""")
@cli_util.option('--artifact-version', required=True, help="""Users can set this as a placeholder value that refers to a pipeline parameter, for example, ${appVersion}. [required]""")
@cli_util.option('--artifact-chart-url', required=True, help=u"""The URL of an OCIR repository. [required]""")
@cli_util.option('--helm-verification-key-source', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'helm-verification-key-source': {'module': 'devops', 'class': 'VerificationKeySource'}}, output_type={'module': 'devops', 'class': 'DeployArtifact'})
@cli_util.wrap_exceptions
def create_deploy_artifact_helm_repository_deploy_artifact_source_extended(ctx, **kwargs):
    if 'artifact_type' in kwargs:
        kwargs['deploy_artifact_type'] = kwargs['artifact_type']
        kwargs.pop('artifact_type')
    if 'artifact_version' in kwargs:
        kwargs['deploy_artifact_source_deploy_artifact_version'] = kwargs['artifact_version']
        kwargs.pop('artifact_version')
    if 'artifact_chart_url' in kwargs:
        kwargs['deploy_artifact_source_chart_url'] = kwargs['artifact_chart_url']
        kwargs.pop('artifact_chart_url')
    if 'helm_verification_key_source' in kwargs:
        kwargs['deploy_artifact_source_helm_verification_key_source'] = kwargs['helm_verification_key_source']
        kwargs.pop('helm_verification_key_source')
    ctx.invoke(devops_cli.create_deploy_artifact_helm_repository_deploy_artifact_source, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_artifact_generic_deploy_artifact_source, params_to_exclude=['deploy_artifact_source_repository_id', 'deploy_artifact_source_deploy_artifact_path', 'deploy_artifact_source_deploy_artifact_version', 'deploy_artifact_id', 'deploy_artifact_type'])
@devops_cli.deploy_artifact_group.command(name=cli_util.override('deploy_artifact.update_deploy_artifact_generic_deploy_artifact_source.command_name', 'update-generic-artifact'), help=devops_cli.update_deploy_artifact_generic_deploy_artifact_source.help)
@cli_util.option('--artifact-id', required=True, help=u"""unique Artifact identifier""")
@cli_util.option('--repository-id', help=u"""Specifies the repository id""")
@cli_util.option('--artifact-path', help=u"""Specifies the artifact path in the repository""")
@cli_util.option('--artifact-version', help=u"""Users should be able to set this as a pipeline parameter for example ${appVersion}""")
@cli_util.option('--artifact-type', type=custom_types.CliCaseInsensitiveChoice(["COMMAND_SPEC", "DEPLOYMENT_SPEC", "JOB_SPEC", "KUBERNETES_MANIFEST", "GENERIC_FILE", "DOCKER_IMAGE"]), help=u"""Type of the DeployArtifact""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'artifact-parameters': {'module': 'devops', 'class': 'DeployArtifactParameterCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployArtifact'})
@cli_util.wrap_exceptions
def update_deploy_artifact_generic_deploy_artifact_source_extended(ctx, **kwargs):
    if 'artifact_id' in kwargs:
        kwargs['deploy_artifact_id'] = kwargs['artifact_id']
        kwargs.pop('artifact_id')
    if 'repository_id' in kwargs:
        kwargs['deploy_artifact_source_repository_id'] = kwargs['repository_id']
        kwargs.pop('repository_id')
    if 'artifact_path' in kwargs:
        kwargs['deploy_artifact_source_deploy_artifact_path'] = kwargs['artifact_path']
        kwargs.pop('artifact_path')
    if 'artifact_version' in kwargs:
        kwargs['deploy_artifact_source_deploy_artifact_version'] = kwargs['artifact_version']
        kwargs.pop('artifact_version')
    if 'artifact_type' in kwargs:
        kwargs['deploy_artifact_type'] = kwargs['artifact_type']
        kwargs.pop('artifact_type')
    ctx.invoke(devops_cli.update_deploy_artifact_generic_deploy_artifact_source, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_artifact_inline_deploy_artifact_source, params_to_exclude=['deploy_artifact_source_base64_encoded_content', 'deploy_artifact_id', 'deploy_artifact_type'])
@devops_cli.deploy_artifact_group.command(name=cli_util.override('deploy_artifact.update_deploy_artifact_inline_deploy_artifact_source.command_name', 'update-inline-artifact'), help=devops_cli.update_deploy_artifact_inline_deploy_artifact_source.help)
@cli_util.option('--artifact-id', required=True, help=u"""unique Artifact identifier""")
@cli_util.option('--base64-encoded-content', help=u"""base64 Encoded String""")
@cli_util.option('--artifact-type', type=custom_types.CliCaseInsensitiveChoice(["COMMAND_SPEC", "DEPLOYMENT_SPEC", "JOB_SPEC", "KUBERNETES_MANIFEST", "GENERIC_FILE", "DOCKER_IMAGE"]), help=u"""Type of the DeployArtifact""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'artifact-parameters': {'module': 'devops', 'class': 'DeployArtifactParameterCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployArtifact'})
@cli_util.wrap_exceptions
def update_deploy_artifact_inline_deploy_artifact_source_extended(ctx, **kwargs):
    if 'artifact_id' in kwargs:
        kwargs['deploy_artifact_id'] = kwargs['artifact_id']
        kwargs.pop('artifact_id')
    if 'base64_encoded_content' in kwargs:
        kwargs['deploy_artifact_source_base64_encoded_content'] = kwargs['base64_encoded_content']
        kwargs.pop('base64_encoded_content')
    if 'artifact_type' in kwargs:
        kwargs['deploy_artifact_type'] = kwargs['artifact_type']
        kwargs.pop('artifact_type')
    ctx.invoke(devops_cli.update_deploy_artifact_inline_deploy_artifact_source, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_artifact_ocir_deploy_artifact_source, params_to_exclude=['deploy_artifact_source_image_uri', 'deploy_artifact_source_image_digest', 'deploy_artifact_id', 'deploy_artifact_type'])
@devops_cli.deploy_artifact_group.command(name=cli_util.override('deploy_artifact.update_deploy_artifact_ocir_deploy_artifact_source.command_name', 'update-ocir-artifact'), help=devops_cli.update_deploy_artifact_ocir_deploy_artifact_source.help)
@cli_util.option('--artifact-id', required=True, help=u"""unique Artifact identifier""")
@cli_util.option('--source-image-uri', help=u"""base64 Encoded String""")
@cli_util.option('--image-digest', help=u"""Specifies image digest for the version of the image""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'artifact-parameters': {'module': 'devops', 'class': 'DeployArtifactParameterCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployArtifact'})
@cli_util.wrap_exceptions
def update_deploy_artifact_ocir_deploy_artifact_source_extended(ctx, **kwargs):
    if 'artifact_id' in kwargs:
        kwargs['deploy_artifact_id'] = kwargs['artifact_id']
        kwargs.pop('artifact_id')
    if 'source_image_uri' in kwargs:
        kwargs['deploy_artifact_source_image_uri'] = kwargs['source_image_uri']
        kwargs.pop('source_image_uri')
    if 'image_digest' in kwargs:
        kwargs['deploy_artifact_source_image_digest'] = kwargs['image_digest']
        kwargs.pop('image_digest')
    ctx.invoke(devops_cli.update_deploy_artifact_ocir_deploy_artifact_source, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_artifact_helm_repository_deploy_artifact_source, params_to_exclude=['deploy_artifact_id', 'deploy_artifact_source_chart_url', 'deploy_artifact_source_deploy_artifact_version', 'deploy_artifact_source_helm_verification_key_source'])
@devops_cli.deploy_artifact_group.command(name=cli_util.override('deploy_artifact.update_deploy_artifact_helm_repository_deploy_artifact_source.command_name', 'update-helm-repository-artifact'), help=devops_cli.update_deploy_artifact_helm_repository_deploy_artifact_source.help)
@cli_util.option('--artifact-version', required=True, help="""Users can set this as a placeholder value that refers to a pipeline parameter, for example, ${appVersion}. [required]""")
@cli_util.option('--artifact-chart-url', required=True, help="""The URL of an OCIR repository. [required]""")
@cli_util.option('--artifact-id', required=True, help=u"""Unique artifact identifier. [required]""")
@cli_util.option('--helm-verification-key-source', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'helm-verification-key-source': {'module': 'devops', 'class': 'VerificationKeySource'}}, output_type={'module': 'devops', 'class': 'DeployArtifact'})
@cli_util.wrap_exceptions
def update_deploy_artifact_helm_repository_deploy_artifact_source_extended(ctx, **kwargs):
    if 'artifact_version' in kwargs:
        kwargs['deploy_artifact_source_deploy_artifact_version'] = kwargs['artifact_version']
        kwargs.pop('artifact_version')
    if 'artifact_chart_url' in kwargs:
        kwargs['deploy_artifact_source_chart_url'] = kwargs['artifact_chart_url']
        kwargs.pop('artifact_chart_url')
    if 'artifact_id' in kwargs:
        kwargs['deploy_artifact_id'] = kwargs['artifact_id']
        kwargs.pop('artifact_id')
    if 'helm_verification_key_source' in kwargs:
        kwargs['deploy_artifact_source_helm_verification_key_source'] = kwargs['helm_verification_key_source']
        kwargs.pop('helm_verification_key_source')
    ctx.invoke(devops_cli.update_deploy_artifact_helm_repository_deploy_artifact_source, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.get_deploy_artifact, params_to_exclude=['deploy_artifact_id'])
@devops_cli.deploy_artifact_group.command(name=cli_util.override('deploy_artifact.get_deploy_artifact.command_name', 'get'), help=devops_cli.get_deploy_artifact.help)
@cli_util.option('--artifact-id', required=True, help=u"""unique Artifact identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'DeployArtifact'})
@cli_util.wrap_exceptions
def get_deploy_artifact_extended(ctx, **kwargs):
    if 'artifact_id' in kwargs:
        kwargs['deploy_artifact_id'] = kwargs['artifact_id']
        kwargs.pop('artifact_id')
    ctx.invoke(devops_cli.get_deploy_artifact, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.delete_deploy_artifact, params_to_exclude=['deploy_artifact_id'])
@devops_cli.deploy_artifact_group.command(name=cli_util.override('deploy_artifact.delete_deploy_artifact.command_name', 'delete'), help=devops_cli.delete_deploy_artifact.help)
@cli_util.option('--artifact-id', required=True, help=u"""unique Artifact identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_deploy_artifact_extended(ctx, **kwargs):
    if 'artifact_id' in kwargs:
        kwargs['deploy_artifact_id'] = kwargs['artifact_id']
        kwargs.pop('artifact_id')
    ctx.invoke(devops_cli.delete_deploy_artifact, **kwargs)


# oci devops deploy-environment deploy-environment create-deploy-environment-create-compute-instance-group-deploy-environment-details -> oci devops deploy-environment deploy-environment create-compute-instance-environment
cli_util.rename_command(devops_cli, devops_cli.deploy_environment_group, devops_cli.create_deploy_environment_create_compute_instance_group_deploy_environment_details, "create-compute-instance-environment")


# oci devops deploy-environment deploy-environment create-deploy-environment-create-function-deploy-environment-details -> oci devops deploy-environment deploy-environment create-function-environment
cli_util.rename_command(devops_cli, devops_cli.deploy_environment_group, devops_cli.create_deploy_environment_create_function_deploy_environment_details, "create-function-environment")


# oci devops deploy-environment deploy-environment create-deploy-environment-create-oke-cluster-deploy-environment-details -> oci devops deploy-environment deploy-environment create-oke-cluster-environment
cli_util.rename_command(devops_cli, devops_cli.deploy_environment_group, devops_cli.create_deploy_environment_create_oke_cluster_deploy_environment_details, "create-oke-cluster-environment")


# oci devops deploy-environment deploy-environment-summary list-deploy-environments -> oci devops deploy-environment deploy-environment-summary list
cli_util.rename_command(devops_cli, devops_cli.deploy_environment_summary_group, devops_cli.list_deploy_environments, "list")


# Move commands under 'oci devops deploy-environment deploy-environment-summary' -> 'oci devops deploy-environment'
devops_cli.devops_root_group.commands.pop(devops_cli.deploy_environment_summary_group.name)
devops_cli.deploy_environment_group.add_command(devops_cli.list_deploy_environments)

# Remove oci devops deploy-environment create/update
devops_cli.deploy_environment_group.commands.pop(devops_cli.create_deploy_environment.name)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_environment, params_to_exclude=['deploy_environment_id', 'deploy_environment_type'])
@devops_cli.deploy_environment_group.command(name=cli_util.override('devops_cli.update_deploy_environment.command_name', 'update'), help=devops_cli.update_deploy_environment.help)
@cli_util.option('--environment-id', required=True, help=u"""unique Environment identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployEnvironment'})
@cli_util.wrap_exceptions
def update_deploy_environment_extended(ctx, **kwargs):
    if 'environment_id' in kwargs:
        kwargs['deploy_environment_id'] = kwargs['environment_id']
        kwargs.pop('environment_id')
    ctx.invoke(devops_cli.update_deploy_environment, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_environment_update_compute_instance_group_deploy_environment_details, params_to_exclude=['deploy_environment_id'])
@devops_cli.deploy_environment_group.command(name=cli_util.override('devops_cli.update_deploy_environment_update_compute_instance_group_deploy_environment_details.command_name', 'update-compute-instance-environment'), help=devops_cli.update_deploy_environment_update_compute_instance_group_deploy_environment_details.help)
@cli_util.option('--environment-id', required=True, help=u"""unique Environment identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'compute-instance-group-selectors': {'module': 'devops', 'class': 'ComputeInstanceGroupSelectorCollection'}}, output_type={'module': 'devops', 'class': 'DeployEnvironment'})
@cli_util.wrap_exceptions
def update_deploy_environment_update_compute_instance_group_deploy_environment_details_extended(ctx, **kwargs):
    if 'environment_id' in kwargs:
        kwargs['deploy_environment_id'] = kwargs['environment_id']
        kwargs.pop('environment_id')
    ctx.invoke(devops_cli.update_deploy_environment_update_compute_instance_group_deploy_environment_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.delete_deploy_environment, params_to_exclude=['deploy_environment_id'])
@devops_cli.deploy_environment_group.command(name=cli_util.override('devops_cli.delete_deploy_environment.command_name', 'delete'), help=devops_cli.delete_deploy_environment.help)
@cli_util.option('--environment-id', required=True, help=u"""unique Environment identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_deploy_environment_extended(ctx, **kwargs):
    if 'environment_id' in kwargs:
        kwargs['deploy_environment_id'] = kwargs['environment_id']
        kwargs.pop('environment_id')
    ctx.invoke(devops_cli.delete_deploy_environment, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.get_deploy_environment, params_to_exclude=['deploy_environment_id'])
@devops_cli.deploy_environment_group.command(name=cli_util.override('devops_cli.get_deploy_environment.command_name', 'get'), help=devops_cli.get_deploy_environment.help)
@cli_util.option('--environment-id', required=True, help=u"""unique Environment identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'DeployEnvironment'})
@cli_util.wrap_exceptions
def get_deploy_environment_extended(ctx, **kwargs):
    if 'environment_id' in kwargs:
        kwargs['deploy_environment_id'] = kwargs['environment_id']
        kwargs.pop('environment_id')
    ctx.invoke(devops_cli.get_deploy_environment, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_environment_update_function_deploy_environment_details, params_to_exclude=['deploy_environment_id'])
@devops_cli.deploy_environment_group.command(name=cli_util.override('devops_cli.update_deploy_environment_update_function_deploy_environment_details.command_name', 'update-function-environment'), help=devops_cli.update_deploy_environment_update_function_deploy_environment_details.help)
@cli_util.option('--environment-id', required=True, help=u"""unique Environment identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployEnvironment'})
@cli_util.wrap_exceptions
def update_deploy_environment_update_function_deploy_environment_details_extended(ctx, **kwargs):
    if 'environment_id' in kwargs:
        kwargs['deploy_environment_id'] = kwargs['environment_id']
        kwargs.pop('environment_id')
    ctx.invoke(devops_cli.update_deploy_environment_update_function_deploy_environment_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_environment_update_oke_cluster_deploy_environment_details, params_to_exclude=['deploy_environment_id'])
@devops_cli.deploy_environment_group.command(name=cli_util.override('devops_cli.update_deploy_environment_update_oke_cluster_deploy_environment_details.command_name', 'update-oke-cluster-environment'), help=devops_cli.update_deploy_environment_update_oke_cluster_deploy_environment_details.help)
@cli_util.option('--environment-id', required=True, help=u"""unique Environment identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployEnvironment'})
@cli_util.wrap_exceptions
def update_deploy_environment_update_oke_cluster_deploy_environment_details_extended(ctx, **kwargs):
    if 'environment_id' in kwargs:
        kwargs['deploy_environment_id'] = kwargs['environment_id']
        kwargs.pop('environment_id')
    ctx.invoke(devops_cli.update_deploy_environment_update_oke_cluster_deploy_environment_details, **kwargs)


# oci devops deploy-pipeline deploy-pipeline-summary list-deploy-pipelines -> oci devops deploy-pipeline deploy-pipeline-summary list
cli_util.rename_command(devops_cli, devops_cli.deploy_pipeline_summary_group, devops_cli.list_deploy_pipelines, "list")


# Move commands under 'oci devops deploy-pipeline deploy-pipeline-summary' -> 'oci devops deploy-pipeline'
devops_cli.devops_root_group.commands.pop(devops_cli.deploy_pipeline_summary_group.name)
devops_cli.deploy_pipeline_group.add_command(devops_cli.list_deploy_pipelines)


@cli_util.copy_params_from_generated_command(devops_cli.create_deploy_pipeline, params_to_exclude=['deploy_pipeline_parameters'])
@devops_cli.deploy_pipeline_group.command(name=cli_util.override('devops_cli.create_deploy_pipeline.command_name', 'create'), help=devops_cli.create_deploy_pipeline.help)
@cli_util.option('--pipeline-parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'pipeline-parameters': {'module': 'devops', 'class': 'DeployPipelineParameterCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployPipeline'})
@cli_util.wrap_exceptions
def create_deploy_pipeline_extended(ctx, **kwargs):
    if 'pipeline_parameters' in kwargs:
        kwargs['deploy_pipeline_parameters'] = kwargs['pipeline_parameters']
        kwargs.pop('pipeline_parameters')
    ctx.invoke(devops_cli.create_deploy_pipeline, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.delete_deploy_pipeline, params_to_exclude=['deploy_pipeline_id'])
@devops_cli.deploy_pipeline_group.command(name=cli_util.override('devops_cli.delete_deploy_pipeline.command_name', 'delete'), help=devops_cli.delete_deploy_pipeline.help)
@cli_util.option('--pipeline-id', required=True, help=u"""unique Pipeline identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_deploy_pipeline_extended(ctx, **kwargs):
    if 'pipeline_id' in kwargs:
        kwargs['deploy_pipeline_id'] = kwargs['pipeline_id']
        kwargs.pop('pipeline_id')
    ctx.invoke(devops_cli.delete_deploy_pipeline, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.get_deploy_pipeline, params_to_exclude=['deploy_pipeline_id'])
@devops_cli.deploy_pipeline_group.command(name=cli_util.override('devops_cli.get_deploy_pipeline.command_name', 'get'), help=devops_cli.get_deploy_pipeline.help)
@cli_util.option('--pipeline-id', required=True, help=u"""unique Pipeline identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'DeployPipeline'})
@cli_util.wrap_exceptions
def get_deploy_pipeline_extended(ctx, **kwargs):
    if 'pipeline_id' in kwargs:
        kwargs['deploy_pipeline_id'] = kwargs['pipeline_id']
        kwargs.pop('pipeline_id')
    ctx.invoke(devops_cli.get_deploy_pipeline, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_pipeline, params_to_exclude=['deploy_pipeline_id', 'deploy_pipeline_parameters'])
@devops_cli.deploy_pipeline_group.command(name=cli_util.override('devops_cli.update_deploy_pipeline.command_name', 'update'), help=devops_cli.update_deploy_pipeline.help)
@cli_util.option('--pipeline-id', required=True, help=u"""unique Pipeline identifier""")
@cli_util.option('--pipeline-parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'pipeline-parameters': {'module': 'devops', 'class': 'DeployPipelineParameterCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployPipeline'})
@cli_util.wrap_exceptions
def update_deploy_pipeline_extended(ctx, **kwargs):
    if 'pipeline_id' in kwargs:
        kwargs['deploy_pipeline_id'] = kwargs['pipeline_id']
        kwargs.pop('pipeline_id')
    if 'pipeline_parameters' in kwargs:
        kwargs['deploy_pipeline_parameters'] = kwargs['pipeline_parameters']
        kwargs.pop('pipeline_parameters')
    ctx.invoke(devops_cli.update_deploy_pipeline, **kwargs)


# Move commands under 'oci devops deploy-stage deploy-stage-summary' -> 'oci devops deploy-stage'
devops_cli.devops_root_group.commands.pop(devops_cli.deploy_stage_summary_group.name)

# Remove oci devops deploy-stage create/update
devops_cli.deploy_stage_group.commands.pop(devops_cli.create_deploy_stage.name)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_stage, params_to_exclude=['deploy_stage_id', 'deploy_stage_type', 'deploy_stage_predecessor_collection'])
@devops_cli.deploy_stage_group.command(name=cli_util.override('devops_cli.update_deploy_stage.command_name', 'update'), help=devops_cli.update_deploy_stage.help)
@cli_util.option('--stage-id', required=True, help=u"""unique Stage identifier""")
@cli_util.option('--stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_extended(ctx, **kwargs):
    if 'stage_id' in kwargs:
        kwargs['deploy_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')
    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')
    ctx.invoke(devops_cli.update_deploy_stage, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_deploy_stage_create_compute_instance_group_deploy_stage_details, params_to_exclude=['deploy_pipeline_id', 'deploy_stage_predecessor_collection', 'compute_instance_group_deploy_environment_id', 'deploy_artifact_ids', 'deployment_spec_deploy_artifact_id'])
@devops_cli.deploy_stage_group.command(name=cli_util.override('devops_cli.create_deploy_stage_create_compute_instance_group_deploy_stage_details.command_name', 'create-deploy-compute-instance-group-stage'), help=devops_cli.create_deploy_stage_create_compute_instance_group_deploy_stage_details.help)
@cli_util.option('--pipeline-id', required=True, help=u"""Pipeline Identifier""")
@cli_util.option('--stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compute-instance-group-environment-id', required=True, help=u"""A compute instance group environment OCID for rolling deployment.""")
@cli_util.option('--deployment-spec-artifact-id', required=True, help=u"""The OCID of the artifact that contains the deployment specification.""")
@cli_util.option('--artifact-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Additional file artifact OCIDs.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollout-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupRolloutPolicy'}, 'rollback-policy': {'module': 'devops', 'class': 'DeployStageRollbackPolicy'}, 'failure-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupFailurePolicy'}, 'load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_compute_instance_group_deploy_stage_details_extended(ctx, **kwargs):
    if 'pipeline_id' in kwargs:
        kwargs['deploy_pipeline_id'] = kwargs['pipeline_id']
        kwargs.pop('pipeline_id')
    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')
    if 'compute_instance_group_environment_id' in kwargs:
        kwargs['compute_instance_group_deploy_environment_id'] = kwargs['compute_instance_group_environment_id']
        kwargs.pop('compute_instance_group_environment_id')
    if 'artifact_ids' in kwargs:
        kwargs['deploy_artifact_ids'] = kwargs['artifact_ids']
        kwargs.pop('artifact_ids')
    if 'deployment_spec_artifact_id' in kwargs:
        kwargs['deployment_spec_deploy_artifact_id'] = kwargs['deployment_spec_artifact_id']
        kwargs.pop('deployment_spec_artifact_id')
    ctx.invoke(devops_cli.create_deploy_stage_create_compute_instance_group_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.delete_deploy_stage, params_to_exclude=['deploy_stage_id'])
@devops_cli.deploy_stage_group.command(name=cli_util.override('devops_cli.delete_deploy_stage.command_name', 'delete'), help=devops_cli.delete_deploy_stage.help)
@cli_util.option('--stage-id', required=True, help=u"""unique Stage identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_deploy_stage_extended(ctx, **kwargs):
    if 'stage_id' in kwargs:
        kwargs['deploy_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')
    ctx.invoke(devops_cli.delete_deploy_stage, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.list_deploy_stages, params_to_exclude=['deploy_pipeline_id'])
@devops_cli.deploy_stage_group.command(name=cli_util.override('devops_cli.list_deploy_stages.command_name', 'list'), help=devops_cli.list_deploy_stages.help)
@cli_util.option('--pipeline-id', help=u"""Pipeline Identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'DeployStageCollection'})
@cli_util.wrap_exceptions
def list_deploy_stages_extended(ctx, **kwargs):
    if 'pipeline_id' in kwargs:
        kwargs['deploy_pipeline_id'] = kwargs['pipeline_id']
        kwargs.pop('pipeline_id')
    ctx.invoke(devops_cli.list_deploy_stages, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_deploy_stage_create_oke_deploy_stage_details, params_to_exclude=['kubernetes_manifest_deploy_artifact_ids', 'deploy_pipeline_id', 'deploy_stage_predecessor_collection', 'oke_cluster_deploy_environment_id'])
@devops_cli.deploy_stage_group.command(name=cli_util.override('devops_cli.create_deploy_stage_create_oke_deploy_stage_details.command_name', 'create-deploy-oke-stage'), help=devops_cli.create_deploy_stage_create_oke_deploy_stage_details.help)
@cli_util.option('--pipeline-id', required=True, help=u"""Pipeline Identifier""")
@cli_util.option('--kubernetes-manifest-artifact-ids', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of KubernetesManifest artifact OCIDs, the manifests should not include any Job resource.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--oke-cluster-environment-id', required=True, help=u"""OkeCluster environment OCID for deployment.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'kubernetes-manifest-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollback-policy': {'module': 'devops', 'class': 'DeployStageRollbackPolicy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_oke_deploy_stage_details_extended(ctx, **kwargs):
    if 'kubernetes_manifest_artifact_ids' in kwargs:
        kwargs['kubernetes_manifest_deploy_artifact_ids'] = kwargs['kubernetes_manifest_artifact_ids']
        kwargs.pop('kubernetes_manifest_artifact_ids')
    if 'pipeline_id' in kwargs:
        kwargs['deploy_pipeline_id'] = kwargs['pipeline_id']
        kwargs.pop('pipeline_id')
    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')
    if 'oke_cluster_environment_id' in kwargs:
        kwargs['oke_cluster_deploy_environment_id'] = kwargs['oke_cluster_environment_id']
        kwargs.pop('oke_cluster_environment_id')
    ctx.invoke(devops_cli.create_deploy_stage_create_oke_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_deploy_stage_create_function_deploy_stage_details, params_to_exclude=['deploy_pipeline_id', 'deploy_stage_predecessor_collection', 'function_deploy_environment_id', 'docker_image_deploy_artifact_id'])
@devops_cli.deploy_stage_group.command(name=cli_util.override('devops_cli.create_deploy_stage_create_function_deploy_stage_details.command_name', 'create-deploy-function-stage'), help=devops_cli.create_deploy_stage_create_function_deploy_stage_details.help)
@cli_util.option('--stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--pipeline-id', required=True, help=u"""Pipeline Identifier""")
@cli_util.option('--function-environment-id', required=True, help=u"""Function environment OCID.""")
@cli_util.option('--docker-image-artifact-id', required=True, help=u"""A docker image artifact OCID.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'config': {'module': 'devops', 'class': 'dict(str, string)'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_function_deploy_stage_details_extended(ctx, **kwargs):
    if 'pipeline_id' in kwargs:
        kwargs['deploy_pipeline_id'] = kwargs['pipeline_id']
        kwargs.pop('pipeline_id')
    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')
    if 'function_environment_id' in kwargs:
        kwargs['function_deploy_environment_id'] = kwargs['function_environment_id']
        kwargs.pop('function_environment_id')
    if 'docker_image_artifact_id' in kwargs:
        kwargs['docker_image_deploy_artifact_id'] = kwargs['docker_image_artifact_id']
        kwargs.pop('docker_image_artifact_id')
    ctx.invoke(devops_cli.create_deploy_stage_create_function_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_deploy_stage_create_oke_helm_chart_deploy_stage_details, params_to_exclude=['deploy_pipeline_id', 'deploy_stage_predecessor_collection', 'helm_chart_deploy_artifact_id', 'oke_cluster_deploy_environment_id', 'are_hooks_enabled', 'is_debug_enabled', 'is_force_enabled', 'max_history', 'should_cleanup_on_fail', 'should_not_wait', 'should_reset_values', 'should_reuse_values', 'should_skip_crds', 'should_skip_render_subchart_notes'])
@devops_cli.deploy_stage_group.command(name=cli_util.override('devops_cli.create_deploy_stage_create_oke_helm_chart_deploy_stage_details.command_name', 'create-oke-helm-chart-stage'), help=devops_cli.create_deploy_stage_create_oke_helm_chart_deploy_stage_details.help)
@cli_util.option('--oke-cluster-environment-id', required=True, help="""Kubernetes cluster environment OCID for deployment. [required]""")
@cli_util.option('--helm-chart-artifact-id', required=True, help="""Helm chart artifact OCID. [required]""")
@cli_util.option('--stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help="""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.
 [required]""")
@cli_util.option('--pipeline-id', required=True, help=u"""The OCID of a pipeline. [required]""")
@cli_util.option('--cleanup-on-fail', type=click.BOOL, help=u"""Passes the --cleanup-on-fail flag for helm upgrade. Set to false by default""")
@cli_util.option('--debug-helm', type=click.BOOL, help=u"""Passes the --debug flag for helm upgrade. Set to false by default""")
@cli_util.option('--force-helm', type=click.BOOL, help=u"""Passes the --force flag for helm upgrade. Set to false by default""")
@cli_util.option('--history-max', type=click.INT, help=u"""Passes the --history-max flag for helm upgrade. Set to 10 by default""")
@cli_util.option('--no-hooks', type=click.BOOL, help=u"""Passes the --no-hooks flag for helm upgrade. Set to true by default""")
@cli_util.option('--render-subchart-notes', type=click.BOOL, help=u"""Passes the --render-subchart-notes flag for helm upgrade. Set to true by default""")
@cli_util.option('--reset-values', type=click.BOOL, help=u"""Passes the --reset-values flag for helm upgrade. Set to false by default""")
@cli_util.option('--reuse-values', type=click.BOOL, help=u"""Passes the --reuse-values flag for helm upgrade. Set to false by default""")
@cli_util.option('--skip-crds', type=click.BOOL, help=u"""Passes the --skip-crds flag for helm upgrade. Set to false by default""")
@cli_util.option('--wait-helm', type=click.BOOL, help=u"""Passes the --wait flag for helm upgrade. Set to true by default""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'values-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollback-policy': {'module': 'devops', 'class': 'DeployStageRollbackPolicy'}, 'set-values': {'module': 'devops', 'class': 'HelmSetValueCollection'}, 'set-string': {'module': 'devops', 'class': 'HelmSetValueCollection'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_oke_helm_chart_deploy_stage_details_extended(ctx, **kwargs):
    if 'oke_cluster_environment_id' in kwargs:
        kwargs['oke_cluster_deploy_environment_id'] = kwargs['oke_cluster_environment_id']
        kwargs.pop('oke_cluster_environment_id')
    if 'helm_chart_artifact_id' in kwargs:
        kwargs['helm_chart_deploy_artifact_id'] = kwargs['helm_chart_artifact_id']
        kwargs.pop('helm_chart_artifact_id')
    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')
    if 'pipeline_id' in kwargs:
        kwargs['deploy_pipeline_id'] = kwargs['pipeline_id']
        kwargs.pop('pipeline_id')
    if 'cleanup_on_fail' in kwargs:
        kwargs['should_cleanup_on_fail'] = kwargs['cleanup_on_fail']
        kwargs.pop('cleanup_on_fail')
    if 'debug_helm' in kwargs:
        kwargs['is_debug_enabled'] = kwargs['debug_helm']
        kwargs.pop('debug_helm')
    if 'force_helm' in kwargs:
        kwargs['is_force_enabled'] = kwargs['force_helm']
        kwargs.pop('force_helm')
    if 'history_max' in kwargs:
        kwargs['max_history'] = kwargs['history_max']
        kwargs.pop('history_max')
    if 'no_hooks' in kwargs:
        kwargs['are_hooks_enabled'] = not kwargs['no_hooks']
        kwargs.pop('no_hooks')
    if 'render_subchart_notes' in kwargs:
        kwargs['should_skip_render_subchart_notes'] = not kwargs['render_subchart_notes']
        kwargs.pop('render_subchart_notes')
    if 'reuse_values' in kwargs:
        kwargs['should_reuse_values'] = kwargs['reuse_values']
        kwargs.pop('reuse_values')
    if 'reset_values' in kwargs:
        kwargs['should_reset_values'] = kwargs['reset_values']
        kwargs.pop('reset_values')
    if 'skip_crds' in kwargs:
        kwargs['should_skip_crds'] = kwargs['skip_crds']
        kwargs.pop('skip_crds')
    if 'wait_helm' in kwargs:
        kwargs['should_not_wait'] = not kwargs['wait_helm']
        kwargs.pop('wait_helm')
    ctx.invoke(devops_cli.create_deploy_stage_create_oke_helm_chart_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_deploy_stage_create_invoke_function_deploy_stage_details, params_to_exclude=['deploy_pipeline_id', 'deploy_stage_predecessor_collection', 'function_deploy_environment_id', 'deploy_artifact_id'])
@devops_cli.deploy_stage_group.command(name=cli_util.override('devops_cli.create_deploy_stage_create_invoke_function_deploy_stage_details.command_name', 'create-invoke-function-stage'), help=devops_cli.create_deploy_stage_create_invoke_function_deploy_stage_details.help)
@cli_util.option('--pipeline-id', required=True, help=u"""Pipeline Identifier""")
@cli_util.option('--stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--function-environment-id', required=True, help=u"""Function environment OCID.""")
@cli_util.option('--artifact-id', help=u"""Optional binary artifat OCID user may provide to this stage.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_invoke_function_deploy_stage_details_extended(ctx, **kwargs):
    if 'pipeline_id' in kwargs:
        kwargs['deploy_pipeline_id'] = kwargs['pipeline_id']
        kwargs.pop('pipeline_id')
    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')
    if 'function_environment_id' in kwargs:
        kwargs['function_deploy_environment_id'] = kwargs['function_environment_id']
        kwargs.pop('function_environment_id')
    if 'artifact_id' in kwargs:
        kwargs['deploy_artifact_id'] = kwargs['artifact_id']
        kwargs.pop('artifact_id')
    ctx.invoke(devops_cli.create_deploy_stage_create_invoke_function_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_deploy_stage_create_load_balancer_traffic_shift_deploy_stage_details, params_to_exclude=['deploy_pipeline_id', 'deploy_stage_predecessor_collection'])
@devops_cli.deploy_stage_group.command(name=cli_util.override('devops_cli.create_deploy_stage_create_load_balancer_traffic_shift_deploy_stage_details.command_name', 'create-load-balancer-traffic-shift-stage'), help=devops_cli.create_deploy_stage_create_load_balancer_traffic_shift_deploy_stage_details.help)
@cli_util.option('--pipeline-id', required=True, help=u"""Pipeline Identifier""")
@cli_util.option('--stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'blue-backend-ips': {'module': 'devops', 'class': 'BackendSetIpCollection'}, 'green-backend-ips': {'module': 'devops', 'class': 'BackendSetIpCollection'}, 'rollout-policy': {'module': 'devops', 'class': 'LoadBalancerTrafficShiftRolloutPolicy'}, 'load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}, 'rollback-policy': {'module': 'devops', 'class': 'DeployStageRollbackPolicy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_load_balancer_traffic_shift_deploy_stage_details_extended(ctx, **kwargs):
    if 'pipeline_id' in kwargs:
        kwargs['deploy_pipeline_id'] = kwargs['pipeline_id']
        kwargs.pop('pipeline_id')
    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')
    ctx.invoke(devops_cli.create_deploy_stage_create_load_balancer_traffic_shift_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_deploy_stage_create_manual_approval_deploy_stage_details, params_to_exclude=['deploy_pipeline_id', 'deploy_stage_predecessor_collection'])
@devops_cli.deploy_stage_group.command(name=cli_util.override('devops_cli.create_deploy_stage_create_manual_approval_deploy_stage_details.command_name', 'create-manual-approval-stage'), help=devops_cli.create_deploy_stage_create_manual_approval_deploy_stage_details.help)
@cli_util.option('--pipeline-id', required=True, help=u"""Pipeline Identifier""")
@cli_util.option('--stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'approval-policy': {'module': 'devops', 'class': 'ApprovalPolicy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_manual_approval_deploy_stage_details_extended(ctx, **kwargs):
    if 'pipeline_id' in kwargs:
        kwargs['deploy_pipeline_id'] = kwargs['pipeline_id']
        kwargs.pop('pipeline_id')
    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')
    ctx.invoke(devops_cli.create_deploy_stage_create_manual_approval_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_deploy_stage_create_wait_deploy_stage_details, params_to_exclude=['deploy_pipeline_id', 'deploy_stage_predecessor_collection'])
@devops_cli.deploy_stage_group.command(name=cli_util.override('devops_cli.create_deploy_stage_create_wait_deploy_stage_details.command_name', 'create-wait-stage'), help=devops_cli.create_deploy_stage_create_wait_deploy_stage_details.help)
@cli_util.option('--pipeline-id', required=True, help=u"""Pipeline Identifier""")
@cli_util.option('--stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'wait-criteria': {'module': 'devops', 'class': 'WaitCriteria'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_wait_deploy_stage_details_extended(ctx, **kwargs):
    if 'pipeline_id' in kwargs:
        kwargs['deploy_pipeline_id'] = kwargs['pipeline_id']
        kwargs.pop('pipeline_id')
    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')
    ctx.invoke(devops_cli.create_deploy_stage_create_wait_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.get_deploy_stage, params_to_exclude=['deploy_stage_id'])
@devops_cli.deploy_stage_group.command(name=cli_util.override('devops_cli.get_deploy_stage.command_name', 'get'), help=devops_cli.get_deploy_stage.help)
@cli_util.option('--stage-id', required=True, help=u"""unique Stage identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def get_deploy_stage_extended(ctx, **kwargs):
    if 'stage_id' in kwargs:
        kwargs['deploy_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')
    ctx.invoke(devops_cli.get_deploy_stage, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_stage_update_compute_instance_group_deploy_stage_details, params_to_exclude=['deploy_stage_id', 'deploy_stage_predecessor_collection', 'deploy_artifact_ids', 'deployment_spec_deploy_artifact_id', 'compute_instance_group_deploy_environment_id'])
@devops_cli.deploy_stage_group.command(name=cli_util.override('devops_cli.update_deploy_stage_update_compute_instance_group_deploy_stage_details.command_name', 'update-deploy-compute-instance-group-stage'), help=devops_cli.update_deploy_stage_update_compute_instance_group_deploy_stage_details.help)
@cli_util.option('--stage-id', required=True, help=u"""unique Stage identifier""")
@cli_util.option('--stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--artifact-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Additional file artifact OCIDs.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--deployment-spec-artifact-id', help=u"""The OCID of the artifact that contains the deployment specification.""")
@cli_util.option('--compute-instance-group-environment-id', help=u"""A compute instance group environment OCID for rolling deployment.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollout-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupRolloutPolicy'}, 'rollback-policy': {'module': 'devops', 'class': 'DeployStageRollbackPolicy'}, 'failure-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupFailurePolicy'}, 'load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_compute_instance_group_deploy_stage_details_extended(ctx, **kwargs):
    if 'stage_id' in kwargs:
        kwargs['deploy_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')
    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')
    if 'artifact_ids' in kwargs:
        kwargs['deploy_artifact_ids'] = kwargs['artifact_ids']
        kwargs.pop('artifact_ids')
    if 'deployment_spec_artifact_id' in kwargs:
        kwargs['deployment_spec_deploy_artifact_id'] = kwargs['deployment_spec_artifact_id']
        kwargs.pop('deployment_spec_artifact_id')
    if 'compute_instance_group_environment_id' in kwargs:
        kwargs['compute_instance_group_deploy_environment_id'] = kwargs['compute_instance_group_environment_id']
        kwargs.pop('compute_instance_group_environment_id')
    ctx.invoke(devops_cli.update_deploy_stage_update_compute_instance_group_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_stage_update_function_deploy_stage_details, params_to_exclude=['deploy_stage_id', 'deploy_stage_predecessor_collection', 'function_deploy_environment_id', 'docker_image_deploy_artifact_id'])
@devops_cli.deploy_stage_group.command(name=cli_util.override('devops_cli.update_deploy_stage_update_function_deploy_stage_details.command_name', 'update-deploy-function-stage'), help=devops_cli.update_deploy_stage_update_function_deploy_stage_details.help)
@cli_util.option('--stage-id', required=True, help=u"""unique Stage identifier""")
@cli_util.option('--stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--function-environment-id', help=u"""Function environment OCID.""")
@cli_util.option('--docker-image-artifact-id', help=u"""A docker image artifact OCID.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'config': {'module': 'devops', 'class': 'dict(str, string)'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_function_deploy_stage_details_extended(ctx, **kwargs):
    if 'stage_id' in kwargs:
        kwargs['deploy_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')
    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')
    if 'function_environment_id' in kwargs:
        kwargs['function_deploy_environment_id'] = kwargs['function_environment_id']
        kwargs.pop('function_environment_id')
    if 'docker_image_artifact_id' in kwargs:
        kwargs['docker_image_deploy_artifact_id'] = kwargs['docker_image_artifact_id']
        kwargs.pop('docker_image_artifact_id')
    ctx.invoke(devops_cli.update_deploy_stage_update_function_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_stage_update_invoke_function_deploy_stage_details, params_to_exclude=['deploy_stage_id', 'deploy_stage_predecessor_collection', 'function_deploy_environment_id', 'deploy_artifact_id'])
@devops_cli.deploy_stage_group.command(name=cli_util.override('devops_cli.update_deploy_stage_update_invoke_function_deploy_stage_details.command_name', 'update-invoke-function-stage'), help=devops_cli.update_deploy_stage_update_invoke_function_deploy_stage_details.help)
@cli_util.option('--stage-id', required=True, help=u"""unique Stage identifier""")
@cli_util.option('--stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--function-environment-id', help=u"""Function environment OCID.""")
@cli_util.option('--artifact-id', help=u"""Optional binary artifat OCID user may provide to this stage.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'config': {'module': 'devops', 'class': 'dict(str, string)'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_invoke_function_deploy_stage_details_extended(ctx, **kwargs):
    if 'stage_id' in kwargs:
        kwargs['deploy_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')
    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')
    if 'function_environment_id' in kwargs:
        kwargs['function_deploy_environment_id'] = kwargs['function_environment_id']
        kwargs.pop('function_environment_id')
    if 'artifact_id' in kwargs:
        kwargs['deploy_artifact_id'] = kwargs['artifact_id']
        kwargs.pop('artifact_id')
    ctx.invoke(devops_cli.update_deploy_stage_update_invoke_function_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_stage_update_load_balancer_traffic_shift_deploy_stage_details, params_to_exclude=['deploy_stage_id', 'deploy_stage_predecessor_collection'])
@devops_cli.deploy_stage_group.command(name=cli_util.override('devops_cli.update_deploy_stage_update_load_balancer_traffic_shift_deploy_stage_details.command_name', 'update-load-balancer-traffic-shift-stage'), help=devops_cli.update_deploy_stage_update_load_balancer_traffic_shift_deploy_stage_details.help)
@cli_util.option('--stage-id', required=True, help=u"""unique Stage identifier""")
@cli_util.option('--stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'blue-backend-ips': {'module': 'devops', 'class': 'BackendSetIpCollection'}, 'green-backend-ips': {'module': 'devops', 'class': 'BackendSetIpCollection'}, 'rollout-policy': {'module': 'devops', 'class': 'LoadBalancerTrafficShiftRolloutPolicy'}, 'load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}, 'rollback-policy': {'module': 'devops', 'class': 'DeployStageRollbackPolicy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_load_balancer_traffic_shift_deploy_stage_details_extended(ctx, **kwargs):
    if 'stage_id' in kwargs:
        kwargs['deploy_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')
    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')
    ctx.invoke(devops_cli.update_deploy_stage_update_load_balancer_traffic_shift_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_stage_update_manual_approval_deploy_stage_details, params_to_exclude=['deploy_stage_id', 'deploy_stage_predecessor_collection'])
@devops_cli.deploy_stage_group.command(name=cli_util.override('devops_cli.update_deploy_stage_update_manual_approval_deploy_stage_details.command_name', 'update-manual-approval-stage'), help=devops_cli.update_deploy_stage_update_manual_approval_deploy_stage_details.help)
@cli_util.option('--stage-id', required=True, help=u"""unique Stage identifier""")
@cli_util.option('--stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'approval-policy': {'module': 'devops', 'class': 'ApprovalPolicy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_manual_approval_deploy_stage_details_extended(ctx, **kwargs):
    if 'stage_id' in kwargs:
        kwargs['deploy_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')
    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')
    ctx.invoke(devops_cli.update_deploy_stage_update_manual_approval_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_stage_update_oke_deploy_stage_details, params_to_exclude=['deploy_stage_id', 'deploy_stage_predecessor_collection', 'kubernetes_manifest_deploy_artifact_ids', 'oke_cluster_deploy_environment_id'])
@devops_cli.deploy_stage_group.command(name=cli_util.override('devops_cli.update_deploy_stage_update_oke_deploy_stage_details.command_name', 'update-deploy-oke-stage'), help=devops_cli.update_deploy_stage_update_oke_deploy_stage_details.help)
@cli_util.option('--stage-id', required=True, help=u"""unique Stage identifier""")
@cli_util.option('--stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--kubernetes-manifest-artifact-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of KubernetesManifest artifact OCIDs, the manifests should not include any Job resource.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--oke-cluster-environment-id', help=u"""OkeCluster environment OCID for deployment.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'kubernetes-manifest-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollback-policy': {'module': 'devops', 'class': 'DeployStageRollbackPolicy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_oke_deploy_stage_details_extended(ctx, **kwargs):
    if 'stage_id' in kwargs:
        kwargs['deploy_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')
    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')
    if 'kubernetes_manifest_artifact_ids' in kwargs:
        kwargs['kubernetes_manifest_deploy_artifact_ids'] = kwargs['kubernetes_manifest_artifact_ids']
        kwargs.pop('kubernetes_manifest_artifact_ids')
    if 'oke_cluster_environment_id' in kwargs:
        kwargs['oke_cluster_deploy_environment_id'] = kwargs['oke_cluster_environment_id']
        kwargs.pop('oke_cluster_environment_id')
    ctx.invoke(devops_cli.update_deploy_stage_update_oke_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_stage_update_oke_helm_chart_deploy_stage_details, params_to_exclude=['deploy_stage_id', 'deploy_stage_predecessor_collection', 'helm_chart_deploy_artifact_id', 'oke_cluster_deploy_environment_id', 'are_hooks_enabled', 'is_debug_enabled', 'is_force_enabled', 'max_history', 'should_cleanup_on_fail', 'should_not_wait', 'should_reset_values', 'should_reuse_values', 'should_skip_crds', 'should_skip_render_subchart_notes'])
@devops_cli.deploy_stage_group.command(name=cli_util.override('devops_cli.update_deploy_stage_update_oke_helm_chart_deploy_stage_details.command_name', 'update-oke-helm-chart-stage'), help=devops_cli.update_deploy_stage_update_oke_helm_chart_deploy_stage_details.help)
@cli_util.option('--oke-cluster-environment-id', help="""Kubernetes cluster environment OCID for deployment.""")
@cli_util.option('--helm-chart-artifact-id', help="""Helm chart artifact OCID.""")
@cli_util.option('--stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help="""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--stage-id', required=True, help=u"""Unique stage identifier. [required]""")
@cli_util.option('--cleanup-on-fail', type=click.BOOL, help=u"""Passes the --cleanup-on-fail flag for helm upgrade. Set to false by default""")
@cli_util.option('--debug-helm', type=click.BOOL, help=u"""Passes the --debug flag for helm upgrade. Set to false by default""")
@cli_util.option('--force-helm', type=click.BOOL, help=u"""Passes the --force flag for helm upgrade. Set to false by default""")
@cli_util.option('--history-max', type=click.INT, help=u"""Passes the --history-max flag for helm upgrade. Set to 10 by default""")
@cli_util.option('--no-hooks', type=click.BOOL, help=u"""Passes the --no-hooks flag for helm upgrade. Set to true by default""")
@cli_util.option('--render-subchart-notes', type=click.BOOL, help=u"""Passes the --render-subchart-notes flag for helm upgrade. Set to true by default""")
@cli_util.option('--reset-values', type=click.BOOL, help=u"""Passes the --reset-values flag for helm upgrade. Set to false by default""")
@cli_util.option('--reuse-values', type=click.BOOL, help=u"""Passes the --reuse-values flag for helm upgrade. Set to false by default""")
@cli_util.option('--skip-crds', type=click.BOOL, help=u"""Passes the --skip-crds flag for helm upgrade. Set to false by default""")
@cli_util.option('--wait-helm', type=click.BOOL, help=u"""Passes the --wait flag for helm upgrade. Set to true by default""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'values-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollback-policy': {'module': 'devops', 'class': 'DeployStageRollbackPolicy'}, 'set-values': {'module': 'devops', 'class': 'HelmSetValueCollection'}, 'set-string': {'module': 'devops', 'class': 'HelmSetValueCollection'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_oke_helm_chart_deploy_stage_details_extended(ctx, **kwargs):
    if 'oke_cluster_environment_id' in kwargs:
        kwargs['oke_cluster_deploy_environment_id'] = kwargs['oke_cluster_environment_id']
        kwargs.pop('oke_cluster_environment_id')
    if 'helm_chart_artifact_id' in kwargs:
        kwargs['helm_chart_deploy_artifact_id'] = kwargs['helm_chart_artifact_id']
        kwargs.pop('helm_chart_artifact_id')
    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')
    if 'stage_id' in kwargs:
        kwargs['deploy_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')
    if 'cleanup_on_fail' in kwargs:
        kwargs['should_cleanup_on_fail'] = kwargs['cleanup_on_fail']
        kwargs.pop('cleanup_on_fail')
    if 'debug_helm' in kwargs:
        kwargs['is_debug_enabled'] = kwargs['debug_helm']
        kwargs.pop('debug_helm')
    if 'force_helm' in kwargs:
        kwargs['is_force_enabled'] = kwargs['force_helm']
        kwargs.pop('force_helm')
    if 'history_max' in kwargs:
        kwargs['max_history'] = kwargs['history_max']
        kwargs.pop('history_max')
    if 'no_hooks' in kwargs:
        kwargs['are_hooks_enabled'] = not kwargs['no_hooks']
        kwargs.pop('no_hooks')
    if 'render_subchart_notes' in kwargs:
        kwargs['should_skip_render_subchart_notes'] = not kwargs['render_subchart_notes']
        kwargs.pop('render_subchart_notes')
    if 'reuse_values' in kwargs:
        kwargs['should_reuse_values'] = kwargs['reuse_values']
        kwargs.pop('reuse_values')
    if 'reset_values' in kwargs:
        kwargs['should_reset_values'] = kwargs['reset_values']
        kwargs.pop('reset_values')
    if 'skip_crds' in kwargs:
        kwargs['should_skip_crds'] = kwargs['skip_crds']
        kwargs.pop('skip_crds')
    if 'wait_helm' in kwargs:
        kwargs['should_not_wait'] = not kwargs['wait_helm']
        kwargs.pop('wait_helm')
    ctx.invoke(devops_cli.update_deploy_stage_update_oke_helm_chart_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_stage_update_wait_deploy_stage_details, params_to_exclude=['deploy_stage_id', 'deploy_stage_predecessor_collection'])
@devops_cli.deploy_stage_group.command(name=cli_util.override('devops_cli.update_deploy_stage_update_wait_deploy_stage_details.command_name', 'update-wait-stage'), help=devops_cli.update_deploy_stage_update_wait_deploy_stage_details.help)
@cli_util.option('--stage-id', required=True, help=u"""unique Stage identifier""")
@cli_util.option('--stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'wait-criteria': {'module': 'devops', 'class': 'WaitCriteria'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_wait_deploy_stage_details_extended(ctx, **kwargs):
    if 'stage_id' in kwargs:
        kwargs['deploy_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')
    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')
    ctx.invoke(devops_cli.update_deploy_stage_update_wait_deploy_stage_details, **kwargs)


# Remove oci devops deployment update-deployment-update-deploy-pipeline-redeployment-details
# Remove oci devops deployment update-deployment-update-single-deploy-stage-deployment-details
# Remove oci devops deployment update-deployment-update-deploy-pipeline-deployment-details
devops_cli.deployment_group.commands.pop(devops_cli.update_deployment_update_deploy_pipeline_redeployment_details.name)
devops_cli.deployment_group.commands.pop(devops_cli.update_deployment_update_single_deploy_stage_deployment_details.name)
devops_cli.deployment_group.commands.pop(devops_cli.update_deployment_update_deploy_pipeline_deployment_details.name)


# Move commands under 'oci devops deployment deployment-summary' -> 'oci devops deployment'
devops_cli.devops_root_group.commands.pop(devops_cli.deployment_summary_group.name)

# Remove oci devops deployment create/update
devops_cli.deployment_group.commands.pop(devops_cli.create_deployment.name)
devops_cli.deployment_group.commands.pop(devops_cli.update_deployment.name)


@cli_util.copy_params_from_generated_command(devops_cli.update_deployment_update_deploy_pipeline_deployment_details, params_to_exclude=[])
@devops_cli.deployment_group.command(name=cli_util.override('devops_cli.update_deployment_update_deploy_pipeline_deployment_details.command_name', 'update'), help=devops_cli.update_deployment_update_deploy_pipeline_deployment_details.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Deployment'})
@cli_util.wrap_exceptions
def update_deployment_update_deploy_pipeline_deployment_details_extended(ctx, **kwargs):
    ctx.invoke(devops_cli.update_deployment_update_deploy_pipeline_deployment_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.list_deployments, params_to_exclude=['deploy_pipeline_id'])
@devops_cli.deployment_group.command(name=cli_util.override('devops_cli.list_deployments.command_name', 'list'), help=devops_cli.list_deployments.help)
@cli_util.option('--pipeline-id', help=u"""Pipeline Identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'DeploymentCollection'})
@cli_util.wrap_exceptions
def list_deployments_extended(ctx, **kwargs):
    if 'pipeline_id' in kwargs:
        kwargs['deploy_pipeline_id'] = kwargs['pipeline_id']
        kwargs.pop('pipeline_id')
    ctx.invoke(devops_cli.list_deployments, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_deployment_create_deploy_pipeline_deployment_details, params_to_exclude=['deploy_pipeline_id', 'deploy_artifact_override_arguments', 'deploy_stage_override_arguments'])
@devops_cli.deployment_group.command(name=cli_util.override('devops_cli.create_deployment_create_deploy_pipeline_deployment_details.command_name', 'create-pipeline-deployment'), help=devops_cli.create_deployment_create_deploy_pipeline_deployment_details.help)
@cli_util.option('--stage-override-arguments', type=custom_types.CLI_COMPLEX_TYPE, help="""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--pipeline-id', required=True, help=u"""Pipeline Identifier""")
@cli_util.option('--artifact-override-arguments', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--dry-run', type=click.BOOL, help=u"""Set this flag to execute a dry run deployment. Only available for helm deployments as of now""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'deployment-arguments': {'module': 'devops', 'class': 'DeploymentArgumentCollection'}, 'stage-override-arguments': {'module': 'devops', 'class': 'DeployStageOverrideArgumentCollection'}, 'artifact-override-arguments': {'module': 'devops', 'class': 'DeployArtifactOverrideArgumentCollection'}}, output_type={'module': 'devops', 'class': 'Deployment'})
@cli_util.wrap_exceptions
def create_deployment_create_deploy_pipeline_deployment_details_extended(ctx, **kwargs):

    if 'stage_override_arguments' in kwargs:
        kwargs['deploy_stage_override_arguments'] = kwargs['stage_override_arguments']
        kwargs.pop('stage_override_arguments')
    if 'pipeline_id' in kwargs:
        kwargs['deploy_pipeline_id'] = kwargs['pipeline_id']
        kwargs.pop('pipeline_id')
    if 'artifact_override_arguments' in kwargs:
        kwargs['deploy_artifact_override_arguments'] = kwargs['artifact_override_arguments']
        kwargs.pop('artifact_override_arguments')
    if kwargs['dry_run'] is not None:
        dry_run_arg = {
            'name': 'dry_run',
            'value': str(kwargs['dry_run'])
        }
        if kwargs['deployment_arguments'] is not None:
            deployment_args = cli_util.parse_json_parameter("deployment_arguments", kwargs['deployment_arguments'])
            deployment_args['items'].append(dry_run_arg)
            kwargs['deployment_arguments'] = json.dumps(deployment_args)
        else:
            items = [dry_run_arg]
            deployment_arg = {
                'items': items
            }
            kwargs['deployment_arguments'] = deployment_arg
    kwargs.pop('dry_run')
    ctx.invoke(devops_cli.create_deployment_create_deploy_pipeline_deployment_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.approve_deployment, params_to_exclude=['deploy_stage_id'])
@devops_cli.deployment_group.command(name=cli_util.override('devops_cli.approve_deployment.command_name', 'approve'), help=devops_cli.approve_deployment.help)
@cli_util.option('--stage-id', required=True, help=u"""The [OCID] of the stage which is marked for approval.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'Deployment'})
@cli_util.wrap_exceptions
def approve_deployment_extended(ctx, **kwargs):
    if 'stage_id' in kwargs:
        kwargs['deploy_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')
    ctx.invoke(devops_cli.approve_deployment, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_deployment_create_deploy_pipeline_redeployment_details, params_to_exclude=['deploy_pipeline_id'])
@devops_cli.deployment_group.command(name=cli_util.override('devops_cli.create_deployment_create_deploy_pipeline_redeployment_details.command_name', 'create-pipeline-redeployment'), help=devops_cli.create_deployment_create_deploy_pipeline_redeployment_details.help)
@cli_util.option('--deployment-id', required=True, help=u"""Pipeline Identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Deployment'})
@cli_util.wrap_exceptions
def create_deployment_create_deploy_pipeline_redeployment_details_extended(ctx, **kwargs):
    if 'deployment_id' in kwargs:
        kwargs['deploy_pipeline_id'] = kwargs['deployment_id']
        kwargs.pop('deployment_id')
    ctx.invoke(devops_cli.create_deployment_create_deploy_pipeline_redeployment_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.create_deployment_create_single_deploy_stage_deployment_details, params_to_exclude=['deploy_pipeline_id', 'deploy_stage_id', 'deploy_artifact_override_arguments', 'deploy_stage_override_arguments'])
@devops_cli.deployment_group.command(name=cli_util.override('devops_cli.create_deployment_create_single_deploy_stage_deployment_details.command_name', 'create-single-stage-deployment'), help=devops_cli.create_deployment_create_single_deploy_stage_deployment_details.help)
@cli_util.option('--stage-override-arguments', type=custom_types.CLI_COMPLEX_TYPE, help="""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--pipeline-id', required=True, help=u"""Pipeline Identifier""")
@cli_util.option('--stage-id', required=True, help=u"""The [OCID] of the stage which is marked for approval.""")
@cli_util.option('--artifact-override-arguments', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--dry-run', type=click.BOOL, help=u"""Set this flag to execute a dry run deployment. Only available for helm deployments as of now""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'deployment-arguments': {'module': 'devops', 'class': 'DeploymentArgumentCollection'}, 'stage-override-arguments': {'module': 'devops', 'class': 'DeployStageOverrideArgumentCollection'}, 'artifact-override-arguments': {'module': 'devops', 'class': 'DeployArtifactOverrideArgumentCollection'}}, output_type={'module': 'devops', 'class': 'Deployment'})
@cli_util.wrap_exceptions
def create_deployment_create_single_deploy_stage_deployment_details_extended(ctx, **kwargs):
    if 'stage_override_arguments' in kwargs:
        kwargs['deploy_stage_override_arguments'] = kwargs['stage_override_arguments']
        kwargs.pop('stage_override_arguments')
    if 'pipeline_id' in kwargs:
        kwargs['deploy_pipeline_id'] = kwargs['pipeline_id']
        kwargs.pop('pipeline_id')
    if 'stage_id' in kwargs:
        kwargs['deploy_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')
    if 'artifact_override_arguments' in kwargs:
        kwargs['deploy_artifact_override_arguments'] = kwargs['artifact_override_arguments']
        kwargs.pop('artifact_override_arguments')
    if kwargs['dry_run'] is not None:
        dry_run_arg = {
            'name': 'dry_run',
            'value': str(kwargs['dry_run'])
        }
        if kwargs['deployment_arguments'] is not None:
            deployment_args = cli_util.parse_json_parameter("deployment_arguments", kwargs['deployment_arguments'])
            deployment_args['items'].append(dry_run_arg)
            kwargs['deployment_arguments'] = json.dumps(deployment_args)
        else:
            items = [dry_run_arg]
            deployment_arg = {
                'items': items
            }
            kwargs['deployment_arguments'] = deployment_arg
    kwargs.pop('dry_run')
    ctx.invoke(devops_cli.create_deployment_create_single_deploy_stage_deployment_details, **kwargs)


# oci devops project project-summary list-projects -> oci devops project project-summary list
cli_util.rename_command(devops_cli, devops_cli.project_summary_group, devops_cli.list_projects, "list")


# Move commands under 'oci devops project project-summary' -> 'oci devops project'
devops_cli.devops_root_group.commands.pop(devops_cli.project_summary_group.name)
devops_cli.project_group.add_command(devops_cli.list_projects)


# oci devops work-request work-request-log-entry list-work-request-logs -> oci devops work-request work-request-log-entry list-logs
cli_util.rename_command(devops_cli, devops_cli.work_request_log_entry_group, devops_cli.list_work_request_logs, "list")


# Move commands under 'oci devops work-request work-request-log-entry' -> 'oci devops work-request work-request-log'
cli_util.rename_command(devops_cli, devops_cli.devops_root_group, devops_cli.work_request_log_entry_group, "work-request-log")


# oci devops repository put-repository-ref-put-repository-branch-details -> oci devops repository put-repository-ref-branch-details
cli_util.rename_command(devops_cli, devops_cli.repository_group, devops_cli.put_repository_ref_put_repository_branch_details, "put-repository-ref-branch-details")


# oci devops repository put-repository-ref-put-repository-tag-details -> oci devops repository put-repository-ref-tag-details
cli_util.rename_command(devops_cli, devops_cli.repository_group, devops_cli.put_repository_ref_put_repository_tag_details, "put-repository-ref-tag-details")


# Remove put-repository-ref from oci devops repository
devops_cli.repository_group.commands.pop(devops_cli.put_repository_ref.name)


# Move commands under 'oci devops repository-ref' -> 'oci devops repository'
devops_cli.devops_root_group.commands.pop(devops_cli.repository_ref_group.name)
devops_cli.repository_group.add_command(devops_cli.list_refs)


# Move commands under 'oci devops repository-object' -> 'oci devops repository'
devops_cli.devops_root_group.commands.pop(devops_cli.repository_object_group.name)
devops_cli.repository_group.add_command(devops_cli.get_object)


# Move commands under 'oci devops repository-commit' -> 'oci devops repository'
devops_cli.devops_root_group.commands.pop(devops_cli.repository_commit_group.name)
devops_cli.repository_group.add_command(devops_cli.list_commits)


@cli_util.copy_params_from_generated_command(devops_cli.delete_ref, params_to_exclude=['is_forced'])
@devops_cli.repository_group.command(name=devops_cli.delete_ref.name, help=devops_cli.delete_ref.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_ref_extended(ctx, **kwargs):

    ctx.invoke(devops_cli.delete_ref, **kwargs)


# oci devops connection create-connection-create-vbs-access-token-connection-details -> oci devops connection create-vbs-connection
cli_util.rename_command(devops_cli, devops_cli.connection_group, devops_cli.create_connection_create_vbs_access_token_connection_details, "create-vbs-connection")


# oci devops connection update-connection-update-vbs-access-token-connection-details -> oci devops connection update-vbs-connection
cli_util.rename_command(devops_cli, devops_cli.connection_group, devops_cli.update_connection_update_vbs_access_token_connection_details, "update-vbs-connection")


# oci devops trigger create-trigger-create-vbs-trigger-details -> oci devops trigger create-vbs-trigger
cli_util.rename_command(devops_cli, devops_cli.trigger_group, devops_cli.create_trigger_create_vbs_trigger_details, "create-vbs-trigger")


# oci devops trigger update-trigger-update-vbs-trigger-details -> oci devops trigger update-vbs-trigger
cli_util.rename_command(devops_cli, devops_cli.trigger_group, devops_cli.update_trigger_update_vbs_trigger_details, "update-vbs-trigger")

# oci devops project cancel-scheduled-cascading-project-deletion -> oci devops project cancel-cascading-delete
cli_util.rename_command(devops_cli, devops_cli.project_group, devops_cli.cancel_scheduled_cascading_project_deletion, "cancel-cascading-delete")

# oci devops project schedule-cascading-project-deletion -> oci devops project schedule-cascading-delete
cli_util.rename_command(devops_cli, devops_cli.project_group, devops_cli.schedule_cascading_project_deletion, "schedule-cascading-delete")

# oci devops deploy-stage create-deploy-stage-create-shell-deploy-stage-details -> oci devops deploy-stage create-shell-stage
cli_util.rename_command(devops_cli, devops_cli.deploy_stage_group, devops_cli.create_deploy_stage_create_shell_deploy_stage_details, "create-shell-stage")

# oci devops deploy-stage update-deploy-stage-update-shell-deploy-stage-details -> oci devops deploy-stage update-shell-stage
cli_util.rename_command(devops_cli, devops_cli.deploy_stage_group, devops_cli.update_deploy_stage_update_shell_deploy_stage_details, "update-shell-stage")


@cli_util.copy_params_from_generated_command(devops_cli.create_deploy_stage_create_shell_deploy_stage_details, params_to_exclude=['command_spec_deploy_artifact_id', 'deploy_stage_predecessor_collection', 'deploy_pipeline_id'])
@devops_cli.deploy_stage_group.command(name=devops_cli.create_deploy_stage_create_shell_deploy_stage_details.name, help=devops_cli.create_deploy_stage_create_shell_deploy_stage_details.help)
@cli_util.option('--command-spec-artifact-id', required=True, help=u"""The OCID of the artifact that contains the command specification. [required]""")
@cli_util.option('--stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--pipeline-id', required=True, help=u"""The OCID of a pipeline. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'container-config': {'module': 'devops', 'class': 'ContainerConfig'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_shell_deploy_stage_details_extended(ctx, **kwargs):

    if 'command_spec_artifact_id' in kwargs:
        kwargs['command_spec_deploy_artifact_id'] = kwargs['command_spec_artifact_id']
        kwargs.pop('command_spec_artifact_id')

    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')

    if 'pipeline_id' in kwargs:
        kwargs['deploy_pipeline_id'] = kwargs['pipeline_id']
        kwargs.pop('pipeline_id')

    ctx.invoke(devops_cli.create_deploy_stage_create_shell_deploy_stage_details, **kwargs)


@cli_util.copy_params_from_generated_command(devops_cli.update_deploy_stage_update_shell_deploy_stage_details, params_to_exclude=['command_spec_deploy_artifact_id', 'deploy_stage_id', 'deploy_stage_predecessor_collection'])
@devops_cli.deploy_stage_group.command(name=devops_cli.update_deploy_stage_update_shell_deploy_stage_details.name, help=devops_cli.update_deploy_stage_update_shell_deploy_stage_details.help)
@cli_util.option('--command-spec-artifact-id', help=u"""The OCID of the artifact that contains the command specification.""")
@cli_util.option('--stage-id', required=True, help=u"""Unique stage identifier. [required]""")
@cli_util.option('--stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'container-config': {'module': 'devops', 'class': 'ContainerConfig'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_shell_deploy_stage_details_extended(ctx, **kwargs):

    if 'command_spec_artifact_id' in kwargs:
        kwargs['command_spec_deploy_artifact_id'] = kwargs['command_spec_artifact_id']
        kwargs.pop('command_spec_artifact_id')

    if 'stage_id' in kwargs:
        kwargs['deploy_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')

    if 'stage_predecessor_collection' in kwargs:
        kwargs['deploy_stage_predecessor_collection'] = kwargs['stage_predecessor_collection']
        kwargs.pop('stage_predecessor_collection')

    ctx.invoke(devops_cli.update_deploy_stage_update_shell_deploy_stage_details, **kwargs)
