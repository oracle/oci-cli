# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import os
import sys
import pkgutil
from inspect import getsourcefile
from os.path import abspath

from oci import fips
ALL_SERVICES_DIR = "services"

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

# Add platformization directories to the python system path (PYTHONPATH)
# This has to be done prior to importing cli_root.
this_file_path = abspath(getsourcefile(lambda: 0))
if "site-packages" in this_file_path or "dist-packages" in this_file_path:
    # If the installation directory starts with oci_cli, we need to find the
    # last occurrence of oci_cli in the path.
    python_cli_root_dir = this_file_path[0:this_file_path.rindex("oci_cli")]
else:
    python_cli_root_dir = this_file_path[0:this_file_path.index("/src/oci_cli")]
sys.path.append(python_cli_root_dir + 'src')
sys.path.append(python_cli_root_dir)
services_dir = os.path.join(python_cli_root_dir, ALL_SERVICES_DIR)

# These imports are used by tests. The primary entry point for the CLI is cli.py.
from .cli_root import cli  # noqa: F401,E402
from .custom_types import cli_datetime  # noqa: F401,E402
from .custom_types import cli_from_json  # noqa: F401,E402

# Import generated and extended code from platformization directories.
# This has to be done after importing cli_root
for importer1, modname1, ispkg1 in pkgutil.iter_modules(path=[services_dir]):
    for importer, modname, ispkg in pkgutil.iter_modules(path=[services_dir + '/' + modname1 + '/src']):
        if ispkg and modname.startswith("oci_cli_"):
            oci_cli_module_name = modname.split(".")[0]
            service_name = oci_cli_module_name[8:]
            oci_cli_module = __import__(ALL_SERVICES_DIR + '.' + modname1 + '.src.' + oci_cli_module_name)
            service_dir = os.path.join(services_dir, modname1, 'src', oci_cli_module_name)
            generated_module = service_name.replace('_', '') + "_cli"
            if os.path.isfile(os.path.join(service_dir, 'generated', generated_module + ".py")):
                __import__(ALL_SERVICES_DIR + '.' + modname1 + '.src.' + oci_cli_module_name + ".generated." + generated_module)

            for file_name in os.listdir(service_dir):
                if 'extended' in file_name and os.path.isfile(os.path.join(service_dir, file_name)):
                    extended_module = file_name[:-3]
                    __import__(ALL_SERVICES_DIR + '.' + modname1 + '.src.' + oci_cli_module_name + "." + extended_module)

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
