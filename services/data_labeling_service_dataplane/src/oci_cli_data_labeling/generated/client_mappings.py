# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.data_labeling_service_dataplane import DataLabelingClient

MODULE_TO_TYPE_MAPPINGS["data_labeling_service_dataplane"] = oci.data_labeling_service_dataplane.models.data_labeling_service_dataplane_type_mapping
if CLIENT_MAP.get("data_labeling_service_dataplane") is None:
    CLIENT_MAP["data_labeling_service_dataplane"] = {}
CLIENT_MAP["data_labeling_service_dataplane"]["data_labeling"] = DataLabelingClient
