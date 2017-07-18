# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from .cli_root import cli
from . import object_storage_cli  # noqa: F401

# Add additional service cli imports here.
from .generated import blockstorage_cli  # noqa: F401
from .generated import compute_cli  # noqa: F401
from .generated import identity_cli  # noqa: F401
from .generated import virtualnetwork_cli  # noqa: F401
from . import core_cli_extended  # noqa: F401
from . import identity_cli_extended  # noqa: F401
from . import final_command_processor  # noqa: F401
from . import cli_setup  # noqa: F401

if __name__ == '__main__':
    cli()
