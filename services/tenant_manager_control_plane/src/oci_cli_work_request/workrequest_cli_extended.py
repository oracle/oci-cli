# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.tenant_manager_control_plane.src.oci_cli_work_request.generated import workrequest_cli
from services.tenant_manager_control_plane.src.oci_cli_tenant_manager_control_plane.generated import organizations_service_cli
from oci_cli import cli_util

workrequest_cli.work_request_root_group.commands.pop(workrequest_cli.work_request_group.name)
workrequest_cli.work_request_root_group.add_command(workrequest_cli.get_work_request)
workrequest_cli.work_request_root_group.add_command(workrequest_cli.list_work_requests)

workrequest_cli.work_request_root_group.commands.pop(workrequest_cli.work_request_error_group.name)
workrequest_cli.work_request_root_group.commands.pop(workrequest_cli.work_request_log_entry_group.name)
organizations_service_cli.organizations_service_group.add_command(workrequest_cli.work_request_error_group)
organizations_service_cli.organizations_service_group.add_command(workrequest_cli.work_request_log_entry_group)

cli_util.rename_command(organizations_service_cli, workrequest_cli.work_request_log_entry_group, workrequest_cli.list_work_request_logs, "list")
