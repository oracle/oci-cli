# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .cli_root import cli

# Add additional service cli imports here.
from .generated import *  # noqa: F401,F403
from .extended import *  # noqa: F401,F403

from . import final_command_processor  # noqa: F401
from . import cli_setup  # noqa: F401

if __name__ == '__main__':
    cli()
