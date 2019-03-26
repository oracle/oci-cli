# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from .cli_root import cli
from . import final_command_processor  # noqa: F401
from . import cli_session  # noqa: F401,E402
from . import cli_setup  # noqa: F401
from . import cli_setup_bootstrap  # noqa: F401

if __name__ == '__main__':
    cli()
