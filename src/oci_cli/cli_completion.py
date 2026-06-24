# coding: utf-8

# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function

import pathlib

from oci_cli import cli_util
from oci_cli.cli_root import cli

# from alloy import alloy_util

completion_instructions = """
    This command prints completion code for the specified shell (bash).
"""


@cli.group('completion', help=completion_instructions)
@cli_util.help_option_group
def completion():
    pass


@completion.command('bash', help="""Print completions for bash""")
def completion_bash():
    from oci_cli.cli_setup import setup_autocomplete_non_windows_completion_script_file as csf

    csf_contents = pathlib.Path(csf()).read_text()

    print(csf_contents)
