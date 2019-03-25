# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

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
python_cli_root_dir = this_file_path[:-24]  # chop off "/src/oci_cli/__init__.py"
sys.path.append(python_cli_root_dir + '/src')
if os.path.isdir(python_cli_root_dir + '/' + ALL_SERVICES_DIR):
    for dir_name in os.listdir(python_cli_root_dir + '/' + ALL_SERVICES_DIR):
        if os.path.isdir(os.path.join(python_cli_root_dir, ALL_SERVICES_DIR, dir_name)):
            spec_dir_src = os.path.join(python_cli_root_dir, ALL_SERVICES_DIR, dir_name, 'src')
            if os.path.isdir(spec_dir_src):
                sys.path.append(spec_dir_src)

# These imports are used by tests. The primary entry point for the CLI is cli.py.
from .cli_root import cli  # noqa: F401,E402
from .custom_types import cli_datetime  # noqa: F401,E402
from .custom_types import cli_from_json  # noqa: F401,E402

# Import generated and extended code from platformization directories.
# This has to be done after importing cli_root
for importer, modname, ispkg in pkgutil.iter_modules(path=None):
    if ispkg and modname.startswith("oci_cli_"):
        oci_cli_module_name = modname.split(".")[0]
        service_name = oci_cli_module_name[8:]
        oci_cli_module = __import__(oci_cli_module_name)
        service_dir = oci_cli_module.__path__[0]
        generated_module = service_name.replace('_', '') + "_cli"
        if os.path.isdir(os.path.join(service_dir, 'generated')) and os.path.isfile(os.path.join(service_dir, 'generated', generated_module + ".py")):
            __import__(oci_cli_module_name + ".generated." + generated_module)

        for file_name in os.listdir(service_dir):
            if 'extended' in file_name and os.path.isfile(os.path.join(service_dir, file_name)):
                extended_module = file_name[:-3]
                __import__(oci_cli_module_name + "." + extended_module)

from . import aliasing  # noqa: F401,E402
from . import file_filters  # noqa: F401,E402
from . import final_command_processor  # noqa: F401,E402
from . import cli_setup  # noqa: F401,E402
from . import cli_session  # noqa: F401,E402
from . import cli_setup_bootstrap  # noqa: F401,E402
from . import cli_util  # noqa: F401,E402
from . import cli_exceptions  # noqa: F401,E402
from . import object_storage_transfer_manager  # noqa: F401,E402
from . import json_skeleton_utils  # noqa: F401,E402
from . import string_utils  # noqa: F401,E402
from . import help_text_producer  # noqa: F401,E402
from oci import config  # noqa: F401,E402
from .version import __version__  # noqa: F401,E402
