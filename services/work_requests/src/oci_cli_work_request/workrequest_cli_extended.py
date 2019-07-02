# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from services.work_requests.src.oci_cli_work_request.generated import workrequest_cli
from oci_cli import cli_util

cli_util.rename_command(workrequest_cli.work_request_log_entry_group, workrequest_cli.list_work_request_logs, "list")
