# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.email.src.oci_cli_email.generated import email_cli
from oci_cli import cli_util


email_cli.email_root_group.help = "Email Delivery Service CLI"


# oci email work-request-error-collection list-work-request-errors -> oci email work-request-error-collection list
cli_util.rename_command(email_cli, email_cli.work_request_error_collection_group, email_cli.list_work_request_errors, "list")


# oci email work-request-log-entry-collection -> oci email work-request-log
cli_util.rename_command(email_cli, email_cli.email_root_group, email_cli.work_request_log_entry_collection_group, "work-request-log")


# oci email work-request-log-entry-collection list-work-request-logs -> oci email work-request-log-entry-collection work-request-log-entry-collectionlist
cli_util.rename_command(email_cli, email_cli.work_request_log_entry_collection_group, email_cli.list_work_request_logs, "list")


# oci email email-domain -> oci email domain
cli_util.rename_command(email_cli, email_cli.email_root_group, email_cli.email_domain_group, "domain")


# oci email work-request-summary-collection list-work-requests -> oci email work-request
email_cli.work_request_summary_collection_group.commands.pop(email_cli.list_work_requests.name)
cli_util.rename_command(email_cli, email_cli.work_request_group, email_cli.list_work_requests, "list")
email_cli.email_root_group.commands.pop(email_cli.work_request_summary_collection_group.name)


# oci email work-request-error-collection -> oci email work-request-error
cli_util.rename_command(email_cli, email_cli.email_root_group, email_cli.work_request_error_collection_group, "work-request-error")
