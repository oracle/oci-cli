# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
from services.artifacts.src.oci_cli_artifacts.generated import artifacts_cli
from oci_cli import cli_util, json_skeleton_utils
import click
from oci_cli.aliasing import CommandGroupWithAlias
from oci_cli import custom_types  # noqa: F401

import re
import json
import base64
import oci


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
artifacts_cli.container_image_signature_group.add_command(artifacts_cli.list_container_image_signatures)
cli_util.rename_command(artifacts_cli, artifacts_cli.container_image_signature_group, artifacts_cli.list_container_image_signatures, 'list')


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
def build_vault_crypto_client(ctx, key_id, region):
    split_list = re.split("ocid1\\.key\\.([\\w-]+)\\.([\\w-]+)\\.([\\w-]+)\\.([\\w]){60}", key_id)
    if len(split_list) < 4:
        raise click.ClickException("Failed to split key ocid. Please check the kms_key_id is correct.")
    vault_ext = split_list[3]
    realm = oci.regions.REGION_REALMS.get(region)
    second_level_domain = oci.regions.REALMS[realm]
    # region example: us-phoenix-1
    crypto_endpoint = "https://" + vault_ext + "-crypto.kms." + region + "." + second_level_domain
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
