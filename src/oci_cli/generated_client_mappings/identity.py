# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.identity import IdentityClient

MODULE_TO_TYPE_MAPPINGS["identity"] = oci.identity.models.identity_type_mapping
CLIENT_MAP["identity"] = IdentityClient
