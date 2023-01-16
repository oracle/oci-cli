# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.stack_monitoring import StackMonitoringClient

MODULE_TO_TYPE_MAPPINGS["stack_monitoring"] = oci.stack_monitoring.models.stack_monitoring_type_mapping
if CLIENT_MAP.get("stack_monitoring") is None:
    CLIENT_MAP["stack_monitoring"] = {}
CLIENT_MAP["stack_monitoring"]["stack_monitoring"] = StackMonitoringClient
