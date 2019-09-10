# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.oce import OceInstanceClient

MODULE_TO_TYPE_MAPPINGS["oce"] = oci.oce.models.oce_type_mapping
CLIENT_MAP["oce_instance"] = OceInstanceClient
