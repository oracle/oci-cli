# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.fusion_apps.src.oci_cli_service_attachment.generated import serviceattachment_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# Move commands under 'oci fusion-apps service-attachment service-attachment' -> 'oci fusion-apps service-attachment'
serviceattachment_cli.service_attachment_root_group.commands.pop(serviceattachment_cli.service_attachment_group.name)
serviceattachment_cli.service_attachment_root_group.add_command(serviceattachment_cli.get_service_attachment)
serviceattachment_cli.service_attachment_root_group.add_command(serviceattachment_cli.list_service_attachments)
