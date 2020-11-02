# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
from services.optimizer.src.oci_cli_optimizer.generated import optimizer_cli
from oci_cli import custom_types  # noqa: F401
from oci_cli import cli_util

# oci optimizer work-request-log-entry list-work-request-logs
# oci optimizer work-request-log-entry list
cli_util.rename_command(optimizer_cli, optimizer_cli.work_request_log_entry_group, optimizer_cli.list_work_request_logs, "list")

# oci optimizer category-summary list-categories
# oci optimizer category-summary list
cli_util.rename_command(optimizer_cli, optimizer_cli.category_summary_group, optimizer_cli.list_categories, "list")

# oci optimizer enrollment-status-summary list-enrollment-statuses
# oci optimizer enrollment-status-summary list
cli_util.rename_command(optimizer_cli, optimizer_cli.enrollment_status_summary_group, optimizer_cli.list_enrollment_statuses, "list")

# oci optimizer history-summary list-histories
# oci optimizer history-summary list
cli_util.rename_command(optimizer_cli, optimizer_cli.history_summary_group, optimizer_cli.list_histories, "list")

# oci optimizer profile-summary list-profiles
# oci optimizer profile-summary list
cli_util.rename_command(optimizer_cli, optimizer_cli.profile_summary_group, optimizer_cli.list_profiles, "list")

# oci optimizer recommendation-summary list-recommendations
# oci optimizer recommendation-summary list
cli_util.rename_command(optimizer_cli, optimizer_cli.recommendation_summary_group, optimizer_cli.list_recommendations, "list")

# oci optimizer resource-action-summary list-resource-actions
# oci optimizer resource-action-summary list
cli_util.rename_command(optimizer_cli, optimizer_cli.resource_action_summary_group, optimizer_cli.list_resource_actions, "list")
