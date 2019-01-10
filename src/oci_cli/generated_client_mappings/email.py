# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.email import EmailClient

MODULE_TO_TYPE_MAPPINGS["email"] = oci.email.models.email_type_mapping
CLIENT_MAP["email"] = EmailClient
