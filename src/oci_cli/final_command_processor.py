# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
from . import cli_root, cli_util

# Map parameter variable names to shortcuts.
PARAMETER_SHORTCUT = {
    'compartment_id': '-c'
}

# Services such as object storage and identity register special code to execute.
SERVICE_FUNCTIONS_TO_EXECUTE = []


def add_shortcuts():
    commands = cli_util.collect_commands(cli_root.cli)
    for command in commands:
        for param in command.params:
            shortcut = PARAMETER_SHORTCUT.get(param.name)

            # "shortcut not in param.opts" is For where we use the cli_util.copy_params_from_generated_command
            # and the source command already contains the parameter shortcut, we don't want to shove it in again.
            #
            # This is used in scenarios like:
            #
            # The `import_image_from_object` command is annotated with `@cli_util.copy_params_from_generated_command`.
            # The command we copy from has --compartment-id as one of the options
            #
            # When we fall into this code for the `import_image_from_object` command, the command we copy from has
            # already had a shortcut applied to the --compartment-id option. If we do not check for the shortcut's
            # presence we would append the shortcut again so the help looks like:
            #
            #     -c, -c, -c, --compartment-id TEXT
            #
            # Instead of:
            #     -c, --compartment-id TEXT
            if shortcut and shortcut not in param.opts:
                param.opts.append(shortcut)


def process():
    add_shortcuts()
    for f in SERVICE_FUNCTIONS_TO_EXECUTE:
        f()
