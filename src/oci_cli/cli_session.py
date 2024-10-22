# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
from oci_cli.cli_root import cli
from oci_cli import cli_constants
from oci_cli import cli_setup
from oci_cli import cli_setup_bootstrap
from oci_cli import cli_util
from pathlib import Path

import click
import configparser
import json
import oci
import os
from oci._vendor import requests
import six
from shutil import copy, make_archive, rmtree
import sys
import tempfile
import zipfile
import datetime

CONFIG_KEY_FILE_SUFFIX = "_file"
TOKEN_FILE_SUFFIX = "_token"

ZIP_FILE_FORMAT = 'zip'


@cli.group('session', help="""Session commands for CLI""")
@cli_util.help_option_group
def session_group():
    pass


@session_group.command('authenticate', help="""Creates a CLI session using a browser based login flow. --region is a [required] argument""")
@click.option('--region', help=','.join(oci.regions.REGIONS))
@click.option('--tenancy-name', help='Name of the tenancy')
@click.option('--no-browser', is_flag=True, help="""Triggers user authentication without requiring interactive browser login""")
@cli_util.option('--public-key-file-path', type=click.Path(), help="""Full path of the public key PEM file that corresponds to the RSA key pair used for signing requests""")
@click.option('--session-expiration-in-minutes', default=cli_constants.OCI_CLI_UPST_TOKEN_MAX_TTL, help="""User session expiration in minutes to which the requested user principal session token (UPST) is bounded. Valid values are from 5 to 60 for all realms. If not provided, a default value of 60 minutes if set.""")
@cli_util.option('--token-location', default=cli_setup.DEFAULT_TOKEN_DIRECTORY, help=u"""Provide the directory where you would like to store token and private/public key. Default is ~/.oci/sessions""")
@click.option('--profile-name', help='Name of the profile you are creating')
@click.option('--config-location', help='Path to the config for the new session')
@click.option('--use-passphrase', is_flag=True, help='Provide a passphrase to be used to encrypt the private key from the generated key pair')
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def authenticate(ctx, region, tenancy_name, profile_name, config_location, use_passphrase, no_browser, public_key_file_path, session_expiration_in_minutes, token_location):
    region = ctx.obj['region']
    if region is None:
        region = cli_setup.prompt_for_region()
    persist_only_public_key = False
    if no_browser:
        if int(session_expiration_in_minutes) > int(cli_constants.OCI_CLI_UPST_TOKEN_MAX_TTL):
            click.echo("""Session expiration cannot be longer than 60 minutes""")
            sys.exit(1)

        if int(session_expiration_in_minutes) < int(cli_constants.OCI_CLI_UPST_TOKEN_MIN_TTL):
            click.echo("""Session expiration cannot be shorter than 5 minutes""")
            sys.exit(1)

        # check if user is able to access identity_data_plane
        client = cli_util.build_client('identity_data_plane', 'dataplane', ctx)

        token_path = os.path.normpath(os.path.expanduser(token_location))
        Path(token_path).mkdir(parents=True, exist_ok=True)

        # If public key is provided, use it
        if public_key_file_path:
            persist_only_public_key = True
            try:
                public_key = cli_util.get_public_key_from_file(public_key_file_path)
            except Exception as e:
                click.echo("""Could not load public key from public-key-file-path provided""")
                sys.exit(1)
            private_key = None

        # If public key is not provided, create a new private/public key pair
        else:
            private_key = cli_util.generate_key()
            public_key = private_key.public_key()

        fingerprint = cli_setup.public_key_to_fingerprint(public_key)
        public_key_serialized = cli_util.serialize_key(public_key=public_key).decode('UTF-8')

        # Call API
        kwargs = {'opc_request_id': cli_util.use_or_generate_request_id(ctx.obj['request_id'])}
        _details = {'publicKey': public_key_serialized, 'sessionExpirationInMinutes': session_expiration_in_minutes}
        result = client.generate_user_security_token(
            generate_user_security_token_details=_details,
            **kwargs
        )

        response = cli_util.to_dict(result.data)
        token = response['token']
        # get user / tenant info out of token
        security_token_container = oci.auth.security_token_container.SecurityTokenContainer(None, security_token=token)
        token_data = security_token_container.get_jwt()
        user_ocid = token_data['sub']
        tenancy_ocid = token_data['tenant']
        user_session = cli_setup_bootstrap.UserSession(user_ocid, tenancy_ocid, region, token, public_key, private_key, fingerprint)
    else:
        # create a user session through the browser login flow
        user_session = cli_setup_bootstrap.create_user_session(region, tenancy_name)

    # persist the session to a config (including the token value)
    profile, config = cli_setup_bootstrap.persist_user_session(user_session, profile_name=profile_name, config=config_location, use_passphrase=use_passphrase, persist_token=True, session_auth=True, persist_only_public_key=persist_only_public_key)

    click.echo('Config written to: {}'.format(config))

    click.echo("""
    Try out your newly created session credentials with the following example command:

    oci iam region list --config-file {config_file} --profile {profile} --auth {auth}
""".format(config_file=config, profile=profile, auth=cli_constants.OCI_CLI_AUTH_SESSION_TOKEN))


@session_group.command('validate', help="""Tests whether a CLI session is still valid""")
@cli_util.option('--local', is_flag=True, help='Only perform local validation of session by checking expiry time.')
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def validate(ctx, local):
    # manually set authentication mode to session so that we attempt to use the session token
    ctx.obj['auth'] = cli_constants.OCI_CLI_AUTH_SESSION_TOKEN

    client_config = cli_util.build_config(ctx.obj)
    profile_name = ctx.obj['profile']

    security_token_location = client_config.get('security_token_file')
    if not security_token_location:
        click.echo("ERROR: No security_token_file was found in config for profile: {}".format(profile_name), file=sys.stderr)
        sys.exit(1)

    if not os.path.exists(security_token_location):
        click.echo("ERROR: 'security_token_file' not found: {}".format(security_token_location), file=sys.stderr)
        sys.exit(1)

    with open(security_token_location, 'r') as security_token_file:
        token = security_token_file.read()

    security_token_container = oci.auth.security_token_container.SecurityTokenContainer(None, token)
    if local:
        if not security_token_container.valid():
            click.echo("Session has expired", file=sys.stderr)
            sys.exit(1)
    else:
        client = cli_util.build_client('identity', 'identity', ctx)
        try:
            client.list_regions()
        except oci.exceptions.ServiceError as service_error:
            if service_error.status == 401:
                click.echo("Session was deemed invalid by service", file=sys.stderr)
                sys.exit(1)
            else:
                raise service_error

    security_token_file = security_token_container.get_jwt()
    expiry_time = datetime.datetime.fromtimestamp(security_token_file['exp']).strftime("%Y-%m-%d %H:%M:%S")
    click.echo("Session is valid until " + expiry_time, file=sys.stderr)


@session_group.command('terminate', help="""Terminates a CLI session by removing the entry from the config and removing all referenced resources (e.g. keys)""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def terminate(ctx):
    client_config = cli_util.build_config(ctx.obj)

    token = client_config.get('security_token_file')
    if not token:
        click.echo("ERROR: Cannot terminate a profile that does not have a value for 'security_token_file'", file=sys.stderr)
        sys.exit(1)

    config_file = os.path.expanduser(ctx.obj['config_file'])
    profile_name_to_terminate = ctx.obj['profile']

    config = configparser.ConfigParser()
    config.read(config_file)
    current_profiles = [key for key, value in config.items()]

    if profile_name_to_terminate == 'DEFAULT':
        click.echo("ERROR: Cannot terminate DEFAULT profile", file=sys.stderr)
        sys.exit(1)

    if profile_name_to_terminate not in current_profiles:
        click.echo("ERROR: Profile does not exist", file=sys.stderr)
        sys.exit(1)

    cli_setup.remove_profile_from_config(config_file, profile_name_to_terminate)

    profile_to_terminate = os.path.join(cli_setup.DEFAULT_TOKEN_DIRECTORY, profile_name_to_terminate)

    if os.path.exists(profile_to_terminate):
        rmtree(os.path.abspath(profile_to_terminate))

    click.echo("Successfully removed profile: {} from config: {}".format(profile_name_to_terminate, config_file), file=sys.stderr)


@session_group.command('refresh', help="""Refreshes a CLI session""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def refresh(ctx):
    client_config = cli_util.build_config(ctx.obj)

    security_token_file = client_config.get('security_token_file')
    if not security_token_file:
        click.echo("ERROR: Cannot refresh a profile that does not have a value for 'security_token_file'", file=sys.stderr)
        sys.exit(1)

    expanded_security_token_location = os.path.expanduser(security_token_file)
    if not os.path.exists(expanded_security_token_location):
        click.echo("ERROR: Cannot refresh token, 'security_token_file' does not exist: {}".format(expanded_security_token_location))
        sys.exit(1)

    with open(expanded_security_token_location, 'r') as security_token_file:
        token = security_token_file.read()

    try:
        private_key = oci.signer.load_private_key_from_file(client_config.get('key_file'), client_config.get('pass_phrase'))
    except oci.exceptions.MissingPrivateKeyPassphrase:
        client_config['pass_phrase'] = cli_util.prompt_for_passphrase()
        private_key = oci.signer.load_private_key_from_file(client_config.get('key_file'), client_config.get('pass_phrase'))
    auth = oci.auth.signers.SecurityTokenSigner(token, private_key)

    refresh_url = "{endpoint}/v1/authentication/refresh".format(endpoint=oci.regions.endpoint_for("auth", client_config.get('region')))
    click.echo("Attempting to refresh token from {refresh_url}".format(refresh_url=refresh_url), file=sys.stderr)

    response = requests.post(
        refresh_url,
        headers={
            'content-type': 'application/json'
        },
        data=json.dumps({
            'currentToken': token
        }),
        auth=auth
    )

    if response.status_code == 200:
        refreshed_token = json.loads(response.content.decode('UTF-8'))['token']
        with open(expanded_security_token_location, 'w') as security_token_file:
            security_token_file.write(refreshed_token)
        cli_util.apply_user_only_access_permissions(expanded_security_token_location)
        click.echo("Successfully refreshed token", file=sys.stderr)
    elif response.status_code == 401:
        click.echo("Your session is no longer valid and cannot be refreshed. Please use 'oci session authenticate' to create a new session.", file=sys.stderr)
        sys.exit(1)
    else:
        click.echo("ERROR: Failed to refresh sesison. Error: {}".format(str(response.content.decode('UTF-8'))))
        sys.exit(1)


@session_group.command('export', help="""Exports a CLI session into a zip that can be imported.
The session exported is the active profile (specified either by defaults or the --config-file / --profile arguments.""")
@cli_util.option('--output-file', required=True, help="""The name of the export file to create, including the path, minus any format-specific extension.""", type=click.Path())
@cli_util.help_option
@cli_util.option('--force', is_flag=True, help='If the ouptut zip already exists, overwrite the existing zip without a confirmation prompt.')
@click.pass_context
@cli_util.wrap_exceptions
def export(ctx, output_file, force):
    config_file = os.path.expanduser(ctx.obj['config_file'])
    profile = ctx.obj['profile']

    config = configparser.ConfigParser()
    config.read(config_file)
    profile_to_export = {key: value for key, value in config[profile].items()}

    if 'security_token_file' not in profile_to_export:
        click.echo('ERROR: Specified profile is not a valid token profile. Please specify valid token profile with --profile', file=sys.stderr)
        sys.exit(1)

    zip_filename = output_file + '.' + ZIP_FILE_FORMAT
    if os.path.exists(zip_filename) and not force:
        if not click.confirm("File {} already exists, do you want to overwrite it?".format(zip_filename)):
            click.echo('Export canceled.', file=sys.stderr)
            sys.exit(0)

    click.echo('Exporting profile: {} from config file: {}'.format(profile, config_file), file=sys.stderr)

    try:
        temp_dir_name = tempfile.mkdtemp()
        with open(os.path.join(temp_dir_name, 'config'), 'w') as export_config_file:
            config = configparser.ConfigParser()
            config[profile] = translate_config_filepaths_to_prefix(profile_to_export)
            config.write(export_config_file)

        for key, value in six.iteritems(profile_to_export):
            if key.endswith((CONFIG_KEY_FILE_SUFFIX, TOKEN_FILE_SUFFIX)):
                copy(os.path.expanduser(value), temp_dir_name)

        archive_name = make_archive(output_file, ZIP_FILE_FORMAT, root_dir=temp_dir_name)
    finally:
        rmtree(temp_dir_name)

    click.echo('Export file written to: {}'.format(archive_name), file=sys.stderr)


@session_group.command('import', help="""Imports a CLI session from an archive.""")
@cli_util.option('--session-archive', required=True, help="""The session archive to import.""", type=click.Path())
@cli_util.help_option
@cli_util.option('--force', is_flag=True, help='If the profile being imported already exists, overwrite the existing profile without a confirmation prompt.')
@click.pass_context
@cli_util.wrap_exceptions
def import_session(ctx, session_archive, force):
    if not os.path.exists(session_archive):
        click.echo('File {} does not exist.'.format(session_archive), file=sys.stderr)
        sys.exit(1)

    config_file = os.path.expanduser(ctx.obj['config_file'])
    profile = ctx.obj['profile']

    config = configparser.ConfigParser()
    config.read(config_file)
    current_profiles = [key for key, value in config.items()]

    try:
        temp_dir_name = tempfile.mkdtemp()

        with zipfile.ZipFile(session_archive) as zf:
            zf.extractall(temp_dir_name)

            archived_config_location = os.path.join(temp_dir_name, 'config')
            if not os.path.exists(archived_config_location):
                click.echo("Session archive {} is invalid. Did not contain file 'config'.".format(session_archive), file=sys.stderr)
                sys.exit(1)

            archived_config = configparser.ConfigParser()
            archived_config.read(archived_config_location)
            archived_profiles = [key for key, value in archived_config.items()]

            if len(archived_profiles) < 1:
                click.echo('ERROR: The archived config does not contain valid profiles.', file=sys.stderr)
                sys.exit(1)

            # Ignore the default DEFAULT section item and pick the last item. If empty or only DEFAULT picks DEFAULT.
            profile_no = len(archived_profiles) - 1
            archived_profile_name = archived_profiles[profile_no]
            archived_profile = archived_config[archived_profile_name]

            if 'security_token_file' not in archived_profile:
                click.echo('ERROR: Cannot import non token based profile (profile must contain value for security_token_file).', file=sys.stderr)
                sys.exit(1)

            if force:
                cli_setup.remove_profile_from_config(config_file, archived_profile_name)

            while archived_profile_name in current_profiles and not force:
                archived_profile_name = click.prompt("Config already contains a profile with the same name as the archived profile: {}. Provide an alternative name for the imported profile".format(archived_profile_name))

            imported_resources_dir = os.path.join(cli_setup.DEFAULT_TOKEN_DIRECTORY, archived_profile_name)
            if not os.path.exists(imported_resources_dir):
                os.makedirs(imported_resources_dir)

            # copy referenced files from archived config to imported_resources_dir
            for key, value in six.iteritems(archived_profile):
                if key.endswith((CONFIG_KEY_FILE_SUFFIX, TOKEN_FILE_SUFFIX)):
                    # there is no nesting in the archive so the config will always reference the filename directly
                    new_file_location = os.path.join(imported_resources_dir, value)

                    existing_file_location = os.path.join(temp_dir_name, value)
                    copy(existing_file_location, imported_resources_dir)

                    cli_util.apply_user_only_access_permissions(new_file_location)

            # write new profile to existing config file
            archived_profile = translate_config_filepaths_to_prefix(archived_profile, imported_resources_dir)
            cli_setup.write_config(filename=config_file, profile_name=archived_profile_name, **archived_profile)
    finally:
        rmtree(temp_dir_name)

    click.echo('Imported profile {} written to: {}'.format(archived_profile_name, config_file), file=sys.stderr)

    click.echo("""
    Try out your newly imported session credentials with the following example command:

    oci iam region list --config-file {config_file} --profile {profile} --auth {auth}
""".format(config_file=config_file, profile=archived_profile_name, auth=cli_constants.OCI_CLI_AUTH_SESSION_TOKEN))


def translate_config_filepaths_to_prefix(config, prefix=''):
    translated_config = {}
    for key, value in six.iteritems(config):
        if key.endswith((CONFIG_KEY_FILE_SUFFIX, TOKEN_FILE_SUFFIX)):
            basename = os.path.basename(value)
            translated_config[key] = os.path.join(prefix, basename)
        else:
            translated_config[key] = value

    return translated_config
