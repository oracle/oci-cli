# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

import sys
from oci.config import DEFAULT_LOCATION
import click
import configparser
import os.path
import logging

from .version import __version__

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

BMCS_DEPRECATION_NOTICE = """WARNING: Invoking the CLI using 'bmcs' is deprecated and will be removed in future versions, starting in March 2018. To avoid interruption at that time, please move to invoking the CLI using 'oci' instead."""


@click.group(name='oci', invoke_without_command=True, context_settings=dict(allow_interspersed_args=True, ignore_unknown_options=True), help="""Oracle Cloud Infrastructure command line interface, with support for Block Volume, Compute, Database, IAM, Networking, and Object Storage Services.

Most commands must specify a service, followed by a resource type and then an action. For example, to list users (where $T contains the OCID of the current tenant):

  oci iam user list --compartment-id $T

Output is in JSON format.

For information on configuration, see https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/sdkconfig.htm.""")
@click.version_option(__version__, '-v', '--version', message='%(version)s')
@click.option('--config-file',
              default=DEFAULT_LOCATION, show_default=True,
              help='The path to the config file.')
@click.option('--profile',
              default='DEFAULT', show_default=True,
              help='The profile in the config file to load.')
@click.option('--defaults-file',
              default='~/.oci/cli-defaults', show_default=True,
              help='The path to a file containing default values for the CLI.')
@click.option('--request-id', help='The request id to use for tracking the request.')
@click.option('--region', help='The region to make calls against.  For a list of valid region names use the command: "oci iam region list".')
@click.option('--endpoint', help='The value to use as the service endpoint, including any required API version path. For example: "https://iaas.us-phoenix-1.oracle.com/20160918". This will override the default service endpoint / API version path. Note: The --region parameter is the recommended way of targeting different regions.')
@click.option('--cert-bundle', help='The full path to a CA certificate bundle to be used for SSL verification. This will override the default CA certificate bundle.')
@click.option('--output', type=click.Choice(choices=['json', 'table']), help='The output format. [Default is json]')
@click.option('--query', help='JMESPath query [http://jmespath.org/] to run on the response JSON before output.')
@click.option('-d', '--debug', is_flag=True, help='Show additional debug information.')
@click.option('-?', '-h', '--help', is_flag=True, help='Show this message and exit.')
@click.pass_context
def cli(ctx, config_file, profile, defaults_file, request_id, region, endpoint, cert_bundle, output, query, debug, help):
    if ctx.command_path == 'bmcs':
        click.echo(click.style(BMCS_DEPRECATION_NOTICE, fg='red'), file=sys.stderr)

    # Show help in any case if there are no subcommands, or if the help option
    # is used but there are subcommands, then set a flag for user later.
    if not ctx.invoked_subcommand:
        click.echo(ctx.get_help(), color=ctx.color)
        ctx.exit()

    ctx.obj = {
        'config_file': config_file,
        'profile': profile,
        'defaults_file': defaults_file,
        'request_id': request_id,
        'region': region,
        'endpoint': endpoint,
        'cert_bundle': cert_bundle,
        'output': output,
        'query': query,
        'debug': debug}

    load_default_values(ctx, defaults_file, profile)

    if help:
        ctx.obj['help'] = True


def load_default_values(ctx, defaults_file, profile):
    file_location = os.path.expandvars(os.path.expanduser(defaults_file))
    ctx.obj['default_values_from_file'] = {}

    if os.path.exists(file_location):
        parser = configparser.ConfigParser(interpolation=None)
        parser.read(file_location)

        if profile in parser:
            ctx.obj['default_values_from_file'] = dict(parser.items(profile))
