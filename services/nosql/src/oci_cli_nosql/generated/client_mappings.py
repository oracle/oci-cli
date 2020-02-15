# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.nosql import NosqlClient

MODULE_TO_TYPE_MAPPINGS["nosql"] = oci.nosql.models.nosql_type_mapping
CLIENT_MAP["nosql"] = NosqlClient
