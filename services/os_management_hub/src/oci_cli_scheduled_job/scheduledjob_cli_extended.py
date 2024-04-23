# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.os_management_hub.src.oci_cli_scheduled_job.generated import scheduledjob_cli
from services.os_management_hub.src.oci_cli_os_management_hub.generated import os_management_hub_service_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci os-management-hub scheduled-job scheduled-job run-scheduled-job-now -> oci os-management-hub scheduled-job scheduled-job run-now
cli_util.rename_command(scheduledjob_cli, scheduledjob_cli.scheduled_job_group, scheduledjob_cli.run_scheduled_job_now, "run-now")


# Move commands under 'oci os-management-hub scheduled-job scheduled-job' -> 'oci os-management-hub scheduled-job'
scheduledjob_cli.scheduled_job_root_group.commands.pop(scheduledjob_cli.scheduled_job_group.name)
os_management_hub_service_cli.os_management_hub_service_group.commands.pop(scheduledjob_cli.scheduled_job_root_group.name)
os_management_hub_service_cli.os_management_hub_service_group.add_command(scheduledjob_cli.scheduled_job_group)


@cli_util.copy_params_from_generated_command(scheduledjob_cli.create_scheduled_job, params_to_exclude=['managed_instance_group_ids', 'lifecycle_stage_ids', 'is_managed_by_autonomous_linux'])
@scheduledjob_cli.scheduled_job_group.command(name=scheduledjob_cli.create_scheduled_job.name, help=scheduledjob_cli.create_scheduled_job.help)
@cli_util.option('--is-managed-by-alx', type=click.BOOL, help="""Indicates whether this scheduled job is managed by the Autonomous Linux service.""")
@cli_util.option('--group-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of managed instance group OCIDs this scheduled job operates on. Either this or managedInstanceIds, or managedCompartmentIds, or lifecycleStageIds must be supplied.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--stage-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of lifecycle stage OCIDs this scheduled job operates on. Either this or managedInstanceIds, or managedInstanceGroupIds, or managedCompartmentIds must be supplied.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'managed-instance-ids': {'module': 'os_management_hub', 'class': 'list[string]'}, 'group-ids': {'module': 'os_management_hub', 'class': 'list[string]'}, 'managed-compartment-ids': {'module': 'os_management_hub', 'class': 'list[string]'}, 'stage-ids': {'module': 'os_management_hub', 'class': 'list[string]'}, 'operations': {'module': 'os_management_hub', 'class': 'list[ScheduledJobOperation]'}, 'freeform-tags': {'module': 'os_management_hub', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'os_management_hub', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'os_management_hub', 'class': 'ScheduledJob'})
@cli_util.wrap_exceptions
def create_scheduled_job_extended(ctx, **kwargs):

    if 'is_managed_by_alx' in kwargs:
        kwargs['is_managed_by_autonomous_linux'] = kwargs['is_managed_by_alx']
        kwargs.pop('is_managed_by_alx')

    if 'group_ids' in kwargs:
        kwargs['managed_instance_group_ids'] = kwargs['group_ids']
        kwargs.pop('group_ids')

    if 'stage_ids' in kwargs:
        kwargs['lifecycle_stage_ids'] = kwargs['stage_ids']
        kwargs.pop('stage_ids')

    ctx.invoke(scheduledjob_cli.create_scheduled_job, **kwargs)


@cli_util.copy_params_from_generated_command(scheduledjob_cli.list_scheduled_jobs, params_to_exclude=['managed_instance_group_id', 'lifecycle_stage_id', 'id', 'is_managed_by_autonomous_linux', 'location_not_equal_to'])
@scheduledjob_cli.scheduled_job_group.command(name=scheduledjob_cli.list_scheduled_jobs.name, help=scheduledjob_cli.list_scheduled_jobs.help)
@cli_util.option('--is-managed-by-alx', type=click.BOOL, help="""Indicates whether to list only resources managed by the Autonomous Linux service.""")
@cli_util.option('--location-ne', type=custom_types.CliCaseInsensitiveChoice(["ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", "GCP"]), multiple=True, help="""A filter to return only resources whose location does not match the given value.""")
@cli_util.option('--group-id', help=u"""The OCID of the managed instance group for which to list resources.""")
@cli_util.option('--stage-id', help=u"""The OCID of the lifecycle stage for which to list resources.""")
@cli_util.option('--scheduled-job-id', help=u"""The OCID of the scheduled job.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management_hub', 'class': 'ScheduledJobCollection'})
@cli_util.wrap_exceptions
def list_scheduled_jobs_extended(ctx, **kwargs):

    if 'is_managed_by_alx' in kwargs:
        kwargs['is_managed_by_autonomous_linux'] = kwargs['is_managed_by_alx']
        kwargs.pop('is_managed_by_alx')
    if 'location_ne' in kwargs:
        kwargs['location_not_equal_to'] = kwargs['location_ne']
        kwargs.pop('location_ne')

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    if 'stage_id' in kwargs:
        kwargs['lifecycle_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')

    if 'scheduled_job_id' in kwargs:
        kwargs['id'] = kwargs['scheduled_job_id']
        kwargs.pop('scheduled_job_id')

    ctx.invoke(scheduledjob_cli.list_scheduled_jobs, **kwargs)
