# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.fleet_software_update.src.oci_cli_fleet_software_update.generated import fleetsoftwareupdate_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci fleet-software-update fsu-action create-fsu-action-create-apply-action-details -> oci fleet-software-update fsu-action create-apply
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_action_group, fleetsoftwareupdate_cli.create_fsu_action_create_apply_action_details, "create-apply")


# oci fleet-software-update fsu-action create-fsu-action-create-cleanup-action-details -> oci fleet-software-update fsu-action create-cleanup
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_action_group, fleetsoftwareupdate_cli.create_fsu_action_create_cleanup_action_details, "create-cleanup")


# oci fleet-software-update fsu-action create-fsu-action-create-precheck-action-details -> oci fleet-software-update fsu-action create-precheck
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_action_group, fleetsoftwareupdate_cli.create_fsu_action_create_precheck_action_details, "create-precheck")


# oci fleet-software-update fsu-action create-fsu-action-create-rollback-action-details -> oci fleet-software-update fsu-action create-rollback
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_action_group, fleetsoftwareupdate_cli.create_fsu_action_create_rollback_action_details, "create-rollback")


# oci fleet-software-update fsu-action create-fsu-action-create-stage-action-details -> oci fleet-software-update fsu-action create-stage
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_action_group, fleetsoftwareupdate_cli.create_fsu_action_create_stage_action_details, "create-stage")


# oci fleet-software-update fsu-action get-fsu-action-output-content -> oci fleet-software-update fsu-action get-output-content
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_action_group, fleetsoftwareupdate_cli.get_fsu_action_output_content, "get-output-content")


# oci fleet-software-update fsu-action update-fsu-action-update-apply-action-details -> oci fleet-software-update fsu-action update-apply
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_action_group, fleetsoftwareupdate_cli.update_fsu_action_update_apply_action_details, "update-apply")


# oci fleet-software-update fsu-action update-fsu-action-update-cleanup-action-details -> oci fleet-software-update fsu-action update-cleanup
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_action_group, fleetsoftwareupdate_cli.update_fsu_action_update_cleanup_action_details, "update-cleanup")


# oci fleet-software-update fsu-action update-fsu-action-update-precheck-action-details -> oci fleet-software-update fsu-action update-precheck
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_action_group, fleetsoftwareupdate_cli.update_fsu_action_update_precheck_action_details, "update-precheck")


# oci fleet-software-update fsu-action update-fsu-action-update-rollback-action-details -> oci fleet-software-update fsu-action update-rollback
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_action_group, fleetsoftwareupdate_cli.update_fsu_action_update_rollback_action_details, "update-rollback")


# oci fleet-software-update fsu-action update-fsu-action-update-stage-action-details -> oci fleet-software-update fsu-action update-stage
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_action_group, fleetsoftwareupdate_cli.update_fsu_action_update_stage_action_details, "update-stage")


# oci fleet-software-update fsu-action-summary-collection -> oci fleet-software-update fsu-action-summary
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fleet_software_update_root_group, fleetsoftwareupdate_cli.fsu_action_summary_collection_group, "fsu-action-summary")


# oci fleet-software-update fsu-action-summary-collection list-fsu-actions -> oci fleet-software-update fsu-action-summary-collection list
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_action_summary_collection_group, fleetsoftwareupdate_cli.list_fsu_actions, "list")


# oci fleet-software-update fsu-collection add -> oci fleet-software-update fsu-collection add-targets
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_collection_group, fleetsoftwareupdate_cli.add_fsu_collection_targets, "add-targets")


# oci fleet-software-update fsu-collection create-fsu-collection-create-db-fsu-collection-details -> oci fleet-software-update fsu-collection create-db
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_collection_group, fleetsoftwareupdate_cli.create_fsu_collection_create_db_fsu_collection_details, "create-db")


# oci fleet-software-update fsu-collection create-fsu-collection-create-gi-fsu-collection-details -> oci fleet-software-update fsu-collection create-gi
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_collection_group, fleetsoftwareupdate_cli.create_fsu_collection_create_gi_fsu_collection_details, "create-gi")


# oci fleet-software-update fsu-collection remove-fsu-collection-targets-target-ids-remove-targets-details -> oci fleet-software-update fsu-collection remove-targets
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_collection_group, fleetsoftwareupdate_cli.remove_fsu_collection_targets_target_ids_remove_targets_details, "remove-targets")


# oci fleet-software-update fsu-collection-summary-collection -> oci fleet-software-update fsu-collection-summary
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fleet_software_update_root_group, fleetsoftwareupdate_cli.fsu_collection_summary_collection_group, "fsu-collection-summary")


# oci fleet-software-update fsu-collection-summary-collection list-fsu-collections -> oci fleet-software-update fsu-collection-summary-collection list
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_collection_summary_collection_group, fleetsoftwareupdate_cli.list_fsu_collections, "list")


# oci fleet-software-update fsu-cycle create-fsu-cycle-create-patch-fsu-cycle -> oci fleet-software-update fsu-cycle create-patch
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_cycle_group, fleetsoftwareupdate_cli.create_fsu_cycle_create_patch_fsu_cycle, "create-patch")


# oci fleet-software-update fsu-cycle update-fsu-cycle-image-id-fsu-target-details -> oci fleet-software-update fsu-cycle update-image-id-target
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_cycle_group, fleetsoftwareupdate_cli.update_fsu_cycle_image_id_fsu_target_details, "update-image-id-target")


# oci fleet-software-update fsu-cycle update-fsu-cycle-none-batching-strategy-details -> oci fleet-software-update fsu-cycle update-none-batch
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_cycle_group, fleetsoftwareupdate_cli.update_fsu_cycle_none_batching_strategy_details, "update-none-batch")


# oci fleet-software-update fsu-cycle update-fsu-cycle-update-fifty-fifty-batching-strategy-details -> oci fleet-software-update fsu-cycle update-fifty-batch
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_cycle_group, fleetsoftwareupdate_cli.update_fsu_cycle_update_fifty_fifty_batching_strategy_details, "update-fifty-batch")


# oci fleet-software-update fsu-cycle update-fsu-cycle-update-non-rolling-batching-strategy-details -> oci fleet-software-update fsu-cycle update-non-rolling-batch
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_cycle_group, fleetsoftwareupdate_cli.update_fsu_cycle_update_non_rolling_batching_strategy_details, "update-non-rolling-batch")


# oci fleet-software-update fsu-cycle update-fsu-cycle-update-patch-fsu-cycle -> oci fleet-software-update fsu-cycle update-patch
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_cycle_group, fleetsoftwareupdate_cli.update_fsu_cycle_update_patch_fsu_cycle, "update-patch")


# oci fleet-software-update fsu-cycle update-fsu-cycle-update-sequential-batching-strategy-details -> oci fleet-software-update fsu-cycle update-sequential-batch
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_cycle_group, fleetsoftwareupdate_cli.update_fsu_cycle_update_sequential_batching_strategy_details, "update-sequential-batch")


# oci fleet-software-update fsu-cycle update-fsu-cycle-update-service-availability-factor-batching-strategy-details -> oci fleet-software-update fsu-cycle update-saf-batch
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_cycle_group, fleetsoftwareupdate_cli.update_fsu_cycle_update_service_availability_factor_batching_strategy_details, "update-saf-batch")


# oci fleet-software-update fsu-cycle update-fsu-cycle-version-fsu-target-details -> oci fleet-software-update fsu-cycle update-version-target
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_cycle_group, fleetsoftwareupdate_cli.update_fsu_cycle_version_fsu_target_details, "update-version-target")


# oci fleet-software-update fsu-cycle-summary list-fsu-cycles -> oci fleet-software-update fsu-cycle-summary list
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_cycle_summary_group, fleetsoftwareupdate_cli.list_fsu_cycles, "list")


# oci fleet-software-update fsu-discovery create-fsu-discovery-db-discovery-details -> oci fleet-software-update fsu-discovery create-db
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_discovery_group, fleetsoftwareupdate_cli.create_fsu_discovery_db_discovery_details, "create-db")


# oci fleet-software-update fsu-discovery create-fsu-discovery-gi-discovery-details -> oci fleet-software-update fsu-discovery create-gi
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_discovery_group, fleetsoftwareupdate_cli.create_fsu_discovery_gi_discovery_details, "create-gi")


# oci fleet-software-update fsu-discovery-summary list-fsu-discoveries -> oci fleet-software-update fsu-discovery-summary list
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_discovery_summary_group, fleetsoftwareupdate_cli.list_fsu_discoveries, "list")


# oci fleet-software-update fsu-job get-fsu-job-output-content -> oci fleet-software-update fsu-job get-output-content
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_job_group, fleetsoftwareupdate_cli.get_fsu_job_output_content, "get-output-content")


# oci fleet-software-update fsu-job-output-summary list-fsu-job-outputs -> oci fleet-software-update fsu-job-output-summary list
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_job_output_summary_group, fleetsoftwareupdate_cli.list_fsu_job_outputs, "list")


# oci fleet-software-update fsu-job-summary list-fsu-jobs -> oci fleet-software-update fsu-job-summary list
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_job_summary_group, fleetsoftwareupdate_cli.list_fsu_jobs, "list")


# oci fleet-software-update target-summary-collection list-fsu-collection-targets -> oci fleet-software-update target-summary-collection list-collection
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.target_summary_collection_group, fleetsoftwareupdate_cli.list_fsu_collection_targets, "list-collection")


# oci fleet-software-update target-summary-collection list-fsu-discovery-targets -> oci fleet-software-update target-summary-collection list-discovery
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.target_summary_collection_group, fleetsoftwareupdate_cli.list_fsu_discovery_targets, "list-discovery")


# oci fleet-software-update work-request-log-entry list-work-request-logs -> oci fleet-software-update work-request-log-entry list
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.work_request_log_entry_group, fleetsoftwareupdate_cli.list_work_request_logs, "list")


@cli_util.copy_params_from_generated_command(fleetsoftwareupdate_cli.create_fsu_cycle_create_patch_fsu_cycle, params_to_exclude=['max_drain_timeout_in_seconds'])
@fleetsoftwareupdate_cli.fsu_cycle_group.command(name=fleetsoftwareupdate_cli.create_fsu_cycle_create_patch_fsu_cycle.name, help=fleetsoftwareupdate_cli.create_fsu_cycle_create_patch_fsu_cycle.help)
@cli_util.option('--max-drain-timeout-in-sec', type=click.INT, help=u"""Service drain timeout specified in seconds.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'goal-version-details': {'module': 'fleet_software_update', 'class': 'FsuGoalVersionDetails'}, 'batching-strategy': {'module': 'fleet_software_update', 'class': 'CreateBatchingStrategyDetails'}, 'stage-action-schedule': {'module': 'fleet_software_update', 'class': 'CreateScheduleDetails'}, 'apply-action-schedule': {'module': 'fleet_software_update', 'class': 'CreateScheduleDetails'}, 'freeform-tags': {'module': 'fleet_software_update', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'fleet_software_update', 'class': 'dict(str, dict(str, object))'}, 'is-ignore-missing-patches': {'module': 'fleet_software_update', 'class': 'list[string]'}}, output_type={'module': 'fleet_software_update', 'class': 'FsuCycle'})
@cli_util.wrap_exceptions
def create_fsu_cycle_create_patch_fsu_cycle_extended(ctx, **kwargs):

    if 'max_drain_timeout_in_sec' in kwargs:
        kwargs['max_drain_timeout_in_seconds'] = kwargs['max_drain_timeout_in_sec']
        kwargs.pop('max_drain_timeout_in_sec')

    ctx.invoke(fleetsoftwareupdate_cli.create_fsu_cycle_create_patch_fsu_cycle, **kwargs)


@cli_util.copy_params_from_generated_command(fleetsoftwareupdate_cli.update_fsu_cycle_image_id_fsu_target_details, params_to_exclude=['goal_version_details_software_image_id', 'goal_version_details_home_policy', 'goal_version_details_new_home_prefix'])
@fleetsoftwareupdate_cli.fsu_cycle_group.command(name=fleetsoftwareupdate_cli.update_fsu_cycle_image_id_fsu_target_details.name, help=fleetsoftwareupdate_cli.update_fsu_cycle_image_id_fsu_target_details.help)
@cli_util.option('--gvd-software-image-id', required=True, help=u"""Target database software image OCID. [required]""")
@cli_util.option('--gvd-home-policy', type=custom_types.CliCaseInsensitiveChoice(["CREATE_NEW", "USE_EXITING"]), help=u"""Goal home policy to use when Staging the Goal Version during patching. CREATE_NEW: Create a new DBHome (for Database Collections) for the specified image or version. USE_EXITING: All database targets in the same VMCluster or CloudVmCluster will be moved to a shared database home.   If an existing home for the selected image or version is not found in the VM Cluster for a target database, then a new home will be created.   If more than one existing home for the selected image is found, then the home with the least number of databases will be used.   If multiple homes have the least number of databases, then a home will be selected at random.""")
@cli_util.option('--gvd-new-home-prefix', help=u"""Prefix name used for new DB home resources created as part of the Stage Action. Format: <specified_prefix>_<timestamp> If not specified, a default OCI DB home resource will be generated for the new DB home resources created.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'batching-strategy': {'module': 'fleet_software_update', 'class': 'UpdateBatchingStrategyDetails'}, 'freeform-tags': {'module': 'fleet_software_update', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'fleet_software_update', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_fsu_cycle_image_id_fsu_target_details_extended(ctx, **kwargs):

    if 'gvd_software_image_id' in kwargs:
        kwargs['goal_version_details_software_image_id'] = kwargs['gvd_software_image_id']
        kwargs.pop('gvd_software_image_id')

    if 'gvd_home_policy' in kwargs:
        kwargs['goal_version_details_home_policy'] = kwargs['gvd_home_policy']
        kwargs.pop('gvd_home_policy')

    if 'gvd_new_home_prefix' in kwargs:
        kwargs['goal_version_details_new_home_prefix'] = kwargs['gvd_new_home_prefix']
        kwargs.pop('gvd_new_home_prefix')

    ctx.invoke(fleetsoftwareupdate_cli.update_fsu_cycle_image_id_fsu_target_details, **kwargs)


@cli_util.copy_params_from_generated_command(fleetsoftwareupdate_cli.update_fsu_cycle_update_fifty_fifty_batching_strategy_details, params_to_exclude=['batching_strategy_is_force_rolling', 'batching_strategy_is_wait_for_batch_resume'])
@fleetsoftwareupdate_cli.fsu_cycle_group.command(name=fleetsoftwareupdate_cli.update_fsu_cycle_update_fifty_fifty_batching_strategy_details.name, help=fleetsoftwareupdate_cli.update_fsu_cycle_update_fifty_fifty_batching_strategy_details.help)
@cli_util.option('--batch-is-force-rolling', type=click.BOOL, help=u"""True to force rolling patching.""")
@cli_util.option('--batch-is-wait-f-batch-res', type=click.BOOL, help=u"""True to wait for customer to resume the Apply Action once the first half is done. False to automatically patch the second half.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'goal-version-details': {'module': 'fleet_software_update', 'class': 'FsuGoalVersionDetails'}, 'freeform-tags': {'module': 'fleet_software_update', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'fleet_software_update', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_fsu_cycle_update_fifty_fifty_batching_strategy_details_extended(ctx, **kwargs):

    if 'batch_is_force_rolling' in kwargs:
        kwargs['batching_strategy_is_force_rolling'] = kwargs['batch_is_force_rolling']
        kwargs.pop('batch_is_force_rolling')

    if 'batch_is_wait_f_batch_res' in kwargs:
        kwargs['batching_strategy_is_wait_for_batch_resume'] = kwargs['batch_is_wait_f_batch_res']
        kwargs.pop('batch_is_wait_f_batch_res')

    ctx.invoke(fleetsoftwareupdate_cli.update_fsu_cycle_update_fifty_fifty_batching_strategy_details, **kwargs)


@cli_util.copy_params_from_generated_command(fleetsoftwareupdate_cli.update_fsu_cycle_update_patch_fsu_cycle, params_to_exclude=['max_drain_timeout_in_seconds'])
@fleetsoftwareupdate_cli.fsu_cycle_group.command(name=fleetsoftwareupdate_cli.update_fsu_cycle_update_patch_fsu_cycle.name, help=fleetsoftwareupdate_cli.update_fsu_cycle_update_patch_fsu_cycle.help)
@cli_util.option('---max-drain-timeout-in-sec', type=click.INT, help=u"""Service drain timeout specified in seconds.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'goal-version-details': {'module': 'fleet_software_update', 'class': 'FsuGoalVersionDetails'}, 'batching-strategy': {'module': 'fleet_software_update', 'class': 'UpdateBatchingStrategyDetails'}, 'freeform-tags': {'module': 'fleet_software_update', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'fleet_software_update', 'class': 'dict(str, dict(str, object))'}, 'is-ignore-missing-patches': {'module': 'fleet_software_update', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_fsu_cycle_update_patch_fsu_cycle_extended(ctx, **kwargs):

    if '_max_drain_timeout_in_sec' in kwargs:
        kwargs['max_drain_timeout_in_seconds'] = kwargs['_max_drain_timeout_in_sec']
        kwargs.pop('_max_drain_timeout_in_sec')

    ctx.invoke(fleetsoftwareupdate_cli.update_fsu_cycle_update_patch_fsu_cycle, **kwargs)


@cli_util.copy_params_from_generated_command(fleetsoftwareupdate_cli.update_fsu_cycle_update_sequential_batching_strategy_details, params_to_exclude=['batching_strategy_is_force_rolling'])
@fleetsoftwareupdate_cli.fsu_cycle_group.command(name=fleetsoftwareupdate_cli.update_fsu_cycle_update_sequential_batching_strategy_details.name, help=fleetsoftwareupdate_cli.update_fsu_cycle_update_sequential_batching_strategy_details.help)
@cli_util.option('--batch-is-force-rolling', type=click.BOOL, help=u"""True to force rolling patching.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'goal-version-details': {'module': 'fleet_software_update', 'class': 'FsuGoalVersionDetails'}, 'freeform-tags': {'module': 'fleet_software_update', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'fleet_software_update', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_fsu_cycle_update_sequential_batching_strategy_details_extended(ctx, **kwargs):

    if 'batch_is_force_rolling' in kwargs:
        kwargs['batching_strategy_is_force_rolling'] = kwargs['batch_is_force_rolling']
        kwargs.pop('batch_is_force_rolling')

    ctx.invoke(fleetsoftwareupdate_cli.update_fsu_cycle_update_sequential_batching_strategy_details, **kwargs)


@cli_util.copy_params_from_generated_command(fleetsoftwareupdate_cli.update_fsu_cycle_update_service_availability_factor_batching_strategy_details, params_to_exclude=['batching_strategy_is_force_rolling', 'batching_strategy_percentage'])
@fleetsoftwareupdate_cli.fsu_cycle_group.command(name=fleetsoftwareupdate_cli.update_fsu_cycle_update_service_availability_factor_batching_strategy_details.name, help=fleetsoftwareupdate_cli.update_fsu_cycle_update_service_availability_factor_batching_strategy_details.help)
@cli_util.option('--batch-is-force-rolling', type=click.BOOL, help=u"""True to force rolling patching.""")
@cli_util.option('--batch-percentage', type=click.INT, help=u"""Percentage of availability in the service during the Patch operation.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'goal-version-details': {'module': 'fleet_software_update', 'class': 'FsuGoalVersionDetails'}, 'freeform-tags': {'module': 'fleet_software_update', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'fleet_software_update', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_fsu_cycle_update_service_availability_factor_batching_strategy_details_extended(ctx, **kwargs):

    if 'batch_is_force_rolling' in kwargs:
        kwargs['batching_strategy_is_force_rolling'] = kwargs['batch_is_force_rolling']
        kwargs.pop('batch_is_force_rolling')

    if 'batch_percentage' in kwargs:
        kwargs['batching_strategy_percentage'] = kwargs['batch_percentage']
        kwargs.pop('batch_percentage')

    ctx.invoke(fleetsoftwareupdate_cli.update_fsu_cycle_update_service_availability_factor_batching_strategy_details, **kwargs)


@cli_util.copy_params_from_generated_command(fleetsoftwareupdate_cli.update_fsu_cycle_version_fsu_target_details, params_to_exclude=['goal_version_details_version', 'goal_version_details_home_policy', 'goal_version_details_new_home_prefix'])
@fleetsoftwareupdate_cli.fsu_cycle_group.command(name=fleetsoftwareupdate_cli.update_fsu_cycle_version_fsu_target_details.name, help=fleetsoftwareupdate_cli.update_fsu_cycle_version_fsu_target_details.help)
@cli_util.option('--gvd-version', required=True, help=u"""Target DB or GI version string for the Exadata Fleet Update Cycle. [required]""")
@cli_util.option('--gvd-home-policy', type=custom_types.CliCaseInsensitiveChoice(["CREATE_NEW", "USE_EXITING"]), help=u"""Goal home policy to use when Staging the Goal Version during patching. CREATE_NEW: Create a new DBHome (for Database Collections) for the specified image or version. USE_EXITING: All database targets in the same VMCluster or CloudVmCluster will be moved to a shared database home.   If an existing home for the selected image or version is not found in the VM Cluster for a target database, then a new home will be created.   If more than one existing home for the selected image is found, then the home with the least number of databases will be used.   If multiple homes have the least number of databases, then a home will be selected at random.""")
@cli_util.option('--gvd-new-home-prefix', help=u"""Prefix name used for new DB home resources created as part of the Stage Action. Format: <specified_prefix>_<timestamp> If not specified, a default OCI DB home resource will be generated for the new DB home resources created.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'batching-strategy': {'module': 'fleet_software_update', 'class': 'UpdateBatchingStrategyDetails'}, 'freeform-tags': {'module': 'fleet_software_update', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'fleet_software_update', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_fsu_cycle_version_fsu_target_details_extended(ctx, **kwargs):

    if 'gvd_version' in kwargs:
        kwargs['goal_version_details_version'] = kwargs['gvd_version']
        kwargs.pop('gvd_version')

    if 'gvd_home_policy' in kwargs:
        kwargs['goal_version_details_home_policy'] = kwargs['gvd_home_policy']
        kwargs.pop('gvd_home_policy')

    if 'gvd_new_home_prefix' in kwargs:
        kwargs['goal_version_details_new_home_prefix'] = kwargs['gvd_new_home_prefix']
        kwargs.pop('gvd_new_home_prefix')

    ctx.invoke(fleetsoftwareupdate_cli.update_fsu_cycle_version_fsu_target_details, **kwargs)


# oci fleet-software-update fsu-collection create-fsu-collection-create-guest-os-fsu-collection-details -> oci fleet-software-update fsu-collection create-guest-os
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_collection_group, fleetsoftwareupdate_cli.create_fsu_collection_create_guest_os_fsu_collection_details, "create-guest-os")


# oci fleet-software-update fsu-discovery create-fsu-discovery-guest-os-discovery-details -> oci fleet-software-update fsu-discovery create-guest-os
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_discovery_group, fleetsoftwareupdate_cli.create_fsu_discovery_guest_os_discovery_details, "create-guest-os")


# oci fleet-software-update fsu-collection create-fsu-collection-create-exadb-stack-fsu-collection-details -> oci fleet-software-update fsu-collection create-exadb-stack
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_collection_group, fleetsoftwareupdate_cli.create_fsu_collection_create_exadb_stack_fsu_collection_details, "create-exadb-stack")


# oci fleet-software-update fsu-discovery create-fsu-discovery-exadb-stack-discovery-details -> oci fleet-software-update fsu-discovery create-exadb-stack
cli_util.rename_command(fleetsoftwareupdate_cli, fleetsoftwareupdate_cli.fsu_discovery_group, fleetsoftwareupdate_cli.create_fsu_discovery_exadb_stack_discovery_details, "create-exadb-stack")
