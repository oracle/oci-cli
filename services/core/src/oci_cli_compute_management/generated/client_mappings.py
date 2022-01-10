# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.core import ComputeManagementClient

MODULE_TO_TYPE_MAPPINGS["core"] = oci.core.models.core_type_mapping
if CLIENT_MAP.get("core") is None:
    CLIENT_MAP["core"] = {}
CLIENT_MAP["core"]["compute_management"] = ComputeManagementClient
