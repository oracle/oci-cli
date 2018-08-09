# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
from .cli_root import cli
from .cli_constants import CLI_RC_CANNED_QUERIES_SECTION_NAME, CLI_RC_COMMAND_ALIASES_SECTION_NAME, CLI_RC_PARAM_ALIASES_SECTION_NAME, CLI_RC_DEFAULT_LOCATION
from . import cli_util
from .util import pymd5

import base64
import os
import os.path
import stat
import subprocess
import sys

from oci.regions import is_region
from oci.regions import REGIONS
from oci import config

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

generate_oci_config_instructions = """
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

default_canned_queries = """
[OCI_CLI_CANNED_QUERIES]
# For list results, this gets the ID and display-name of each item in the list. Note that when the names of attirbutes have
# dashes in them they need to be surrounded with double quotes. This query knows to look for a list because of the
# [*] syntax
get_id_and_display_name_from_list=data[*].{id: id, "display-name": "display-name"}

get_id_and_display_name_from_single_result=data.{id: id, "display-name": "display-name"}

# Retrieves a comma separated string, for example:
#     ocid1.instance.oc1.phx.xyz....,cli_test_instance_675195,RUNNING
get_id_display_name_and_lifecycle_state_from_single_result_as_csv=data.[id, "display-name", "lifecycle-state"] | join(`,`, @)

# Retrieves comma separated strings from a list of results
get_id_display_name_and_lifecycle_state_from_list_as_csv=data[*].[join(`,`, [id, "display-name", "lifecycle-state"])][]

# Filters where the display name contains some text
filter_by_display_name_contains_text=data[?contains("display-name", `your_text_here`)]

# Filters where the display name contains some text and pull out certain attributes(id and time-created)
filter_by_display_name_contains_text_and_get_attributes=data[?contains("display-name", `your_text_here`)].{id: id, timeCreated: "time-created"}

# Get the top 5 results from a list operation
get_top_5_results=data[:5]

# Get the last 2 results from a list operation
get_last_2_results=data[-2:]

# List instance public IPs from list vnics response
# Example: oci compute instance list-vnics --instance-id $I --query query://list_public_ips
list_public_ips=data[?"public-ip" != null]."public-ip"

# Get first public IP from list vnics response
# Example: oci compute instance list-vnics --instance-id $I --query query://get_public_ip
get_public_ip=data[?"public-ip" != null]."public-ip" | [0]
"""

default_command_aliases = """
[OCI_CLI_COMMAND_ALIASES]
# This lets you use "ls" instead of "list" for any list command in the CLI
ls = list

# This lets you do "oci os object rm" rather than "oci os object delete". This is an example of a "command sequence alias", where the alias on the left
# hand side only applies when the command sequence on the right hand side is invoked. You can think of these as being of the form:
#    <alias> = <dot-separated sequence of groups and sub-groups>.<command or group to alias>
#
# So in our example, <alias> = rm, <sequence of groups and sub-groups> = os object, <command or group to alias> = delete
rm = os.object.delete
"""

default_param_aliases = """
[OCI_CLI_PARAM_ALIASES]
# Parameter aliases either need to start with a double dash (--) or be a single dash (-) followed by a single letter. For example: --foo, -f
--ad = --availability-domain
--dn = --display-name
--egress-rules = --egress-security-rules
--ingress-rules = --ingress-security-rules
"""


public_key_filename_suffix = '_public.pem'
private_key_filename_suffix = '.pem'

config_generation_canceled_message = "Config creation canceled."

default_directory = os.path.join(os.path.expanduser('~'), '.oci')


@cli.group('setup', help="""Setup commands for CLI""")
@cli_util.help_option_group
def setup_group():
    pass


@setup_group.command('keys', help="""Generates an RSA key pair. A passphrase for the private key can be provided using either the 'passphrase' or 'passphrase-file' option. If neither option is provided, the user will be prompted for a passphrase via stdin.""")
@cli_util.option('--key-name', default='oci_api_key', help="""A name for the key. Generated key files will be {key-name}.pem and {key-name}_public.pem""")
@cli_util.option('--output-dir', default=default_directory, help="""An optional directory to output the generated keys.""", type=click.Path())
@cli_util.option('--passphrase', help="""An optional passphrase to encrypt the private key.""")
@cli_util.option('--passphrase-file', help="""An optional file with the first line specifying a passphrase to encrypt the private key (or '-' to read from stdin).""", type=click.File(mode='r'))
@cli_util.option('--overwrite', default=False, help="""An option to overwrite existing files without a confirmation prompt.""", is_flag=True)
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
        create_directory(output_dir)

    private_key = cli_util.generate_key()
    public_key = private_key.public_key()

    write_public_key_to_file(os.path.join(output_dir, key_name + public_key_filename_suffix), public_key, overwrite)
    write_private_key_to_file(os.path.join(output_dir, key_name + private_key_filename_suffix), private_key, passphrase, overwrite)

    fingerprint = public_key_to_fingerprint(public_key)
    click.echo('Public key fingerprint: {}'.format(fingerprint))
    click.echo(click.wrap_text(upload_public_key_instructions, preserve_paragraphs=True))


@setup_group.command('config', help="""Interactive script to generate oci config file.""")
@cli_util.help_option
def generate_oci_config():
    click.echo(click.wrap_text(text=generate_oci_config_instructions, preserve_paragraphs=True))

    config_location = os.path.abspath(click.prompt('Enter a location for your config', default=os.path.join(default_directory, 'config'), value_proc=process_config_filename))
    if os.path.exists(config_location):
        if not click.confirm('File: {} already exists. Do you want to overwrite?'.format(config_location)):
            click.echo(config_generation_canceled_message)
            return
    else:
        dirname = os.path.dirname(config_location)

        # if user inputs only a filename (dirname=='') it implies the current directory so no need to create a dir
        if dirname and not os.path.exists(dirname):
            create_directory(dirname)

    user_id = click.prompt('Enter a user OCID', value_proc=lambda ocid: validate_ocid(ocid, config.PATTERNS['user']))
    tenant_id = click.prompt('Enter a tenancy OCID', value_proc=lambda ocid: validate_ocid(ocid, config.PATTERNS['tenancy']))

    region = None
    while not region:
        region_list = ', '.join(sorted(REGIONS))
        region = click.prompt(text='Enter a region (e.g. {})'.format(region_list), value_proc=validate_region)

    if click.confirm("Do you want to generate a new RSA key pair? (If you decline you will be asked to supply the path to an existing key.)", default=True):
        key_location = os.path.abspath(click.prompt(text='Enter a directory for your keys to be created', default=default_directory))
        key_location = os.path.expanduser(key_location)
        if not os.path.exists(key_location):
            create_directory(key_location)

        private_key = cli_util.generate_key()
        public_key = private_key.public_key()

        key_name = click.prompt('Enter a name for your key', 'oci_api_key')
        if not write_public_key_to_file(os.path.join(key_location, key_name + public_key_filename_suffix), public_key):
            click.echo(config_generation_canceled_message)
            return

        key_passphrase = click.prompt(text='Enter a passphrase for your private key (empty for no passphrase)', default='', hide_input=True, show_default=False, confirmation_prompt=True)
        private_key_file = os.path.join(key_location, key_name + private_key_filename_suffix)
        if not write_private_key_to_file(private_key_file, private_key, key_passphrase):
            click.echo(config_generation_canceled_message)
            return

        fingerprint = public_key_to_fingerprint(public_key)
        click.echo("Fingerprint: {}".format(fingerprint))
    else:
        private_key_file, has_passphrase, private_key = click.prompt(text='Enter the location of your private key file', value_proc=validate_private_key_file)
        private_key_file = os.path.abspath(private_key_file)

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


@setup_group.command('oci-cli-rc', help="""Generates a oci_cli_rc file that can contain parameter default values and other configuration information such as command aliases and predefined queries.

This command will populate the file with some default aliases and predefined queries.
""")
@cli_util.option('--file', show_default=True, default=CLI_RC_DEFAULT_LOCATION, type=click.File(mode='a+b'), help="The file into which default aliases and predefined queries will be loaded")
@cli_util.help_option
def setup_cli_rc(file):
    if hasattr(file, 'name') and file.name == '<stdout>':
        raise click.UsageError('This command does not support writing data to stdout')

    file.seek(0)
    data = file.read().decode()

    if CLI_RC_CANNED_QUERIES_SECTION_NAME in data:
        click.echo('Predefined queries will not be written as the specified file already contains a section for these queries', file=sys.stderr)
    else:
        file.write(('\n\n{}'.format(default_canned_queries)).encode())
        click.echo('Predefined queries written under section {}'.format(CLI_RC_CANNED_QUERIES_SECTION_NAME))

    if CLI_RC_COMMAND_ALIASES_SECTION_NAME in data:
        click.echo('Command aliases will not be written as the specified file already contains a section for command aliases', file=sys.stderr)
    else:
        file.write(('\n\n{}'.format(default_command_aliases)).encode())
        click.echo('Command aliases written under section {}'.format(CLI_RC_COMMAND_ALIASES_SECTION_NAME))

    if CLI_RC_PARAM_ALIASES_SECTION_NAME in data:
        click.echo('Parameter aliases will not be written as the specified file already contains a section for parameter aliases', file=sys.stderr)
    else:
        file.write(('\n\n{}'.format(default_param_aliases)).encode())
        click.echo('Parameter aliases written under section {}'.format(CLI_RC_PARAM_ALIASES_SECTION_NAME))


@setup_group.command('autocomplete', help="""Interactive script to set up tab completion for commands and parameters.""")
@cli_util.help_option
def setup_autocomplete():
    # TODO: we might be able to support completion in bash on windows so we should test that but in the meantime it is better to return a clear error for most Windows users who will not be able to use this
    if sys.platform == 'cygwin':
        click.echo("Tab completion only available on Windows when using Powershell.")
        return

    if sys.platform == 'win32':
        setup_autocomplete_windows()
    else:
        setup_autocomplete_non_windows()


def setup_autocomplete_windows():
    oci_tab_completion_file = 'OciTabExpansion.ps1'

    script_relative_path = os.path.join('bin', oci_tab_completion_file)
    path_to_install_dir = os.path.dirname(os.path.abspath(__file__))
    completion_script_file = os.path.join(path_to_install_dir, script_relative_path)
    if not os.path.exists(completion_script_file):
        click.echo('Could not locate autocomplete script at {}. Exiting script.'.format(completion_script_file))
        sys.exit(1)

    click.echo("Using tab completion script at: {}".format(completion_script_file))

    # subprocess.check_output looks like it comes back as a byte string, so coerce to a regular string
    ps_profile_file_path = subprocess.check_output(['powershell', '-NoProfile', 'echo $profile']).decode(sys.stdout.encoding).strip()
    confirm_prompt = 'To set up autocomplete, we need to add a few lines to your Powershell profile: {}. Please confirm this is ok.'.format(ps_profile_file_path)

    if click.confirm(confirm_prompt, default=True):
        if not os.path.exists(os.path.dirname(ps_profile_file_path)):
            os.makedirs(os.path.dirname(ps_profile_file_path))

        with open(ps_profile_file_path, mode='a+') as f:
            f.seek(0)
            content = f.read()

            if oci_tab_completion_file in content:
                click.echo("It looks like tab completion for oci is already configured in {ps_profile_file_path}. If you want to re-run the setup command please remove any lines containing '{oci_tab_completion_file}' from {ps_profile_file_path}.".format(oci_tab_completion_file=oci_tab_completion_file, ps_profile_file_path=ps_profile_file_path))
                return

            f.write('\n. {}\n'.format(completion_script_file))
            click.echo('Success!\nReload your Powershell profile or restart your shell for the changes to take effect.')
            click.echo('In order to run the autocomplete script, you may also need to set your Powershell execution policy to allow for running local scripts (as an Administrator run Set-ExecutionPolicy RemoteSigned in a Powershell prompt)')
    else:
        click.echo('Exiting script. Tab completion not set up.')
        return


def setup_autocomplete_non_windows():
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
    script_relative_path = os.path.join('bin', 'oci_autocomplete.sh')
    path_to_install_dir = os.path.dirname(os.path.abspath(__file__))
    completion_script_file = os.path.join(path_to_install_dir, script_relative_path)
    if not os.path.exists(completion_script_file):
        click.echo('Could not locate autocomplete script at {}. Exiting script.'.format(completion_script_file))
        sys.exit(1)

    click.echo("Using tab completion script at: {}".format(completion_script_file))

    bash_profile_line = '[[ -e "{completion_script_file}" ]] && source "{completion_script_file}"'.format(completion_script_file=completion_script_file)
    confirm_prompt = 'To set up autocomplete, we need to add a few lines to your {bash_config_location} file. Please confirm this is ok.'.format(bash_config_location=bash_config_location)

    if click.confirm(confirm_prompt, default=True):
        with open(bash_config_location, mode='a+') as f:
            f.seek(0)
            content = f.read()

            # this check is not foolproof but we want to avoid adding a bunch of lines to .bash_profile/.bashrc if the user re-runs the command
            if script_relative_path in content:
                click.echo("It looks like tab completion for oci is already configured in {bash_config_location}. If you want to re-run the setup command please remove the line containing '{script_relative_path}' from {bash_config_location}.".format(script_relative_path=script_relative_path, bash_config_location=bash_config_location))
                return

            f.write('\n{}\n'.format(bash_profile_line))

        click.echo("Success!\nRun '{}' or restart your terminal for the changes to take effect.".format(bash_profile_line))
    else:
        click.echo('Exiting script. Tab completion not set up.')
        return


@setup_group.command('repair-file-permissions', help="""Resets permissions on a given file to an appropriate access level for sensitive files. Generally this is used to fix permissions on a private key file or config file to meet the requirements of the CLI.
On Windows, full control will be given to System, Administrators, and the current user.  On Unix, Read / Write permissions will be given to the current user.""")
@cli_util.option('--file', required=True, help="""The file to repair permissions on.""")
@cli_util.help_option
def repair_file_permissions(file):
    file = os.path.expanduser(file)
    if not os.path.exists(file):
        raise click.UsageError('Could not find file: {}'.format(file))

    if not os.path.isfile(file):
        raise click.UsageError('This command is only supported for files.')

    apply_user_only_access_permissions(file)


def public_key_to_fingerprint(public_key):
    bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo)

    header = b'-----BEGIN PUBLIC KEY-----'
    footer = b'-----END PUBLIC KEY-----'
    bytes = bytes.replace(header, b'').replace(footer, b'').replace(b'\n', b'')

    key = base64.b64decode(bytes)
    fp_plain = pymd5.md5(key).hexdigest()
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

    # only user has R/W permissions to the config file
    apply_user_only_access_permissions(filename)


def write_public_key_to_file(filename, public_key, overwrite=False):
    if not overwrite and os.path.isfile(filename) and not click.confirm('File {} already exists, do you want to overwrite?'.format(filename)):
        return False

    with open(filename, "wb") as f:
        f.write(cli_util.serialize_key(public_key=public_key))

    # only user has R/W permissions to the key file
    apply_user_only_access_permissions(filename)

    click.echo('Public key written to: {}'.format(filename))
    return True


def write_private_key_to_file(filename, private_key, passphrase, overwrite=False):
    if not overwrite and os.path.isfile(filename) and not click.confirm('File {} already exists, do you want to overwrite?'.format(filename)):
        return False

    with open(filename, "wb") as f:
        f.write(cli_util.serialize_key(private_key=private_key, passphrase=passphrase))

    # only user has R/W permissions to the key file
    apply_user_only_access_permissions(filename)

    click.echo('Private key written to: {}'.format(filename))
    return True


def apply_user_only_access_permissions(path):
    if not os.path.exists(path):
        raise RuntimeError("Failed attempting to set permissions on path that does not exist: {}".format(path))

    if cli_util.is_windows():
        # General permissions strategy is:
        #   - if we create a new folder (e.g. C:\Users\opc\.oci), set access to allow full control for current user and no access for anyone else
        #   - if we create a new file, set access to allow full control for current user and no access for anyone else
        #   - thus if the user elects to place a new file (config or key) in an existing directory, we will not change the
        #     permissions of that directory but will explicitly set the permissions on that file
        username = os.environ['USERNAME']
        admin_grp = '*S-1-5-32-544'
        system_usr = '*S-1-5-18'
        try:
            if os.path.isfile(path):
                subprocess.check_output('icacls "{path}" /reset'.format(path=path), stderr=subprocess.STDOUT)
                subprocess.check_output('icacls "{path}" /inheritance:r /grant:r {username}:F /grant {admin_grp}:F /grant {system_usr}:F'.format(path=path, username=username, admin_grp=admin_grp, system_usr=system_usr), stderr=subprocess.STDOUT)
            else:
                if os.listdir(path):
                    # safety check to make sure we aren't changing permissions of existing files
                    raise RuntimeError("Failed attempting to set permissions on existing folder that is not empty.")
                subprocess.check_output('icacls "{path}" /reset'.format(path=path), stderr=subprocess.STDOUT)
                subprocess.check_output('icacls "{path}" /inheritance:r /grant:r {username}:(OI)(CI)F  /grant:r {admin_grp}:(OI)(CI)F /grant:r {system_usr}:(OI)(CI)F'.format(path=path, username=username, admin_grp=admin_grp, system_usr=system_usr), stderr=subprocess.STDOUT)

        except subprocess.CalledProcessError as exc_info:
            print("Error occurred while attempting to set permissions for {path}: {exception}".format(path=path, exception=str(exc_info)))
            sys.exit(exc_info.returncode)
    else:
        if os.path.isfile(path):
            os.chmod(path, stat.S_IRUSR | stat.S_IWUSR)
        else:
            # For directories, we need to apply S_IXUSER otherwise it looks like on Linux/Unix/macOS if we create the directory then
            # it won't behave like a directory and let files be put into it
            os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)


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


def process_config_filename(filename):
    filename_expanded = os.path.expanduser(filename)
    if os.path.isdir(filename_expanded):
        raise click.BadParameter("Config location must be a filename not a directory")

    return filename_expanded


def validate_ocid(ocid, pattern):
    if not pattern.match(ocid):
        raise click.BadParameter("Invalid OCID format. Instructions to find OCIDs: https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm#Other")

    return ocid


def create_directory(dirname):
    os.makedirs(dirname)
    apply_user_only_access_permissions(dirname)
