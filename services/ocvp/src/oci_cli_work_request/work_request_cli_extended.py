# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci_cli.cli_util import rename_command
from services.ocvp.src.oci_cli_ocvp.generated import ocvs_service_cli
from services.ocvp.src.oci_cli_work_request.generated import workrequest_cli

rename_command(ocvs_service_cli, workrequest_cli.work_request_group, workrequest_cli.list_work_requests, "list")
rename_command(ocvs_service_cli, workrequest_cli.work_request_log_entry_group, workrequest_cli.list_work_request_logs, "list")
rename_command(ocvs_service_cli, workrequest_cli.work_request_root_group, workrequest_cli.work_request_log_entry_group, "work-request-log")
ocvs_service_cli.ocvs_service_group.commands.pop(workrequest_cli.work_request_root_group.name)
ocvs_service_cli.ocvs_service_group.add_command(workrequest_cli.work_request_group)
ocvs_service_cli.ocvs_service_group.add_command(workrequest_cli.work_request_log_entry_group)
ocvs_service_cli.ocvs_service_group.add_command(workrequest_cli.work_request_error_group)
