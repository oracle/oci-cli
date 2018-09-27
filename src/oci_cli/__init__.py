# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

import os
from . import fips

# This needs to be done prior to other imports otherwise things like hashlib
# may not get properly bound to the desired libcrypto.
fips_libcrypto_file = os.getenv("OCI_CLI_FIPS_LIBCRYPTO_FILE")
if fips_libcrypto_file:
    fips.override_libcrypto(fips_libcrypto_file)
    fips.patch_hashlib_md5()


# These imports are used by tests. The primary entry point for the CLI is cli.py.
from .cli_root import cli  # noqa: F401,E402
from .custom_types import cli_datetime  # noqa: F401,E402
from .custom_types import cli_from_json  # noqa: F401,E402

from .generated import *   # noqa: F401,F403,E402
from .extended import *  # noqa: F401,F403,E402

from . import aliasing  # noqa: F401,E402
from . import file_filters  # noqa: F401,E402
from . import final_command_processor  # noqa: F401,E402
from . import cli_setup  # noqa: F401,E402
from . import cli_util  # noqa: F401,E402
from . import cli_exceptions  # noqa: F401,E402
from . import object_storage_transfer_manager  # noqa: F401,E402
from . import json_skeleton_utils  # noqa: F401,E402
from . import string_utils  # noqa: F401,E402
from . import help_text_producer  # noqa: F401,E402
from oci import config  # noqa: F401,E402
from .version import __version__  # noqa: F401,E402
