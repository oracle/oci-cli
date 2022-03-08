# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click  # noqa: F401
import json  # noqa: F401
from services.database_migration.src.oci_cli_database_migration.generated import databasemigration_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401
from oci_cli import cli_exceptions

databasemigration_cli.database_migration_root_group.short_help = "Oracle Database Migration Service"

# oci database-migration agent-image-summary -> oci database-migration agent-image
cli_util.rename_command(databasemigration_cli, databasemigration_cli.database_migration_root_group, databasemigration_cli.agent_image_summary_group, "agent-image")


# oci database-migration agent-image-summary list-agent-images -> oci database-migration agent-image-summary list
cli_util.rename_command(databasemigration_cli, databasemigration_cli.agent_image_summary_group, databasemigration_cli.list_agent_images, "list")


# oci database-migration agent-summary list-agents -> oci database-migration agent-summary list
cli_util.rename_command(databasemigration_cli, databasemigration_cli.agent_summary_group, databasemigration_cli.list_agents, "list")


# oci database-migration connection-summary list-connections -> oci database-migration connection-summary list
cli_util.rename_command(databasemigration_cli, databasemigration_cli.connection_summary_group, databasemigration_cli.list_connections, "list")


# oci database-migration job evaluate-migration -> oci database-migration job evaluate
cli_util.rename_command(databasemigration_cli, databasemigration_cli.job_group, databasemigration_cli.evaluate_migration, "evaluate")


# oci database-migration job start-migration -> oci database-migration job start
cli_util.rename_command(databasemigration_cli, databasemigration_cli.job_group, databasemigration_cli.start_migration, "start")


# oci database-migration job-output-summary -> oci database-migration job-output
cli_util.rename_command(databasemigration_cli, databasemigration_cli.database_migration_root_group, databasemigration_cli.job_output_summary_group, "job-output")


# oci database-migration job-output-summary list-job-outputs -> oci database-migration job-output-summary list
cli_util.rename_command(databasemigration_cli, databasemigration_cli.job_output_summary_group, databasemigration_cli.list_job_outputs, "list")


# oci database-migration job-summary list-jobs -> oci database-migration job-summary list
cli_util.rename_command(databasemigration_cli, databasemigration_cli.job_summary_group, databasemigration_cli.list_jobs, "list")


# oci database-migration migration-summary list-migrations -> oci database-migration migration-summary list
cli_util.rename_command(databasemigration_cli, databasemigration_cli.migration_summary_group, databasemigration_cli.list_migrations, "list")


# oci database-migration work-request-log-entry -> oci database-migration work-request-logs
cli_util.rename_command(databasemigration_cli, databasemigration_cli.database_migration_root_group, databasemigration_cli.work_request_log_entry_group, "work-request-logs")


# oci database-migration work-request-log-entry list-work-request-logs -> oci database-migration work-request-log-entry list
cli_util.rename_command(databasemigration_cli, databasemigration_cli.work_request_log_entry_group, databasemigration_cli.list_work_request_logs, "list")


# oci database-migration work-request-summary list-work-requests -> oci database-migration work-request-summary list
cli_util.rename_command(databasemigration_cli, databasemigration_cli.work_request_summary_group, databasemigration_cli.list_work_requests, "list")


# oci database-migration job evaluate-migration -> oci database-migration migration
databasemigration_cli.job_group.commands.pop(databasemigration_cli.evaluate_migration.name)
databasemigration_cli.migration_group.add_command(databasemigration_cli.evaluate_migration)


# oci database-migration job start-migration -> oci database-migration migration
databasemigration_cli.job_group.commands.pop(databasemigration_cli.start_migration.name)
databasemigration_cli.migration_group.add_command(databasemigration_cli.start_migration)


# oci database-migration agent-summary list-agents -> oci database-migration agent
databasemigration_cli.agent_summary_group.commands.pop(databasemigration_cli.list_agents.name)
databasemigration_cli.agent_group.add_command(databasemigration_cli.list_agents)


# oci database-migration connection-summary list-connections -> oci database-migration connection
databasemigration_cli.connection_summary_group.commands.pop(databasemigration_cli.list_connections.name)
databasemigration_cli.connection_group.add_command(databasemigration_cli.list_connections)


# oci database-migration job-summary list-jobs -> oci database-migration job
databasemigration_cli.job_summary_group.commands.pop(databasemigration_cli.list_jobs.name)
databasemigration_cli.job_group.add_command(databasemigration_cli.list_jobs)


# oci database-migration migration-summary list-migrations -> oci database-migration migration
databasemigration_cli.migration_summary_group.commands.pop(databasemigration_cli.list_migrations.name)
databasemigration_cli.migration_group.add_command(databasemigration_cli.list_migrations)


# oci database-migration work-request-summary list-work-requests -> oci database-migration work-request
databasemigration_cli.work_request_summary_group.commands.pop(databasemigration_cli.list_work_requests.name)
databasemigration_cli.work_request_group.add_command(databasemigration_cli.list_work_requests)

# remove groups previously renamed
databasemigration_cli.database_migration_root_group.commands.pop(databasemigration_cli.agent_summary_group.name)
databasemigration_cli.database_migration_root_group.commands.pop(databasemigration_cli.connection_summary_group.name)
databasemigration_cli.database_migration_root_group.commands.pop(databasemigration_cli.job_summary_group.name)
databasemigration_cli.database_migration_root_group.commands.pop(databasemigration_cli.migration_summary_group.name)
databasemigration_cli.database_migration_root_group.commands.pop(databasemigration_cli.work_request_summary_group.name)


@cli_util.copy_params_from_generated_command(databasemigration_cli.update_agent, params_to_exclude=['version_parameterconflict'])
@databasemigration_cli.agent_group.command(name=databasemigration_cli.update_agent.name, help=databasemigration_cli.update_agent.help)
@cli_util.option('--agent-version', help=u"""ODMS Agent version""")
@cli_util.option('--public-key-file', type=click.File('r'), help=u"""ODMS Agent public key file path.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'database_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database_migration', 'class': 'Agent'})
@cli_util.wrap_exceptions
def update_agent_extended(ctx, **kwargs):
    if 'agent_version' in kwargs:
        kwargs['version_parameterconflict'] = kwargs['agent_version']
        kwargs.pop('agent_version')

    if kwargs.get('public_key') and kwargs.get('public_key_file'):
        raise cli_exceptions.RequiredValueNotInDefaultOrUserInputError('Cannot specify both --public-key or --public-key-file.')

    key_file = kwargs.get('public_key_file')
    if key_file:
        kwargs['public_key'] = key_file.read()

    kwargs.pop('public_key_file')

    ctx.invoke(databasemigration_cli.update_agent, **kwargs)


# oci database-migration connection create --tls-keystore-file --tls-wallet-file  --ssh-details.sshkeyFile
@cli_util.copy_params_from_generated_command(databasemigration_cli.create_connection, params_to_exclude=['manual_database_sub_type'])
@databasemigration_cli.connection_group.command(name='create', help=databasemigration_cli.create_connection.help)
@cli_util.option('--db-subtype', type=custom_types.CliCaseInsensitiveChoice(["ORACLE", "RDS_ORACLE"]), help="""Database manual connection subtype. This value can only be specified for manual connections.""")
@cli_util.option('--tls-wallet-file', type=click.File('r'), help=u"""cwallet.sso fle path containing containing the TCPS/SSL certificate; base64 encoded String. Not required for source container database connections.""")
@cli_util.option('--tls-keystore-file', type=click.File('r'), help=u"""keystore.jks file path; base64 encoded String content. Requires a TLS wallet to be specified. Not required for source container database connections.""")
@cli_util.option('--sshkey-file', type=click.File('r'), help=u""" Private ssh key file.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'connect-descriptor': {'module': 'database_migration', 'class': 'CreateConnectDescriptor'}, 'ssh-details': {'module': 'database_migration', 'class': 'CreateSshDetails'}, 'admin-credentials': {'module': 'database_migration', 'class': 'CreateAdminCredentials'}, 'private-endpoint': {'module': 'database_migration', 'class': 'CreatePrivateEndpoint'}, 'vault-details': {'module': 'database_migration', 'class': 'CreateVaultDetails'}, 'freeform-tags': {'module': 'database_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database_migration', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection(ctx, **kwargs):

    if 'db_subtype' in kwargs:
        kwargs['manual_database_sub_type'] = kwargs['db_subtype']
        kwargs.pop('db_subtype')

    # read --sshkey-file into ssh_details['sshkey']
    if 'sshkey_file' in kwargs and kwargs['sshkey_file'] is not None:
        ssh_details = {}
        if 'ssh_details' in kwargs and kwargs['ssh_details'] is not None:
            if ssh_details.get('sshkey') and ssh_details['sshkey'] is not None:
                raise cli_exceptions.RequiredValueNotInDefaultOrUserInputError('Cannot specify both --sshkey-file and sshDetails.sshkey.')
            ssh_details = kwargs['ssh_details']
        sshkey_file = kwargs.get('sshkey_file')
        if sshkey_file:
            ssh_details['sshkey'] = sshkey_file.read()
            kwargs['ssh_details'] = json.dumps(ssh_details)
    kwargs.pop('sshkey_file')

    # create_connection read --tls-wallet using --tls-wallet-file
    if kwargs.get('tls_wallet') and kwargs.get('tls_wallet_file'):
        raise cli_exceptions.RequiredValueNotInDefaultOrUserInputError('Cannot specify both --tls-wallet and --tls-wallet-file.')

    tls_wallet_file = kwargs.get('tls_wallet_file')
    if tls_wallet_file:
        kwargs['tls_wallet'] = tls_wallet_file.read()

    kwargs.pop('tls_wallet_file')

    # create_connection read --tls-keystore using --tls-keystore-file
    if kwargs.get('tls_keystore') and kwargs.get('tls_keystore_file'):
        raise cli_exceptions.RequiredValueNotInDefaultOrUserInputError('Cannot specify both --tls-keystore or --tls-keystore-file.')

    tls_keystore_file = kwargs.get('tls_keystore_file')
    if tls_keystore_file:
        kwargs['tls_keystore'] = tls_keystore_file.read()

    kwargs.pop('tls_keystore_file')

    ctx.invoke(databasemigration_cli.create_connection, **kwargs)


# oci database-migration connection update --tls-keystore-file --tls-wallet-file  --ssh-details.sshkeyFile
@cli_util.copy_params_from_generated_command(databasemigration_cli.update_connection, params_to_exclude=[])
@databasemigration_cli.connection_group.command(name='update', help=databasemigration_cli.update_connection.help)
@cli_util.option('--tls-wallet-file', type=click.File('r'), help=u"""cwallet.sso file path containing containing the TCPS/SSL certificate; base64 encoded String. Not required for source container database connections.""")
@cli_util.option('--tls-keystore-file', type=click.File('r'), help=u"""keystore.jks file path; base64 encoded String contents. Requires a TLS wallet to be specified. Not required for source container database connections.""")
@cli_util.option('--sshkey-file', type=click.File('r'), help=u""" Private ssh key file.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'connect-descriptor': {'module': 'database_migration', 'class': 'UpdateConnectDescriptor'}, 'ssh-details': {'module': 'database_migration', 'class': 'UpdateSshDetails'}, 'admin-credentials': {'module': 'database_migration', 'class': 'UpdateAdminCredentials'}, 'private-endpoint': {'module': 'database_migration', 'class': 'UpdatePrivateEndpoint'}, 'vault-details': {'module': 'database_migration', 'class': 'UpdateVaultDetails'}, 'freeform-tags': {'module': 'database_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_connection(ctx, **kwargs):
    # read --sshkey-file into ssh_details['sshkey']
    if 'sshkey_file' in kwargs and kwargs['sshkey_file'] is not None:
        ssh_details = {}
        if 'ssh_details' in kwargs and kwargs['ssh_details'] is not None:
            if ssh_details.get('sshkey') and ssh_details['sshkey'] is not None:
                raise cli_exceptions.RequiredValueNotInDefaultOrUserInputError('Cannot specify both --sshkey-file and sshDetails.sshkey.')
            ssh_details = kwargs['ssh_details']
        sshkey_file = kwargs.get('sshkey_file')
        if sshkey_file:
            ssh_details['sshkey'] = sshkey_file.read()
            kwargs['ssh_details'] = json.dumps(ssh_details)
    kwargs.pop('sshkey_file')

    # update_connection read --tls-wallet using --tls-wallet-file
    if kwargs.get('tls_wallet') and kwargs.get('tls_wallet_file'):
        raise cli_exceptions.RequiredValueNotInDefaultOrUserInputError('Cannot specify both --tls-wallet or --tls-wallet-file.')

    tls_wallet_file = kwargs.get('tls_wallet_file')
    if tls_wallet_file:
        kwargs['tls_wallet'] = tls_wallet_file.read()

    kwargs.pop('tls_wallet_file')

    # update_connection read --tls-keystore using --tls-keystore-file
    if kwargs.get('tls_keystore') and kwargs.get('tls_keystore_file'):
        raise cli_exceptions.RequiredValueNotInDefaultOrUserInputError('Cannot specify both --tls-keystore or --tls-keystore-file.')

    tls_keystore_file = kwargs.get('tls_keystore_file')
    if tls_keystore_file:
        kwargs['tls_keystore'] = tls_keystore_file.read()

    kwargs.pop('tls_keystore_file')

    ctx.invoke(databasemigration_cli.update_connection, **kwargs)


# oci database-migration migration-object-type-summary list-migration-object-types -> oci database-migration migration-object-type-summary list
cli_util.rename_command(databasemigration_cli, databasemigration_cli.migration_object_type_summary_group, databasemigration_cli.list_migration_object_types, "list")

# oci database-migration excluded-object-summary list-excluded-objects -> oci database-migration excluded-object-summary list
cli_util.rename_command(databasemigration_cli, databasemigration_cli.excluded_object_summary_group, databasemigration_cli.list_excluded_objects, "list")


# oci database-migration migration-object-collection list-migration-objects -> oci database-migration migration-object-collection list
cli_util.rename_command(databasemigration_cli, databasemigration_cli.migration_object_collection_group, databasemigration_cli.list_migration_objects, "list")


# oci database-migration migration-object-collection -> oci database-migration migration-objects
cli_util.rename_command(databasemigration_cli, databasemigration_cli.database_migration_root_group, databasemigration_cli.migration_object_collection_group, "migration-objects")
