# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from services.mysql.src.oci_cli_db_system.generated import dbsystem_cli
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
import click

# rename  oci mysql db-system create-db-system-create-db-system-source-from-backup-details -> oci mysql db-system clone
cli_util.rename_command(dbsystem_cli, dbsystem_cli.db_system_group, dbsystem_cli.create_db_system_create_db_system_source_from_backup_details, "clone")

# rename  oci mysql db-system create-db-system-create-db-system-source-import-from-url-details -> oci mysql db-system import
cli_util.rename_command(dbsystem_cli, dbsystem_cli.db_system_group, dbsystem_cli.create_db_system_create_db_system_source_import_from_url_details, "import")

# oci mysql db-system db-system -> oci mysql db-system system
dbsystem_cli.db_system_root_group.commands.pop(dbsystem_cli.db_system_group.name)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.create_db_system)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.create_db_system_create_db_system_source_from_backup_details)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.create_db_system_create_db_system_source_import_from_url_details)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.delete_db_system)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.get_db_system)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.list_db_systems)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.restart_db_system)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.start_db_system)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.stop_db_system)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.update_db_system)


# rename --source-source-url argument
@cli_util.copy_params_from_generated_command(dbsystem_cli.create_db_system_create_db_system_source_import_from_url_details, params_to_exclude=['source_source_url'])
@cli_util.option('--source-url', required=True, help="""The Pre-Authenticated Request (PAR) URL of the file you want to import from Object Storage.""")
@dbsystem_cli.db_system_root_group.command(name="import", help=dbsystem_cli.create_db_system_create_db_system_source_import_from_url_details.help)
@json_skeleton_utils.get_cli_json_input_option({'backup-policy': {'module': 'mysql', 'class': 'CreateBackupPolicyDetails'}, 'maintenance': {'module': 'mysql', 'class': 'CreateMaintenanceDetails'}, 'freeform-tags': {'module': 'mysql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'mysql', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backup-policy': {'module': 'mysql', 'class': 'CreateBackupPolicyDetails'}, 'maintenance': {'module': 'mysql', 'class': 'CreateMaintenanceDetails'}, 'freeform-tags': {'module': 'mysql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'mysql', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'mysql', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def rename_create_import_args(ctx, **kwargs):
    if 'source_url' in kwargs:
        kwargs['source_source_url'] = kwargs['source_url']
        kwargs.pop('source_url')

    ctx.invoke(dbsystem_cli.create_db_system_create_db_system_source_import_from_url_details, **kwargs)
