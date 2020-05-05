# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

import click
from services.key_management.src.oci_cli_kms_management.generated import kmsmanagement_cli
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli.cli_util import get_param, copy_help_from_generated_code


# oci kms management key backup-key-backup-location-bucket
kmsmanagement_cli.key_group.commands.pop(kmsmanagement_cli.backup_key_backup_location_bucket.name)

# oci kms management key backup-key-backup-location-uri
kmsmanagement_cli.key_group.commands.pop(kmsmanagement_cli.backup_key_backup_location_uri.name)

# oci kms management key restore-key-from-object-store
kmsmanagement_cli.key_group.commands.pop(kmsmanagement_cli.restore_key_from_object_store.name)

# oci kms management key restore-key-from-object-store-backup-location-bucket
kmsmanagement_cli.key_group.commands.pop(kmsmanagement_cli.restore_key_from_object_store_backup_location_bucket.name)

# oci kms management key restore-key-from-object-store-backup-location-uri
kmsmanagement_cli.key_group.commands.pop(kmsmanagement_cli.restore_key_from_object_store_backup_location_uri.name)

# oci kms management key restore-key-from-file
kmsmanagement_cli.key_group.commands.pop(kmsmanagement_cli.restore_key_from_file.name)

key_backup_params_from_generated = {
    'wait_for_state': get_param(kmsmanagement_cli.backup_key_backup_location_bucket, 'wait_for_state'),
    'max_wait_seconds': get_param(kmsmanagement_cli.backup_key_backup_location_bucket, 'max_wait_seconds'),
    'wait_interval_seconds': get_param(kmsmanagement_cli.backup_key_backup_location_bucket, 'wait_interval_seconds')
}


@kmsmanagement_cli.key_group.command(name=cli_util.override('kms_management.key_backup_from_bucket_or_uri.command_name', 'backup'), help=kmsmanagement_cli.backup_key_backup_location_bucket.help)
@cli_util.option('--key-id', required=True, help=copy_help_from_generated_code(kmsmanagement_cli.backup_key_backup_location_bucket, 'key_id', remove_required=True))
@cli_util.option('--namespace', help=copy_help_from_generated_code(kmsmanagement_cli.backup_key_backup_location_bucket, 'backup_location_namespace', remove_required=True))
@cli_util.option('--bucket-name', help=copy_help_from_generated_code(kmsmanagement_cli.backup_key_backup_location_bucket, 'backup_location_bucket_name', remove_required=True))
@cli_util.option('--object-name', help=copy_help_from_generated_code(kmsmanagement_cli.backup_key_backup_location_bucket, 'backup_location_object_name', remove_required=True))
@cli_util.option('--uri', help=copy_help_from_generated_code(kmsmanagement_cli.backup_key_backup_location_uri, 'backup_location_uri', remove_required=True))
@cli_util.option('--if-match', help=copy_help_from_generated_code(kmsmanagement_cli.backup_key_backup_location_bucket, 'if_match'))
@cli_util.option('--wait-for-state', type=key_backup_params_from_generated['wait_for_state'].type, multiple=key_backup_params_from_generated['wait_for_state'].multiple, help=key_backup_params_from_generated['wait_for_state'].help)
@cli_util.option('--max-wait-seconds', type=key_backup_params_from_generated['max_wait_seconds'].type, help=key_backup_params_from_generated['max_wait_seconds'].help)
@cli_util.option('--wait-interval-seconds', type=key_backup_params_from_generated['wait_interval_seconds'].type, help=key_backup_params_from_generated['wait_interval_seconds'].help)
@json_skeleton_utils.get_cli_json_input_option({'backup-location': {'module': 'key_management', 'class': 'BackupLocation'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backup-location': {'module': 'key_management', 'class': 'BackupLocation'}}, output_type={'module': 'key_management', 'class': 'Key'})
@cli_util.wrap_exceptions
def key_backup_from_bucket_or_uri(ctx, **kwargs):

    if kwargs['uri']:
        key_backup_location_uri_kwargs = {
            'wait_for_state': kwargs['wait_for_state'],
            'max_wait_seconds': kwargs['max_wait_seconds'],
            'wait_interval_seconds': kwargs['wait_interval_seconds'],
            'key_id': kwargs['key_id'],
            'backup_location_uri': kwargs['uri'],
            'if_match': kwargs['if_match']
        }
        ctx.invoke(kmsmanagement_cli.backup_key_backup_location_uri,
                   **key_backup_location_uri_kwargs)
    elif kwargs['bucket_name'] and kwargs['namespace'] and kwargs['object_name']:
        key_backup_location_bucket_kwargs = {
            'wait_for_state': kwargs['wait_for_state'],
            'max_wait_seconds': kwargs['max_wait_seconds'],
            'wait_interval_seconds': kwargs['wait_interval_seconds'],
            'key_id': kwargs['key_id'],
            'backup_location_namespace': kwargs['namespace'],
            'backup_location_bucket_name': kwargs['bucket_name'],
            'if_match': kwargs['if_match'],
            'backup_location_object_name': kwargs['object_name']
        }
        ctx.invoke(kmsmanagement_cli.backup_key_backup_location_bucket,
                   **key_backup_location_bucket_kwargs)
    else:
        raise click.UsageError('either --uri or all of (--bucket-name, --object-name and --namespace) must be provided.'
                               )


@kmsmanagement_cli.key_group.command(name=cli_util.override('kms_management.key_restore_from_bucket_or_uri.command_name', 'restore'), help=kmsmanagement_cli.restore_key_from_object_store_backup_location_bucket.help)
@cli_util.option('--namespace', help=copy_help_from_generated_code(kmsmanagement_cli.restore_key_from_object_store_backup_location_bucket, 'backup_location_namespace', remove_required=True))
@cli_util.option('--bucket-name', help=copy_help_from_generated_code(kmsmanagement_cli.restore_key_from_object_store_backup_location_bucket, 'backup_location_bucket_name', remove_required=True))
@cli_util.option('--object-name', help=copy_help_from_generated_code(kmsmanagement_cli.restore_key_from_object_store_backup_location_bucket, 'backup_location_object_name', remove_required=True))
@cli_util.option('--uri', help=copy_help_from_generated_code(kmsmanagement_cli.restore_key_from_object_store_backup_location_uri, 'backup_location_uri', remove_required=True))
@cli_util.option('--if-match', help=copy_help_from_generated_code(kmsmanagement_cli.restore_key_from_object_store_backup_location_bucket, 'if_match'))
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'Key'})
@cli_util.wrap_exceptions
def key_restore_from_bucket_or_uri(ctx, **kwargs):

    if kwargs['uri']:
        key_restore_location_uri_kwargs = {
            'backup_location_uri': kwargs['uri'],
            'if_match': kwargs['if_match']
        }
        ctx.invoke(kmsmanagement_cli.restore_key_from_object_store_backup_location_uri,
                   **key_restore_location_uri_kwargs)
    elif kwargs['bucket_name'] and kwargs['namespace'] and kwargs['object_name']:
        key_restore_location_bucket_kwargs = {
            'backup_location_namespace': kwargs['namespace'],
            'backup_location_bucket_name': kwargs['bucket_name'],
            'if_match': kwargs['if_match'],
            'backup_location_object_name': kwargs['object_name']
        }
        ctx.invoke(kmsmanagement_cli.restore_key_from_object_store_backup_location_bucket,
                   **key_restore_location_bucket_kwargs)
    else:
        raise click.UsageError('either --uri or all of (--bucket-name, --object-name and --namespace) must be provided.'
                               )


@cli_util.copy_params_from_generated_command(kmsmanagement_cli.restore_key_from_file, params_to_exclude=['restore_key_from_file_details'])
@kmsmanagement_cli.key_group.command(name=cli_util.override('kms_management.restore_from_file.command_name', 'restore-from-file'), help=kmsmanagement_cli.restore_key_from_file.help)
@cli_util.option('--restore-key-from-file-location', required=True, help=u"""The file location of the encrypted payload to upload to restore the key.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'key_management', 'class': 'Key'})
@cli_util.wrap_exceptions
def restore_from_file(ctx, **kwargs):

    # read file and send it's content
    file = kwargs['restore_key_from_file_location']

    # Since the generated function expects the parameter name to be restore_key_from_file_details
    del(kwargs['restore_key_from_file_location'])
    try:
        with open(file, 'r') as myfile:
            data = myfile.read()
            kwargs['restore_key_from_file_details'] = data
        ctx.invoke(kmsmanagement_cli.restore_key_from_file, **kwargs)
    except Exception:
        click.echo("Can't open the file")
