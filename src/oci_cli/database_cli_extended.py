# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

import sys
import click
import json
import oci

from . import cli_util
from . import json_skeleton_utils
from .generated import database_cli


@cli_util.copy_params_from_generated_command(database_cli.create_db_home, params_to_exclude=['database', 'display_name', 'db_version'])
@database_cli.database_group.command(name='create', help="""Creates a new database in the given DB System.""")
@click.option('--admin-password', help="""A strong password for SYS, SYSTEM, and PDB Admin. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, #, or -. [required]""")
@click.option('--character-set', required=False, help="""The character set for the database. The default is AL32UTF8. Allowed values are: AL32UTF8, AR8ADOS710, AR8ADOS720, AR8APTEC715, AR8ARABICMACS, AR8ASMO8X, AR8ISO8859P6, AR8MSWIN1256, AR8MUSSAD768, AR8NAFITHA711, AR8NAFITHA721, AR8SAKHR706, AR8SAKHR707, AZ8ISO8859P9E, BG8MSWIN, BG8PC437S, BLT8CP921, BLT8ISO8859P13, BLT8MSWIN1257, BLT8PC775, BN8BSCII, CDN8PC863, CEL8ISO8859P14, CL8ISO8859P5, CL8ISOIR111, CL8KOI8R, CL8KOI8U, CL8MACCYRILLICS, CL8MSWIN1251, EE8ISO8859P2, EE8MACCES, EE8MACCROATIANS, EE8MSWIN1250, EE8PC852, EL8DEC, EL8ISO8859P7, EL8MACGREEKS, EL8MSWIN1253, EL8PC437S, EL8PC851, EL8PC869, ET8MSWIN923, HU8ABMOD, HU8CWI2, IN8ISCII, IS8PC861, IW8ISO8859P8, IW8MACHEBREWS, IW8MSWIN1255, IW8PC1507, JA16EUC, JA16EUCTILDE, JA16SJIS, JA16SJISTILDE, JA16VMS, KO16KSCCS, KO16MSWIN949, LA8ISO6937, LA8PASSPORT, LT8MSWIN921, LT8PC772, LT8PC774, LV8PC1117, LV8PC8LR, LV8RST104090, N8PC865, NE8ISO8859P10, NEE8ISO8859P4, RU8BESTA, RU8PC855, RU8PC866, SE8ISO8859P3, TH8MACTHAIS, TH8TISASCII, TR8DEC, TR8MACTURKISHS, TR8MSWIN1254, TR8PC857, US7ASCII, US8PC437, UTF8, VN8MSWIN1258, VN8VN3, WE8DEC, WE8DG, WE8ISO8859P15, WE8ISO8859P9, WE8MACROMAN8S, WE8MSWIN1252, WE8NCR4970, WE8NEXTSTEP, WE8PC850, WE8PC858, WE8PC860, WE8ROMAN8, ZHS16CGB231280, ZHS16GBK, ZHT16BIG5, ZHT16CCDC, ZHT16DBT, ZHT16HKSCS, ZHT16MSWIN950, ZHT32EUC, ZHT32SOPS, ZHT32TRIS.""")
@click.option('--db-name', help="""The database name. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted. [required]""")
@click.option('--db-workload', required=False, help="""Database workload type. Allowed values are: OLTP, DSS""")
@click.option('--ncharacter-set', required=False, help="""National character set for the database. The default is AL16UTF16. Allowed values are: AL16UTF16 or UTF8.""")
@click.option('--pdb-name', required=False, help="""Pluggable database name. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted. Pluggable database should not be same as database name.""")
@click.option('--db-version', help="""A valid Oracle database version. To get a list of supported versions, use the command 'oci db version list'. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DatabaseSummary'})
@cli_util.wrap_exceptions
def create_database(ctx, **kwargs):
    if kwargs.get('generate_param_json_input') and kwargs.get('generate_full_command_json_input'):
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if kwargs.get('generate_full_command_json_input'):
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif kwargs.get('generate_param_json_input'):
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, kwargs.get('generate_param_json_input'))

    cli_util.load_context_obj_values_from_defaults(ctx)
    kwargs['admin_password'] = cli_util.coalesce_provided_and_default_value(ctx, 'admin-password', kwargs.get('admin_password'), True)
    kwargs['character_set'] = cli_util.coalesce_provided_and_default_value(ctx, 'character-set', kwargs.get('character_set'), False)
    kwargs['db_name'] = cli_util.coalesce_provided_and_default_value(ctx, 'db-name', kwargs.get('db_name'), True)
    kwargs['db_workload'] = cli_util.coalesce_provided_and_default_value(ctx, 'db-workload', kwargs.get('db_workload'), False)
    kwargs['ncharacter_set'] = cli_util.coalesce_provided_and_default_value(ctx, 'ncharacter-set', kwargs.get('ncharacter_set'), False)
    kwargs['pdb_name'] = cli_util.coalesce_provided_and_default_value(ctx, 'pdb-name', kwargs.get('pdb_name'), False)
    kwargs['db_version'] = cli_util.coalesce_provided_and_default_value(ctx, 'db-version', kwargs.get('db_version'), True)

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
    result = client.list_databases(compartment_id, db_home_id)

    # there is only one database per db-home (confirm?)
    # so just return the first database in this newly created db-home
    database = result.data[0]

    cli_util.render(database, None, ctx)


@database_cli.database_group.command(name='delete', help="""Deletes a database.""")
@click.option('--database-id', required=True, help="""The OCID of the database to delete.""")
@cli_util.confirm_delete_option
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_database(ctx, **kwargs):
    if kwargs.get('generate_param_json_input') and kwargs.get('generate_full_command_json_input'):
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if kwargs.get('generate_full_command_json_input'):
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif kwargs.get('generate_param_json_input'):
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, kwargs.get('generate_param_json_input'))

    cli_util.load_context_obj_values_from_defaults(ctx)
    kwargs['database_id'] = cli_util.coalesce_provided_and_default_value(ctx, 'database-id', kwargs.get('database_id'), True)

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


@cli_util.copy_params_from_generated_command(database_cli.list_db_homes, params_to_exclude=['db_home_id', 'page'])
@database_cli.database_group.command(name='list', help="""Lists all databases in a given DB System.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[DatabaseSummary]'})
@cli_util.wrap_exceptions
def list_databases(ctx, **kwargs):
    if kwargs.get('generate_param_json_input') and kwargs.get('generate_full_command_json_input'):
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if kwargs.get('generate_full_command_json_input'):
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif kwargs.get('generate_param_json_input'):
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, kwargs.get('generate_param_json_input'))

    cli_util.load_context_obj_values_from_defaults(ctx)
    kwargs['compartment_id'] = cli_util.coalesce_provided_and_default_value(ctx, 'compartment-id', kwargs.get('compartment_id'), True)
    kwargs['limit'] = cli_util.coalesce_provided_and_default_value(ctx, 'limit', kwargs.get('limit'), False)

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
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DbNode'})
@cli_util.wrap_exceptions
def db_node_start(ctx, **kwargs):
    if kwargs.get('generate_param_json_input') and kwargs.get('generate_full_command_json_input'):
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if kwargs.get('generate_full_command_json_input'):
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif kwargs.get('generate_param_json_input'):
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, kwargs.get('generate_param_json_input'))

    json_skeleton_utils.remove_json_skeleton_params_from_dict(kwargs)

    cli_util.load_context_obj_values_from_defaults(ctx)
    kwargs['db_node_id'] = cli_util.coalesce_provided_and_default_value(ctx, 'db-node-id', kwargs.get('db_node_id'), True)

    kwargs['action'] = 'start'
    ctx.invoke(database_cli.db_node_action, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.db_node_action, params_to_exclude=['action'])
@database_cli.db_node_group.command(name='stop', help="""Powers off the specified DB node.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DbNode'})
@cli_util.wrap_exceptions
def db_node_stop(ctx, **kwargs):
    if kwargs.get('generate_param_json_input') and kwargs.get('generate_full_command_json_input'):
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if kwargs.get('generate_full_command_json_input'):
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif kwargs.get('generate_param_json_input'):
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, kwargs.get('generate_param_json_input'))

    json_skeleton_utils.remove_json_skeleton_params_from_dict(kwargs)

    cli_util.load_context_obj_values_from_defaults(ctx)
    kwargs['db_node_id'] = cli_util.coalesce_provided_and_default_value(ctx, 'db-node-id', kwargs.get('db_node_id'), True)

    kwargs['action'] = 'stop'
    ctx.invoke(database_cli.db_node_action, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.db_node_action, params_to_exclude=['action'])
@database_cli.db_node_group.command(name='soft-reset', help="""Performs an ACPI shutdown and powers on the specified DB node.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DbNode'})
@cli_util.wrap_exceptions
def db_node_softreset(ctx, **kwargs):
    if kwargs.get('generate_param_json_input') and kwargs.get('generate_full_command_json_input'):
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if kwargs.get('generate_full_command_json_input'):
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif kwargs.get('generate_param_json_input'):
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, kwargs.get('generate_param_json_input'))

    json_skeleton_utils.remove_json_skeleton_params_from_dict(kwargs)

    cli_util.load_context_obj_values_from_defaults(ctx)
    kwargs['db_node_id'] = cli_util.coalesce_provided_and_default_value(ctx, 'db-node-id', kwargs.get('db_node_id'), True)

    kwargs['action'] = 'softreset'
    ctx.invoke(database_cli.db_node_action, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.db_node_action, params_to_exclude=['action'])
@database_cli.db_node_group.command(name='reset', help="""Powers off and powers on the specified DB node.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DbNode'})
@cli_util.wrap_exceptions
def db_node_reset(ctx, **kwargs):
    if kwargs.get('generate_param_json_input') and kwargs.get('generate_full_command_json_input'):
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if kwargs.get('generate_full_command_json_input'):
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif kwargs.get('generate_param_json_input'):
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, kwargs.get('generate_param_json_input'))

    json_skeleton_utils.remove_json_skeleton_params_from_dict(kwargs)

    cli_util.load_context_obj_values_from_defaults(ctx)
    kwargs['db_node_id'] = cli_util.coalesce_provided_and_default_value(ctx, 'db-node-id', kwargs.get('db_node_id'), True)

    kwargs['action'] = 'reset'
    ctx.invoke(database_cli.db_node_action, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.launch_db_system, params_to_exclude=['db_home', 'ssh_public_keys'])
@database_cli.db_system_group.command(name='launch', help=database_cli.launch_db_system.help)
@click.option('--admin-password', help="""A strong password for SYS, SYSTEM, and PDB Admin. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, #, or -. [required]""")
@click.option('--character-set', required=False, help="""The character set for the database. The default is AL32UTF8. Allowed values are: AL32UTF8, AR8ADOS710, AR8ADOS720, AR8APTEC715, AR8ARABICMACS, AR8ASMO8X, AR8ISO8859P6, AR8MSWIN1256, AR8MUSSAD768, AR8NAFITHA711, AR8NAFITHA721, AR8SAKHR706, AR8SAKHR707, AZ8ISO8859P9E, BG8MSWIN, BG8PC437S, BLT8CP921, BLT8ISO8859P13, BLT8MSWIN1257, BLT8PC775, BN8BSCII, CDN8PC863, CEL8ISO8859P14, CL8ISO8859P5, CL8ISOIR111, CL8KOI8R, CL8KOI8U, CL8MACCYRILLICS, CL8MSWIN1251, EE8ISO8859P2, EE8MACCES, EE8MACCROATIANS, EE8MSWIN1250, EE8PC852, EL8DEC, EL8ISO8859P7, EL8MACGREEKS, EL8MSWIN1253, EL8PC437S, EL8PC851, EL8PC869, ET8MSWIN923, HU8ABMOD, HU8CWI2, IN8ISCII, IS8PC861, IW8ISO8859P8, IW8MACHEBREWS, IW8MSWIN1255, IW8PC1507, JA16EUC, JA16EUCTILDE, JA16SJIS, JA16SJISTILDE, JA16VMS, KO16KSCCS, KO16MSWIN949, LA8ISO6937, LA8PASSPORT, LT8MSWIN921, LT8PC772, LT8PC774, LV8PC1117, LV8PC8LR, LV8RST104090, N8PC865, NE8ISO8859P10, NEE8ISO8859P4, RU8BESTA, RU8PC855, RU8PC866, SE8ISO8859P3, TH8MACTHAIS, TH8TISASCII, TR8DEC, TR8MACTURKISHS, TR8MSWIN1254, TR8PC857, US7ASCII, US8PC437, UTF8, VN8MSWIN1258, VN8VN3, WE8DEC, WE8DG, WE8ISO8859P15, WE8ISO8859P9, WE8MACROMAN8S, WE8MSWIN1252, WE8NCR4970, WE8NEXTSTEP, WE8PC850, WE8PC858, WE8PC860, WE8ROMAN8, ZHS16CGB231280, ZHS16GBK, ZHT16BIG5, ZHT16CCDC, ZHT16DBT, ZHT16HKSCS, ZHT16MSWIN950, ZHT32EUC, ZHT32SOPS, ZHT32TRIS.""")
@click.option('--db-name', help="""The database name. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted. [required]""")
@click.option('--db-version', help="""A valid Oracle database version. To get a list of supported versions, use the command 'oci db version list'. [required]""")
@click.option('--db-workload', required=False, help="""Database workload type. Allowed values are: OLTP, DSS""")
@click.option('--ncharacter-set', required=False, help="""National character set for the database. The default is AL16UTF16. Allowed values are: AL16UTF16 or UTF8.""")
@click.option('--pdb-name', required=False, help="""Pluggable database name. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted. Pluggable database should not be same as database name.""")
@click.option('--ssh-authorized-keys-file', type=click.File('r'), help="""A file containing one or more public SSH keys to use for SSH access to the DB System. Use a newline character to separate multiple keys. The length of the combined keys cannot exceed 10,000 characters. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def launch_db_system_extended(ctx, **kwargs):
    if kwargs.get('generate_param_json_input') and kwargs.get('generate_full_command_json_input'):
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if kwargs.get('generate_full_command_json_input'):
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif kwargs.get('generate_param_json_input'):
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, kwargs.get('generate_param_json_input'))

    json_skeleton_utils.remove_json_skeleton_params_from_dict(kwargs)

    cli_util.load_context_obj_values_from_defaults(ctx)
    kwargs['availability_domain'] = cli_util.coalesce_provided_and_default_value(ctx, 'availability-domain', kwargs.get('availability_domain'), True)
    kwargs['compartment_id'] = cli_util.coalesce_provided_and_default_value(ctx, 'compartment-id', kwargs.get('compartment_id'), True)
    kwargs['cpu_core_count'] = cli_util.coalesce_provided_and_default_value(ctx, 'cpu-core-count', kwargs.get('cpu_core_count'), True)
    kwargs['database_edition'] = cli_util.coalesce_provided_and_default_value(ctx, 'database-edition', kwargs.get('database_edition'), True)
    kwargs['hostname'] = cli_util.coalesce_provided_and_default_value(ctx, 'hostname', kwargs.get('hostname'), True)
    kwargs['shape'] = cli_util.coalesce_provided_and_default_value(ctx, 'shape', kwargs.get('shape'), True)
    kwargs['subnet_id'] = cli_util.coalesce_provided_and_default_value(ctx, 'subnet-id', kwargs.get('subnet_id'), True)
    kwargs['backup_subnet_id'] = cli_util.coalesce_provided_and_default_value(ctx, 'backup-subnet-id', kwargs.get('backup_subnet_id'), False)
    kwargs['cluster_name'] = cli_util.coalesce_provided_and_default_value(ctx, 'cluster-name', kwargs.get('cluster_name'), False)
    kwargs['data_storage_percentage'] = cli_util.coalesce_provided_and_default_value(ctx, 'data-storage-percentage', kwargs.get('data_storage_percentage'), False)
    kwargs['disk_redundancy'] = cli_util.coalesce_provided_and_default_value(ctx, 'disk-redundancy', kwargs.get('disk_redundancy'), False)
    kwargs['display_name'] = cli_util.coalesce_provided_and_default_value(ctx, 'display-name', kwargs.get('display_name'), False)
    kwargs['domain'] = cli_util.coalesce_provided_and_default_value(ctx, 'domain', kwargs.get('domain'), False)
    kwargs['admin_password'] = cli_util.coalesce_provided_and_default_value(ctx, 'admin-password', kwargs.get('admin_password'), True)
    kwargs['character_set'] = cli_util.coalesce_provided_and_default_value(ctx, 'character-set', kwargs.get('character_set'), False)
    kwargs['db_name'] = cli_util.coalesce_provided_and_default_value(ctx, 'db-name', kwargs.get('db_name'), True)
    kwargs['db_version'] = cli_util.coalesce_provided_and_default_value(ctx, 'db-version', kwargs.get('db_version'), True)
    kwargs['db_workload'] = cli_util.coalesce_provided_and_default_value(ctx, 'db-workload', kwargs.get('db_workload'), False)
    kwargs['ncharacter_set'] = cli_util.coalesce_provided_and_default_value(ctx, 'ncharacter-set', kwargs.get('ncharacter_set'), False)
    kwargs['pdb_name'] = cli_util.coalesce_provided_and_default_value(ctx, 'pdb-name', kwargs.get('pdb_name'), False)

    if not kwargs.get('ssh_authorized_keys_file'):
        file = cli_util.get_click_file_from_default_values_file(ctx, 'ssh-authorized-keys-file', 'r', False)
        if file:
            kwargs['ssh_authorized_keys_file'] = file

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

    ctx.invoke(database_cli.launch_db_system, **kwargs)


@cli_util.copy_params_from_generated_command(database_cli.update_db_system, params_to_exclude=['ssh_public_keys', 'version'])
@database_cli.db_system_group.command(name='update', help=database_cli.update_db_system.help)
@click.option('--ssh-authorized-keys-file', required=False, type=click.File('r'), help="""A file containing one or more public SSH keys to use for SSH access to the DB System. Use a newline character to separate multiple keys. The length of the combined keys cannot exceed 10,000 characters.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def update_db_system_extended(ctx, **kwargs):
    if kwargs.get('generate_param_json_input') and kwargs.get('generate_full_command_json_input'):
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if kwargs.get('generate_full_command_json_input'):
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif kwargs.get('generate_param_json_input'):
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, kwargs.get('generate_param_json_input'))

    json_skeleton_utils.remove_json_skeleton_params_from_dict(kwargs)

    cli_util.load_context_obj_values_from_defaults(ctx)
    if not kwargs.get('ssh_authorized_keys_file'):
        file = cli_util.get_click_file_from_default_values_file(ctx, 'ssh-authorized-keys-file', 'r', False)
        if file:
            kwargs['ssh_authorized_keys_file'] = file

    if 'ssh_authorized_keys_file' in kwargs and kwargs['ssh_authorized_keys_file']:
        content = [line.rstrip('\n') for line in kwargs['ssh_authorized_keys_file']]
        kwargs['ssh_public_keys'] = json.dumps(content)

    # remove kwargs that update_db_system wont recognize
    del kwargs['ssh_authorized_keys_file']

    ctx.invoke(database_cli.update_db_system, **kwargs)


@database_cli.data_guard_association_group.group(name=cli_util.override('create_data_guard_association.command_name', 'create'), help="""Creates a new Data Guard association.  A Data Guard association represents the replication relationship between the specified database and a peer database. For more information, see [Using Oracle Data Guard].

All Oracle Cloud Infrastructure resources, including Data Guard associations, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. Fore more information, see [Resource Identifiers].""")
@cli_util.help_option_group
def create_data_guard_association_group():
    pass


@cli_util.copy_params_from_generated_command(database_cli.create_data_guard_association, params_to_exclude=[''])
@create_data_guard_association_group.command('from-existing-db-system', help="""Creates a new Data Guard association using an existing DB System.  A Data Guard association represents the replication relationship between the specified database and a peer database. For more information, see [Using Oracle Data Guard].

All Oracle Cloud Infrastructue resources, including Data Guard associations, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. Fore more information, see [Resource Identifiers].""")
@click.option('--peer-db-system-id', help="""The OCID of the DB System to create the standby database on. [required]""")
@click.pass_context
@cli_util.wrap_exceptions
def create_data_guard_association_from_existing_db_system(ctx, generate_param_json_input, generate_full_command_json_input, from_json, database_id, creation_type, database_admin_password, protection_mode, transport_type, peer_db_system_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    database_id = cli_util.coalesce_provided_and_default_value(ctx, 'database-id', database_id, True)
    creation_type = cli_util.coalesce_provided_and_default_value(ctx, 'creation-type', creation_type, True)
    database_admin_password = cli_util.coalesce_provided_and_default_value(ctx, 'database-admin-password', database_admin_password, True)
    protection_mode = cli_util.coalesce_provided_and_default_value(ctx, 'protection-mode', protection_mode, True)
    transport_type = cli_util.coalesce_provided_and_default_value(ctx, 'transport-type', transport_type, True)
    peer_db_system_id = cli_util.coalesce_provided_and_default_value(ctx, 'peer-db-system-id', peer_db_system_id, True)

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


database_cli.db_group.add_command(database_cli.database_group)
database_cli.db_group.add_command(database_cli.db_node_group)
database_cli.db_group.add_command(database_cli.db_system_group)
database_cli.db_group.add_command(database_cli.db_system_shape_group)
database_cli.db_group.add_command(database_cli.db_version_group)

database_cli.database_group.commands.pop(database_cli.list_databases.name)
database_cli.db_node_group.commands.pop(database_cli.db_node_action.name)
database_cli.db_system_group.commands.pop(database_cli.launch_db_system.name)
database_cli.db_system_group.commands.pop(database_cli.update_db_system.name)
database_cli.db_group.add_command(database_cli.data_guard_association_group)

# we need to expose customized create / delete / list database commands in order to avoid exposing DbHomes
database_cli.database_group.add_command(create_database)
database_cli.database_group.add_command(delete_database)
database_cli.database_group.add_command(list_databases)
database_cli.db_system_group.add_command(launch_db_system_extended)
database_cli.db_system_group.add_command(update_db_system_extended)

cpu_core_count_help_override = """The number of CPU cores to enable. The valid values depend on the specified shape:

- BM.DenseIO1.36 and BM.HighIO1.36 - Specify a multiple of 2, from 2 to 36. - BM.RACLocalStorage1.72 - Specify a multiple of 4, from 4 to 72. - Exadata.Quarter1.84 - Specify a multiple of 2, from 22 to 84. - Exadata.Half1.168 - Specify a multiple of 4, from 44 to 168. - Exadata.Full1.336 - Specify a multiple of 8, from 88 to 336. [required]"""

cli_util.override_option_help(launch_db_system_extended, 'cpu_core_count', cpu_core_count_help_override)
