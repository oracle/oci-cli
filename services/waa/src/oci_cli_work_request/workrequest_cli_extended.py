# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.waa.src.oci_cli_work_request.generated import workrequest_cli
from services.waa.src.oci_cli_waa.generated import waa_service_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci waa work-request work-request-log-entry list-work-request-logs -> oci waa work-request work-request-log-entry list
cli_util.rename_command(workrequest_cli, workrequest_cli.work_request_log_entry_group, workrequest_cli.list_work_request_logs, "list")


# oci waa work-request work-request-log-entry -> oci waa work-request work-request-log
cli_util.rename_command(workrequest_cli, workrequest_cli.work_request_root_group, workrequest_cli.work_request_log_entry_group, "work-request-log")


# Move commands under 'oci waa work-request' -> 'oci waa'
waa_service_cli.waa_service_group.commands.pop(workrequest_cli.work_request_root_group.name)
waa_service_cli.waa_service_group.add_command(workrequest_cli.work_request_error_group)
waa_service_cli.waa_service_group.add_command(workrequest_cli.work_request_log_entry_group)
waa_service_cli.waa_service_group.add_command(workrequest_cli.work_request_group)
