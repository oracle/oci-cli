# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
from .cli_root import cli
from .cli_constants import CLI_RC_CANNED_QUERIES_SECTION_NAME, CLI_RC_COMMAND_ALIASES_SECTION_NAME, CLI_RC_PARAM_ALIASES_SECTION_NAME, CLI_RC_DEFAULT_LOCATION, OCI_CLI_AUTH_API_KEY, OCI_CLI_AUTH_SESSION_TOKEN, OCI_CLI_AUTH_INSTANCE_PRINCIPAL, OCI_CLI_AUTH_RESOURCE_PRINCIPAL
from . import cli_util
from services.identity.src.oci_cli_identity.generated import identity_cli
from .util import pymd5

import base64

import configparser
import os
import os.path
import subprocess
import sys
import errno
import json
import re
import glob

from oci.regions import is_region
from oci.regions import REGIONS
from oci import config, exceptions, signer

import platform
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

generate_oci_config_instructions = """
    This command provides a walkthrough of creating a valid CLI config file.

    The following links explain where to find the information required by this script:

    User API Signing Key, OCID and Tenancy OCID:


    \b
    https://docs.cloud.oracle.com/Content/API/Concepts/apisigningkey.htm#Other


    Region:


    \b
    https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm

    General config documentation:


    \b
    https://docs.cloud.oracle.com/Content/API/Concepts/sdkconfig.htm

    \n

"""

instance_principal_setup_instructions = """
    This command provides a walkthrough of setting up instance principal authentication for an OCI compute instance.

    The following links provide information about topics and resources referenced by this script:

    Resource OCIDs:


    \b
    https://docs.oracle.com/en-us/iaas/Content/General/Concepts/identifiers.htm


    Compute Instances:


    \b
    https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/computeoverview.htm


    Dynamic Groups:


    \b
    https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingdynamicgroups.htm


    Policies:


    \b
    https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm


    In order to successfully run this command, you must:


        - have an existing instance from which you want to run commands using instance principal authentication

        - be an administrator in your tenancy so that you can create/update the necessary dynamic group and policy used to enable instance principal authentication for your instance


    This script also requires an existing form of valid authentication to successfully run. If you do not have an existing config file and you ran this command using {api_key_auth} or {security_token_auth} auth, you will be prompted to create a new config file to use for authentication during this instance principal setup process.

    \n

""".format(api_key_auth=OCI_CLI_AUTH_API_KEY, security_token_auth=OCI_CLI_AUTH_SESSION_TOKEN)

instance_principal_setup_end_message = """
    \n
    If you haven't already, you can install the CLI on your instance by connecting to your instance using SSH and running the following command:


    \b
    bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"


    After you have installed the CLI on your instance, you can test out your instance principal authentication by connecting to your instance using SSH and running the following example command (Note: if you entered a custom policy that does not allow your dynamic group to view all compute instances in your instance's compartment, then the following example command will not work):


    \b
    oci compute instance list --compartment-id {compartment_id} --auth {auth}

    \n
"""

upload_public_key_instructions = """
    \n
    If you haven't already uploaded your API Signing public key through the console, follow the instructions on the page linked below in the section 'How to upload the public key':

    \b
    https://docs.cloud.oracle.com/Content/API/Concepts/apisigningkey.htm#How2

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


PUBLIC_KEY_FILENAME_SUFFIX = '_public.pem'
PRIVATE_KEY_FILENAME_SUFFIX = '.pem'

config_generation_canceled_message = "Config creation canceled."

DEFAULT_DIRECTORY = os.path.join(os.path.expanduser('~'), '.oci')
DEFAULT_KEY_NAME = 'oci_api_key'
DEFAULT_PROFILE_NAME = 'DEFAULT'
DEFAULT_TOKEN_DIRECTORY = os.path.join(DEFAULT_DIRECTORY, 'sessions')
DEFAULT_CONFIG_LOCATION = os.path.join(DEFAULT_DIRECTORY, 'config')
USER_BASH_RC = os.path.expanduser(os.path.join('~', '.bashrc'))
USER_BASH_PROFILE = os.path.expanduser(os.path.join('~', '.bash_profile'))
DEFAULT_INSTALL_DIR = os.path.expanduser(os.path.join('~', 'lib', 'oracle-cli'))
OCI_EXECUTABLE_NAME = 'oci.exe' if sys.platform == 'win32' else 'oci'


@cli.group('setup', help="""Setup commands for CLI""")
@cli_util.help_option_group
def setup_group():
    pass


@setup_group.command('keys', help="""Generates an API Signing RSA key pair. A passphrase for the private key can be provided using either the 'passphrase' or 'passphrase-file' option. If neither option is provided, the user will be prompted for a passphrase via stdin.""")
@cli_util.option('--key-name', default=DEFAULT_KEY_NAME, help="""A name for the API Signing key. Generated key files will be {key-name}.pem and {key-name}_public.pem""")
@cli_util.option('--output-dir', default=DEFAULT_DIRECTORY, help="""An optional directory to output the generated API Signing keys.""", type=click.Path())
@cli_util.option('--passphrase', help="""An optional passphrase to encrypt the private API Signing key.""")
@cli_util.option('--passphrase-file', help="""An optional file with the first line specifying a passphrase to encrypt the API Signing private key (or '-' to read from stdin).""", type=click.File(mode='r'))
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
        cli_util.create_directory(output_dir)

    private_key = cli_util.generate_key()
    public_key = private_key.public_key()

    write_public_key_to_file(os.path.join(output_dir, key_name + PUBLIC_KEY_FILENAME_SUFFIX), public_key, overwrite)
    write_private_key_to_file(os.path.join(output_dir, key_name + PRIVATE_KEY_FILENAME_SUFFIX), private_key, passphrase, overwrite)

    fingerprint = public_key_to_fingerprint(public_key)
    click.echo('Public key fingerprint: {}'.format(fingerprint))
    click.echo(click.wrap_text(upload_public_key_instructions, preserve_paragraphs=True))


@setup_group.command('config', help="""Interactive script to generate oci config file.""")
@cli_util.help_option
def generate_oci_config():
    click.echo(click.wrap_text(text=generate_oci_config_instructions, preserve_paragraphs=True))

    config_location, profile_name = prompt_for_config_location()
    if not config_location:
        click.echo(config_generation_canceled_message)
        sys.exit(0)

    user_id = click.prompt('Enter a user OCID', value_proc=lambda ocid: validate_ocid(ocid, config.PATTERNS['user']))
    tenant_id = click.prompt('Enter a tenancy OCID', value_proc=lambda ocid: validate_ocid(ocid, config.PATTERNS['tenancy']))

    region = prompt_for_region()

    if click.confirm("Do you want to generate a new API Signing RSA key pair? (If you decline you will be asked to supply the path to an existing key.)", default=True):
        key_location = os.path.abspath(os.path.expanduser(click.prompt(text='Enter a directory for your keys to be created', default=DEFAULT_DIRECTORY)))
        if not os.path.exists(key_location):
            cli_util.create_directory(key_location)

        private_key = cli_util.generate_key()
        public_key = private_key.public_key()

        key_name = click.prompt('Enter a name for your key', DEFAULT_KEY_NAME)
        if not write_public_key_to_file(os.path.join(key_location, key_name + PUBLIC_KEY_FILENAME_SUFFIX), public_key):
            click.echo(config_generation_canceled_message)
            return

        key_passphrase = click.prompt(text='Enter a passphrase for your private key (empty for no passphrase)', default='', hide_input=True, show_default=False, confirmation_prompt=True)
        private_key_file = os.path.join(key_location, key_name + PRIVATE_KEY_FILENAME_SUFFIX)
        if not write_private_key_to_file(private_key_file, private_key, key_passphrase):
            click.echo(config_generation_canceled_message)
            return

        fingerprint = public_key_to_fingerprint(public_key)
        click.echo("Fingerprint: {}".format(fingerprint))
    else:
        private_key_file, has_passphrase, private_key = click.prompt(text='Enter the location of your API Signing private key file', value_proc=validate_private_key_file)
        private_key_file = os.path.abspath(private_key_file)

        key_passphrase = None
        if has_passphrase:
            key_passphrase, private_key = click.prompt(text='Enter the passphrase for your private key', hide_input=True, value_proc=lambda passphrase: validate_private_key_passphrase(private_key_file, passphrase))

        fingerprint = public_key_to_fingerprint(private_key.public_key())
        click.echo("Fingerprint: {}".format(fingerprint))

    if key_passphrase and not click.confirm('Do you want to write your passphrase to the config file? (If not, you will need to enter it when prompted each time you run an oci command)', default=False):
        key_passphrase = None

    write_config(
        config_location,
        user_id,
        fingerprint,
        private_key_file,
        tenant_id,
        region,
        pass_phrase=key_passphrase,
        profile_name=profile_name
    )

    click.echo('Config written to {}'.format(config_location))
    click.echo(click.wrap_text(upload_public_key_instructions, preserve_paragraphs=True))


@setup_group.command('instance-principal', help="""Interactive script to set up instance principal authentication for an existing compute instance.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def setup_instance_principal(ctx):
    click.echo(click.wrap_text(text=instance_principal_setup_instructions, preserve_paragraphs=True))

    # get the private key passphrase (applicable for api key pair and session token auth), and if the passphrase is not None, then return it each time the passphrase is requested during this script
    passphrase = None
    if ctx.obj['auth'] == OCI_CLI_AUTH_API_KEY or ctx.obj['auth'] == OCI_CLI_AUTH_SESSION_TOKEN:
        passphrase = get_passphrase(ctx)
    if passphrase:
        def passphrase_provider():
            return passphrase
        cli_util.prompt_for_passphrase = passphrase_provider

    # build necessary client objects; these functions also handle authentication
    compute_client = cli_util.build_client('core', 'compute', ctx)
    identity_client = cli_util.build_client('identity', 'identity', ctx)

    # build the config object (applicable for auth types other than instance principal or resource principal)
    config_obj = None
    if ctx.obj['auth'] != OCI_CLI_AUTH_INSTANCE_PRINCIPAL and ctx.obj['auth'] != OCI_CLI_AUTH_RESOURCE_PRINCIPAL:
        config_obj = cli_util.build_config(ctx.obj)

    if not click.confirm('Do you have an existing compute instance for which you would like to set up instance principal authentication?', default=True):
        click.echo('Please create a compute instance and then run this command again. For information regarding how to create a compute instance, please visit https://docs.oracle.com/en-us/iaas/Content/GSG/Reference/overviewworkflow.htm')
        sys.exit(1)

    # get the instance OCID and the name of the compartment that the instance is in
    instance_ocid, result = get_resource('instance', compute_client.get_instance)
    instance_compartment_ocid = result.data.compartment_id
    result = identity_client.get_compartment(instance_compartment_ocid)
    instance_compartment_name = result.data.name

    if click.confirm('Do you want to add this instance to an existing dynamic group?', default=False):
        # get dynamic group OCID and update its matching rules
        group_ocid, result = get_resource('dynamic group', identity_client.get_dynamic_group)
        group_name = result.data.name
        click.echo('For information about dynamic group matching rule syntax, please visit https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#Writing')
        current_rule = result.data.matching_rule
        if instance_ocid in current_rule:
            default_group_rule = current_rule
        elif '{' in current_rule:
            default_group_rule = "Any " + current_rule[current_rule.index('{'):current_rule.rindex('}')] + ", instance.id = '{}'}}".format(instance_ocid)
        else:
            default_group_rule = "Any {" + current_rule + ", instance.id = '{}'}}".format(instance_ocid)
        group_rule = click.prompt('Enter the matching rule(s) you would like to set for this dynamic group', default=default_group_rule)
        ctx.invoke(identity_cli.update_dynamic_group, wait_for_state='ACTIVE', dynamic_group_id=group_ocid, matching_rule=group_rule)

        # check if the user wants to create/update a policy for this group
        if click.confirm('Do you want to create a new policy for this group?', default=False):
            new_policy = True
        else:
            new_policy = False

        if (not new_policy) and click.confirm('Do you want to update a policy for this group?', default=False):
            policy_ocid, result = get_resource('policy', identity_client.get_policy)
            click.echo('For information about policy syntax, please visit https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policysyntax.htm')
            default_policy_statement = json.dumps(result.data.statements)
            policy_statement = click.prompt('Enter the statement(s) you would like to set for this policy (please enter your statements in JSON format, as a bracket-enclosed list of strings)', default=default_policy_statement, value_proc=lambda statements: validate_statements(statements))
            ctx.invoke(identity_cli.update_policy, wait_for_state='ACTIVE', policy_id=policy_ocid, statements=policy_statement)
    else:
        # create dynamic group and add this instance to the group using a matching rule
        if config_obj:
            tenancy_ocid = config_obj['tenancy']
        else:
            tenancy_ocid, result = get_resource('tenancy', identity_client.get_tenancy)
        group_name = click.prompt('Enter a name for your new dynamic group', value_proc=lambda name: validate_resource_name(name))
        group_description = click.prompt('Enter a description for your new dynamic group')
        click.echo('For information about dynamic group matching rule syntax, please visit https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#Writing')
        default_group_rule = "Any {{instance.id = '{}'}}".format(instance_ocid)
        group_rule = click.prompt('Enter the matching rule(s) you would like to set for this dynamic group', default=default_group_rule)
        ctx.invoke(identity_cli.create_dynamic_group, wait_for_state='ACTIVE', compartment_id=tenancy_ocid, name=group_name, matching_rule=group_rule, description=group_description)

        # since this is a new group that won't have an existing policy, have the user go through policy creation flow
        new_policy = True

    if new_policy:
        # create policy for the new dynamic group
        policy_name = click.prompt('Enter a name for the new policy to be used for your new dynamic group', value_proc=lambda name: validate_resource_name(name))
        policy_description = click.prompt('Enter a description for the new policy to be used for your new dynamic group')
        click.echo('WARNING: Using the default policy at the prompt below will grant all permissions for all your OCI resources to every instance in the dynamic group. Please ensure that this is the policy you want to use. If not, you can enter your custom policy statement(s) at the prompt.')
        click.echo('For information about policy syntax, please visit https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policysyntax.htm')
        default_policy_statement = '["Allow dynamic-group {} to manage all-resources in compartment {}"]'.format(group_name, instance_compartment_name)
        policy_statement = click.prompt('Enter the statement(s) you would like to set for this policy (please enter your statements in JSON format, as a bracket-enclosed list of strings)', default=default_policy_statement, value_proc=lambda statements: validate_statements(statements))
        policy_compartment_ocid = instance_compartment_ocid
        if click.confirm('This policy is currently set to be put in compartment {}, which is the compartment that your instance is in. Do you want to create this policy in a different compartment?'.format(instance_compartment_name), default=False):
            policy_compartment_ocid, result = get_resource('compartment', identity_client.get_compartment)
        ctx.invoke(identity_cli.create_policy, wait_for_state='ACTIVE', compartment_id=policy_compartment_ocid, name=policy_name, statements=policy_statement, description=policy_description)

    click.echo('Successfully set up instance principal authentication for your instance!')
    click.echo(click.wrap_text(text=instance_principal_setup_end_message.format(compartment_id=instance_compartment_ocid, auth=OCI_CLI_AUTH_INSTANCE_PRINCIPAL), preserve_paragraphs=True))


@setup_group.command('oci-cli-rc', help="""Generates a oci_cli_rc file that can contain parameter default values and other configuration information such as command aliases and predefined queries.

This command will populate the file with some default aliases and predefined queries.
""")
@cli_util.option('--file', show_default=True, default=CLI_RC_DEFAULT_LOCATION, type=click.File(mode='a+b', lazy=True), help="The file into which default aliases and predefined queries will be loaded")
@cli_util.help_option
def setup_cli_rc(file):
    if hasattr(file, 'name') and file.name == '<stdout>':
        raise click.UsageError('This command does not support writing data to stdout')

    if not os.path.exists(file.name):
        try:
            os.makedirs(os.path.dirname(file.name))
        except OSError as exc:  # Python >2.5
            if exc.errno == errno.EEXIST:
                pass
            else:
                raise

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


def _get_default_rc_file():
    bashrc_exists = os.path.isfile(USER_BASH_RC)
    bash_profile_exists = os.path.isfile(USER_BASH_PROFILE)
    if not bashrc_exists and bash_profile_exists:
        return USER_BASH_PROFILE
    if bashrc_exists and bash_profile_exists and platform.system().lower() == 'darwin':
        return USER_BASH_PROFILE
    return USER_BASH_RC if bashrc_exists else None


class CLIInstallError(Exception):
    pass


def prompt_y_n(msg, default=None):
    if default not in [None, 'y', 'n']:
        raise ValueError("Valid values for default are 'y', 'n' or None")
    y = 'Y' if default == 'y' else 'y'
    n = 'N' if default == 'n' else 'n'

    while True:
        ans = prompt_input('{} ({}/{}): '.format(msg, y, n))
        if ans.lower() == n.lower():
            return False
        if ans.lower() == y.lower():
            return True
        if default and not ans:
            return default == y.lower()


def _default_rc_file_creation_step():
    rcfile = USER_BASH_PROFILE if platform.system().lower() == 'darwin' else USER_BASH_RC
    ans_yes = prompt_y_n('Could not automatically find a suitable file to use. Create {} now?'.format(rcfile), default='y')
    if ans_yes:
        open(rcfile, 'a').close()
        return rcfile
    return None


def get_rc_file_path():
    rc_file = None
    default_rc_file = _get_default_rc_file()
    if not default_rc_file:
        rc_file = _default_rc_file_creation_step()
    rc_file = rc_file or prompt_input_with_default('Enter a path to an rc file to update (file will be created if it does not exist)', default_rc_file)
    if rc_file:
        rc_file_path = os.path.realpath(os.path.expanduser(rc_file))
        if not os.path.isfile(rc_file_path):
            print_status("Automatically created rc file at '{}'".format(rc_file_path))
        return rc_file_path
    return None


def print_status(msg=''):
    print('-- ' + msg)


def prompt_input(msg):
    if sys.version_info >= (3, 0):
        return input('\n===> ' + msg)
    else:
        return raw_input('\n===> ' + msg)  # noqa: F821


def prompt_input_with_default(msg, default):
    if default:
        return prompt_input("{} (leave blank to use '{}'): ".format(msg, default)) or default
    else:
        return prompt_input('{}: '.format(msg))


def setup_autocomplete_non_windows():
    click.echo("To set up autocomplete, we would update few lines in rc/bash_profile file.")
    rc_file_path = get_rc_file_path()
    if not rc_file_path:
        raise CLIInstallError('No suitable profile file found.')

    # source bash completion script in CLI install directory
    script_relative_path = os.path.join('bin', 'oci_autocomplete.sh')
    path_to_install_dir = os.path.dirname(os.path.abspath(__file__))
    completion_script_file = os.path.join(path_to_install_dir, script_relative_path)
    if not os.path.exists(completion_script_file):
        click.echo('Could not locate autocomplete script at {}. Exiting script.'.format(completion_script_file))
        sys.exit(1)

    click.echo("Using tab completion script at: {}".format(completion_script_file))
    soft_link = os.path.expanduser("~/lib/oci_autocomplete.sh")
    soft_link_completion_script_file = soft_link
    bash_profile_line = '[[ -e "{soft_link_completion_script_file}" ]] && source "{soft_link_completion_script_file}"'.format(soft_link_completion_script_file=soft_link_completion_script_file)
    confirm_prompt = 'We need to add a few lines to your {rc_file_path} file. Please confirm this is ok.'.format(rc_file_path=rc_file_path)

    if click.confirm(confirm_prompt, default=True):

        if os.path.exists(soft_link):
            os.chmod(soft_link, 0o0644)
            os.remove(soft_link)
        try:
            src = completion_script_file
            dst = soft_link

            if not os.path.isdir(os.path.dirname(dst)):
                os.makedirs(os.path.dirname(dst))
            os.symlink(src, dst)
        except Exception:
            click.echo(
                "Unable to symlink ~/lib/oci_autocomplete.sh to {}. \nAdd '{}' to your rc file and restart your terminal for the changes to take effect.".format(
                    bash_profile_line, bash_profile_line))
            return

        with open(rc_file_path, mode='a+') as f:
            f.seek(0)
            content = f.read()

            # this check is not foolproof but we want to avoid adding a bunch of lines to .bash_profile/.bashrc if the user re-runs the command
            if "lib/oci_autocomplete.sh" not in content:
                f.write('\n{}\n'.format(bash_profile_line))
            else:
                click.echo("It looks like tab completion for oci is already configured in {rc_file_path}. If you want to re-run the setup command please remove the line containing 'oci_autocomplete.sh' from {rc_file_path} and run oci setup authenticate again.\n".format(rc_file_path=rc_file_path))

        click.echo("Success! \n Restart your terminal or Run '{}' for the changes to take effect.".format(bash_profile_line))
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

    cli_util.apply_user_only_access_permissions(file)


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


def write_config(filename, user_id=None, fingerprint=None, key_file=None, tenancy=None, region=None, pass_phrase=None, profile_name=DEFAULT_PROFILE_NAME, security_token_file=None, **kwargs):
    existing_file = os.path.exists(filename)
    with open(filename, 'a') as f:
        if existing_file:
            f.write('\n\n')

        f.write('[{}]\n'.format(profile_name))

        if user_id:
            f.write('user={}\n'.format(user_id))

        f.write('fingerprint={}\n'.format(fingerprint))
        f.write('key_file={}\n'.format(key_file))
        f.write('tenancy={}\n'.format(tenancy))
        f.write('region={}\n'.format(region))

        if pass_phrase:
            f.write("pass_phrase={}\n".format(pass_phrase))

        if security_token_file:
            f.write("security_token_file={}\n".format(security_token_file))

    # only user has R/W permissions to the config file
    cli_util.apply_user_only_access_permissions(filename)


def write_public_key_to_file(filename, public_key, overwrite=False, silent=False):
    if not overwrite and os.path.isfile(filename) and not click.confirm('File {} already exists, do you want to overwrite?'.format(filename)):
        return False

    with open(filename, "wb") as f:
        f.write(cli_util.serialize_key(public_key=public_key))

    # only user has R/W permissions to the key file
    cli_util.apply_user_only_access_permissions(filename)

    if not silent:
        click.echo('Public key written to: {}'.format(filename))
    return True


def write_private_key_to_file(filename, private_key, passphrase, overwrite=False, silent=False):
    if not overwrite and os.path.isfile(filename) and not click.confirm('File {} already exists, do you want to overwrite?'.format(filename)):
        return False

    with open(filename, "wb") as f:
        f.write(cli_util.serialize_key(private_key=private_key, passphrase=passphrase))

    # only user has R/W permissions to the key file
    cli_util.apply_user_only_access_permissions(filename)

    if not silent:
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
    if not (is_region(region) or is_valid_region_index(region)):
        click.echo("Unrecognized region: {}. Please enter a number between 1 to {}, or valid regions can be found here: https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm".format(region, len(REGIONS)))
        if not click.confirm("Continue with unrecognized region? (Enter 'n' to re-enter region)"):
            return None

    return region


def is_valid_region_index(region):

    return region.isdigit() and len(REGIONS) >= int(region) >= 1


def process_config_filename(filename):
    filename_expanded = os.path.expanduser(filename)
    if os.path.isdir(filename_expanded):
        raise click.BadParameter("Config location must be a filename not a directory")

    return filename_expanded


def validate_ocid(ocid, pattern):
    if not pattern.match(ocid):
        raise click.BadParameter("Invalid OCID format. Instructions to find OCIDs: https://docs.cloud.oracle.com/Content/API/Concepts/apisigningkey.htm#Other")

    return ocid


def validate_resource_ocid(ocid):
    # the link provided in the error message in the validate_ocid function is not applicable for general resource OCIDs
    # so, the validate_ocid function should not be used to validate general resource OCIDs since the link in the error message could be misleading
    pattern = re.compile("^(ocid1.)([0-9a-zA-Z-_]+.)(oc[1-3].)([0-9a-zA-Z-_]*.)([0-9a-zA-Z-_]+)$")
    if not pattern.match(ocid):
        raise click.BadParameter("Invalid OCID format. OCID syntax can be found here: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/identifiers.htm#Oracle")

    return ocid


def validate_statements(statements):
    try:
        json.loads(statements)
    except ValueError:
        raise click.BadParameter("Please enter your statements in JSON format, as a bracket-enclosed list of strings")

    return statements


def validate_resource_name(name):
    pattern = re.compile("^[a-zA-Z0-9._-]+$")
    if not pattern.match(name):
        raise click.BadParameter("Invalid resource name. The name cannot contain spaces; only letters, numerals, hyphens, periods, or underscores are allowed.")

    return name


def validate_profile_name(value, config_parser, overwrite=False, makeUpper=True):
    if not value:
        click.echo('Cannot specify blank profile name')
        return None

    sections = [section.upper() for section in config_parser.sections()]
    if config_parser['DEFAULT']:
        sections.append('DEFAULT')

    if makeUpper:
        value = value.upper()

    if value in sections and not overwrite:
        click.echo('Profile {section} already exists in config. Cannot specify a profile that conflicts with any existing profile(s): {sections}'.format(
            section=value,
            sections=', '.join(sections)
        ))
        value = None

    return value


def prompt_for_config_location():
    config_location = os.path.abspath(click.prompt('Enter a location for your config', default=os.path.join(DEFAULT_DIRECTORY, 'config'), value_proc=process_config_filename))
    if os.path.exists(config_location):
        config_parser = configparser.ConfigParser()
        try:
            config_parser.read(config_location)
            if click.confirm('Config file: {} already exists. Do you want add a profile here? (If no, you will be prompted to overwrite the file)'.format(config_location), default=True):
                profile_name = None
                while not profile_name:
                    profile_name = click.prompt('Enter the name of the profile you would like to create', value_proc=lambda value: validate_profile_name(value, config_parser))

                return (config_location, profile_name)
        except configparser.Error as e:
            pass

        if not click.confirm('File: {} already exists. Do you want to overwrite (Removes existing profiles!!!)?'.format(config_location)):
            return (None, None)

        # remove the config file, since we are in the overwrite path
        os.remove(config_location)
    else:
        dirname = os.path.dirname(config_location)

        # if user inputs only a filename (dirname=='') it implies the current directory so no need to create a dir
        if dirname and not os.path.exists(dirname):
            cli_util.create_directory(dirname)

    return (config_location, DEFAULT_PROFILE_NAME)


def prompt_session_for_profile():
    config_parser = configparser.ConfigParser()
    try:
        if not os.path.exists(DEFAULT_CONFIG_LOCATION):
            return (DEFAULT_CONFIG_LOCATION, DEFAULT_PROFILE_NAME)
        config_parser.read(DEFAULT_CONFIG_LOCATION)
        profile_name = click.prompt('Enter the name of the profile you would like to create',
                                    value_proc=lambda value: validate_profile_name(value, config_parser, True, False))
    except configparser.Error as e:
        pass

    return DEFAULT_CONFIG_LOCATION, profile_name


def prompt_for_region():
    region = None

    # CHUNK_LENGTH represents how many regions will be displayed per line
    CHUNK_LENGTH = 5
    sorted_region_list = sorted(REGIONS)
    numeric_region_list = ['{}: {}'.format(index + 1, numeric_region) for index, numeric_region in enumerate(sorted_region_list)]
    chunked_region_list = [numeric_region_list[index:index + CHUNK_LENGTH] for index in range(0, len(numeric_region_list), CHUNK_LENGTH)]
    region_list = ',\n'.join([', '.join(chunked_region) for chunked_region in chunked_region_list])
    while not region:
        region = click.prompt(text='Enter a region by index or name(e.g.\n{})'.format(region_list), value_proc=validate_region)

    return sorted_region_list[int(region) - 1] if is_valid_region_index(region) else region


def remove_profile_from_config(config_file, profile_name_to_terminate):
    # Set default_section to custom value or else we can't delete 'DEFAULT'
    # profiles since it is protected by configparser
    config = configparser.ConfigParser(default_section="")
    config.read(config_file)
    config.remove_section(profile_name_to_terminate)
    with open(config_file, 'w') as config_file_handle:
        config.write(config_file_handle)


def get_resource(resource_type, get_func):
    prompt_ocid = True
    while prompt_ocid:
        resource_ocid = click.prompt('Enter the {resource} OCID'.format(resource=resource_type), value_proc=lambda ocid: validate_resource_ocid(ocid))
        try:
            result = get_func(resource_ocid)
            prompt_ocid = False
        except exceptions.ServiceError as e:
            if e.code == 'NotAuthorizedOrNotFound':
                click.echo('Error: Could not find {resource} with the given OCID; please ensure that you have entered the correct {resource} OCID and that you are authorized to access the {resource}'.format(resource=resource_type))
            else:
                click.echo('Error: ' + e.message)
                sys.exit(1)

    return resource_ocid, result


def get_passphrase(ctx):
    try:
        client_config = cli_util.build_config(ctx.obj)
        private_key = signer.load_private_key_from_file(client_config['key_file'], client_config['pass_phrase'])
    except exceptions.ConfigFileNotFound:
        # if the user is missing a config file, they will be prompted to create one during the build_client flow, which is called later in the instance principal setup process
        # so, we don't have to handle this exception here, and can just return None as the passphrase
        return None
    except exceptions.MissingPrivateKeyPassphrase:
        # if this exception is thrown, then the client_config was built successfully, but the private key was encrypted with a passphrase that isn't in the config
        # so, we can prompt for the private key passphrase once, and then have it be returned each time this script invokes another CLI function that needs the passphrase
        # if the entered passphrase is incorrect, the script will terminate with the exception thrown by load_private_key_from_file
        passphrase = cli_util.prompt_for_passphrase()
        private_key = signer.load_private_key_from_file(client_config['key_file'], passphrase)
        return passphrase
    return None


@setup_group.command('find-installations', help="""Finds and lists locations of all default OCI CLI installs.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def find_cli_installations(ctx):

    package_locations = []
    executable_locations = []

    # check for installer script installation
    click.echo('Checking for CLI installer script default installation...')
    if os.path.exists(DEFAULT_INSTALL_DIR):
        # if the above condition is satisfied, that means the CLI package was installed at the default location from the installer script
        installation_loc = DEFAULT_INSTALL_DIR
        package_locations.append(('CLI Installer Script', installation_loc))

    # check for homebrew installation
    click.echo('Checking for Homebrew installation...')
    result = subprocess.run(['brew list'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            universal_newlines=True)
    if (result.returncode == 0) and ('oci-cli' in result.stdout):
        # if the above condition is satisfied, that means oci-cli is an installed homebrew package
        # get the oci-cli installation location
        installation_loc = []
        result = subprocess.run(['brew --cellar oci-cli'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                universal_newlines=True)
        installation_loc.append(result.stdout.strip())
        result = subprocess.run(['brew --prefix oci-cli'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                universal_newlines=True)
        installation_loc.append(result.stdout.strip())
        package_locations.append(('Homebrew', ', '.join(installation_loc)))

    # check for yum installation
    click.echo('Checking for yum installation...')
    result = subprocess.run(['yum list installed'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            universal_newlines=True)
    if (result.returncode == 0) and ('oci-cli' in result.stdout):
        # if the above condition is satisfied, that means the CLI is an installed yum package
        # CLI yum package name has the form pythonXX-oci-cli; the python version determines where the package is installed
        package_name = re.findall('python[0-9]+-oci-cli', result.stdout)
        python_version_num = re.findall('[0-9]+', package_name[0])
        python_version = '.'.join(list(python_version_num[0]))
        installation_loc = '/usr/lib/python{version}/site-packages/oci_cli'.format(version=python_version)
        package_locations.append(('yum', installation_loc))

    # check for pip installation
    click.echo('Checking for pip installation...')
    result = subprocess.run(['pip3 show oci-cli'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            universal_newlines=True)
    if result.returncode == 0:
        # if the above condition is satisfied, that means oci-cli is an installed pip package
        # parse result string to get the oci-cli installation location
        location_line = re.findall('Location: .*\n', result.stdout)
        installation_loc = os.path.join(location_line[0].split()[1], 'oci_cli')
        package_locations.append(('pip3', installation_loc))

    # check for oci executables on the user's PATH
    click.echo('Searching for CLI executables on your $PATH...')
    try:
        if 'PATH' in os.environ:
            path_env = os.environ['PATH']
            click.echo('Your current $PATH is {}'.format(path_env))
            for path in path_env.split(os.pathsep):
                search_path = os.path.join(path, '**', OCI_EXECUTABLE_NAME)
                executable_locations.extend(glob.glob(search_path, recursive=True))
        else:
            click.echo('No PATH variable found in your environment')
    except Exception as ex:
        pass
    click.echo()

    # print the installations that were found
    if len(package_locations) == 0:
        click.echo('No OCI CLI package installations were found')
    else:
        click.echo('The following OCI CLI package installations were found:\n')
        for i in range(len(package_locations)):
            click.echo('\t[{index}] {method}: {location}'.format(index=i + 1, method=package_locations[i][0],
                                                                 location=package_locations[i][1]))
    click.echo()

    # print the installations that were found
    if len(executable_locations) == 0:
        click.echo('No OCI CLI executables were found on your $PATH')
    else:
        click.echo('The following OCI CLI executables were found on your $PATH:\n')
        for i in range(len(executable_locations)):
            click.echo('\t[{index}] {location}'.format(index=i + 1, location=executable_locations[i]))

    click.echo()

    click.echo(click.wrap_text(
        text="Visit https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliuninstall.htm to uninstall OCI-CLI",
        preserve_paragraphs=True))
    find_install_note = 'PLEASE NOTE: This command lists CLI installations in default locations and CLI executables on your $PATH. There may be additional (unlisted) CLI installations at other non-default locations or CLI executables that are not on your current $PATH.'
    click.echo(click.wrap_text(text=find_install_note, preserve_paragraphs=True))

    ctx.exit()
