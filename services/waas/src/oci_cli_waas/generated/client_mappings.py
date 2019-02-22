# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.waas import WaasClient

MODULE_TO_TYPE_MAPPINGS["waas"] = oci.waas.models.waas_type_mapping
CLIENT_MAP["waas"] = WaasClient
