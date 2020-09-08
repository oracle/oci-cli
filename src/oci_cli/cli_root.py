# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import sys
from oci.config import DEFAULT_LOCATION, DEFAULT_PROFILE
import click
import configparser
import os.path
import logging
from oci.util import Sentinel
import six
import importlib
import re
from .version import __version__
from .aliasing import parameter_alias, CommandGroupWithAlias
from . import help_text_producer
from . import cli_util

from . import cli_constants
from collections import OrderedDict
from oci._vendor import requests

# Enable WARN logging to surface important warnings attached to loading
# defaults, automatic coercion, or fallback values/endpoints that may impact
# the user's security.
#
# For example, a user can specify a region that the cli doesn't know about.  Most of
# the time this will be when new regions come out but the user doesn't update the cli.
#
# However, an unknown region could also be a mis-configured config file
# that is trying to redirect the user to a compromised endpoint.
#
# Users can increase this to DEBUG with -d, but we don't want to suppress
# important security information.
logging.basicConfig(level=logging.WARN)

OCI_CLI_AUTH_CHOICES = [cli_constants.OCI_CLI_AUTH_API_KEY, cli_constants.OCI_CLI_AUTH_INSTANCE_PRINCIPAL, cli_constants.OCI_CLI_AUTH_SESSION_TOKEN, cli_constants.OCI_CLI_AUTH_INSTANCE_OBO_USER, cli_constants.OCI_CLI_AUTH_RESOURCE_PRINCIPAL]


def eager_load_cli_rc_file(ctx, param, value):
    expanded_rc_default_location = os.path.expandvars(os.path.expanduser(cli_constants.CLI_RC_DEFAULT_LOCATION))
    expanded_rc_fallback_location = os.path.expandvars(os.path.expanduser(cli_constants.CLI_RC_FALLBACK_LOCATION))

    file_location = os.path.expandvars(os.path.expanduser(value))
    ctx.obj = {
        'canned_queries': {},
        'global_command_alias': {},
        'command_sequence_alias': {},
        'parameter_aliases': {},
        'settings': {}
    }

    # read rc file location from env variable if present.
    file_location_from_env = None
    if cli_constants.OCI_CLI_RC_FILE_ENV_VAR in os.environ:
        file_location_from_env = os.path.expandvars(os.path.expanduser(os.environ[cli_constants.OCI_CLI_RC_FILE_ENV_VAR]))

    # Try and find the configuration file. This is checked in the following order:
    #
    #   - The file which the customer specified
    #   - Read file path from OCI_CLI_RC_FILE env variable
    #   - The default location
    #   - The fallback location
    #
    # If we find the file, this function returns the expanded version of the file path for use later on.
    # Otherwise we return whatever value was originally provided to the function.
    parser_without_defaults = configparser.ConfigParser(interpolation=None, default_section=None)  # Don't use DEFAULT as the default section, so this doesn't bring in any extra stuff
    if os.path.exists(file_location):
        parser_without_defaults.read(file_location)
        populate_aliases_canned_queries_and_settings(ctx, parser_without_defaults)

        return file_location
    elif file_location_from_env and os.path.exists(file_location_from_env):
        parser_without_defaults.read(file_location_from_env)
        populate_aliases_canned_queries_and_settings(ctx, parser_without_defaults)

        return file_location_from_env
    elif os.path.exists(expanded_rc_default_location):
        parser_without_defaults.read(expanded_rc_default_location)
        populate_aliases_canned_queries_and_settings(ctx, parser_without_defaults)

        return expanded_rc_default_location
    elif os.path.exists(expanded_rc_fallback_location):
        parser_without_defaults.read(expanded_rc_fallback_location)
        populate_aliases_canned_queries_and_settings(ctx, parser_without_defaults)

        return expanded_rc_fallback_location
    else:
        return value


# Read values from env variables if value is None or default value and corresponding env variable is set.
# This is used to read region, endpoint, cert_bundle, config_file values from env variables.
def read_values_from_env(ctx, param, value):
    if not value or value == param.default:
        if param.name in cli_constants.OCI_CLI_PARAM_TO_ENV_MAP and cli_constants.OCI_CLI_PARAM_TO_ENV_MAP[param.name] in os.environ:
            return os.environ[cli_constants.OCI_CLI_PARAM_TO_ENV_MAP[param.name]]

    return value


def populate_aliases_canned_queries_and_settings(ctx, parser_without_defaults):
    populate_canned_queries(ctx, parser_without_defaults)
    populate_command_aliases(ctx, parser_without_defaults)
    populate_parameter_aliases(ctx, parser_without_defaults)
    populate_settings(ctx, parser_without_defaults)


def populate_settings(ctx, parser_without_defaults):
    raw_settings = get_section_without_defaults(parser_without_defaults, cli_constants.CLI_RC_GENERIC_SETTINGS_SECTION_NAME)

    settings = {}
    if raw_settings:
        for setting in raw_settings:
            settings[setting[0]] = setting[1]

    ctx.obj['settings'] = settings


def populate_command_aliases(ctx, parser_without_defaults):
    raw_command_aliases = get_section_without_defaults(parser_without_defaults, cli_constants.CLI_RC_COMMAND_ALIASES_SECTION_NAME)

    # Global aliases, e.g. a "ls=list" mapping would mean someone could do "compute image ls" or "os bucket ls" or "network subnet ls". These aliases
    # must be a single word only
    global_aliases = {}

    # Aliases which apply to a sequence of commands. For example "img = compute.image" means let "img" be an alias for "image" when invoked via "compute image"
    # (i.e. it makes "compute img" valid)
    command_sequenced_aliases = {}

    for alias in raw_command_aliases:
        if '.' not in alias[1]:
            global_aliases[alias[0]] = alias[1]
        else:
            split_target = alias[1].split('.')
            command_chain = ' '.join(split_target[:-1])

            if command_chain not in command_sequenced_aliases:
                command_sequenced_aliases[command_chain] = {}

            command_sequenced_aliases[command_chain][alias[0]] = split_target[-1]

    ctx.obj['global_command_alias'] = global_aliases
    ctx.obj['command_sequence_alias'] = command_sequenced_aliases


def populate_parameter_aliases(ctx, parser_without_defaults):
    raw_parameter_aliases = get_section_without_defaults(parser_without_defaults, cli_constants.CLI_RC_PARAM_ALIASES_SECTION_NAME)

    canonical_param_to_alias = {}

    for alias in raw_parameter_aliases:
        # Ignore anything that doesn't look like a parameter
        if not alias[0].startswith('-'):
            continue

        # This is because click with allow_interspersed_args=True doesn't reliably parse single dashed options of more than one word. Some combinations appear to work (e.g. -ns and
        # -bn for namespace and bucket name, respectively) but others don't. As an example, -ad for availability domain won't parse properly and -avd (actually any single dashed
        # parameter with a "v" in there) will invoke the function to print out the CLI version
        if not alias[0].startswith('--'):
            if len(alias[0]) > 2:
                click.echo(
                    click.style(
                        "Could not create an alias for {} as aliases need to be prefixed with '--' or be a single dash followed by a single letter. For example: --alias, -a".format(alias[0]), fg='red'
                    ),
                    file=sys.stderr
                )

        if alias[1] not in canonical_param_to_alias:
            canonical_param_to_alias[alias[1]] = []

        canonical_param_to_alias[alias[1]].append(alias[0])

    ctx.obj['parameter_aliases'] = canonical_param_to_alias

    parameter_alias.ALIASES = canonical_param_to_alias

    collisions = set()
    collisions.update(parameter_alias.shim_in_aliases(ctx.command))
    collisions.update(parameter_alias.add_alias_to_command_params(ctx.command.params))

    if len(collisions) > 0:
        click.echo(click.style('\n'.join(collisions), fg='red'), file=sys.stderr)


def populate_canned_queries(ctx, parser_without_defaults):
    raw_canned_queries = get_section_without_defaults(parser_without_defaults, cli_constants.CLI_RC_CANNED_QUERIES_SECTION_NAME)

    if raw_canned_queries:
        ctx.obj['canned_queries'] = dict(raw_canned_queries)
    else:
        ctx.obj['canned_queries'] = {}


def get_section_without_defaults(parser_without_defaults, section_name):
    if not parser_without_defaults.has_section(section_name):
        return []

    return parser_without_defaults.items(section_name)


def find_latest_release_info(ctx, param, value):
    if not value:
        return
    od = OrderedDict()
    version = re.search(r'^(\d+(?:\.\d+)+)*', __version__).group(1)
    try:
        response = requests.get(cli_constants.CHANGE_LOG_URL)
        # Raises stored HTTPError, if one occurred.
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        click.echo(click.style("Unable to access Github. HTTP Error : {}").format(errh))
    except requests.exceptions.ConnectionError as errc:
        click.echo(click.style("Unable to access Github. Error Connecting: {}").format(errc))
    except requests.exceptions.Timeout as errt:
        click.echo(click.style("Unable to access Github. Timeout Error: {}").format(errt))
    except requests.exceptions.RequestException as err:
        click.echo(click.style("Unable to access Github. {}").format(err))
    except Exception as e:
        click.echo(click.style("Unexpected error. {}").format(e))
    else:
        matches = re.findall(r'^(\d+(?:\.\d+)+) +- +\d{4}-\d{2}-\d{2}\r?\n((?:(?!\d+\.\d).*(?:\r?\n|$))*)', response.content.decode("utf-8"), re.M)
        for match in matches:
            od[match[0].strip()] = match[1]
        if version not in od:
            click.echo(click.style("Version {} not found".format(version), fg='red'), file=sys.stderr)
        else:
            version_up_to_date = True
            for key in od.keys():
                if key == version:
                    if version_up_to_date:
                        click.echo(click.style("Version {} is up to date with latest release".format(version)))
                    ctx.exit()
                version_up_to_date = False
                click.echo(key)
                click.echo(od[key])
    ctx.exit()


def find_latest_release_version(ctx, param, value):
    if not value:
        return
    current_version = re.search(r'^(\d+(?:\.\d+)+)*', __version__).group(1)
    exit_code = 0
    try:
        response = requests.get(cli_constants.OCI_CLI_PYPI_URL)
        # Raises stored HTTPError, if one occurred.
        response.raise_for_status()
        latest_version = response.json()['info']['version']
    except requests.exceptions.HTTPError as errh:
        click.echo(click.style("Unable to access Pypi. HTTP Error : {}").format(errh))
        exit_code = 2
    except requests.exceptions.ConnectionError as errc:
        click.echo(click.style("Unable to access Pypi. Error Connecting: {}").format(errc))
        exit_code = 2
    except requests.exceptions.Timeout as errt:
        click.echo(click.style("Unable to access Pypi. Timeout Error: {}").format(errt))
        exit_code = 2
    except requests.exceptions.RequestException as err:
        click.echo(click.style("Unable to access Pypi. {}").format(err))
        exit_code = 2
    except Exception as e:
        click.echo(click.style("Unexpected Error. {}").format(e))
        exit_code = 2
    else:
        click.echo(latest_version)
        current_version_list = [int(x) for x in current_version.split(".")]
        latest_version_list = [int(x) for x in latest_version.split(".")]
        if current_version_list < latest_version_list:
            click.echo(click.style("You are using OCI CLI version {}, however version {} is available. You should consider upgrading using"
                                   " https://docs.cloud.oracle.com/en-us/iaas/Content/API/SDKDocs/cliupgrading.htm".format(current_version, latest_version), fg='red'))
            exit_code = 1

    ctx.exit(exit_code)


@click.command(name='oci', cls=CommandGroupWithAlias, invoke_without_command=True,
               context_settings=dict(allow_interspersed_args=True, ignore_unknown_options=True),
               help="""Oracle Cloud Infrastructure command line interface, with support for Audit, Block Volume,
Compute, Database, IAM, Load Balancing, Networking, DNS, File Storage, Email Delivery and Object Storage Services.

Most commands must specify a service, followed by a resource type and then an action. For example, to list users (where
$T contains the OCID of the current tenant):

  oci iam user list --compartment-id $T

Output is in JSON format.

For information on configuration, see https://docs.cloud.oracle.com/Content/API/Concepts/sdkconfig.htm.""")
@click.version_option(__version__, '-v', '--version', message='%(version)s')
@click.option('--release-info', is_flag=True, show_default=False, callback=find_latest_release_info,
              expose_value=False, is_eager=True, help='Print latest release info. Please visit https://raw.githubusercontent.com/oracle/oci-cli/master/CHANGELOG.rst for more info')
@click.option('--latest-version', is_flag=True, show_default=False, callback=find_latest_release_version,
              expose_value=False, is_eager=True, help='Print latest release version.')
@click.option('--config-file',
              default=DEFAULT_LOCATION, show_default=True, callback=read_values_from_env,
              help='The path to the config file.')
@click.option('--profile',
              default=Sentinel(DEFAULT_PROFILE), show_default=False,
              help='The profile in the config file to load. This profile will also be used to locate any default parameter values which have been specified in the OCI CLI-specific configuration file.  [default: DEFAULT]')
@click.option('--cli-rc-file', '--defaults-file',
              default=cli_constants.CLI_RC_DEFAULT_LOCATION, show_default=True,
              is_eager=True, callback=eager_load_cli_rc_file,
              help='The path to the OCI CLI-specific configuration file, containing parameter default values and other configuration information such as command aliases and predefined queries. The --defaults-file option is deprecated and you should use the --cli-rc-file option instead.')
@click.option('--opc-request-id', '--opc-client-request-id', '--request-id', 'request_id',
              help='The request id to use for tracking the request.')
@click.option('--region', callback=read_values_from_env, help='The region to make calls against.  For a list of valid region names use the command: "oci iam region list".')
@click.option('--endpoint', callback=read_values_from_env, help='The value to use as the service endpoint, including any required API version path. For example: "https://iaas.us-phoenix-1.oracle.com/20160918". This will override the default service endpoint / API version path. Note: The --region parameter is the recommended way of targeting different regions.')
@click.option('--cert-bundle', callback=read_values_from_env, help='The full path to a CA certificate bundle to be used for SSL verification. This will override the default CA certificate bundle.')
@click.option('--output', type=click.Choice(choices=['json', 'table']), help='The output format. [Default is json]')
@click.option('--query', help="""JMESPath query [http://jmespath.org/] to run on the response JSON before output.

Queries can be entered directly on the command line or referenced from the [OCI_CLI_COMMAND_ALIASES] section of your configuration file by using the syntax query://<query_name>, for example query://get_id_and_name
""")
@click.option('--raw-output', is_flag=True, help='If the output of a given query is a single string value, this will return the string without surrounding quotes')
@click.option('--auth', type=click.Choice(choices=OCI_CLI_AUTH_CHOICES), help='The type of auth to use for the API request. By default the API key in your config file will be used.  This value can also be provided in the {auth_env_var} environment variable.'.format(auth_env_var=cli_constants.OCI_CLI_AUTH_ENV_VAR))
@click.option('--auth-purpose', help='The The auth purpose which can be used in conjunction with --auth.')
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@click.option('--no-retry', is_flag=True, help='Disable retry logic for calls to services.')
@click.option('-d', '--debug', is_flag=True, help='Show additional debug information.')
@click.option('-?', '-h', '--help', is_flag=True, help='For detailed help on the individual OCI CLI command, enter <command> --help.')
@click.pass_context
def cli(ctx, config_file, profile, defaults_file, request_id, region, endpoint, cert_bundle, output, query, raw_output, auth, auth_purpose, no_retry, generate_full_command_json_input, generate_param_json_input, debug, help):
    # Show help in any case if there are no subcommands, or if the help option
    # is used but there are subcommands, then set a flag for user later.
    if not ctx.invoked_subcommand:
        click.echo(ctx.get_help(), color=ctx.color)
        ctx.exit()

    if profile == Sentinel(DEFAULT_PROFILE):
        # if --profile is not supplied, fallback accordingly:
        #   - if OCI_CLI_PROFILE exists, use that
        #   - if default_profile is specified in oci_cli_rc then use that
        #
        # --profile cannot be specified as a regular default because we use it to determine which
        # section of the default file to read from
        if cli_constants.OCI_CLI_PROFILE_ENV_VAR in os.environ:
            profile = os.environ[cli_constants.OCI_CLI_PROFILE_ENV_VAR]
        elif 'settings' in ctx.obj and cli_constants.CLI_RC_GENERIC_SETTINGS_DEFAULT_PROFILE_KEY in ctx.obj['settings']:
            profile = ctx.obj['settings'][cli_constants.CLI_RC_GENERIC_SETTINGS_DEFAULT_PROFILE_KEY]
        else:
            profile = DEFAULT_PROFILE

    if auth is None:
        # if --auth is not supplied, fallback accordingly:
        #   - if OCI_CLI_AUTH exists, use that
        if cli_constants.OCI_CLI_AUTH_ENV_VAR in os.environ:
            if os.environ[cli_constants.OCI_CLI_AUTH_ENV_VAR] in OCI_CLI_AUTH_CHOICES:
                auth = os.environ[cli_constants.OCI_CLI_AUTH_ENV_VAR]
            else:
                raise click.BadParameter('invalid choice: {arg_value}. (choose from {choices})'.format(arg_value=os.environ[cli_constants.OCI_CLI_AUTH_ENV_VAR], choices=', '.join(OCI_CLI_AUTH_CHOICES)), param_hint='OCI_CLI_AUTH')

    initial_dict = {
        'config_file': config_file,
        'profile': profile,
        'defaults_file': defaults_file,
        'request_id': request_id,
        'region': region,
        'endpoint': endpoint,
        'cert_bundle': cert_bundle,
        'output': output,
        'query': query,
        'raw_output': raw_output,
        'generate_full_command_json_input': generate_full_command_json_input,
        'generate_param_json_input': generate_param_json_input,
        'debug': debug,
        'no_retry': no_retry,
        'auth': auth,
        'auth_purpose': auth_purpose
    }

    if not ctx.obj:
        ctx.obj = initial_dict
    else:
        ctx.obj.update(initial_dict)

    load_default_values(ctx, defaults_file, profile)

    if help:
        ctx.obj['help'] = True
        if is_top_level_help(ctx) and not cli_util.parse_boolean(ctx.obj.get('settings', {}).get(cli_constants.CLI_RC_GENERIC_SETTINGS_USE_CLICK_HELP, False)):
            help_text_producer.render_help_text(ctx, [sys.argv[1]])

    # Support inititialization for a subcommand.
    # In an "extended" file, add a mapping of the subcommand to the subcommand_init_module.
    # The subcommand_init_module can be the extended file itself or a separate module altogether.
    # The subcommand_init_module must have an init() function defined which will be called by this logic.
    # Ex: cli_util.SUBCOMMAND_TO_SERVICE_INIT_MODULE['dts'] = 'services.dts.src.oci_cli_dts.dts_service_cli_extended.py'
    try:
        subcommand_init_module_name = cli_util.SUBCOMMAND_TO_SERVICE_INIT_MODULE[ctx.invoked_subcommand]
        subcommand_init_module = importlib.import_module(subcommand_init_module_name)
        subcommand_init_module.init()
    except Exception as e:
        pass


def is_top_level_help(ctx):
    if len(sys.argv) != 3:
        return False

    top_level_command_tuples = []
    for cmd_name, cmd_obj in six.iteritems(ctx.command.commands):
        if isinstance(cmd_obj, click.Group):
            top_level_command_tuples.append((cmd_name, cmd_obj))

    for cmd_tuple in top_level_command_tuples:
        if cmd_tuple[0] == sys.argv[1] and sys.argv[2] in ['-?', '-h', '--help']:
            return True

    return False


def load_default_values(ctx, defaults_file, profile):
    file_location = os.path.expandvars(os.path.expanduser(defaults_file))
    ctx.obj['default_values_from_file'] = {}
    if os.path.exists(file_location):
        parser = configparser.ConfigParser(interpolation=None)
        parser.read(file_location)
        if profile in parser:
            ctx.obj['default_values_from_file'] = dict(parser.items(profile))
