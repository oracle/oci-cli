# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.container_engine import ContainerEngineClient

MODULE_TO_TYPE_MAPPINGS["container_engine"] = oci.container_engine.models.container_engine_type_mapping
CLIENT_MAP["container_engine"] = ContainerEngineClient
