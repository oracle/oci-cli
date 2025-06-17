# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.apiaccesscontrol.src.oci_cli_api_metadata.generated import apimetadata_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# Move commands under 'oci apiaccesscontrol api-metadata api-metadata' -> 'oci apiaccesscontrol api-metadata'
apimetadata_cli.api_metadata_root_group.commands.pop(apimetadata_cli.api_metadata_group.name)
apimetadata_cli.api_metadata_root_group.add_command(apimetadata_cli.get_api_metadata)
apimetadata_cli.api_metadata_root_group.add_command(apimetadata_cli.list_api_metadata)
apimetadata_cli.api_metadata_root_group.add_command(apimetadata_cli.list_api_metadata_by_entity_types)
