# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401

from services.rover.src.oci_cli_rover.generated import rover_service_cli
from services.rover.src.oci_cli_rover_bundle.generated import roverbundle_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


roverbundle_cli.rover_bundle_root_group.commands.pop(roverbundle_cli.rover_cluster_group.name)
roverbundle_cli.rover_bundle_root_group.commands.pop(roverbundle_cli.rover_node_group.name)
rover_service_cli.rover_service_group.commands.pop(roverbundle_cli.rover_bundle_root_group.name)
