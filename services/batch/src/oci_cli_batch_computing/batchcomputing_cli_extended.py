# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.batch.src.oci_cli_batch_computing.generated import batchcomputing_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci batch batch-context-collection list-batch-contexts -> oci batch batch-context-collection list
cli_util.rename_command(batchcomputing_cli, batchcomputing_cli.batch_context_collection_group, batchcomputing_cli.list_batch_contexts, "list")


# oci batch batch-context create-batch-context-oci-logging-configuration -> oci batch batch-context create-oci-logging-configuration
cli_util.rename_command(batchcomputing_cli, batchcomputing_cli.batch_context_group, batchcomputing_cli.create_batch_context_oci_logging_configuration, "create-oci-logging-configuration")


# oci batch batch-context-shape-collection list-batch-context-shapes -> oci batch batch-context-shape-collection list
cli_util.rename_command(batchcomputing_cli, batchcomputing_cli.batch_context_shape_collection_group, batchcomputing_cli.list_batch_context_shapes, "list")


# oci batch batch-job-collection list-batch-jobs -> oci batch batch-job-collection list
cli_util.rename_command(batchcomputing_cli, batchcomputing_cli.batch_job_collection_group, batchcomputing_cli.list_batch_jobs, "list")


# oci batch batch-task-collection list-batch-job-tasks -> oci batch batch-task-collection list
cli_util.rename_command(batchcomputing_cli, batchcomputing_cli.batch_task_collection_group, batchcomputing_cli.list_batch_job_tasks, "list")


# oci batch batch-task-environment-collection list-batch-task-environments -> oci batch batch-task-environment-collection list
cli_util.rename_command(batchcomputing_cli, batchcomputing_cli.batch_task_environment_collection_group, batchcomputing_cli.list_batch_task_environments, "list")


# oci batch batch-task-profile-collection list-batch-task-profiles -> oci batch batch-task-profile-collection list
cli_util.rename_command(batchcomputing_cli, batchcomputing_cli.batch_task_profile_collection_group, batchcomputing_cli.list_batch_task_profiles, "list")


# oci batch batch-job-pool-collection list_batch_job_pools -> oci batch batch-job-pool  list
cli_util.rename_command(batchcomputing_cli, batchcomputing_cli.batch_job_pool_collection_group, batchcomputing_cli.list_batch_job_pools, "list")


# Move commands under 'oci batch batch-context-collection' -> 'oci batch batch-context'
batchcomputing_cli.batch_root_group.commands.pop(batchcomputing_cli.batch_context_collection_group.name)
batchcomputing_cli.batch_context_group.add_command(batchcomputing_cli.list_batch_contexts)


# Move commands under 'oci batch batch-job-collection' -> 'oci batch batch-job'
batchcomputing_cli.batch_root_group.commands.pop(batchcomputing_cli.batch_job_collection_group.name)
batchcomputing_cli.batch_job_group.add_command(batchcomputing_cli.list_batch_jobs)


# Move commands under 'oci batch batch-task-collection' -> 'oci batch batch-task'
batchcomputing_cli.batch_root_group.commands.pop(batchcomputing_cli.batch_task_collection_group.name)
batchcomputing_cli.batch_task_group.add_command(batchcomputing_cli.list_batch_job_tasks)
batchcomputing_cli.batch_task_group.add_command(batchcomputing_cli.list_batch_tasks)


# Move commands under 'oci batch batch-task-environment-collection' -> 'oci batch batch-task-environment'
batchcomputing_cli.batch_root_group.commands.pop(batchcomputing_cli.batch_task_environment_collection_group.name)
batchcomputing_cli.batch_task_environment_group.add_command(batchcomputing_cli.list_batch_task_environments)


# Move commands under 'oci batch batch-task-profile-collection' -> 'oci batch batch-task-profile'
batchcomputing_cli.batch_root_group.commands.pop(batchcomputing_cli.batch_task_profile_collection_group.name)
batchcomputing_cli.batch_task_profile_group.add_command(batchcomputing_cli.list_batch_task_profiles)


# Move commands under 'oci batch batch-job-pool-collection' -> 'oci batch batch-job-pool'
batchcomputing_cli.batch_root_group.commands.pop(batchcomputing_cli.batch_job_pool_collection_group.name)
batchcomputing_cli.batch_job_pool_group.add_command(batchcomputing_cli.list_batch_job_pools)


@cli_util.copy_params_from_generated_command(batchcomputing_cli.create_batch_context_oci_logging_configuration, params_to_exclude=['logging_configuration_log_group_id', 'logging_configuration_log_id'])
@batchcomputing_cli.batch_context_group.command(name=batchcomputing_cli.create_batch_context_oci_logging_configuration.name, help=batchcomputing_cli.create_batch_context_oci_logging_configuration.help)
@cli_util.option('--log-group-id', required=True, help=u"""The [OCID] of the log group. [required]""")
@cli_util.option('--log-id', required=True, help=u"""The [OCID] of the log. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'batch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'batch', 'class': 'dict(str, dict(str, object))'}, 'job-priority-configurations': {'module': 'batch', 'class': 'list[JobPriorityConfiguration]'}, 'network': {'module': 'batch', 'class': 'CreateNetworkDetails'}, 'fleets': {'module': 'batch', 'class': 'list[CreateFleetDetails]'}, 'entitlements': {'module': 'batch', 'class': 'dict(str, integer)'}}, output_type={'module': 'batch', 'class': 'BatchContext'})
@cli_util.wrap_exceptions
def create_batch_context_oci_logging_configuration_extended(ctx, **kwargs):

    if 'log_group_id' in kwargs:
        kwargs['logging_configuration_log_group_id'] = kwargs['log_group_id']
        kwargs.pop('log_group_id')

    if 'log_id' in kwargs:
        kwargs['logging_configuration_log_id'] = kwargs['log_id']
        kwargs.pop('log_id')

    ctx.invoke(batchcomputing_cli.create_batch_context_oci_logging_configuration, **kwargs)
