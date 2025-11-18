# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
from services.artifacts.src.oci_cli_artifacts.generated import artifacts_cli
from services.generic_artifacts_content.src.oci_cli_generic_artifacts_content.generated import genericartifactscontent_cli
from oci_cli import cli_util, json_skeleton_utils
import click
from oci_cli.aliasing import CommandGroupWithAlias
from oci_cli import custom_types  # noqa: F401

import re
import json
import base64
import oci


artifacts_cli.artifacts_root_group.commands.pop(artifacts_cli.generic_artifact_group.name)


# oci artifacts generic-artifact -> oci artifacts generic artifact
@click.command('generic', cls=CommandGroupWithAlias, help='Generic metadata.')
@cli_util.help_option_group
def generic_group():
    pass


@cli_util.copy_params_from_generated_command(genericartifactscontent_cli.get_generic_artifact_content_by_path, params_to_exclude=['version_parameterconflict'])
@artifacts_cli.generic_artifact_group.command(name='download-by-path', help=genericartifactscontent_cli.get_generic_artifact_content_by_path.help)
@cli_util.option('--artifact-version', required=True, help=u"""The generic artifact version.

Example: `1.1.2`""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_generic_artifact_content_by_path_extended(ctx, **kwargs):
    if 'artifact_version' in kwargs:
        kwargs['version_parameterconflict'] = kwargs['artifact_version']
        kwargs.pop('artifact_version')
    ctx.invoke(genericartifactscontent_cli.get_generic_artifact_content_by_path, **kwargs)


@cli_util.copy_params_from_generated_command(genericartifactscontent_cli.put_generic_artifact_content_by_path, params_to_exclude=['version_parameterconflict', 'generic_artifact_content_body'])
@artifacts_cli.generic_artifact_group.command(name='upload-by-path', help=genericartifactscontent_cli.put_generic_artifact_content_by_path.help)
@cli_util.option('--artifact-version', required=True, help=u"""The generic artifact version.

Example: `1.1.2`""")
@cli_util.option('--content-body', required=True, help=u"""Put generic artifact content file. Example: --content-body /Users/me/myfile.txt""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'generic_artifacts_content', 'class': 'GenericArtifact'})
@cli_util.wrap_exceptions
def put_generic_artifact_content_by_path_extended(ctx, **kwargs):
    if 'artifact_version' in kwargs:
        kwargs['version_parameterconflict'] = kwargs['artifact_version']
        kwargs.pop('artifact_version')

    upload_file = kwargs['content_body']
    kwargs.pop('content_body')
    with open(upload_file, 'rb') as ufile:
        kwargs['generic_artifact_content_body'] = ufile
        ctx.invoke(genericartifactscontent_cli.put_generic_artifact_content_by_path, **kwargs)


# oci artifacts generic artifact XX-generic-artifact-by-path -> XX-by-path
@cli_util.copy_params_from_generated_command(artifacts_cli.delete_generic_artifact_by_path, params_to_exclude=['version_parameterconflict'])
@artifacts_cli.generic_artifact_group.command(name=cli_util.override('delete_generic_artifact_by_path.command_name', 'delete-by-path'), help=artifacts_cli.delete_generic_artifact_by_path.help)
@cli_util.option('--artifact-version', required=True, help=u"""The generic artifact version.

Example: `1.1.2`""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_generic_artifact_by_path_extended(ctx, **kwargs):
    if 'artifact_version' in kwargs:
        kwargs['version_parameterconflict'] = kwargs['artifact_version']
        kwargs.pop('artifact_version')
    ctx.invoke(artifacts_cli.delete_generic_artifact_by_path, **kwargs)


@cli_util.copy_params_from_generated_command(artifacts_cli.get_generic_artifact_by_path, params_to_exclude=['version_parameterconflict'])
@artifacts_cli.generic_artifact_group.command(name=cli_util.override('get_generic_artifact_by_path.command_name', 'get-by-path'), help=artifacts_cli.get_generic_artifact_by_path.help)
@cli_util.option('--artifact-version', required=True, help=u"""The generic artifact version.

Example: `1.1.2`""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'artifacts', 'class': 'GenericArtifact'})
@cli_util.wrap_exceptions
def get_generic_artifact_by_path_extended(ctx, **kwargs):
    if 'artifact_version' in kwargs:
        kwargs['version_parameterconflict'] = kwargs['artifact_version']
        kwargs.pop('artifact_version')
    ctx.invoke(artifacts_cli.get_generic_artifact_by_path, **kwargs)


@cli_util.copy_params_from_generated_command(artifacts_cli.update_generic_artifact_by_path, params_to_exclude=['version_parameterconflict'])
@artifacts_cli.generic_artifact_group.command(name=cli_util.override('update_generic_artifact_by_path.command_name', 'update-by-path'), help=artifacts_cli.update_generic_artifact_by_path.help)
@cli_util.option('--artifact-version', required=True, help=u"""The generic artifact version.

Example: `1.1.2`""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'artifacts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'artifacts', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'artifacts', 'class': 'GenericArtifact'})
@cli_util.wrap_exceptions
def update_generic_artifact_by_path_extended(ctx, **kwargs):
    if 'artifact_version' in kwargs:
        kwargs['version_parameterconflict'] = kwargs['artifact_version']
        kwargs.pop('artifact_version')
    ctx.invoke(artifacts_cli.update_generic_artifact_by_path, **kwargs)


artifacts_cli.artifacts_root_group.add_command(generic_group)
cli_util.rename_command(artifacts_cli, generic_group, artifacts_cli.generic_artifact_group, 'artifact')
cli_util.rename_command(artifacts_cli, artifacts_cli.generic_artifact_group, genericartifactscontent_cli.get_generic_artifact_content, 'download')
artifacts_cli.generic_artifact_group.commands.pop(artifacts_cli.update_generic_artifact_by_path.name)
artifacts_cli.generic_artifact_group.commands.pop(artifacts_cli.get_generic_artifact_by_path.name)
artifacts_cli.generic_artifact_group.commands.pop(artifacts_cli.delete_generic_artifact_by_path.name)


cli_util.rename_command(artifacts_cli, artifacts_cli.repository_group, artifacts_cli.update_repository_update_generic_repository_details, 'update-generic-repository')
cli_util.rename_command(artifacts_cli, artifacts_cli.repository_group, artifacts_cli.create_repository_create_generic_repository_details, 'create-generic-repository')


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
    input_params_to_complex_types={'readme': {'module': 'artifacts', 'class': 'ContainerRepositoryReadme'}, 'freeform-tags': {'module': 'artifacts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'artifacts', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'artifacts', 'class': 'ContainerRepository'})
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

# ------------------------ oci artifacts container image-signature ------------------------
# Rename group: oci artifacts container-image-signature => oci artifacts container image-signature
artifacts_cli.artifacts_root_group.commands.pop(artifacts_cli.container_image_signature_group.name)
container_group.add_command(artifacts_cli.container_image_signature_group)
cli_util.rename_command(artifacts_cli, container_group, artifacts_cli.container_image_signature_group, 'image-signature')


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

# Move container_image_signature_summary_group as a command under container_image_signature_group:
# oci artifacts container-image-signature-summary list-container-image-signatures => oci artifacts container image-signature list


artifacts_cli.artifacts_root_group.commands.pop(artifacts_cli.container_image_signature_summary_group.name)
# artifacts_cli.container_image_signature_group.add_command(artifacts_cli.list_container_image_signatures)
# cli_util.rename_command(artifacts_cli, artifacts_cli.container_image_signature_group, artifacts_cli.list_container_image_signatures, 'list')


# Using list_call_get_all_results_multiple_keys
@cli_util.copy_params_from_generated_command(artifacts_cli.list_container_image_signatures)
@artifacts_cli.container_image_signature_group.command(name=cli_util.override('list_container_image_signatures.command_name', 'list'), help=artifacts_cli.list_container_image_signatures.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'artifacts', 'class': 'ContainerImageSignatureCollection'})
@cli_util.wrap_exceptions
def list_container_image_signatures_extended(ctx, from_json, all_pages, page_size, compartment_id, compartment_id_in_subtree, image_id, repository_id, repository_name, image_digest, display_name, kms_key_id, kms_key_version_id, signing_algorithm, limit, page, sort_by, sort_order):
    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    if image_id is not None:
        kwargs['image_id'] = image_id
    if repository_id is not None:
        kwargs['repository_id'] = repository_id
    if repository_name is not None:
        kwargs['repository_name'] = repository_name
    if image_digest is not None:
        kwargs['image_digest'] = image_digest
    if display_name is not None:
        kwargs['display_name'] = display_name
    if kms_key_id is not None:
        kwargs['kms_key_id'] = kms_key_id
    if kms_key_version_id is not None:
        kwargs['kms_key_version_id'] = kms_key_version_id
    if signing_algorithm is not None:
        kwargs['signing_algorithm'] = signing_algorithm
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results_multiple_keys(
            client.list_container_image_signatures,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit_multiple_keys(
            client.list_container_image_signatures,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_container_image_signatures(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


# Using list_call_get_all_results_multiple_keys
@cli_util.copy_params_from_generated_command(artifacts_cli.list_repositories)
@artifacts_cli.repository_group.command(name=cli_util.override('list_repositories.command_name', 'list'), help=artifacts_cli.list_repositories.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'artifacts', 'class': 'RepositoryCollection'})
@cli_util.wrap_exceptions
def list_repositories_extended(ctx, from_json, all_pages, page_size, compartment_id, id, display_name, is_immutable, lifecycle_state, limit, page, sort_by, sort_order):
    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if is_immutable is not None:
        kwargs['is_immutable'] = is_immutable
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results_multiple_keys(
            client.list_repositories,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit_multiple_keys(
            client.list_repositories,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_repositories(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


# Using list_call_get_all_results_multiple_keys
@cli_util.copy_params_from_generated_command(artifacts_cli.list_generic_artifacts, params_to_exclude=['version_parameterconflict'])
@artifacts_cli.generic_artifact_group.command(name=cli_util.override('list_generic_artifacts.command_name', 'list'), help=artifacts_cli.list_generic_artifacts.help)
@cli_util.option('--artifact-version', help=u"""The generic artifact version.

Example: `1.1.2`""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'artifacts', 'class': 'GenericArtifactCollection'})
@cli_util.wrap_exceptions
def list_generic_artifacts_extended(ctx, from_json, all_pages, page_size, compartment_id, repository_id, id, display_name, artifact_path, artifact_version, sha256, lifecycle_state, limit, page, sort_by, sort_order):
    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if artifact_path is not None:
        kwargs['artifact_path'] = artifact_path
    if artifact_version is not None:
        kwargs['version'] = artifact_version
    if sha256 is not None:
        kwargs['sha256'] = sha256
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results_multiple_keys(
            client.list_generic_artifacts,
            compartment_id=compartment_id,
            repository_id=repository_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit_multiple_keys(
            client.list_generic_artifacts,
            limit,
            page_size,
            compartment_id=compartment_id,
            repository_id=repository_id,
            **kwargs
        )
    else:
        result = client.list_generic_artifacts(
            compartment_id=compartment_id,
            repository_id=repository_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


# Using list_call_get_all_results_multiple_keys
@cli_util.copy_params_from_generated_command(artifacts_cli.list_container_repositories,)
@artifacts_cli.container_repository_group.command(name=cli_util.override('list_container_repositories.command_name', 'list'), help=artifacts_cli.list_container_repositories.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'artifacts', 'class': 'ContainerRepositoryCollection'})
@cli_util.wrap_exceptions
def list_container_repositories_extended(ctx, from_json, all_pages, page_size, compartment_id, compartment_id_in_subtree, repository_id, display_name, is_public, lifecycle_state, limit, page, sort_by, sort_order):
    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    if repository_id is not None:
        kwargs['repository_id'] = repository_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if is_public is not None:
        kwargs['is_public'] = is_public
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results_multiple_keys(
            client.list_container_repositories,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit_multiple_keys(
            client.list_container_repositories,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_container_repositories(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


# Rename argument: oci artifacts container image list --version-parameterconflict
# => oci artifacts container image list --image-version
# Using list_call_get_all_results_multiple_keys
@cli_util.copy_params_from_generated_command(artifacts_cli.list_container_images, params_to_exclude=['version_parameterconflict'])
@artifacts_cli.container_image_group.command(name=cli_util.override('list_container_images.command_name', 'list'), help=artifacts_cli.list_container_images.help)
@cli_util.option('--image-version', help=u"""A filter to return container images that match the version.

Example: `foo` or `foo*`""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'artifacts',
                                                                                                     'class': 'ContainerImageCollection'})
@cli_util.wrap_exceptions
def list_container_images_extended(ctx, from_json, all_pages, page_size, compartment_id, compartment_id_in_subtree, display_name, image_id, is_versioned, repository_id, repository_name, lifecycle_state, limit, page, sort_by, sort_order, **kwargs):
    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if 'image_version' in kwargs:
        kwargs['version'] = kwargs['image_version']
        kwargs.pop('image_version')
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    if display_name is not None:
        kwargs['display_name'] = display_name
    if image_id is not None:
        kwargs['image_id'] = image_id
    if is_versioned is not None:
        kwargs['is_versioned'] = is_versioned
    if repository_id is not None:
        kwargs['repository_id'] = repository_id
    if repository_name is not None:
        kwargs['repository_name'] = repository_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results_multiple_keys(
            client.list_container_images,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit_multiple_keys(
            client.list_container_images,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_container_images(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@artifacts_cli.container_image_signature_group.command(name='sign-upload', help=u"""Sign a container image metadata and upload the signature. \n[Command Reference](SignAndUploadContainerImageSignatureMetadata)""")
@cli_util.option('--kms-key-id', required=True, help=u"""The [OCID] of the kmsKeyId used to sign the container image.""")
@cli_util.option('--kms-key-version-id', required=True, help=u"""The [OCID] of the kmsKeyVersionId used to sign the container image.""")
@cli_util.option('--signing-algorithm', required=True, type=custom_types.CliCaseInsensitiveChoice(["SHA_224_RSA_PKCS_PSS", "SHA_256_RSA_PKCS_PSS", "SHA_384_RSA_PKCS_PSS", "SHA_512_RSA_PKCS_PSS"]), help=u"""The algorithm to be used for signing. These are the only supported signing algorithms for container images.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which the container repository exists.""")
@cli_util.option('--image-id', required=True, help=u"""The [OCID] of the container image.""")
@cli_util.option('--description', help="""The optional text of your choice to describe the image. The description is included as part of the signature, and is shown in the Console. For example, --description "Image for UAT testing" """)
@cli_util.option('--metadata', help="""The optional information of your choice about the image, in a valid JSON format (alphanumeric characters only, with no whitespace or escape characters). For example, --metadata "{\"buildNumber\":\"123\"}" """)
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def sign_and_upload_container_image_signature_metadata(ctx, from_json, kms_key_id, kms_key_version_id,
                                                       signing_algorithm,
                                                       compartment_id, image_id,
                                                       description, metadata):
    """
    SignAndUploadContainerImageSignatureMetadata calls KMS to sign the message then calls OCIR to upload the returned signature

    :param ctx: Context
    :param kms_key_id: The OCID of the kmsKeyId used to sign the container image. eg) ocid1.key.oc1..exampleuniqueID. Max length: 255, Min length:1
    :param kms_key_version_id: The OCID of the kmsKeyVersionId used to sign the container image. eg) ocid1.keyversion.oc1..exampleuniqueID. Max length: 255, Min length:1
    :param signing_algorithm: The algorithm to be used for signing. These are the only supported signing algorithms for container images.
    - SHA_224_RSA_PKCS_PSS
    - SHA_256_RSA_PKCS_PSS
    - SHA_384_RSA_PKCS_PSS
    - SHA_512_RSA_PKCS_PSS
    :param compartment_id: The OCID of the compartment in which the container repository exists. eg) ocid1.compartment.oc1..exampleuniqueID. Max length: 100, Min length: 1
    :param image_id: The OCID of the container image. eg) ocid1.containerimage.oc1..exampleuniqueID. Max length: 255, Min length:1
    :param description: An user inputted message.
    :param metadata:  An user defined information about the container image in JSON format eg) {"buildNumber":"123"}
    restriction:
    - should only contains alphanumeric key strings.
    - should be alphabetically sorted.
    - should not have whitespaces or escape characters.
    :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.artifacts.models.ContainerImageSignature`
    """

    if description is None:
        description = ""

    if metadata is None:
        metadata = ""
    else:
        try:
            json.loads(metadata)
        except ValueError as e:
            raise Exception("Metadata should be in valid json format (alphanumeric characters only, with no whitespace or escape characters).")

    signing_algo_kms = signing_algorithm
    signing_algo_ocir = signing_algorithm

    region_name = get_region_from_config(ctx)

    # Create KMS client
    kms_crypto_client = build_vault_crypto_client(ctx, kms_key_id, region_name)

    # Get container image metadata
    click.echo("Obtaining container image metadata by the image ID")
    artifacts_client, container_image_metadata = get_container_image_metadata(ctx, image_id, region_name)

    # Generate message
    message = {
        "description": description,
        "imageDigest": container_image_metadata.digest,
        "kmsKeyId": kms_key_id,
        "kmsKeyVersionId": kms_key_version_id,
        "metadata": metadata,
        "region": region_name,
        "repositoryName": container_image_metadata.repository_name,
        "signingAlgorithm": signing_algorithm
    }
    json_string = json.dumps(message, separators=(',', ':'))
    encoded_json = base64.b64encode(json_string.encode()).decode()

    # Sign image digest
    click.echo("Generating signature")
    signed_data = sign_container_image(
        kms_crypto_client, encoded_json, kms_key_id, kms_key_version_id, signing_algo_kms)
    click.echo("Signature: " + signed_data.signature)

    # Upload signature metadata
    click.echo("Uploading signature")
    container_image_signature_uploaded = upload_signature_metadata(ctx, artifacts_client, compartment_id,
                                                                   image_id, kms_key_id, kms_key_version_id,
                                                                   signing_algo_ocir,
                                                                   encoded_json, signed_data.signature)
    click.echo("Uploaded signature: " + container_image_signature_uploaded.data.signature + "\nMessage: " + container_image_signature_uploaded.data.message + "\nID: " + container_image_signature_uploaded.data.id)
    cli_util.render_response(container_image_signature_uploaded, ctx)


@artifacts_cli.container_image_signature_group.command(name='get-verify', help=u"""Fetch a container image signature metadata and verity the signature. \n[Command Reference](GetAndVerifyImageSignatureMetadata)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which the container repository exists.""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""When set to true, the hierarchy of compartments is traversed""")
@cli_util.option('--repo-name', required=True, help=u"""The repository name in which the container image exists eg) busybox""")
@cli_util.option('--image-digest', required=True, help=u"""The digest of the container image.""")
@cli_util.option('--trusted-keys', required=True, multiple=True, help=u"""List of OCIDs of the kmsKeyId used to sign the container image.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_and_verify_image_signature_metadata(ctx, from_json, compartment_id, compartment_id_in_subtree,
                                            repo_name, image_digest, trusted_keys):
    """
    GetAndVerifyImageSignatureMetadata calls OCIR to list all the signatures satisfying the user provided criterion then
    calls KMS to verify the returned signatures

    :param ctx: Context
    :param compartment_id: The git OCID of the compartment in which the container repository exists. eg) ocid1.compartment.oc1..exampleuniqueID. MAX length: 100, MIN length 1
    :param compartment_id_in_subtree: When set to true, the hierarchy of compartments is traversed
    :param repo_name: The repository name in which the container image exists eg) busybox
    :param image_digest: The sha256 digest of the docker image. eg) sha256:12345
    :param trusted_keys: List of OCIDs of the kmsKeyId used to sign the container image.
    :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.key_management.models.VerifiedData`
    """
    region_name = get_region_from_config(ctx)
    artifacts_client = cli_util.build_client("artifacts", "artifacts", ctx)

    result = get_and_verify_image_signature_metadata_helper(ctx, artifacts_client, region_name, compartment_id, compartment_id_in_subtree, repo_name, image_digest, trusted_keys, None)

    cli_util.render_response(result, ctx)


def get_and_verify_image_signature_metadata_helper(ctx, artifacts_client, region_name, compartment_id, compartment_id_in_subtree,
                                                   repository_name, image_digest, trusted_keys, page):

    click.echo("Fetching signatures")
    signature_collection, next_page = list_container_image_signatures_with_repo_path(
        artifacts_client, compartment_id, compartment_id_in_subtree, repository_name, image_digest, page)

    # Filter out the keys
    container_image_signature_summaries = filter_item_by_trusted_keys(signature_collection.items, trusted_keys)
    if len(container_image_signature_summaries) == 0:
        raise Exception("No signature in the image was signed by the supplied trusted keys")
    num = len(signature_collection.items) - len(container_image_signature_summaries)
    click.echo("Filtered out " + str(num) + " signatures by the trusted keys")

    # Verify signature
    click.echo("Verifying signature")
    verified = verify_signatures(ctx, container_image_signature_summaries, region_name)
    if verified.data.is_signature_valid is False and next_page is not None:
        return get_and_verify_image_signature_metadata_helper(ctx, artifacts_client, region_name, compartment_id,
                                                              compartment_id_in_subtree,
                                                              repository_name,
                                                              image_digest,
                                                              trusted_keys,
                                                              next_page)
    return verified


def sign_container_image(kms_crypto_client, message, key_id, key_version_id, signing_algorithm):
    sign_data_details = {
        "message": message,
        "keyId": key_id,
        "keyVersionId": key_version_id,
        "signingAlgorithm": signing_algorithm,
        "messageType": "RAW"
    }

    response = kms_crypto_client.sign(
        sign_data_details
    )

    return response.data


def upload_signature_metadata(ctx, artifacts_client, compartment_id, image_id, key_id, key_version_id, signing_algorithm,
                              message, signature):
    create_container_image_signature_details = {
        "compartmentId": compartment_id,
        "imageId": image_id,
        "kmsKeyId": key_id,
        "kmsKeyVersionId": key_version_id,
        "message": message,
        "signature": signature,
        "signingAlgorithm": signing_algorithm
    }

    response = artifacts_client.create_container_image_signature(
        create_container_image_signature_details
    )

    if response.status != 200:
        raise click.ClickException("Failed to upload the signature to OCI Registry. Status code: " + response.status)
    return response


# Build the KmsCryptoClient based on the vault extension OCID in the keyId
# OCI public endpoint is not available for KMS endpoint for the regions below
# https://confluence.oraclecorp.com/confluence/display/KMS/KMS+Vault+Endpoints+FAQ#KMSVaultEndpointsFAQ-Whichendpointsuse.oci
regions_without_oci = [
    'us-ashburn-1', 'us-phoenix-1', 'us-seattle-1', 'eu-frankfurt-1', 'uk-london-1',
    'ap-melbourne-1', 'ap-mumbai-1', 'ap-osaka-1', 'ap-seoul-1', 'ap-sydney-1',
    'ap-tokyo-1', 'eu-amsterdam-1', 'eu-zurich-1', 'ca-montreal-1', 'ca-toronto-1',
    'me-jeddah-1', 'sa-saopaulo-1', 'us-luke-1', 'us-langley-1', 'us-gov-ashburn-1',
    'us-gov-chicago-1', 'us-gov-phoenix-1', 'uk-gov-london-1', 'us-seattle-1'
]


def build_vault_crypto_client(ctx, key_id, region):
    split_list = re.split("ocid1\\.key\\.([\\w-]+)\\.([\\w-]+)\\.([\\w-]+)\\.([\\w]){60}", key_id)
    if len(split_list) < 4:
        raise click.ClickException("Failed to split key ocid. Please check the kms_key_id is correct.")
    vault_ext = split_list[3]
    realm = oci.regions.REGION_REALMS.get(region)
    second_level_domain = oci.regions.REALMS[realm]
    # region example: us-phoenix-1
    if region in regions_without_oci:
        crypto_endpoint = f"https://{vault_ext}-crypto.kms.{region}.{second_level_domain}"
    else:
        crypto_endpoint = f"https://{vault_ext}-crypto.kms.{region}.oci.{second_level_domain}"
    ctx.obj['endpoint'] = crypto_endpoint

    # Build kms_crypto client
    kms_crypto_client = cli_util.build_client("key_management", "kms_crypto", ctx)
    return kms_crypto_client


def list_container_image_signatures_with_repo_path(artifacts_client, compartment_id, compartment_id_in_subtree,
                                                   repository_name, image_digest, page):
    # compartmentIdInSubtree is currently only supported for the root tenancy
    response = artifacts_client.list_container_image_signatures(
        compartment_id=compartment_id,
        compartment_id_in_subtree=compartment_id_in_subtree,
        repository_name=repository_name,
        image_digest=image_digest,
        page=page)

    if response.status != 200:
        raise Exception("Failed to list the signatures of repository_name %s, image_digest %s, status_code %d",
                        repository_name, image_digest, response.status)
    return response.data, response.next_page


def is_trusted_key(key, trusted_keys):
    for k in trusted_keys:
        if k == key:
            return True
    return False


def filter_item_by_trusted_keys(items, trusted_keys):
    ret = []
    for item in items:
        if is_trusted_key(item.kms_key_id, trusted_keys):
            ret.append(item)
    return ret


def verify_signatures(ctx, container_image_signature_summary, region_name):
    verified = None
    for signature_summary in container_image_signature_summary:
        vault_crypto_client = build_vault_crypto_client(ctx, signature_summary.kms_key_id, region_name)
        algo = signature_summary.signing_algorithm
        signing_algo_list = [
            "SHA_224_RSA_PKCS_PSS", "SHA_256_RSA_PKCS_PSS", "SHA_384_RSA_PKCS_PSS", "SHA_512_RSA_PKCS_PSS"
        ]
        if algo not in signing_algo_list:
            raise click.BadParameter("The signing algorithm is not valid. Please check.")
        verified = verify_signature(
            vault_crypto_client,
            signature_summary.message,
            signature_summary.signature,
            signature_summary.kms_key_id,
            signature_summary.kms_key_version_id,
            algo
        )
        if verified.data.is_signature_valid is True:
            return verified

    return verified


def verify_signature(kms_crypto_client, message, signature, key_id, key_version_id, signing_algorithm):
    verify_data_details = {
        "keyId": key_id,
        "keyVersionId": key_version_id,
        "signingAlgorithm": signing_algorithm,
        "message": message,
        "signature": signature
    }
    return kms_crypto_client.verify(verify_data_details)


def get_region_from_config(ctx):
    client_config = None
    try:
        client_config = cli_util.build_config(ctx.obj)
        if 'region' not in client_config:
            return None
    except Exception:
        return None
    return client_config['region']


def get_container_image_metadata(ctx, image_id, region):
    # Set endpoint
    realm = oci.regions.REGION_REALMS.get(region)
    second_level_domain = oci.regions.REALMS[realm]
    ctx.obj['endpoint'] = "https://artifacts." + region + ".oci." + second_level_domain
    artifacts_client = cli_util.build_client("artifacts", "artifacts", ctx)
    container_image_response = artifacts_client.get_container_image(image_id)
    return artifacts_client, container_image_response.data


# oci artifacts container image lookup-container-image-by-uri -> oci artifacts container image lookup
cli_util.rename_command(artifacts_cli, artifacts_cli.container_image_group, artifacts_cli.lookup_container_image_by_uri, "lookup")
