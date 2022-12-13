# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import click
from oci_cli import json_skeleton_utils, cli_util

from services.media_services.src.oci_cli_media_services.generated import mediaservices_cli

# exclude media-workflow-job-fact command
mediaservices_cli.media_services_service_cli.media_services_service_group.commands.pop(mediaservices_cli.media_workflow_job_fact_group.name)


# Rename the version-parameterconflict to avoid conflict
@cli_util.copy_params_from_generated_command(mediaservices_cli.delete_media_asset_distribution_channel_attachment,
                                             params_to_exclude=['version_parameterconflict'])
@mediaservices_cli.media_asset_distribution_channel_attachment_group.command(name=cli_util.override('media_services.delete_media_asset_distribution_channel_attachment.command_name', 'delete'), help=u"""Deletes a MediaAsset from DistributionChannel by identifiers \n[Command Reference](deleteMediaAssetDistributionChannelAttachment)""")
@cli_util.option('--madc-attachment-version', type=click.INT, help=u"""version of the attachment""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_delete_madc_attachment_version(ctx, **kwargs):
    if 'madc_attachment_version' in kwargs:
        kwargs['version_parameterconflict'] = kwargs['madc_attachment_version']
        kwargs.pop('madc_attachment_version')
    ctx.invoke(mediaservices_cli.delete_media_asset_distribution_channel_attachment, **kwargs)


@cli_util.copy_params_from_generated_command(mediaservices_cli.get_media_asset_distribution_channel_attachment,
                                             params_to_exclude=['version_parameterconflict'])
@mediaservices_cli.media_asset_distribution_channel_attachment_group.command(name=cli_util.override('media_services.get_media_asset_distribution_channel_attachment.command_name', 'get'), help=u"""Gets a MediaAssetDistributionChannelAttachment for a MediaAsset by identifiers \n[Command Reference](getMediaAssetDistributionChannelAttachment)""")
@cli_util.option('--madc-attachment-version', type=click.INT, help=u"""version of the attachment""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'media_services', 'class': 'MediaAssetDistributionChannelAttachment'})
@cli_util.wrap_exceptions
def update_get_madc_attachment_version(ctx, **kwargs):
    if 'madc_attachment_version' in kwargs:
        kwargs['version_parameterconflict'] = kwargs['madc_attachment_version']
        kwargs.pop('madc_attachment_version')
    ctx.invoke(mediaservices_cli.get_media_asset_distribution_channel_attachment, **kwargs)


# oci media-services media-workflow-task-declaration-collection list-media-workflow-task-declarations -> oci media-services media-workflow-task-declaration-collection list
cli_util.rename_command(mediaservices_cli, mediaservices_cli.media_workflow_task_declaration_collection_group, mediaservices_cli.list_media_workflow_task_declarations, "list")


# oci media-services media-workflow-task-declaration-collection -> oci media-services media-workflow-task-declaration
cli_util.rename_command(mediaservices_cli.media_services_service_cli, mediaservices_cli.media_services_service_cli.media_services_service_group, mediaservices_cli.media_workflow_task_declaration_collection_group, "media-workflow-task-declaration")


@cli_util.copy_params_from_generated_command(mediaservices_cli.list_media_workflow_task_declarations,
                                             params_to_exclude=['version_parameterconflict'])
@mediaservices_cli.media_workflow_task_declaration_collection_group.command(name=cli_util.override('media_services.list_media_workflow_task_declarations.command_name', 'list-media-workflow-task-declarations'), help=u"""Returns a list of MediaWorkflowTaskDeclarations. \n[Command Reference](listMediaWorkflowTaskDeclarations)""")
@cli_util.option('--task-declaration-version', type=click.INT, help=u"""A filter to select MediaWorkflowTaskDeclaration by version""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'media_services', 'class': 'MediaWorkflowTaskDeclarationCollection'})
@cli_util.wrap_exceptions
def update_list_media_workflow_task_declarations_version(ctx, **kwargs):
    if 'task_declaration_version' in kwargs:
        kwargs['version_parameterconflict'] = kwargs['task_declaration_version']
        kwargs.pop('task_declaration_version')
    ctx.invoke(mediaservices_cli.list_media_workflow_task_declarations, **kwargs)


mediaservices_cli.media_workflow_job_group.commands.pop(mediaservices_cli.create_media_workflow_job.name)

cli_util.rename_command(mediaservices_cli, mediaservices_cli.media_workflow_job_group, mediaservices_cli.create_media_workflow_job_create_media_workflow_job_by_name_details, "create-media-workflow-job-by-name")

cli_util.rename_command(mediaservices_cli, mediaservices_cli.media_workflow_job_group, mediaservices_cli.create_media_workflow_job_create_media_workflow_job_by_id_details, "create-media-workflow-job-by-id")

mediaservices_cli.stream_cdn_config_group.commands.pop(mediaservices_cli.create_stream_cdn_config.name)

cli_util.rename_command(mediaservices_cli, mediaservices_cli.stream_cdn_config_group, mediaservices_cli.create_stream_cdn_config_akamai_manual_stream_cdn_config, "create-akamai-stream-cdn-config")

cli_util.rename_command(mediaservices_cli, mediaservices_cli.stream_cdn_config_group, mediaservices_cli.create_stream_cdn_config_edge_stream_cdn_config, "create-edge-stream-cdn-config")

mediaservices_cli.stream_cdn_config_group.commands.pop(mediaservices_cli.update_stream_cdn_config.name)

cli_util.rename_command(mediaservices_cli, mediaservices_cli.stream_cdn_config_group, mediaservices_cli.update_stream_cdn_config_akamai_manual_stream_cdn_config, "update-akamai-stream-cdn-config")

cli_util.rename_command(mediaservices_cli, mediaservices_cli.stream_cdn_config_group, mediaservices_cli.update_stream_cdn_config_edge_stream_cdn_config, "update-edge-stream-cdn-config")

mediaservices_cli.media_workflow_configuration_collection_group.commands.pop(mediaservices_cli.list_media_workflow_configurations.name)

mediaservices_cli.media_workflow_configuration_group.add_command(mediaservices_cli.list_media_workflow_configurations)

cli_util.rename_command(mediaservices_cli, mediaservices_cli.media_workflow_configuration_group, mediaservices_cli.list_media_workflow_configurations, "list")

mediaservices_cli.media_services_service_cli.media_services_service_group.commands.pop(mediaservices_cli.media_workflow_configuration_collection_group.name)

mediaservices_cli.media_asset_distribution_channel_attachment_collection_group.commands.pop(mediaservices_cli.list_media_asset_distribution_channel_attachments.name)

mediaservices_cli.media_asset_distribution_channel_attachment_group.add_command(mediaservices_cli.list_media_asset_distribution_channel_attachments)

cli_util.rename_command(mediaservices_cli, mediaservices_cli.media_asset_distribution_channel_attachment_group, mediaservices_cli.list_media_asset_distribution_channel_attachments, "list")

mediaservices_cli.media_services_service_cli.media_services_service_group.commands.pop(mediaservices_cli.media_asset_distribution_channel_attachment_collection_group.name)

# exclude stream-packaging-config create command
mediaservices_cli.stream_packaging_config_group.commands.pop(mediaservices_cli.create_stream_packaging_config.name)

# rename stream-packaging-config create-aes128/none
cli_util.rename_command(mediaservices_cli, mediaservices_cli.stream_packaging_config_group, mediaservices_cli.create_stream_packaging_config_stream_packaging_config_encryption_aes128, "create-stream-packaging-config-encryption-aes128")

cli_util.rename_command(mediaservices_cli, mediaservices_cli.stream_packaging_config_group, mediaservices_cli.create_stream_packaging_config_stream_packaging_config_encryption_none, "create-stream-packaging-config-encryption-none")

# Rename ingest-stream-distribution-channel-asset-metadata-entry-details to just ingest
mediaservices_cli.stream_distribution_channel_group.commands.pop(mediaservices_cli.ingest_stream_distribution_channel.name)
cli_util.rename_command(mediaservices_cli, mediaservices_cli.stream_distribution_channel_group, mediaservices_cli.ingest_stream_distribution_channel_asset_metadata_entry_details, "ingest")
