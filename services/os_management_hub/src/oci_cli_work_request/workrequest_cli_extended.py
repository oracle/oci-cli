# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401

from services.os_management_hub.src.oci_cli_os_management_hub.generated import os_management_hub_service_cli
from services.os_management_hub.src.oci_cli_work_request.generated import workrequest_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci os-management-hub work-request work-request list-work-request-errors -> oci os-management-hub work-request work-request list-errors
cli_util.rename_command(workrequest_cli, workrequest_cli.work_request_group, workrequest_cli.list_work_request_errors, "list-errors")


# oci os-management-hub work-request work-request list-work-request-logs -> oci os-management-hub work-request work-request list-logs
cli_util.rename_command(workrequest_cli, workrequest_cli.work_request_group, workrequest_cli.list_work_request_logs, "list-logs")


# Move commands under 'oci os-management-hub work-request work-request' -> 'oci os-management-hub work-request'
workrequest_cli.work_request_root_group.commands.pop(workrequest_cli.work_request_group.name)
os_management_hub_service_cli.os_management_hub_service_group.commands.pop(workrequest_cli.work_request_root_group.name)
os_management_hub_service_cli.os_management_hub_service_group.add_command(workrequest_cli.work_request_group)


@cli_util.copy_params_from_generated_command(workrequest_cli.list_work_requests, params_to_exclude=['parent_resources_not_equal_to'])
@workrequest_cli.work_request_group.command(name=workrequest_cli.list_work_requests.name, help=workrequest_cli.list_work_requests.help)
@cli_util.option('--parent-resources-ne', multiple=True, help=u"""A filter to return the resources whose parent resources are not the same as the given resource OCID(s).""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-resources-not-equal-to': {'module': 'os_management_hub', 'class': 'list[string]'}}, output_type={'module': 'os_management_hub', 'class': 'WorkRequestSummaryCollection'})
@cli_util.wrap_exceptions
def list_work_requests_extended(ctx, **kwargs):

    if 'parent_resources_ne' in kwargs:
        kwargs['parent_resources_not_equal_to'] = kwargs['parent_resources_ne']
        kwargs.pop('parent_resources_ne')

    ctx.invoke(workrequest_cli.list_work_requests, **kwargs)
