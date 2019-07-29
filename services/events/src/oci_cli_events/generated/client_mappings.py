# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.events import EventsClient

MODULE_TO_TYPE_MAPPINGS["events"] = oci.events.models.events_type_mapping
CLIENT_MAP["events"] = EventsClient
