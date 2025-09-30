# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.ocvp.src.oci_cli_datastore.generated import datastore_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci ocvs datastore datastore add -> oci ocvs datastore datastore add-block-volume
cli_util.rename_command(datastore_cli, datastore_cli.datastore_group, datastore_cli.add_block_volume_to_datastore, "add-block-volume")


# Move commands under 'oci ocvs datastore datastore' -> 'oci ocvs datastore'
datastore_cli.datastore_root_group.commands.pop(datastore_cli.datastore_group.name)
datastore_cli.datastore_root_group.add_command(datastore_cli.add_block_volume_to_datastore)
datastore_cli.datastore_root_group.add_command(datastore_cli.change_datastore_compartment)
datastore_cli.datastore_root_group.add_command(datastore_cli.create_datastore)
datastore_cli.datastore_root_group.add_command(datastore_cli.delete_datastore)
datastore_cli.datastore_root_group.add_command(datastore_cli.get_datastore)
datastore_cli.datastore_root_group.add_command(datastore_cli.list_datastores)
datastore_cli.datastore_root_group.add_command(datastore_cli.update_datastore)
