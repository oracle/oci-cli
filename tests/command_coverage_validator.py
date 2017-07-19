# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
from . import util


class CommandCoverageValidator:
    """Validates that all of the leaf commands under a given root command are called."""

    def __init__(self, root_command, expected_not_called_count=0):
        self.root_command = root_command
        self.expected_not_called_count = expected_not_called_count

    def register_call(self, commands):
        command_string = ' '.join(commands)
        for command in self.remaining_commands:
            if command in command_string:
                self.remaining_commands.remove(command)
                break

    def __call__(self, func):
        validator = self

        def wrapper(*args, **kwargs):
            validator.remaining_commands = []
            for command in sorted(util.collect_commands(validator.root_command, leaf_commands_only=True)):
                validator.remaining_commands.append(' '.join(command))

            total_command_count = len(validator.remaining_commands)
            result = func(*args, validator=validator, **kwargs)

            remaining_command_count = len(validator.remaining_commands)
            print("Called {called} of {total} commands.".format(called=str(total_command_count - remaining_command_count), total=str(total_command_count)))

            if remaining_command_count > 0:
                print("Did not call the following commands:")
                for command in validator.remaining_commands:
                    print(str(command))

            if self.expected_not_called_count >= 0:
                assert(remaining_command_count == self.expected_not_called_count)

            return result

        return wrapper
