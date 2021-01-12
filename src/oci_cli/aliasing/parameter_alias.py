# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from copy import deepcopy
import click
import six

ALIASES = {}


def get_aliases_for_long_parameter(long_param_name):
    if long_param_name in ALIASES:
        return ALIASES[long_param_name]
    else:
        return []


def shim_in_aliases(command_group):
    remove_redundant_aliases()
    collision_errors = set()
    for cmd_name, cmd_obj in six.iteritems(command_group.commands):
        if isinstance(cmd_obj, click.Group):
            collision_errors.update(shim_in_aliases(cmd_obj))
        elif isinstance(cmd_obj, click.Command):
            collision_errors.update(add_alias_to_command_params(cmd_obj.params))

    return collision_errors


def add_alias_to_command_params(params):
    original_opts = {}
    for param in params:
        original_opts[param.name] = param.opts

    collision_errors = set()
    for param in params:
        available_opts = param.opts
        for o in available_opts:
            if o in ALIASES:
                alias_exists_tuple = does_option_name_already_exist(original_opts, param.name, ALIASES[o])
                if alias_exists_tuple:
                    collision_errors.add(
                        'Could not add alias {} to param {} as it conflicts with existing options for parameter {}'.format(alias_exists_tuple[0], available_opts[0], alias_exists_tuple[2][0])
                    )
                else:
                    available_opts.extend(ALIASES[o])

    return collision_errors


def does_option_name_already_exist(original_opts, param_name, aliases):
    for param, opts in six.iteritems(original_opts):
        if param == param_name:
            continue

        for a in aliases:
            if a in opts:
                return (a, param, opts)

    return None


# Remove aliases that are the same as the parameter.
def remove_redundant_aliases():
    global ALIASES
    new_aliases = deepcopy(ALIASES)
    for param, aliases in ALIASES.items():
        if param in aliases:
            new_aliases[param] = list(filter(lambda alias: alias != param, aliases))
    ALIASES = new_aliases
    return
