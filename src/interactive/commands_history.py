# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import os
import datetime
from prompt_toolkit.history import FileHistory
from oci_cli import cli_util
from interactive.utils import (
    INTERACTIVE_COMMANDS_HISTORY_DIR_NAME,
    validate_commands_limit,
)


class CommandsHistory(FileHistory):
    """
    :class:`.CommandsHistory` object that remembers Interactive CLI commands and save, read them from a file.
    """

    def store_string(self, string: str) -> None:
        """
        When user executes the command, this function in being called by the prompt toolkit to save the command in
        the history file
        """

        # The location of the history file consists of directory (~/.oci) and file name, so checking if the directory does
        # not exist, create it
        if not os.path.isdir(INTERACTIVE_COMMANDS_HISTORY_DIR_NAME):
            cli_util.create_directory(INTERACTIVE_COMMANDS_HISTORY_DIR_NAME)
        with open(self.filename, "ab") as f:

            def write(s: str) -> None:
                f.write(s.encode("utf-8"))

            write("\n# %s\n" % datetime.datetime.now())
            write("+%s\n" % string)
        validate_commands_limit(self.filename)
