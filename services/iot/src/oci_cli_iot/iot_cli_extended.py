# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.iot.src.oci_cli_iot.generated import iot_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci iot iot-domain-group configure-iot-domain-group-data-access -> oci iot iot-domain-group configure-data-access
cli_util.rename_command(iot_cli, iot_cli.iot_domain_group_group, iot_cli.configure_iot_domain_group_data_access, "configure-data-access")


# oci iot iot-domain change-iot-domain-data-retention-period -> oci iot iot-domain change-data-retention-period
cli_util.rename_command(iot_cli, iot_cli.iot_domain_group, iot_cli.change_iot_domain_data_retention_period, "change-data-retention-period")


# oci iot iot-domain configure-iot-domain-data-access-apex-data-access-details -> oci iot iot-domain configure-apex-data-access
cli_util.rename_command(iot_cli, iot_cli.iot_domain_group, iot_cli.configure_iot_domain_data_access_apex_data_access_details, "configure-apex-data-access")


# oci iot iot-domain configure-iot-domain-data-access-direct-data-access-details -> oci iot iot-domain configure-direct-data-access
cli_util.rename_command(iot_cli, iot_cli.iot_domain_group, iot_cli.configure_iot_domain_data_access_direct_data_access_details, "configure-direct-data-access")


# oci iot iot-domain configure-iot-domain-data-access-ords-data-access-details -> oci iot iot-domain configure-ords-data-access
cli_util.rename_command(iot_cli, iot_cli.iot_domain_group, iot_cli.configure_iot_domain_data_access_ords_data_access_details, "configure-ords-data-access")


# oci iot digital-twin-instance invoke-raw-command-invoke-raw-binary-command-details -> oci iot digital-twin-instance invoke-raw-binary-command
cli_util.rename_command(iot_cli, iot_cli.digital_twin_instance_group, iot_cli.invoke_raw_command_invoke_raw_binary_command_details, "invoke-raw-binary-command")


# oci iot digital-twin-instance invoke-raw-command-invoke-raw-json-command-details -> oci iot digital-twin-instance invoke-raw-json-command
cli_util.rename_command(iot_cli, iot_cli.digital_twin_instance_group, iot_cli.invoke_raw_command_invoke_raw_json_command_details, "invoke-raw-json-command")


# oci iot digital-twin-instance invoke-raw-command-invoke-raw-text-command-details -> oci iot digital-twin-instance invoke-raw-text-command
cli_util.rename_command(iot_cli, iot_cli.digital_twin_instance_group, iot_cli.invoke_raw_command_invoke_raw_text_command_details, "invoke-raw-text-command")


# oci iot digital-twin-model get-digital-twin-model-spec -> oci iot digital-twin-model get-spec
cli_util.rename_command(iot_cli, iot_cli.digital_twin_model_group, iot_cli.get_digital_twin_model_spec, "get-spec")


# oci iot digital-twin-instance get-digital-twin-instance-content -> oci iot digital-twin-instance get-content
cli_util.rename_command(iot_cli, iot_cli.digital_twin_instance_group, iot_cli.get_digital_twin_instance_content, "get-content")


# oci iot work-request list-work-request-errors -> oci iot work-request list-errors
cli_util.rename_command(iot_cli, iot_cli.work_request_group, iot_cli.list_work_request_errors, "list-errors")


# oci iot work-request list-work-request-logs -> oci iot work-request list-logs
cli_util.rename_command(iot_cli, iot_cli.work_request_group, iot_cli.list_work_request_logs, "list-logs")


# oci iot iot-domain -> oci iot domain
cli_util.rename_command(iot_cli, iot_cli.iot_root_group, iot_cli.iot_domain_group, "domain")


# oci iot iot-domain-group -> oci iot domain-group
cli_util.rename_command(iot_cli, iot_cli.iot_root_group, iot_cli.iot_domain_group_group, "domain-group")


# Remove configure-iot-domain-data-access from oci iot iot-domain
iot_cli.iot_domain_group.commands.pop(iot_cli.configure_iot_domain_data_access.name)


# Remove invoke-raw-command from oci iot digital-twin-instance
iot_cli.digital_twin_instance_group.commands.pop(iot_cli.invoke_raw_command.name)
