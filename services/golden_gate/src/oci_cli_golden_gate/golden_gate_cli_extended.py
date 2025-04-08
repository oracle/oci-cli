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
                                             params_to_exclude=['ogg_data', 'maintenance_window'],
                                             copy_from_json=False)
@goldengate_cli.deployment_group.command(name='create', help=goldengate_cli.create_deployment.help)
@cli_util.option('--deployment-name', help="""The name given to the GoldenGate service deployment.
The name must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter.""")
@cli_util.option('--credential-store', type=click.Choice(['IAM', 'GOLDENGATE'], case_sensitive=True), help="""The type of credential store for OGG.""")
@cli_util.option('--identity-domain-id', help="""The [OCID] of the Identity Domain when IAM credential store is used.""")
@cli_util.option('--admin-username', help="""The GoldenGate deployment console username.""")
@cli_util.option('--admin-password', help="""The password associated with the GoldenGate deployment console username.
The password must be 8 to 30 characters long and must contain at least 1 uppercase, 1 lowercase, 1 numeric,
and 1 special character. Special characters such as '$', '^', or '?' are not allowed.
This field will be deprecated and replaced by 'password-secret-id'.""")
@cli_util.option('--password-secret-id', help="""The [OCID] of the Secret where the deployment password is stored.""")
@cli_util.option('--certificate-file', type=click.File('r'), help="""The SSL certificate for this deployment in PEM format.""")
@cli_util.option('--private-key-file', type=click.File('r'), help="""The private key for your certificate in PEM format.""")
@cli_util.option('--ogg-version', help="""Version of OGG.""")
@cli_util.option('--maintenance-window-day', type=custom_types.CliCaseInsensitiveChoice(["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]), help="""Day of week for the maintenance.""")
@cli_util.option('--maintenance-window-start-hour', help="""Start hour for maintenance period. Hour is in UTC.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}, 'maintenance-window': {'module': 'golden_gate', 'class': 'CreateMaintenanceWindowDetails'}}, output_type={'module': 'golden_gate', 'class': 'Deployment'})
@cli_util.wrap_exceptions
def create_deployment_extended(ctx, **kwargs):
    if kwargs.get('ogg_data') is None:
        _ogg_details = {}
        _missing_params = []
        if kwargs.get('deployment_name') is None:
            _missing_params.append("deployment-name")
        else:
            _ogg_details['deploymentName'] = kwargs.get('deployment_name')
        del kwargs['deployment_name']

        if len(_missing_params) != 0:
            raise cli_exceptions.RequiredValueNotInDefaultOrUserInputError('Missing option(s) --{}.'
                                                                           .format(', --'.join(_missing_params)))

        if kwargs.get('credential_store') is not None:
            _ogg_details['credentialStore'] = kwargs.get('credential_store')
        if kwargs.get('credential_store') == 'IAM':
            if kwargs.get('identity_domain_id') is None:
                raise click.UsageError('--identity-domain-id is required if using IAM credential store.')
            else:
                _ogg_details['identityDomainId'] = kwargs.get('identity_domain_id')
        else:
            if kwargs.get('admin_username') is None:
                raise click.UsageError('--admin-username is required if using GOLDENGATE credential store.')
            elif kwargs.get('admin_password') is None and kwargs.get('password_secret_id') is None:
                raise click.UsageError('Either --password-secret-id or --admin-password is required if using GOLDENGATE credential store.')
            else:
                _ogg_details['adminUsername'] = kwargs.get('admin_username')
                if kwargs.get('password_secret_id') is not None:
                    _ogg_details['passwordSecretId'] = kwargs.get('password_secret_id')
                else:
                    _ogg_details['adminPassword'] = kwargs.get('admin_password')
        del kwargs['admin_username']
        del kwargs['password_secret_id']
        del kwargs['admin_password']
        del kwargs['identity_domain_id']
        del kwargs['credential_store']

        if kwargs.get('certificate_file') is not None:
            _ogg_details['certificate'] = kwargs.get('certificate_file').read()
        del kwargs['certificate_file']

        if kwargs.get('private_key_file') is not None:
            _ogg_details['key'] = kwargs.get('private_key_file').read()
        del kwargs['private_key_file']

        if kwargs.get('ogg_version') is not None:
            _ogg_details['oggVersion'] = kwargs.get('ogg_version')
        del kwargs['ogg_version']

        kwargs['ogg_data'] = json.dumps(_ogg_details)

    if kwargs.get('maintenance_window') is None:
        _maintenance_window = {}

        if kwargs.get('maintenance_window_day') is not None:
            _maintenance_window['day'] = kwargs.get('maintenance_window_day')
        del kwargs['maintenance_window_day']

        if kwargs.get('maintenance_window_start_hour') is not None:
            _maintenance_window['startHour'] = kwargs.get('maintenance_window_start_hour')
        del kwargs['maintenance_window_start_hour']

        if "day" in _maintenance_window or "startHour" in _maintenance_window:
            kwargs['maintenance_window'] = json.dumps(_maintenance_window)

    ctx.invoke(goldengate_cli.create_deployment, **kwargs)


# from oci goldengate deployment update <blah> -ogg-data <json>
# to   oci goldengate deployment update <blah>
#                 --admin-username <text>
#                 [--admin-password <text>]
#                 --certificate-file <file>
#                 --private-key-file <file>

@cli_util.copy_params_from_generated_command(goldengate_cli.update_deployment,
                                             params_to_exclude=['ogg_data', 'maintenance_window'],
                                             copy_from_json=False)
@goldengate_cli.deployment_group.command(name='update', help=goldengate_cli.update_deployment.help)
@cli_util.option('--credential-store', type=click.Choice(['IAM', 'GOLDENGATE'], case_sensitive=True), help="""The type of credential store for OGG.""")
@cli_util.option('--identity-domain-id', help="""The [OCID] of the Identity Domain when IAM credential store is used.""")
@cli_util.option('--admin-username', help="""The GoldenGate deployment console username.""")
@cli_util.option('--admin-password', help="""The password associated with the GoldenGate deployment console username.
The password must be 8 to 30 characters long and must contain at least 1 uppercase, 1 lowercase, 1 numeric,
and 1 special character. Special characters such as '$', '^', or '?' are not allowed.
This field will be deprecated and replaced by 'password-secret-id'.""")
@cli_util.option('--password-secret-id', help="""The [OCID] of the Secret where the deployment password is stored.""")
@cli_util.option('--certificate-file', type=click.File('r'), help="""The SSL certificate for this deployment in PEM format.""")
@cli_util.option('--private-key-file', type=click.File('r'), help="""The private key for your certificate in PEM format.""")
@cli_util.option('--maintenance-window-day', help="""Day of week for the maintenance.""")
@cli_util.option('--maintenance-window-start-hour', help="""Start hour for maintenance period. Hour is in UTC.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}, 'maintenance-window': {'module': 'golden_gate', 'class': 'UpdateMaintenanceWindowDetails'}})
@cli_util.wrap_exceptions
def update_deployment_extended(ctx, **kwargs):
    if kwargs.get('ogg_data') is None:
        _ogg_details = {}

        if kwargs.get('credential_store') is None:
            if kwargs.get('admin_username') is not None or kwargs.get('password_secret_id') is not None or kwargs.get('admin_password') is not None or kwargs.get('identity_domain_id') is not None:
                raise click.UsageError('--credential-store is required if changing admin username, password secret ID, admin password or identity domain ID.')
        elif kwargs.get('credential_store') == 'GOLDENGATE':
            if kwargs.get('admin_username') is None:
                raise click.UsageError('--admin-username is required if using GOLDENGATE credential store.')
            elif kwargs.get('admin_password') is None and kwargs.get('password_secret_id') is None:
                raise click.UsageError('Either --password-secret-id or --admin-password is required if using GOLDENGATE credential store.')
            else:
                _ogg_details['adminUsername'] = kwargs.get('admin_username')
                if kwargs.get('password_secret_id') is not None:
                    _ogg_details['passwordSecretId'] = kwargs.get('password_secret_id')
                else:
                    _ogg_details['adminPassword'] = kwargs.get('admin_password')
        elif kwargs.get('credential_store') == 'IAM':
            if kwargs.get('identity_domain_id') is None:
                raise click.UsageError('--identity-domain-id is required if using IAM credential store.')
            else:
                _ogg_details['identityDomainId'] = kwargs.get('identity_domain_id')
        del kwargs['credential_store']
        del kwargs['admin_username']
        del kwargs['admin_password']
        del kwargs['password_secret_id']
        del kwargs['identity_domain_id']

        if kwargs.get('certificate_file') is not None:
            _ogg_details['certificate'] = kwargs.get('certificate_file').read()
        del kwargs['certificate_file']

        if kwargs.get('private_key_file') is not None:
            _ogg_details['key'] = kwargs.get('private_key_file').read()
        del kwargs['private_key_file']

        kwargs['ogg_data'] = json.dumps(_ogg_details)

    if kwargs.get('maintenance_window') is None:
        _maintenance_window = {}

        if kwargs.get('maintenance_window_day') is not None:
            _maintenance_window['day'] = kwargs.get('maintenance_window_day')
        del kwargs['maintenance_window_day']

        if kwargs.get('maintenance_window_start_hour') is not None:
            _maintenance_window['startHour'] = kwargs.get('maintenance_window_start_hour')
        del kwargs['maintenance_window_start_hour']

        if "day" in _maintenance_window or "startHour" in _maintenance_window:
            kwargs['maintenance_window'] = json.dumps(_maintenance_window)

    ctx.invoke(goldengate_cli.update_deployment, **kwargs)


# Remove cancel from oci goldengate deployment-backup
goldengate_cli.deployment_backup_group.commands.pop(goldengate_cli.cancel_deployment_backup.name)

# oci goldengate deployment-backup cancel-deployment-backup-default-cancel-deployment-backup-details -> oci goldengate deployment-backup cancel
cli_util.rename_command(goldengate_cli, goldengate_cli.deployment_backup_group, goldengate_cli.cancel_deployment_backup_default_cancel_deployment_backup_details, "cancel")


# oci goldengate deployment collect-deployment-diagnostic -> oci goldengate deployment collect-diagnostics
cli_util.rename_command(goldengate_cli, goldengate_cli.deployment_group, goldengate_cli.collect_deployment_diagnostic, "collect-diagnostics")


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


# oci goldengate deployment upgrade-deployment-upgrade-deployment-specific-release-details -> oci goldengate deployment upgrade-to
cli_util.rename_command(goldengate_cli, goldengate_cli.deployment_group, goldengate_cli.upgrade_deployment_upgrade_deployment_specific_release_details, "upgrade-to")


# oci goldengate deployment-upgrade snooze-deployment-upgrade-default-snooze-deployment-upgrade-details -> oci goldengate deployment-upgrade snooze
cli_util.rename_command(goldengate_cli, goldengate_cli.deployment_upgrade_group, goldengate_cli.snooze_deployment_upgrade_default_snooze_deployment_upgrade_details, "snooze")


# oci goldengate deployment-upgrade cancel-snooze-deployment-upgrade-default-cancel-snooze-deployment-upgrade-details -> oci goldengate deployment-upgrade cancel-snooze
cli_util.rename_command(goldengate_cli, goldengate_cli.deployment_upgrade_group, goldengate_cli.cancel_snooze_deployment_upgrade_default_cancel_snooze_deployment_upgrade_details, "cancel-snooze")


# oci goldengate deployment-upgrade rollback-deployment-upgrade-default-rollback-deployment-upgrade-details -> oci goldengate deployment-upgrade rollback
cli_util.rename_command(goldengate_cli, goldengate_cli.deployment_upgrade_group, goldengate_cli.rollback_deployment_upgrade_default_rollback_deployment_upgrade_details, "rollback")


# oci goldengate deployment-upgrade upgrade-deployment-upgrade-default-upgrade-deployment-upgrade-details -> oci goldengate deployment-upgrade upgrade
cli_util.rename_command(goldengate_cli, goldengate_cli.deployment_upgrade_group, goldengate_cli.upgrade_deployment_upgrade_default_upgrade_deployment_upgrade_details, "upgrade")


# oci goldengate deployment-version-collection list-deployment-versions -> oci goldengate deployment-version-collection list
cli_util.rename_command(goldengate_cli, goldengate_cli.deployment_version_collection_group, goldengate_cli.list_deployment_versions, "list")


# oci goldengate deployment-version-collection -> oci goldengate deployment-version
cli_util.rename_command(goldengate_cli, goldengate_cli.goldengate_root_group, goldengate_cli.deployment_version_collection_group, "deployment-version")

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


# oci goldengate connection create-connection-create-azure-data-lake-storage-connection-details -> oci goldengate connection create-azure-data-lake-storage-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_azure_data_lake_storage_connection_details, "create-azure-data-lake-storage-connection")


# oci goldengate connection create-connection-create-azure-synapse-connection-details -> oci goldengate connection create-azure-synapse-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_azure_synapse_connection_details, "create-azure-synapse-connection")


# oci goldengate connection create-connection-create-kafka-schema-registry-connection-details -> oci goldengate connection create-kafka-schema-registry-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_kafka_schema_registry_connection_details, "create-kafka-schema-registry-connection")


# oci goldengate connection create-connection-create-postgresql-connection-details -> oci goldengate connection create-postgresql-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_postgresql_connection_details, "create-postgresql-connection")


# oci goldengate connection update-connection-update-azure-data-lake-storage-connection-details -> oci goldengate connection update-azure-data-lake-storage-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_azure_data_lake_storage_connection_details, "update-azure-data-lake-storage-connection")


# oci goldengate connection update-connection-update-azure-synapse-connection-details -> oci goldengate connection update-azure-synapse-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_azure_synapse_connection_details, "update-azure-synapse-connection")


# oci goldengate connection update-connection-update-kafka-schema-registry-connection-details -> oci goldengate connection update-kafka-schema-registry-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_kafka_schema_registry_connection_details, "update-kafka-schema-registry-connection")


# oci goldengate connection update-connection-update-postgresql-connection-details -> oci goldengate connection update-postgresql-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_postgresql_connection_details, "update-postgresql-connection")


# oci goldengate connection create-connection-create-amazon-s3-connection-details -> oci goldengate connection create-amazon-s3-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_amazon_s3_connection_details, "create-amazon-s3-connection")


# oci goldengate connection create-connection-create-hdfs-connection-details -> oci goldengate connection create-hdfs-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_hdfs_connection_details, "create-hdfs-connection")


# oci goldengate connection create-connection-create-microsoft-sqlserver-connection-details -> oci goldengate connection create-microsoft-sqlserver-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_microsoft_sqlserver_connection_details, "create-microsoft-sqlserver-connection")


# oci goldengate connection create-connection-create-mongo-db-connection-details -> oci goldengate connection create-mongo-db-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_mongo_db_connection_details, "create-mongo-db-connection")


# oci goldengate connection create-connection-create-oracle-nosql-connection-details -> oci goldengate connection create-oracle-nosql-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_oracle_nosql_connection_details, "create-oracle-nosql-connection")


# oci goldengate connection create-connection-create-snowflake-connection-details -> oci goldengate connection create-snowflake-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_snowflake_connection_details, "create-snowflake-connection")


# oci goldengate connection update-connection-update-amazon-s3-connection-details -> oci goldengate connection update-amazon-s3-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_amazon_s3_connection_details, "update-amazon-s3-connection")


# oci goldengate connection update-connection-update-hdfs-connection-details -> oci goldengate connection update-hdfs-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_hdfs_connection_details, "update-hdfs-connection")


# oci goldengate connection update-connection-update-microsoft-sqlserver-connection-details -> oci goldengate connection update-microsoft-sqlserver-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_microsoft_sqlserver_connection_details, "update-microsoft-sqlserver-connection")


# oci goldengate connection update-connection-update-mongo-db-connection-details -> oci goldengate connection update-mongo-db-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_mongo_db_connection_details, "update-mongo-db-connection")


# oci goldengate connection update-connection-update-oracle-nosql-connection-details -> oci goldengate connection update-oracle-nosql-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_oracle_nosql_connection_details, "update-oracle-nosql-connection")


# oci goldengate connection update-connection-update-snowflake-connection-details -> oci goldengate connection update-snowflake-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_snowflake_connection_details, "update-snowflake-connection")


@cli_util.copy_params_from_generated_command(goldengate_cli.create_connection_create_azure_data_lake_storage_connection_details, params_to_exclude=['endpoint_parameterconflict'])
@goldengate_cli.connection_group.command(name=goldengate_cli.create_connection_create_azure_data_lake_storage_connection_details.name, help=goldengate_cli.create_connection_create_azure_data_lake_storage_connection_details.help)
@cli_util.option('--connection-endpoint', help=u"""Azure Storage service endpoint. e.g: https://test.blob.core.windows.net""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}}, output_type={'module': 'golden_gate', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection_create_azure_data_lake_storage_connection_details_extended(ctx, **kwargs):

    if 'connection_endpoint' in kwargs:
        kwargs['endpoint_parameterconflict'] = kwargs['connection_endpoint']
        kwargs.pop('connection_endpoint')

    ctx.invoke(goldengate_cli.create_connection_create_azure_data_lake_storage_connection_details, **kwargs)


@cli_util.copy_params_from_generated_command(goldengate_cli.update_connection_update_azure_data_lake_storage_connection_details, params_to_exclude=['endpoint_parameterconflict'])
@goldengate_cli.connection_group.command(name=goldengate_cli.update_connection_update_azure_data_lake_storage_connection_details.name, help=goldengate_cli.update_connection_update_azure_data_lake_storage_connection_details.help)
@cli_util.option('--connection-endpoint', help=u"""Azure Storage service endpoint. e.g: https://test.blob.core.windows.net""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_connection_update_azure_data_lake_storage_connection_details_extended(ctx, **kwargs):

    if 'connection_endpoint' in kwargs:
        kwargs['endpoint_parameterconflict'] = kwargs['connection_endpoint']
        kwargs.pop('connection_endpoint')

    ctx.invoke(goldengate_cli.update_connection_update_azure_data_lake_storage_connection_details, **kwargs)


@cli_util.copy_params_from_generated_command(goldengate_cli.create_connection_create_oracle_nosql_connection_details, params_to_exclude=['region_parameterconflict'])
@goldengate_cli.connection_group.command(name=goldengate_cli.create_connection_create_oracle_nosql_connection_details.name, help=goldengate_cli.create_connection_create_oracle_nosql_connection_details.help)
@cli_util.option('--connection-region', help=u"""The name of the region. e.g.: us-ashburn-1""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}}, output_type={'module': 'golden_gate', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection_create_oracle_nosql_connection_details_extended(ctx, **kwargs):

    if 'connection_region' in kwargs:
        kwargs['region_parameterconflict'] = kwargs['connection_region']
        kwargs.pop('connection_region')

    ctx.invoke(goldengate_cli.create_connection_create_oracle_nosql_connection_details, **kwargs)


@cli_util.copy_params_from_generated_command(goldengate_cli.update_connection_update_oracle_nosql_connection_details, params_to_exclude=['region_parameterconflict'])
@goldengate_cli.connection_group.command(name=goldengate_cli.update_connection_update_oracle_nosql_connection_details.name, help=goldengate_cli.update_connection_update_oracle_nosql_connection_details.help)
@cli_util.option('--connection-region', help=u"""The name of the region. e.g.: us-ashburn-1""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_connection_update_oracle_nosql_connection_details_extended(ctx, **kwargs):

    if 'connection_region' in kwargs:
        kwargs['region_parameterconflict'] = kwargs['connection_region']
        kwargs.pop('connection_region')

    ctx.invoke(goldengate_cli.update_connection_update_oracle_nosql_connection_details, **kwargs)


# oci goldengate connection create-connection-create-java-message-service-connection-details -> oci goldengate connection create-jms-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_java_message_service_connection_details, "create-jms-connection")


# oci goldengate connection update-connection-update-java-message-service-connection-details -> oci goldengate connection update-jms-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_java_message_service_connection_details, "update-jms-connection")


# oci goldengate connection-assignment test-connection-assignment-default-test-connection-assignment-details -> oci goldengate connection-assignment test
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_assignment_group, goldengate_cli.test_connection_assignment_default_test_connection_assignment_details, "test")


# oci goldengate deployment-upgrade cancel-deployment-upgrade-default-cancel-deployment-upgrade-details -> oci goldengate deployment-upgrade cancel
cli_util.rename_command(goldengate_cli, goldengate_cli.deployment_upgrade_group, goldengate_cli.cancel_deployment_upgrade_default_cancel_deployment_upgrade_details, "cancel")


# oci goldengate deployment-upgrade reschedule-deployment-upgrade-reschedule-deployment-upgrade-to-date-details -> oci goldengate deployment-upgrade reschedule
cli_util.rename_command(goldengate_cli, goldengate_cli.deployment_upgrade_group, goldengate_cli.reschedule_deployment_upgrade_reschedule_deployment_upgrade_to_date_details, "reschedule")


# oci goldengate connection create-connection-create-amazon-kinesis-connection-details -> oci goldengate connection create-amazon-kinesis-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_amazon_kinesis_connection_details, "create-amazon-kinesis-connection")


# oci goldengate connection create-connection-create-amazon-redshift-connection-details -> oci goldengate connection create-amazon-redshift-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_amazon_redshift_connection_details, "create-amazon-redshift-connection")


# oci goldengate connection create-connection-create-cassandra-connection-details -> oci goldengate connection create-cassandra-connection
# cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_cassandra_connection_details, "create-cassandra-connection")


# oci goldengate connection create-connection-create-db2-connection-details -> oci goldengate connection create-db2-connection
# cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_db2_connection_details, "create-db2-connection")


# oci goldengate connection create-connection-create-elasticsearch-connection-details -> oci goldengate connection create-elasticsearch-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_elasticsearch_connection_details, "create-elasticsearch-connection")


# oci goldengate connection create-connection-create-generic-connection-details -> oci goldengate connection create-generic-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_generic_connection_details, "create-generic-connection")


# oci goldengate connection create-connection-create-google-big-query-connection-details -> oci goldengate connection create-google-big-query-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_google_big_query_connection_details, "create-google-big-query-connection")


# oci goldengate connection create-connection-create-google-cloud-storage-connection-details -> oci goldengate connection create-google-cloud-storage-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_google_cloud_storage_connection_details, "create-google-cloud-storage-connection")


# oci goldengate connection create-connection-create-redis-connection-details -> oci goldengate connection create-redis-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_redis_connection_details, "create-redis-connection")


# oci goldengate connection update-connection-update-amazon-kinesis-connection-details -> oci goldengate connection update-amazon-kinesis-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_amazon_kinesis_connection_details, "update-amazon-kinesis-connection")


# oci goldengate connection update-connection-update-amazon-redshift-connection-details -> oci goldengate connection update-amazon-redshift-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_amazon_redshift_connection_details, "update-amazon-redshift-connection")


# oci goldengate connection update-connection-update-cassandra-connection-details -> oci goldengate connection update-cassandra-connection
# cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_cassandra_connection_details, "update-cassandra-connection")


# oci goldengate connection update-connection-update-db2-connection-details -> oci goldengate connection update-db2-connection
# cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_db2_connection_details, "update-db2-connection")


# oci goldengate connection update-connection-update-elasticsearch-connection-details -> oci goldengate connection update-elasticsearch-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_elasticsearch_connection_details, "update-elasticsearch-connection")


# oci goldengate connection update-connection-update-generic-connection-details -> oci goldengate connection update-generic-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_generic_connection_details, "update-generic-connection")


# oci goldengate connection update-connection-update-google-big-query-connection-details -> oci goldengate connection update-google-big-query-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_google_big_query_connection_details, "update-google-big-query-connection")


# oci goldengate connection update-connection-update-google-cloud-storage-connection-details -> oci goldengate connection update-google-cloud-storage-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_google_cloud_storage_connection_details, "update-google-cloud-storage-connection")


# oci goldengate connection update-connection-update-redis-connection-details -> oci goldengate connection update-redis-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_redis_connection_details, "update-redis-connection")


# oci goldengate certificate-collection create-certificate -> oci goldengate certificate-collection create
cli_util.rename_command(goldengate_cli, goldengate_cli.certificate_collection_group, goldengate_cli.create_certificate, "create")


# oci goldengate certificate-collection list-certificates -> oci goldengate certificate-collection list
cli_util.rename_command(goldengate_cli, goldengate_cli.certificate_collection_group, goldengate_cli.list_certificates, "list")


# Move commands under 'oci goldengate certificate-collection' -> 'oci goldengate certificate'
goldengate_cli.goldengate_root_group.commands.pop(goldengate_cli.certificate_collection_group.name)
goldengate_cli.certificate_group.add_command(goldengate_cli.create_certificate)
goldengate_cli.certificate_group.add_command(goldengate_cli.list_certificates)


# oci goldengate connection add -> oci goldengate connection add-lock
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.add_connection_lock, "add-lock")


# oci goldengate connection remove -> oci goldengate connection remove-lock
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.remove_connection_lock, "remove-lock")


# oci goldengate deployment add -> oci goldengate deployment add-lock
cli_util.rename_command(goldengate_cli, goldengate_cli.deployment_group, goldengate_cli.add_deployment_lock, "add-lock")


# oci goldengate deployment remove -> oci goldengate deployment remove-lock
cli_util.rename_command(goldengate_cli, goldengate_cli.deployment_group, goldengate_cli.remove_deployment_lock, "remove-lock")


# oci goldengate deployment-backup add -> oci goldengate deployment-backup add-lock
cli_util.rename_command(goldengate_cli, goldengate_cli.deployment_backup_group, goldengate_cli.add_deployment_backup_lock, "add-lock")


# oci goldengate deployment-backup remove -> oci goldengate deployment-backup remove-lock
cli_util.rename_command(goldengate_cli, goldengate_cli.deployment_backup_group, goldengate_cli.remove_deployment_backup_lock, "remove-lock")


# oci goldengate deployment add -> oci goldengate deployment add-deployment-local-peer
cli_util.rename_command(goldengate_cli, goldengate_cli.deployment_group, goldengate_cli.add_deployment_local_peer, "add-deployment-local-peer")


# oci goldengate deployment remove -> oci goldengate deployment remove-deployment-local-peer
cli_util.rename_command(goldengate_cli, goldengate_cli.deployment_group, goldengate_cli.remove_deployment_local_peer, "remove-deployment-local-peer")


# oci goldengate connection create-connection-create-db2-connection-details -> oci goldengate connection create-db2-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_db2_connection_details, "create-db2-connection")


# oci goldengate connection update-connection-update-db2-connection-details -> oci goldengate connection update-db2-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_db2_connection_details, "update-db2-connection")


# oci goldengate deployment generate-library-url-generate-log-reader-component-library-url-details -> oci goldengate deployment generate-log-reader-component-library-url
cli_util.rename_command(goldengate_cli, goldengate_cli.deployment_group, goldengate_cli.generate_library_url_generate_log_reader_component_library_url_details, "generate-log-reader-component-library-url")

# oci goldengate connection refresh-connection-default-refresh-connection-details -> oci goldengate connection refresh
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.refresh_connection_default_refresh_connection_details, "refresh")

# oci goldengate deployment-environment-collection list-deployment-environments -> oci goldengate deployment-environment-collection list
cli_util.rename_command(goldengate_cli, goldengate_cli.deployment_environment_collection_group, goldengate_cli.list_deployment_environments, "list")

# oci goldengate deployment-environment-collection -> oci goldengate deployment-environment
cli_util.rename_command(goldengate_cli, goldengate_cli.goldengate_root_group, goldengate_cli.deployment_environment_collection_group, "deployment-environment")


# oci goldengate pipeline create-pipeline-create-zero-etl-pipeline-details -> oci goldengate pipeline create-zero-etl-pipeline
cli_util.rename_command(goldengate_cli, goldengate_cli.pipeline_group, goldengate_cli.create_pipeline_create_zero_etl_pipeline_details, "create-zero-etl-pipeline")


# oci goldengate pipeline list-pipeline-initialization-steps -> oci goldengate pipeline list-initialization-steps
cli_util.rename_command(goldengate_cli, goldengate_cli.pipeline_group, goldengate_cli.list_pipeline_initialization_steps, "list-initialization-steps")


# oci goldengate pipeline list-pipeline-running-processes -> oci goldengate pipeline list-running-processes
cli_util.rename_command(goldengate_cli, goldengate_cli.pipeline_group, goldengate_cli.list_pipeline_running_processes, "list-running-processes")


# oci goldengate pipeline list-pipeline-schema-tables -> oci goldengate pipeline list-schema-tables
cli_util.rename_command(goldengate_cli, goldengate_cli.pipeline_group, goldengate_cli.list_pipeline_schema_tables, "list-schema-tables")


# oci goldengate pipeline list-pipeline-schemas -> oci goldengate pipeline list-schemas
cli_util.rename_command(goldengate_cli, goldengate_cli.pipeline_group, goldengate_cli.list_pipeline_schemas, "list-schemas")


# oci goldengate pipeline start-pipeline-default-start-pipeline-details -> oci goldengate pipeline start
cli_util.rename_command(goldengate_cli, goldengate_cli.pipeline_group, goldengate_cli.start_pipeline_default_start_pipeline_details, "start")


# oci goldengate pipeline stop-pipeline-default-stop-pipeline-details -> oci goldengate pipeline stop
cli_util.rename_command(goldengate_cli, goldengate_cli.pipeline_group, goldengate_cli.stop_pipeline_default_stop_pipeline_details, "stop")


# oci goldengate pipeline test-pipeline-connection-default-test-pipeline-connection-details -> oci goldengate pipeline test-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.pipeline_group, goldengate_cli.test_pipeline_connection_default_test_pipeline_connection_details, "test-connection")


# oci goldengate pipeline update-pipeline-update-zero-etl-pipeline-details -> oci goldengate pipeline update-zero-etl-pipeline
cli_util.rename_command(goldengate_cli, goldengate_cli.pipeline_group, goldengate_cli.update_pipeline_update_zero_etl_pipeline_details, "update-zero-etl-pipeline")


# oci goldengate recipe-summary-collection -> oci goldengate pipeline-recipe-collection
cli_util.rename_command(goldengate_cli, goldengate_cli.goldengate_root_group, goldengate_cli.recipe_summary_collection_group, "pipeline-recipe-collection")


# Remove create from oci goldengate pipeline
goldengate_cli.pipeline_group.commands.pop(goldengate_cli.create_pipeline.name)


# Remove update from oci goldengate pipeline
goldengate_cli.pipeline_group.commands.pop(goldengate_cli.update_pipeline.name)


# Remove test-pipeline-connection from oci goldengate pipeline
goldengate_cli.pipeline_group.commands.pop(goldengate_cli.test_pipeline_connection.name)


@cli_util.copy_params_from_generated_command(goldengate_cli.create_pipeline_create_zero_etl_pipeline_details, params_to_exclude=['source_connection_details', 'target_connection_details'])
@goldengate_cli.pipeline_group.command(name=goldengate_cli.create_pipeline_create_zero_etl_pipeline_details.name, help=goldengate_cli.create_pipeline_create_zero_etl_pipeline_details.help)
@cli_util.option('--source-connection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.
 [required]""")
@cli_util.option('--target-connection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.
 [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'locks': {'module': 'golden_gate', 'class': 'list[ResourceLock]'}, 'source-connection': {'module': 'golden_gate', 'class': 'SourcePipelineConnectionDetails'}, 'target-connection': {'module': 'golden_gate', 'class': 'TargetPipelineConnectionDetails'}, 'process-options': {'module': 'golden_gate', 'class': 'ProcessOptions'}}, output_type={'module': 'golden_gate', 'class': 'Pipeline'})
@cli_util.wrap_exceptions
def create_pipeline_create_zero_etl_pipeline_details_extended(ctx, **kwargs):

    if 'source_connection' in kwargs:
        kwargs['source_connection_details'] = kwargs['source_connection']
        kwargs.pop('source_connection')

    if 'target_connection' in kwargs:
        kwargs['target_connection_details'] = kwargs['target_connection']
        kwargs.pop('target_connection')

    ctx.invoke(goldengate_cli.create_pipeline_create_zero_etl_pipeline_details, **kwargs)


# oci goldengate connection create-connection-create-databricks-connection-details -> oci goldengate connection create-databricks-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_databricks_connection_details, "create-databricks-connection")

# oci goldengate connection update-connection-update-databricks-connection-details -> oci goldengate connection update-databricks-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_databricks_connection_details, "update-databricks-connection")

# oci goldengate connection create-connection-create-google-pub-sub-connection-details -> oci goldengate connection create-google-pub-sub-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_google_pub_sub_connection_details, "create-google-pub-sub-connection")

# oci goldengate connection update-connection-update-google-pub-sub-connection-details -> oci goldengate connection update-google-pub-sub-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_google_pub_sub_connection_details, "update-google-pub-sub-connection")

# oci goldengate connection create-connection-create-microsoft-fabric-connection-details -> oci goldengate connection create-microsoft-fabric-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.create_connection_create_microsoft_fabric_connection_details, "create-microsoft-fabric-connection")

# oci goldengate connection update-connection-update-microsoft-fabric-connection-details -> oci goldengate connection update-microsoft-fabric-connection
cli_util.rename_command(goldengate_cli, goldengate_cli.connection_group, goldengate_cli.update_connection_update_microsoft_fabric_connection_details, "update-microsoft-fabric-connection")


@cli_util.copy_params_from_generated_command(goldengate_cli.create_connection_create_microsoft_fabric_connection_details, params_to_exclude=['endpoint_parameterconflict'])
@goldengate_cli.connection_group.command(name=goldengate_cli.create_connection_create_microsoft_fabric_connection_details.name, help=goldengate_cli.create_connection_create_microsoft_fabric_connection_details.help)
@cli_util.option('--connection-endpoint', help=u"""Optional Microsoft Fabric service endpoint. Default value: https://onelake.dfs.fabric.microsoft.com""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'locks': {'module': 'golden_gate', 'class': 'list[AddResourceLockDetails]'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}}, output_type={'module': 'golden_gate', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection_create_microsoft_fabric_connection_details_extended(ctx, **kwargs):

    if 'connection_endpoint' in kwargs:
        kwargs['endpoint_parameterconflict'] = kwargs['connection_endpoint']
        kwargs.pop('connection_endpoint')

    ctx.invoke(goldengate_cli.create_connection_create_microsoft_fabric_connection_details, **kwargs)


@cli_util.copy_params_from_generated_command(goldengate_cli.update_connection_update_microsoft_fabric_connection_details, params_to_exclude=['endpoint_parameterconflict'])
@goldengate_cli.connection_group.command(name=goldengate_cli.update_connection_update_microsoft_fabric_connection_details.name, help=goldengate_cli.update_connection_update_microsoft_fabric_connection_details.help)
@cli_util.option('--connection-endpoint', help=u"""Optional Microsoft Fabric service endpoint. Default value: https://onelake.dfs.fabric.microsoft.com""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_connection_update_microsoft_fabric_connection_details_extended(ctx, **kwargs):

    if 'connection_endpoint' in kwargs:
        kwargs['endpoint_parameterconflict'] = kwargs['connection_endpoint']
        kwargs.pop('connection_endpoint')

    ctx.invoke(goldengate_cli.update_connection_update_microsoft_fabric_connection_details, **kwargs)


# oci goldengate pipeline collect-pipeline-diagnostic -> oci goldengate pipeline collect-diagnostic
cli_util.rename_command(goldengate_cli, goldengate_cli.pipeline_group, goldengate_cli.collect_pipeline_diagnostic, "collect-diagnostic")
