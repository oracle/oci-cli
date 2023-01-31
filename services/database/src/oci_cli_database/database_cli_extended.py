# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import sys
import click
import json
import oci
import six  # noqa: F401

from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types
from services.database.src.oci_cli_database.generated import database_cli
from oci_cli.aliasing import CommandGroupWithAlias

# Rename some commands and groups
cli_util.rename_command(database_cli, database_cli.db_root_group, database_cli.db_node_group, "node")
cli_util.rename_command(database_cli, database_cli.db_root_group, database_cli.db_system_group, "system")
cli_util.rename_command(database_cli, database_cli.db_root_group, database_cli.db_system_shape_group, "system-shape")
cli_util.rename_command(database_cli, database_cli.db_root_group, database_cli.db_version_group, "version")
cli_util.rename_command(database_cli, database_cli.db_root_group, database_cli.patch_history_entry_group, "patch-history")

cli_util.rename_command(database_cli, database_cli.database_group, database_cli.create_database_create_database_from_backup, "create-database-from-backup")

database_cli.patch_group.commands.pop("get-db-system")
database_cli.patch_group.commands.pop("list-db-system")
database_cli.patch_history_entry_group.commands.pop("get-db-system")
database_cli.patch_history_entry_group.commands.pop("list-db-system")

database_cli.get_db_system_patch.name = "by-db-system"
database_cli.get_db_system_patch_history_entry.name = "by-db-system"
database_cli.list_db_system_patches.name = "by-db-system"
database_cli.list_db_system_patch_history_entries.name = "by-db-system"

cli_util.rename_command(database_cli, database_cli.autonomous_database_group, database_cli.generate_autonomous_database_wallet, "generate-wallet")

database_cli.autonomous_database_group.commands.pop(database_cli.create_autonomous_database.name)
cli_util.rename_command(database_cli, database_cli.autonomous_database_group, database_cli.create_autonomous_database_create_autonomous_database_clone_details, "create-from-clone")
cli_util.rename_command(database_cli, database_cli.autonomous_database_group, database_cli.create_autonomous_database_create_autonomous_database_details, "create")

cli_util.rename_command(database_cli, database_cli.exadata_infrastructure_group, database_cli.download_exadata_infrastructure_config_file, "download-config-file")
cli_util.rename_command(database_cli, database_cli.autonomous_container_database_group, database_cli.rotate_autonomous_container_database_encryption_key, "rotate-key")
cli_util.rename_command(database_cli, database_cli.autonomous_database_group, database_cli.rotate_autonomous_database_encryption_key, "rotate-key")

cli_util.rename_command(database_cli, database_cli.db_root_group, database_cli.autonomous_container_database_dataguard_association_group, "autonomous-container-database-dataguard")
cli_util.rename_command(database_cli, database_cli.db_root_group, database_cli.autonomous_database_dataguard_association_group, "autonomous-database-dataguard")

# Commands are being temporarily removed by Database team
# cli_util.rename_command(database_cli.db_root_group, database_cli.autonomous_container_database_mission_critical_association_group, "autonomous-mission-critical-data-guard")
# cli_util.rename_command(database_cli.db_root_group, database_cli.autonomous_database_mission_critical_association_group, "autonomous-mission-critical-database-data-guard")
cli_util.rename_command(database_cli, database_cli.db_root_group, database_cli.autonomous_exadata_infrastructure_shape_group, "shape")

# Move autonomous_exadata_infrastructure_shape_group as sub command within autonomous_exadata_infrastructure_group
database_cli.db_root_group.commands.pop(database_cli.autonomous_exadata_infrastructure_shape_group.name)
database_cli.autonomous_exadata_infrastructure_group.add_command(database_cli.autonomous_exadata_infrastructure_shape_group)

cli_util.rename_command(database_cli, database_cli.backup_destination_group, database_cli.create_backup_destination_create_nfs_backup_destination_details, "create-nfs-details")
cli_util.rename_command(database_cli, database_cli.backup_destination_group, database_cli.create_backup_destination_create_recovery_appliance_backup_destination_details, "create-recovery-appliance-details")
database_cli.backup_destination_group.commands.pop(database_cli.create_backup_destination.name)
database_cli.db_root_group.commands.pop(database_cli.backup_destination_summary_group.name)

# Clone from Db System Rename for VM/BM
cli_util.rename_command(database_cli, database_cli.db_system_group, database_cli.launch_db_system_launch_db_system_from_db_system_details, "launch-from-db-system")


# Renaming db-system-upgrade-history-entry sub command
cli_util.rename_command(database_cli, database_cli.db_root_group, database_cli.db_system_upgrade_history_entry_group, "db-system-upgrade-history")

DATA_COLLECTION_OPTIONS_HELP = u"""Available options are \"isDiagnosticsEventsEnabled\", \"isHealthMonitoringEnabled\" and \"isIncidentLogsEnabled\". Provide a value true or false to enable or disable a particular option.
Example: `{\"isDiagnosticsEventsEnabled\":true, \"isHealthMonitoringEnabled\":true, \"isIncidentLogsEnabled\":true}`
""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP


# Renaming the db system upgrade history parameter upgrade-history-entry-id to upgrade-history-id
@cli_util.copy_params_from_generated_command(database_cli.get_db_system_upgrade_history_entry, params_to_exclude=['upgrade_history_entry_id'])
@cli_util.option('--upgrade-history-id', required=True, help=u"""The database/db system upgrade History [OCID].""")
@database_cli.db_system_upgrade_history_entry_group.command(name='get', help=database_cli.database_group.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DbSystemUpgradeHistoryEntry'})
@cli_util.wrap_exceptions
def get_db_system_upgrade_history_entry_extended(ctx, **kwargs):
    if 'upgrade_history_id' in kwargs and kwargs['upgrade_history_id']:
        kwargs['upgrade_history_entry_id'] = kwargs['upgrade_history_id']

    del kwargs['upgrade_history_id']
    ctx.invoke(database_cli.get_db_system_upgrade_history_entry, **kwargs)


# Renaming the db system upgrade parameters snapshot-retention-period-in-days to snapshot-retention-period and is-snapshot-retention-days-force-updated to force
@cli_util.copy_params_from_generated_command(database_cli.upgrade_db_system, params_to_exclude=['snapshot_retention_period_in_days', 'is_snapshot_retention_days_force_updated'])
@cli_util.option('--snapshot-retention-period', type=click.INT, help=u"""The retention period, in days, for the snapshot that allows you to perform a rollback of the upgrade operation. After this number of days passes, you cannot roll back the upgrade.""")
@cli_util.option('--force', type=click.BOOL, help=u"""If true, rollback time is updated even if operating system upgrade history contains errors.""")
@database_cli.db_system_group.command(name='upgrade', help=database_cli.upgrade_db_system.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def upgrade_db_system_extended(ctx, **kwargs):
    if 'snapshot_retention_period' in kwargs and kwargs['snapshot_retention_period']:
        kwargs['snapshot_retention_period_in_days'] = kwargs['snapshot_retention_period']

    if 'force' in kwargs and kwargs['force']:
        kwargs['is_snapshot_retention_days_force_updated'] = kwargs['force']

    del kwargs['snapshot_retention_period']
    del kwargs['force']
    ctx.invoke(database_cli.upgrade_db_system, **kwargs)


# Renaming Db Upgrade sub command and group
cli_util.rename_command(database_cli, database_cli.database_group, database_cli.list_database_upgrade_history_entries, "list-upgrade-history")
cli_util.rename_command(database_cli, database_cli.db_root_group, database_cli.database_upgrade_history_entry_group, "upgrade-history")


# Removing the 3 generated polymorphic upgrade commands as we are redefining them
database_cli.database_group.commands.pop(database_cli.upgrade_database_database_upgrade_with_database_software_image_details.name)
database_cli.database_group.commands.pop(database_cli.upgrade_database_database_upgrade_with_db_version_details.name)
database_cli.database_group.commands.pop(database_cli.upgrade_database_database_upgrade_with_db_home_details.name)


# Rename the command upgrade_database_database_upgrade_with_database_software_image_details and the parameter database-upgrade-source-details-database-software-image-id to database-software-image-id and database_upgrade_source_details_options to options.
@cli_util.copy_params_from_generated_command(database_cli.upgrade_database_database_upgrade_with_database_software_image_details, params_to_exclude=['database_upgrade_source_details_database_software_image_id', 'database_upgrade_source_details_options'])
@cli_util.option('--database-software-image-id', required=True, help=u"""the database software id used for upgrading the database.""")
@cli_util.option('--options', help=u"""Additional upgrade options supported by DBUA(Database Upgrade Assistant). Example: \"-upgradeTimezone false -keepEvents\"""")
@database_cli.database_group.command(name='upgrade-with-database-software-image', help=database_cli.database_group.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'Database'})
@cli_util.wrap_exceptions
def upgrade_database_database_upgrade_with_database_software_image_details_extended(ctx, **kwargs):
    if 'database_software_image_id' in kwargs and kwargs['database_software_image_id']:
        kwargs['database_upgrade_source_details_database_software_image_id'] = kwargs['database_software_image_id']

    if 'options' in kwargs and kwargs['options']:
        kwargs['database_upgrade_source_details_options'] = kwargs['options']

    del kwargs['database_software_image_id']
    del kwargs['options']

    ctx.invoke(database_cli.upgrade_database_database_upgrade_with_database_software_image_details, **kwargs)


# Rename the command upgrade_database_database_upgrade_with_db_version_details and the parameter database-upgrade-source-details-db-version to db-version and database_upgrade_source_details_options to options.
@cli_util.copy_params_from_generated_command(database_cli.upgrade_database_database_upgrade_with_db_version_details, params_to_exclude=['database_upgrade_source_details_db_version', 'database_upgrade_source_details_options'])
@cli_util.option('--db-version', required=True, help=u"""A valid Oracle Database version. To get a list of supported versions, use the [ListDbVersions] operation.""")
@cli_util.option('--options', help=u"""Additional upgrade options supported by DBUA(Database Upgrade Assistant). Example: \"-upgradeTimezone false -keepEvents\"""")
@database_cli.database_group.command(name='upgrade-with-db-version', help=database_cli.database_group.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'Database'})
@cli_util.wrap_exceptions
def upgrade_database_database_upgrade_with_db_version_details_extended(ctx, **kwargs):
    if 'db_version' in kwargs and kwargs['db_version']:
        kwargs['database_upgrade_source_details_db_version'] = kwargs['db_version']

    if 'options' in kwargs and kwargs['options']:
        kwargs['database_upgrade_source_details_options'] = kwargs['options']

    del kwargs['db_version']
    del kwargs['options']

    ctx.invoke(database_cli.upgrade_database_database_upgrade_with_db_version_details, **kwargs)


# Rename the command upgrade_database_database_upgrade_with_db_home_details and the parameter database-upgrade-source-details-db-home-id to db-home-id and database_upgrade_source_details_options to options.
@cli_util.copy_params_from_generated_command(database_cli.upgrade_database_database_upgrade_with_db_home_details, params_to_exclude=['database_upgrade_source_details_db_home_id', 'database_upgrade_source_details_options'])
@cli_util.option('--db-home-id', required=True, help=u"""The [OCID] of the Database Home.""")
@cli_util.option('--options', help=u"""Additional upgrade options supported by DBUA(Database Upgrade Assistant). Example: \"-upgradeTimezone false -keepEvents\"""")
@database_cli.database_group.command(name='upgrade-with-db-home', help=database_cli.database_group.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'Database'})
@cli_util.wrap_exceptions
def upgrade_database_database_upgrade_with_db_home_details_extended(ctx, **kwargs):
    if 'db_home_id' in kwargs and kwargs['db_home_id']:
        kwargs['database_upgrade_source_details_db_home_id'] = kwargs['db_home_id']

    if 'options' in kwargs and kwargs['options']:
        kwargs['database_upgrade_source_details_options'] = kwargs['options']

    del kwargs['db_home_id']
    del kwargs['options']

    ctx.invoke(database_cli.upgrade_database_database_upgrade_with_db_home_details, **kwargs)


# Renaming the upgrade command to upgrade-rollback and removing parameters database_upgrade_source_details and action
@cli_util.copy_params_from_generated_command(database_cli.upgrade_database, params_to_exclude=['database_upgrade_source_details', 'action'])
@database_cli.database_group.command('upgrade-rollback', help=database_cli.database_group.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-upgrade-source-details': {'module': 'database', 'class': 'DatabaseUpgradeSourceBase'}}, output_type={'module': 'database', 'class': 'Database'})
@cli_util.wrap_exceptions
def upgrade_database_extended(ctx, **kwargs):
    kwargs['action'] = "ROLLBACK"
    ctx.invoke(database_cli.upgrade_database, **kwargs)


# Renaming the parameter upgrade-history-entry-id to upgrade-history-id
@cli_util.copy_params_from_generated_command(database_cli.get_database_upgrade_history_entry, params_to_exclude=['upgrade_history_entry_id'])
@cli_util.option('--upgrade-history-id', required=True, help=u"""The database upgrade History [OCID].""")
@database_cli.database_upgrade_history_entry_group.command(name='get', help=database_cli.database_group.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DatabaseUpgradeHistoryEntry'})
@cli_util.wrap_exceptions
def get_database_upgrade_history_entry_extended(ctx, **kwargs):
    if 'upgrade_history_id' in kwargs and kwargs['upgrade_history_id']:
        kwargs['upgrade_history_entry_id'] = kwargs['upgrade_history_id']

    del kwargs['upgrade_history_id']
    ctx.invoke(database_cli.get_database_upgrade_history_entry, **kwargs)


# Renaming the parameter should-pdb-admin-account-be-locked to is-pdb-admin-acc-locked
@cli_util.copy_params_from_generated_command(database_cli.create_pluggable_database, params_to_exclude=['should_pdb_admin_account_be_locked'])
@cli_util.option('--is-pdb-admin-acc-locked', type=click.BOOL, help=u"""The locked mode of the pluggable database admin account. If false, the user needs to provide the PDB Admin Password to connect to it. If true, the pluggable database will be locked and user cannot login to it.""")
@database_cli.pluggable_database_group.command(name='create', help=database_cli.database_group.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'PluggableDatabase'})
@cli_util.wrap_exceptions
def create_pluggable_database_extended(ctx, **kwargs):
    if 'is_pdb_admin_acc_locked' in kwargs and kwargs['is_pdb_admin_acc_locked']:
        kwargs['should_pdb_admin_account_be_locked'] = kwargs['is_pdb_admin_acc_locked']

    del kwargs['is_pdb_admin_acc_locked']
    ctx.invoke(database_cli.create_pluggable_database, **kwargs)


# Renaming the parameter should-pdb-admin-account-be-locked to is-pdb-admin-acc-locked
@cli_util.copy_params_from_generated_command(database_cli.local_clone_pluggable_database, params_to_exclude=['should_pdb_admin_account_be_locked'])
@cli_util.option('--is-pdb-admin-acc-locked', type=click.BOOL, help=u"""The locked mode of the pluggable database admin account. If false, the user needs to provide the PDB Admin Password to connect to it. If true, the pluggable database will be locked and user cannot login to it.""")
@database_cli.pluggable_database_group.command(name='local-clone', help=database_cli.database_group.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'PluggableDatabase'})
@cli_util.wrap_exceptions
def local_clone_pluggable_database_extended(ctx, **kwargs):
    if 'is_pdb_admin_acc_locked' in kwargs and kwargs['is_pdb_admin_acc_locked']:
        kwargs['should_pdb_admin_account_be_locked'] = kwargs['is_pdb_admin_acc_locked']

    del kwargs['is_pdb_admin_acc_locked']
    ctx.invoke(database_cli.local_clone_pluggable_database, **kwargs)


# Renaming the parameter should-pdb-admin-account-be-locked to is-pdb-admin-acc-locked
@cli_util.copy_params_from_generated_command(database_cli.remote_clone_pluggable_database, params_to_exclude=['should_pdb_admin_account_be_locked'])
@cli_util.option('--is-pdb-admin-acc-locked', type=click.BOOL, help=u"""The locked mode of the pluggable database admin account. If false, the user needs to provide the PDB Admin Password to connect to it. If true, the pluggable database will be locked and user cannot login to it.""")
@database_cli.pluggable_database_group.command(name='remote-clone', help=database_cli.database_group.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'PluggableDatabase'})
@cli_util.wrap_exceptions
def remote_clone_pluggable_database_extended(ctx, **kwargs):
    if 'is_pdb_admin_acc_locked' in kwargs and kwargs['is_pdb_admin_acc_locked']:
        kwargs['should_pdb_admin_account_be_locked'] = kwargs['is_pdb_admin_acc_locked']

    del kwargs['is_pdb_admin_acc_locked']
    ctx.invoke(database_cli.remote_clone_pluggable_database, **kwargs)


# OCPUs
database_cli.exadata_infrastructure_group.add_command(database_cli.get_exadata_infrastructure_ocpus)
database_cli.ocp_us_group.commands.pop(database_cli.get_exadata_infrastructure_ocpus.name)
cli_util.rename_command(database_cli, database_cli.exadata_infrastructure_group, database_cli.get_exadata_infrastructure_ocpus, "get-compute-units")
database_cli.db_root_group.commands.pop(database_cli.ocp_us_group.name)

# Clone from Backup Rename for ADB
cli_util.rename_command(database_cli, database_cli.autonomous_database_group, database_cli.create_autonomous_database_create_autonomous_database_from_backup_details, "create-from-backup-id")
cli_util.rename_command(database_cli, database_cli.autonomous_database_group, database_cli.create_autonomous_database_create_autonomous_database_from_backup_timestamp_details, "create-from-backup-timestamp")

cli_util.rename_command(database_cli, database_cli.autonomous_container_database_group, database_cli.rotate_autonomous_container_database_encryption_key, "rotate-key")
cli_util.rename_command(database_cli, database_cli.autonomous_database_group, database_cli.rotate_autonomous_database_encryption_key, "rotate-key")

# wallet commands

cli_util.rename_command(database_cli, database_cli.autonomous_database_wallet_group, database_cli.get_autonomous_database_wallet, "get-metadata")
cli_util.rename_command(database_cli, database_cli.autonomous_database_wallet_group, database_cli.get_autonomous_database_regional_wallet, "get-regional-wallet-metadata")
cli_util.rename_command(database_cli, database_cli.autonomous_database_wallet_group, database_cli.update_autonomous_database_wallet, "rotate")
cli_util.rename_command(database_cli, database_cli.autonomous_database_wallet_group, database_cli.update_autonomous_database_regional_wallet, "rotate-regional-wallet")

# refreshable clone
cli_util.rename_command(database_cli, database_cli.autonomous_database_group, database_cli.autonomous_database_manual_refresh, "manual-refresh")
cli_util.rename_command(database_cli, database_cli.autonomous_database_group, database_cli.list_autonomous_database_clones, "list-clones")

# Exadata shape prefix.
# Example for Exadata shapes: Exadata.Quarter1.84, Exadata.Half1.168, ExadataCC.Base3.48, ExadataCC.Quarter3.100
EXADATA_SHAPE_PREFIX = 'Exadata'

# Cloud Vm Cluster id prefix
CLOUD_VM_CLUSTER_PREFIX = 'cloudvmcluster'
DB_SYSTEM_PREFIX = 'dbsystem'

cli_util.rename_command(database_cli, database_cli.autonomous_database_group, database_cli.create_autonomous_database_create_refreshable_autonomous_database_clone_details, "create-refreshable-clone")


@cli_util.copy_params_from_generated_command(database_cli.get_autonomous_database_wallet, params_to_exclude=['autonomous_database_id'])
@cli_util.option('--id', required=True, help="""The OCID of the Autonomous Database to get the wallet metadata for.""")
@database_cli.autonomous_database_wallet_group.command(name='get-metadata', help=database_cli.get_autonomous_database_wallet.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_wallet_metadata(ctx, **kwargs):
    if 'id' in kwargs and kwargs['id']:
        kwargs['autonomous_database_id'] = kwargs['id']

    del kwargs['id']

    ctx.invoke(database_cli.get_autonomous_database_wallet, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.update_autonomous_database_wallet, params_to_exclude=['autonomous_database_id'])
@cli_util.option('--id', required=True, help="""The OCID of the Autonomous Database to rotate the wallet for.""")
@database_cli.autonomous_database_wallet_group.command(name='rotate', help=database_cli.update_autonomous_database_wallet.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def rotate_wallet(ctx, **kwargs):
    if 'id' in kwargs and kwargs['id']:
        kwargs['autonomous_database_id'] = kwargs['id']

    del kwargs['id']

    ctx.invoke(database_cli.update_autonomous_database_wallet, **kwargs)


# Rename from:
# oci db autonomous-database deregister-autonomous-database-data-safe
# oci db autonomous-database register-autonomous-database-data-safe --autonomous-database-id
# To:
# oci db autonomous-database data-safe register
# oci db autonomous-database data-safe deregister
@click.command('data-safe', cls=CommandGroupWithAlias, help="""The Data Safe to use with this Autonomous Database.""")
@cli_util.help_option_group
def autonomous_database_data_safe_group():
    pass


database_cli.autonomous_database_group.add_command(autonomous_database_data_safe_group)
autonomous_database_data_safe_group.add_command(database_cli.register_autonomous_database_data_safe)
autonomous_database_data_safe_group.add_command(database_cli.deregister_autonomous_database_data_safe)
database_cli.autonomous_database_group.commands.pop(database_cli.register_autonomous_database_data_safe.name)
database_cli.autonomous_database_group.commands.pop(database_cli.deregister_autonomous_database_data_safe.name)
cli_util.rename_command(database_cli, autonomous_database_data_safe_group, database_cli.register_autonomous_database_data_safe, "register")
cli_util.rename_command(database_cli, autonomous_database_data_safe_group, database_cli.deregister_autonomous_database_data_safe, "deregister")

# Rename from:
# oci db autonomous-database enable-autonomous-database-operations-insights
# oci db autonomous-database disable-autonomous-database-operations-insights
# To:
# oci db autonomous-database operations-insights enable
# oci db autonomous-database operations-insights disable
cli_util.rename_command(database_cli, database_cli.autonomous_database_group, database_cli.enable_autonomous_database_operations_insights, "enable-operations-insights")
cli_util.rename_command(database_cli, database_cli.autonomous_database_group, database_cli.disable_autonomous_database_operations_insights, "disable-operations-insights")


@cli_util.copy_params_from_generated_command(database_cli.launch_db_system_launch_db_system_details, params_to_exclude=['db_home', 'db_system_options', 'ssh_public_keys', 'storage_volume_performance_mode', 'data_collection_options'])
@database_cli.db_system_group.command(name='launch', help=database_cli.launch_db_system_launch_db_system_details.help)
@cli_util.option('--admin-password', required=True, help="""A strong password for SYS, SYSTEM, and PDB Admin. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, #, or -.""")
@cli_util.option('--character-set', help="""The character set for the database. The default is AL32UTF8. Allowed values are: AL32UTF8, AR8ADOS710, AR8ADOS720, AR8APTEC715, AR8ARABICMACS, AR8ASMO8X, AR8ISO8859P6, AR8MSWIN1256, AR8MUSSAD768, AR8NAFITHA711, AR8NAFITHA721, AR8SAKHR706, AR8SAKHR707, AZ8ISO8859P9E, BG8MSWIN, BG8PC437S, BLT8CP921, BLT8ISO8859P13, BLT8MSWIN1257, BLT8PC775, BN8BSCII, CDN8PC863, CEL8ISO8859P14, CL8ISO8859P5, CL8ISOIR111, CL8KOI8R, CL8KOI8U, CL8MACCYRILLICS, CL8MSWIN1251, EE8ISO8859P2, EE8MACCES, EE8MACCROATIANS, EE8MSWIN1250, EE8PC852, EL8DEC, EL8ISO8859P7, EL8MACGREEKS, EL8MSWIN1253, EL8PC437S, EL8PC851, EL8PC869, ET8MSWIN923, HU8ABMOD, HU8CWI2, IN8ISCII, IS8PC861, IW8ISO8859P8, IW8MACHEBREWS, IW8MSWIN1255, IW8PC1507, JA16EUC, JA16EUCTILDE, JA16SJIS, JA16SJISTILDE, JA16VMS, KO16KSC5601, KO16KSCCS, KO16MSWIN949, LA8ISO6937, LA8PASSPORT, LT8MSWIN921, LT8PC772, LT8PC774, LV8PC1117, LV8PC8LR, LV8RST104090, N8PC865, NE8ISO8859P10, NEE8ISO8859P4, RU8BESTA, RU8PC855, RU8PC866, SE8ISO8859P3, TH8MACTHAIS, TH8TISASCII, TR8DEC, TR8MACTURKISHS, TR8MSWIN1254, TR8PC857, US7ASCII, US8PC437, UTF8, VN8MSWIN1258, VN8VN3, WE8DEC, WE8DG, WE8ISO8859P1, WE8ISO8859P15, WE8ISO8859P9, WE8MACROMAN8S, WE8MSWIN1252, WE8NCR4970, WE8NEXTSTEP, WE8PC850, WE8PC858, WE8PC860, WE8ROMAN8, ZHS16CGB231280, ZHS16GBK, ZHT16BIG5, ZHT16CCDC, ZHT16DBT, ZHT16HKSCS, ZHT16MSWIN950, ZHT32EUC, ZHT32SOPS, ZHT32TRIS.""")
@cli_util.option('--db-name', required=True, help="""The database name. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted.""")
@cli_util.option('--db-unique-name', required=False, help="""The database unique name. It must be greater than 3 characters, but at most 30 characters, begin with a letter, and contain only letters, numbers, and underscores. The first eight characters must also be unique within a Database Domain and within a Database System or VM Cluster. In addition, if it is not on a VM Cluster it might either be identical to the database name or prefixed by the datbase name and followed by an underscore.""")
@cli_util.option('--db-version', required=True, help="""A valid Oracle database version. To get a list of supported versions, use the command 'oci db version list'.""")
@cli_util.option('--tde-wallet-password', help="""The optional password to open the TDE wallet. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numeric, and two special characters. The special characters must be _, #, or -.""")
@cli_util.option('--db-workload', help="""Database workload type. Allowed values are: OLTP, DSS""")
@cli_util.option('--ncharacter-set', help="""National character set for the database. The default is AL16UTF16. Allowed values are: AL16UTF16 or UTF8.""")
@cli_util.option('--pdb-name', help="""Pluggable database name. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted. Pluggable database should not be same as database name.""")
@cli_util.option('--auto-backup-enabled', type=click.BOOL, help="""If set to true, schedules backups automatically. Default is false.""")
@cli_util.option('--recovery-window-in-days', type=click.IntRange(1, 60), help="""The number of days between the current and the earliest point of recoverability covered by automatic backups (1 to 60).""")
@cli_util.option('--ssh-authorized-keys-file', required=True, type=click.File('r'), help="""A file containing one or more public SSH keys to use for SSH access to the DB System. Use a newline character to separate multiple keys. The length of the combined keys cannot exceed 10,000 characters.""")
@cli_util.option('--storage-management', type=custom_types.CliCaseInsensitiveChoice(["LVM", "ASM"]), help="""Option for storage management for the database system. Allowed values are: LVM, ASM.""")
@cli_util.option('--database-software-image-id', required=False, help="""The OCID of database software image. This Custom Database Software Image will be used to create the database instead of Oracle-published Database Software Images""")
@cli_util.option('--storage-performance', type=custom_types.CliCaseInsensitiveChoice(["BALANCED", "HIGH_PERFORMANCE"]), help=u"""The block storage volume performance level. Valid values are `BALANCED` and `HIGH_PERFORMANCE`. See [Block Volume Performance] for more information.""")
@cli_util.option('--vault-id', required=False, help="""The OCID of the Oracle Cloud Infrastructure vault.""")
@cli_util.option('--is-diagnostics-events-enabled', required=False, type=click.BOOL, help="""Enables customer to receive Events service notifications for guest VM issues""")
@cli_util.option('--is-health-monitoring-enabled', required=False, type=click.BOOL, help="""Enables Oracle to receive diagnostic data and share it with its operations and support personnel""")
@cli_util.option('--is-incident-logs-enabled', required=False, type=click.BOOL, help="""Enables Oracle to receive Events service notifications for guest VM issues, collect incident logs and traces""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fault-domains': {'module': 'database', 'class': 'list[string]'}, 'nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'backup-network-nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'maintenance-window-details': {'module': 'database', 'class': 'MaintenanceWindow'}}, output_type={'module': 'database', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def launch_db_system_extended(ctx, **kwargs):
    create_db_home_details = {}
    create_db_system_options = {}

    if 'db_version' in kwargs and kwargs['db_version']:
        create_db_home_details['dbVersion'] = kwargs['db_version']

    if 'database_software_image_id' in kwargs and kwargs['database_software_image_id']:
        create_db_home_details['databaseSoftwareImageId'] = kwargs['database_software_image_id']

    create_database_details = {}
    if 'admin_password' in kwargs and kwargs['admin_password']:
        create_database_details['adminPassword'] = kwargs['admin_password']

    if 'tde_wallet_password' in kwargs and kwargs['tde_wallet_password']:
        create_database_details['tde_wallet_password'] = kwargs['tde_wallet_password']

    if 'character_set' in kwargs and kwargs['character_set']:
        create_database_details['characterSet'] = kwargs['character_set']

    if 'db_name' in kwargs and kwargs['db_name']:
        create_database_details['dbName'] = kwargs['db_name']

    if 'db_unique_name' in kwargs and kwargs['db_unique_name']:
        create_database_details['db_unique_name'] = kwargs['db_unique_name']

    if 'db_workload' in kwargs and kwargs['db_workload']:
        create_database_details['dbWorkload'] = kwargs['db_workload']

    if 'ncharacter_set' in kwargs and kwargs['ncharacter_set']:
        create_database_details['ncharacterSet'] = kwargs['ncharacter_set']

    if 'pdb_name' in kwargs and kwargs['pdb_name']:
        create_database_details['pdbName'] = kwargs['pdb_name']

    if 'vault_id' in kwargs and kwargs['vault_id']:
        create_database_details['vaultId'] = kwargs['vault_id']

    if 'kms_key_id' in kwargs and kwargs['kms_key_id']:
        create_database_details['kmsKeyId'] = kwargs['kms_key_id']

    if 'kms_key_version_id' in kwargs and kwargs['kms_key_version_id']:
        create_database_details['kmsKeyVersionId'] = kwargs['kms_key_version_id']

    if kwargs['auto_backup_enabled'] is not None or kwargs['recovery_window_in_days'] is not None:
        db_backup_config = {}
        if kwargs['auto_backup_enabled'] is not None:
            db_backup_config['autoBackupEnabled'] = kwargs['auto_backup_enabled']
        if kwargs['recovery_window_in_days'] is not None:
            db_backup_config['recoveryWindowInDays'] = kwargs['recovery_window_in_days']
        create_database_details['db_backup_config'] = db_backup_config
    create_db_home_details['database'] = create_database_details

    kwargs['db_home'] = json.dumps(create_db_home_details)

    if 'ssh_authorized_keys_file' in kwargs and kwargs['ssh_authorized_keys_file']:
        content = [line.rstrip('\n') for line in kwargs['ssh_authorized_keys_file']]
        kwargs['ssh_public_keys'] = json.dumps(content)

    if 'storage_management' in kwargs and kwargs['storage_management']:
        create_db_system_options['storage_management'] = kwargs['storage_management']

    if create_db_system_options:
        kwargs['db_system_options'] = json.dumps(create_db_system_options)

    if 'storage_performance' in kwargs:
        kwargs['storage_volume_performance_mode'] = kwargs['storage_performance']
        kwargs.pop('storage_performance')

    data_collection_options = {}
    if 'is_diagnostics_events_enabled' in kwargs and kwargs['is_diagnostics_events_enabled'] is not None:
        data_collection_options['is_diagnostics_events_enabled'] = kwargs['is_diagnostics_events_enabled']

    if 'is_health_monitoring_enabled' in kwargs and kwargs['is_health_monitoring_enabled'] is not None:
        data_collection_options['is_health_monitoring_enabled'] = kwargs['is_health_monitoring_enabled']

    if 'is_incident_logs_enabled' in kwargs and kwargs['is_incident_logs_enabled'] is not None:
        data_collection_options['is_incident_logs_enabled'] = kwargs['is_incident_logs_enabled']

    if len(data_collection_options) > 0:
        kwargs['data_collection_options'] = json.dumps(data_collection_options)

    # remove all of the kwargs that launch_db_system wont recognize
    del kwargs['admin_password']
    del kwargs['tde_wallet_password']
    del kwargs['character_set']
    del kwargs['db_unique_name']
    del kwargs['db_name']
    del kwargs['db_version']
    del kwargs['db_workload']
    del kwargs['ncharacter_set']
    del kwargs['pdb_name']
    del kwargs['ssh_authorized_keys_file']
    del kwargs['auto_backup_enabled']
    del kwargs['recovery_window_in_days']
    del kwargs['storage_management']
    del kwargs['database_software_image_id']
    del kwargs['vault_id']
    del kwargs['kms_key_id']
    del kwargs['kms_key_version_id']
    del kwargs['is_diagnostics_events_enabled']
    del kwargs['is_health_monitoring_enabled']
    del kwargs['is_incident_logs_enabled']

    ctx.invoke(database_cli.launch_db_system_launch_db_system_details, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.launch_db_system_launch_db_system_from_backup_details, params_to_exclude=['db_home', 'db_system_options', 'ssh_public_keys', 'storage_volume_performance_mode', 'data_collection_options'])
@database_cli.db_system_group.command(name='launch-from-backup', help=database_cli.launch_db_system_launch_db_system_from_backup_details.help)
@cli_util.option('--admin-password', required=True, help="""A strong password for SYS, SYSTEM, and PDB Admin. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, #, or -.""")
@cli_util.option('--backup-id', required=True, help="""The backup OCID.""")
@cli_util.option('--backup-tde-password', required=False, help="""The password to open the TDE wallet.""")
@cli_util.option('--db-name', required=False, help="""The display name of the database to be created from the backup. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted.""")
@cli_util.option('--db-unique-name', required=False, help="""The database unique name. It must be greater than 3 characters, but at most 30 characters, begin with a letter, and contain only letters, numbers, and underscores. The first eight characters must also be unique within a Database Domain and within a Database System or VM Cluster. In addition, if it is not on a VM Cluster it might either be identical to the database name or prefixed by the datbase name and followed by an underscore.""")
@cli_util.option('--ssh-authorized-keys-file', required=True, type=click.File('r'), help="""A file containing one or more public SSH keys to use for SSH access to the DB System. Use a newline character to separate multiple keys. The length of the combined keys cannot exceed 10,000 characters.""")
@cli_util.option('--storage-management', type=custom_types.CliCaseInsensitiveChoice(["LVM", "ASM"]), help="""Option for storage management for the database system. Allowed values are: LVM, ASM.""")
@cli_util.option('--database-software-image-id', required=False, help="""The OCID of database software image. This Custom Database Software Image will be used to create the database instead of Oracle-published Database Software Images""")
@cli_util.option('--storage-performance', type=custom_types.CliCaseInsensitiveChoice(["BALANCED", "HIGH_PERFORMANCE"]), help=u"""The block storage volume performance level. Valid values are `BALANCED` and `HIGH_PERFORMANCE`. See [Block Volume Performance] for more information.""")
@cli_util.option('--is-diagnostics-events-enabled', required=False, type=click.BOOL, help="""Enables customer to receive Events service notifications for guest VM issues""")
@cli_util.option('--is-health-monitoring-enabled', required=False, type=click.BOOL, help="""Enables Oracle to receive diagnostic data and share it with its operations and support personnel""")
@cli_util.option('--is-incident-logs-enabled', required=False, type=click.BOOL, help="""Enables Oracle to receive Events service notifications for guest VM issues, collect incident logs and traces""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fault-domains': {'module': 'database', 'class': 'list[string]'}, 'nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'backup-network-nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def launch_db_system_backup_extended(ctx, **kwargs):

    create_database_details = {}
    create_db_system_options = {}

    if 'admin_password' in kwargs and kwargs['admin_password']:
        create_database_details['adminPassword'] = kwargs['admin_password']

    if 'backup_id' in kwargs and kwargs['backup_id']:
        create_database_details['backupId'] = kwargs['backup_id']

    if 'backup_tde_password' in kwargs and kwargs['backup_tde_password']:
        create_database_details['backupTDEPassword'] = kwargs['backup_tde_password']

    if 'db_name' in kwargs and kwargs['db_name']:
        create_database_details['dbName'] = kwargs['db_name']

    if 'db_unique_name' in kwargs and kwargs['db_unique_name']:
        create_database_details['db_unique_name'] = kwargs['db_unique_name']

    create_db_home_details = {}
    create_db_home_details['database'] = create_database_details

    if 'database_software_image_id' in kwargs and kwargs['database_software_image_id']:
        create_db_home_details['databaseSoftwareImageId'] = kwargs['database_software_image_id']

    kwargs['db_home'] = json.dumps(create_db_home_details)

    if 'ssh_authorized_keys_file' in kwargs and kwargs['ssh_authorized_keys_file']:
        content = [line.rstrip('\n') for line in kwargs['ssh_authorized_keys_file']]
        kwargs['ssh_public_keys'] = json.dumps(content)

    if 'storage_management' in kwargs and kwargs['storage_management']:
        create_db_system_options['storage_management'] = kwargs['storage_management']

    if create_db_system_options:
        kwargs['db_system_options'] = json.dumps(create_db_system_options)

    if 'storage_performance' in kwargs:
        kwargs['storage_volume_performance_mode'] = kwargs['storage_performance']
        kwargs.pop('storage_performance')

    data_collection_options = {}
    if 'is_diagnostics_events_enabled' in kwargs and kwargs['is_diagnostics_events_enabled'] is not None:
        data_collection_options['is_diagnostics_events_enabled'] = kwargs['is_diagnostics_events_enabled']

    if 'is_health_monitoring_enabled' in kwargs and kwargs['is_health_monitoring_enabled'] is not None:
        data_collection_options['is_health_monitoring_enabled'] = kwargs['is_health_monitoring_enabled']

    if 'is_incident_logs_enabled' in kwargs and kwargs['is_incident_logs_enabled'] is not None:
        data_collection_options['is_incident_logs_enabled'] = kwargs['is_incident_logs_enabled']

    if len(data_collection_options) > 0:
        kwargs['data_collection_options'] = json.dumps(data_collection_options)

    # remove all of the kwargs that launch_db_system wont recognize
    del kwargs['db_unique_name']
    del kwargs['admin_password']
    del kwargs['backup_id']
    del kwargs['backup_tde_password']
    del kwargs['ssh_authorized_keys_file']
    del kwargs['db_name']
    del kwargs['storage_management']
    del kwargs['database_software_image_id']
    del kwargs['is_diagnostics_events_enabled']
    del kwargs['is_health_monitoring_enabled']
    del kwargs['is_incident_logs_enabled']

    ctx.invoke(database_cli.launch_db_system_launch_db_system_from_backup_details, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.launch_db_system_launch_db_system_from_database_details, params_to_exclude=['storage_volume_performance_mode', 'data_collection_options'])
@database_cli.db_system_group.command(name='launch-from-database', help=database_cli.launch_db_system_launch_db_system_from_database_details.help)
@cli_util.option('--storage-performance', type=custom_types.CliCaseInsensitiveChoice(["BALANCED", "HIGH_PERFORMANCE"]), help=u"""The block storage volume performance level. Valid values are `BALANCED` and `HIGH_PERFORMANCE`. See [Block Volume Performance] for more information.""")
@cli_util.option('--is-diagnostics-events-enabled', required=False, type=click.BOOL, help="""Enables customer to receive Events service notifications for guest VM issues""")
@cli_util.option('--is-health-monitoring-enabled', required=False, type=click.BOOL, help="""Enables Oracle to receive diagnostic data and share it with its operations and support personnel""")
@cli_util.option('--is-incident-logs-enabled', required=False, type=click.BOOL, help="""Enables Oracle to receive Events service notifications for guest VM issues, collect incident logs and traces""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fault-domains': {'module': 'database', 'class': 'list[string]'}, 'nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'backup-network-nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'db-system-options': {'module': 'database', 'class': 'DbSystemOptions'}, 'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'db-home': {'module': 'database', 'class': 'CreateDbHomeFromDatabaseDetails'}}, output_type={'module': 'database', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def launch_db_system_from_database_extended(ctx, **kwargs):

    if 'storage_performance' in kwargs:
        kwargs['storage_volume_performance_mode'] = kwargs['storage_performance']
        kwargs.pop('storage_performance')

    data_collection_options = {}
    if 'is_diagnostics_events_enabled' in kwargs and kwargs['is_diagnostics_events_enabled'] is not None:
        data_collection_options['is_diagnostics_events_enabled'] = kwargs['is_diagnostics_events_enabled']

    if 'is_health_monitoring_enabled' in kwargs and kwargs['is_health_monitoring_enabled'] is not None:
        data_collection_options['is_health_monitoring_enabled'] = kwargs['is_health_monitoring_enabled']

    if 'is_incident_logs_enabled' in kwargs and kwargs['is_incident_logs_enabled'] is not None:
        data_collection_options['is_incident_logs_enabled'] = kwargs['is_incident_logs_enabled']

    if len(data_collection_options) > 0:
        kwargs['data_collection_options'] = json.dumps(data_collection_options)

    # remove all of the kwargs that launch_db_system wont recognize
    del kwargs['is_diagnostics_events_enabled']
    del kwargs['is_health_monitoring_enabled']
    del kwargs['is_incident_logs_enabled']

    ctx.invoke(database_cli.launch_db_system_launch_db_system_from_database_details, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.create_db_home, params_to_exclude=['database', 'display_name', 'db_version'])
@database_cli.database_group.command(name='create', help="""Creates a new database in the given DB System.""")
@cli_util.option('--admin-password', required=True, help="""A strong password for SYS, SYSTEM, and PDB Admin. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, #, or -.""")
@cli_util.option('--db-home-id', required=False, help="""The Db Home Id to create this database under.""")
@cli_util.option('--db-system-id', required=False, help="""The Db System Id to create this database under. Either --db-system-id or --vm-cluster-id must be specified, but if both are passed, --vm-cluster-id will be ignored.""")
@cli_util.option('--vm-cluster-id', required=False, help="""The Vm Cluster Id to create this database under. Either --db-system-id or --vm-cluster-id must be specified, but if both are passed, --vm-cluster-id will be ignored.""")
@cli_util.option('--character-set', help="""The character set for the database. The default is AL32UTF8. Allowed values are: AL32UTF8, AR8ADOS710, AR8ADOS720, AR8APTEC715, AR8ARABICMACS, AR8ASMO8X, AR8ISO8859P6, AR8MSWIN1256, AR8MUSSAD768, AR8NAFITHA711, AR8NAFITHA721, AR8SAKHR706, AR8SAKHR707, AZ8ISO8859P9E, BG8MSWIN, BG8PC437S, BLT8CP921, BLT8ISO8859P13, BLT8MSWIN1257, BLT8PC775, BN8BSCII, CDN8PC863, CEL8ISO8859P14, CL8ISO8859P5, CL8ISOIR111, CL8KOI8R, CL8KOI8U, CL8MACCYRILLICS, CL8MSWIN1251, EE8ISO8859P2, EE8MACCES, EE8MACCROATIANS, EE8MSWIN1250, EE8PC852, EL8DEC, EL8ISO8859P7, EL8MACGREEKS, EL8MSWIN1253, EL8PC437S, EL8PC851, EL8PC869, ET8MSWIN923, HU8ABMOD, HU8CWI2, IN8ISCII, IS8PC861, IW8ISO8859P8, IW8MACHEBREWS, IW8MSWIN1255, IW8PC1507, JA16EUC, JA16EUCTILDE, JA16SJIS, JA16SJISTILDE, JA16VMS, KO16KSC5601, KO16KSCCS, KO16MSWIN949, LA8ISO6937, LA8PASSPORT, LT8MSWIN921, LT8PC772, LT8PC774, LV8PC1117, LV8PC8LR, LV8RST104090, N8PC865, NE8ISO8859P10, NEE8ISO8859P4, RU8BESTA, RU8PC855, RU8PC866, SE8ISO8859P3, TH8MACTHAIS, TH8TISASCII, TR8DEC, TR8MACTURKISHS, TR8MSWIN1254, TR8PC857, US7ASCII, US8PC437, UTF8, VN8MSWIN1258, VN8VN3, WE8DEC, WE8DG, WE8ISO8859P1, WE8ISO8859P15, WE8ISO8859P9, WE8MACROMAN8S, WE8MSWIN1252, WE8NCR4970, WE8NEXTSTEP, WE8PC850, WE8PC858, WE8PC860, WE8ROMAN8, ZHS16CGB231280, ZHS16GBK, ZHT16BIG5, ZHT16CCDC, ZHT16DBT, ZHT16HKSCS, ZHT16MSWIN950, ZHT32EUC, ZHT32SOPS, ZHT32TRIS.""")
@cli_util.option('--db-name', required=True, help="""The database name. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted.""")
@cli_util.option('--db-unique-name', required=False, help="""The database unique name. It must be greater than 3 characters, but at most 30 characters, begin with a letter, and contain only letters, numbers, and underscores. The first eight characters must also be unique within a Database Domain and within a Database System or VM Cluster. In addition, if it is not on a VM Cluster it might either be identical to the database name or prefixed by the database name and followed by an underscore.""")
@cli_util.option('--sid-prefix', required=False, help="""Specifies a prefix for the `Oracle SID` of the database to be created.""")
@cli_util.option('--tde-wallet-password', help="""The optional password to open the TDE wallet. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numeric, and two special characters. The special characters must be _, #, or -.""")
@cli_util.option('--db-workload', type=custom_types.CliCaseInsensitiveChoice(["OLTP", "DSS"]), help="""Database workload type. Allowed values are: OLTP, DSS""")
@cli_util.option('--ncharacter-set', help="""National character set for the database. The default is AL16UTF16. Allowed values are: AL16UTF16 or UTF8.""")
@cli_util.option('--pdb-name', help="""Pluggable database name. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted. Pluggable database should not be same as database name.""")
@cli_util.option('--db-version', required=False, help="""A valid Oracle database version. To get a list of supported versions, use the command 'oci db version list'.""")
@cli_util.option('--auto-backup-enabled', type=click.BOOL, help="""If set to true, schedules backups automatically. Default is false.""")
@cli_util.option('--recovery-window-in-days', type=click.IntRange(1, 60), help="""The number of days between the current and the earliest point of recoverability covered by automatic backups (1 to 60).""")
@cli_util.option('--auto-backup-window', required=False, help="""Specifying a two hour slot when the backup should kick in eg:- SLOT_ONE,SLOT_TWO. Default is anytime""")
@cli_util.option('--backup-destination', required=False, type=custom_types.CLI_COMPLEX_TYPE, help="""backup destination list""")
@cli_util.option('--vault-id', required=False, help="""The OCID of the Oracle Cloud Infrastructure vault.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backup-destination': {'module': 'database', 'class': 'list[BackupDestinationDetails]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'DatabaseSummary'})
@cli_util.wrap_exceptions
def create_database(ctx, wait_for_state, max_wait_seconds, wait_interval_seconds, **kwargs):
    if kwargs['db_home_id'] is None and kwargs['db_version'] is None:
        click.echo(message="Missing a required parameter. Either --db-home-id or --db-version must be specified.", file=sys.stderr)
        sys.exit(1)

    if 'db_system_id' in kwargs and kwargs['db_system_id']:
        create_db_home_details = oci.database.models.CreateDbHomeWithDbSystemIdDetails()
        create_db_home_details.db_system_id = kwargs['db_system_id']
    else:
        if 'vm_cluster_id' in kwargs and kwargs['vm_cluster_id']:
            create_db_home_details = oci.database.models.CreateDbHomeWithVmClusterIdDetails()
            create_db_home_details.vm_cluster_id = kwargs['vm_cluster_id']
        else:
            click.echo(message="Missing a required parameter. Either --db-system-id or --vm-cluster-id must be specified.", file=sys.stderr)
            sys.exit(1)

    if 'database_software_image_id' in kwargs and kwargs['database_software_image_id']:
        create_db_home_details.database_software_image_id = kwargs['database_software_image_id']

    if 'is_desupported_version' in kwargs and kwargs['is_desupported_version']:
        create_db_home_details.is_desupported_version = kwargs['is_desupported_version']

    db_backup_config = oci.database.models.DbBackupConfig()

    create_database_details = oci.database.models.CreateDatabaseDetails()
    if 'admin_password' in kwargs and kwargs['admin_password']:
        create_database_details.admin_password = kwargs['admin_password']

    if 'tde_wallet_password' in kwargs and kwargs['tde_wallet_password']:
        create_database_details.tde_wallet_password = kwargs['tde_wallet_password']

    if 'character_set' in kwargs and kwargs['character_set']:
        create_database_details.character_set = kwargs['character_set']

    if 'db_name' in kwargs and kwargs['db_name']:
        create_database_details.db_name = kwargs['db_name']

    if 'db_unique_name' in kwargs and kwargs['db_unique_name']:
        create_database_details.db_unique_name = kwargs['db_unique_name']

    if 'sid_prefix' in kwargs and kwargs['sid_prefix']:
        create_database_details.sid_prefix = kwargs['sid_prefix']

    if 'db_workload' in kwargs and kwargs['db_workload']:
        create_database_details.db_workload = kwargs['db_workload']

    if 'backup_destination' in kwargs and kwargs['backup_destination']:
        db_backup_config.backup_destination_details = cli_util.parse_json_parameter("backup_destination_details", kwargs['backup_destination'])

    if 'ncharacter_set' in kwargs and kwargs['ncharacter_set']:
        create_database_details.ncharacter_set = kwargs['ncharacter_set']

    if 'pdb_name' in kwargs and kwargs['pdb_name']:
        create_database_details.pdb_name = kwargs['pdb_name']

    if 'defined_tags' in kwargs and kwargs['defined_tags']:
        create_database_details.defined_tags = kwargs['defined_tags']

    if 'freeform_tags' in kwargs and kwargs['freeform_tags']:
        create_database_details.freeform_tags = kwargs['freeform_tags']

    if 'vault_id' in kwargs and kwargs['vault_id']:
        create_database_details['vaultId'] = kwargs['vault_id']

    if 'kms_key_id' in kwargs and kwargs['kms_key_id']:
        create_database_details['kmsKeyId'] = kwargs['kms_key_id']

    if 'kms_key_version_id' in kwargs and kwargs['kms_key_version_id']:
        create_database_details['kmsKeyVersionId'] = kwargs['kms_key_version_id']

    if 'auto-backup-window' in kwargs and kwargs['auto-backup-window'] and kwargs['auto_backup_enabled'] is not None:
        db_backup_config.auto_backup_enabled = kwargs['auto_backup_enabled']
        db_backup_config.auto_backup_window = kwargs['auto-backup-window']
        del kwargs['auto-backup-window']

    if kwargs['auto_backup_enabled'] is not None or kwargs['recovery_window_in_days'] is not None:
        if kwargs['auto_backup_enabled'] is not None:
            db_backup_config.auto_backup_enabled = kwargs['auto_backup_enabled']
        if kwargs['recovery_window_in_days'] is not None:
            db_backup_config.recoveryWindowInDays = kwargs['recovery_window_in_days']
    create_database_details.db_backup_config = db_backup_config
    del kwargs['auto_backup_enabled']
    del kwargs['recovery_window_in_days']
    del kwargs['backup_destination']
    del kwargs['vault_id']
    del kwargs['kms_key_id']
    del kwargs['kms_key_version_id']

    create_db_home_details.database = create_database_details
    if 'db_version' in kwargs and kwargs['db_version']:
        create_db_home_details.db_version = kwargs['db_version']

    client = cli_util.build_client('database', 'database', ctx)

    create_new_database_details = oci.database.models.CreateNewDatabaseDetails()
    if kwargs['db_home_id'] is not None:
        create_new_database_details.db_home_id = kwargs['db_home_id']
        create_new_database_details.database = create_database_details
        result = client.create_database(create_new_database_details)
        db_home_id = kwargs['db_home_id']
        compartment_id = result.data.compartment_id
    else:
        result = client.create_db_home(create_db_home_details)
        db_home_id = result.data.id
        compartment_id = result.data.compartment_id

    if wait_for_state:

        if hasattr(client, 'get_db_home') and callable(getattr(client, 'get_db_home')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_db_home(db_home_id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)

    # result is now the DbHome that was created, so we need to get the
    # corresponding database and print that out for the user
    try:
        result = client.list_databases(db_home_id=db_home_id, compartment_id=compartment_id)
    except oci.exceptions.ServiceError:
        click.echo("Successfully created database but failed to retrieve metadata. You can view the status of databases in this DB system by executing: oci db database list -c {comp_id} --db-system-id {db_sys_id} ".format(comp_id=compartment_id, db_sys_id=kwargs['db_system_id']), file=sys.stderr)
        sys.exit(1)

    # there is only one database per db-home
    # so just return the first database in this newly created db-home
    database = result.data[0]

    cli_util.render(database, None, ctx)


@cli_util.copy_params_from_generated_command(database_cli.create_db_home, params_to_exclude=['database', 'display_name', 'db_version', 'source'])
@database_cli.database_group.command(name='create-from-backup', help="""Creates a new database in the given DB System from a backup.""")
@cli_util.option('--vm-cluster-id', required=False, help="""The Vm Cluster Id to create this database under. Either --db-system-id or --vm-cluster-id must be specified, but if both are passed, --vm-cluster-id will be ignored.""")
@cli_util.option('--db-system-id', required=False, help="""The Db System Id to restore this database under. Either --db-system-id or --vm-cluster-id must be specified, but if both are passed, --vm-cluster-id will be ignored.""")
@cli_util.option('--admin-password', required=True, help="""A strong password for SYS, SYSTEM, and PDB Admin. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, #, or -.""")
@cli_util.option('--backup-id', required=True, help="""The backup OCID.""")
@cli_util.option('--backup-tde-password', required=False, help="""The password to open the TDE wallet.""")
@cli_util.option('--db-name', required=False, help="""The display name of the database to be created from the backup. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted.""")
@cli_util.option('--db-unique-name', required=False, help="""The database unique name. It must be greater than 3 characters, but at most 30 characters, begin with a letter, and contain only letters, numbers, and underscores. The first eight characters must also be unique within a Database Domain and within a Database System or VM Cluster. In addition, if it is not on a VM Cluster it might either be identical to the database name or prefixed by the datbase name and followed by an underscore.""")
@cli_util.option('--sid-prefix', required=False, help="""Specifies a prefix for the `Oracle SID` of the database to be created.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'DatabaseSummary'})
@cli_util.wrap_exceptions
def create_database_from_backup(ctx, wait_for_state, max_wait_seconds, wait_interval_seconds, **kwargs):

    if 'db_system_id' in kwargs and kwargs['db_system_id']:
        create_db_home_with_system_details = oci.database.models.CreateDbHomeWithDbSystemIdFromBackupDetails()
        create_db_home_with_system_details.db_system_id = kwargs['db_system_id']
        create_db_home_with_system_details.source = 'DB_BACKUP'

    else:
        if 'vm_cluster_id' in kwargs and kwargs['vm_cluster_id']:
            create_db_home_with_system_details = oci.database.models.CreateDbHomeWithVmClusterIdFromBackupDetails()
            create_db_home_with_system_details.vm_cluster_id = kwargs['vm_cluster_id']
            create_db_home_with_system_details.source = 'VM_CLUSTER_BACKUP'
        else:
            click.echo(message="Missing a required parameter. Either --db-system-id or --vm-cluster-id must be specified.", file=sys.stderr)
            sys.exit(1)

    create_database_details = oci.database.models.CreateDatabaseFromBackupDetails()
    if 'admin_password' in kwargs and kwargs['admin_password']:
        create_database_details.admin_password = kwargs['admin_password']

    if 'backup_id' in kwargs and kwargs['backup_id']:
        create_database_details.backup_id = kwargs['backup_id']

    if 'backup_tde_password' in kwargs and kwargs['backup_tde_password']:
        create_database_details.backup_tde_password = kwargs['backup_tde_password']

    if 'db_name' in kwargs and kwargs['db_name']:
        create_database_details.db_name = kwargs['db_name']

    if 'db_unique_name' in kwargs and kwargs['db_unique_name']:
        create_database_details.db_unique_name = kwargs['db_unique_name']

    if 'sid_prefix' in kwargs and kwargs['sid_prefix']:
        create_database_details.sid_prefix = kwargs['sid_prefix']

    if 'database_software_image_id' in kwargs and kwargs['database_software_image_id']:
        create_db_home_with_system_details.database_software_image_id = kwargs['database_software_image_id']

    if 'is_desupported_version' in kwargs and kwargs['is_desupported_version']:
        create_db_home_with_system_details.is_desupported_version = kwargs['is_desupported_version']

    create_db_home_with_system_details.database = create_database_details

    client = cli_util.build_client('database', 'database', ctx)

    result = client.create_db_home(create_db_home_with_system_details)

    db_home_id = result.data.id
    compartment_id = result.data.compartment_id

    if wait_for_state:

        if hasattr(client, 'get_db_home') and callable(getattr(client, 'get_db_home')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_db_home(db_home_id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)

    # result is now the DbHome that was created, so we need to get the
    # corresponding database and print that out for the user
    try:
        result = client.list_databases(db_home_id=db_home_id, compartment_id=compartment_id)
    except oci.exceptions.ServiceError:
        click.echo("Failed retrieving database info after successfully creation.  You can view the status of databases in this DB system by executing: oci db database list -c {comp_id} --db-system-id {db_sys_id} ".format(comp_id=compartment_id, db_sys_id=kwargs['db_system_id']), file=sys.stderr)
        sys.exit(1)

    # Return the first database in this newly created db-home
    database = result.data[0]

    cli_util.render(database, None, ctx)


@cli_util.copy_params_from_generated_command(database_cli.update_database, params_to_exclude=['db_backup_config'])
@database_cli.database_group.command(name='update', help="""Update a Database based on the request parameters you provide.""")
@cli_util.option('--auto-backup-enabled', type=click.BOOL, help="""If set to true, schedules backups automatically. Default is false.""")
@cli_util.option('--recovery-window-in-days', type=click.IntRange(1, 60), help="""The number of days between the current and the earliest point of recoverability covered by automatic backups (1 to 60).""")
@cli_util.option('--auto-backup-window', required=False, help="""Specifying a two hour slot when the backup should kick in eg:- SLOT_ONE,SLOT_TWO. Default is anytime""")
@cli_util.option('--backup-destination', required=False, type=custom_types.CLI_COMPLEX_TYPE, help="""backup destination list""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backup-destination': {'module': 'database', 'class': 'list[BackupDestinationDetails]'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}}, output_type={'module': 'database', 'class': 'Database'})
@cli_util.wrap_exceptions
def update_database_extended(ctx, **kwargs):
    if kwargs['auto_backup_enabled'] is not None or kwargs['recovery_window_in_days'] is not None:
        db_backup_config = {}
        if 'auto_backup_window' in kwargs and kwargs['auto_backup_window'] and kwargs['auto_backup_enabled'] is not None:
            db_backup_config['autoBackupEnabled'] = kwargs['auto_backup_enabled']
            db_backup_config['autoBackupWindow'] = kwargs['auto_backup_window']
        if kwargs['auto_backup_enabled'] is not None:
            db_backup_config['autoBackupEnabled'] = kwargs['auto_backup_enabled']
        if kwargs['recovery_window_in_days'] is not None:
            db_backup_config['recoveryWindowInDays'] = kwargs['recovery_window_in_days']
        if 'backup_destination' in kwargs and kwargs['backup_destination']:
            db_backup_config['backupDestinationDetails'] = cli_util.parse_json_parameter("backup_destination_details", kwargs['backup_destination'])
        kwargs['db_backup_config'] = json.dumps(db_backup_config)

    del kwargs['auto_backup_enabled']
    del kwargs['recovery_window_in_days']
    del kwargs['auto_backup_window']
    del kwargs['backup_destination']

    ctx.invoke(database_cli.update_database, **kwargs)


# Creates a database from the settings of another existing database.
# This function was added so we could have this command structure -- "oci db database create-from-database".
# This is similar to what was done for create_database_from_backup.
# Db home is not exposed to the end user.
@cli_util.copy_params_from_generated_command(database_cli.create_db_home, params_to_exclude=['database', 'display_name', 'db_version', 'source'])
@database_cli.database_group.command(name='create-from-database', help="""Creates a new database in the given DB System from another database.""")
@cli_util.option('--db-system-id', required=False, help="""The Db System Id to clone this database under.""")
@cli_util.option('--admin-password', required=True, help="""A strong password for SYS, SYSTEM, and PDB Admin. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, #, or -.""")
@cli_util.option('--database-id', required=True, help="""The OCID of the from-database.""")
@cli_util.option('--backup-tde-password', required=False, help="""The password to open the TDE wallet.""")
@cli_util.option('--point-in-time-recovery-timestamp', required=False, help="""The point in time of the original database from which the new database is created. If not specifed, the latest backup is used to create the database.""")
@cli_util.option('--db-name', required=False, help="""The display name of the database to be created. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'DatabaseSummary'})
@cli_util.wrap_exceptions
def create_database_from_another_database(ctx, wait_for_state, max_wait_seconds, wait_interval_seconds, **kwargs):
    create_db_home_with_system_details = oci.database.models.CreateDbHomeWithDbSystemIdFromDatabaseDetails()
    create_database_details = oci.database.models.CreateDatabaseFromAnotherDatabaseDetails()
    if 'admin_password' in kwargs and kwargs['admin_password']:
        create_database_details.admin_password = kwargs['admin_password']

    if 'database_id' in kwargs and kwargs['database_id']:
        create_database_details.database_id = kwargs['database_id']

    if 'backup_tde_password' in kwargs and kwargs['backup_tde_password']:
        create_database_details.backup_tde_password = kwargs['backup_tde_password']

    if 'db_name' in kwargs and kwargs['db_name']:
        create_database_details.db_name = kwargs['db_name']

    if 'point_in_time_recovery_timestamp' in kwargs and kwargs['point_in_time_recovery_timestamp']:
        create_database_details.time_stamp_for_point_in_time_recovery = kwargs['point_in_time_recovery_timestamp']

    create_db_home_with_system_details.database = create_database_details

    if 'db_system_id' in kwargs and kwargs['db_system_id']:
        create_db_home_with_system_details.db_system_id = kwargs['db_system_id']

    if 'database_software_image_id' in kwargs and kwargs['database_software_image_id']:
        create_db_home_with_system_details.database_software_image_id = kwargs['database_software_image_id']

    if 'is_desupported_version' in kwargs and kwargs['is_desupported_version']:
        create_db_home_with_system_details.is_desupported_version = kwargs['is_desupported_version']

    create_db_home_with_system_details.source = 'DATABASE'

    client = cli_util.build_client('database', 'database', ctx)

    result = client.create_db_home(create_db_home_with_system_details)

    db_home_id = result.data.id
    compartment_id = result.data.compartment_id

    if wait_for_state:

        if hasattr(client, 'get_db_home') and callable(getattr(client, 'get_db_home')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_db_home(db_home_id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)

    # result is now the DbHome that was created, so we need to get the
    # corresponding database and print that out for the user
    try:
        result = client.list_databases(db_home_id=db_home_id, compartment_id=compartment_id)
    except oci.exceptions.ServiceError:
        click.echo("Failed retrieving database info after successfully creation.  You can view the status of databases in this DB system by executing: oci db database list -c {comp_id} --db-system-id {db_sys_id} ".format(comp_id=compartment_id, db_sys_id=kwargs['db_system_id']), file=sys.stderr)
        sys.exit(1)

    # there is only one database per db-home
    # so just return the first database in this newly created db-home
    database = result.data[0]

    cli_util.render(database, None, ctx)


@database_cli.database_group.command(name='patch', help="""Perform a patch action for a given patch and database.""")
@cli_util.option('--database-id', required=True, help="""The OCID of the database.""")
@cli_util.option('--patch-action', required=False, help="""The action to perform on the patch.""")
@cli_util.option('--patch-id', required=False, help="""The OCID of the patch.""")
@cli_util.option('--one-off-patches', required=False, type=custom_types.CLI_COMPLEX_TYPE, help="""The list of one-off patches.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--database-software-image-id', required=False, help="""The OCID of the database software image.""")
@click.pass_context
@json_skeleton_utils.get_cli_json_input_option({'one-off-patches': {'module': 'database', 'class': 'list[string]'}})
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'one-off-patches': {'module': 'database', 'class': 'list[string]'}}, output_type={'module': 'database', 'class': 'Database'})
@cli_util.help_option
@cli_util.wrap_exceptions
def patch_database(ctx, **kwargs):
    client = cli_util.build_client('database', 'database', ctx)

    if (kwargs['one_off_patches'] is not None and (kwargs['database_software_image_id'] is not None or kwargs['patch_id'] is not None or kwargs['patch_action'] is not None)) or \
            (kwargs['database_software_image_id'] is not None and (kwargs['patch_action'] is None or kwargs['one_off_patches'] is not None or kwargs['patch_id'] is not None)) or \
            (kwargs['patch_id'] is not None and (kwargs['patch_action'] is None or kwargs['one_off_patches'] is not None or kwargs['database_software_image_id'] is not None)) or \
            (kwargs['patch_id'] is None and kwargs['one_off_patches'] is None and kwargs['database_software_image_id'] is None):
        click.echo(message="Please specify one of the three options. 1. '--one-off-patches',  2. '--database-software-image-id and --patch-action' or 3. '--patch-id and --patch-action'.", file=sys.stderr)
        sys.exit(1)

    response = client.get_database(kwargs['database_id'])
    db_home_id = response.data.db_home_id

    update_db_home_details = oci.database.models.UpdateDbHomeDetails()

    if kwargs['database_software_image_id'] is not None and kwargs['patch_action'] is not None:
        patch_details = oci.database.models.PatchDetails()
        patch_details.action = kwargs['patch_action']
        patch_details.database_software_image_id = kwargs['database_software_image_id']
        update_db_home_details.db_version = patch_details

    if kwargs['one_off_patches'] is not None:
        update_db_home_details.one_off_patches = cli_util.parse_json_parameter("one_off_patches", kwargs['one_off_patches'])

    if kwargs['patch_id'] is not None and kwargs['patch_action'] is not None:
        patch_details = oci.database.models.PatchDetails()
        patch_details.action = kwargs['patch_action']
        patch_details.patch_id = kwargs['patch_id']
        update_db_home_details.db_version = patch_details

    client.update_db_home(db_home_id, update_db_home_details)

    # update_db_home returns the DbHome, so we need to get the
    # corresponding database and print that out for the user
    result = client.get_database(kwargs['database_id'])
    database = result.data

    cli_util.render(database, None, ctx)


@database_cli.database_group.command(name='delete', help="""Deletes a database.""")
@cli_util.option('--database-id', required=True, help="""The OCID of the database to delete.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_database(ctx, **kwargs):
    client = cli_util.build_client('database', 'database', ctx)

    # get the db-home for this database
    response = client.get_database(kwargs['database_id'])
    db_home_id = response.data.db_home_id
    compartment_id = response.data.compartment_id

    # we only want to delete this single database, but the only API
    # available deletes the entire db-home, so check to make sure
    # this is the only database in the db-home before deleting
    response = client.get_db_home(db_home_id)
    vm_cluster_id = response.data.vm_cluster_id
    if vm_cluster_id is not None:
        if CLOUD_VM_CLUSTER_PREFIX in vm_cluster_id or DB_SYSTEM_PREFIX in vm_cluster_id:
            # If vm_cluster_id is not null and includes 'cloudvmcluster' or 'dbsystem' for migrated case
            # It is a cloud vm cluster and shape will be Exadata only
            db_system_shape = EXADATA_SHAPE_PREFIX

        else:
            # For Exacc db homes, vm_cluster_id will be not null
            get_db_system_response = client.get_vm_cluster(response.data.vm_cluster_id)
            db_system_shape = get_db_system_response.data.shape

    else:
        # For dbSystem db homes, db_system_id will be not null
        get_db_system_response = client.get_db_system(response.data.db_system_id)
        db_system_shape = get_db_system_response.data.shape

    response = client.list_databases(db_home_id=db_home_id, compartment_id=compartment_id)
    # For Exadata systems delete database is called
    if EXADATA_SHAPE_PREFIX in db_system_shape:
        response = client.delete_database(kwargs['database_id'])
    else:
        if len(response.data) != 1:
            click.echo(message="Cannot delete a DB Home which contains multiple databases through the CLI. Please use the console to delete this database.", file=sys.stderr)
            sys.exit(1)
        # delete DbHome
        response = client.delete_db_home(db_home_id)
    cli_util.render_response(response, ctx)


@cli_util.copy_params_from_generated_command(database_cli.list_db_homes, params_to_exclude=['db_home_id', 'page', 'all_pages', 'page_size', 'db_system_id', 'db_version'])
@database_cli.database_group.command(name='list', help="""Lists all databases in a given DB System.""")
@click.pass_context
@cli_util.option('--db-system-id', help="""The OCID of the db system to list within.""")
@cli_util.option('--vm-cluster-id', help="""The OCID of the vm cluster to list within.""")
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[DatabaseSummary]'})
@cli_util.wrap_exceptions
def list_databases(ctx, **kwargs):
    client = cli_util.build_client('database', 'database', ctx)

    if kwargs['db_system_id'] is not None and kwargs['compartment_id'] is None:
        response = client.get_db_system(kwargs['db_system_id'])
        compartment_id = response.data.compartment_id
    else:
        if kwargs['compartment_id'] is None:
            click.echo(message="Could not determine compartment_id from db_system_id and wasn't provided by caller.", file=sys.stderr)
            sys.exit(1)
        else:
            compartment_id = kwargs['compartment_id']

    list_db_home_kw_args = {'db_system_id': kwargs['db_system_id'], 'vm_cluster_id': kwargs['vm_cluster_id']}
    response = client.list_db_homes(compartment_id, **list_db_home_kw_args)
    db_homes = response.data
    while response.has_next_page:
        if response.next_page is not None:
            list_db_home_kw_args['page'] = response.next_page

        response = client.list_db_homes(compartment_id, **list_db_home_kw_args)

        if response.data is not None:
            db_homes += response.data

    list_db_kw_args = {}
    if kwargs['sort_by'] is not None:
        list_db_kw_args['sort_by'] = kwargs['sort_by']
    if kwargs['sort_order'] is not None:
        list_db_kw_args['sort_order'] = kwargs['sort_order']
    if kwargs['lifecycle_state'] is not None:
        list_db_kw_args['lifecycle_state'] = kwargs['lifecycle_state']
    if kwargs['display_name'] is not None:
        list_db_kw_args['db_name'] = kwargs['display_name']

    # go through all db_homes and list all dbs
    databases = []
    for db_home in db_homes:
        if 'limit' in kwargs and kwargs['limit'] is not None and len(databases) >= int(kwargs['limit']):
            break

        response = client.list_databases(compartment_id=compartment_id, db_home_id=db_home.id, **list_db_kw_args)
        if response.data is not None:
            for database in response.data:
                if 'limit' in kwargs and kwargs['limit'] is not None and len(databases) >= int(kwargs['limit']):
                    break

                databases.append(database)

    cli_util.render(databases, None, ctx)


@cli_util.copy_params_from_generated_command(database_cli.db_node_action, params_to_exclude=['action'])
@database_cli.db_node_group.command(name='start', help="""Powers on the specified DB node.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DbNode'})
@cli_util.wrap_exceptions
def db_node_start(ctx, **kwargs):
    kwargs['action'] = 'start'
    ctx.invoke(database_cli.db_node_action, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.db_node_action, params_to_exclude=['action'])
@database_cli.db_node_group.command(name='stop', help="""Powers off the specified DB node.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DbNode'})
@cli_util.wrap_exceptions
def db_node_stop(ctx, **kwargs):
    kwargs['action'] = 'stop'
    ctx.invoke(database_cli.db_node_action, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.db_node_action, params_to_exclude=['action'])
@database_cli.db_node_group.command(name='soft-reset', help="""Performs an ACPI shutdown and powers on the specified DB node.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DbNode'})
@cli_util.wrap_exceptions
def db_node_softreset(ctx, **kwargs):
    kwargs['action'] = 'softreset'
    ctx.invoke(database_cli.db_node_action, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.db_node_action, params_to_exclude=['action'])
@database_cli.db_node_group.command(name='reset', help="""Powers off and powers on the specified DB node.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DbNode'})
@cli_util.wrap_exceptions
def db_node_reset(ctx, **kwargs):
    kwargs['action'] = 'reset'
    ctx.invoke(database_cli.db_node_action, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.update_db_system, params_to_exclude=['ssh_public_keys', 'version_parameterconflict', 'data_collection_options'])
@database_cli.db_system_group.command(name='update', help=database_cli.update_db_system.help)
@cli_util.option('--patch-action', help="""The action to perform on the patch.""")
@cli_util.option('--patch-id', help="""The OCID of the patch.""")
@cli_util.option('--ssh-authorized-keys-file', type=click.File('r'), help="""A file containing one or more public SSH keys to use for SSH access to the DB System. Use a newline character to separate multiple keys. The length of the combined keys cannot exceed 10,000 characters.""")
@cli_util.option('--is-diagnostics-events-enabled', required=False, type=click.BOOL, help="""Enables customer to receive Events service notifications for guest VM issues""")
@cli_util.option('--is-health-monitoring-enabled', required=False, type=click.BOOL, help="""Enables Oracle to receive diagnostic data and share it with its operations and support personnel""")
@cli_util.option('--is-incident-logs-enabled', required=False, type=click.BOOL, help="""Enables Oracle to receive Events service notifications for guest VM issues, collect incident logs and traces""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'backup-network-nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'maintenance-window-details': {'module': 'database', 'class': 'MaintenanceWindow'}}, output_type={'module': 'database', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def update_db_system_extended(ctx, **kwargs):
    if 'ssh_authorized_keys_file' in kwargs and kwargs['ssh_authorized_keys_file']:
        content = [line.rstrip('\n') for line in kwargs['ssh_authorized_keys_file']]
        kwargs['ssh_public_keys'] = json.dumps(content)

    patch_action = kwargs.get('patch_action')
    patch_id = kwargs.get('patch_id')
    if patch_action and not patch_id:
        raise click.UsageError('--patch-id is required if --patch-action is specified')
    elif patch_id and not patch_action:
        raise click.UsageError('--patch-action is required if --patch-id is specified')
    elif patch_id and patch_action:
        kwargs['version_parameterconflict'] = {
            "action": patch_action,
            "patchId": patch_id
        }

    data_collection_options = {}
    if 'is_diagnostics_events_enabled' in kwargs and kwargs['is_diagnostics_events_enabled'] is not None:
        data_collection_options['is_diagnostics_events_enabled'] = kwargs['is_diagnostics_events_enabled']

    if 'is_health_monitoring_enabled' in kwargs and kwargs['is_health_monitoring_enabled'] is not None:
        data_collection_options['is_health_monitoring_enabled'] = kwargs['is_health_monitoring_enabled']

    if 'is_incident_logs_enabled' in kwargs and kwargs['is_incident_logs_enabled'] is not None:
        data_collection_options['is_incident_logs_enabled'] = kwargs['is_incident_logs_enabled']

    if len(data_collection_options) > 0:
        kwargs['data_collection_options'] = json.dumps(data_collection_options)

    # remove kwargs that update_db_system wont recognize
    del kwargs['ssh_authorized_keys_file']
    del kwargs['patch_action']
    del kwargs['patch_id']
    del kwargs['is_diagnostics_events_enabled']
    del kwargs['is_health_monitoring_enabled']
    del kwargs['is_incident_logs_enabled']

    ctx.invoke(database_cli.update_db_system, **kwargs)


@database_cli.db_system_group.command(name='patch', help="""Perform an action on a Patch for a DB System.""")
@cli_util.option('--db-system-id', required=True, help="""The OCID of the DB System.""")
@cli_util.option('--patch-action', required=True, type=custom_types.CliCaseInsensitiveChoice(["APPLY", "PRECHECK"]), help="""The action to perform on the patch.""")
@cli_util.option('--patch-id', required=True, help="""The OCID of the patch.""")
@click.pass_context
@cli_util.help_option
@json_skeleton_utils.get_cli_json_input_option({})
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def patch_db_system(ctx, **kwargs):
    client = cli_util.build_client('database', 'database', ctx)

    patch_details = oci.database.models.PatchDetails()
    patch_details.action = kwargs['patch_action']
    patch_details.patch_id = kwargs['patch_id']

    update_db_system_details = oci.database.models.UpdateDbSystemDetails()
    update_db_system_details.version = patch_details

    result = client.update_db_system(kwargs['db_system_id'], update_db_system_details)
    db_system = result.data

    cli_util.render(db_system, None, ctx)


# DEX-11726 Bring exacc vm cluster update and update-history-entry into vm-cluster group
# This would change "oci db vm-cluster-update get/list" commands to "oci db vm-cluster get-update/list-updates"
# and change "oci db vm-cluster-update-history-entry get/list" to "oci db vm-cluster get-update-history/list-update-histories"
cli_util.rename_command(database_cli, database_cli.vm_cluster_update_group, database_cli.get_vm_cluster_update, "get-update")
cli_util.rename_command(database_cli, database_cli.vm_cluster_update_group, database_cli.list_vm_cluster_updates, "list-updates")
cli_util.rename_command(database_cli, database_cli.vm_cluster_update_history_entry_group, database_cli.get_vm_cluster_update_history_entry, "get-update-history")
cli_util.rename_command(database_cli, database_cli.vm_cluster_update_history_entry_group, database_cli.list_vm_cluster_update_history_entries, "list-update-histories")
database_cli.vm_cluster_group.add_command(database_cli.get_vm_cluster_update)
database_cli.vm_cluster_group.add_command(database_cli.list_vm_cluster_updates)
database_cli.vm_cluster_group.add_command(database_cli.get_vm_cluster_update_history_entry)
database_cli.vm_cluster_group.add_command(database_cli.list_vm_cluster_update_history_entries)
database_cli.db_root_group.commands.pop(database_cli.vm_cluster_update_group.name)
database_cli.db_root_group.commands.pop(database_cli.vm_cluster_update_history_entry_group.name)


@cli_util.copy_params_from_generated_command(database_cli.update_vm_cluster, params_to_exclude=['version_parameterconflict', 'update_details', 'data_collection_options'])
@database_cli.vm_cluster_group.command(name='update', help=database_cli.update_vm_cluster.help)
@cli_util.option('--patch-action', help="""The action to perform on the patch.""")
@cli_util.option('--patch-id', help="""The OCID of the patch.""")
@cli_util.option('--update-action', help="""The action to perform on the update.""")
@cli_util.option('--update-id', help="""The [OCID](/Content/General/Concepts/identifiers.htm) of the maintenance update.""")
@cli_util.option('--data-collection-options', type=custom_types.CLI_COMPLEX_TYPE, help=DATA_COLLECTION_OPTIONS_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}, 'version-parameterconflict': {'module': 'database', 'class': 'PatchDetails'}, 'update-details': {'module': 'database', 'class': 'VmClusterUpdateDetails'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'data-collection-options': {'module': 'database', 'class': 'DataCollectionOptions'}}, output_type={'module': 'database', 'class': 'VmCluster'})
@cli_util.wrap_exceptions
def update_vm_cluster_extended(ctx, **kwargs):
    patch_action = kwargs.get('patch_action')
    patch_id = kwargs.get('patch_id')
    if patch_action and not patch_id:
        raise click.UsageError('--patch-id is required if --patch-action is specified')
    elif patch_id and not patch_action:
        raise click.UsageError('--patch-action is required if --patch-id is specified')
    elif patch_id and patch_action:
        kwargs['version_parameterconflict'] = {
            "action": patch_action,
            "patchId": patch_id
        }

    update_action = kwargs.get('update_action')
    update_id = kwargs.get('update_id')
    if update_action and not update_id:
        raise click.UsageError('--update-id is required if --update-action is specified')
    elif update_id and not update_action:
        raise click.UsageError('--update-action is required if --update-id is specified')
    elif update_id and update_action:
        kwargs['update_details'] = {
            "updateAction": update_action,
            "updateId": update_id
        }

    # remove kwargs that update_vm_cluster wont recognize
    del kwargs['patch_action']
    del kwargs['patch_id']
    del kwargs['update_action']
    del kwargs['update_id']

    ctx.invoke(database_cli.update_vm_cluster, **kwargs)


@database_cli.data_guard_association_group.command(name=cli_util.override('create_data_guard_association.command_name', 'create'), cls=CommandGroupWithAlias, help="""Creates a new Data Guard association.  A Data Guard association represents the replication relationship between the specified database and a peer database. For more information, see [Using Oracle Data Guard].

All Oracle Cloud Infrastructure resources, including Data Guard associations, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. Fore more information, see [Resource Identifiers].""")
@cli_util.help_option_group
def create_data_guard_association_group():
    pass


@cli_util.copy_params_from_generated_command(database_cli.create_data_guard_association, params_to_exclude=['wait_for_state', 'max_wait_seconds', 'wait_interval_seconds'])
@create_data_guard_association_group.command('from-existing-db-system', help="""Creates a new Data Guard association using an existing DB System.  A Data Guard association represents the replication relationship between the specified database and a peer database. For more information, see [Using Oracle Data Guard].

All Oracle Cloud Infrastructue resources, including Data Guard associations, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. Fore more information, see [Resource Identifiers].""")
@cli_util.option('--peer-db-system-id', required=True, help="""The OCID of the DB System to create the standby database on.""")
@cli_util.option('--peer-db-home-id', required=False, help="""The OCID of the DB Home to create the standby database on.""")
@cli_util.option('--is-active-data-guard-enabled', type=click.BOOL, help=u"""True if active Data Guard is enabled.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DataGuardAssociation'})
@cli_util.wrap_exceptions
def create_data_guard_association_from_existing_db_system(ctx, from_json, database_id, creation_type, database_admin_password, protection_mode, transport_type, database_software_image_id, is_active_data_guard_enabled, peer_db_system_id, peer_db_unique_name, peer_sid_prefix, peer_db_home_id):
    kwargs = {}

    details = {}
    details['creationType'] = creation_type
    details['databaseAdminPassword'] = database_admin_password
    details['protectionMode'] = protection_mode
    details['transportType'] = transport_type
    details['peerDbSystemId'] = peer_db_system_id

    if database_software_image_id is not None:
        details['databaseSoftwareImageId'] = database_software_image_id
    if peer_db_home_id is not None:
        details['peerDbHomeId'] = peer_db_home_id
    if peer_db_unique_name is not None:
        details['peerDbUniqueName'] = peer_db_unique_name
    if peer_sid_prefix is not None:
        details['peerSidPrefix'] = peer_sid_prefix
    if is_active_data_guard_enabled is not None:
        details['isActiveDataGuardEnabled'] = is_active_data_guard_enabled

    client = cli_util.build_client('database', 'database', ctx)
    result = client.create_data_guard_association(
        database_id=database_id,
        create_data_guard_association_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cli_util.copy_params_from_generated_command(database_cli.create_data_guard_association, params_to_exclude=['wait_for_state', 'max_wait_seconds', 'wait_interval_seconds', 'peer_db_unique_name', 'peer_sid_prefix', 'storage_volume_performance_mode'])
@create_data_guard_association_group.command('with-new-db-system', help="""Creates a new Data Guard association with a new DB System.  A Data Guard association represents the replication relationship between the specified database and a peer database. For more information, see [Using Oracle Data Guard].


All Oracle Cloud Infrastructue resources, including Data Guard associations, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. Fore more information, see [Resource Identifiers].""")
@cli_util.option('--display-name', required=True, help="""The user-friendly name for the DB System to create the standby database on. It does not have to be unique.""")
@cli_util.option('--hostname', required=True, help="""The host name for the DB Node.""")
@cli_util.option('--availability-domain', required=True, help="""The name of the Availability Domain that the standby database DB System will be located in.""")
@cli_util.option('--storage-performance', type=custom_types.CliCaseInsensitiveChoice(["BALANCED", "HIGH_PERFORMANCE"]), help=u"""The block storage volume performance level. Valid values are `BALANCED` and `HIGH_PERFORMANCE`. See [Block Volume Performance] for more information.""")
@cli_util.option('--cpu-core-count', type=click.INT, help=u"""The number of OCPU cores available for AMD-based virtual machine DB systems.""")
@cli_util.option('--shape', help=u"""The shape of the DB system to launch to set up the Data Guard association. The shape determines the number of CPU cores and the amount of memory available for the DB system. Only virtual machine shapes are valid shapes. If you do not supply this parameter, the default shape is the shape of the primary DB system. To get a list of all shapes, use the [ListDbSystemShapes] operation.""")
@cli_util.option('--subnet-id', required=True, help="""The OCID of the subnet the DB System is associated with. **Subnet Restrictions:** - For 1- and 2-node RAC DB Systems, do not use a subnet that overlaps with 192.168.16.16/28

These subnets are used by the Oracle Clusterware private interconnect on the database instance. Specifying an overlapping subnet will cause the private interconnect to malfunction. This restriction applies to both the client subnet and backup subnet.""")
@cli_util.option('--is-active-data-guard-enabled', type=click.BOOL, help=u"""True if active Data Guard is enabled.""")
@cli_util.option('--node-count', type=click.INT, help=u"""The number of nodes to launch for the DB system of the standby in the Data Guard association. For a 2-node RAC virtual machine DB system, specify either 1 or 2. If you do not supply this parameter, the default is the node count of the primary DB system.""")
@cli_util.option('--time-zone', help=u"""The time zone of the dataguard standby DB system. For details, see [DB System Time Zones].""")
@cli_util.option('--fault-domains', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A Fault Domain is a grouping of hardware and infrastructure within an availability domain. Fault Domains let you distribute your instances so that they are not on the same physical hardware within a single availability domain. A hardware failure or maintenance that affects one Fault Domain does not affect DB systems in other Fault Domains.\n\nIf you do not specify the Fault Domain, the system selects one for you. To change the Fault Domain for a DB system, terminate it and launch a new DB system in the preferred Fault Domain.\n\nIf the node count is greater than 1, you can specify which Fault Domains these nodes will be distributed into. The system assigns your nodes automatically to the Fault Domains you specify so that no Fault Domain contains more than one node.\n\nTo get a list of Fault Domains, use the [ListFaultDomains] operation in the Identity and Access Management Service API.\n\nExample: `FAULT-DOMAIN-1`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--private-ip', help=u"""The IPv4 address from the provided OCI subnet which needs to be assigned to the VNIC. If not provided, it will be auto-assigned with an available IPv4 address from the subnet.""")
@cli_util.option('--license-model', type=custom_types.CliCaseInsensitiveChoice(["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]), help=u"""The Oracle license model that applies to all the databases on the dataguard standby DB system. The default is LICENSE_INCLUDED.""")
@cli_util.option('--db-system-freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].\n\nExample: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--db-system-defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--database-freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].\n\nExample: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--database-defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-diagnostics-events-enabled', required=False, type=click.BOOL, help="""Enables customer to receive Events service notifications for guest VM issues""")
@cli_util.option('--is-health-monitoring-enabled', required=False, type=click.BOOL, help="""Enables Oracle to receive diagnostic data and share it with its operations and support personnel""")
@cli_util.option('--is-incident-logs-enabled', required=False, type=click.BOOL, help="""Enables Oracle to receive Events service notifications for guest VM issues, collect incident logs and traces""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fault-domains': {'module': 'database', 'class': 'list[string]'}, 'db-system-freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'db-system-defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'database-freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'database-defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'DataGuardAssociation'})
@cli_util.wrap_exceptions
def create_data_guard_association_with_new_db_system(ctx, from_json, database_id, creation_type, database_admin_password, protection_mode, transport_type, availability_domain, display_name, hostname, shape, subnet_id, database_software_image_id, is_active_data_guard_enabled, storage_performance, cpu_core_count, node_count, time_zone, fault_domains, private_ip, license_model, db_system_freeform_tags, db_system_defined_tags, database_freeform_tags, database_defined_tags, is_diagnostics_events_enabled, is_health_monitoring_enabled, is_incident_logs_enabled, **kwargs):
    kwargs = {}

    details = {}
    details['creationType'] = creation_type
    details['databaseAdminPassword'] = database_admin_password
    details['protectionMode'] = protection_mode
    details['transportType'] = transport_type

    if database_software_image_id is not None:
        details['databaseSoftwareImageId'] = database_software_image_id
    if availability_domain is not None:
        details['availabilityDomain'] = availability_domain
    if display_name is not None:
        details['displayName'] = display_name
    if hostname is not None:
        details['hostname'] = hostname
    if subnet_id is not None:
        details['subnetId'] = subnet_id
    if shape is not None:
        details['shape'] = shape
    if is_active_data_guard_enabled is not None:
        details['isActiveDataGuardEnabled'] = is_active_data_guard_enabled
    if cpu_core_count is not None:
        details['cpuCoreCount'] = cpu_core_count
    if storage_performance is not None:
        details['storageVolumePerformanceMode'] = storage_performance
    if node_count is not None:
        details['nodeCount'] = node_count
    if time_zone is not None:
        details['timeZone'] = time_zone
    if fault_domains is not None:
        details['faultDomains'] = cli_util.parse_json_parameter("fault_domains", fault_domains)
    if private_ip is not None:
        details['privateIp'] = private_ip
    if license_model is not None:
        details['licenseModel'] = license_model
    if db_system_freeform_tags is not None:
        details['dbSystemFreeformTags'] = cli_util.parse_json_parameter("db_system_freeform_tags", db_system_freeform_tags)
    if db_system_defined_tags is not None:
        details['dbSystemDefinedTags'] = cli_util.parse_json_parameter("db_system_defined_tags", db_system_defined_tags)
    if database_freeform_tags is not None:
        details['databaseFreeformTags'] = cli_util.parse_json_parameter("database_freeform_tags", database_freeform_tags)
    if database_defined_tags is not None:
        details['databaseDefinedTags'] = cli_util.parse_json_parameter("database_defined_tags", database_defined_tags)

    data_collection_options = {}
    if is_diagnostics_events_enabled is not None:
        data_collection_options['isDiagnosticsEventsEnabled'] = is_diagnostics_events_enabled
    if is_health_monitoring_enabled is not None:
        data_collection_options['isHealthMonitoringEnabled'] = is_health_monitoring_enabled
    if is_incident_logs_enabled is not None:
        data_collection_options['isIncidentLogsEnabled'] = is_incident_logs_enabled
    if len(data_collection_options) > 0:
        details['dataCollectionOptions'] = cli_util.parse_json_parameter("data_collection_options", data_collection_options)

    details['creationType'] = 'NewDbSystem'

    client = cli_util.build_client('database', 'database', ctx)
    result = client.create_data_guard_association(
        database_id=database_id,
        create_data_guard_association_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cli_util.copy_params_from_generated_command(database_cli.create_data_guard_association, params_to_exclude=['wait_for_state', 'max_wait_seconds', 'wait_interval_seconds', 'creation_type'])
@create_data_guard_association_group.command('from-existing-vm-cluster', help=u"""Creates a new Data Guard association.  A Data Guard association represents the replication relationship between the specified database and a peer database. For more information, see [Using Oracle Data Guard].

All Oracle Cloud Infrastructure resources, including Data Guard associations, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. For more information, see [Resource Identifiers].""")
@cli_util.option('--peer-vm-cluster-id', required=True, help=u"""The [OCID] of the VM Cluster in which to create the standby database. You must supply this value if creationType is `ExistingVmCluster`.""")
@cli_util.option('--peer-db-home-id', required=False, help="""The OCID of the DB Home to create the standby database on.""")
@cli_util.option('--is-active-data-guard-enabled', type=click.BOOL, help=u"""True if active Data Guard is enabled.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DataGuardAssociation'})
@cli_util.wrap_exceptions
def create_data_guard_association_from_existing_vm_cluster(ctx, from_json, database_id, database_admin_password, protection_mode, transport_type, database_software_image_id, is_active_data_guard_enabled, peer_vm_cluster_id, peer_db_unique_name, peer_sid_prefix, peer_db_home_id):

    kwargs = {}

    details = {}
    details['databaseAdminPassword'] = database_admin_password
    details['protectionMode'] = protection_mode
    details['transportType'] = transport_type
    details['peerVmClusterId'] = peer_vm_cluster_id
    details['creationType'] = 'ExistingVmCluster'

    if database_software_image_id is not None:
        details['databaseSoftwareImageId'] = database_software_image_id
    if peer_db_home_id is not None:
        details['peerDbHomeId'] = peer_db_home_id
    if peer_db_unique_name is not None:
        details['peerDbUniqueName'] = peer_db_unique_name
    if peer_sid_prefix is not None:
        details['peerSidPrefix'] = peer_sid_prefix
    if is_active_data_guard_enabled is not None:
        details['isActiveDataGuardEnabled'] = is_active_data_guard_enabled

    client = cli_util.build_client('database', 'database', ctx)
    result = client.create_data_guard_association(
        database_id=database_id,
        create_data_guard_association_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_cli.patch_group.command('get', cls=CommandGroupWithAlias, help=database_cli.get_db_home_patch.help)
@cli_util.help_option_group
def patch_get_group():
    pass


@database_cli.patch_group.command('list', cls=CommandGroupWithAlias, help=database_cli.list_db_home_patches.help)
@cli_util.help_option_group
def patch_list_group():
    pass


@database_cli.patch_history_entry_group.command('get', cls=CommandGroupWithAlias, help=database_cli.get_db_home_patch_history_entry.help)
@cli_util.help_option_group
def patch_history_get_group():
    pass


@database_cli.patch_history_entry_group.command('list', cls=CommandGroupWithAlias, help=database_cli.list_db_home_patch_history_entries.help)
@cli_util.help_option_group
def patch_history_list_group():
    pass


@cli_util.copy_params_from_generated_command(database_cli.get_db_home_patch, params_to_exclude=['db_home_id'])
@patch_get_group.command('by-database', help="""Get patch for a given database""")
@cli_util.option('--database-id', required=True, help="""The database [OCID].""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'Patch'})
@cli_util.wrap_exceptions
def get_patch_by_database(ctx, **kwargs):
    client = cli_util.build_client('database', 'database', ctx)

    # get the db-home for this database
    response = client.get_database(kwargs['database_id'])
    kwargs['db_home_id'] = response.data.db_home_id

    del kwargs['database_id']

    ctx.invoke(database_cli.get_db_home_patch, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.list_db_home_patches, params_to_exclude=['db_home_id'])
@patch_list_group.command('by-database', help="""List patches for a given database""")
@cli_util.option('--database-id', required=True, help="""The database [OCID].""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[PatchSummary]'})
@cli_util.wrap_exceptions
def list_patch_by_database(ctx, **kwargs):
    client = cli_util.build_client('database', 'database', ctx)

    # get the db-home for this database
    response = client.get_database(kwargs['database_id'])
    kwargs['db_home_id'] = response.data.db_home_id

    del kwargs['database_id']

    ctx.invoke(database_cli.list_db_home_patches, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.get_db_home_patch_history_entry, params_to_exclude=['db_home_id'])
@patch_history_get_group.command('by-database', help="""Get patch history for a given database""")
@cli_util.option('--database-id', required=True, help="""The database [OCID].""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'PatchHistoryEntry'})
@cli_util.wrap_exceptions
def get_patch_history_entry_by_database(ctx, **kwargs):
    client = cli_util.build_client('database', 'database', ctx)

    # get the db-home for this database
    response = client.get_database(kwargs['database_id'])
    kwargs['db_home_id'] = response.data.db_home_id

    del kwargs['database_id']

    ctx.invoke(database_cli.get_db_home_patch_history_entry, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.list_db_home_patch_history_entries, params_to_exclude=['db_home_id'])
@patch_history_list_group.command('by-database', help="""List patch history entries for a given database""")
@cli_util.option('--database-id', required=True, help="""The database [OCID].""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[PatchHistoryEntrySummary]'})
@cli_util.wrap_exceptions
def list_patch_history_entries_by_database(ctx, **kwargs):
    client = cli_util.build_client('database', 'database', ctx)

    # get the db-home for this database
    response = client.get_database(kwargs['database_id'])
    kwargs['db_home_id'] = response.data.db_home_id

    del kwargs['database_id']

    ctx.invoke(database_cli.list_db_home_patch_history_entries, **kwargs)


# Rename Exacs New resource model names
cli_util.rename_command(database_cli, database_cli.db_root_group, database_cli.cloud_exadata_infrastructure_group, "cloud-exa-infra")
cli_util.rename_command(database_cli, database_cli.cloud_exadata_infrastructure_group, database_cli.add_storage_capacity_cloud_exadata_infrastructure, "add-storage")
cli_util.rename_command(database_cli, database_cli.cloud_vm_cluster_group, database_cli.get_cloud_vm_cluster_iorm_config, "get-exadata-iorm-config")
cli_util.rename_command(database_cli, database_cli.cloud_vm_cluster_group, database_cli.update_cloud_vm_cluster_iorm_config, "update-exadata-iorm-config")
cli_util.rename_command(database_cli, database_cli.db_system_group, database_cli.migrate_exadata_db_system_resource_model, "switch")

# move update, update-history to cloud vm cluster group
cli_util.rename_command(database_cli, database_cli.update_group, database_cli.get_cloud_vm_cluster_update, "get-update")
cli_util.rename_command(database_cli, database_cli.update_group, database_cli.list_cloud_vm_cluster_updates, "list-updates")
cli_util.rename_command(database_cli, database_cli.update_history_entry_group, database_cli.get_cloud_vm_cluster_update_history_entry, "get-update-history")
cli_util.rename_command(database_cli, database_cli.update_history_entry_group, database_cli.list_cloud_vm_cluster_update_history_entries, "list-update-histories")
database_cli.cloud_vm_cluster_group.add_command(database_cli.get_cloud_vm_cluster_update)
database_cli.cloud_vm_cluster_group.add_command(database_cli.list_cloud_vm_cluster_updates)
database_cli.cloud_vm_cluster_group.add_command(database_cli.get_cloud_vm_cluster_update_history_entry)
database_cli.cloud_vm_cluster_group.add_command(database_cli.list_cloud_vm_cluster_update_history_entries)
database_cli.db_root_group.commands.pop(database_cli.update_group.name)
database_cli.db_root_group.commands.pop(database_cli.update_history_entry_group.name)


@cli_util.copy_params_from_generated_command(database_cli.add_storage_capacity_cloud_exadata_infrastructure, params_to_exclude=['cloud_exadata_infrastructure_id'])
@database_cli.cloud_exadata_infrastructure_group.command('add-storage', help=database_cli.add_storage_capacity_cloud_exadata_infrastructure.help)
@cli_util.option('--cloud-exa-infra-id', required=True, help=u"""The [OCID] of the cloud Exadata infrastructure.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def add_storage_capacity_cloud_exadata_infrastructure(ctx, **kwargs):
    kwargs['cloud_exadata_infrastructure_id'] = kwargs['cloud_exa_infra_id']
    kwargs.pop('cloud_exa_infra_id')

    ctx.invoke(database_cli.add_storage_capacity_cloud_exadata_infrastructure, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.create_cloud_vm_cluster, params_to_exclude=['cloud_exadata_infrastructure_id', 'is_sparse_diskgroup_enabled', 'is_local_backup_enabled', 'ssh_public_keys', 'data_collection_options'])
@database_cli.cloud_vm_cluster_group.command('create', help=database_cli.create_cloud_vm_cluster.help)
@cli_util.option('--cloud-exa-infra-id', required=True, help=u"""The [OCID] of the cloud Exadata infrastructure.""")
@cli_util.option('--is-sparse-diskgroup', type=click.BOOL, help=u"""If true, the sparse disk group is configured for the cloud VM cluster. If false, the sparse disk group is not created.""")
@cli_util.option('--is-local-backup', type=click.BOOL, help=u"""If true, database backup on local Exadata storage is configured for the cloud VM cluster. If false, database backup on local Exadata storage is not available in the cloud VM cluster.""")
@cli_util.option('--ssh-authorized-keys-file', required=True, type=click.File('r'), help="""A file containing one or more public SSH keys to use for SSH access to the Cloud VM Cluster. Use a newline character to separate multiple keys. The length of the combined keys cannot exceed 10,000 characters.""")
@cli_util.option('--data-collection-options', type=custom_types.CLI_COMPLEX_TYPE, help=DATA_COLLECTION_OPTIONS_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}, 'nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'backup-network-nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'data-collection-options': {'module': 'database', 'class': 'DataCollectionOptions'}}, output_type={'module': 'database', 'class': 'CloudVmCluster'})
@cli_util.wrap_exceptions
def create_cloud_vm_cluster(ctx, **kwargs):
    kwargs['cloud_exadata_infrastructure_id'] = kwargs['cloud_exa_infra_id']
    kwargs['is_sparse_diskgroup_enabled'] = kwargs['is_sparse_diskgroup']
    kwargs['is_local_backup_enabled'] = kwargs['is_local_backup']

    if 'ssh_authorized_keys_file' in kwargs and kwargs['ssh_authorized_keys_file']:
        content = [line.rstrip('\n') for line in kwargs['ssh_authorized_keys_file']]
        kwargs['ssh_public_keys'] = json.dumps(content)

    kwargs.pop('cloud_exa_infra_id')
    kwargs.pop('is_sparse_diskgroup')
    kwargs.pop('is_local_backup')
    kwargs.pop('ssh_authorized_keys_file')

    ctx.invoke(database_cli.create_cloud_vm_cluster, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.change_cloud_exadata_infrastructure_compartment, params_to_exclude=['cloud_exadata_infrastructure_id'])
@database_cli.cloud_exadata_infrastructure_group.command('change-compartment', help=database_cli.change_cloud_exadata_infrastructure_compartment.help)
@cli_util.option('--cloud-exa-infra-id', required=True, help=u"""The [OCID] of the cloud Exadata infrastructure.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_cloud_exadata_infrastructure_compartment(ctx, **kwargs):
    kwargs['cloud_exadata_infrastructure_id'] = kwargs['cloud_exa_infra_id']
    kwargs.pop('cloud_exa_infra_id')

    ctx.invoke(database_cli.change_cloud_exadata_infrastructure_compartment, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.list_backups, params_to_exclude=[])
@database_cli.backup_group.command('list', help=database_cli.list_backups.help)
@click.pass_context
@cli_util.wrap_exceptions
def list_backups_extended(ctx, **kwargs):
    compartment_id = kwargs.get('compartment_id')
    database_id = kwargs.get('database_id')
    if not compartment_id and not database_id:
        raise click.UsageError('--compartment-id or --database-id must be provided')
    if compartment_id and database_id:
        raise click.UsageError(
            'You can only specify one of either --compartment-id or --database-id option'
        )
    ctx.invoke(database_cli.list_backups, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.list_cloud_vm_clusters, params_to_exclude=['cloud_exadata_infrastructure_id'])
@database_cli.cloud_vm_cluster_group.command('list', help=database_cli.list_cloud_vm_clusters.help)
@cli_util.option('--cloud-exa-infra-id', help=u"""If provided, filters the results for the given Cloud Exadata Infrastructure.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[CloudVmClusterSummary]'})
@cli_util.wrap_exceptions
def list_cloud_vm_clusters(ctx, **kwargs):
    kwargs['cloud_exadata_infrastructure_id'] = kwargs['cloud_exa_infra_id']
    kwargs.pop('cloud_exa_infra_id')

    ctx.invoke(database_cli.list_cloud_vm_clusters, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.update_cloud_vm_cluster, params_to_exclude=['ssh_public_keys', 'update_details', 'data_collection_options'])
@database_cli.cloud_vm_cluster_group.command(name='update', help=database_cli.update_cloud_vm_cluster.help)
@cli_util.option('--update-action', help="""The action to perform on the update.""")
@cli_util.option('--update-id', help="""The [OCID](/Content/General/Concepts/identifiers.htm) of the maintenance update.""")
@cli_util.option('--ssh-authorized-keys-file', type=click.File('r'), help="""A file containing one or more public SSH keys to use for SSH access to the cloud VM cluster. Use a newline character to separate multiple keys. The length of the combined keys cannot exceed 10,000 characters.""")
@cli_util.option('--data-collection-options', type=custom_types.CLI_COMPLEX_TYPE, help=DATA_COLLECTION_OPTIONS_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}, 'update-details': {'module': 'database', 'class': 'UpdateDetails'}, 'nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'backup-network-nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'compute-nodes': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'data-collection-options': {'module': 'database', 'class': 'DataCollectionOptions'}}, output_type={'module': 'database', 'class': 'CloudVmCluster'})
@cli_util.wrap_exceptions
def update_cloud_vm_cluster(ctx, **kwargs):
    if 'ssh_authorized_keys_file' in kwargs and kwargs['ssh_authorized_keys_file']:
        content = [line.rstrip('\n') for line in kwargs['ssh_authorized_keys_file']]
        kwargs['ssh_public_keys'] = json.dumps(content)

    update_action = kwargs.get('update_action')
    update_id = kwargs.get('update_id')
    if update_action and not update_id:
        raise click.UsageError('--update-id is required if --update-action is specified')
    elif update_id and not update_action:
        raise click.UsageError('--update-action is required if --update-id is specified')
    elif update_id and update_action:
        kwargs['update_details'] = {
            "updateAction": update_action,
            "updateId": update_id
        }

    # remove kwargs that update cloud vm cluster wont recognize
    del kwargs['ssh_authorized_keys_file']
    del kwargs['update_action']
    del kwargs['update_id']

    ctx.invoke(database_cli.update_cloud_vm_cluster, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.delete_cloud_exadata_infrastructure, params_to_exclude=['cloud_exadata_infrastructure_id'])
@database_cli.cloud_exadata_infrastructure_group.command('delete', help=database_cli.delete_cloud_exadata_infrastructure.help)
@cli_util.option('--cloud-exa-infra-id', required=True, help=u"""The [OCID] of the cloud Exadata infrastructure.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_cloud_exadata_infrastructure(ctx, **kwargs):
    kwargs['cloud_exadata_infrastructure_id'] = kwargs['cloud_exa_infra_id']
    kwargs.pop('cloud_exa_infra_id')

    ctx.invoke(database_cli.delete_cloud_exadata_infrastructure, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.get_cloud_exadata_infrastructure, params_to_exclude=['cloud_exadata_infrastructure_id'])
@database_cli.cloud_exadata_infrastructure_group.command('get', help=database_cli.get_cloud_exadata_infrastructure.help)
@cli_util.option('--cloud-exa-infra-id', required=True, help=u"""The [OCID] of the cloud Exadata infrastructure.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'CloudExadataInfrastructure'})
@cli_util.wrap_exceptions
def get_cloud_exadata_infrastructure(ctx, **kwargs):
    kwargs['cloud_exadata_infrastructure_id'] = kwargs['cloud_exa_infra_id']
    kwargs.pop('cloud_exa_infra_id')

    ctx.invoke(database_cli.get_cloud_exadata_infrastructure, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.update_cloud_exadata_infrastructure, params_to_exclude=['cloud_exadata_infrastructure_id'])
@database_cli.cloud_exadata_infrastructure_group.command('update', help=database_cli.update_cloud_exadata_infrastructure.help)
@cli_util.option('--cloud-exa-infra-id', required=True, help=u"""The [OCID] of the cloud Exadata infrastructure.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'maintenance-window': {'module': 'database', 'class': 'MaintenanceWindow'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'customer-contacts': {'module': 'database', 'class': 'list[CustomerContact]'}}, output_type={'module': 'database', 'class': 'CloudExadataInfrastructure'})
@cli_util.wrap_exceptions
def update_cloud_exadata_infrastructure(ctx, **kwargs):
    kwargs['cloud_exadata_infrastructure_id'] = kwargs['cloud_exa_infra_id']
    kwargs.pop('cloud_exa_infra_id')

    ctx.invoke(database_cli.update_cloud_exadata_infrastructure, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.create_db_home, params_to_exclude=['database', 'db_version'])
@database_cli.db_home_group.command(name='create', help="""Creates a new database in the given DB System or VM Cluster.""")
@cli_util.option('--vm-cluster-id', required=False, help="""The Vm Cluster Id to create this Db Home under. Either --db-system-id or --vm-cluster-id must be specified, but if both are passed, --vm-cluster-id will be ignored.""")
@cli_util.option('--db-system-id', required=False, help="""The Db System Id to restore this Db Home under. Either --db-system-id or --vm-cluster-id must be specified, but if both are passed, --vm-cluster-id will be ignored.""")
@cli_util.option('--db-version', required=False, help="""A valid Oracle database version. To get a list of supported versions, use the command 'oci db version list'.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backup-destination': {'module': 'database', 'class': 'list[BackupDestinationDetails]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'DatabaseSummary'})
@cli_util.wrap_exceptions
def create_db_home(ctx, wait_for_state, max_wait_seconds, wait_interval_seconds, **kwargs):
    client = cli_util.build_client('database', 'database', ctx)

    if 'db_system_id' in kwargs and kwargs['db_system_id']:
        db_home_details = oci.database.models.CreateDbHomeWithDbSystemIdDetails()
        db_home_details.db_system_id = kwargs['db_system_id']
        get_db_system_response = client.get_db_system(kwargs['db_system_id'])

    else:
        if 'vm_cluster_id' in kwargs and kwargs['vm_cluster_id']:
            vm_cluster_id = kwargs['vm_cluster_id']
            db_home_details = oci.database.models.CreateDbHomeWithVmClusterIdDetails()
            db_home_details.vm_cluster_id = vm_cluster_id
            if CLOUD_VM_CLUSTER_PREFIX in vm_cluster_id or DB_SYSTEM_PREFIX in vm_cluster_id:
                # Call get_cloud_vm_cluster for (migrated) cloud vm cluster
                get_db_system_response = client.get_cloud_vm_cluster(vm_cluster_id)
            else:
                # Call get_vm_cluster for exacc vm cluster
                get_db_system_response = client.get_vm_cluster(vm_cluster_id)

        else:
            click.echo(message="Missing a required parameter. Either --db-system-id or --vm-cluster-id must be specified.", file=sys.stderr)
            sys.exit(1)

    if kwargs['db_version'] is not None:
        db_home_details.db_version = kwargs['db_version']
    if kwargs['database_software_image_id'] is not None:
        db_home_details.database_software_image_id = kwargs['database_software_image_id']
    if kwargs['display_name'] is not None:
        db_home_details.display_name = kwargs['display_name']
    if kwargs['is_desupported_version'] is not None:
        db_home_details.is_desupported_version = kwargs['is_desupported_version']

    db_system_shape = get_db_system_response.data.shape
    # For Exadata systems create db home is called
    if EXADATA_SHAPE_PREFIX in db_system_shape:
        result = client.create_db_home(db_home_details)

        if wait_for_state:

            if hasattr(client, 'get_db_home') and callable(getattr(client, 'get_db_home')):
                try:
                    wait_period_kwargs = {}
                    if max_wait_seconds is not None:
                        wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                    if wait_interval_seconds is not None:
                        wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                    click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                    result = oci.wait_until(client, client.get_db_home(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
                except oci.exceptions.MaximumWaitTimeExceeded as e:
                    # If we fail, we should show an error, but we should still provide the information to the customer
                    click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                    cli_util.render_response(result, ctx)
                    sys.exit(2)
                except Exception:
                    click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                    cli_util.render_response(result, ctx)
                    raise
            else:
                click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)

        cli_util.render_response(result, ctx)
    else:
        click.echo(message="Cannot create a DB Home for Db systems with non Exadata shapes.", file=sys.stderr)
        sys.exit(1)


# db-home group is exposed to the customers now
# database_cli.db_root_group.commands.pop(database_cli.db_home_group.name)

# db-home update is excluded from the db-home command group
database_cli.db_home_group.commands.pop(database_cli.create_db_home.name)
database_cli.db_home_group.commands.pop(database_cli.create_db_home_create_db_home_with_db_system_id_from_backup_details.name)
database_cli.db_home_group.commands.pop(database_cli.create_db_home_create_db_home_with_vm_cluster_id_from_backup_details.name)
database_cli.db_home_group.commands.pop(database_cli.create_db_home_create_db_home_with_db_system_id_details.name)
database_cli.db_home_group.commands.pop(database_cli.create_db_home_create_db_home_with_vm_cluster_id_details.name)
database_cli.db_home_group.commands.pop(database_cli.create_db_home_create_db_home_with_db_system_id_from_database_details.name)

# This is simulated via oci cli create database --db-home-id
database_cli.database_group.commands.pop(database_cli.create_database_create_new_database_details.name)


database_cli.database_group.commands.pop(database_cli.list_databases.name)
database_cli.db_node_group.commands.pop(database_cli.db_node_action.name)
database_cli.db_system_group.commands.pop(database_cli.launch_db_system.name)

# Disable subclass commands
database_cli.db_system_group.commands.pop(database_cli.launch_db_system_launch_db_system_details.name)
database_cli.db_system_group.commands.pop(database_cli.launch_db_system_launch_db_system_from_backup_details.name)
database_cli.db_system_group.commands.pop(database_cli.launch_db_system_launch_db_system_from_database_details.name)

database_cli.db_system_group.commands.pop(database_cli.update_db_system.name)

# Disable subclass command
database_cli.data_guard_association_group.commands.pop(database_cli.create_data_guard_association_create_data_guard_association_to_existing_db_system_details.name)
database_cli.data_guard_association_group.commands.pop(database_cli.create_data_guard_association_create_data_guard_association_with_new_db_system_details.name)
database_cli.data_guard_association_group.commands.pop(database_cli.create_data_guard_association_create_data_guard_association_to_existing_vm_cluster_details.name)

# we need to expose customized create / delete / list database commands in order to avoid exposing DbHomes
database_cli.database_group.add_command(create_database)
database_cli.database_group.add_command(create_database_from_backup)
database_cli.database_group.add_command(create_database_from_another_database)
database_cli.database_group.add_command(delete_database)
database_cli.database_group.add_command(list_databases)
database_cli.db_system_group.add_command(launch_db_system_extended)
database_cli.db_system_group.add_command(launch_db_system_backup_extended)
database_cli.db_system_group.add_command(update_db_system_extended)

database_cli.db_home_group.add_command(create_db_home)

patch_get_group.add_command(database_cli.get_db_system_patch)
patch_list_group.add_command(database_cli.list_db_system_patches)

patch_history_get_group.add_command(database_cli.get_db_system_patch_history_entry)
patch_history_list_group.add_command(database_cli.list_db_system_patch_history_entries)

cli_util.override_command_short_help_and_help(database_cli.backup_group, """A database backup. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
cli_util.override_command_short_help_and_help(database_cli.data_guard_association_group, """The properties that define a Data Guard association.
To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].
For information about endpoints and signing API requests, see [About the API]. For information about available SDKs and tools, see [SDKS and Other Tools].""")
cli_util.override_command_short_help_and_help(database_cli.database_group, """An Oracle database on a bare metal or virtual machine DB system. For more information, see Bare Metal and Virtual Machine DB Systems.
To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].
**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
cli_util.override_command_short_help_and_help(database_cli.db_node_group, """A server where Oracle Database software is running.
To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].
**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
cli_util.override_command_short_help_and_help(database_cli.patch_group, """A Patch for a DB system or DB Home.
To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
cli_util.override_command_short_help_and_help(database_cli.patch_history_entry_group, """The record of a patch action on a specified target.""")
cli_util.override_command_short_help_and_help(database_cli.db_system_group, """The Database Service supports several types of DB systems, ranging in size, price, and performance. For details about each type of system, see:
- Exadata DB Systems - Bare Metal and Virtual Machine DB Systems
To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see [Getting Started with Policies].
For information about access control and compartments, see Overview of the Identity Service.
For information about availability domains, see [Regions and Availability Domains].
To get a list of availability domains, use the `ListAvailabilityDomains` operation in the Identity Service API.
**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")


# DEX-9777 Key store command changes
# Key store - hide basic create. Shorten the create okv command. (create-key-store-key-store-type-from-oracle-key-vault-details -> create-oracle-key-vault-details)
database_cli.key_store_group.commands.pop(database_cli.create_key_store.name)
cli_util.rename_command(database_cli, database_cli.key_store_group, database_cli.create_key_store_key_store_type_from_oracle_key_vault_details, "create-oracle-key-vault-details")

# Key store - hide basic update. Shorten the update okv command. (update-key-store-key-store-type-from-oracle-key-vault-details -> update-oracle-key-vault-details)
database_cli.key_store_group.commands.pop(database_cli.update_key_store.name)
cli_util.rename_command(database_cli, database_cli.key_store_group, database_cli.update_key_store_key_store_type_from_oracle_key_vault_details, "update-oracle-key-vault-details")

# Add key store list command to key_store_group (oci db key-store-summary list-key-stores -> oci db key-store list)
database_cli.db_root_group.commands.pop(database_cli.key_store_summary_group.name)
cli_util.rename_command(database_cli, database_cli.key_store_summary_group, database_cli.list_key_stores, "list")
database_cli.key_store_group.add_command(database_cli.list_key_stores)


# Rename create Key store params that start with type-details to shorten the names
@cli_util.copy_params_from_generated_command(database_cli.create_key_store_key_store_type_from_oracle_key_vault_details, params_to_exclude=['type_details_connection_ips', 'type_details_admin_username', 'type_details_vault_id', 'type_details_secret_id'])
@cli_util.option('--connection-ips', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of Oracle Key Vault connection IP addresses.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--admin-username', required=True, help=u"""The administrator username to connect to Oracle Key Vault""")
@cli_util.option('--vault-id', required=True, help=u"""The [OCID] of the Oracle Cloud Infrastructure [vault].""")
@cli_util.option('--secret-id', required=True, help=u"""The [OCID] of the Oracle Cloud Infrastructure [secret].""")
@database_cli.key_store_group.command(name='create-oracle-key-vault-details', help=database_cli.create_key_store_key_store_type_from_oracle_key_vault_details.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'connection-ips': {'module': 'database', 'class': 'list[string]'}}, output_type={'module': 'database', 'class': 'KeyStore'})
@cli_util.wrap_exceptions
def create_okv_keystore(ctx, **kwargs):
    if 'connection_ips' in kwargs and kwargs['connection_ips']:
        kwargs['type_details_connection_ips'] = cli_util.parse_json_parameter("connection_ips", kwargs['connection_ips'])

    del kwargs['connection_ips']

    if 'admin_username' in kwargs and kwargs['admin_username']:
        kwargs['type_details_admin_username'] = kwargs['admin_username']

    del kwargs['admin_username']

    if 'vault_id' in kwargs and kwargs['vault_id']:
        kwargs['type_details_vault_id'] = kwargs['vault_id']

    del kwargs['vault_id']

    if 'secret_id' in kwargs and kwargs['secret_id']:
        kwargs['type_details_secret_id'] = kwargs['secret_id']

    del kwargs['secret_id']

    ctx.invoke(database_cli.create_key_store_key_store_type_from_oracle_key_vault_details, **kwargs)


# DEX-9777 Rename update Key store params starting with type-details to shorten the names
@cli_util.copy_params_from_generated_command(database_cli.update_key_store_key_store_type_from_oracle_key_vault_details, params_to_exclude=['type_details_connection_ips', 'type_details_admin_username', 'type_details_vault_id', 'type_details_secret_id'])
@cli_util.option('--connection-ips', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of Oracle Key Vault connection IP addresses.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--admin-username', required=True, help=u"""The administrator username to connect to Oracle Key Vault""")
@cli_util.option('--vault-id', required=True, help=u"""The [OCID] of the Oracle Cloud Infrastructure [vault].""")
@cli_util.option('--secret-id', required=True, help=u"""The [OCID] of the Oracle Cloud Infrastructure [secret].""")
@database_cli.key_store_group.command(name='update-oracle-key-vault-details', help=database_cli.update_key_store_key_store_type_from_oracle_key_vault_details.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'connection-ips': {'module': 'database', 'class': 'list[string]'}}, output_type={'module': 'database', 'class': 'KeyStore'})
@cli_util.wrap_exceptions
def update_okv_keystore(ctx, **kwargs):
    if 'connection_ips' in kwargs and kwargs['connection_ips']:
        kwargs['type_details_connection_ips'] = cli_util.parse_json_parameter("connection_ips", kwargs['connection_ips'])

    del kwargs['connection_ips']

    if 'admin_username' in kwargs and kwargs['admin_username']:
        kwargs['type_details_admin_username'] = kwargs['admin_username']

    del kwargs['admin_username']

    if 'vault_id' in kwargs and kwargs['vault_id']:
        kwargs['type_details_vault_id'] = kwargs['vault_id']

    del kwargs['vault_id']

    if 'secret_id' in kwargs and kwargs['secret_id']:
        kwargs['type_details_secret_id'] = kwargs['secret_id']

    del kwargs['secret_id']

    ctx.invoke(database_cli.update_key_store_key_store_type_from_oracle_key_vault_details, **kwargs)


# DEX-9562 Rename parameter name for create_autonomous_database
@cli_util.copy_params_from_generated_command(database_cli.create_autonomous_database_create_autonomous_database_details, params_to_exclude=['is_access_control_enabled', 'autonomous_maintenance_schedule_type'])
@cli_util.option('--maintenance-schedule-type', type=custom_types.CliCaseInsensitiveChoice(["EARLY", "REGULAR"]), help="""The maintenance schedule type of the Autonomous Database on shared Exadata infrastructure. The EARLY maintenance schedule of this Autonomous Database follows a schedule that applies patches prior to the REGULAR schedule.The REGULAR maintenance schedule of this Autonomous Database follows the normal cycle.""")
@cli_util.option('--is-acl-enabled', required=False, type=click.BOOL, help="""Indicates if the database-level access control is enabled. If disabled, database access is defined by the network security rules. If enabled, database access is restricted to the IP addresses defined by the rules specified with the `whitelistedIps` property. While specifying `whitelistedIps` rules is optional,  if database-level access control is enabled and no rules are specified, the database will become inaccessible. The rules can be added later using the `UpdateAutonomousDatabase` API operation or edit option in console. When creating a database clone, the desired access control setting should be specified. By default, database-level access control will be disabled for the clone.

This property is applicable only to Autonomous Databases on the Exadata Cloud@Customer platform.""")
@database_cli.autonomous_database_group.command(name='create', help=database_cli.create_autonomous_database_create_autonomous_database_details.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'whitelisted-ips': {'module': 'database', 'class': 'list[string]'}, 'standby-whitelisted-ips': {'module': 'database', 'class': 'list[string]'}, 'nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'customer-contacts': {'module': 'database', 'class': 'list[CustomerContact]'}, 'scheduled-operations': {'module': 'database', 'class': 'list[ScheduledOperationDetails]'}, 'db-tools-details': {'module': 'database', 'class': 'list[DatabaseTool]'}}, output_type={'module': 'database', 'class': 'AutonomousDatabase'})
@cli_util.wrap_exceptions
def create_autonomous_database_create_autonomous_database_details(ctx, **kwargs):

    if 'maintenance_schedule_type' in kwargs:
        kwargs['autonomous_maintenance_schedule_type'] = kwargs['maintenance_schedule_type']
        kwargs.pop('maintenance_schedule_type')

    if 'is_acl_enabled' in kwargs and kwargs['is_acl_enabled']:
        kwargs['is_access_control_enabled'] = kwargs['is_acl_enabled']

    del kwargs['is_acl_enabled']

    ctx.invoke(database_cli.create_autonomous_database_create_autonomous_database_details, **kwargs)


# Rename parameter name for create_autonomous_database_create_autonomous_database_clone_details
@cli_util.copy_params_from_generated_command(database_cli.create_autonomous_database_create_autonomous_database_clone_details, params_to_exclude=['is_access_control_enabled', 'autonomous_maintenance_schedule_type'])
@cli_util.option('--maintenance-schedule-type', type=custom_types.CliCaseInsensitiveChoice(["EARLY", "REGULAR"]), help="""The maintenance schedule type of the Autonomous Database on shared Exadata infrastructure. The EARLY maintenance schedule of this Autonomous Database follows a schedule that applies patches prior to the REGULAR schedule.The REGULAR maintenance schedule of this Autonomous Database follows the normal cycle.""")
@cli_util.option('--is-acl-enabled', required=False, type=click.BOOL, help="""Indicates if the database-level access control is enabled. If disabled, database access is defined by the network security rules. If enabled, database access is restricted to the IP addresses defined by the rules specified with the `whitelistedIps` property. While specifying `whitelistedIps` rules is optional,  if database-level access control is enabled and no rules are specified, the database will become inaccessible. The rules can be added later using the `UpdateAutonomousDatabase` API operation or edit option in console. When creating a database clone, the desired access control setting should be specified. By default, database-level access control will be disabled for the clone.

This property is applicable only to Autonomous Databases on the Exadata Cloud@Customer platform.""")
@database_cli.autonomous_database_group.command(name='create-from-clone', help=database_cli.create_autonomous_database_create_autonomous_database_clone_details.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'whitelisted-ips': {'module': 'database', 'class': 'list[string]'}, 'standby-whitelisted-ips': {'module': 'database', 'class': 'list[string]'}, 'nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'customer-contacts': {'module': 'database', 'class': 'list[CustomerContact]'}, 'scheduled-operations': {'module': 'database', 'class': 'list[ScheduledOperationDetails]'}, 'db-tools-details': {'module': 'database', 'class': 'list[DatabaseTool]'}}, output_type={'module': 'database', 'class': 'AutonomousDatabase'})
@cli_util.wrap_exceptions
def create_autonomous_database_create_autonomous_database_clone_details(ctx, **kwargs):

    if 'maintenance_schedule_type' in kwargs:
        kwargs['autonomous_maintenance_schedule_type'] = kwargs['maintenance_schedule_type']
        kwargs.pop('maintenance_schedule_type')

    if 'is_acl_enabled' in kwargs and kwargs['is_acl_enabled']:
        kwargs['is_access_control_enabled'] = kwargs['is_acl_enabled']

    del kwargs['is_acl_enabled']

    ctx.invoke(database_cli.create_autonomous_database_create_autonomous_database_clone_details, **kwargs)


# Rename parameter name for update_autonomous_database
@cli_util.copy_params_from_generated_command(database_cli.update_autonomous_database, params_to_exclude=['is_access_control_enabled'])
@cli_util.option('--is-acl-enabled', required=False, type=click.BOOL, help="""Indicates if the database-level access control is enabled. If disabled, database access is defined by the network security rules. If enabled, database access is restricted to the IP addresses defined by the rules specified with the `whitelistedIps` property. While specifying `whitelistedIps` rules is optional,  if database-level access control is enabled and no rules are specified, the database will become inaccessible. The rules can be added later using the `UpdateAutonomousDatabase` API operation or edit option in console. When creating a database clone, the desired access control setting should be specified. By default, database-level access control will be disabled for the clone.

This property is applicable only to Autonomous Databases on the Exadata Cloud@Customer platform.""")
@database_cli.autonomous_database_group.command(name='update', help=database_cli.update_autonomous_database.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'whitelisted-ips': {'module': 'database', 'class': 'list[string]'}, 'standby-whitelisted-ips': {'module': 'database', 'class': 'list[string]'}, 'nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'customer-contacts': {'module': 'database', 'class': 'list[CustomerContact]'}, 'scheduled-operations': {'module': 'database', 'class': 'list[ScheduledOperationDetails]'}, 'db-tools-details': {'module': 'database', 'class': 'list[DatabaseTool]'}}, output_type={'module': 'database', 'class': 'AutonomousDatabase'})
@cli_util.wrap_exceptions
def update_autonomous_database(ctx, **kwargs):
    if 'is_acl_enabled' in kwargs and kwargs['is_acl_enabled']:
        kwargs['is_access_control_enabled'] = kwargs['is_acl_enabled']

    del kwargs['is_acl_enabled']

    ctx.invoke(database_cli.update_autonomous_database, **kwargs)


# Simplifying complex parameter credential_details, enable_database_management
@cli_util.copy_params_from_generated_command(database_cli.enable_database_management, params_to_exclude=['credential_details'])
@database_cli.database_group.command(name='enable-database-management', help=u"""Enables the Database Management service for an Oracle Database located in Oracle Cloud Infrastructure. This service allows the database to access tools including Metrics and Performance hub. Database Management is enabled at the container database (CDB) level.""")
@cli_util.option('--user-name', required=True, help=u"""The name of the Oracle Database user that will be used to connect to the database.""")
@cli_util.option('--password-secret-id', required=True, help=u"""The OCID of the Oracle Cloud Infrastructure secret.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def enable_database_management_extended(ctx, **kwargs):
    credential_details = {}
    if 'user_name' in kwargs and kwargs['user_name'] is not None:
        credential_details['userName'] = kwargs['user_name']
        kwargs.pop('user_name')

    if 'password_secret_id' in kwargs and kwargs['password_secret_id'] is not None:
        credential_details['passwordSecretId'] = kwargs['password_secret_id']
        kwargs.pop('password_secret_id')

    if len(credential_details) > 0:
        kwargs['credential_details'] = json.dumps(credential_details)

    ctx.invoke(database_cli.enable_database_management, **kwargs)


# Simplifying complex parameter credential_details, modify_database_management
@cli_util.copy_params_from_generated_command(database_cli.modify_database_management, params_to_exclude=['credential_details'])
@database_cli.database_group.command(name='modify-database-management', help=u"""Updates one or more attributes of the Database Management service for the database.""")
@cli_util.option('--user-name', help=u"""The name of the Oracle Database user that will be used to connect to the database.""")
@cli_util.option('--password-secret-id', help=u"""The OCID of the Oracle Cloud Infrastructure secret.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def modify_database_management_extended(ctx, **kwargs):
    credential_details = {}
    if 'user_name' in kwargs and kwargs['user_name'] is not None:
        credential_details['userName'] = kwargs['user_name']

    if 'password_secret_id' in kwargs and kwargs['password_secret_id'] is not None:
        credential_details['passwordSecretId'] = kwargs['password_secret_id']

    if len(credential_details) > 0:
        kwargs['credential_details'] = json.dumps(credential_details)
    kwargs.pop('user_name')
    kwargs.pop('password_secret_id')
    ctx.invoke(database_cli.modify_database_management, **kwargs)


# Hide --is-access-control-enabled from following command
@cli_util.copy_params_from_generated_command(database_cli.create_autonomous_database_create_refreshable_autonomous_database_clone_details, params_to_exclude=['is_access_control_enabled', 'autonomous_maintenance_schedule_type'])
@database_cli.autonomous_database_group.command(name='create-refreshable-clone', help=database_cli.create_autonomous_database_create_refreshable_autonomous_database_clone_details.help)
@cli_util.option('--maintenance-schedule-type', type=custom_types.CliCaseInsensitiveChoice(["EARLY", "REGULAR"]), help="""The maintenance schedule type of the Autonomous Database on shared Exadata infrastructure. The EARLY maintenance schedule of this Autonomous Database follows a schedule that applies patches prior to the REGULAR schedule.The REGULAR maintenance schedule of this Autonomous Database follows the normal cycle.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'whitelisted-ips': {'module': 'database', 'class': 'list[string]'}, 'standby-whitelisted-ips': {'module': 'database', 'class': 'list[string]'}, 'nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'customer-contacts': {'module': 'database', 'class': 'list[CustomerContact]'}, 'scheduled-operations': {'module': 'database', 'class': 'list[ScheduledOperationDetails]'}, 'db-tools-details': {'module': 'database', 'class': 'list[DatabaseTool]'}}, output_type={'module': 'database', 'class': 'AutonomousDatabase'})
@cli_util.wrap_exceptions
def create_autonomous_database_create_refreshable_autonomous_database_clone_details(ctx, **kwargs):

    if 'maintenance_schedule_type' in kwargs:
        kwargs['autonomous_maintenance_schedule_type'] = kwargs['maintenance_schedule_type']
        kwargs.pop('maintenance_schedule_type')

    ctx.invoke(database_cli.create_autonomous_database_create_refreshable_autonomous_database_clone_details, **kwargs)


# Hide --is-access-control-enabled from following command
@cli_util.copy_params_from_generated_command(database_cli.create_autonomous_database_create_autonomous_database_from_backup_details, params_to_exclude=['is_access_control_enabled', 'autonomous_maintenance_schedule_type'])
@database_cli.autonomous_database_group.command(name='create-from-backup-id', help=database_cli.create_autonomous_database_create_autonomous_database_from_backup_details.help)
@cli_util.option('--maintenance-schedule-type', type=custom_types.CliCaseInsensitiveChoice(["EARLY", "REGULAR"]), help="""The maintenance schedule type of the Autonomous Database on shared Exadata infrastructure. The EARLY maintenance schedule of this Autonomous Database follows a schedule that applies patches prior to the REGULAR schedule.The REGULAR maintenance schedule of this Autonomous Database follows the normal cycle.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'whitelisted-ips': {'module': 'database', 'class': 'list[string]'}, 'standby-whitelisted-ips': {'module': 'database', 'class': 'list[string]'}, 'nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'customer-contacts': {'module': 'database', 'class': 'list[CustomerContact]'}, 'scheduled-operations': {'module': 'database', 'class': 'list[ScheduledOperationDetails]'}, 'db-tools-details': {'module': 'database', 'class': 'list[DatabaseTool]'}}, output_type={'module': 'database', 'class': 'AutonomousDatabase'})
@cli_util.wrap_exceptions
def create_autonomous_database_create_autonomous_database_from_backup_details(ctx, **kwargs):

    if 'maintenance_schedule_type' in kwargs:
        kwargs['autonomous_maintenance_schedule_type'] = kwargs['maintenance_schedule_type']
        kwargs.pop('maintenance_schedule_type')

    ctx.invoke(database_cli.create_autonomous_database_create_autonomous_database_from_backup_details, **kwargs)


# Hide --is-access-control-enabled from following command
@cli_util.copy_params_from_generated_command(database_cli.create_autonomous_database_create_autonomous_database_from_backup_timestamp_details, params_to_exclude=['is_access_control_enabled', 'autonomous_maintenance_schedule_type'])
@database_cli.autonomous_database_group.command(name='create-from-backup-timestamp', help=database_cli.create_autonomous_database_create_autonomous_database_from_backup_timestamp_details.help)
@cli_util.option('--maintenance-schedule-type', type=custom_types.CliCaseInsensitiveChoice(["EARLY", "REGULAR"]), help="""The maintenance schedule type of the Autonomous Database on shared Exadata infrastructure. The EARLY maintenance schedule of this Autonomous Database follows a schedule that applies patches prior to the REGULAR schedule.The REGULAR maintenance schedule of this Autonomous Database follows the normal cycle.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'whitelisted-ips': {'module': 'database', 'class': 'list[string]'}, 'standby-whitelisted-ips': {'module': 'database', 'class': 'list[string]'}, 'nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'customer-contacts': {'module': 'database', 'class': 'list[CustomerContact]'}, 'scheduled-operations': {'module': 'database', 'class': 'list[ScheduledOperationDetails]'}, 'db-tools-details': {'module': 'database', 'class': 'list[DatabaseTool]'}}, output_type={'module': 'database', 'class': 'AutonomousDatabase'})
@cli_util.wrap_exceptions
def create_autonomous_database_create_autonomous_database_from_backup_timestamp_details(ctx, **kwargs):

    if 'maintenance_schedule_type' in kwargs:
        kwargs['autonomous_maintenance_schedule_type'] = kwargs['maintenance_schedule_type']
        kwargs.pop('maintenance_schedule_type')

    ctx.invoke(database_cli.create_autonomous_database_create_autonomous_database_from_backup_timestamp_details, **kwargs)


cli_util.rename_command(database_cli, database_cli.db_root_group, database_cli.flex_component_collection_group, "flex-component")
cli_util.rename_command(database_cli, database_cli.flex_component_collection_group, database_cli.list_flex_components, "list")


# oci db external-container-database -> oci db external-cdb
# oci db external-pluggable-database -> oci db external-pdb
# oci db external-non-container-database -> oci db external-non-cdb
# oci db external-database-connector -> oci db external-db-connector
# oci db external-container-database enable-external-container-database-database-management -> oci db external-container-database enable-db-management
# oci db external-non-container-database enable-external-non-container-database-database-management -> oci db external-non-container-database enable-db-management
# oci db external-pluggable-database enable-external-pluggable-database-database-management -> oci db external-pluggable-database enable-db-management
# oci db external-container-database disable-external-container-database-database-management -> oci db external-container-database disable-db-management
# oci db external-non-container-database disable-external-non-container-database-database-management -> oci db external-non-container-database disable-db-management
# oci db external-pluggable-database disable-external-pluggable-database-database-management -> oci db external-pluggable-database disable-db-management
# oci db external-database-connector create-external-database-connector-create-external-macs-connector-details -> oci db external-database-connector create-macs-connector
# oci db external-database-connector check-external-database-connector-connection-status -> oci db external-database-connector check-connection-status
# oci db external-container-database list-external-pluggable-databases -> oci db external-container-database list-external-pdbs
# oci db external-container-database scan-external-container-database-pluggable-databases -> oci db external-container-database scan-pluggable-databases
# Remove oci db external-database-connector create (user should use concrete subtypes, such as create-macs-connector)
# Remove oci db external-database-connector update (user should use concrete subtypes, such as update-macs-connector)
cli_util.rename_command(database_cli, database_cli.db_root_group, database_cli.external_container_database_group, "external-cdb")
cli_util.rename_command(database_cli, database_cli.db_root_group, database_cli.external_pluggable_database_group, "external-pdb")
cli_util.rename_command(database_cli, database_cli.db_root_group, database_cli.external_non_container_database_group, "external-non-cdb")
cli_util.rename_command(database_cli, database_cli.db_root_group, database_cli.external_database_connector_group, "external-db-connector")
cli_util.rename_command(database_cli, database_cli.external_container_database_group, database_cli.enable_external_container_database_database_management, "enable-db-management")
cli_util.rename_command(database_cli, database_cli.external_non_container_database_group, database_cli.enable_external_non_container_database_database_management, "enable-db-management")
cli_util.rename_command(database_cli, database_cli.external_pluggable_database_group, database_cli.enable_external_pluggable_database_database_management, "enable-db-management")
cli_util.rename_command(database_cli, database_cli.external_container_database_group, database_cli.disable_external_container_database_database_management, "disable-db-management")
cli_util.rename_command(database_cli, database_cli.external_non_container_database_group, database_cli.disable_external_non_container_database_database_management, "disable-db-management")
cli_util.rename_command(database_cli, database_cli.external_pluggable_database_group, database_cli.disable_external_pluggable_database_database_management, "disable-db-management")
cli_util.rename_command(database_cli, database_cli.external_database_connector_group, database_cli.create_external_database_connector_create_external_macs_connector_details, "create-macs-connector")
cli_util.rename_command(database_cli, database_cli.external_database_connector_group, database_cli.check_external_database_connector_connection_status, "check-connection-status")

cli_util.rename_command(database_cli, database_cli.external_container_database_group, database_cli.scan_external_container_database_pluggable_databases, "scan-pluggable-databases")
cli_util.rename_command(database_cli, database_cli.external_database_connector_group, database_cli.update_external_database_connector_update_external_macs_connector_details, "update-macs-connector")
database_cli.external_database_connector_group.commands.pop(database_cli.create_external_database_connector.name)
database_cli.external_database_connector_group.commands.pop(database_cli.update_external_database_connector.name)

database_cli.external_pluggable_database_group.commands.pop(database_cli.list_external_pluggable_databases.name)
# cli_util.rename_command(database_cli, database_cli.external_container_database_group, database_cli.list_external_pluggable_databases, "")


@cli_util.copy_params_from_generated_command(database_cli.change_external_container_database_compartment, params_to_exclude=['external_container_database_id'])
@database_cli.external_container_database_group.command(name=database_cli.change_external_container_database_compartment.name, help=database_cli.change_external_container_database_compartment.help)
@cli_util.option('--external-cdb-id', required=True, help=u"""The ExternalContainerDatabase [OCID]. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_external_container_database_compartment_extended(ctx, **kwargs):
    if 'external_cdb_id' in kwargs:
        kwargs['external_container_database_id'] = kwargs['external_cdb_id']
        kwargs.pop('external_cdb_id')

    ctx.invoke(database_cli.change_external_container_database_compartment, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.delete_external_container_database, params_to_exclude=['external_container_database_id'])
@database_cli.external_container_database_group.command(name=database_cli.delete_external_container_database.name, help=database_cli.delete_external_container_database.help)
@cli_util.option('--external-cdb-id', required=True, help=u"""The ExternalContainerDatabase [OCID]. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_external_container_database_extended(ctx, **kwargs):
    if 'external_cdb_id' in kwargs:
        kwargs['external_container_database_id'] = kwargs['external_cdb_id']
        kwargs.pop('external_cdb_id')

    ctx.invoke(database_cli.delete_external_container_database, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.disable_external_container_database_database_management, params_to_exclude=['external_container_database_id'])
@database_cli.external_container_database_group.command(name=database_cli.disable_external_container_database_database_management.name, help=database_cli.disable_external_container_database_database_management.help)
@cli_util.option('--external-cdb-id', required=True, help=u"""The ExternalContainerDatabase [OCID]. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def disable_external_container_database_database_management_extended(ctx, **kwargs):
    if 'external_cdb_id' in kwargs:
        kwargs['external_container_database_id'] = kwargs['external_cdb_id']
        kwargs.pop('external_cdb_id')

    ctx.invoke(database_cli.disable_external_container_database_database_management, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.enable_external_container_database_database_management, params_to_exclude=['external_container_database_id', 'external_database_connector_id'])
@database_cli.external_container_database_group.command(name=database_cli.enable_external_container_database_database_management.name, help=database_cli.enable_external_container_database_database_management.help)
@cli_util.option('--external-cdb-id', required=True, help=u"""The ExternalContainerDatabase [OCID]. [required]""")
@cli_util.option('--external-db-connector-id', required=True, help=u"""The [OCID] of the [external database connector]. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def enable_external_container_database_database_management_extended(ctx, **kwargs):
    if 'external_cdb_id' in kwargs:
        kwargs['external_container_database_id'] = kwargs['external_cdb_id']
        kwargs.pop('external_cdb_id')

    if 'external_db_connector_id' in kwargs:
        kwargs['external_database_connector_id'] = kwargs['external_db_connector_id']
        kwargs.pop('external_db_connector_id')

    ctx.invoke(database_cli.enable_external_container_database_database_management, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.get_external_container_database, params_to_exclude=['external_container_database_id'])
@database_cli.external_container_database_group.command(name=database_cli.get_external_container_database.name, help=database_cli.get_external_container_database.help)
@cli_util.option('--external-cdb-id', required=True, help=u"""The ExternalContainerDatabase [OCID]. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'ExternalContainerDatabase'})
@cli_util.wrap_exceptions
def get_external_container_database_extended(ctx, **kwargs):
    if 'external_cdb_id' in kwargs:
        kwargs['external_container_database_id'] = kwargs['external_cdb_id']
        kwargs.pop('external_cdb_id')

    ctx.invoke(database_cli.get_external_container_database, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.list_external_pluggable_databases, params_to_exclude=['external_container_database_id'])
@database_cli.external_container_database_group.command(name="list-external-pdbs", help=database_cli.list_external_pluggable_databases.help)
@cli_util.option('--external-cdb-id', help=u"""The ExternalContainerDatabase [OCID].""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[ExternalPluggableDatabaseSummary]'})
@cli_util.wrap_exceptions
def list_external_pluggable_databases_extended(ctx, **kwargs):
    if 'external_cdb_id' in kwargs:
        kwargs['external_container_database_id'] = kwargs['external_cdb_id']
        kwargs.pop('external_cdb_id')

    ctx.invoke(database_cli.list_external_pluggable_databases, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.scan_external_container_database_pluggable_databases, params_to_exclude=['external_container_database_id', 'external_database_connector_id'])
@database_cli.external_container_database_group.command(name=database_cli.scan_external_container_database_pluggable_databases.name, help=database_cli.scan_external_container_database_pluggable_databases.help)
@cli_util.option('--external-cdb-id', required=True, help=u"""The ExternalContainerDatabase [OCID]. [required]""")
@cli_util.option('--external-db-connector-id', required=True, help=u"""The [OCID] of the external database connector resource (`ExternalDatabaseConnectorId`). [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def scan_external_container_database_pluggable_databases_extended(ctx, **kwargs):
    if 'external_cdb_id' in kwargs:
        kwargs['external_container_database_id'] = kwargs['external_cdb_id']
        kwargs.pop('external_cdb_id')

    if 'external_db_connector_id' in kwargs:
        kwargs['external_database_connector_id'] = kwargs['external_db_connector_id']
        kwargs.pop('external_db_connector_id')

    ctx.invoke(database_cli.scan_external_container_database_pluggable_databases, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.update_external_container_database, params_to_exclude=['external_container_database_id', 'display_name'])
@database_cli.external_container_database_group.command(name=database_cli.update_external_container_database.name, help=database_cli.update_external_container_database.help)
@cli_util.option('--external-cdb-id', required=True, help=u"""The ExternalContainerDatabase [OCID]. [required]""")
@cli_util.option('--display-name', help=u"""The user-friendly name for the external database. The name does not have to be unique.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'ExternalContainerDatabase'})
@cli_util.wrap_exceptions
def update_external_container_database_extended(ctx, **kwargs):
    if 'external_cdb_id' in kwargs:
        kwargs['external_container_database_id'] = kwargs['external_cdb_id']
        kwargs.pop('external_cdb_id')

    ctx.invoke(database_cli.update_external_container_database, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.check_external_database_connector_connection_status, params_to_exclude=['external_database_connector_id'])
@database_cli.external_database_connector_group.command(name=database_cli.check_external_database_connector_connection_status.name, help=database_cli.check_external_database_connector_connection_status.help)
@cli_util.option('--external-db-connector-id', required=True, help=u"""The [OCID] of the external database connector resource (`ExternalDatabaseConnectorId`). [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def check_external_database_connector_connection_status_extended(ctx, **kwargs):
    if 'external_db_connector_id' in kwargs:
        kwargs['external_database_connector_id'] = kwargs['external_db_connector_id']
        kwargs.pop('external_db_connector_id')

    ctx.invoke(database_cli.check_external_database_connector_connection_status, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.delete_external_database_connector, params_to_exclude=['external_database_connector_id'])
@database_cli.external_database_connector_group.command(name=database_cli.delete_external_database_connector.name, help=database_cli.delete_external_database_connector.help)
@cli_util.option('--external-db-connector-id', required=True, help=u"""The [OCID] of the external database connector resource (`ExternalDatabaseConnectorId`). [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_external_database_connector_extended(ctx, **kwargs):
    if 'external_db_connector_id' in kwargs:
        kwargs['external_database_connector_id'] = kwargs['external_db_connector_id']
        kwargs.pop('external_db_connector_id')

    ctx.invoke(database_cli.delete_external_database_connector, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.get_external_database_connector, params_to_exclude=['external_database_connector_id'])
@database_cli.external_database_connector_group.command(name=database_cli.get_external_database_connector.name, help=database_cli.get_external_database_connector.help)
@cli_util.option('--external-db-connector-id', required=True, help=u"""The [OCID] of the external database connector resource (`ExternalDatabaseConnectorId`). [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'ExternalDatabaseConnector'})
@cli_util.wrap_exceptions
def get_external_database_connector_extended(ctx, **kwargs):
    if 'external_db_connector_id' in kwargs:
        kwargs['external_database_connector_id'] = kwargs['external_db_connector_id']
        kwargs.pop('external_db_connector_id')

    ctx.invoke(database_cli.get_external_database_connector, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.update_external_database_connector, params_to_exclude=['external_database_connector_id'])
@database_cli.external_database_connector_group.command(name=database_cli.update_external_database_connector.name, help=database_cli.update_external_database_connector.help)
@cli_util.option('--external-db-connector-id', required=True, help=u"""The [OCID] of the external database connector resource (`ExternalDatabaseConnectorId`). [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'ExternalDatabaseConnector'})
@cli_util.wrap_exceptions
def update_external_database_connector_extended(ctx, **kwargs):
    if 'external_db_connector_id' in kwargs:
        kwargs['external_database_connector_id'] = kwargs['external_db_connector_id']
        kwargs.pop('external_db_connector_id')

    ctx.invoke(database_cli.update_external_database_connector, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.update_external_database_connector_update_external_macs_connector_details, params_to_exclude=['external_database_connector_id'])
@database_cli.external_database_connector_group.command(name=database_cli.update_external_database_connector_update_external_macs_connector_details.name, help=database_cli.update_external_database_connector_update_external_macs_connector_details.help)
@cli_util.option('--external-db-connector-id', required=True, help=u"""The [OCID] of the external database connector resource (`ExternalDatabaseConnectorId`). [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'connection-string': {'module': 'database', 'class': 'DatabaseConnectionString'}, 'connection-credentials': {'module': 'database', 'class': 'DatabaseConnectionCredentials'}}, output_type={'module': 'database', 'class': 'ExternalDatabaseConnector'})
@cli_util.wrap_exceptions
def update_external_database_connector_update_external_macs_connector_details_extended(ctx, **kwargs):
    if 'external_db_connector_id' in kwargs:
        kwargs['external_database_connector_id'] = kwargs['external_db_connector_id']
        kwargs.pop('external_db_connector_id')

    ctx.invoke(database_cli.update_external_database_connector_update_external_macs_connector_details, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.change_external_non_container_database_compartment, params_to_exclude=['external_non_container_database_id'])
@database_cli.external_non_container_database_group.command(name=database_cli.change_external_non_container_database_compartment.name, help=database_cli.change_external_non_container_database_compartment.help)
@cli_util.option('--external-non-cdb-id', required=True, help=u"""The external non-container database [OCID]. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_external_non_container_database_compartment_extended(ctx, **kwargs):
    if 'external_non_cdb_id' in kwargs:
        kwargs['external_non_container_database_id'] = kwargs['external_non_cdb_id']
        kwargs.pop('external_non_cdb_id')

    ctx.invoke(database_cli.change_external_non_container_database_compartment, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.delete_external_non_container_database, params_to_exclude=['external_non_container_database_id'])
@database_cli.external_non_container_database_group.command(name=database_cli.delete_external_non_container_database.name, help=database_cli.delete_external_non_container_database.help)
@cli_util.option('--external-non-cdb-id', required=True, help=u"""The external non-container database [OCID]. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_external_non_container_database_extended(ctx, **kwargs):
    if 'external_non_cdb_id' in kwargs:
        kwargs['external_non_container_database_id'] = kwargs['external_non_cdb_id']
        kwargs.pop('external_non_cdb_id')

    ctx.invoke(database_cli.delete_external_non_container_database, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.disable_external_non_container_database_database_management, params_to_exclude=['external_non_container_database_id'])
@database_cli.external_non_container_database_group.command(name=database_cli.disable_external_non_container_database_database_management.name, help=database_cli.disable_external_non_container_database_database_management.help)
@cli_util.option('--external-non-cdb-id', required=True, help=u"""The external non-container database [OCID]. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def disable_external_non_container_database_database_management_extended(ctx, **kwargs):
    if 'external_non_cdb_id' in kwargs:
        kwargs['external_non_container_database_id'] = kwargs['external_non_cdb_id']
        kwargs.pop('external_non_cdb_id')

    ctx.invoke(database_cli.disable_external_non_container_database_database_management, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.enable_external_non_container_database_database_management, params_to_exclude=['external_database_connector_id', 'external_non_container_database_id'])
@database_cli.external_non_container_database_group.command(name=database_cli.enable_external_non_container_database_database_management.name, help=database_cli.enable_external_non_container_database_database_management.help)
@cli_util.option('--external-db-connector-id', required=True, help=u"""The [OCID] of the [external database connector]. [required]""")
@cli_util.option('--external-non-cdb-id', required=True, help=u"""The external non-container database [OCID]. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def enable_external_non_container_database_database_management_extended(ctx, **kwargs):
    if 'external_db_connector_id' in kwargs:
        kwargs['external_database_connector_id'] = kwargs['external_db_connector_id']
        kwargs.pop('external_db_connector_id')

    if 'external_non_cdb_id' in kwargs:
        kwargs['external_non_container_database_id'] = kwargs['external_non_cdb_id']
        kwargs.pop('external_non_cdb_id')

    ctx.invoke(database_cli.enable_external_non_container_database_database_management, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.get_external_non_container_database, params_to_exclude=['external_non_container_database_id'])
@database_cli.external_non_container_database_group.command(name=database_cli.get_external_non_container_database.name, help=database_cli.get_external_non_container_database.help)
@cli_util.option('--external-non-cdb-id', required=True, help=u"""The external non-container database [OCID]. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'ExternalNonContainerDatabase'})
@cli_util.wrap_exceptions
def get_external_non_container_database_extended(ctx, **kwargs):
    if 'external_non_cdb_id' in kwargs:
        kwargs['external_non_container_database_id'] = kwargs['external_non_cdb_id']
        kwargs.pop('external_non_cdb_id')

    ctx.invoke(database_cli.get_external_non_container_database, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.update_external_non_container_database, params_to_exclude=['external_non_container_database_id', 'display_name'])
@database_cli.external_non_container_database_group.command(name=database_cli.update_external_non_container_database.name, help=database_cli.update_external_non_container_database.help)
@cli_util.option('--external-non-cdb-id', required=True, help=u"""The external non-container database [OCID]. [required]""")
@cli_util.option('--display-name', help=u"""The user-friendly name for the external database. The name does not have to be unique.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'ExternalNonContainerDatabase'})
@cli_util.wrap_exceptions
def update_external_non_container_database_extended(ctx, **kwargs):
    if 'external_non_cdb_id' in kwargs:
        kwargs['external_non_container_database_id'] = kwargs['external_non_cdb_id']
        kwargs.pop('external_non_cdb_id')

    ctx.invoke(database_cli.update_external_non_container_database, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.change_external_pluggable_database_compartment, params_to_exclude=['external_pluggable_database_id'])
@database_cli.external_pluggable_database_group.command(name=database_cli.change_external_pluggable_database_compartment.name, help=database_cli.change_external_pluggable_database_compartment.help)
@cli_util.option('--external-pdb-id', required=True, help=u"""The ExternalPluggableDatabaseId [OCID]. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_external_pluggable_database_compartment_extended(ctx, **kwargs):
    if 'external_pdb_id' in kwargs:
        kwargs['external_pluggable_database_id'] = kwargs['external_pdb_id']
        kwargs.pop('external_pdb_id')

    ctx.invoke(database_cli.change_external_pluggable_database_compartment, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.create_external_pluggable_database, params_to_exclude=['external_container_database_id'])
@database_cli.external_pluggable_database_group.command(name=database_cli.create_external_pluggable_database.name, help=database_cli.create_external_pluggable_database.help)
@cli_util.option('--external-cdb-id', required=True, help=u"""The [OCID] of the [external container database] that contains the specified [external pluggable database] resource. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'ExternalPluggableDatabase'})
@cli_util.wrap_exceptions
def create_external_pluggable_database_extended(ctx, **kwargs):
    if 'external_cdb_id' in kwargs:
        kwargs['external_container_database_id'] = kwargs['external_cdb_id']
        kwargs.pop('external_cdb_id')

    ctx.invoke(database_cli.create_external_pluggable_database, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.delete_external_pluggable_database, params_to_exclude=['external_pluggable_database_id'])
@database_cli.external_pluggable_database_group.command(name=database_cli.delete_external_pluggable_database.name, help=database_cli.delete_external_pluggable_database.help)
@cli_util.option('--external-pdb-id', required=True, help=u"""The ExternalPluggableDatabaseId [OCID]. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_external_pluggable_database_extended(ctx, **kwargs):
    if 'external_pdb_id' in kwargs:
        kwargs['external_pluggable_database_id'] = kwargs['external_pdb_id']
        kwargs.pop('external_pdb_id')

    ctx.invoke(database_cli.delete_external_pluggable_database, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.disable_external_pluggable_database_database_management, params_to_exclude=['external_pluggable_database_id'])
@database_cli.external_pluggable_database_group.command(name=database_cli.disable_external_pluggable_database_database_management.name, help=database_cli.disable_external_pluggable_database_database_management.help)
@cli_util.option('--external-pdb-id', required=True, help=u"""The ExternalPluggableDatabaseId [OCID]. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def disable_external_pluggable_database_database_management_extended(ctx, **kwargs):
    if 'external_pdb_id' in kwargs:
        kwargs['external_pluggable_database_id'] = kwargs['external_pdb_id']
        kwargs.pop('external_pdb_id')

    ctx.invoke(database_cli.disable_external_pluggable_database_database_management, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.enable_external_pluggable_database_database_management, params_to_exclude=['external_database_connector_id', 'external_pluggable_database_id'])
@database_cli.external_pluggable_database_group.command(name=database_cli.enable_external_pluggable_database_database_management.name, help=database_cli.enable_external_pluggable_database_database_management.help)
@cli_util.option('--external-db-connector-id', required=True, help=u"""The [OCID] of the [external database connector]. [required]""")
@cli_util.option('--external-pdb-id', required=True, help=u"""The ExternalPluggableDatabaseId [OCID]. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def enable_external_pluggable_database_database_management_extended(ctx, **kwargs):
    if 'external_db_connector_id' in kwargs:
        kwargs['external_database_connector_id'] = kwargs['external_db_connector_id']
        kwargs.pop('external_db_connector_id')

    if 'external_pdb_id' in kwargs:
        kwargs['external_pluggable_database_id'] = kwargs['external_pdb_id']
        kwargs.pop('external_pdb_id')

    ctx.invoke(database_cli.enable_external_pluggable_database_database_management, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.get_external_pluggable_database, params_to_exclude=['external_pluggable_database_id'])
@database_cli.external_pluggable_database_group.command(name=database_cli.get_external_pluggable_database.name, help=database_cli.get_external_pluggable_database.help)
@cli_util.option('--external-pdb-id', required=True, help=u"""The ExternalPluggableDatabaseId [OCID]. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'ExternalPluggableDatabase'})
@cli_util.wrap_exceptions
def get_external_pluggable_database_extended(ctx, **kwargs):
    if 'external_pdb_id' in kwargs:
        kwargs['external_pluggable_database_id'] = kwargs['external_pdb_id']
        kwargs.pop('external_pdb_id')

    ctx.invoke(database_cli.get_external_pluggable_database, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.update_external_pluggable_database, params_to_exclude=['external_pluggable_database_id', 'display_name'])
@database_cli.external_pluggable_database_group.command(name=database_cli.update_external_pluggable_database.name, help=database_cli.update_external_pluggable_database.help)
@cli_util.option('--external-pdb-id', required=True, help=u"""The ExternalPluggableDatabaseId [OCID]. [required]""")
@cli_util.option('--display-name', help=u"""The user-friendly name for the external database. The name does not have to be unique.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'ExternalPluggableDatabase'})
@cli_util.wrap_exceptions
def update_external_pluggable_database_extended(ctx, **kwargs):
    if 'external_pdb_id' in kwargs:
        kwargs['external_pluggable_database_id'] = kwargs['external_pdb_id']
        kwargs.pop('external_pdb_id')

    ctx.invoke(database_cli.update_external_pluggable_database, **kwargs)


# oci db external-non-cdb disable-external-non-container-database-operations-insights -> oci db external-non-cdb disable-operations-insights
cli_util.rename_command(database_cli, database_cli.external_non_container_database_group, database_cli.disable_external_non_container_database_operations_insights, "disable-operations-insights")


# oci db external-non-cdb enable-external-non-container-database-operations-insights -> oci db external-non-cdb enable-operations-insights
cli_util.rename_command(database_cli, database_cli.external_non_container_database_group, database_cli.enable_external_non_container_database_operations_insights, "enable-operations-insights")


# oci db external-pdb disable-external-pluggable-database-operations-insights -> oci db external-pdb disable-operations-insights
cli_util.rename_command(database_cli, database_cli.external_pluggable_database_group, database_cli.disable_external_pluggable_database_operations_insights, "disable-operations-insights")


# oci db external-pdb enable-external-pluggable-database-operations-insights -> oci db external-pdb enable-operations-insights
cli_util.rename_command(database_cli, database_cli.external_pluggable_database_group, database_cli.enable_external_pluggable_database_operations_insights, "enable-operations-insights")


@cli_util.copy_params_from_generated_command(database_cli.disable_external_non_container_database_operations_insights, params_to_exclude=['external_non_container_database_id'])
@database_cli.external_non_container_database_group.command(name=database_cli.disable_external_non_container_database_operations_insights.name, help=database_cli.disable_external_non_container_database_operations_insights.help)
@cli_util.option('--external-non-cdb-id', required=True, help=u"""The external non-container database [OCID]. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def disable_external_non_container_database_operations_insights_extended(ctx, **kwargs):
    if 'external_non_cdb_id' in kwargs:
        kwargs['external_non_container_database_id'] = kwargs['external_non_cdb_id']
        kwargs.pop('external_non_cdb_id')

    ctx.invoke(database_cli.disable_external_non_container_database_operations_insights, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.enable_external_non_container_database_operations_insights, params_to_exclude=['external_database_connector_id', 'external_non_container_database_id', 'external_database_connector_id'])
@database_cli.external_non_container_database_group.command(name=database_cli.enable_external_non_container_database_operations_insights.name, help=database_cli.enable_external_non_container_database_operations_insights.help)
@cli_util.option('--external-db-connector-id', required=True, help="""The [OCID] of the [external database connector]. [required]""")
@cli_util.option('--external-non-cdb-id', required=True, help=u"""The [OCID] of the external non-container database. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def enable_external_non_container_database_operations_insights_extended(ctx, **kwargs):

    if 'external_db_connector_id' in kwargs:
        kwargs['external_database_connector_id'] = kwargs['external_db_connector_id']
        kwargs.pop('external_db_connector_id')

    if 'external_non_cdb_id' in kwargs:
        kwargs['external_database_connector_id'] = kwargs['external_non_cdb_id']
        kwargs.pop('external_non_cdb_id')

    ctx.invoke(database_cli.enable_external_non_container_database_operations_insights, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.disable_external_pluggable_database_operations_insights, params_to_exclude=['external_pluggable_database_id'])
@database_cli.external_pluggable_database_group.command(name=database_cli.disable_external_pluggable_database_operations_insights.name, help=database_cli.disable_external_pluggable_database_operations_insights.help)
@cli_util.option('--external-pdb-id', required=True, help=u"""The ExternalPluggableDatabaseId [OCID]. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def disable_external_pluggable_database_operations_insights_extended(ctx, **kwargs):
    if 'external_pdb_id' in kwargs:
        kwargs['external_pluggable_database_id'] = kwargs['external_pdb_id']
        kwargs.pop('external_pdb_id')

    ctx.invoke(database_cli.disable_external_pluggable_database_operations_insights, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.enable_external_pluggable_database_operations_insights, params_to_exclude=['external_database_connector_id', 'external_pluggable_database_id', 'external_database_connector_id'])
@database_cli.external_pluggable_database_group.command(name=database_cli.enable_external_pluggable_database_operations_insights.name, help=database_cli.enable_external_pluggable_database_operations_insights.help)
@cli_util.option('--external-db-connector-id', required=True, help="""The [OCID] of the [external database connector]. [required]""")
@cli_util.option('--external-pdb-id', required=True, help=u"""The [OCID] of the external pluggable database. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def enable_external_pluggable_database_operations_insights_extended(ctx, **kwargs):

    if 'external_db_connector_id' in kwargs:
        kwargs['external_database_connector_id'] = kwargs['external_db_connector_id']
        kwargs.pop('external_db_connector_id')

    if 'external_pdb_id' in kwargs:
        kwargs['external_database_connector_id'] = kwargs['external_pdb_id']
        kwargs.pop('external_pdb_id')

    ctx.invoke(database_cli.enable_external_pluggable_database_operations_insights, **kwargs)


# oci db autonomous-database configure-autonomous-database-vault-key -> oci db autonomous-database configure-key
cli_util.rename_command(database_cli, database_cli.autonomous_database_group, database_cli.configure_autonomous_database_vault_key, "configure-key")

# oci db exadata-infrastructure add -> oci db exadata-infrastructure add-storage-capacity
cli_util.rename_command(database_cli, database_cli.exadata_infrastructure_group, database_cli.add_storage_capacity_exadata_infrastructure, "add-storage-capacity")

# oci db autonomous-database create-autonomous-database-create-cross-region-autonomous-database-data-guard-details -> oci db autonomous-database create-adb-cross-region-data-guard-details
cli_util.rename_command(database_cli, database_cli.autonomous_database_group, database_cli.create_autonomous_database_create_cross_region_autonomous_database_data_guard_details, "create-adb-cross-region-data-guard-details")


@cli_util.copy_params_from_generated_command(database_cli.create_autonomous_database_create_cross_region_autonomous_database_data_guard_details, params_to_exclude=['autonomous_maintenance_schedule_type'])
@database_cli.autonomous_database_group.command(name=database_cli.create_autonomous_database_create_cross_region_autonomous_database_data_guard_details.name, help=u"""Details to create an Autonomous Data Guard association for an existing Autonomous Database where the standby is in a different (remote) region from the source primary database.\n\r\n\rThe following parameters are optional for the cross-region standby database. If included in the request, these parameters contain the same values as the source Autonomous Database:\n\r    - customerContacts\n\r    - scheduledOperations\n\r    - isAutoScalingForStorageEnabled\n\r    - definedTags\n\r    - freeformTags\n\r    - licenseModel\n\r    - whitelistedIps\n\r    - isMtlsConnectionRequired\n\r    - dbName\n\r    - adminPassword\n\r    - cpuCoreCount\n\r    - dataStorageSizeInTB\n\r    - dbVersion\n\r\n\rExample I - Creating a cross-region standby with required parameters only:\n\r{\n\r   "compartmentId": "ocid.compartment.oc1..<var>&lt;unique_ID&gt;</var>",\n\r   "sourceId": "ocid1.autonomousdatabase.oc1.phx..<var>&lt;unique_ID&gt;</var>",\n\r   "source": "CROSS_REGION_DATAGUARD"\n\r}\n\rExample II - Creating a cross-region standby that specifies optional parameters in addition to the required parameters:\n\r{\n\r   "compartmentId": "ocid.compartment.oc1..<var>&lt;unique_ID&gt;</var>",\n\r   "cpuCoreCount": 1,\n\r   "dbName": "adatabasedb1",\n\r   "sourceId": "ocid1.autonomousdatabase.oc1.phx..<var>&lt;unique_ID&gt;</var>",\n\r   "dataStorageSizeInTBs": 1,\n\r   "source": "CROSS_REGION_DATAGUARD",\n\r   "adminPassword" : "<var>&lt;password&gt;</var>",\n\r   "dbVersion": "19c",\n\r   "licenseModel": "LICENSE_INCLUDED",\n\r   "isAutoScalingForStorageEnabled": "true"\n\r}""")
@cli_util.option('--maintenance-schedule-type', type=custom_types.CliCaseInsensitiveChoice(["EARLY", "REGULAR"]), help=u"""The maintenance schedule type of the Autonomous Database on shared Exadata infrastructure. The EARLY maintenance schedule of this Autonomous Database follows a schedule that applies patches prior to the REGULAR schedule.The REGULAR maintenance schedule of this Autonomous Database follows the normal cycle.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'whitelisted-ips': {'module': 'database', 'class': 'list[string]'}, 'standby-whitelisted-ips': {'module': 'database', 'class': 'list[string]'}, 'nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'customer-contacts': {'module': 'database', 'class': 'list[CustomerContact]'}, 'scheduled-operations': {'module': 'database', 'class': 'list[ScheduledOperationDetails]'}, 'db-tools-details': {'module': 'database', 'class': 'list[DatabaseTool]'}}, output_type={'module': 'database', 'class': 'AutonomousDatabase'})
@cli_util.wrap_exceptions
def create_autonomous_database_create_cross_region_autonomous_database_data_guard_details_extended(ctx, **kwargs):
    if 'maintenance_schedule_type' in kwargs:
        kwargs['autonomous_maintenance_schedule_type'] = kwargs['maintenance_schedule_type']
        kwargs.pop('maintenance_schedule_type')

    ctx.invoke(database_cli.create_autonomous_database_create_cross_region_autonomous_database_data_guard_details, **kwargs)


# Renaming DB PDB conversion sub command and history group
cli_util.rename_command(database_cli, database_cli.database_group, database_cli.list_pdb_conversion_history_entries, "list-pdb-conversion-history")
cli_util.rename_command(database_cli, database_cli.db_root_group, database_cli.pdb_conversion_history_entry_group, "pdb-conversion-history")

# Removing the  generated polymorphic  commands as we are redefining them
database_cli.database_group.commands.pop(database_cli.convert_to_pdb.name)
database_cli.database_group.commands.pop(database_cli.convert_to_pdb_pdb_conversion_to_new_database_details.name)


# Renaming the parameter pdb-conversion-history-entry-id to history-id
@cli_util.copy_params_from_generated_command(database_cli.get_pdb_conversion_history_entry, params_to_exclude=['pdb_conversion_history_entry_id'])
@cli_util.option('--history-id', required=True, help=u"""The database conversion history [OCID].""")
@database_cli.pdb_conversion_history_entry_group.command(name='get', help=database_cli.pdb_conversion_history_entry_group.help)
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'PdbConversionHistoryEntry'})
@cli_util.wrap_exceptions
def pdb_conversion_history_entry_extended(ctx, **kwargs):
    if 'history_id' in kwargs:
        kwargs['pdb_conversion_history_entry_id'] = kwargs['history_id']
        kwargs.pop('history_id')

    ctx.invoke(database_cli.get_pdb_conversion_history_entry, **kwargs)


# Renaming the parameter convert-to-pdb-target-details-cdb-name to cdb-name
# Renaming the parameter convert-to-pdb-target-details-pdb-admin-password to pdb-admin-password
# Renaming the parameter convert-to-pdb-target-details-cdb-tde-wallet-password to cdb-tde-password
# Renaming the parameter convert-to-pdb-target-details-additional-cdb-params to additional-cdb-params
# Renaming the parameter convert-to-pdb-target-details-non-cdb-tde-wallet-password to non-cdb-tde-password
# Renaming the parameter convert-to-pdb-target-details-cdb-admin-password to cdb-admin-password
# Renaming the convert-to-pdb-pdb-conversion-to-new-database-detail command to convert-to-new-pdb-precheck and removing parameter action
@cli_util.copy_params_from_generated_command(database_cli.convert_to_pdb_pdb_conversion_to_new_database_details,
                                             params_to_exclude=['convert_to_pdb_target_details_cdb_name',
                                                                'convert_to_pdb_target_details_cdb_admin_password',
                                                                'convert_to_pdb_target_details_non_cdb_tde_wallet_password',
                                                                'convert_to_pdb_target_details_additional_cdb_params',
                                                                'convert_to_pdb_target_details_cdb_tde_wallet_password',
                                                                'convert_to_pdb_target_details_pdb_admin_password',
                                                                'action'])
@cli_util.option('--cdb-name', required=True,
                 help=u"""The database name. The name must begin with an alphabetic character and can contain a maximum of 14 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.""")
@cli_util.option('--cdb-admin-password', required=True,
                 help=u"""A strong password for SYS, SYSTEM, and the plugbable database ADMIN user of the container database after conversion. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numeric, and two special characters. The special characters must be _, \\#, or -.""")
@cli_util.option('--non-cdb-tde-password', required=True,
                 help=u"""The existing TDE wallet password of the non-container database.""")
@cli_util.option('--additional-cdb-params',
                 help=u"""Additional container database parameters. Example: \"_pdb_name_case_sensitive=true\"""")
@cli_util.option('--cdb-tde-password',
                 help=u"""The database name. The name must begin with an alphabetic character and can contain a maximum of 14 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.""")
@cli_util.option('--pdb-admin-password',
                 help=u"""A strong password for plugbable database ADMIN user of the container database after conversion. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numeric, and two special characters. The special characters must be _, \\#, or -.""")
@database_cli.database_group.command(name='convert-to-new-pdb-precheck', help=database_cli.database_group.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'Database'})
@cli_util.wrap_exceptions
def convert_to_pdb_pdb_conversion_to_new_database_details_precheck_extended(ctx, **kwargs):
    if 'cdb_name' in kwargs and kwargs['cdb_name']:
        kwargs['convert_to_pdb_target_details_cdb_name'] = kwargs['cdb_name']
        kwargs.pop('cdb_name')

    if 'cdb_admin_password' in kwargs and kwargs['cdb_admin_password']:
        kwargs['convert_to_pdb_target_details_cdb_admin_password'] = kwargs['cdb_admin_password']
        kwargs.pop('cdb_admin_password')

    if 'non_cdb_tde_password' in kwargs and kwargs['non_cdb_tde_password']:
        kwargs['convert_to_pdb_target_details_non_cdb_tde_wallet_password'] = kwargs['non_cdb_tde_password']
        kwargs.pop('non_cdb_tde_password')

    if 'additional_cdb_params' in kwargs and kwargs['additional_cdb_params']:
        kwargs['convert_to_pdb_target_details_additional_cdb_params'] = kwargs['additional_cdb_params']

    if 'cdb_tde_password' in kwargs and kwargs['cdb_tde_password']:
        kwargs['convert_to_pdb_target_details_cdb_tde_wallet_password'] = kwargs['cdb_tde_password']

    if 'pdb_admin_password' in kwargs and kwargs['pdb_admin_password']:
        kwargs['convert_to_pdb_target_details_pdb_admin_password'] = kwargs['pdb_admin_password']

    kwargs['action'] = "PRECHECK"

    kwargs.pop('additional_cdb_params')
    kwargs.pop('pdb_admin_password')
    kwargs.pop('cdb_tde_password')

    ctx.invoke(database_cli.convert_to_pdb_pdb_conversion_to_new_database_details, **kwargs)


# Renaming the parameter convert-to-pdb-target-details-cdb-name to cdb-name
# Renaming the parameter convert-to-pdb-target-details-pdb-admin-password to pdb-admin-password
# Renaming the parameter convert-to-pdb-target-details-cdb-tde-wallet-password to cdb-tde-password
# Renaming the parameter convert-to-pdb-target-details-additional-cdb-params to additional-cdb-params
# Renaming the parameter convert-to-pdb-target-details-non-cdb-tde-wallet-password to non-cdb-tde-password
# Renaming the parameter convert-to-pdb-target-details-cdb-admin-password to cdb-admin-password
# Renaming the convert-to-pdb-pdb-conversion-to-new-database-detail command to convert-to-new-pdb and removing parameter action
@cli_util.copy_params_from_generated_command(database_cli.convert_to_pdb_pdb_conversion_to_new_database_details,
                                             params_to_exclude=['convert_to_pdb_target_details_cdb_name',
                                                                'convert_to_pdb_target_details_cdb_admin_password',
                                                                'convert_to_pdb_target_details_non_cdb_tde_wallet_password',
                                                                'convert_to_pdb_target_details_additional_cdb_params',
                                                                'convert_to_pdb_target_details_cdb_tde_wallet_password',
                                                                'convert_to_pdb_target_details_pdb_admin_password',
                                                                'action'])
@cli_util.option('--cdb-name', required=True,
                 help=u"""The database name. The name must begin with an alphabetic character and can contain a maximum of 14 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.""")
@cli_util.option('--cdb-admin-password', required=True,
                 help=u"""A strong password for SYS, SYSTEM, and the plugbable database ADMIN user of the container database after conversion. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numeric, and two special characters. The special characters must be _, \\#, or -.""")
@cli_util.option('--non-cdb-tde-password', required=True,
                 help=u"""The existing TDE wallet password of the non-container database.""")
@cli_util.option('--additional-cdb-params',
                 help=u"""Additional container database parameters. Example: \"_pdb_name_case_sensitive=true\"""")
@cli_util.option('--cdb-tde-password',
                 help=u"""The database name. The name must begin with an alphabetic character and can contain a maximum of 14 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.""")
@cli_util.option('--pdb-admin-password',
                 help=u"""A strong password for plugbable database ADMIN user of the container database after conversion. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numeric, and two special characters. The special characters must be _, \\#, or -.""")
@database_cli.database_group.command(name='convert-to-new-pdb', help=database_cli.database_group.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'Database'})
@cli_util.wrap_exceptions
def convert_to_pdb_pdb_conversion_to_new_database_details_new_pdb_extended(ctx, **kwargs):
    if 'cdb_name' in kwargs and kwargs['cdb_name']:
        kwargs['convert_to_pdb_target_details_cdb_name'] = kwargs['cdb_name']
        kwargs.pop('cdb_name')

    if 'cdb_admin_password' in kwargs and kwargs['cdb_admin_password']:
        kwargs['convert_to_pdb_target_details_cdb_admin_password'] = kwargs['cdb_admin_password']
        kwargs.pop('cdb_admin_password')

    if 'non_cdb_tde_password' in kwargs and kwargs['non_cdb_tde_password']:
        kwargs['convert_to_pdb_target_details_non_cdb_tde_wallet_password'] = kwargs['non_cdb_tde_password']
        kwargs.pop('non_cdb_tde_password')

    if 'additional_cdb_params' in kwargs and kwargs['additional_cdb_params']:
        kwargs['convert_to_pdb_target_details_additional_cdb_params'] = kwargs['additional_cdb_params']

    if 'cdb_tde_password' in kwargs and kwargs['cdb_tde_password']:
        kwargs['convert_to_pdb_target_details_cdb_tde_wallet_password'] = kwargs['cdb_tde_password']

    if 'pdb_admin_password' in kwargs and kwargs['pdb_admin_password']:
        kwargs['convert_to_pdb_target_details_pdb_admin_password'] = kwargs['pdb_admin_password']

    kwargs['action'] = "CONVERT"

    kwargs.pop('additional_cdb_params')
    kwargs.pop('pdb_admin_password')
    kwargs.pop('cdb_tde_password')

    ctx.invoke(database_cli.convert_to_pdb_pdb_conversion_to_new_database_details, **kwargs)


# Renaming the convert-to-pdb command to convert-to-pdb-rollback and removing parameter action
@cli_util.copy_params_from_generated_command(database_cli.convert_to_pdb, params_to_exclude=['action', 'convert_to_pdb_target_details'])
@database_cli.database_group.command('convert-to-pdb-sync-rollback', help=database_cli.database_group.help)
@json_skeleton_utils.get_cli_json_input_option({'convert-to-pdb-target-details': {'module': 'database', 'class': 'ConvertToPdbTargetBase'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'convert-to-pdb-target-details': {'module': 'database', 'class': 'ConvertToPdbTargetBase'}}, output_type={'module': 'database', 'class': 'Database'})
@cli_util.wrap_exceptions
def convert_to_pdb_rollback_extended(ctx, **kwargs):
    kwargs['action'] = "SYNC_ROLLBACK"
    ctx.invoke(database_cli.convert_to_pdb, **kwargs)


# Renaming the convert-to-pdb command to convert-to-pdb-sync and removing parameter action
@cli_util.copy_params_from_generated_command(database_cli.convert_to_pdb, params_to_exclude=['action', 'convert_to_pdb_target_details'])
@database_cli.database_group.command('convert-to-pdb-sync', help=database_cli.database_group.help)
@json_skeleton_utils.get_cli_json_input_option({'convert-to-pdb-target-details': {'module': 'database', 'class': 'ConvertToPdbTargetBase'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'convert-to-pdb-target-details': {'module': 'database', 'class': 'ConvertToPdbTargetBase'}}, output_type={'module': 'database', 'class': 'Database'})
@cli_util.wrap_exceptions
def convert_to_pdb_sync_extended(ctx, **kwargs):
    kwargs['action'] = "SYNC"
    ctx.invoke(database_cli.convert_to_pdb, **kwargs)


# Renaming the parameter storage-volume-performance-mode to storage-performance
@cli_util.copy_params_from_generated_command(database_cli.launch_db_system_launch_db_system_from_db_system_details, params_to_exclude=['storage_volume_performance_mode', 'data_collection_options'])
@database_cli.db_system_group.command(name='launch-from-db-system', help=database_cli.launch_db_system_launch_db_system_from_db_system_details.help)
@cli_util.option('--storage-performance', type=custom_types.CliCaseInsensitiveChoice(["BALANCED", "HIGH_PERFORMANCE"]), help=u"""The block storage volume performance level. Valid values are `BALANCED` and `HIGH_PERFORMANCE`. See [Block Volume Performance] for more information.""")
@cli_util.option('--is-diagnostics-events-enabled', required=False, type=click.BOOL, help="""Enables customer to receive Events service notifications for guest VM issues""")
@cli_util.option('--is-health-monitoring-enabled', required=False, type=click.BOOL, help="""Enables Oracle to receive diagnostic data and share it with its operations and support personnel""")
@cli_util.option('--is-incident-logs-enabled', required=False, type=click.BOOL, help="""Enables Oracle to receive Events service notifications for guest VM issues, collect incident logs and traces""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fault-domains': {'module': 'database', 'class': 'list[string]'}, 'nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'backup-network-nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'db-system-options': {'module': 'database', 'class': 'DbSystemOptions'}, 'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'db-home': {'module': 'database', 'class': 'CreateDbHomeFromDbSystemDetails'}}, output_type={'module': 'database', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def launch_db_system_launch_db_system_from_db_system_details_extended(ctx, **kwargs):
    if 'storage_performance' in kwargs:
        kwargs['storage_volume_performance_mode'] = kwargs['storage_performance']
        kwargs.pop('storage_performance')
    data_collection_options = {}
    if 'is_diagnostics_events_enabled' in kwargs and kwargs['is_diagnostics_events_enabled'] is not None:
        data_collection_options['is_diagnostics_events_enabled'] = kwargs['is_diagnostics_events_enabled']

    if 'is_health_monitoring_enabled' in kwargs and kwargs['is_health_monitoring_enabled'] is not None:
        data_collection_options['is_health_monitoring_enabled'] = kwargs['is_health_monitoring_enabled']

    if 'is_incident_logs_enabled' in kwargs and kwargs['is_incident_logs_enabled'] is not None:
        data_collection_options['is_incident_logs_enabled'] = kwargs['is_incident_logs_enabled']

    if len(data_collection_options) > 0:
        kwargs['data_collection_options'] = json.dumps(data_collection_options)

    del kwargs['is_diagnostics_events_enabled']
    del kwargs['is_health_monitoring_enabled']
    del kwargs['is_incident_logs_enabled']
    ctx.invoke(database_cli.launch_db_system_launch_db_system_from_db_system_details, **kwargs)


# Expanding complex parameter credential_details for enable_pluggable_database_management
@cli_util.copy_params_from_generated_command(database_cli.enable_pluggable_database_management, params_to_exclude=['credential_details'])
@database_cli.pluggable_database_group.command(name='enable-pluggable-database-management', help=u"""Enables the Database Management service for an Oracle Pluggable Database located in Oracle Cloud Infrastructure. This service allows the pluggable database to access tools including Metrics and Performance hub. Database Management is enabled at the pluggable database (PDB) level.""")
@cli_util.option('--user-name', required=True, help=u"""The name of the Oracle Database user that will be used to connect to the database.""")
@cli_util.option('--password-secret-id', required=True, help=u"""The OCID of the Oracle Cloud Infrastructure secret.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def enable_pluggable_database_management_extended(ctx, **kwargs):
    credential_details = {}
    if 'user_name' in kwargs and kwargs['user_name'] is not None:
        credential_details['userName'] = kwargs['user_name']
        kwargs.pop('user_name')

    if 'password_secret_id' in kwargs and kwargs['password_secret_id'] is not None:
        credential_details['passwordSecretId'] = kwargs['password_secret_id']
        kwargs.pop('password_secret_id')

    if len(credential_details) > 0:
        kwargs['credential_details'] = json.dumps(credential_details)

    ctx.invoke(database_cli.enable_pluggable_database_management, **kwargs)


# Expanding complex parameter credential_details for modify_pluggable_database_management
@cli_util.copy_params_from_generated_command(database_cli.modify_pluggable_database_management, params_to_exclude=['credential_details'])
@database_cli.pluggable_database_group.command(name='modify-pluggable-database-management', help=u"""Updates one or more attributes of the Database Management service for the pluggable database.""")
@cli_util.option('--user-name', help=u"""The name of the Oracle Database user that will be used to connect to the database.""")
@cli_util.option('--password-secret-id', help=u"""The OCID of the Oracle Cloud Infrastructure secret.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def modify_pluggable_database_management_extended(ctx, **kwargs):
    credential_details = {}
    if 'user_name' in kwargs and kwargs['user_name'] is not None:
        credential_details['userName'] = kwargs['user_name']

    if 'password_secret_id' in kwargs and kwargs['password_secret_id'] is not None:
        credential_details['passwordSecretId'] = kwargs['password_secret_id']

    if len(credential_details) > 0:
        kwargs['credential_details'] = json.dumps(credential_details)
    kwargs.pop('user_name')
    kwargs.pop('password_secret_id')
    ctx.invoke(database_cli.modify_pluggable_database_management, **kwargs)


# renaming db-system-storage-performance command group to storage-performance
cli_util.rename_command(database_cli, database_cli.db_root_group, database_cli.db_system_storage_performance_group, "storage-performance")
# renaming db-system-compute-performance command group to compute-performance
cli_util.rename_command(database_cli, database_cli.db_root_group, database_cli.db_system_compute_performance_group, "compute-performance")


# CLI-341
@cli_util.copy_params_from_generated_command(database_cli.failover_data_guard_association, params_to_exclude=[''])
@database_cli.data_guard_association_group.command(name=database_cli.failover_data_guard_association.name, help=database_cli.failover_data_guard_association.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DataGuardAssociation'})
@cli_util.wrap_exceptions
def failover_data_guard_association_extended(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_id, data_guard_association_id, database_admin_password, if_match):

    if isinstance(database_id, six.string_types) and len(database_id.strip()) == 0:
        raise click.UsageError('Parameter --database-id cannot be whitespace or empty string')

    if isinstance(data_guard_association_id, six.string_types) and len(data_guard_association_id.strip()) == 0:
        raise click.UsageError('Parameter --data-guard-association-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}
    _details['databaseAdminPassword'] = database_admin_password

    client = cli_util.build_client('database', 'database', ctx)
    result = client.failover_data_guard_association(
        database_id=database_id,
        data_guard_association_id=data_guard_association_id,
        failover_data_guard_association_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_data_guard_association') and callable(getattr(client, 'get_data_guard_association')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_guard_association(database_id, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@cli_util.copy_params_from_generated_command(database_cli.reinstate_data_guard_association, params_to_exclude=[''])
@database_cli.data_guard_association_group.command(name=database_cli.reinstate_data_guard_association.name, help=database_cli.reinstate_data_guard_association.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DataGuardAssociation'})
@cli_util.wrap_exceptions
def reinstate_data_guard_association_extended(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_id, data_guard_association_id, database_admin_password, if_match):

    if isinstance(database_id, six.string_types) and len(database_id.strip()) == 0:
        raise click.UsageError('Parameter --database-id cannot be whitespace or empty string')

    if isinstance(data_guard_association_id, six.string_types) and len(data_guard_association_id.strip()) == 0:
        raise click.UsageError('Parameter --data-guard-association-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}
    _details['databaseAdminPassword'] = database_admin_password

    client = cli_util.build_client('database', 'database', ctx)
    result = client.reinstate_data_guard_association(
        database_id=database_id,
        data_guard_association_id=data_guard_association_id,
        reinstate_data_guard_association_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_data_guard_association') and callable(getattr(client, 'get_data_guard_association')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_guard_association(database_id, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@cli_util.copy_params_from_generated_command(database_cli.switchover_data_guard_association, params_to_exclude=[''])
@database_cli.data_guard_association_group.command(name=database_cli.switchover_data_guard_association.name, help=database_cli.switchover_data_guard_association.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DataGuardAssociation'})
@cli_util.wrap_exceptions
def switchover_data_guard_association_extended(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_id, data_guard_association_id, database_admin_password, if_match):

    if isinstance(database_id, six.string_types) and len(database_id.strip()) == 0:
        raise click.UsageError('Parameter --database-id cannot be whitespace or empty string')

    if isinstance(data_guard_association_id, six.string_types) and len(data_guard_association_id.strip()) == 0:
        raise click.UsageError('Parameter --data-guard-association-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}
    _details['databaseAdminPassword'] = database_admin_password

    client = cli_util.build_client('database', 'database', ctx)
    result = client.switchover_data_guard_association(
        database_id=database_id,
        data_guard_association_id=data_guard_association_id,
        switchover_data_guard_association_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_data_guard_association') and callable(getattr(client, 'get_data_guard_association')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_guard_association(database_id, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@cli_util.copy_params_from_generated_command(database_cli.update_data_guard_association, params_to_exclude=[''])
@database_cli.data_guard_association_group.command(name=database_cli.update_data_guard_association.name, help=database_cli.update_data_guard_association.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DataGuardAssociation'})
@cli_util.wrap_exceptions
def update_data_guard_association(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_id, data_guard_association_id, database_admin_password, protection_mode, transport_type, is_active_data_guard_enabled, if_match):

    if isinstance(database_id, six.string_types) and len(database_id.strip()) == 0:
        raise click.UsageError('Parameter --database-id cannot be whitespace or empty string')

    if isinstance(data_guard_association_id, six.string_types) and len(data_guard_association_id.strip()) == 0:
        raise click.UsageError('Parameter --data-guard-association-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if database_admin_password is not None:
        _details['databaseAdminPassword'] = database_admin_password

    if protection_mode is not None:
        _details['protectionMode'] = protection_mode

    if transport_type is not None:
        _details['transportType'] = transport_type

    if is_active_data_guard_enabled is not None:
        _details['isActiveDataGuardEnabled'] = is_active_data_guard_enabled

    client = cli_util.build_client('database', 'database', ctx)
    result = client.update_data_guard_association(
        database_id=database_id,
        data_guard_association_id=data_guard_association_id,
        update_data_guard_association_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_data_guard_association') and callable(getattr(client, 'get_data_guard_association')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_guard_association(database_id, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@cli_util.copy_params_from_generated_command(database_cli.delete_autonomous_database, params_to_exclude=[''])
@database_cli.autonomous_database_group.command(name=database_cli.delete_autonomous_database.name, help=database_cli.delete_autonomous_database.help)
@click.pass_context
@cli_util.wrap_exceptions
def delete_autonomous_database_extended(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, autonomous_database_id, if_match):

    if isinstance(autonomous_database_id, six.string_types) and len(autonomous_database_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-database-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', 'database', ctx)
    result = client.delete_autonomous_database(
        autonomous_database_id=autonomous_database_id,
        **kwargs
    )
    work_request_client = cli_util.build_client('work_requests', 'work_request', ctx)
    if wait_for_state:

        if hasattr(work_request_client, 'get_work_request') and callable(getattr(work_request_client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(work_request_client, work_request_client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


# oci db autonomous-database list-autonomous-database-refreshable-clones -> oci db autonomous-database list-refreshable-clones
cli_util.rename_command(database_cli, database_cli.autonomous_database_group, database_cli.list_autonomous_database_refreshable_clones, "list-refreshable-clones")


# DEX-16751 Add custom help text for data collection options
@cli_util.copy_params_from_generated_command(database_cli.create_vm_cluster, params_to_exclude=['data_collection_options'])
@database_cli.vm_cluster_group.command('create', help=database_cli.create_vm_cluster.help)
@cli_util.option('--data-collection-options', type=custom_types.CLI_COMPLEX_TYPE, help=DATA_COLLECTION_OPTIONS_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}, 'db-servers': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'data-collection-options': {'module': 'database', 'class': 'DataCollectionOptions'}}, output_type={'module': 'database', 'class': 'VmCluster'})
@cli_util.wrap_exceptions
def create_vm_cluster_extended(ctx, **kwargs):

    ctx.invoke(database_cli.create_vm_cluster, **kwargs)
