# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

import click
from services.key_management.src.oci_cli_kms_vault.generated import kmsvault_cli
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli.cli_util import get_param, copy_help_from_generated_code

# oci kms management vault backup-vault-backup-location-bucket
kmsvault_cli.vault_group.commands.pop(kmsvault_cli.backup_vault_backup_location_bucket.name)

# oci kms management vault backup-vault-backup-location-uri
kmsvault_cli.vault_group.commands.pop(kmsvault_cli.backup_vault_backup_location_uri.name)

# oci kms management vault restore-vault-from-object-store
kmsvault_cli.vault_group.commands.pop(kmsvault_cli.restore_vault_from_object_store.name)


# oci kms management vault restore-vault-from-object-store-backup-location-bucket
kmsvault_cli.vault_group.commands.pop(kmsvault_cli.restore_vault_from_object_store_backup_location_bucket.name)

# oci kms management vault restore-vault-from-object-store-backup-location-uri
kmsvault_cli.vault_group.commands.pop(kmsvault_cli.restore_vault_from_object_store_backup_location_uri.name)

# oci kms management vault restore-vault-from-file
kmsvault_cli.vault_group.commands.pop(kmsvault_cli.restore_vault_from_file.name)

vault_backup_params_from_generated = {
    'wait_for_state': get_param(kmsvault_cli.backup_vault_backup_location_bucket, 'wait_for_state'),
    'max_wait_seconds': get_param(kmsvault_cli.backup_vault_backup_location_bucket, 'max_wait_seconds'),
    'wait_interval_seconds': get_param(kmsvault_cli.backup_vault_backup_location_bucket, 'wait_interval_seconds'),
    'is_include_keys': get_param(kmsvault_cli.backup_vault_backup_location_bucket, 'is_include_keys')
}


@kmsvault_cli.vault_group.command(name=cli_util.override('kmsvault_cli.vault_backup_from_bucket_or_uri.command_name', 'backup'), help=kmsvault_cli.backup_vault_backup_location_bucket.help)
@cli_util.option('--vault-id', required=True, help=copy_help_from_generated_code(kmsvault_cli.backup_vault_backup_location_bucket, 'vault_id', remove_required=True))
@cli_util.option('--namespace', help=copy_help_from_generated_code(kmsvault_cli.backup_vault_backup_location_bucket, 'backup_location_namespace', remove_required=True))
@cli_util.option('--bucket-name', help=copy_help_from_generated_code(kmsvault_cli.backup_vault_backup_location_bucket, 'backup_location_bucket_name', remove_required=True))
@cli_util.option('--object-name', help=copy_help_from_generated_code(kmsvault_cli.backup_vault_backup_location_bucket, 'backup_location_object_name', remove_required=True))
@cli_util.option('--uri', help=copy_help_from_generated_code(kmsvault_cli.backup_vault_backup_location_uri, 'backup_location_uri', remove_required=True))
@cli_util.option('--if-match', help=copy_help_from_generated_code(kmsvault_cli.backup_vault_backup_location_bucket, 'if_match'))
@cli_util.option('--wait-for-state', type=vault_backup_params_from_generated['wait_for_state'].type, multiple=vault_backup_params_from_generated['wait_for_state'].multiple, help=vault_backup_params_from_generated['wait_for_state'].help)
@cli_util.option('--max-wait-seconds', type=vault_backup_params_from_generated['max_wait_seconds'].type, help=vault_backup_params_from_generated['max_wait_seconds'].help)
@cli_util.option('--wait-interval-seconds', type=vault_backup_params_from_generated['wait_interval_seconds'].type, help=vault_backup_params_from_generated['wait_interval_seconds'].help)
@cli_util.option('--is-include-keys', type=vault_backup_params_from_generated['is_include_keys'].type, help=vault_backup_params_from_generated['is_include_keys'].help)
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'Vault'})
@cli_util.wrap_exceptions
def vault_backup_from_bucket_or_uri(ctx, **kwargs):

    if kwargs['uri']:
        vault_backup_location_uri_kwargs = {
            'wait_for_state': kwargs['wait_for_state'],
            'max_wait_seconds': kwargs['max_wait_seconds'],
            'wait_interval_seconds': kwargs['wait_interval_seconds'],
            'vault_id': kwargs['vault_id'],
            'backup_location_uri': kwargs['uri'],
            'if_match': kwargs['if_match'],
            'is_include_keys': kwargs['is_include_keys']
        }
        ctx.invoke(kmsvault_cli.backup_vault_backup_location_uri,
                   **vault_backup_location_uri_kwargs)
    elif kwargs['bucket_name'] and kwargs['namespace'] and kwargs['object_name']:
        vault_backup_location_bucket_kwargs = {
            'wait_for_state': kwargs['wait_for_state'],
            'max_wait_seconds': kwargs['max_wait_seconds'],
            'wait_interval_seconds': kwargs['wait_interval_seconds'],
            'vault_id': kwargs['vault_id'],
            'backup_location_namespace': kwargs['namespace'],
            'backup_location_bucket_name': kwargs['bucket_name'],
            'if_match': kwargs['if_match'],
            'backup_location_object_name': kwargs['object_name'],
            'is_include_keys': kwargs['is_include_keys']
        }
        ctx.invoke(kmsvault_cli.backup_vault_backup_location_bucket,
                   **vault_backup_location_bucket_kwargs)
    else:
        raise click.UsageError('either --uri or all of (--bucket-name, --object-name and --namespace) must be provided.'
                               )


@kmsvault_cli.vault_group.command(name=cli_util.override('kmsvault_cli.vault_restore_from_bucket_or_uri.command_name', 'restore'), help=kmsvault_cli.restore_vault_from_object_store_backup_location_bucket.help)
@cli_util.option('--compartment-id', required=True, help=copy_help_from_generated_code(kmsvault_cli.restore_vault_from_object_store_backup_location_bucket, 'compartment_id', remove_required=True))
@cli_util.option('--namespace', help=copy_help_from_generated_code(kmsvault_cli.restore_vault_from_object_store_backup_location_bucket, 'backup_location_namespace', remove_required=True))
@cli_util.option('--bucket-name', help=copy_help_from_generated_code(kmsvault_cli.restore_vault_from_object_store_backup_location_bucket, 'backup_location_bucket_name', remove_required=True))
@cli_util.option('--object-name', help=copy_help_from_generated_code(kmsvault_cli.restore_vault_from_object_store_backup_location_bucket, 'backup_location_object_name', remove_required=True))
@cli_util.option('--uri', help=copy_help_from_generated_code(kmsvault_cli.restore_vault_from_object_store_backup_location_uri, 'backup_location_uri', remove_required=True))
@cli_util.option('--if-match', help=copy_help_from_generated_code(kmsvault_cli.restore_vault_from_object_store_backup_location_bucket, 'if_match'))
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'Vault'})
@cli_util.wrap_exceptions
def vault_restore_from_bucket_or_uri(ctx, **kwargs):

    if kwargs['uri']:
        vault_restore_location_uri_kwargs = {
            'compartment_id': kwargs['compartment_id'],
            'backup_location_uri': kwargs['uri'],
            'if_match': kwargs['if_match']
        }
        ctx.invoke(kmsvault_cli.restore_vault_from_object_store_backup_location_uri,
                   **vault_restore_location_uri_kwargs)
    elif kwargs['bucket_name'] and kwargs['namespace'] and kwargs['object_name']:
        vault_restore_location_bucket_kwargs = {
            'compartment_id': kwargs['compartment_id'],
            'backup_location_namespace': kwargs['namespace'],
            'backup_location_bucket_name': kwargs['bucket_name'],
            'if_match': kwargs['if_match'],
            'backup_location_object_name': kwargs['object_name']
        }
        ctx.invoke(kmsvault_cli.restore_vault_from_object_store_backup_location_bucket,
                   **vault_restore_location_bucket_kwargs)
    else:
        raise click.UsageError('either --uri or all of (--bucket-name, --object-name and --namespace) must be provided.'
                               )


@cli_util.copy_params_from_generated_command(kmsvault_cli.restore_vault_from_file, params_to_exclude=['restore_vault_from_file_details'])
@kmsvault_cli.vault_group.command(name=cli_util.override('kmsvault_cli.restore_from_file.command_name', 'restore-from-file'), help=kmsvault_cli.restore_vault_from_file.help)
@cli_util.option('--restore-vault-from-file-location', required=True, help=u"""The file location which contains the encrypted payload to upload to restore the vault.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'Vault'})
@cli_util.wrap_exceptions
def restore_from_file(ctx, **kwargs):

    # read file and send it's content

    file = kwargs['restore_vault_from_file_location']
    # Since the generated function expects the parameter name to be restore_vault_from_file_details
    del (kwargs['restore_vault_from_file_location'])
    try:
        with open(file, 'rb') as myfile:
            data = myfile.read()
            kwargs['restore_vault_from_file_details'] = data
        ctx.invoke(kmsvault_cli.restore_vault_from_file, **kwargs)
    except Exception:
        click.echo("Can't open the file")
