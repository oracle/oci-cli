# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
import datetime
import functools
import getpass
import jmespath
import json
import oci
import os
import os.path
import pytz
import re
import six
import sys
import uuid
from .formatting import render_config_errors
from terminaltables import AsciiTable

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

from . import cli_exceptions

from oci import exceptions, config
from oci.core import BlockstorageClient
from oci.core import ComputeClient
from oci.core import VirtualNetworkClient
from oci.identity import IdentityClient
from oci.object_storage import ObjectStorageClient
from oci.database import DatabaseClient

from .version import __version__

from . import string_utils

try:
    # PY3+
    import collections.abc as abc
except ImportError:
    # PY2
    import collections as abc

missing_attr = object()

DISPLAY_HEADERS = {
    "etag",
    "opc-next-page"
}


OVERRIDES = {
    "blockstorage_group.command_name": "bv",
    "blockstorage_group.help": "Block Volume Service",
    "compute_group.command_name": "compute",
    "compute_group.help": "Compute Service",
    "db_group.help": "Database Service",
    "db_group.command_name": "db",
    "db_node_group.command_name": "node",
    "db_system_group.command_name": "system",
    "db_system_shape_group.command_name": "system-shape",
    "db_version_group.command_name": "version",
    "get_windows_instance_initial_credentials.command_name": "get-windows-initial-creds",
    "identity_group.command_name": "iam",
    "identity_group.help": "Identity and Access Management Service",
    "virtual_network_group.command_name": "network",
    "virtual_network_group.help": "Networking Service",
    "get_console_history_content.command_name": "get-content",
    "instance_action.command_name": "action",
    "volume_backup_group.command_name": "backup"
}


GENERIC_JSON_FORMAT_HELP = """This must be provided in JSON format. See API reference for additional help."""


PARAM_LOOKUP_HEIRARCHY_TOP_LEVEL = ''


DEFAULT_FILE_CONVERT_PARAM_TRUTHY_VALUES = ['1', 'y', 't', 'yes', 'true', 'on']


def override(key, default):
    return OVERRIDES.get(key, default)


def build_client(service_name, ctx):
    client_config = build_config(ctx.obj)

    try:
        config.validate_config(client_config)
    except exceptions.InvalidConfig as bad_config:
        table = render_config_errors(bad_config)
        template = "ERROR: The config file at {config_file} is invalid:\n\n{errors}"
        sys.exit(template.format(
            config_file=ctx.obj['config_file'],
            errors=table
        ))

    # Add to ctx for later by the operations.
    ctx.obj["config"] = client_config

    # If not set by the user as part of the command, then set it to a default.
    # This value is used later by some commands.
    if not ctx.obj['request_id']:
        ctx.obj['request_id'] = str(uuid.uuid4()).replace('-', '').upper()

    # Build the client, then fix up a few properties.
    try:
        client_class = {
            "identity": IdentityClient,
            "os": ObjectStorageClient,
            "blockstorage": BlockstorageClient,
            "compute": ComputeClient,
            "database": DatabaseClient,
            "virtual_network": VirtualNetworkClient
        }[service_name]

        try:
            client = client_class(client_config)
        except exceptions.MissingPrivateKeyPassphrase:
            client_config['pass_phrase'] = prompt_for_passphrase()
            client = client_class(client_config)

        if ctx.obj['endpoint']:
            client.base_client.endpoint = ctx.obj['endpoint']

        cert_bundle = ctx.obj['cert_bundle']
        if cert_bundle:
            if not os.path.isfile(cert_bundle):
                raise click.BadParameter(param_hint='cert_bundle', message='Cannot find cert_bundle file: {}'.format(cert_bundle))

            # TODO: Update this once alternate certs are exposed in the SDK.
            client.base_client.session.verify = ctx.obj['cert_bundle']

        return client
    except exceptions.InvalidPrivateKey as bad_key:
        sys.exit(str(bad_key))


def prompt_for_passphrase():
    return getpass.getpass('Private key passphrase:')


def build_config(command_args):
    """Load the config object from file, and apply any overrides found in command_args."""

    try:
        client_config = config.from_file(file_location=command_args['config_file'], profile_name=command_args['profile'])
    except exceptions.ConfigFileNotFound as e:
        sys.exit("ERROR: " + str(e))
    except exceptions.ProfileNotFound as e:
        sys.exit("ERROR: " + str(e))

    client_config["additional_user_agent"] = 'Oracle-PythonCLI/{}'.format(__version__)

    if command_args['region']:
        client_config["region"] = command_args['region']

    if command_args['debug']:
        client_config["log_requests"] = True

    if command_args['endpoint']:
        # The SDK does support endpoint in the config, and uses that when validating during client creation.
        # However, when the config is validated prior to creation, the endpoint is not factored in, and
        # for that we need to make the region not required if the endpoint is provided.
        client_config["endpoint"] = command_args['endpoint']
        if "region" in config.REQUIRED:
            config.REQUIRED.remove("region")
    else:
        # Do not allow an endpoint to be set in the config file. (This can be removed
        # once the SDK removes support for this.)
        client_config.pop("endpoint", None)

    return client_config


def render_response(response, ctx):
    render(response.data, response.headers, ctx)


def render(data, headers, ctx, display_all_headers=False):
    display_dictionary = {}

    if data:
        display_dictionary["data"] = to_dict(data)

    expression = None
    if ctx.obj['query']:
        search_path = ctx.obj['query']
        expression = jmespath.compile(search_path)

    if headers:
        for header in headers:
            header = header.lower()
            if header in DISPLAY_HEADERS or display_all_headers:
                display_dictionary[header] = headers.get(header, None)

    if display_dictionary:
        display_data = display_dictionary
        if expression:
            display_data = expression.search(display_dictionary)
            if not display_data:
                click.echo("Query returned empty result, no output to show.", file=sys.stderr)
                return

        if ctx.obj['output'] == "json":
            print(pretty_print_format(display_data))
        elif ctx.obj['output'] == 'table':
            table_data = display_data

            # By default our JSON responses contain a nested field called 'data' with the relevant response data
            # we want to create a table based on this data and NOT the top level response object
            # If there is a query run on the output, we will attempt to render the JSON resulting from the query
            # directly as a table
            if 'data' in display_data and not expression:
                table_data = display_data['data']

            print_table(table_data)

            # if there were any additional headers in the response, print them out here, below the table
            # if there is no 'data' in the display dictionary (i.e. oci os object put) then all we have is headers
            # and we can output those in table format, so no need to duplicate printing them here
            if 'data' in display_dictionary:
                for key in display_dictionary:
                    if key is not 'data':
                        click.echo('{}: {}'.format(key, display_dictionary[key]), file=sys.stderr)


def print_table(data):
    table_data = []

    if isinstance(data, six.string_types):
        # if data is just a raw string, hard code the column header to 'Column1'
        table_data.append(['Column1'])
        table_data.append([data])
    elif isinstance(data, list):
        if len(data) == 0:
            click.echo("Command returned empty list, no table to display.")
            return

        if isinstance(data[0], six.string_types):
            # handle strings so they dont get handled as a list below
            table_data = [["Column1"]]
            for row in data:
                table_data.append([row])
        elif isinstance(data[0], abc.Mapping):
            column_headers = build_table_headers(data)
            table_data.append(column_headers)

            for item in data:
                item = to_dict(item)
                table_data.append([item[key] for key in column_headers])
        elif isinstance(data[0], list):
            table_data = data

            headers = ["Column{}".format(col_number) for col_number in range(1, len(data[0]) + 1)]
            table_data.insert(0, headers)
        else:
            # some other primitive
            table_data = [["Column1"]]
            for row in data:
                table_data.append([row])

    elif isinstance(data, dict):
        column_headers = build_table_headers(data)
        table_data.append(column_headers)

        table_data.append([data[key] for key in column_headers])
    else:
        click.echo("Table format not supported for operation return type: {}".format(data))
        return

    print(AsciiTable(table_data).table)


def build_table_headers(data):
    # data is either a list of dicts or a dict
    # we can build the column headers from all keys on all objects (de-duped)
    cols = set()
    if isinstance(data, list):
        for entry in data:
            for key in entry.keys():
                cols.add(key)
        return sorted(list(cols))
    else:
        return sorted(list(data.keys()))


def to_dict(obj):
    """Helper to flatten models into dicts for rendering.

    The following conversions are applied:
        * datetime.date, datetime.datetime, datetime.time
          are converted into ISO8601 UTC strings
        * Underscores are replaced by hyphens in dictionary
          key only.
    """
    # Shortcut strings so they don't count as Iterables
    if isinstance(obj, six.string_types):
        return obj
    elif isinstance(obj, (datetime.datetime, datetime.time)):
        # always use UTC
        if not obj.tzinfo:
            obj = pytz.utc.localize(obj)
        if isinstance(obj, datetime.datetime):
            # only datetime.datetime takes a separator
            return obj.isoformat(sep="T")
        return obj.isoformat()
    elif isinstance(obj, datetime.date):
        # datetime.date doesn't have a timezone
        return obj.isoformat()
    elif isinstance(obj, abc.Mapping):
        return {k: to_dict(v) for k, v in six.iteritems(obj)}
    elif isinstance(obj, abc.Iterable):
        return [to_dict(v) for v in obj]
    # Not a string, datetime, dict, list, or model - return directly
    elif not hasattr(obj, "swagger_types"):
        return obj

    # Collect attrs from obj according to swagger_types into a dict
    as_dict = {}
    for key in six.iterkeys(obj.swagger_types):
        value = getattr(obj, key, missing_attr)
        if value is not missing_attr:
            key = key.replace("_", "-")
            as_dict[key] = to_dict(value)
    return as_dict


def formatted_flat_dict(model):
    """Returns a string of the model flattened as a dict, sorted"""
    return pretty_print_format(to_dict(model))


def pretty_print_format(d):
    return json.dumps(
        d,
        indent=2,
        sort_keys=True
    )


def wrap_exceptions(func):
    @functools.wraps(func)
    def wrapped_call(ctx, *args, **kwargs):
        try:
            func(ctx, *args, **kwargs)
        except exceptions.ServiceError as exception:
            if ctx.obj["debug"]:
                raise
            tpl = "{exc}:\n{details}"
            details = json.dumps(exception.args[0], indent=4, sort_keys=True)
            sys.exit(tpl.format(exc=exception.__class__.__name__, details=details))
        except cli_exceptions.RequiredValueNotInDefaultOrUserInputError as exception:
            if ctx.obj["debug"]:
                raise
            tpl = "{usage}\n\nError: {details}"
            sys.exit(tpl.format(usage=ctx.get_usage(), details=str(exception)))
        except Exception as exception:
            if ctx.obj["debug"]:
                raise
            tpl = "{exc}: {details}"
            sys.exit(tpl.format(exc=exception.__class__.__name__, details=str(exception)))
    return wrapped_call


def parse_json_parameter(parameter_name, parameter_value, default=None, camelize_keys=True):
    if parameter_value is None:
        return default

    # Can't parse something which isn't a string, so just return it as-is. We'd hit this flow if we had already
    # pre-parsed the data, such as when we provide the input via --from-json, since that already parses out the JSON
    if not isinstance(parameter_value, six.string_types):
        return parameter_value

    # Try to load from a file first. If we couldn't (e.g. because the parameter didn't specify a file) then
    # just try to load the parameter_value raw
    json_to_parse = load_file_contents(parameter_value)
    if json_to_parse is None:
        json_to_parse = parameter_value

    try:
        if camelize_keys:
            return make_dict_keys_camel_case(json.loads(json_to_parse), parameter_name)
        else:
            return json.loads(json_to_parse)
    except ValueError:
        sys.exit('Parameter {!r} must be in JSON format.\nFor help with formatting JSON input see our documentation here: https://docs.us-phoenix-1.oraclecloud.com/Content/API/SDKDocs/cli.htm#complexinput'.format(parameter_name))


# Takes a dictionary representing a JSON object and converts keys into their camelized form. This will do a deep conversion - for example if a value in the dictionary is a dictionary itself
# then we will convert the value's keys to camel case and so on.
#
# There is different handling depending on what kind of data we're provided in original_obj:
#
#    - If it is a string or a primitive type return it as is (primitive here is taken as not a map and not iterable)
#    - If it is a known type (e.g. it is really a class like EgressSecurityRule) then camelize its keys and do a deep conversion
#    - If it is a dictionary of string to <something> then do not convert the keys to camel case but still do a deep conversion of the <something>
#        - The reason for this is that if the key is arbitrary, we take it to be user input and so we don't want to mangle it
#    - If it is a list then convert each element in the list. For this, we need to know the type of each element. We also assume uniform types in the list
#      rather than the list containing different types.
#    - If it is an unknown type, then do nothing to its keys
#
# In order to identify the types we're dealing with, we use the following parameters:
#
#    - complex_parameter_type explicitly states the type and is always honoured if present
#    - parameter_name can be used to look up the type from the metadata of (complex) types against each command. This metadata is decorated via
#      @json_skeleton_utils.json_skeleton_wrapper_metadata on each command
def make_dict_keys_camel_case(original_obj, parameter_name=None, complex_parameter_type=None):
    if isinstance(original_obj, six.string_types):
        return original_obj

    if not isinstance(original_obj, abc.Mapping) and not isinstance(original_obj, abc.Iterable):
        # Either a primitive or something we don't know how to deal with...given the entry point (from the output of
        # json.loads, which should be a dict) more likely a primitive
        return original_obj

    # We expect this to be a dictionary of {'module':'<module name>', 'class':'<class name>'} to match what we get from
    # the @json_skeleton_utils.json_skeleton_wrapper_metadata decorator
    if complex_parameter_type:
        complex_type_definition = complex_parameter_type
    else:
        complex_type_definition = get_complex_type_definition_for_key_camelization(parameter_name)

    if isinstance(original_obj, abc.Mapping):
        camelize_keys = True
        if complex_type_definition:
            class_name = complex_type_definition['class']
            if class_name.find("dict(str,") == 0 or class_name not in MODULE_TO_TYPE_MAPPINGS[complex_type_definition['module']]:
                # If the parameter is a dict of string --> <something>, then the keys are things which the customer provides and so we don't
                # want to reinterpret them.
                #
                # If we don't know recognize type, don't try and do anything
                camelize_keys = False

        new_dict = {}
        for key, value in six.iteritems(original_obj):
            camelized_key = string_utils.camelize(key)

            # Figure out what the type of "value" is so that we can pass it to the next call to this method. The different cases are:
            #
            #    - We don't know (or don't need to worry about) the type, so pass nothing. An example of this would be primitives
            #    - The current type we're dealing with is a dictionary, so just figure out what the value part of the dictionary is
            #    - The current type we're dealing with is a complex type, so figure out what attribute we're on and what the attribute's data type is
            param_type_to_pass = None
            if complex_type_definition:
                if complex_type_definition['class'].find("dict(") == 0:
                    param_type_to_pass = {
                        'module': complex_type_definition['module'],
                        'class': re.match('dict\(([^,]*), (.*)\)', complex_type_definition['class']).group(2)
                    }
                elif complex_type_definition['class'] not in MODULE_TO_TYPE_MAPPINGS[complex_type_definition['module']]:
                    param_type_to_pass = complex_type_definition
                else:
                    cls_type = MODULE_TO_TYPE_MAPPINGS[complex_type_definition['module']][complex_type_definition['class']]
                    instance = cls_type()
                    for underscored_name, camelized_name in instance.attribute_map.items():
                        if camelized_key == camelized_name:
                            param_type_to_pass = {
                                'module': complex_type_definition['module'],
                                'class': instance.swagger_types[underscored_name]
                            }
                            break

            if camelize_keys:
                new_dict[camelized_key] = make_dict_keys_camel_case(value, parameter_name=key, complex_parameter_type=param_type_to_pass)
            else:
                new_dict[key] = make_dict_keys_camel_case(value, parameter_name=key, complex_parameter_type=param_type_to_pass)

        return new_dict

    if isinstance(original_obj, abc.Iterable):
        new_list = []
        list_type = None
        if complex_type_definition and complex_type_definition['class'].find('list[') == 0:
            list_type = {'module': complex_type_definition['module'], 'class': re.match('list\[(.*)\]', complex_type_definition['class']).group(1)}

        for obj in original_obj:
            new_list.append(make_dict_keys_camel_case(obj, complex_parameter_type=list_type))

        return new_list


MODULE_TO_TYPE_MAPPINGS = {
    'core': oci.core.models.core_type_mapping,
    'database': oci.database.models.database_type_mapping,
    'identity': oci.identity.models.identity_type_mapping,
    'load_balancer': oci.load_balancer.models.load_balancer_type_mapping,
    'object_storage': oci.object_storage.models.object_storage_type_mapping
}


# If type information has been written to metadata (e.g. the operation is decorated with @json_skeleton_utils.json_skeleton_wrapper_metadata), then retrieve it
# so that we can use it as part of key camelization when parsing a JSON object.
#
# This method will return:
#
#    - None if provided none or if we could not find a complex type definition in the metadata (this is possible if its a primitive)
#    - The definition of the complex type. The options are:
#         - The name of a type (e.g. EgressSecurityRule)
#         - list[X] where X could be primitive or complex (complex here includes another list, a dict, as well as a typed object)
#         - dict(Y,Z). We assume Y will be primitive (most likely a string) but Z could be primitive or complex (complex here includes another list, a dict, as well as a typed object)
def get_complex_type_definition_for_key_camelization(parameter_name, ctx=None):
    if parameter_name is None:
        return None

    if not ctx:
        current_context = click.get_current_context(silent=True)
    else:
        current_context = ctx

    complex_type_definitions = None
    if current_context and current_context.obj:
        if 'input_params_to_complex_types' in current_context.obj:
            complex_type_definitions = current_context.obj['input_params_to_complex_types']

    if not complex_type_definitions:
        return None

    camelized_param_name = string_utils.camelize(parameter_name)
    for key in complex_type_definitions:
        if string_utils.camelize(key) == camelized_param_name:
            return complex_type_definitions[key]

    return None


def get_param(command, param_name):
    for param in command.params:
        if param.name == param_name:
            return param

    raise RuntimeError('Could not find param {!r}.'.format(param_name))


def update_param_help(command, param_name, updated_help, append=False, example=None):
    """Update help for the given parameter and command, either by replacing or adding to existing help."""
    param = get_param(command, param_name)

    if append and len(param.help) > 0:
        updated_help = param.help + " " + updated_help

    if example:
        updated_help = """{help}

Example: {example}""".format(help=updated_help, example=example)

    param.help = updated_help


def collect_commands(command):
    """Returns a list of leaf commands under the given command."""
    if not hasattr(command, "commands"):
        yield command
    else:
        for _, subcommand in six.iteritems(command.commands):
            for descendent in collect_commands(subcommand):
                yield descendent


def filter_object_headers(headers, whitelist):
    """Filter headers based on the whitelist."""
    whitelist = [x.lower() for x in whitelist]
    return {h.lower(): v for h, v in six.iteritems(headers) if h.lower() in whitelist}


def help_callback(ctx, param, value):
    if ctx.obj.get("help", False):
        click.echo(ctx.get_help(), color=ctx.color)
        ctx.exit()


'''Help option to use for commands.'''
help_option = click.option('-?', '-h', '--help', is_flag=True, help='Show this message and exit.', expose_value=False, is_eager=True, callback=help_callback)


'''Help option to use for groups (except for oci).'''
help_option_group = click.help_option('-?', '-h', '--help', help='Show this message and exit.')


def confirmation_callback(ctx, param, value):
    if not value:
        ctx.abort()


confirm_delete_option = click.option(
    '--force',
    is_flag=True,
    callback=confirmation_callback,
    expose_value=False,
    help="Perform deletion without prompting for confirmation.",
    prompt="Are you sure you want to delete this resource?")


def generate_key(key_size=2048):
    return rsa.generate_private_key(public_exponent=65537, key_size=key_size, backend=default_backend())


def serialize_key(private_key=None, public_key=None, passphrase=None):
    """
    >>> private_key = generate_key(2048)
    >>> public_key = private_key.public()
    >>> serialize_key(public_key=public_key)
    >>> serialize_key(private_key=private_key)
    """

    if private_key:
        if passphrase:
            if isinstance(passphrase, six.string_types):
                passphrase = passphrase.encode("ascii")
            encryption_algorithm = serialization.BestAvailableEncryption(passphrase)
        else:
            encryption_algorithm = serialization.NoEncryption()
        return private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=encryption_algorithm)
    else:
        return public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo)


def copy_params_from_generated_command(generated_command, params_to_exclude):
    def copy_params(extended_func):
        index = 0
        for param in generated_command.params[0:-2]:
            if params_to_exclude and param.name not in params_to_exclude:
                extended_func.params.insert(index, param)
                index += 1

        # last two params params are the '--from-json' and '--help' params and we want to make sure they stay last
        extended_func.params.append(generated_command.params[-2])
        extended_func.params.append(generated_command.params[-1])

        return extended_func

    return copy_params


def load_file_contents(path):
    file_contents = None
    if isinstance(path, six.string_types):
        for prefix, function_spec in FILE_LOAD_PREFIX_MAP.items():
            if path.startswith(prefix):
                function, kwargs = function_spec
                file_contents = function(prefix, path, **kwargs)

    return file_contents


def get_file(prefix, path, mode):
    file_path = os.path.expandvars(os.path.expanduser(path[len(prefix):]))

    if not os.path.exists(file_path):
        sys.exit("The specified file '{}' did not exist  (Resolved to path: '{}')".format(path, file_path))

    with open(file_path, mode) as f:
        return f.read()


FILE_LOAD_PREFIX_MAP = {
    'file://': (get_file, {'mode': 'r'})
}


def load_context_obj_values_from_defaults_decorator(func):
    @functools.wraps(func)
    def wrapped_call(ctx, *args, **kwargs):
        load_context_obj_values_from_defaults(ctx)
        func(ctx, *args, **kwargs)

    return wrapped_call


# For the context object, load in shared/commond values (e.g. region, debug) from the default values file if they exist there and the
# shared/common values have not been previously set.
#
# This method assumes that the context object has already had any explicit values set (e.g. in cli_root). Any explicitly set (taken here as not None)
# values will not be overwritten.
def load_context_obj_values_from_defaults(ctx):
    populate_dict_key_with_default_value(ctx, 'region', click.STRING)
    populate_dict_key_with_default_value(ctx, 'endpoint', click.STRING)
    populate_dict_key_with_default_value(ctx, 'cert_bundle', click.STRING, param_name='cert-bundle')
    populate_dict_key_with_default_value(ctx, 'output', click.STRING)
    populate_dict_key_with_default_value(ctx, 'query', click.STRING)

    if ctx.obj['output'] is None:
        ctx.obj['output'] = 'json'

    if 'debug' in ctx.obj:
        if not ctx.obj['debug']:
            # False for debug means not provided, so just load it if there is a default value. If there's nothing there, then this'll be
            # None, which is still false-y
            ctx.obj['debug'] = get_default_value_from_defaults_file(ctx, 'debug', click.BOOL, False)
    else:
        populate_dict_key_with_default_value(ctx, 'debug', click.BOOL)


def populate_dict_key_with_default_value(ctx, key, param_type, param_name=None, param_takes_multiple=False):
    if param_name:
        param_name_to_use = param_name
    else:
        param_name_to_use = key

    if key in ctx.obj:
        ctx.obj[key] = coalesce_provided_and_default_value(ctx, param_name_to_use, ctx.obj[key], False)
    else:
        value_from_default = get_default_value_from_defaults_file(ctx, param_name_to_use, param_type, param_takes_multiple)
        if value_from_default is not None:
            ctx.obj[key] = value_from_default


def coalesce_provided_and_default_value(ctx, param_name, original_value, is_required):
    # Grab the parameter so we can inspect its definition and types later as needed
    param_from_context = get_param_from_click_context(ctx, param_name)
    param_type = None
    param_takes_multiple = False
    if param_from_context:
        param_type = param_from_context.type
        param_takes_multiple = param_from_context.multiple

    # Special case handling: switches
    # ===============================
    # We have single option switches (set using is_flag=True) that when not set will provide their default value.
    # In this case, if we get the default value for the switch AND we have something in the defaults file, honour
    # what was in the defaults file
    flag_param = None
    if param_from_context and param_from_context.is_flag and len(param_from_context.secondary_opts) == 0:  # We found the parameter AND it is a flag AND it is single option
        flag_param = param_from_context
    if flag_param:
        if original_value == flag_param.default:
            from_default_file = get_default_value_from_defaults_file(ctx, param_name, click.BOOL, param_takes_multiple)  # Flags are booleans
            if from_default_file is None:
                return original_value
            else:
                return from_default_file
        else:
            return original_value

    # The logic here:
    #
    #   - If an explicit value was provided for the parameter then use it
    #   - If no explicit value was provided, find a default and use it
    #   - If no default exists, return None. However, if the parameter is also required then
    #     throw an error instead
    #
    # We have special handling for multiple parameters as these come out as empty (if nothing is provided) rather than
    # None. If the parameter was actually an empty list, that's OK as the function we call - get_default_value_from_defaults_file - will
    # return an empty list if there is no default value present
    if param_takes_multiple:
        if original_value:
            return original_value
    else:
        if original_value is not None:
            return original_value

    value_from_defaults_file = get_default_value_from_defaults_file(ctx, param_name, param_type, param_takes_multiple)
    if value_from_defaults_file is not None:
        return value_from_defaults_file

    if is_required:
        raise cli_exceptions.RequiredValueNotInDefaultOrUserInputError('Missing option "--{}".'.format(param_name))

    return None


def get_param_from_click_context(ctx, param_name):
    for param in ctx.command.params:
        long_param_name = '--{}'.format(param_name)
        if long_param_name in param.opts:
            return param

    return None


def get_default_value_from_defaults_file(ctx, param_name, param_type, param_takes_multiple):
    if 'parameter_lookup_heirarchy' not in ctx.obj:
        ctx.obj['parameter_lookup_heirarchy'] = get_param_lookup_heirarchy_from_context(ctx)

    parameter_lookup_heirarchy = ctx.obj['parameter_lookup_heirarchy']

    for heirarchy_entry in parameter_lookup_heirarchy:
        if heirarchy_entry == PARAM_LOOKUP_HEIRARCHY_TOP_LEVEL:
            target_key = param_name
        else:
            target_key = heirarchy_entry + "." + param_name

        if target_key in ctx.obj['default_values_from_file']:
            return convert_value_from_param_type(ctx.obj['default_values_from_file'][target_key], param_type, param_takes_multiple)

    return None


def convert_value_from_param_type(value, param_type, param_takes_multiple):
    if value is None:
        return value

    # Expansion only really makes sense for strings
    if isinstance(value, six.string_types):
        expanded_value = os.path.expandvars(value)
    else:
        expanded_value = value

    if param_takes_multiple:
        return convert_value_from_param_type_accepting_multiple(expanded_value, param_type)

    if param_type is None:
        return expanded_value
    elif param_type == click.STRING:
        return str(expanded_value)
    elif param_type == click.BOOL:
        # This is taken from what distutils considers to parse to True
        return str(expanded_value).lower() in DEFAULT_FILE_CONVERT_PARAM_TRUTHY_VALUES
    elif param_type == click.FLOAT:
        return float(expanded_value)
    elif param_type == click.INT:
        return int(expanded_value)
    else:
        return expanded_value


def convert_value_from_param_type_accepting_multiple(value, param_type):
    # Since our splitting into multiples relies on a string split, we can't do anything if it's
    # not a string
    if not isinstance(value, six.string_types):
        if isinstance(value, abc.Iterable):
            return value
        else:
            return [value]

    split_param = value.splitlines()
    converted_values = []

    for sp in split_param:
        stripped_val = sp.strip()
        if stripped_val:
            if param_type is None or param_type == click.STRING:
                converted_values.append(stripped_val)
            elif param_type == click.BOOL:
                converted_values.append(
                    stripped_val.lower() in DEFAULT_FILE_CONVERT_PARAM_TRUTHY_VALUES
                )
            elif param_type == click.FLOAT:
                converted_values.append(float(stripped_val))
            elif param_type == click.INT:
                converted_values.append(int(stripped_val))
            else:
                converted_values.append(stripped_val)

    return converted_values


def get_param_lookup_heirarchy_from_context(ctx):
    # This will eventually hold the call chain like: ['', 'compute' ,'image', 'export', 'to-object']
    ordered_command_chain = []

    parent = ctx.parent
    while parent is not None:
        if parent.parent is not None:
            ordered_command_chain.append(parent.info_name)
        else:
            # Append a top level item so that we can handle globally set defaults
            ordered_command_chain.append(PARAM_LOOKUP_HEIRARCHY_TOP_LEVEL)

        parent = parent.parent

    # At this point we have the chain (without the command that was actually invoked) but in the reverse
    # order like: ['export', 'image', 'compute', ''] so we want to reverse it and then put in the
    # name of the command which was actually invoked to give us the chain in the right order
    ordered_command_chain.reverse()
    ordered_command_chain.append(ctx.info_name)

    # Now that we have the call chain, we want to form the list of keys to check in the default values
    # config, in the right order to check them in (most specific to least specific). For example:
    #
    #    compute.image.export.to-object
    #    compute.image.export
    #    compute.image
    #    compute
    #    <top level> (possibly an empty string)

    parameter_lookup_heirarchy = []
    prefix = ordered_command_chain[0]
    ordered_command_chain.pop(0)
    parameter_lookup_heirarchy.append(prefix)

    for command_name in ordered_command_chain:
        if prefix == PARAM_LOOKUP_HEIRARCHY_TOP_LEVEL:
            prefix = command_name
        else:
            prefix = prefix + "." + command_name
        parameter_lookup_heirarchy.append(prefix)

    parameter_lookup_heirarchy.reverse()
    return parameter_lookup_heirarchy


# This method is intended for commands which read data from a file and where the user has not provided the data on the
# command line. In this case, we will try and see if a path is defined in the default values file and, if so, we'll open
# the file given by that path
def get_click_file_from_default_values_file(ctx, param_name, file_open_mode, is_required):
    path_from_default_file = coalesce_provided_and_default_value(ctx, param_name, None, is_required)

    if path_from_default_file:
        click_file_type = click.File(file_open_mode)
        return click_file_type.convert(path_from_default_file, None, ctx)

    return None


def override_option_help(command, option_name, help_override):
    option = next(option for option in command.params if option.name == option_name)
    option.help = help_override
