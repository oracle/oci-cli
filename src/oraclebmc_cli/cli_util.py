# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
import datetime
import functools
import getpass
import json
import pytz
import six
import sys
import uuid
from .formatting import render_config_errors

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

from oraclebmc import exceptions, config
from oraclebmc.core import BlockstorageClient
from oraclebmc.core import ComputeClient
from oraclebmc.core import VirtualNetworkClient
from oraclebmc.identity import IdentityClient
from oraclebmc.object_storage import ObjectStorageClient

from .version import __version__

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
            "virtual_network": VirtualNetworkClient
        }[service_name]

        try:
            client = client_class(client_config)
        except exceptions.MissingPrivateKeyPassphrase:
            client_config['pass_phrase'] = prompt_for_passphrase()
            client = client_class(client_config)

        if ctx.obj['endpoint']:
            client.base_client.endpoint = ctx.obj['endpoint']

        if ctx.obj['cert_bundle']:
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


def render_response(response):
    render(response.data, response.headers)


def render(data, headers, display_all_headers=False):
    display_dictionary = {}

    if data:
        display_dictionary["data"] = data

    if headers:
        for header in headers:
            header = header.lower()
            if header in DISPLAY_HEADERS or display_all_headers:
                display_dictionary[header] = headers.get(header, None)

    if display_dictionary:
        print(formatted_flat_dict(display_dictionary))


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
    as_dict = to_dict(model)
    return json.dumps(
        as_dict,
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
        except Exception as exception:
            if ctx.obj["debug"]:
                raise
            tpl = "{exc}: {details}"
            sys.exit(tpl.format(exc=exception.__class__.__name__, details=str(exception)))
    return wrapped_call


def parse_json_parameter(parameter_name, parameter_value, default=None):
    if parameter_value is None:
        return default

    try:
        return json.loads(parameter_value)
    except ValueError:
        sys.exit('Parameter {!r} must be in JSON format.\nFor help with formatting JSON input see our documentation here: https://docs.us-phoenix-1.oraclecloud.com/Content/API/SDKDocs/cli.htm#complexinput'.format(parameter_name))


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
help_option = click.option('-?', '--help', is_flag=True, help='Show this message and exit.', expose_value=False, is_eager=True, callback=help_callback)


'''Help option to use for groups (except for bmcs).'''
help_option_group = click.help_option('-?', '--help', help='Show this message and exit.')


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
        for param in generated_command.params[0:-1]:
            if params_to_exclude and param.name not in params_to_exclude:
                extended_func.params.insert(index, param)
                index += 1

        # last param is the '--help' and we want to make sure it stays last
        extended_func.params.append(generated_command.params[-1])

        return extended_func

    return copy_params
