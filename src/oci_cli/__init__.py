# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import os

os.environ["OCI_PYTHON_SDK_NO_SERVICE_IMPORTS"] = "1"

from oci import fips  # noqa: F401,E402

# This needs to be done prior to other imports otherwise things like hashlib
# may not get properly bound to the desired libcrypto.
fips_libcrypto_file = os.getenv("OCI_CLI_FIPS_LIBCRYPTO_FILE")
if fips_libcrypto_file:
    # This is used by python sdk.
    os.putenv("FIPS_LIBCRYPTO_PATH", fips_libcrypto_file)
else:
    fips_libcrypto_file = os.getenv("FIPS_LIBCRYPTO_PATH")
if fips_libcrypto_file:
    fips.enable_fips_mode(fips_libcrypto_file)


# These imports are used by tests. The primary entry point for the CLI is cli.py.
from .cli_root import cli  # noqa: F401,E402
from .custom_types import cli_datetime  # noqa: F401,E402
from .custom_types import cli_from_json  # noqa: F401,E402
from . import dynamic_loader as dl  # noqa: F401,E402

dl.load_required_services_for_invocation()

from . import aliasing  # noqa: F401,E402
from . import file_filters  # noqa: F401,E402
from . import final_command_processor  # noqa: F401,E402
from . import cli_setup  # noqa: F401,E402
from . import cli_session  # noqa: F401,E402
from . import cli_setup_bootstrap  # noqa: F401,E402
from . import cli_util  # noqa: F401,E402
from . import cli_exceptions  # noqa: F401,E402
from . import json_skeleton_utils  # noqa: F401,E402
from . import string_utils  # noqa: F401,E402
from . import help_text_producer  # noqa: F401,E402
from . import raw_request_cli  # noqa: F401,E402
from oci import config  # noqa: F401,E402
from .version import __version__  # noqa: F401,E402

final_command_processor.process()
