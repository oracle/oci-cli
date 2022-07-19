# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.fusion_apps.src.oci_cli_fusion_environment.generated import fusionenvironment_cli
from services.fusion_apps.src.oci_cli_fusion_apps.generated import fusion_apps_service_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# Move commands under 'oci fusion-apps fusion-environment fusion-environment' -> 'oci fusion-apps fusion-environment'
fusionenvironment_cli.fusion_environment_root_group.commands.pop(fusionenvironment_cli.fusion_environment_group.name)
fusionenvironment_cli.fusion_environment_root_group.add_command(fusionenvironment_cli.change_fusion_environment_compartment)
fusionenvironment_cli.fusion_environment_root_group.add_command(fusionenvironment_cli.create_fusion_environment)
fusionenvironment_cli.fusion_environment_root_group.add_command(fusionenvironment_cli.create_fusion_environment_admin_user)
fusionenvironment_cli.fusion_environment_root_group.add_command(fusionenvironment_cli.delete_fusion_environment)
fusionenvironment_cli.fusion_environment_root_group.add_command(fusionenvironment_cli.delete_fusion_environment_admin_user)
fusionenvironment_cli.fusion_environment_root_group.add_command(fusionenvironment_cli.get_fusion_environment)
fusionenvironment_cli.fusion_environment_root_group.add_command(fusionenvironment_cli.list_admin_users)
fusionenvironment_cli.fusion_environment_root_group.add_command(fusionenvironment_cli.list_fusion_environments)
fusionenvironment_cli.fusion_environment_root_group.add_command(fusionenvironment_cli.reset_fusion_environment_password)
fusionenvironment_cli.fusion_environment_root_group.add_command(fusionenvironment_cli.update_fusion_environment)

# Move commands under 'oci fusion-apps fusion-environment work-request -> oci fusion-apps work-request'
fusionenvironment_cli.fusion_environment_root_group.commands.pop(fusionenvironment_cli.work_request_group.name)
fusion_apps_service_cli.fusion_apps_service_group.add_command(fusionenvironment_cli.work_request_group)

# Move commands under 'oci fusion-apps fusion-environment work-request-error -> oci fusion-apps work-request-error'
fusionenvironment_cli.fusion_environment_root_group.commands.pop(fusionenvironment_cli.work_request_error_group.name)
fusion_apps_service_cli.fusion_apps_service_group.add_command(fusionenvironment_cli.work_request_error_group)

# Move commands under 'oci fusion-apps fusion-environment work-request-log-entry -> oci fusion-apps work-request-log-entry'
fusionenvironment_cli.fusion_environment_root_group.commands.pop(fusionenvironment_cli.work_request_log_entry_group.name)
fusion_apps_service_cli.fusion_apps_service_group.add_command(fusionenvironment_cli.work_request_log_entry_group)

# Move commands under 'oci fusion-apps fusion-environment fusion-environment-status -> oci fusion-apps fusion-environment-status'
fusionenvironment_cli.fusion_environment_root_group.commands.pop(fusionenvironment_cli.fusion_environment_status_group.name)
fusion_apps_service_cli.fusion_apps_service_group.add_command(fusionenvironment_cli.fusion_environment_status_group)
