# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
from .cli_root import cli
from . import cli_util

import base64
import hashlib
import os.path
import sys

from oraclebmc.regions import is_region
from oraclebmc import config

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

generate_bmcs_config_instructions = """
    This command provides a walkthrough of creating a valid CLI config file.

    The following links explain where to find the information required by this script:

    User OCID and Tenancy OCID:


    \b
    https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm#Other


    Region:


    \b
    https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm

    General config documentation:


    \b
    https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/sdkconfig.htm

    \n

"""

upload_public_key_instructions = """
    \n
    If you haven't already uploaded your public key through the console, follow the instructions on the page linked below in the section 'How to upload the public key':

    \b
    https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm#How2

    \n
"""

public_key_filename_suffix = '_public.pem'
private_key_filename_suffix = '.pem'

config_generation_canceled_message = "Config creation canceled."

default_directory = os.path.join(os.path.expanduser('~'), '.oraclebmc')


@cli.group('setup', help="""Setup commands for CLI""")
@cli_util.help_option_group
def setup_group():
    pass


@setup_group.command('keys', help="""Generates an RSA key pair. A passphrase for the private key can be provided using either the 'passphrase' or 'passphrase-file' option. If neither option is provided, the user will be prompted for a passphrase via stdin.""")
@click.option('--key-name', default='bmcs_api_key', help="""A name for the key. Generated key files will be {key-name}.pem and {key-name}_public.pem""")
@click.option('--output-dir', default=default_directory, help="""An optional directory to output the generated keys.""", type=click.Path())
@click.option('--passphrase', help="""An optional passphrase to encrypt the private key.""")
@click.option('--passphrase-file', help="""An optional file with the first line specifying a passphrase to encrypt the private key (or '-' to read from stdin).""", type=click.File(mode='r'))
@click.option('--overwrite', default=False, help="""An option to overwrite existing files without a confirmation prompt.""", is_flag=True)
@cli_util.help_option
def generate_key_pair(key_name, output_dir, passphrase, passphrase_file, overwrite):
    if passphrase and passphrase_file:
        raise click.UsageError("Cannot specify both passphrase and passphrase-file options")

    if passphrase_file:
        passphrase = passphrase_file.readline()
        if not passphrase or passphrase.isspace():
            raise click.UsageError("passphrase-file must specify a password in the first line of the file")

    # if no passphrase arguments are specified, then prompt for one (can still be left empty explicitly by user)
    if not passphrase:
        passphrase = click.prompt(text='Enter a passphrase for your private key (empty for no passphrase)', default='', hide_input=True, show_default=False, confirmation_prompt=True)

    output_dir = os.path.expanduser(output_dir)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    private_key = cli_util.generate_key()
    public_key = private_key.public_key()

    write_public_key_to_file(os.path.join(output_dir, key_name + public_key_filename_suffix), public_key, overwrite)
    write_private_key_to_file(os.path.join(output_dir, key_name + private_key_filename_suffix), private_key, passphrase, overwrite)

    fingerprint = public_key_to_fingerprint(public_key)
    click.echo('Public key fingerprint: {}'.format(fingerprint))
    click.echo(click.wrap_text(upload_public_key_instructions, preserve_paragraphs=True))


@setup_group.command('config', help="""Interactive script to generate bmcs config file.""")
@cli_util.help_option
def generate_bmcs_config():
    click.echo(click.wrap_text(text=generate_bmcs_config_instructions, preserve_paragraphs=True))

    config_location = click.prompt('Enter a location for your config', default=os.path.join(default_directory, 'config'), value_proc=validate_config_filename)
    if os.path.exists(config_location):
        if not click.confirm('File: {} already exists. Do you want to overwrite?'.format(config_location)):
            click.echo(config_generation_canceled_message)
            return
    else:
        dirname = os.path.dirname(config_location)

        # if user inputs only a filename (dirname=='') it implies the current directory so no need to create a dir
        if dirname and not os.path.exists(dirname):
            os.makedirs(dirname)

    user_id = click.prompt('Enter a user OCID', value_proc=lambda ocid: validate_ocid(ocid, config.PATTERNS['user']))
    tenant_id = click.prompt('Enter a tenancy OCID', value_proc=lambda ocid: validate_ocid(ocid, config.PATTERNS['tenancy']))

    region = None
    while not region:
        region = click.prompt(text='Enter a region', value_proc=validate_region)

    if click.confirm("Do you want to generate a new RSA key pair? (If you decline you will be asked to supply the path to an existing key.)", default=True):
        key_location = click.prompt(text='Enter a directory for your keys to be created', default=default_directory)
        key_location = os.path.expanduser(key_location)
        if not os.path.exists(key_location):
            os.makedirs(key_location)

        private_key = cli_util.generate_key()
        public_key = private_key.public_key()

        key_name = click.prompt('Enter a name for your key', 'bmcs_api_key')
        if not write_public_key_to_file(os.path.join(key_location, key_name + public_key_filename_suffix), public_key):
            click.echo(config_generation_canceled_message)
            return

        key_passphrase = click.prompt(text='Enter a passphrase for your private key (empty for no passphrase)', default='', hide_input=True, show_default=False, confirmation_prompt=True)
        private_key_file = os.path.join(key_location, key_name + private_key_filename_suffix)
        if not write_private_key_to_file(private_key_file, private_key, key_passphrase):
            click.echo(config_generation_canceled_message)
            return

        fingerprint = public_key_to_fingerprint(public_key)
    else:
        private_key_file, has_passphrase, private_key = click.prompt(text='Enter the location of your private key file', value_proc=validate_private_key_file)

        key_passphrase = None
        if has_passphrase:
            key_passphrase, private_key = click.prompt(text='Enter the passphrase for your private key', hide_input=True, value_proc=lambda passphrase: validate_private_key_passphrase(private_key_file, passphrase))

        fingerprint = public_key_to_fingerprint(private_key.public_key())
        click.echo("Fingerprint: {}".format(fingerprint))

    if key_passphrase and not click.confirm('Do you want to write your passphrase to the config file? (if not, you will need to supply it as an argument to the CLI)', default=False):
        key_passphrase = None

    write_config(config_location, user_id, fingerprint, private_key_file, tenant_id, region, key_passphrase)

    click.echo('Config written to {}'.format(config_location))
    click.echo(click.wrap_text(upload_public_key_instructions, preserve_paragraphs=True))


@setup_group.command('autocomplete', help="""Interactive script to set up tab completion for commands and parameters.""")
@cli_util.help_option
def setup_autocomplete():
    # TODO: we might be able to support completion in bash on windows so we should test that but in the meantime it is better to return a clear error for most Windows users who will not be able to use this
    if sys.platform == 'win32' or sys.platform == 'cygwin':
        click.echo("Tab completion is not currently available on Windows.")
        return

    # guidance from click is to add to .bashrc so if user has a .bashrc file, use that
    # if .bashrc does not exist but .bash_profile does exist, we fall back to that
    # if neither exist, we must create one. On Linux we use bashrc as recommended by click,
    # but Mac terminal does not source .bashrc by default so use .bash_profile instead
    bash_profile_location = os.path.expanduser('~/.bash_profile')
    bash_rc_location = os.path.expanduser('~/.bashrc')
    bash_config_location = bash_profile_location if sys.platform == 'darwin' else bash_rc_location
    if os.path.exists(bash_rc_location):
        bash_config_location = bash_rc_location
    elif os.path.exists(bash_profile_location):
        bash_config_location = bash_profile_location

    # source bash completion script in CLI install directory
    script_relative_path = os.path.join('bin', 'bmcs_autocomplete.sh')
    path_to_install_dir = os.path.dirname(os.path.abspath(__file__))
    completion_script_file = os.path.join(path_to_install_dir, script_relative_path)
    if not os.path.exists(completion_script_file):
        click.echo('Could not locate autocomplete script at {}. Exiting script.'.format(completion_script_file))
        return

    click.echo("Using tab completion script at: {}".format(completion_script_file))

    bash_profile_line = '. {}'.format(completion_script_file)
    confirm_prompt = 'To set up autocomplete, we need to add a few lines to your {bash_config_location} file. Please confirm this is ok.'.format(bash_config_location=bash_config_location)

    if click.confirm(confirm_prompt, default=True):
        with open(bash_config_location, mode='a+') as f:
            f.seek(0)
            content = f.read()

            # this check is not foolproof but we want to avoid adding a bunch of lines to .bash_profile/.bashrc if the user re-runs the command
            if script_relative_path in content:
                click.echo("It looks like tab completion for bmcs is already configured in {bash_config_location}. If you want to re-run the setup command please remove the line containing '{script_relative_path}' from {bash_config_location}.".format(script_relative_path=script_relative_path, bash_config_location=bash_config_location))
                return

            f.write('\n{}\n'.format(bash_profile_line))

        click.echo("Success!\nRun '{}' or restart your terminal for the changes to take effect.".format(bash_profile_line))
    else:
        click.echo('Exiting script. Tab completion not set up.')
        return


def public_key_to_fingerprint(public_key):
    bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo)

    header = b'-----BEGIN PUBLIC KEY-----'
    footer = b'-----END PUBLIC KEY-----'
    bytes = bytes.replace(header, b'').replace(footer, b'').replace(b'\n', b'')

    key = base64.b64decode(bytes)
    fp_plain = hashlib.md5(key).hexdigest()
    return ':'.join(a + b for a, b in zip(fp_plain[::2], fp_plain[1::2]))


def write_config(filename, user_id, fingerprint, key_file, tenant_id, region, passphrase=None):
    with open(filename, 'w') as f:
        f.write('[DEFAULT]\n')
        f.write('user={}\n'.format(user_id))
        f.write('fingerprint={}\n'.format(fingerprint))
        f.write('key_file={}\n'.format(key_file))
        f.write('tenancy={}\n'.format(tenant_id))
        f.write('region={}\n'.format(region))

        if passphrase:
            f.write("pass_phrase={}\n".format(passphrase))


def write_public_key_to_file(filename, public_key, overwrite=False):
    if not overwrite and os.path.isfile(filename) and not click.confirm('File {} already exists, do you want to overwrite?'.format(filename)):
        return False

    with open(filename, "wb") as f:
        f.write(cli_util.serialize_key(public_key=public_key))

    click.echo('Public key written to: {}'.format(filename))
    return True


def write_private_key_to_file(filename, private_key, passphrase, overwrite=False):
    if not overwrite and os.path.isfile(filename) and not click.confirm('File {} already exists, do you want to overwrite?'.format(filename)):
        return False

    with open(filename, "wb") as f:
        f.write(cli_util.serialize_key(private_key=private_key, passphrase=passphrase))

    click.echo('Private key written to: {}'.format(filename))
    return True


def validate_private_key_passphrase(filename, passphrase):
    with open(filename, 'rb') as f:
        try:
            private_key = serialization.load_pem_private_key(data=f.read(), password=passphrase.encode("ascii"), backend=default_backend())
            return passphrase, private_key
        except ValueError:
            # exception from serialization lib is 'Bad decrpt. Incorrect password?'
            raise click.BadParameter("Incorrect passphrase, could not decrypt private key")


def validate_private_key_file(filename):
    filename = os.path.expanduser(filename)
    if not os.path.isfile(filename):
        raise click.BadParameter('No file found at: {}'.format(filename))
    else:
        with open(filename, 'rb') as f:
            try:
                private_key = serialization.load_pem_private_key(data=f.read(), password=None, backend=default_backend())
                return filename, False, private_key
            except TypeError:
                # file is a private key but is password protected
                return filename, True, None
            except ValueError:
                raise click.BadParameter('Could not load file as private key. File: {}'.format(filename))


def validate_fingerprint(fingerprint):
    if len(fingerprint.split(':')) != 16:
        raise click.BadParameter('Invalid fingerprint: {}'.format(fingerprint))


def validate_region(region):
    if not is_region(region):
        click.echo("Unrecognized region: {}. Valid regions can be found here: https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm".format(region))
        if not click.confirm("Continue with unrecognized region? (Enter 'n' to re-enter region)"):
            return None

    return region


def validate_config_filename(filename):
    if os.path.isdir(filename):
        raise click.BadParameter("Config location must be a filename not a directory")

    return filename


def validate_ocid(ocid, pattern):
    if not pattern.match(ocid):
        raise click.BadParameter("Invalid OCID format. Instructions to find OCIDs: https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm#Other")

    return ocid
