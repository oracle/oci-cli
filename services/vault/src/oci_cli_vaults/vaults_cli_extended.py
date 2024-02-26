# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.vault.src.oci_cli_vaults.generated import vaults_cli
from oci_cli import cli_util
import click
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401


cli_util.rename_command(vaults_cli, vaults_cli.secret_group, vaults_cli.create_secret_base64_secret_content_details, "create-base64")
cli_util.rename_command(vaults_cli, vaults_cli.secret_group, vaults_cli.update_secret_base64_secret_content_details, "update-base64")
vaults_cli.secret_group.commands.pop(vaults_cli.create_secret.name)
cli_util.rename_command(vaults_cli, vaults_cli.secret_version_group, vaults_cli.schedule_secret_version_deletion, "schedule-deletion")
cli_util.rename_command(vaults_cli, vaults_cli.secret_version_group, vaults_cli.cancel_secret_version_deletion, "cancel-deletion")
vaults_cli.vault_root_group.help += " To retrieve secrets from vaults, see `Vault Service Secret Retrieval (secrets) <https://docs.cloud.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/secrets.html>"


@cli_util.copy_params_from_generated_command(vaults_cli.create_secret_base64_secret_content_details)
@vaults_cli.secret_group.command(name=vaults_cli.create_secret_base64_secret_content_details.name, help=vaults_cli.create_secret_base64_secret_content_details.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'vault', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'vault', 'class': 'dict(str, string)'}, 'metadata': {'module': 'vault', 'class': 'dict(str, object)'}, 'secret-rules': {'module': 'vault', 'class': 'list[SecretRule]'}, 'secret-generation-context': {'module': 'vault', 'class': 'SecretGenerationContext'}}, output_type={'module': 'vault', 'class': 'Secret'})
@cli_util.wrap_exceptions
def create_secret_base64_secret_content_details_extended(ctx, **kwargs):
    if not (kwargs.get('enable_auto_generation')):
        if not (kwargs.get('secret_content_content')):
            raise click.UsageError(
                'Must specify either --secret-content-content or set --enable-auto-generation to true.'
            )
    else:
        if kwargs.get('secret_content_content'):
            raise click.UsageError(
                'Cannot specify both --secret-content-content and set --enable-auto-generation to true at the same time'
            )
        if not (kwargs.get('secret_generation_context')):
            raise click.UsageError(
                'Must specify --secret-generation-context with --enable-auto-generation set to true.'
            )
    ctx.invoke(vaults_cli.create_secret_base64_secret_content_details, **kwargs)


# Remove create-secret-passphrase-generation-context from oci vault secret
vaults_cli.secret_group.commands.pop(vaults_cli.create_secret_passphrase_generation_context.name)


# Remove create-secret-bytes-generation-context from oci vault secret
vaults_cli.secret_group.commands.pop(vaults_cli.create_secret_bytes_generation_context.name)


# Remove create-secret-ssh-key-generation-context from oci vault secret
vaults_cli.secret_group.commands.pop(vaults_cli.create_secret_ssh_key_generation_context.name)


# Remove update-secret-passphrase-generation-context from oci vault secret
vaults_cli.secret_group.commands.pop(vaults_cli.update_secret_passphrase_generation_context.name)


# Remove update-secret-bytes-generation-context from oci vault secret
vaults_cli.secret_group.commands.pop(vaults_cli.update_secret_bytes_generation_context.name)


# Remove update-secret-ssh-key-generation-context from oci vault secret
vaults_cli.secret_group.commands.pop(vaults_cli.update_secret_ssh_key_generation_context.name)
