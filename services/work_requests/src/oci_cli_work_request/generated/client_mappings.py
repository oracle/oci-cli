# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.work_requests import WorkRequestClient

MODULE_TO_TYPE_MAPPINGS["work_requests"] = oci.work_requests.models.work_requests_type_mapping
if CLIENT_MAP.get("work_requests") is None:
    CLIENT_MAP["work_requests"] = {}
CLIENT_MAP["work_requests"]["work_request"] = WorkRequestClient
