# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from services.mysql.src.oci_cli_work_requests.generated import workrequests_cli
from services.mysql.src.oci_cli_mysql.generated import mysql_service_cli
from oci_cli import cli_util

# rename oci mysql work-requests work-request-log-entry list-work-request-logs -> oci mysql work-requests work-request-log-entry list
cli_util.rename_command(workrequests_cli, workrequests_cli.work_request_log_entry_group, workrequests_cli.list_work_request_logs, "list")

# oci mysql work-requests work-request* -> oci mysql work-request*
mysql_service_cli.mysql_service_group.commands.pop(workrequests_cli.work_requests_root_group.name)
mysql_service_cli.mysql_service_group.add_command(workrequests_cli.work_request_error_group)
mysql_service_cli.mysql_service_group.add_command(workrequests_cli.work_request_log_entry_group)
mysql_service_cli.mysql_service_group.add_command(workrequests_cli.work_request_group)
