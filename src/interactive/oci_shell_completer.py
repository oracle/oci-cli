# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from prompt_toolkit.completion import Completer, Completion
from interactive.oci_resources_completions import get_oci_resources
import collections
import shlex
from oci_cli import dynamic_loader
from oci_cli.service_mapping import service_mapping
from interactive.utils import parameters_to_exclude, styles_dict
from interactive.error_messages import get_error_message


# This function looks for matching closing quotes when there is a space in parameter value such as --display-name.
# for example, this function will return true for  "harsh's instance" and will return false "harsh's instance'
def is_matching_quotes(s):
    quote_type = "'" if s.startswith("'") else '"'
    if len(s) <= 1:
        return False
    for c in s[1:]:
        if c == quote_type:
            return True
    return False


class OciShellCompleter(Completer):
    def __init__(self, ctx, colors_enabled=True, bottom_toolbar=None):
        self.ctx = ctx
        self.top_level_params = ctx.command.params
        self.top_level_params.sort(key=lambda param: param.name)
        self.top_level_commands = self.get_top_level_commands()
        self.colors_enabled = colors_enabled
        self.bottom_toolbar = bottom_toolbar
        self.list_of_required_params = (
            set()
        )  # used in key_binding to know set of all required params

    def get_top_level_commands(self):
        top_level_commands = {}
        initial_oci_commands = getattr(self.ctx.command, "commands", {})

        for cmd_name, cmd_object in initial_oci_commands.items():
            top_level_commands[cmd_name] = cmd_object.help

        for service in service_mapping:
            top_level_commands[service] = service_mapping[service][1]

        top_level_commands = collections.OrderedDict(sorted(top_level_commands.items()))
        return top_level_commands

    def add_completion(
        self,
        token,
        name,
        word_before_cursor,
        style="",
        display_meta="",
        required_field=False,
    ):
        if token.strip() == "" or name.startswith(token):
            return Completion(
                name,
                -len(word_before_cursor),
                style=style,
                display_meta=display_meta,
                display=name + " (*)" if required_field else name,
            )
        else:
            return None

    def get_required_and_optional_params(self, params):
        req_params = [
            param
            for param in filter(
                lambda param: param.help.endswith(" [required]"), params
            )
        ]
        opt_params = [
            param for param in filter(lambda param: param not in req_params, params)
        ] + self.top_level_params
        req_params.sort(key=lambda param: param.name)
        opt_params.sort(key=lambda param: param.name)

        return req_params, opt_params

    def get_list_of_req_param(self, command):
        req_params, opt_params = self.get_required_and_optional_params(command.params)
        for param in req_params:
            param_name = param.opts[0]
            # convert list to tuple(param.opts) because set needs hashable type
            self.list_of_required_params.add(tuple(param.opts))

    def append_parameter_completions(
        self,
        command,
        word_before_cursor,
        token,
        already_chosen_parameters=set(),
        remaing_sub_string="",
    ):
        completions = []

        req_params, opt_params = self.get_required_and_optional_params(command.params)
        for param in req_params:
            param_name = param.opts[0]
            if (
                param_name in already_chosen_parameters
                or remaing_sub_string not in param_name
            ):
                continue
            completion = self.add_completion(
                token,
                param.opts[0],
                word_before_cursor,
                styles_dict["required-parameter"] if self.colors_enabled else "",
                display_meta=param.help,
                required_field=True,
            )
            if completion:
                completions.append(completion)
        for param in opt_params:
            param_name = param.opts[0]
            if (
                param_name in already_chosen_parameters
                or param_name in parameters_to_exclude
                or remaing_sub_string not in param_name
            ):
                continue
            completion = self.add_completion(
                token,
                param.opts[0],
                word_before_cursor,
                display_meta=param.help,
            )
            if completion:
                completions.append(completion)

        return completions

    def append_command_completions(
        self, sorted_sub_commands, word_before_cursor, token
    ):
        completions = []
        for tlp in sorted_sub_commands:
            completion = self.add_completion(
                token,
                tlp,
                word_before_cursor,
                "",
                display_meta=sorted_sub_commands[tlp].help,
            )
            if completion:
                completions.append(completion)
        return completions

    def append_top_level_command_completions(self, word_before_cursor, token):
        completions = []
        for cmd_name, cmd_help in self.top_level_commands.items():
            completion = self.add_completion(
                token, cmd_name, word_before_cursor, "", display_meta=cmd_help
            )
            if completion:
                completions.append(completion)
        return completions

    def list_all_parameter_names(self, command, parameter_name):
        # list all param names for example --compartment-id has the names (--compartment-id, -c)

        param_names = set()
        param_names.add(parameter_name)

        if command:
            params = command.params
        else:  # If no command, it means we are at the root level "oci" and the parameter_name is a global one
            params = self.top_level_params
        for param in params:
            if parameter_name == param.name or parameter_name in param.opts:
                param_names.update(param.opts)
                return param_names
        return param_names

    # Whenever a user enters a space, this function is called. Command is split based on space and a loop processes
    # each token. If last token is a service, it returns groups inside service
    # if last token is a group, it returns list of all required parameter and optional parameter
    # deselecting already chosen params
    # if last token is a parameter, it returns resources from the cloud or user can type the param value
    def get_completions(self, document, _):
        is_leaf_command_met = False
        completions = []
        self.list_of_required_params.clear()  # remove required param from previous command
        word_before_cursor = document.get_word_before_cursor(WORD=True)
        tokens = shlex.split(handle_invalid_chars(document.text))
        # Since not all the services are loaded in the beginning, so root_subcommands reads from service_mapping
        only_at_top_level = True
        top_level_commands = self.top_level_commands
        service_subcommands = []
        token_check = tokens[:] if document.text.endswith(" ") else tokens[:-1]
        remaining_command_tokens = tokens[:]
        command = None
        already_chosen_parameters = set()
        parameter = None
        param_value = ""  # this will save parameter value between quotes ( " " or ' ' ) with space
        for token_index, token in enumerate(token_check):
            # add parameters to the list so they will be excluded from the list given to the user
            if token.startswith("-"):
                already_chosen_parameters.update(
                    self.list_all_parameter_names(command, token)
                )
                parameter = token
                remaining_command_tokens.remove(token)
                continue

            elif token_index == 0 and token in top_level_commands:
                # Load the service and all its subcommands. for example "oci compute instance", load the compute service
                dynamic_loader.load_service(token)
                oci_subcommands = getattr(self.ctx.command, "commands", {})
                command = oci_subcommands[token]
                service_subcommands = getattr(command, "commands", {})
                service_subcommands = collections.OrderedDict(
                    sorted(service_subcommands.items())
                )
                only_at_top_level = False

            elif service_subcommands and token in service_subcommands:
                command = service_subcommands[token]
                service_subcommands = getattr(command, "commands", {})
                if not service_subcommands:
                    is_leaf_command_met = True
                service_subcommands = collections.OrderedDict(
                    sorted(service_subcommands.items())
                )
            elif (
                not parameter
            ):  # Not valid command, subcommand or parameter and not a value for a parameter
                self.bottom_toolbar.set_toolbar_text(
                    get_error_message("invalid_input", token), is_error=True
                )
                return completions
            elif parameter and (
                token.startswith('"') or token.startswith("'") or param_value
            ):
                if token.startswith('"') or token.startswith("'"):
                    param_value += token
                elif param_value:
                    param_value += token
                if is_matching_quotes(param_value):
                    parameter = None
                    param_value = ""
            else:
                parameter = None
            remaining_command_tokens.remove(token)
        remaing_sub_string = (
            "" if len(remaining_command_tokens) == 0 else remaining_command_tokens[0]
        )
        # If at top level, read top level commands and show them in the list
        if only_at_top_level:
            completions = self.append_top_level_command_completions(
                word_before_cursor, remaing_sub_string
            )
            validate_incorrect_input(
                completions, word_before_cursor, self.bottom_toolbar
            )
            return completions

        # If the last token is a command, then show the sub commands
        if len(service_subcommands) > 0:
            completions = self.append_command_completions(
                service_subcommands, word_before_cursor, remaing_sub_string
            )
            validate_incorrect_input(
                completions, word_before_cursor, self.bottom_toolbar
            )
            return completions

        if is_leaf_command_met:
            self.get_list_of_req_param(command)

        if not parameter:
            completions = self.append_parameter_completions(
                command,
                word_before_cursor,
                "",
                already_chosen_parameters,
                remaing_sub_string,
            )
            validate_incorrect_input(
                completions, word_before_cursor, self.bottom_toolbar
            )
            return completions

        # if the last token is a parameter, then check if a list of resources need to be provided or the parameter
        # does not need a value like --all
        if check_param_is_flag(command, parameter):
            completions = self.append_parameter_completions(
                command,
                word_before_cursor,
                "",
                already_chosen_parameters,
                remaing_sub_string,
            )
        else:
            completions = get_oci_resources(
                self.ctx,
                parameter,
                word_before_cursor,
                self.bottom_toolbar,
                remaing_sub_string,
            )
        return completions


def check_param_is_flag(command, param):
    for p in command.params:
        if param in p.opts:
            return p.is_flag
    return False


def remove_backslashes(s):
    return s.replace("\\", "")


def escape_quotes(s):
    return s.replace("'", "\\'").replace('"', '\\"')


def handle_invalid_chars(s):
    s = remove_backslashes(s)
    s = escape_quotes(s)
    return s


def validate_incorrect_input(completions, word_before_cursor, bottom_toolbar):
    # This function checks if the user types incorrect text in the terminal
    if not completions:
        error_message = get_error_message("invalid_input", word_before_cursor)
        bottom_toolbar.set_toolbar_text(error_message, is_error=True)
