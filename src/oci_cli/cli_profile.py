# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.
#
# This software is dual-licensed to you under the Universal Permissive License
# (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl and Apache License
# 2.0 as shown at https://www.apache.org/licenses/LICENSE-2.0. You may choose
# either license.
#
# If you elect to accept the software under the Apache License, Version 2.0,
# the following applies:
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import click

from oci_cli.cli_root import cli
from oci_cli import cli_profile_util
from oci_cli import cli_util


PROFILE_GROUP_HELP = """Inspect local OCI CLI profiles."""


@cli.group('profile', help=PROFILE_GROUP_HELP)
@cli_util.help_option_group
def profile_group():
    pass


@profile_group.command('list', help="""List profiles in the effective OCI CLI config file.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_profiles(ctx):
    try:
        profiles = cli_profile_util.list_profiles(
            ctx.obj['config_file'],
            active_profile=ctx.obj['profile']
        )
    except cli_profile_util.ProfileConfigError as error:
        raise click.ClickException(str(error))

    cli_util.render(
        {'data': [format_profile_for_list(profile) for profile in profiles]},
        {},
        ctx,
        nest_data_in_data_attribute=False
    )


@profile_group.command('current', help="""Show the active profile from the effective OCI CLI config file.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def current_profile(ctx):
    try:
        profile = cli_profile_util.get_current_profile(
            ctx.obj['config_file'],
            active_profile=ctx.obj['profile']
        )
    except cli_profile_util.ProfileConfigError as error:
        raise click.ClickException(str(error))

    cli_util.render(
        {'data': format_profile_for_list(profile)},
        {},
        ctx,
        nest_data_in_data_attribute=False
    )


@profile_group.command('diagnose', help="""Diagnose local OCI CLI profile configuration.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def diagnose_profile(ctx):
    try:
        diagnosis = cli_profile_util.diagnose_profile(
            ctx.obj['config_file'],
            active_profile=ctx.obj['profile'],
            region=get_command_line_value(ctx, 'region'),
            auth=get_command_line_auth(ctx)
        )
    except cli_profile_util.ProfileConfigError as error:
        raise click.ClickException(str(error))

    cli_util.render(
        {'data': diagnosis},
        {},
        ctx,
        nest_data_in_data_attribute=False
    )


def get_command_line_auth(ctx):
    return get_command_line_value(ctx, 'auth')


def get_command_line_value(ctx, parameter_name):
    if ctx.find_root().get_parameter_source(parameter_name) == click.core.ParameterSource.COMMANDLINE:
        return ctx.obj.get(parameter_name)
    return None


def format_profile_for_list(profile):
    return {
        'active': profile['is_active'],
        'name': profile['name'],
        'config-file': profile['config_file'],
        'region': profile['region'],
        'tenancy': profile['tenancy'],
        'user': profile['user'],
        'auth-type': profile['inferred_auth_type'],
        'fingerprint': profile['fingerprint'],
        'key-file-status': get_file_status(profile['key_file']),
        'security-token-file-status': get_file_status(profile['security_token_file']),
        'delegation-token-file-status': get_file_status(profile['delegation_token_file'])
    }


def get_file_status(file_info):
    if not file_info.get('path'):
        return 'not_configured'
    if file_info.get('exists'):
        return 'present'
    return 'missing'
