# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.demand_signal.src.oci_cli_occ_metric_alarm.generated import occmetricalarm_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# Move commands under 'oci demand-signal occ-metric-alarm occ-metric-alarm' -> 'oci demand-signal occ-metric-alarm'
occmetricalarm_cli.occ_metric_alarm_root_group.commands.pop(occmetricalarm_cli.occ_metric_alarm_group.name)
occmetricalarm_cli.occ_metric_alarm_root_group.add_command(occmetricalarm_cli.create_occ_metric_alarm)
occmetricalarm_cli.occ_metric_alarm_root_group.add_command(occmetricalarm_cli.create_occ_metric_alarm_exadata_resource_configuration)
occmetricalarm_cli.occ_metric_alarm_root_group.add_command(occmetricalarm_cli.create_occ_metric_alarm_network_resource_configuration)
occmetricalarm_cli.occ_metric_alarm_root_group.add_command(occmetricalarm_cli.create_occ_metric_alarm_storage_resource_configuration)
occmetricalarm_cli.occ_metric_alarm_root_group.add_command(occmetricalarm_cli.create_occ_metric_alarm_compute_resource_configuration)
occmetricalarm_cli.occ_metric_alarm_root_group.add_command(occmetricalarm_cli.delete_occ_metric_alarm)
occmetricalarm_cli.occ_metric_alarm_root_group.add_command(occmetricalarm_cli.get_occ_metric_alarm)
occmetricalarm_cli.occ_metric_alarm_root_group.add_command(occmetricalarm_cli.update_occ_metric_alarm)
