# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.tenant_manager_control_plane.src.oci_cli_orders.generated import orders_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci organizations orders order -> oci organizations orders
orders_cli.orders_root_group.commands.pop(orders_cli.order_group.name)
orders_cli.orders_root_group.add_command(orders_cli.activate_order)
orders_cli.orders_root_group.add_command(orders_cli.get_order)
