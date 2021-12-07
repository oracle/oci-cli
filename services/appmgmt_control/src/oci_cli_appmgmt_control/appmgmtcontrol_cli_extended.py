# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.appmgmt_control.src.oci_cli_appmgmt_control.generated import appmgmtcontrol_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci appmgmt-control monitored-instance activate-monitoring-plugin -> oci appmgmt-control monitored-instance activate-plugin
cli_util.rename_command(appmgmtcontrol_cli, appmgmtcontrol_cli.monitored_instance_group, appmgmtcontrol_cli.activate_monitoring_plugin, "activate-plugin")


# oci appmgmt-control monitored-instance publish-top-processes-metrics -> oci appmgmt-control monitored-instance publish-top-processes
cli_util.rename_command(appmgmtcontrol_cli, appmgmtcontrol_cli.monitored_instance_group, appmgmtcontrol_cli.publish_top_processes_metrics, "publish-top-processes")


# oci appmgmt-control work-request-log-entry list-work-request-logs -> oci appmgmt-control work-request-log-entry list
cli_util.rename_command(appmgmtcontrol_cli, appmgmtcontrol_cli.work_request_log_entry_group, appmgmtcontrol_cli.list_work_request_logs, "list")
