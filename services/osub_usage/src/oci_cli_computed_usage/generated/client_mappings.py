# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.osub_usage import ComputedUsageClient

MODULE_TO_TYPE_MAPPINGS["osub_usage"] = oci.osub_usage.models.osub_usage_type_mapping
if CLIENT_MAP.get("osub_usage") is None:
    CLIENT_MAP["osub_usage"] = {}
CLIENT_MAP["osub_usage"]["computed_usage"] = ComputedUsageClient
