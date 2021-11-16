# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401
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


@cli_util.copy_params_from_generated_command(optimizer_cli.filter_resource_actions, params_to_exclude=['query_parameterconflict'])
@optimizer_cli.resource_action_summary_group.command(name=optimizer_cli.filter_resource_actions.name, help=optimizer_cli.filter_resource_actions.help)
@cli_util.option('--filter-query', help=u"""The query describing which resources to search for. For more information, see [Query Language Syntax].""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'optimizer', 'class': 'ResourceActionCollection'})
@cli_util.wrap_exceptions
def filter_resource_actions_extended(ctx, **kwargs):
    if 'filter_query' in kwargs:
        kwargs['query_parameterconflict'] = kwargs['filter_query']
        kwargs.pop('filter_query')

    ctx.invoke(optimizer_cli.filter_resource_actions, **kwargs)
