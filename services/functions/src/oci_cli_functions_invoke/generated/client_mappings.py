# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.functions import FunctionsInvokeClient

MODULE_TO_TYPE_MAPPINGS["functions"] = oci.functions.models.functions_type_mapping
CLIENT_MAP["functions_invoke"] = FunctionsInvokeClient
