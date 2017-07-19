# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
from . import cli_root, cli_util


# Map parameter variable names to shortcuts.
PARAMETER_SHORTCUT = {
    'compartment_id': '-c'
}


def add_shortcuts():
    commands = cli_util.collect_commands(cli_root.cli)
    for command in commands:
        for param in command.params:
            shortcut = PARAMETER_SHORTCUT.get(param.name)
            if shortcut:
                param.opts.append(shortcut)


add_shortcuts()
