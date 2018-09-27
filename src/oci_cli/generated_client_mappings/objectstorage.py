# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.object_storage import ObjectStorageClient

MODULE_TO_TYPE_MAPPINGS["object_storage"] = oci.object_storage.models.object_storage_type_mapping
CLIENT_MAP["object_storage"] = ObjectStorageClient
