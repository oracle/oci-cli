# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
from services.artifacts.src.oci_cli_artifacts.generated import artifacts_cli
from oci_cli import cli_util, json_skeleton_utils
import click
from oci_cli.aliasing import CommandGroupWithAlias

# OCIR cli will follow the following format:
# oci artifacts <artifact-type> <resource> <action> <arguments>

# Add another level of group for the artifact-type container


@click.command('container', cls=CommandGroupWithAlias, help='Container registry.')
@cli_util.help_option_group
def container_group():
    pass


artifacts_cli.artifacts_root_group.add_command(container_group)

# ------------------------ oci artifacts container configuration ------------------------
# Rename group: oci artifacts container-configuration => oci artifacts container configuration
artifacts_cli.artifacts_root_group.commands.pop(artifacts_cli.container_configuration_group.name)
container_group.add_command(artifacts_cli.container_configuration_group)
cli_util.rename_command(artifacts_cli, container_group, artifacts_cli.container_configuration_group, 'configuration')

# ------------------------ oci artifacts container repository ------------------------
# Rename group: oci artifacts container-repository => oci artifacts container repository
artifacts_cli.artifacts_root_group.commands.pop(artifacts_cli.container_repository_group.name)
container_group.add_command(artifacts_cli.container_repository_group)
cli_util.rename_command(artifacts_cli, container_group, artifacts_cli.container_repository_group, 'repository')


# Suppress LifecycleState related arguments for update_container_repository: --wait-for-state, --max-wait-seconds,
# --wait-interval-seconds


@cli_util.copy_params_from_generated_command(artifacts_cli.update_container_repository,
                                             params_to_exclude=['wait_for_state', 'max_wait_seconds',
                                                                'wait_interval_seconds'])
@artifacts_cli.container_repository_group.command(
    name=cli_util.override('update_container_repository.command_name', 'update'),
    help=artifacts_cli.update_container_repository.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={'readme': {'module': 'artifacts', 'class': 'ContainerRepositoryReadme'}},
    output_type={'module': 'artifacts', 'class': 'ContainerRepository'})
@cli_util.wrap_exceptions
def update_container_repository_extended(ctx, **kwargs):
    ctx.invoke(artifacts_cli.update_container_repository, **kwargs)


# ------------------------ oci artifacts container image ------------------------
# Rename group: oci artifacts container-image => oci artifacts container image
artifacts_cli.artifacts_root_group.commands.pop(artifacts_cli.container_image_group.name)
container_group.add_command(artifacts_cli.container_image_group)
cli_util.rename_command(artifacts_cli, container_group, artifacts_cli.container_image_group, 'image')

# Rename command: oci artifacts container image remove => oci artifacts container image remove-version
cli_util.rename_command(artifacts_cli, artifacts_cli.container_image_group, artifacts_cli.remove_container_version,
                        "remove-version")


# Rename argument: oci artifacts container image remove-version --version-parameterconflict => oci artifacts
# container image remove-version --image-version Suppress LifecycleState related arguments for
# remove_container_version: --wait-for-state, --max-wait-seconds, --wait-interval-seconds


@cli_util.copy_params_from_generated_command(artifacts_cli.remove_container_version,
                                             params_to_exclude=['version_parameterconflict', 'wait_for_state',
                                                                'max_wait_seconds', 'wait_interval_seconds'])
@artifacts_cli.container_image_group.command(
    name=cli_util.override('remove_container_version.command_name', 'remove-version'),
    help=artifacts_cli.remove_container_version.help)
@cli_util.option('--image-version', help=cli_util.copy_help_from_generated_code(artifacts_cli.remove_container_version,
                                                                                'version_parameterconflict',
                                                                                remove_required=True), required=True)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={},
                                                      output_type={'module': 'artifacts', 'class': 'ContainerImage'})
@cli_util.wrap_exceptions
def remove_container_version_extended(ctx, **kwargs):
    if 'image_version' in kwargs:
        kwargs['version_parameterconflict'] = kwargs['image_version']
        kwargs.pop('image_version')
    ctx.invoke(artifacts_cli.remove_container_version, **kwargs)


# Rename argument: oci artifacts container image restore --version-parameterconflict
# => oci artifacts container image restore --image-version


@cli_util.copy_params_from_generated_command(artifacts_cli.restore_container_image,
                                             params_to_exclude=['version_parameterconflict'])
@artifacts_cli.container_image_group.command(name=cli_util.override('restore_container_image.command_name', 'restore'),
                                             help=artifacts_cli.restore_container_image.help)
@cli_util.option('--image-version', help=cli_util.copy_help_from_generated_code(artifacts_cli.restore_container_image,
                                                                                'version_parameterconflict'))
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={},
                                                      output_type={'module': 'artifacts', 'class': 'ContainerImage'})
@cli_util.wrap_exceptions
def restore_container_image_extended(ctx, **kwargs):
    if 'image_version' in kwargs:
        kwargs['version_parameterconflict'] = kwargs['image_version']
        kwargs.pop('image_version')
    ctx.invoke(artifacts_cli.restore_container_image, **kwargs)


# Move container_image_summary_group as a command under container_image_group:
# oci artifacts container-image-summary list-container-images => oci artifacts container image list


artifacts_cli.artifacts_root_group.commands.pop(artifacts_cli.container_image_summary_group.name)
artifacts_cli.container_image_group.add_command(artifacts_cli.list_container_images)
cli_util.rename_command(artifacts_cli, artifacts_cli.container_image_group, artifacts_cli.list_container_images, 'list')


# Rename argument: oci artifacts container image list --version-parameterconflict
# => oci artifacts container image list --image-version


@cli_util.copy_params_from_generated_command(artifacts_cli.list_container_images,
                                             params_to_exclude=['version_parameterconflict'])
@artifacts_cli.container_image_group.command(name=cli_util.override('list_container_images.command_name', 'list'),
                                             help=artifacts_cli.list_container_images.help)
@cli_util.option('--image-version', help=cli_util.copy_help_from_generated_code(artifacts_cli.list_container_images,
                                                                                'version_parameterconflict'))
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'artifacts',
                                                                                                     'class': 'ContainerImageCollection'})
@cli_util.wrap_exceptions
def list_container_images_extended(ctx, **kwargs):
    if 'image_version' in kwargs:
        kwargs['version_parameterconflict'] = kwargs['image_version']
        kwargs.pop('image_version')
    ctx.invoke(artifacts_cli.list_container_images, **kwargs)
