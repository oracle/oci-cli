# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click
from interactive.utils import parameters_to_exclude


def set_up_context(command):
    context_obj = {'canned_queries': {}, 'global_command_alias': {}, 'command_sequence_alias': {},
                   'parameter_aliases': {},
                   'settings': {}, 'config_file': 'internal_resources/config', 'default_values_from_file': {},
                   'profile': 'DEFAULT',
                   'cli_rc_file': '~/.oci/oci_cli_rc', 'request_id': None, 'region': None, 'endpoint': None,
                   'cert_bundle': None,
                   'output': 'json', 'query': None, 'raw_output': None, 'generate_full_command_json_input': None,
                   'generate_param_json_input': None, 'debug': None, 'auth': 'api_key', 'auth_purpose': None,
                   'proxy': None,
                   'no_retry': None, 'max_attempts': None, 'input_params_to_complex_types': {}, 'output_type': None,
                   'connection_timeout': None, 'read_timeout': None}
    context = click.Context(command, parent=None, info_name=command.name, obj=context_obj)
    return context


def get_expected_commands_list(root_command, current_command):
    expected_commands_list = []
    sub_commands = getattr(current_command, "commands", {})

    # command might have subcommands or might be the leaf so it has only params
    if sub_commands:
        for sub_command in sub_commands:
            expected_commands_list.append(sub_command)
    else:
        # we need subcommand parameters and global parameters excluding parameters_to_exclude list
        params = getattr(current_command, "params", {})
        for param in params:
            if param.opts[0] not in parameters_to_exclude:
                expected_commands_list.append(param.opts[0])
        top_level_params = root_command.params
        for global_param in top_level_params:
            global_param = global_param.opts[0]
            if global_param not in parameters_to_exclude:
                expected_commands_list.append(global_param)

    return expected_commands_list
