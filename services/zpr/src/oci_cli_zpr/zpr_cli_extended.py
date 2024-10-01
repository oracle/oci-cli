# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.zpr.src.oci_cli_zpr.generated import zpr_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci zpr zpr-policy-collection list-zpr-policies -> oci zpr zpr-policy list
# Rename and move policy list command to oci zpr zpr-policy
cli_util.rename_command(zpr_cli, zpr_cli.zpr_policy_collection_group, zpr_cli.list_zpr_policies, "list")
zpr_cli.zpr_policy_collection_group.commands.pop(zpr_cli.list_zpr_policies.name)
zpr_cli.zpr_root_group.commands.pop(zpr_cli.zpr_policy_collection_group.name)
zpr_cli.zpr_policy_group.add_command(zpr_cli.list_zpr_policies)


# Move all work-request commands to oci zpr work-request
# oci zpr work-request-error list-zpr-configuration -> oci zpr work-request-error list-zpr-configuration-errors
cli_util.rename_command(zpr_cli, zpr_cli.work_request_error_group, zpr_cli.list_zpr_configuration_work_request_errors, "list-zpr-configuration-errors")


# oci zpr work-request-error list-zpr-policy -> oci zpr work-request-error list-zpr-policy-errors
cli_util.rename_command(zpr_cli, zpr_cli.work_request_error_group, zpr_cli.list_zpr_policy_work_request_errors, "list-zpr-policy-errors")


# oci zpr work-request-log-entry list-zpr-configuration-work-request-logs -> oci zpr work-request-log-entry list-zpr-configuration-logs
cli_util.rename_command(zpr_cli, zpr_cli.work_request_log_entry_group, zpr_cli.list_zpr_configuration_work_request_logs, "list-zpr-configuration-logs")


# oci zpr work-request-log-entry list-zpr-policy-work-request-logs -> oci zpr work-request-log-entry list-zpr-policy-logs
cli_util.rename_command(zpr_cli, zpr_cli.work_request_log_entry_group, zpr_cli.list_zpr_policy_work_request_logs, "list-zpr-policy-logs")


# oci zpr work-request-error list-zpr-configuration -> oci zpr work-request
zpr_cli.work_request_error_group.commands.pop(zpr_cli.list_zpr_configuration_work_request_errors.name)
zpr_cli.work_request_group.add_command(zpr_cli.list_zpr_configuration_work_request_errors)


# oci zpr work-request-error list-zpr-policy -> oci zpr work-request
zpr_cli.work_request_error_group.commands.pop(zpr_cli.list_zpr_policy_work_request_errors.name)
zpr_cli.work_request_group.add_command(zpr_cli.list_zpr_policy_work_request_errors)


# oci zpr work-request-log-entry list-zpr-configuration-work-request-logs -> oci zpr work-request
zpr_cli.work_request_log_entry_group.commands.pop(zpr_cli.list_zpr_configuration_work_request_logs.name)
zpr_cli.work_request_group.add_command(zpr_cli.list_zpr_configuration_work_request_logs)


# oci zpr work-request-log-entry list-zpr-policy-work-request-logs -> oci zpr work-request
zpr_cli.work_request_log_entry_group.commands.pop(zpr_cli.list_zpr_policy_work_request_logs.name)
zpr_cli.work_request_group.add_command(zpr_cli.list_zpr_policy_work_request_logs)


# Remove work-request-error, work-request-log-entry
zpr_cli.zpr_root_group.commands.pop(zpr_cli.work_request_error_group.name)
zpr_cli.zpr_root_group.commands.pop(zpr_cli.work_request_log_entry_group.name)
