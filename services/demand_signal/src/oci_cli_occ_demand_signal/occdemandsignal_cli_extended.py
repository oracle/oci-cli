# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.demand_signal.src.oci_cli_occ_demand_signal.generated import occdemandsignal_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# Move commands under 'oci demand-signal occ-demand-signal occ-demand-signal' -> 'oci demand-signal occ-demand-signal'
occdemandsignal_cli.occ_demand_signal_root_group.commands.pop(occdemandsignal_cli.occ_demand_signal_group.name)
occdemandsignal_cli.occ_demand_signal_root_group.add_command(occdemandsignal_cli.change_occ_demand_signal_compartment)
occdemandsignal_cli.occ_demand_signal_root_group.add_command(occdemandsignal_cli.create_occ_demand_signal)
occdemandsignal_cli.occ_demand_signal_root_group.add_command(occdemandsignal_cli.delete_occ_demand_signal)
occdemandsignal_cli.occ_demand_signal_root_group.add_command(occdemandsignal_cli.get_occ_demand_signal)
occdemandsignal_cli.occ_demand_signal_root_group.add_command(occdemandsignal_cli.patch_occ_demand_signal)
occdemandsignal_cli.occ_demand_signal_root_group.add_command(occdemandsignal_cli.update_occ_demand_signal)
