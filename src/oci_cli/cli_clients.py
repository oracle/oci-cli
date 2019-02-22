# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import os
import pkgutil
CLIENT_MAP = {}
MODULE_TO_TYPE_MAPPINGS = {}

# Import client mappings from platformization directories.
# This imports the generated client_mappings which populates CLIENT_MAP and MODULE_TO_TYPE_MAPPINGS.
for importer, modname, ispkg in pkgutil.iter_modules(path=None):
    if ispkg and modname.startswith("oci_cli_"):
        oci_cli_module_name = modname.split(".")[0]
        service_name = oci_cli_module_name[8:]
        oci_cli_module = __import__(oci_cli_module_name)
        service_dir = oci_cli_module.__path__[0]
        generated_module = "client_mappings"
        if os.path.isdir(os.path.join(service_dir, 'generated')) and os.path.isfile(os.path.join(service_dir, 'generated', generated_module + ".py")):
            __import__(oci_cli_module_name + ".generated." + generated_module)
