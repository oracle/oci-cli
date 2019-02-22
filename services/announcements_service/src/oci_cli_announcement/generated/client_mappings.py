# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.announcements_service import AnnouncementClient

MODULE_TO_TYPE_MAPPINGS["announcements_service"] = oci.announcements_service.models.announcements_service_type_mapping
CLIENT_MAP["announcement"] = AnnouncementClient
