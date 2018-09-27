# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

CLIENT_MAP = {}
MODULE_TO_TYPE_MAPPINGS = {}

# This import populates CLIENT_MAP and MODULE_TO_TYPE_MAPPINGS
import oci_cli.generated_client_mappings  # noqa: F401,E402
