# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.resource_search import ResourceSearchClient

MODULE_TO_TYPE_MAPPINGS["resource_search"] = oci.resource_search.models.resource_search_type_mapping
if CLIENT_MAP.get("resource_search") is None:
    CLIENT_MAP["resource_search"] = {}
CLIENT_MAP["resource_search"]["resource_search"] = ResourceSearchClient
