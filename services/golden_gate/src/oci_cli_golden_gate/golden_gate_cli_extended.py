# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates. All rights reserved.

import click
import json  # noqa: F401
import oci  # noqa: F401
from services.golden_gate.src.oci_cli_golden_gate.generated import goldengate_cli

from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import custom_types  # noqa: F401
from oci_cli import cli_exceptions  # noqa: F401
from oci_cli import json_skeleton_utils

# Fixup deployment start to use default start
cli_util.rename_command(goldengate_cli,
                        goldengate_cli.deployment_group,
                        goldengate_cli.start_deployment_default_start_deployment_details,
                        goldengate_cli.start_deployment.name)

# Fixup deployment stop to use default stop
cli_util.rename_command(goldengate_cli,
                        goldengate_cli.deployment_group,
                        goldengate_cli.stop_deployment_default_stop_deployment_details,
                        goldengate_cli.stop_deployment.name)

# Fixup deployment upgrade to use current release upgrade
cli_util.rename_command(goldengate_cli,
                        goldengate_cli.deployment_group,
                        goldengate_cli.upgrade_deployment_upgrade_deployment_current_release_details,
                        goldengate_cli.upgrade_deployment.name)

# Fixup deployment-backup restore to use default restore
cli_util.rename_command(goldengate_cli,
                        goldengate_cli.deployment_backup_group,
                        goldengate_cli.restore_deployment_default_restore_deployment_details,
                        goldengate_cli.restore_deployment.name)

# Fixup list-work-request-logs to use list
cli_util.rename_command(goldengate_cli,
                        goldengate_cli.work_request_log_entry_group,
                        goldengate_cli.list_work_request_logs,
                        'list')

# from oci goldengate deployment create <blah> -ogg-data <json>
# to   oci goldengate deployment create <blah>
#                 --deployment-name <text>
#                 --admin-username <text>
#                 [--admin-password <text>]
#                 --certificate-file <file>
#                 --private-key-file <file>


@cli_util.copy_params_from_generated_command(goldengate_cli.create_deployment,
                                             params_to_exclude=['deployment_type', 'ogg_data'],
                                             copy_from_json=False)
@goldengate_cli.deployment_group.command(name='create', help=goldengate_cli.create_deployment.help)
@cli_util.option('--deployment-name', help=u"""The name given to the GoldenGate service deployment.
The name must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter.""")
@cli_util.option('--admin-username', help=u"""The GoldenGate deployment console username.""")
@cli_util.option('--admin-password', help=u"""The password associated with the GoldenGate deployment console username.
The password must be 8 to 30 characters long and must contain at least 1 uppercase, 1 lowercase, 1 numeric,
and 1 special character. Special characters such as ‘$’, ‘^’, or ‘?’ are not allowed.""")
@cli_util.option('--certificate-file', type=click.File('r'), help=u"""The SSL certificate for this deployment in PEM format.""")
@cli_util.option('--private-key-file', type=click.File('r'), help=u"""The private key for your certificate in PEM format.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}}, output_type={'module': 'golden_gate', 'class': 'Deployment'})
@cli_util.wrap_exceptions
def create_deployment_extended(ctx, **kwargs):
    if kwargs.get('deployment_type') is None:
        kwargs['deployment_type'] = "OGG"

    if kwargs.get('ogg_data') is None:
        _ogg_details = {}
        _missing_params = []
        if kwargs.get('deployment_name') is None:
            _missing_params.append("deployment-name")
        else:
            _ogg_details['deploymentName'] = kwargs.get('deployment_name')
        del kwargs['deployment_name']

        if kwargs.get('admin_username') is None:
            _missing_params.append("admin-username")
        else:
            _ogg_details['adminUsername'] = kwargs.get('admin_username')
        del kwargs['admin_username']

        if len(_missing_params) != 0:
            raise cli_exceptions.RequiredValueNotInDefaultOrUserInputError('Missing option(s) --{}.'
                                                                           .format(', --'.join(_missing_params)))

        if kwargs.get('admin_password') is None:
            _ogg_details['adminPassword'] = click.prompt(text='Enter admin password', default='',
                                                         hide_input=True, show_default=False, confirmation_prompt=True)
            if not _ogg_details['adminPassword']:
                raise click.UsageError('Password cannot be whitespace or empty string')
        else:
            _ogg_details['adminPassword'] = kwargs.get('admin_password')
        del kwargs['admin_password']

        if kwargs.get('certificate_file') is not None:
            _ogg_details['certificate'] = kwargs.get('certificate_file').read()
        del kwargs['certificate_file']

        if kwargs.get('private_key_file') is not None:
            _ogg_details['key'] = kwargs.get('private_key_file').read()
        del kwargs['private_key_file']

        kwargs['ogg_data'] = json.dumps(_ogg_details)

    ctx.invoke(goldengate_cli.create_deployment, **kwargs)


# from oci goldengate deployment update <blah> -ogg-data <json>
# to   oci goldengate deployment update <blah>
#                 --admin-username <text>
#                 [--admin-password <text>]
#                 --certificate-file <file>
#                 --private-key-file <file>

@cli_util.copy_params_from_generated_command(goldengate_cli.update_deployment,
                                             params_to_exclude=['ogg_data'],
                                             copy_from_json=False)
@goldengate_cli.deployment_group.command(name='update', help=goldengate_cli.update_deployment.help)
@cli_util.option('--admin-username', help=u"""The GoldenGate deployment console username.""")
@cli_util.option('--admin-password', help=u"""The password associated with the GoldenGate deployment console username.
The password must be 8 to 30 characters long and must contain at least 1 uppercase, 1 lowercase, 1 numeric,
and 1 special character. Special characters such as ‘$’, ‘^’, or ‘?’ are not allowed.""")
@cli_util.option('--certificate-file', type=click.File('r'), help=u"""The SSL certificate for this deployment in PEM format.""")
@cli_util.option('--private-key-file', type=click.File('r'), help=u"""The private key for your certificate in PEM format.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_deployment_extended(ctx, **kwargs):
    if kwargs.get('ogg_data') is None:
        _ogg_details = {}

        if kwargs.get('admin_username') is not None:
            _ogg_details['adminUsername'] = kwargs.get('admin_username')
            if kwargs.get('admin_password') is None:
                _ogg_details['adminPassword'] = click.prompt(text='Enter admin password', default='',
                                                             hide_input=True, show_default=False,
                                                             confirmation_prompt=True)
                if not _ogg_details['adminPassword']:
                    raise click.UsageError('Password cannot be whitespace or empty string')
            else:
                _ogg_details['adminPassword'] = kwargs.get('admin_password')
            del kwargs['admin_password']
        del kwargs['admin_username']

        if 'admin_password' in kwargs:
            if kwargs.get('admin_password') is not None:
                raise cli_exceptions.RequiredValueNotInDefaultOrUserInputError('Missing option(s) --admin-username.')
            del kwargs['admin_password']

        if kwargs.get('certificate_file') is not None:
            _ogg_details['certificate'] = kwargs.get('certificate_file').read()
        del kwargs['certificate_file']

        if kwargs.get('private_key_file') is not None:
            _ogg_details['key'] = kwargs.get('private_key_file').read()
        del kwargs['private_key_file']

        kwargs['ogg_data'] = json.dumps(_ogg_details)

    ctx.invoke(goldengate_cli.update_deployment, **kwargs)


# Remove cancel from oci goldengate deployment-backup
goldengate_cli.deployment_backup_group.commands.pop(goldengate_cli.cancel_deployment_backup.name)

# oci goldengate deployment-backup cancel-deployment-backup-default-cancel-deployment-backup-details -> oci goldengate deployment-backup cancel
cli_util.rename_command(goldengate_cli, goldengate_cli.deployment_backup_group, goldengate_cli.cancel_deployment_backup_default_cancel_deployment_backup_details, "cancel")


# oci goldengate connection create-connection-create-golden-gate-connection-details -> oci goldengate connection create-goldengate-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_golden_gate_connection_details, "create-goldengate-connection")


# oci goldengate connection create-connection-create-kafka-connection-details -> oci goldengate connection create-kafka-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_kafka_connection_details, "create-kafka-connection")


# oci goldengate connection create-connection-create-mysql-connection-details -> oci goldengate connection create-mysql-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_mysql_connection_details, "create-mysql-connection")


# oci goldengate connection create-connection-create-oci-object-storage-connection-details -> oci goldengate connection create-object-storage-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_oci_object_storage_connection_details, "create-object-storage-connection")


# oci goldengate connection create-connection-create-oracle-connection-details -> oci goldengate connection create-oracle-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_oracle_connection_details, "create-oracle-connection")


# oci goldengate connection update-connection-update-golden-gate-connection-details -> oci goldengate connection update-goldengate-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_golden_gate_connection_details, "update-goldengate-connection")


# oci goldengate connection update-connection-update-kafka-connection-details -> oci goldengate connection update-kafka-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_kafka_connection_details, "update-kafka-connection")


# oci goldengate connection update-connection-update-mysql-connection-details -> oci goldengate connection update-mysql-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_mysql_connection_details, "update-mysql-connection")


# oci goldengate connection update-connection-update-oci-object-storage-connection-details -> oci goldengate connection update-object-storage-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_oci_object_storage_connection_details, "update-object-storage-connection")


# oci goldengate connection update-connection-update-oracle-connection-details -> oci goldengate connection update-oracle-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_oracle_connection_details, "update-oracle-connection")


# Remove create from oci goldengate connection
goldengate_cli.connection_group.commands.pop(goldengate_cli.create_connection.name)


# Remove update from oci goldengate connection
goldengate_cli.connection_group.commands.pop(goldengate_cli.update_connection.name)


@cli_util.copy_params_from_generated_command(goldengate_cli.create_connection_create_oci_object_storage_connection_details, params_to_exclude=['region_parameterconflict'])
@goldengate_cli.connection_group.command(name=goldengate_cli.create_connection_create_oci_object_storage_connection_details.name, help=goldengate_cli.create_connection_create_oci_object_storage_connection_details.help)
@cli_util.option('--os-region', help=u"""The name of the region. e.g.: us-ashburn-1""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}}, output_type={'module': 'golden_gate', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection_create_oci_object_storage_connection_details_extended(ctx, **kwargs):

    if 'os_region' in kwargs:
        kwargs['region_parameterconflict'] = kwargs['os_region']
        kwargs.pop('os_region')

    ctx.invoke(goldengate_cli.create_connection_create_oci_object_storage_connection_details, **kwargs)


@cli_util.copy_params_from_generated_command(goldengate_cli.update_connection_update_oci_object_storage_connection_details, params_to_exclude=['region_parameterconflict'])
@goldengate_cli.connection_group.command(name=goldengate_cli.update_connection_update_oci_object_storage_connection_details.name, help=goldengate_cli.update_connection_update_oci_object_storage_connection_details.help)
@cli_util.option('--os-region', help=u"""The name of the region. e.g.: us-ashburn-1""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_connection_update_oci_object_storage_connection_details_extended(ctx, **kwargs):

    if 'os_region' in kwargs:
        kwargs['region_parameterconflict'] = kwargs['os_region']
        kwargs.pop('os_region')

    ctx.invoke(goldengate_cli.update_connection_update_oci_object_storage_connection_details, **kwargs)


# oci goldengate deployment collect-deployment-diagnostic -> oci goldengate deployment collect-diagnostics
cli_util.rename_command(goldengate_cli, goldengate_cli.deployment_group, goldengate_cli.collect_deployment_diagnostic, "collect-diagnostics")

# oci goldengate deployment deployment-wallet-exists-default-deployment-wallet-exists-details -> oci goldengate deployment wallet-exists
cli_util.rename_command(goldengate_cli, goldengate_cli.deployment_group, goldengate_cli.deployment_wallet_exists_default_deployment_wallet_exists_details, "wallet-exists")


# oci goldengate deployment export-deployment-wallet -> oci goldengate deployment export-wallet
cli_util.rename_command(goldengate_cli, goldengate_cli.deployment_group, goldengate_cli.export_deployment_wallet, "export-wallet")


# oci goldengate deployment import-deployment-wallet -> oci goldengate deployment import-wallet
cli_util.rename_command(goldengate_cli, goldengate_cli.deployment_group, goldengate_cli.import_deployment_wallet, "import-wallet")


# oci goldengate deployment-wallets-operation-summary list-deployment-wallets-operations -> oci goldengate deployment-wallets-operation-summary list-wallet-operations
cli_util.rename_command(goldengate_cli, goldengate_cli.deployment_wallets_operation_summary_group, goldengate_cli.list_deployment_wallets_operations, "list-wallet-operations")


# Remove deployment-wallet-exists from oci goldengate deployment
goldengate_cli.deployment_group.commands.pop(goldengate_cli.deployment_wallet_exists.name)
