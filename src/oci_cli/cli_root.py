# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from timeit import default_timer as timer

start = timer()

import sys  # noqa: E402
from oci.config import DEFAULT_LOCATION, DEFAULT_PROFILE    # noqa: E402
import click    # noqa: E402
import configparser     # noqa: E402
import os.path  # noqa: E402
import logging  # noqa: E402
from oci.util import Sentinel   # noqa: E402
import six  # noqa: E402
import importlib    # noqa: E402
import re   # noqa: E402
from oci_cli.version import __version__    # noqa: E402
from oci_cli.aliasing import parameter_alias, CommandGroupWithAlias    # noqa: E402
from oci_cli import help_text_producer    # noqa: E402
from oci_cli import cli_util  # noqa: E402

from oci_cli import cli_constants     # noqa: E402
from collections import OrderedDict     # noqa: E402
from oci._vendor import requests    # noqa: E402
from oci_cli import cli_metrics    # noqa: E402
from interactive import cli_interactive    # noqa: E402
from oci_cli.service_mapping import service_mapping    # noqa: E402

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

GENERATE_PARAM_JSON_HELP = """Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.
Example::
    oci compute instance launch --generate_param_json_input_r agent-config > example.json

    cat example.json
Output::

    {
      "areAllPluginsDisabled": true,
      "isManagementDisabled": true,
      "isMonitoringDisabled": true,
      "pluginsConfig": [
        {
          "desiredState": "string",
          "name": "string"
        },
        {
          "desiredState": "string",
          "name": "string"
        }
      ]
    }

Edit the example.json file with correct values and use it as below ::

    oci compute instance launch --agent-config file://example.json

"""
GENERATE_FULL_COMMAND_JSON_HELP = """Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.
Example::
    oci os bucket get --generate_full_command_json_input_r  > example.json
    cat example.json
Output::

    {
      "bucketName": "string",
      "fields": [
        "approximateCount|approximateSize|autoTiering"
      ],
      "ifMatch": "string",
      "ifNoneMatch": "string",
      "name": "string",
      "namespace": "string",
      "namespaceName": "string"
    }

Edit the example.json file with correct values and use it as below ::

    oci os bucket get --from-json file://example.json
"""


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
                    sys.exit()
                version_up_to_date = False
                click.echo(key)
                click.echo(od[key])
    sys.exit()


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
            click.echo(click.style("You are using OCI CLI version {}, however version {} is available. You should consider upgrading using {}".format(
                current_version, latest_version, cli_constants.UPGRADING_CLI_DOCUMENTATION), fg='red'))
            exit_code = 1

    sys.exit(exit_code)


@click.command(name='oci', cls=CommandGroupWithAlias, invoke_without_command=True,
               context_settings=dict(allow_interspersed_args=True, ignore_unknown_options=True),
               help=f"""Oracle Cloud Infrastructure command line interface, with support for Audit, Block Volume,
Compute, Database, IAM, Load Balancing, Networking, DNS, File Storage, Email Delivery and Object Storage Services.

Most commands must specify a service, followed by a resource type and then an action. For example, to list users (where
$T contains the OCID of the current tenant):

  oci iam user list --compartment-id $T

Output is in JSON format.

For information on configuration, see {cli_constants.OCI_CONFIG_DOCUMENTATION}.

Enable our interactive features to guide you through command usage:

  oci -i

For information on interactive features, see {cli_constants.INTERACTIVE_CLI_DOCUMENTATION}.""")
@click.version_option(__version__, '-v', '--version', message='%(version)s')
@click.option('--release-info', is_flag=True, show_default=False, callback=find_latest_release_info,
              expose_value=False, is_eager=True, help='Prints ChangeLog difference between current installed version and '
                                                      f'latest released version. Please visit {cli_constants.GITHUB_CHANGELOG} for more info')
@click.option('--latest-version', is_flag=True, show_default=False, callback=find_latest_release_version,
              expose_value=False, is_eager=True, help='Prints latest released version.')
@click.option('--config-file',
              default=DEFAULT_LOCATION, show_default=True, callback=read_values_from_env,
              help='The path to the config file.')
@click.option('--profile',
              default=Sentinel(DEFAULT_PROFILE), show_default=False,
              help='The profile in the config file to load. This profile will also be used to locate any default parameter values which have been specified in the OCI CLI-specific configuration file.  [default: DEFAULT]')
@click.option('--cli-rc-file', '--defaults-file',
              default=cli_constants.CLI_RC_DEFAULT_LOCATION, show_default=True,
              is_eager=True, callback=eager_load_cli_rc_file,
              help=f'''The path to the OCI CLI-specific configuration file, containing parameter default values and other configuration information such as command aliases and predefined queries.

The --defaults-file option is deprecated and you should use the --cli-rc-file option instead.

For more information about the cli configuration file, see {cli_constants.CLI_CONFIG_DOCUMENTATION}.''')
@click.option('--opc-request-id', '--opc-client-request-id', '--request-id', 'request_id',
              help='The request id to use for tracking the request.')
@click.option('--region', callback=read_values_from_env, help='The region to make calls against.  For a list of valid region names use the command: "oci iam region list".')
@click.option('--endpoint', callback=read_values_from_env, help='The value to use as the service endpoint, including any required API version path. For example: "https://iaas.us-phoenix-1.oracle.com/20160918". This will override the default service endpoint / API version path. Note: The --region parameter is the recommended way of targeting different regions.')
@click.option('--connection-timeout', 'connection_timeout', type=click.INT, callback=read_values_from_env, help='The value of the connection timeout in seconds to make establish connection from sdk to services. This will override the default connection timeout value of 10 secs. ')
@click.option('--read-timeout', 'read_timeout', type=click.INT, callback=read_values_from_env, help='The value of the read timeout in seconds to wait for service calls to send response to sdk. This will override the default read timeout value of 60 secs. ')
@click.option('--cert-bundle', callback=read_values_from_env, help='The full path to a CA certificate bundle to be used for SSL verification. This will override the default CA certificate bundle.')
@click.option('--output', type=click.Choice(choices=['json', 'table']), help='The output format. [Default is json]')
@click.option('--query', help=f"""JMESPath query [http://jmespath.org/] to run on the response JSON before output.

Queries can be entered directly on the command line or referenced from the [OCI_CLI_COMMAND_ALIASES] section of your configuration file by using the syntax query://<query_name>, for example query://get_id_and_name

For more information, see the Using Queries section at {cli_constants.INPUT_OUTPUT_DOCUMENTATION}
""")
@click.option('--raw-output', is_flag=True, help='If the output of a given query is a single string value, this will return the string without surrounding quotes')
@click.option('--auth', type=click.Choice(choices=OCI_CLI_AUTH_CHOICES), help='The type of auth to use for the API request. By default the API key in your config file will be used.  This value can also be provided in the {auth_env_var} environment variable.'.format(auth_env_var=cli_constants.OCI_CLI_AUTH_ENV_VAR))
@click.option('--auth-purpose', help='The The auth purpose which can be used in conjunction with --auth.')
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, help=GENERATE_FULL_COMMAND_JSON_HELP)
@click.option('--generate-param-json-input', is_eager=True, help=GENERATE_PARAM_JSON_HELP)
@click.option('--no-retry', is_flag=True, help='Disable retry logic for calls to services.')
@click.option('--max-retries', type=click.INT, help='Maximum number of retry calls to be made to the service. For most commands, 5 attempts will be made. For operations with binary bodies, retries are disabled')
@click.option('-d', '--debug', is_flag=True, help='Show additional debug information.')
@click.option('-i', '--cli-auto-prompt', is_flag=True, help=f'''Use the interactive features for autocompletion and quick view of command reference.

For information on interactive features, see {cli_constants.INTERACTIVE_CLI_DOCUMENTATION}.''')
@click.option('-?', '-h', '--help', is_flag=True, help='For detailed help on the individual OCI CLI command, enter <command> --help.')
@click.pass_context
def cli(ctx, config_file, profile, cli_rc_file, request_id, region, endpoint, cert_bundle, output, query, raw_output, auth, auth_purpose, no_retry, max_retries, generate_full_command_json_input, generate_param_json_input, debug, cli_auto_prompt, connection_timeout, read_timeout, help):

    if max_retries and no_retry:
        raise click.UsageError('The option --max-retries is not applicable when using the --no-retry flag.')

    # Show help in any case if there are no subcommands, or if the help option
    # is used but there are subcommands, then set a flag for user later.
    if not ctx.invoked_subcommand and not (cli_constants.OCI_CLI_AUTO_PROMPT_ENV_VAR in os.environ or cli_auto_prompt):
        echo_help(ctx)
        sys.exit()

    if str(profile) == str(Sentinel(DEFAULT_PROFILE)):
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
        'cli_rc_file': cli_rc_file,
        'request_id': request_id,
        'region': region,
        'endpoint': endpoint,
        'connection_timeout': connection_timeout,
        'read_timeout': read_timeout,
        'cert_bundle': cert_bundle,
        'output': output,
        'query': query,
        'raw_output': raw_output,
        'generate_full_command_json_input': generate_full_command_json_input,
        'generate_param_json_input': generate_param_json_input,
        'debug': debug,
        'no_retry': no_retry,
        'auth': auth,
        'auth_purpose': auth_purpose,
        'max_attempts': max_retries
    }

    if not ctx.obj:
        ctx.obj = initial_dict
    else:
        ctx.obj.update(initial_dict)

    load_default_values(ctx, cli_rc_file, profile)

    if help:
        ctx.obj['help'] = True
        if is_top_level_help(ctx) and not cli_util.parse_boolean(ctx.obj.get('settings', {}).get(cli_constants.CLI_RC_GENERIC_SETTINGS_USE_CLICK_HELP, False)):
            help_text_producer.render_help_text(ctx, [sys.argv[1]])

    cli_metrics.Metrics.update_metric("NUM_INVOCATIONS", ctx.obj['debug'])
    ctx.obj['start_time'] = start

    # Support inititialization for a subcommand.
    # In an "extended" file, add a mapping of the subcommand to the subcommand_init_module.
    # The subcommand_init_module can be the extended file itself or a separate module altogether.
    # The subcommand_init_module must have an init() function defined which will be called by this logic.
    # Ex: cli_util.SUBCOMMAND_TO_SERVICE_INIT_MODULE['dts'] = 'services.dts.src.oci_cli_dts.dts_service_cli_extended.py'
    try:
        subcommand_init_module_name = cli_util.SUBCOMMAND_TO_SERVICE_INIT_MODULE[ctx.invoked_subcommand]
        subcommand_init_module = importlib.import_module(subcommand_init_module_name)
        subcommand_init_module.init()
    except Exception:
        pass

    # Show auto prompt mode for the user
    if cli_auto_prompt_env() or cli_auto_prompt:
        cli_interactive.start_interactive_shell(ctx)
        ctx.exit()

    if ctx.obj['debug']:
        import platform
        click.echo(platform.platform())
        click.echo("System name: {}".format(platform.system()))
        click.echo("System release : {}".format(platform.release()))
        click.echo("System version: {}\n".format(platform.version()))
        for env in os.environ:
            if env in ['http_proxy', 'HTTP_PROXY', 'https_proxy', 'HTTPS_PROXY', 'no_proxy', 'NO_PROXY', 'REQUESTS_CA_BUNDLE'] or 'OCI_' in env:
                print("env {} is set".format(env))


def cli_auto_prompt_env():
    if cli_constants.OCI_CLI_AUTO_PROMPT_ENV_VAR in os.environ:
        os.environ.pop(cli_constants.OCI_CLI_AUTO_PROMPT_ENV_VAR)
        return True
    return False


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


def load_default_values(ctx, cli_rc_file, profile):
    file_location = os.path.expandvars(os.path.expanduser(cli_rc_file))
    ctx.obj['default_values_from_file'] = {}
    if os.path.exists(file_location):
        parser = configparser.ConfigParser(interpolation=None)
        parser.read(file_location)
        if profile in parser:
            ctx.obj['default_values_from_file'] = dict(parser.items(profile))


# Need to remove help for commands under root to re-add with all the service commands
# in order to keep formatting consistent.
def echo_help(ctx):
    help_text = ctx.get_help()
    help_text = re.split('(Commands:\n)', help_text, maxsplit=1)
    help_text_commands = help_text[2].split("\n")
    help_text = help_text[0] + help_text[1]
    command_list = []
    for command in help_text_commands:
        # If the service is present in servicemapping.py it should not be added in non service group
        if len(command) > 0 and command.strip().split(None, 1)[0] in service_mapping:
            continue
        else:
            command_list.append(tuple(command.strip().split(None, 1)))
    formatter = click.formatting.HelpFormatter()
    for service in sorted(service_mapping):
        command_list.append((service, service_mapping[service][1]))
    click.echo(help_text, color=ctx.color)
    with formatter.indentation():
        formatter.write_dl(command_list)
        click.echo(formatter.getvalue(), color=ctx.color)
