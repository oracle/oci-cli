# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import sys
import click
import json
import oci

from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli_database.generated import database_cli
from oci_cli.aliasing import CommandGroupWithAlias

# Rename some commands and groups
cli_util.rename_command(database_cli.db_root_group, database_cli.db_node_group, "node")
cli_util.rename_command(database_cli.db_root_group, database_cli.db_system_group, "system")
cli_util.rename_command(database_cli.db_root_group, database_cli.db_system_shape_group, "system-shape")
cli_util.rename_command(database_cli.db_root_group, database_cli.db_version_group, "version")
cli_util.rename_command(database_cli.db_root_group, database_cli.patch_history_entry_group, "patch-history")

database_cli.patch_group.commands.pop("get-db-system")
database_cli.patch_group.commands.pop("list-db-system")
database_cli.patch_history_entry_group.commands.pop("get-db-system")
database_cli.patch_history_entry_group.commands.pop("list-db-system")

database_cli.get_db_system_patch.name = "by-db-system"
database_cli.get_db_system_patch_history_entry.name = "by-db-system"
database_cli.list_db_system_patches.name = "by-db-system"
database_cli.list_db_system_patch_history_entries.name = "by-db-system"

cli_util.rename_command(database_cli.autonomous_database_group, database_cli.generate_autonomous_database_wallet, "generate-wallet")
cli_util.rename_command(database_cli.autonomous_data_warehouse_group, database_cli.generate_autonomous_data_warehouse_wallet, "generate-wallet")

database_cli.autonomous_database_group.commands.pop(database_cli.create_autonomous_database.name)
cli_util.rename_command(database_cli.autonomous_database_group, database_cli.create_autonomous_database_create_autonomous_database_clone_details, "create-from-clone")
cli_util.rename_command(database_cli.autonomous_database_group, database_cli.create_autonomous_database_create_autonomous_database_details, "create")


@cli_util.copy_params_from_generated_command(database_cli.launch_db_system_launch_db_system_details, params_to_exclude=['db_home', 'ssh_public_keys'])
@database_cli.db_system_group.command(name='launch', help=database_cli.launch_db_system_launch_db_system_details.help)
@cli_util.option('--admin-password', required=True, help="""A strong password for SYS, SYSTEM, and PDB Admin. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, #, or -.""")
@cli_util.option('--character-set', help="""The character set for the database. The default is AL32UTF8. Allowed values are: AL32UTF8, AR8ADOS710, AR8ADOS720, AR8APTEC715, AR8ARABICMACS, AR8ASMO8X, AR8ISO8859P6, AR8MSWIN1256, AR8MUSSAD768, AR8NAFITHA711, AR8NAFITHA721, AR8SAKHR706, AR8SAKHR707, AZ8ISO8859P9E, BG8MSWIN, BG8PC437S, BLT8CP921, BLT8ISO8859P13, BLT8MSWIN1257, BLT8PC775, BN8BSCII, CDN8PC863, CEL8ISO8859P14, CL8ISO8859P5, CL8ISOIR111, CL8KOI8R, CL8KOI8U, CL8MACCYRILLICS, CL8MSWIN1251, EE8ISO8859P2, EE8MACCES, EE8MACCROATIANS, EE8MSWIN1250, EE8PC852, EL8DEC, EL8ISO8859P7, EL8MACGREEKS, EL8MSWIN1253, EL8PC437S, EL8PC851, EL8PC869, ET8MSWIN923, HU8ABMOD, HU8CWI2, IN8ISCII, IS8PC861, IW8ISO8859P8, IW8MACHEBREWS, IW8MSWIN1255, IW8PC1507, JA16EUC, JA16EUCTILDE, JA16SJIS, JA16SJISTILDE, JA16VMS, KO16KSC5601, KO16KSCCS, KO16MSWIN949, LA8ISO6937, LA8PASSPORT, LT8MSWIN921, LT8PC772, LT8PC774, LV8PC1117, LV8PC8LR, LV8RST104090, N8PC865, NE8ISO8859P10, NEE8ISO8859P4, RU8BESTA, RU8PC855, RU8PC866, SE8ISO8859P3, TH8MACTHAIS, TH8TISASCII, TR8DEC, TR8MACTURKISHS, TR8MSWIN1254, TR8PC857, US7ASCII, US8PC437, UTF8, VN8MSWIN1258, VN8VN3, WE8DEC, WE8DG, WE8ISO8859P1, WE8ISO8859P15, WE8ISO8859P9, WE8MACROMAN8S, WE8MSWIN1252, WE8NCR4970, WE8NEXTSTEP, WE8PC850, WE8PC858, WE8PC860, WE8ROMAN8, ZHS16CGB231280, ZHS16GBK, ZHT16BIG5, ZHT16CCDC, ZHT16DBT, ZHT16HKSCS, ZHT16MSWIN950, ZHT32EUC, ZHT32SOPS, ZHT32TRIS.""")
@cli_util.option('--db-name', required=True, help="""The database name. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted.""")
@cli_util.option('--db-version', required=True, help="""A valid Oracle database version. To get a list of supported versions, use the command 'oci db version list'.""")
@cli_util.option('--db-workload', help="""Database workload type. Allowed values are: OLTP, DSS""")
@cli_util.option('--ncharacter-set', help="""National character set for the database. The default is AL16UTF16. Allowed values are: AL16UTF16 or UTF8.""")
@cli_util.option('--pdb-name', help="""Pluggable database name. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted. Pluggable database should not be same as database name.""")
@cli_util.option('--ssh-authorized-keys-file', required=True, type=click.File('r'), help="""A file containing one or more public SSH keys to use for SSH access to the DB System. Use a newline character to separate multiple keys. The length of the combined keys cannot exceed 10,000 characters.""")
@cli_util.option('--auto-backup-enabled', type=click.BOOL, help="""If set to true, schedules backups automatically. Default is false.""")
@cli_util.option('--recovery-window-in-days', type=click.IntRange(1, 60), help="""The number of days between the current and the earliest point of recoverability covered by automatic backups (1 to 60).""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fault-domains': {'module': 'database', 'class': 'list[string]'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}}, output_type={'module': 'database', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def launch_db_system_extended(ctx, **kwargs):
    create_db_home_details = {}
    if 'db_version' in kwargs and kwargs['db_version']:
        create_db_home_details['dbVersion'] = kwargs['db_version']

    create_database_details = {}
    if 'admin_password' in kwargs and kwargs['admin_password']:
        create_database_details['adminPassword'] = kwargs['admin_password']

    if 'character_set' in kwargs and kwargs['character_set']:
        create_database_details['characterSet'] = kwargs['character_set']

    if 'db_name' in kwargs and kwargs['db_name']:
        create_database_details['dbName'] = kwargs['db_name']

    if 'db_workload' in kwargs and kwargs['db_workload']:
        create_database_details['dbWorkload'] = kwargs['db_workload']

    if 'ncharacter_set' in kwargs and kwargs['ncharacter_set']:
        create_database_details['ncharacterSet'] = kwargs['ncharacter_set']

    if 'pdb_name' in kwargs and kwargs['pdb_name']:
        create_database_details['pdbName'] = kwargs['pdb_name']

    if kwargs['auto_backup_enabled'] is not None or kwargs['recovery_window_in_days'] is not None:
        db_backup_config = {}
        if kwargs['auto_backup_enabled'] is not None:
            db_backup_config['autoBackupEnabled'] = kwargs['auto_backup_enabled']
        if kwargs['recovery_window_in_days'] is not None:
            db_backup_config['recoveryWindowInDays'] = kwargs['recovery_window_in_days']
        create_database_details['db_backup_config'] = json.dumps(db_backup_config)
    create_db_home_details['database'] = create_database_details

    kwargs['db_home'] = json.dumps(create_db_home_details)

    if 'ssh_authorized_keys_file' in kwargs and kwargs['ssh_authorized_keys_file']:
        content = [line.rstrip('\n') for line in kwargs['ssh_authorized_keys_file']]
        kwargs['ssh_public_keys'] = json.dumps(content)

    # remove all of the kwargs that launch_db_system wont recognize
    del kwargs['admin_password']
    del kwargs['character_set']
    del kwargs['db_name']
    del kwargs['db_version']
    del kwargs['db_workload']
    del kwargs['ncharacter_set']
    del kwargs['pdb_name']
    del kwargs['ssh_authorized_keys_file']
    del kwargs['auto_backup_enabled']
    del kwargs['recovery_window_in_days']

    ctx.invoke(database_cli.launch_db_system_launch_db_system_details, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.launch_db_system_launch_db_system_from_backup_details, params_to_exclude=['db_home', 'ssh_public_keys'])
@database_cli.db_system_group.command(name='launch-from-backup', help=database_cli.launch_db_system_launch_db_system_from_backup_details.help)
@cli_util.option('--admin-password', required=True, help="""A strong password for SYS, SYSTEM, and PDB Admin. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, #, or -.""")
@cli_util.option('--backup-id', required=True, help="""The backup OCID.""")
@cli_util.option('--backup-tde-password', required=True, help="""The password to open the TDE wallet.""")
@cli_util.option('--ssh-authorized-keys-file', required=True, type=click.File('r'), help="""A file containing one or more public SSH keys to use for SSH access to the DB System. Use a newline character to separate multiple keys. The length of the combined keys cannot exceed 10,000 characters.""")
@cli_util.option('--db-name', required=False, help="""The display name of the database to be created from the backup. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}}, output_type={'module': 'database', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def launch_db_system_backup_extended(ctx, **kwargs):

    create_database_details = {}

    if 'admin_password' in kwargs and kwargs['admin_password']:
        create_database_details['adminPassword'] = kwargs['admin_password']

    if 'backup_id' in kwargs and kwargs['backup_id']:
        create_database_details['backupId'] = kwargs['backup_id']

    if 'backup_tde_password' in kwargs and kwargs['backup_tde_password']:
        create_database_details['backupTDEPassword'] = kwargs['backup_tde_password']

    if 'db_name' in kwargs and kwargs['db_name']:
        create_database_details['dbName'] = kwargs['db_name']

    create_db_home_details = {}
    create_db_home_details['database'] = create_database_details

    kwargs['db_home'] = json.dumps(create_db_home_details)

    if 'ssh_authorized_keys_file' in kwargs and kwargs['ssh_authorized_keys_file']:
        content = [line.rstrip('\n') for line in kwargs['ssh_authorized_keys_file']]
        kwargs['ssh_public_keys'] = json.dumps(content)

    # remove all of the kwargs that launch_db_system wont recognize
    del kwargs['admin_password']
    del kwargs['backup_id']
    del kwargs['backup_tde_password']
    del kwargs['ssh_authorized_keys_file']
    del kwargs['db_name']

    ctx.invoke(database_cli.launch_db_system_launch_db_system_from_backup_details, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.create_db_home, params_to_exclude=['database', 'display_name', 'db_version'])
@database_cli.database_group.command(name='create', help="""Creates a new database in the given DB System.""")
@cli_util.option('--admin-password', required=True, help="""A strong password for SYS, SYSTEM, and PDB Admin. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, #, or -.""")
@cli_util.option('--character-set', help="""The character set for the database. The default is AL32UTF8. Allowed values are: AL32UTF8, AR8ADOS710, AR8ADOS720, AR8APTEC715, AR8ARABICMACS, AR8ASMO8X, AR8ISO8859P6, AR8MSWIN1256, AR8MUSSAD768, AR8NAFITHA711, AR8NAFITHA721, AR8SAKHR706, AR8SAKHR707, AZ8ISO8859P9E, BG8MSWIN, BG8PC437S, BLT8CP921, BLT8ISO8859P13, BLT8MSWIN1257, BLT8PC775, BN8BSCII, CDN8PC863, CEL8ISO8859P14, CL8ISO8859P5, CL8ISOIR111, CL8KOI8R, CL8KOI8U, CL8MACCYRILLICS, CL8MSWIN1251, EE8ISO8859P2, EE8MACCES, EE8MACCROATIANS, EE8MSWIN1250, EE8PC852, EL8DEC, EL8ISO8859P7, EL8MACGREEKS, EL8MSWIN1253, EL8PC437S, EL8PC851, EL8PC869, ET8MSWIN923, HU8ABMOD, HU8CWI2, IN8ISCII, IS8PC861, IW8ISO8859P8, IW8MACHEBREWS, IW8MSWIN1255, IW8PC1507, JA16EUC, JA16EUCTILDE, JA16SJIS, JA16SJISTILDE, JA16VMS, KO16KSC5601, KO16KSCCS, KO16MSWIN949, LA8ISO6937, LA8PASSPORT, LT8MSWIN921, LT8PC772, LT8PC774, LV8PC1117, LV8PC8LR, LV8RST104090, N8PC865, NE8ISO8859P10, NEE8ISO8859P4, RU8BESTA, RU8PC855, RU8PC866, SE8ISO8859P3, TH8MACTHAIS, TH8TISASCII, TR8DEC, TR8MACTURKISHS, TR8MSWIN1254, TR8PC857, US7ASCII, US8PC437, UTF8, VN8MSWIN1258, VN8VN3, WE8DEC, WE8DG, WE8ISO8859P1, WE8ISO8859P15, WE8ISO8859P9, WE8MACROMAN8S, WE8MSWIN1252, WE8NCR4970, WE8NEXTSTEP, WE8PC850, WE8PC858, WE8PC860, WE8ROMAN8, ZHS16CGB231280, ZHS16GBK, ZHT16BIG5, ZHT16CCDC, ZHT16DBT, ZHT16HKSCS, ZHT16MSWIN950, ZHT32EUC, ZHT32SOPS, ZHT32TRIS.""")
@cli_util.option('--db-name', required=True, help="""The database name. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted.""")
@cli_util.option('--db-workload', help="""Database workload type. Allowed values are: OLTP, DSS""")
@cli_util.option('--ncharacter-set', help="""National character set for the database. The default is AL16UTF16. Allowed values are: AL16UTF16 or UTF8.""")
@cli_util.option('--pdb-name', help="""Pluggable database name. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted. Pluggable database should not be same as database name.""")
@cli_util.option('--db-version', required=True, help="""A valid Oracle database version. To get a list of supported versions, use the command 'oci db version list'.""")
@cli_util.option('--auto-backup-enabled', type=click.BOOL, help="""If set to true, schedules backups automatically. Default is false.""")
@cli_util.option('--recovery-window-in-days', type=click.IntRange(1, 60), help="""The number of days between the current and the earliest point of recoverability covered by automatic backups (1 to 60).""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DatabaseSummary'})
@cli_util.wrap_exceptions
def create_database(ctx, **kwargs):
    create_db_home_with_system_details = oci.database.models.CreateDbHomeWithDbSystemIdDetails()

    create_database_details = oci.database.models.CreateDatabaseDetails()
    if 'admin_password' in kwargs and kwargs['admin_password']:
        create_database_details.admin_password = kwargs['admin_password']

    if 'character_set' in kwargs and kwargs['character_set']:
        create_database_details.character_set = kwargs['character_set']

    if 'db_name' in kwargs and kwargs['db_name']:
        create_database_details.db_name = kwargs['db_name']

    if 'db_workload' in kwargs and kwargs['db_workload']:
        create_database_details.db_workload = kwargs['db_workload']

    if 'ncharacter_set' in kwargs and kwargs['ncharacter_set']:
        create_database_details.ncharacter_set = kwargs['ncharacter_set']

    if 'pdb_name' in kwargs and kwargs['pdb_name']:
        create_database_details.pdb_name = kwargs['pdb_name']

    if kwargs['auto_backup_enabled'] is not None or kwargs['recovery_window_in_days'] is not None:
        db_backup_config = oci.database.models.DbBackupConfig()
        if kwargs['auto_backup_enabled'] is not None:
            db_backup_config.auto_backup_enabled = kwargs['auto_backup_enabled']
        if kwargs['recovery_window_in_days'] is not None:
            db_backup_config.recoveryWindowInDays = kwargs['recovery_window_in_days']
        create_database_details.db_backup_config = db_backup_config
    del kwargs['auto_backup_enabled']
    del kwargs['recovery_window_in_days']
    create_db_home_with_system_details.database = create_database_details

    if 'db_system_id' in kwargs and kwargs['db_system_id']:
        create_db_home_with_system_details.db_system_id = kwargs['db_system_id']

    if 'db_version' in kwargs and kwargs['db_version']:
        create_db_home_with_system_details.db_version = kwargs['db_version']

    client = cli_util.build_client('database', ctx)

    result = client.create_db_home(create_db_home_with_system_details)

    db_home_id = result.data.id
    compartment_id = result.data.compartment_id

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
@cli_util.option('--admin-password', required=True, help="""A strong password for SYS, SYSTEM, and PDB Admin. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, #, or -.""")
@cli_util.option('--backup-id', required=True, help="""The backup OCID.""")
@cli_util.option('--backup-tde-password', required=True, help="""The password to open the TDE wallet.""")
@cli_util.option('--db-name', required=False, help="""The display name of the database to be created from the backup. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DatabaseSummary'})
@cli_util.wrap_exceptions
def create_database_from_backup(ctx, **kwargs):
    create_db_home_with_system_details = oci.database.models.CreateDbHomeWithDbSystemIdFromBackupDetails()
    create_database_details = oci.database.models.CreateDatabaseFromBackupDetails()
    if 'admin_password' in kwargs and kwargs['admin_password']:
        create_database_details.admin_password = kwargs['admin_password']

    if 'backup_id' in kwargs and kwargs['backup_id']:
        create_database_details.backup_id = kwargs['backup_id']

    if 'backup_tde_password' in kwargs and kwargs['backup_tde_password']:
        create_database_details.backup_tde_password = kwargs['backup_tde_password']

    if 'db_name' in kwargs and kwargs['db_name']:
        create_database_details.db_name = kwargs['db_name']

    create_db_home_with_system_details.database = create_database_details

    if 'db_system_id' in kwargs and kwargs['db_system_id']:
        create_db_home_with_system_details.db_system_id = kwargs['db_system_id']

    create_db_home_with_system_details.source = 'DB_BACKUP'

    client = cli_util.build_client('database', ctx)

    result = client.create_db_home(create_db_home_with_system_details)

    db_home_id = result.data.id
    compartment_id = result.data.compartment_id

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


@cli_util.copy_params_from_generated_command(database_cli.update_database, params_to_exclude=['db_backup_config'])
@database_cli.database_group.command(name='update', help="""Update a Database based on the request parameters you provide.""")
@cli_util.option('--auto-backup-enabled', type=click.BOOL, help="""If set to true, schedules backups automatically. Default is false.""")
@cli_util.option('--recovery-window-in-days', type=click.IntRange(1, 60), help="""The number of days between the current and the earliest point of recoverability covered by automatic backups (1 to 60).""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}}, output_type={'module': 'database', 'class': 'Database'})
@cli_util.wrap_exceptions
def update_database_extended(ctx, **kwargs):
    if kwargs['auto_backup_enabled'] is not None or kwargs['recovery_window_in_days'] is not None:
        db_backup_config = {}
        if kwargs['auto_backup_enabled'] is not None:
            db_backup_config['autoBackupEnabled'] = kwargs['auto_backup_enabled']
        if kwargs['recovery_window_in_days'] is not None:
            db_backup_config['recoveryWindowInDays'] = kwargs['recovery_window_in_days']
        kwargs['db_backup_config'] = json.dumps(db_backup_config)

    del kwargs['auto_backup_enabled']
    del kwargs['recovery_window_in_days']

    ctx.invoke(database_cli.update_database, **kwargs)


@database_cli.database_group.command(name='patch', help="""Perform a patch action for a given patch and database.""")
@cli_util.option('--database-id', required=True, help="""The OCID of the database.""")
@cli_util.option('--patch-action', required=True, help="""The action to perform on the patch.""")
@cli_util.option('--patch-id', required=True, help="""The OCID of the patch.""")
@click.pass_context
@json_skeleton_utils.get_cli_json_input_option({})
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'Database'})
@cli_util.help_option
@cli_util.wrap_exceptions
def patch_database(ctx, **kwargs):
    client = cli_util.build_client('database', ctx)

    response = client.get_database(kwargs['database_id'])
    db_home_id = response.data.db_home_id

    patch_details = oci.database.models.PatchDetails()
    patch_details.action = kwargs['patch_action']
    patch_details.patch_id = kwargs['patch_id']

    update_db_home_details = oci.database.models.UpdateDbHomeDetails()
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
    client = cli_util.build_client('database', ctx)

    # get the db-home for this database
    response = client.get_database(kwargs['database_id'])
    db_home_id = response.data.db_home_id
    compartment_id = response.data.compartment_id

    # we only want to delete this single database, but the only API
    # available deletes the entire db-home, so check to make sure
    # this is the only database in the db-home before deleting
    response = client.get_db_home(db_home_id)
    response = client.list_databases(compartment_id, db_home_id)
    if len(response.data) != 1:
        click.echo(message="Cannot delete a DB Home which contains multiple databases through the CLI. Please use the console to delete this database.", file=sys.stderr)
        sys.exit(1)

    # delete DbHome
    response = client.delete_db_home(db_home_id)
    cli_util.render_response(response, ctx)


@cli_util.copy_params_from_generated_command(database_cli.list_db_homes, params_to_exclude=['db_home_id', 'page', 'all_pages', 'page_size'])
@database_cli.database_group.command(name='list', help="""Lists all databases in a given DB System.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[DatabaseSummary]'})
@cli_util.wrap_exceptions
def list_databases(ctx, **kwargs):
    client = cli_util.build_client('database', ctx)

    response = client.get_db_system(kwargs['db_system_id'])
    compartment_id = response.data.compartment_id

    response = client.list_db_homes(compartment_id, kwargs['db_system_id'])
    db_homes = response.data
    while response.has_next_page:
        response = client.list_db_homes(compartment_id, kwargs['db_system_id'])

        if response.data is not None:
            db_homes += response.data

    # go through all db_homes and list all dbs
    databases = []
    for db_home in db_homes:
        if 'limit' in kwargs and kwargs['limit'] is not None and len(databases) >= int(kwargs['limit']):
            break

        response = client.list_databases(compartment_id, db_home.id)
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


@cli_util.copy_params_from_generated_command(database_cli.update_db_system, params_to_exclude=['ssh_public_keys', 'version'])
@database_cli.db_system_group.command(name='update', help=database_cli.update_db_system.help)
@cli_util.option('--patch-action', help="""The action to perform on the patch.""")
@cli_util.option('--patch-id', help="""The OCID of the patch.""")
@cli_util.option('--ssh-authorized-keys-file', type=click.File('r'), help="""A file containing one or more public SSH keys to use for SSH access to the DB System. Use a newline character to separate multiple keys. The length of the combined keys cannot exceed 10,000 characters.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}}, output_type={'module': 'database', 'class': 'DbSystem'})
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
        kwargs['version'] = {
            "action": patch_action,
            "patchId": patch_id
        }

    # remove kwargs that update_db_system wont recognize
    del kwargs['ssh_authorized_keys_file']
    del kwargs['patch_action']
    del kwargs['patch_id']

    ctx.invoke(database_cli.update_db_system, **kwargs)


@database_cli.db_system_group.command(name='patch', help="""Perform an action on a Patch for a DB System.""")
@cli_util.option('--db-system-id', required=True, help="""The OCID of the DB System.""")
@cli_util.option('--patch-action', required=True, help="""The action to perform on the patch.""")
@cli_util.option('--patch-id', required=True, help="""The OCID of the patch.""")
@click.pass_context
@cli_util.help_option
@json_skeleton_utils.get_cli_json_input_option({})
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def patch_db_system(ctx, **kwargs):
    client = cli_util.build_client('database', ctx)

    patch_details = oci.database.models.PatchDetails()
    patch_details.action = kwargs['patch_action']
    patch_details.patch_id = kwargs['patch_id']

    update_db_system_details = oci.database.models.UpdateDbSystemDetails()
    update_db_system_details.db_version = patch_details

    result = client.update_db_system(kwargs['db_system_id'], update_db_system_details)
    db_system = result.data

    cli_util.render(db_system, None, ctx)


@database_cli.data_guard_association_group.command(name=cli_util.override('create_data_guard_association.command_name', 'create'), cls=CommandGroupWithAlias, help="""Creates a new Data Guard association.  A Data Guard association represents the replication relationship between the specified database and a peer database. For more information, see [Using Oracle Data Guard].

All Oracle Cloud Infrastructure resources, including Data Guard associations, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. Fore more information, see [Resource Identifiers].""")
@cli_util.help_option_group
def create_data_guard_association_group():
    pass


@cli_util.copy_params_from_generated_command(database_cli.create_data_guard_association, params_to_exclude=['wait_for_state', 'max_wait_seconds', 'wait_interval_seconds'])
@create_data_guard_association_group.command('from-existing-db-system', help="""Creates a new Data Guard association using an existing DB System.  A Data Guard association represents the replication relationship between the specified database and a peer database. For more information, see [Using Oracle Data Guard].

All Oracle Cloud Infrastructue resources, including Data Guard associations, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. Fore more information, see [Resource Identifiers].""")
@cli_util.option('--peer-db-system-id', required=True, help="""The OCID of the DB System to create the standby database on.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DataGuardAssociation'})
@cli_util.wrap_exceptions
def create_data_guard_association_from_existing_db_system(ctx, from_json, database_id, creation_type, database_admin_password, protection_mode, transport_type, peer_db_system_id):
    kwargs = {}

    details = {}
    details['creationType'] = creation_type
    details['databaseAdminPassword'] = database_admin_password
    details['protectionMode'] = protection_mode
    details['transportType'] = transport_type
    details['peerDbSystemId'] = peer_db_system_id

    client = cli_util.build_client('database', ctx)
    result = client.create_data_guard_association(
        database_id=database_id,
        create_data_guard_association_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cli_util.copy_params_from_generated_command(database_cli.create_data_guard_association, params_to_exclude=['wait_for_state', 'max_wait_seconds', 'wait_interval_seconds'])
@create_data_guard_association_group.command('with-new-db-system', help="""Creates a new Data Guard association with a new DB System.  A Data Guard association represents the replication relationship between the specified database and a peer database. For more information, see [Using Oracle Data Guard].


All Oracle Cloud Infrastructue resources, including Data Guard associations, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. Fore more information, see [Resource Identifiers].""")
@cli_util.option('--display-name', required=True, help="""The user-friendly name for the DB System to create the standby database on. It does not have to be unique.""")
@cli_util.option('--hostname', required=True, help="""The host name for the DB Node.""")
@cli_util.option('--availability-domain', required=True, help="""The name of the Availability Domain that the standby database DB System will be located in.""")
@cli_util.option('--subnet-id', required=True, help="""The OCID of the subnet the DB System is associated with. **Subnet Restrictions:** - For 1- and 2-node RAC DB Systems, do not use a subnet that overlaps with 192.168.16.16/28

These subnets are used by the Oracle Clusterware private interconnect on the database instance. Specifying an overlapping subnet will cause the private interconnect to malfunction. This restriction applies to both the client subnet and backup subnet.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DataGuardAssociation'})
@cli_util.wrap_exceptions
def create_data_guard_association_with_new_db_system(ctx, from_json, database_id, creation_type, database_admin_password, protection_mode, transport_type, availability_domain, display_name, hostname, subnet_id):
    kwargs = {}

    details = {}
    details['creationType'] = creation_type
    details['databaseAdminPassword'] = database_admin_password
    details['protectionMode'] = protection_mode
    details['transportType'] = transport_type

    if availability_domain is not None:
        details['availabilityDomain'] = availability_domain
    if display_name is not None:
        details['displayName'] = display_name
    if hostname is not None:
        details['hostname'] = hostname
    if subnet_id is not None:
        details['subnetId'] = subnet_id
    details['creationType'] = 'NewDbSystem'

    client = cli_util.build_client('database', ctx)
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
    client = cli_util.build_client('database', ctx)

    # get the db-home for this database
    response = client.get_database(kwargs['database_id'])
    kwargs['db_home_id'] = response.data.db_home_id

    del kwargs['database_id']

    ctx.invoke(database_cli.get_db_home_patch, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.list_db_home_patches, params_to_exclude=['db_home_id'])
@patch_list_group.command('by-database', help="""List patches for a given database""")
@cli_util.option('--database-id', required=True, help="""The database [OCID].""")
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[PatchSummary]'})
@cli_util.wrap_exceptions
def list_patch_by_database(ctx, **kwargs):
    client = cli_util.build_client('database', ctx)

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
    client = cli_util.build_client('database', ctx)

    # get the db-home for this database
    response = client.get_database(kwargs['database_id'])
    kwargs['db_home_id'] = response.data.db_home_id

    del kwargs['database_id']

    ctx.invoke(database_cli.get_db_home_patch_history_entry, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.list_db_home_patch_history_entries, params_to_exclude=['db_home_id'])
@patch_history_list_group.command('by-database', help="""List patch history entries for a given database""")
@cli_util.option('--database-id', required=True, help="""The database [OCID].""")
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[PatchHistoryEntrySummary]'})
@cli_util.wrap_exceptions
def list_patch_history_entries_by_database(ctx, **kwargs):
    client = cli_util.build_client('database', ctx)

    # get the db-home for this database
    response = client.get_database(kwargs['database_id'])
    kwargs['db_home_id'] = response.data.db_home_id

    del kwargs['database_id']

    ctx.invoke(database_cli.list_db_home_patch_history_entries, **kwargs)


database_cli.db_root_group.commands.pop(database_cli.db_home_group.name)

database_cli.database_group.commands.pop(database_cli.list_databases.name)
database_cli.db_node_group.commands.pop(database_cli.db_node_action.name)
database_cli.db_system_group.commands.pop(database_cli.launch_db_system.name)

# Disable subclass commands
database_cli.db_system_group.commands.pop(database_cli.launch_db_system_launch_db_system_details.name)
database_cli.db_system_group.commands.pop(database_cli.launch_db_system_launch_db_system_from_backup_details.name)

database_cli.db_system_group.commands.pop(database_cli.update_db_system.name)

# Disable subclass command
database_cli.data_guard_association_group.commands.pop(database_cli.create_data_guard_association_create_data_guard_association_to_existing_db_system_details.name)
database_cli.data_guard_association_group.commands.pop(database_cli.create_data_guard_association_create_data_guard_association_with_new_db_system_details.name)

# we need to expose customized create / delete / list database commands in order to avoid exposing DbHomes
database_cli.database_group.add_command(create_database)
database_cli.database_group.add_command(create_database_from_backup)
database_cli.database_group.add_command(delete_database)
database_cli.database_group.add_command(list_databases)
database_cli.db_system_group.add_command(launch_db_system_extended)
database_cli.db_system_group.add_command(launch_db_system_backup_extended)
database_cli.db_system_group.add_command(update_db_system_extended)

database_cli.patch_group.commands.pop(database_cli.get_db_home_patch.name)
database_cli.patch_group.commands.pop(database_cli.list_db_home_patches.name)

patch_get_group.add_command(database_cli.get_db_system_patch)
patch_list_group.add_command(database_cli.list_db_system_patches)

database_cli.patch_history_entry_group.commands.pop(database_cli.get_db_home_patch_history_entry.name)
database_cli.patch_history_entry_group.commands.pop(database_cli.list_db_home_patch_history_entries.name)

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
