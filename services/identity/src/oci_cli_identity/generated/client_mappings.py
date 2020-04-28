# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.identity import IdentityClient

MODULE_TO_TYPE_MAPPINGS["identity"] = oci.identity.models.identity_type_mapping
if CLIENT_MAP.get("identity") is None:
    CLIENT_MAP["identity"] = {}
CLIENT_MAP["identity"]["identity"] = IdentityClient
