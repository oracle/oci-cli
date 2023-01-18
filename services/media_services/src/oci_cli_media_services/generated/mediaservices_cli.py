# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.media_services.src.oci_cli_media_services.generated import media_services_service_cli


@click.command(cli_util.override('media_services.media_services_root_group.command_name', 'media-services'), cls=CommandGroupWithAlias, help=cli_util.override('media_services.media_services_root_group.help', """Media Services (includes Media Flow and Media Streams) is a fully managed service for processing media (video) source content. Use Media Flow and Media Streams to transcode and package digital video using configurable workflows and stream video outputs.

Use the Media Services API to configure media workflows and run Media Flow jobs, create distribution channels, ingest assets, create Preview URLs and play assets. For more information, see [Media Flow] and [Media Streams]."""), short_help=cli_util.override('media_services.media_services_root_group.short_help', """Media Services API"""))
@cli_util.help_option_group
def media_services_root_group():
    pass


@click.command(cli_util.override('media_services.stream_packaging_config_group.command_name', 'stream-packaging-config'), cls=CommandGroupWithAlias, help="""A stream packaging configuration for a Distribution Channel.""")
@cli_util.help_option_group
def stream_packaging_config_group():
    pass


@click.command(cli_util.override('media_services.media_asset_group.command_name', 'media-asset'), cls=CommandGroupWithAlias, help="""Represents the metadata associated with an asset that has been either produced by or registered with Media Services.""")
@cli_util.help_option_group
def media_asset_group():
    pass


@click.command(cli_util.override('media_services.media_workflow_job_fact_group.command_name', 'media-workflow-job-fact'), cls=CommandGroupWithAlias, help="""One fact of a list of facts associated to a MediaWorkflowJob that presents a point-in-time snapshot of the resources, data and events that were composed to generate a runnable job. This information will be used internally to trouble-shoot problematic workflows or jobs.""")
@cli_util.help_option_group
def media_workflow_job_fact_group():
    pass


@click.command(cli_util.override('media_services.media_workflow_job_group.command_name', 'media-workflow-job'), cls=CommandGroupWithAlias, help="""A MediaWorkflowJob represents a run of a MediaWorkflow for a specific set of parameters and configurations.""")
@cli_util.help_option_group
def media_workflow_job_group():
    pass


@click.command(cli_util.override('media_services.stream_cdn_config_group.command_name', 'stream-cdn-config'), cls=CommandGroupWithAlias, help="""Configuration used for integrating with a CDN.""")
@cli_util.help_option_group
def stream_cdn_config_group():
    pass


@click.command(cli_util.override('media_services.stream_distribution_channel_group.command_name', 'stream-distribution-channel'), cls=CommandGroupWithAlias, help="""Channel used for delivering video streams to the end-users.""")
@cli_util.help_option_group
def stream_distribution_channel_group():
    pass


@click.command(cli_util.override('media_services.media_asset_distribution_channel_attachment_group.command_name', 'media-asset-distribution-channel-attachment'), cls=CommandGroupWithAlias, help="""Attachment between MediaAsset and streaming DistributionChannel.""")
@cli_util.help_option_group
def media_asset_distribution_channel_attachment_group():
    pass


@click.command(cli_util.override('media_services.media_workflow_configuration_group.command_name', 'media-workflow-configuration'), cls=CommandGroupWithAlias, help="""Resusable set of values that can be referenced either in a MediaWorkflow or when running a MediaWorkflowJob.""")
@cli_util.help_option_group
def media_workflow_configuration_group():
    pass


@click.command(cli_util.override('media_services.media_workflow_task_declaration_collection_group.command_name', 'media-workflow-task-declaration-collection'), cls=CommandGroupWithAlias, help="""Results of the ListMediaWorkflowTaskDeclaration operation, a list of MediaWorkflowTaskDeclarations.""")
@cli_util.help_option_group
def media_workflow_task_declaration_collection_group():
    pass


@click.command(cli_util.override('media_services.media_asset_distribution_channel_attachment_collection_group.command_name', 'media-asset-distribution-channel-attachment-collection'), cls=CommandGroupWithAlias, help="""Results of a MediaAssetDistributionChannelAttachment search. Contains the MediaAssetDistributionChannelAttachmentSummary items.""")
@cli_util.help_option_group
def media_asset_distribution_channel_attachment_collection_group():
    pass


@click.command(cli_util.override('media_services.media_workflow_group.command_name', 'media-workflow'), cls=CommandGroupWithAlias, help="""Configurable workflows that define the series of tasks that will be used to process video files.""")
@cli_util.help_option_group
def media_workflow_group():
    pass


@click.command(cli_util.override('media_services.media_workflow_configuration_collection_group.command_name', 'media-workflow-configuration-collection'), cls=CommandGroupWithAlias, help="""Results of a mediaWorkflowConfiguration search. Contains boh MediaWorkflowConfigurationSummary items and other information, such as metadata.""")
@cli_util.help_option_group
def media_workflow_configuration_collection_group():
    pass


media_services_service_cli.media_services_service_group.add_command(media_services_root_group)
media_services_root_group.add_command(stream_packaging_config_group)
media_services_root_group.add_command(media_asset_group)
media_services_root_group.add_command(media_workflow_job_fact_group)
media_services_root_group.add_command(media_workflow_job_group)
media_services_root_group.add_command(stream_cdn_config_group)
media_services_root_group.add_command(stream_distribution_channel_group)
media_services_root_group.add_command(media_asset_distribution_channel_attachment_group)
media_services_root_group.add_command(media_workflow_configuration_group)
media_services_root_group.add_command(media_workflow_task_declaration_collection_group)
media_services_root_group.add_command(media_asset_distribution_channel_attachment_collection_group)
media_services_root_group.add_command(media_workflow_group)
media_services_root_group.add_command(media_workflow_configuration_collection_group)
# oci media_services media_services --> oci media_services
media_services_service_cli.media_services_service_group.commands.pop(media_services_root_group.name)
media_services_service_cli.media_services_service_group.add_command(stream_packaging_config_group)
media_services_service_cli.media_services_service_group.add_command(media_asset_group)
media_services_service_cli.media_services_service_group.add_command(media_workflow_job_fact_group)
media_services_service_cli.media_services_service_group.add_command(media_workflow_job_group)
media_services_service_cli.media_services_service_group.add_command(stream_cdn_config_group)
media_services_service_cli.media_services_service_group.add_command(stream_distribution_channel_group)
media_services_service_cli.media_services_service_group.add_command(media_asset_distribution_channel_attachment_group)
media_services_service_cli.media_services_service_group.add_command(media_workflow_configuration_group)
media_services_service_cli.media_services_service_group.add_command(media_workflow_task_declaration_collection_group)
media_services_service_cli.media_services_service_group.add_command(media_asset_distribution_channel_attachment_collection_group)
media_services_service_cli.media_services_service_group.add_command(media_workflow_group)
media_services_service_cli.media_services_service_group.add_command(media_workflow_configuration_collection_group)


@media_asset_group.command(name=cli_util.override('media_services.change_media_asset_compartment.command_name', 'change-compartment'), help=u"""Moves a MediaAsset resource from one compartment identifier to another. \n[Command Reference](changeMediaAssetCompartment)""")
@cli_util.option('--media-asset-id', required=True, help=u"""Unique MediaAsset identifier""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_media_asset_compartment(ctx, from_json, media_asset_id, compartment_id, if_match):

    if isinstance(media_asset_id, six.string_types) and len(media_asset_id.strip()) == 0:
        raise click.UsageError('Parameter --media-asset-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.change_media_asset_compartment(
        media_asset_id=media_asset_id,
        change_media_asset_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@media_workflow_group.command(name=cli_util.override('media_services.change_media_workflow_compartment.command_name', 'change-compartment'), help=u"""Moves a MediaWorkflow resource from one compartment identifier to another. \n[Command Reference](changeMediaWorkflowCompartment)""")
@cli_util.option('--media-workflow-id', required=True, help=u"""Unique MediaWorkflow identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_media_workflow_compartment(ctx, from_json, media_workflow_id, compartment_id, if_match):

    if isinstance(media_workflow_id, six.string_types) and len(media_workflow_id.strip()) == 0:
        raise click.UsageError('Parameter --media-workflow-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.change_media_workflow_compartment(
        media_workflow_id=media_workflow_id,
        change_media_workflow_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@media_workflow_configuration_group.command(name=cli_util.override('media_services.change_media_workflow_configuration_compartment.command_name', 'change-compartment'), help=u"""Moves a MediaWorkflowConfiguration resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeMediaWorkflowConfigurationCompartment)""")
@cli_util.option('--media-workflow-configuration-id', required=True, help=u"""Unique MediaWorkflowConfiguration identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_media_workflow_configuration_compartment(ctx, from_json, media_workflow_configuration_id, compartment_id, if_match):

    if isinstance(media_workflow_configuration_id, six.string_types) and len(media_workflow_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --media-workflow-configuration-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.change_media_workflow_configuration_compartment(
        media_workflow_configuration_id=media_workflow_configuration_id,
        change_media_workflow_configuration_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@media_workflow_job_group.command(name=cli_util.override('media_services.change_media_workflow_job_compartment.command_name', 'change-compartment'), help=u"""Moves a MediaWorkflowJob resource from one compartment identifier to another. \n[Command Reference](changeMediaWorkflowJobCompartment)""")
@cli_util.option('--media-workflow-job-id', required=True, help=u"""Unique MediaWorkflowJob identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_media_workflow_job_compartment(ctx, from_json, media_workflow_job_id, compartment_id, if_match):

    if isinstance(media_workflow_job_id, six.string_types) and len(media_workflow_job_id.strip()) == 0:
        raise click.UsageError('Parameter --media-workflow-job-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.change_media_workflow_job_compartment(
        media_workflow_job_id=media_workflow_job_id,
        change_media_workflow_job_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@stream_distribution_channel_group.command(name=cli_util.override('media_services.change_stream_distribution_channel_compartment.command_name', 'change-compartment'), help=u"""Moves a Stream Distribution Channel resource from one compartment identifier to another. \n[Command Reference](changeStreamDistributionChannelCompartment)""")
@cli_util.option('--stream-distribution-channel-id', required=True, help=u"""Unique Stream Distribution Channel path identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_stream_distribution_channel_compartment(ctx, from_json, stream_distribution_channel_id, compartment_id, if_match):

    if isinstance(stream_distribution_channel_id, six.string_types) and len(stream_distribution_channel_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-distribution-channel-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.change_stream_distribution_channel_compartment(
        stream_distribution_channel_id=stream_distribution_channel_id,
        change_stream_distribution_channel_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@media_asset_group.command(name=cli_util.override('media_services.create_media_asset.command_name', 'create'), help=u"""Creates a new MediaAsset. \n[Command Reference](createMediaAsset)""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["AUDIO", "VIDEO", "PLAYLIST", "IMAGE", "CAPTION_FILE", "UNKNOWN"]), help=u"""The type of the media asset.""")
@cli_util.option('--source-media-workflow-id', help=u"""The ID of the MediaWorkflow used to produce this asset.""")
@cli_util.option('--media-workflow-job-id', help=u"""The ID of the MediaWorkflowJob used to produce this asset.""")
@cli_util.option('--source-media-workflow-version', type=click.INT, help=u"""The version of the MediaWorkflow used to produce this asset.""")
@cli_util.option('--display-name', help=u"""Display name for the Media Asset. Does not have to be unique. Avoid entering confidential information.""")
@cli_util.option('--parent-media-asset-id', help=u"""The ID of the parent asset from which this asset is derived.""")
@cli_util.option('--master-media-asset-id', help=u"""The ID of the senior most asset from which this asset is derived.""")
@cli_util.option('--bucket-name', help=u"""The name of the object storage bucket where this asset is located.""")
@cli_util.option('--namespace-name', help=u"""The object storage namespace where this asset is located.""")
@cli_util.option('--object-name', help=u"""The object storage object name that identifies this asset.""")
@cli_util.option('--object-etag', help=u"""eTag of the underlying object storage object.""")
@cli_util.option('--metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Metadata.

This option is a JSON list with items of type Metadata.  For documentation on Metadata please see our API reference: https://docs.cloud.oracle.com/api/#/en/mediaservices/20211101/datatypes/Metadata.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--segment-range-start-index', type=click.INT, help=u"""The start index for video segment files.""")
@cli_util.option('--segment-range-end-index', type=click.INT, help=u"""The end index for video segment files.""")
@cli_util.option('--media-asset-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""list of tags for the MediaAsset.

This option is a JSON list with items of type MediaAssetTag.  For documentation on MediaAssetTag please see our API reference: https://docs.cloud.oracle.com/api/#/en/mediaservices/20211101/datatypes/MediaAssetTag.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'metadata': {'module': 'media_services', 'class': 'list[Metadata]'}, 'media-asset-tags': {'module': 'media_services', 'class': 'list[MediaAssetTag]'}, 'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'metadata': {'module': 'media_services', 'class': 'list[Metadata]'}, 'media-asset-tags': {'module': 'media_services', 'class': 'list[MediaAssetTag]'}, 'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'media_services', 'class': 'MediaAsset'})
@cli_util.wrap_exceptions
def create_media_asset(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, type, source_media_workflow_id, media_workflow_job_id, source_media_workflow_version, display_name, parent_media_asset_id, master_media_asset_id, bucket_name, namespace_name, object_name, object_etag, metadata, segment_range_start_index, segment_range_end_index, media_asset_tags, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['type'] = type

    if source_media_workflow_id is not None:
        _details['sourceMediaWorkflowId'] = source_media_workflow_id

    if media_workflow_job_id is not None:
        _details['mediaWorkflowJobId'] = media_workflow_job_id

    if source_media_workflow_version is not None:
        _details['sourceMediaWorkflowVersion'] = source_media_workflow_version

    if display_name is not None:
        _details['displayName'] = display_name

    if parent_media_asset_id is not None:
        _details['parentMediaAssetId'] = parent_media_asset_id

    if master_media_asset_id is not None:
        _details['masterMediaAssetId'] = master_media_asset_id

    if bucket_name is not None:
        _details['bucketName'] = bucket_name

    if namespace_name is not None:
        _details['namespaceName'] = namespace_name

    if object_name is not None:
        _details['objectName'] = object_name

    if object_etag is not None:
        _details['objectEtag'] = object_etag

    if metadata is not None:
        _details['metadata'] = cli_util.parse_json_parameter("metadata", metadata)

    if segment_range_start_index is not None:
        _details['segmentRangeStartIndex'] = segment_range_start_index

    if segment_range_end_index is not None:
        _details['segmentRangeEndIndex'] = segment_range_end_index

    if media_asset_tags is not None:
        _details['mediaAssetTags'] = cli_util.parse_json_parameter("media_asset_tags", media_asset_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.create_media_asset(
        create_media_asset_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_media_asset') and callable(getattr(client, 'get_media_asset')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_media_asset(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@media_workflow_group.command(name=cli_util.override('media_services.create_media_workflow.command_name', 'create'), help=u"""Creates a new MediaWorkflow. \n[Command Reference](createMediaWorkflow)""")
@cli_util.option('--display-name', required=True, help=u"""Name for the MediaWorkflow. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier.""")
@cli_util.option('--tasks', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The processing to be done in this workflow. Each key of the MediaWorkflowTasks in this array must be unique within the array. The order of tasks given here will be preserved.

This option is a JSON list with items of type MediaWorkflowTask.  For documentation on MediaWorkflowTask please see our API reference: https://docs.cloud.oracle.com/api/#/en/mediaservices/20211101/datatypes/MediaWorkflowTask.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--media-workflow-configuration-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configurations to be applied to all the jobs for this workflow. Parameters in these configurations are overridden by parameters in the MediaWorkflowConfigurations of the MediaWorkflowJob and the parameters of the MediaWorkflowJob.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""JSON object representing named parameters and their default values that can be referenced throughout this workflow. The values declared here can be overridden by the MediaWorkflowConfigurations or parameters supplied when creating MediaWorkflowJobs from this MediaWorkflow.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'tasks': {'module': 'media_services', 'class': 'list[MediaWorkflowTask]'}, 'media-workflow-configuration-ids': {'module': 'media_services', 'class': 'list[string]'}, 'parameters': {'module': 'media_services', 'class': 'dict(str, object)'}, 'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'tasks': {'module': 'media_services', 'class': 'list[MediaWorkflowTask]'}, 'media-workflow-configuration-ids': {'module': 'media_services', 'class': 'list[string]'}, 'parameters': {'module': 'media_services', 'class': 'dict(str, object)'}, 'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'media_services', 'class': 'MediaWorkflow'})
@cli_util.wrap_exceptions
def create_media_workflow(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, tasks, media_workflow_configuration_ids, parameters, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id

    if tasks is not None:
        _details['tasks'] = cli_util.parse_json_parameter("tasks", tasks)

    if media_workflow_configuration_ids is not None:
        _details['mediaWorkflowConfigurationIds'] = cli_util.parse_json_parameter("media_workflow_configuration_ids", media_workflow_configuration_ids)

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.create_media_workflow(
        create_media_workflow_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_media_workflow') and callable(getattr(client, 'get_media_workflow')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_media_workflow(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@media_workflow_configuration_group.command(name=cli_util.override('media_services.create_media_workflow_configuration.command_name', 'create'), help=u"""Creates a new MediaWorkflowConfiguration. \n[Command Reference](createMediaWorkflowConfiguration)""")
@cli_util.option('--display-name', required=True, help=u"""MediaWorkflowConfiguration identifier. Avoid entering confidential information.""")
@cli_util.option('--parameters', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Reuseable parameter values encoded as a JSON; the top and second level JSON elements are objects. Each key of the top level object refers to a task key that is unqiue to the workflow, each of the second level objects' keys refer to the name of a parameter that is unique to the task. taskKey -> parameterName -> parameterValue""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'parameters': {'module': 'media_services', 'class': 'dict(str, object)'}, 'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parameters': {'module': 'media_services', 'class': 'dict(str, object)'}, 'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'media_services', 'class': 'MediaWorkflowConfiguration'})
@cli_util.wrap_exceptions
def create_media_workflow_configuration(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, parameters, compartment_id, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)
    _details['compartmentId'] = compartment_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.create_media_workflow_configuration(
        create_media_workflow_configuration_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_media_workflow_configuration') and callable(getattr(client, 'get_media_workflow_configuration')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_media_workflow_configuration(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@media_workflow_job_group.command(name=cli_util.override('media_services.create_media_workflow_job.command_name', 'create'), help=u"""Run the MediaWorkflow according to the given mediaWorkflow definition and configuration. \n[Command Reference](createMediaWorkflowJob)""")
@cli_util.option('--workflow-identifier-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["ID", "NAME"]), help=u"""Discriminate identification of a workflow by name versus a workflow by ID.""")
@cli_util.option('--compartment-id', required=True, help=u"""ID of the compartment in which the job should be created.""")
@cli_util.option('--media-workflow-configuration-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configurations to be applied to this run of the workflow.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Name of the Media Workflow Job. Does not have to be unique. Avoid entering confidential information.""")
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Parameters that override parameters specified in MediaWorkflowTaskDeclarations, the MediaWorkflow, the MediaWorkflow's MediaWorkflowConfigurations and the MediaWorkflowConfigurations of this MediaWorkflowJob. The parameters are given as JSON. The top level and 2nd level elements must be JSON objects (vs arrays, scalars, etc). The top level keys refer to a task's key and the 2nd level keys refer to a parameter's name.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'media-workflow-configuration-ids': {'module': 'media_services', 'class': 'list[string]'}, 'parameters': {'module': 'media_services', 'class': 'dict(str, object)'}, 'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'media-workflow-configuration-ids': {'module': 'media_services', 'class': 'list[string]'}, 'parameters': {'module': 'media_services', 'class': 'dict(str, object)'}, 'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'media_services', 'class': 'MediaWorkflowJob'})
@cli_util.wrap_exceptions
def create_media_workflow_job(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, workflow_identifier_type, compartment_id, media_workflow_configuration_ids, display_name, parameters, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['workflowIdentifierType'] = workflow_identifier_type
    _details['compartmentId'] = compartment_id

    if media_workflow_configuration_ids is not None:
        _details['mediaWorkflowConfigurationIds'] = cli_util.parse_json_parameter("media_workflow_configuration_ids", media_workflow_configuration_ids)

    if display_name is not None:
        _details['displayName'] = display_name

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.create_media_workflow_job(
        create_media_workflow_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_media_workflow_job') and callable(getattr(client, 'get_media_workflow_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_media_workflow_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@media_workflow_job_group.command(name=cli_util.override('media_services.create_media_workflow_job_create_media_workflow_job_by_name_details.command_name', 'create-media-workflow-job-create-media-workflow-job-by-name-details'), help=u"""Run the MediaWorkflow according to the given mediaWorkflow definition and configuration. \n[Command Reference](createMediaWorkflowJob)""")
@cli_util.option('--compartment-id', required=True, help=u"""ID of the compartment in which the job should be created.""")
@cli_util.option('--media-workflow-configuration-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configurations to be applied to this run of the workflow.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Name of the Media Workflow Job. Does not have to be unique. Avoid entering confidential information.""")
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Parameters that override parameters specified in MediaWorkflowTaskDeclarations, the MediaWorkflow, the MediaWorkflow's MediaWorkflowConfigurations and the MediaWorkflowConfigurations of this MediaWorkflowJob. The parameters are given as JSON. The top level and 2nd level elements must be JSON objects (vs arrays, scalars, etc). The top level keys refer to a task's key and the 2nd level keys refer to a parameter's name.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--media-workflow-name', help=u"""Name of the system MediaWorkflow that should be run.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'media-workflow-configuration-ids': {'module': 'media_services', 'class': 'list[string]'}, 'parameters': {'module': 'media_services', 'class': 'dict(str, object)'}, 'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'media-workflow-configuration-ids': {'module': 'media_services', 'class': 'list[string]'}, 'parameters': {'module': 'media_services', 'class': 'dict(str, object)'}, 'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'media_services', 'class': 'MediaWorkflowJob'})
@cli_util.wrap_exceptions
def create_media_workflow_job_create_media_workflow_job_by_name_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, media_workflow_configuration_ids, display_name, parameters, freeform_tags, defined_tags, media_workflow_name):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    if media_workflow_configuration_ids is not None:
        _details['mediaWorkflowConfigurationIds'] = cli_util.parse_json_parameter("media_workflow_configuration_ids", media_workflow_configuration_ids)

    if display_name is not None:
        _details['displayName'] = display_name

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if media_workflow_name is not None:
        _details['mediaWorkflowName'] = media_workflow_name

    _details['workflowIdentifierType'] = 'NAME'

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.create_media_workflow_job(
        create_media_workflow_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_media_workflow_job') and callable(getattr(client, 'get_media_workflow_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_media_workflow_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@media_workflow_job_group.command(name=cli_util.override('media_services.create_media_workflow_job_create_media_workflow_job_by_id_details.command_name', 'create-media-workflow-job-create-media-workflow-job-by-id-details'), help=u"""Run the MediaWorkflow according to the given mediaWorkflow definition and configuration. \n[Command Reference](createMediaWorkflowJob)""")
@cli_util.option('--compartment-id', required=True, help=u"""ID of the compartment in which the job should be created.""")
@cli_util.option('--media-workflow-configuration-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configurations to be applied to this run of the workflow.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Name of the Media Workflow Job. Does not have to be unique. Avoid entering confidential information.""")
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Parameters that override parameters specified in MediaWorkflowTaskDeclarations, the MediaWorkflow, the MediaWorkflow's MediaWorkflowConfigurations and the MediaWorkflowConfigurations of this MediaWorkflowJob. The parameters are given as JSON. The top level and 2nd level elements must be JSON objects (vs arrays, scalars, etc). The top level keys refer to a task's key and the 2nd level keys refer to a parameter's name.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--media-workflow-id', help=u"""OCID of the MediaWorkflow that should be run.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'media-workflow-configuration-ids': {'module': 'media_services', 'class': 'list[string]'}, 'parameters': {'module': 'media_services', 'class': 'dict(str, object)'}, 'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'media-workflow-configuration-ids': {'module': 'media_services', 'class': 'list[string]'}, 'parameters': {'module': 'media_services', 'class': 'dict(str, object)'}, 'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'media_services', 'class': 'MediaWorkflowJob'})
@cli_util.wrap_exceptions
def create_media_workflow_job_create_media_workflow_job_by_id_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, media_workflow_configuration_ids, display_name, parameters, freeform_tags, defined_tags, media_workflow_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    if media_workflow_configuration_ids is not None:
        _details['mediaWorkflowConfigurationIds'] = cli_util.parse_json_parameter("media_workflow_configuration_ids", media_workflow_configuration_ids)

    if display_name is not None:
        _details['displayName'] = display_name

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if media_workflow_id is not None:
        _details['mediaWorkflowId'] = media_workflow_id

    _details['workflowIdentifierType'] = 'ID'

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.create_media_workflow_job(
        create_media_workflow_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_media_workflow_job') and callable(getattr(client, 'get_media_workflow_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_media_workflow_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@stream_cdn_config_group.command(name=cli_util.override('media_services.create_stream_cdn_config.command_name', 'create'), help=u"""Creates a new CDN Configuration. \n[Command Reference](createStreamCdnConfig)""")
@cli_util.option('--display-name', required=True, help=u"""CDN Config display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--distribution-channel-id', required=True, help=u"""Distribution Channel Identifier.""")
@cli_util.option('--config', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Whether publishing to CDN is enabled.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'config': {'module': 'media_services', 'class': 'StreamCdnConfigSection'}, 'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'config': {'module': 'media_services', 'class': 'StreamCdnConfigSection'}, 'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'media_services', 'class': 'StreamCdnConfig'})
@cli_util.wrap_exceptions
def create_stream_cdn_config(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, distribution_channel_id, config, is_enabled, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['distributionChannelId'] = distribution_channel_id
    _details['config'] = cli_util.parse_json_parameter("config", config)

    if is_enabled is not None:
        _details['isEnabled'] = is_enabled

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.create_stream_cdn_config(
        create_stream_cdn_config_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stream_cdn_config') and callable(getattr(client, 'get_stream_cdn_config')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_stream_cdn_config(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@stream_cdn_config_group.command(name=cli_util.override('media_services.create_stream_cdn_config_akamai_manual_stream_cdn_config.command_name', 'create-stream-cdn-config-akamai-manual-stream-cdn-config'), help=u"""Creates a new CDN Configuration. \n[Command Reference](createStreamCdnConfig)""")
@cli_util.option('--display-name', required=True, help=u"""CDN Config display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--distribution-channel-id', required=True, help=u"""Distribution Channel Identifier.""")
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Whether publishing to CDN is enabled.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--config-origin-auth-sign-type', type=custom_types.CliCaseInsensitiveChoice(["ForwardURL"]), help=u"""The type of data used to compute the signature.""")
@cli_util.option('--config-origin-auth-sign-encryption', type=custom_types.CliCaseInsensitiveChoice(["SHA256-HMAC"]), help=u"""The type of encryption used to compute the signature.""")
@cli_util.option('--config-origin-auth-secret-key-a', help=u"""The shared secret key A, two for errorless key rotation.""")
@cli_util.option('--config-origin-auth-secret-key-nonce-a', help=u"""Nonce identifier for originAuthSecretKeyA (used to determine key used to sign).""")
@cli_util.option('--config-origin-auth-secret-key-b', help=u"""The shared secret key B, two for errorless key rotation.""")
@cli_util.option('--config-origin-auth-secret-key-nonce-b', help=u"""Nonce identifier for originAuthSecretKeyB (used to determine key used to sign).""")
@cli_util.option('--config-edge-hostname', help=u"""The hostname of the CDN edge server to use when building CDN URLs.""")
@cli_util.option('--config-edge-path-prefix', help=u"""The path to prepend when building CDN URLs.""")
@cli_util.option('--config-is-edge-token-auth', type=click.BOOL, help=u"""Whether token authentication should be used at the CDN edge.""")
@cli_util.option('--config-edge-token-key', help=u"""The encryption key to use for edge token authentication.""")
@cli_util.option('--config-edge-token-salt', help=u"""Salt to use when encrypting authentication token.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'media_services', 'class': 'StreamCdnConfig'})
@cli_util.wrap_exceptions
def create_stream_cdn_config_akamai_manual_stream_cdn_config(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, distribution_channel_id, is_enabled, freeform_tags, defined_tags, config_origin_auth_sign_type, config_origin_auth_sign_encryption, config_origin_auth_secret_key_a, config_origin_auth_secret_key_nonce_a, config_origin_auth_secret_key_b, config_origin_auth_secret_key_nonce_b, config_edge_hostname, config_edge_path_prefix, config_is_edge_token_auth, config_edge_token_key, config_edge_token_salt):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['config'] = {}
    _details['displayName'] = display_name
    _details['distributionChannelId'] = distribution_channel_id

    if is_enabled is not None:
        _details['isEnabled'] = is_enabled

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if config_origin_auth_sign_type is not None:
        _details['config']['originAuthSignType'] = config_origin_auth_sign_type

    if config_origin_auth_sign_encryption is not None:
        _details['config']['originAuthSignEncryption'] = config_origin_auth_sign_encryption

    if config_origin_auth_secret_key_a is not None:
        _details['config']['originAuthSecretKeyA'] = config_origin_auth_secret_key_a

    if config_origin_auth_secret_key_nonce_a is not None:
        _details['config']['originAuthSecretKeyNonceA'] = config_origin_auth_secret_key_nonce_a

    if config_origin_auth_secret_key_b is not None:
        _details['config']['originAuthSecretKeyB'] = config_origin_auth_secret_key_b

    if config_origin_auth_secret_key_nonce_b is not None:
        _details['config']['originAuthSecretKeyNonceB'] = config_origin_auth_secret_key_nonce_b

    if config_edge_hostname is not None:
        _details['config']['edgeHostname'] = config_edge_hostname

    if config_edge_path_prefix is not None:
        _details['config']['edgePathPrefix'] = config_edge_path_prefix

    if config_is_edge_token_auth is not None:
        _details['config']['isEdgeTokenAuth'] = config_is_edge_token_auth

    if config_edge_token_key is not None:
        _details['config']['edgeTokenKey'] = config_edge_token_key

    if config_edge_token_salt is not None:
        _details['config']['edgeTokenSalt'] = config_edge_token_salt

    _details['config']['type'] = 'AKAMAI_MANUAL'

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.create_stream_cdn_config(
        create_stream_cdn_config_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stream_cdn_config') and callable(getattr(client, 'get_stream_cdn_config')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_stream_cdn_config(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@stream_cdn_config_group.command(name=cli_util.override('media_services.create_stream_cdn_config_edge_stream_cdn_config.command_name', 'create-stream-cdn-config-edge-stream-cdn-config'), help=u"""Creates a new CDN Configuration. \n[Command Reference](createStreamCdnConfig)""")
@cli_util.option('--display-name', required=True, help=u"""CDN Config display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--distribution-channel-id', required=True, help=u"""Distribution Channel Identifier.""")
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Whether publishing to CDN is enabled.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'media_services', 'class': 'StreamCdnConfig'})
@cli_util.wrap_exceptions
def create_stream_cdn_config_edge_stream_cdn_config(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, distribution_channel_id, is_enabled, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['config'] = {}
    _details['displayName'] = display_name
    _details['distributionChannelId'] = distribution_channel_id

    if is_enabled is not None:
        _details['isEnabled'] = is_enabled

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['config']['type'] = 'EDGE'

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.create_stream_cdn_config(
        create_stream_cdn_config_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stream_cdn_config') and callable(getattr(client, 'get_stream_cdn_config')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_stream_cdn_config(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@stream_distribution_channel_group.command(name=cli_util.override('media_services.create_stream_distribution_channel.command_name', 'create'), help=u"""Creates a new Stream Distribution Channel. \n[Command Reference](createStreamDistributionChannel)""")
@cli_util.option('--display-name', required=True, help=u"""Stream Distribution Channel display name. Avoid entering confidential information.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'media_services', 'class': 'StreamDistributionChannel'})
@cli_util.wrap_exceptions
def create_stream_distribution_channel(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.create_stream_distribution_channel(
        create_stream_distribution_channel_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stream_distribution_channel') and callable(getattr(client, 'get_stream_distribution_channel')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_stream_distribution_channel(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@stream_packaging_config_group.command(name=cli_util.override('media_services.create_stream_packaging_config.command_name', 'create'), help=u"""Creates a new Packaging Configuration. \n[Command Reference](createStreamPackagingConfig)""")
@cli_util.option('--distribution-channel-id', required=True, help=u"""Unique identifier of the Distribution Channel that this stream packaging configuration belongs to.""")
@cli_util.option('--display-name', required=True, help=u"""The name of the stream Packaging Configuration. Avoid entering confidential information.""")
@cli_util.option('--stream-packaging-format', required=True, type=custom_types.CliCaseInsensitiveChoice(["HLS", "DASH"]), help=u"""The output format for the package.""")
@cli_util.option('--segment-time-in-seconds', required=True, type=click.INT, help=u"""The duration in seconds for each fragment.""")
@cli_util.option('--encryption', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'encryption': {'module': 'media_services', 'class': 'StreamPackagingConfigEncryption'}, 'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'encryption': {'module': 'media_services', 'class': 'StreamPackagingConfigEncryption'}, 'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'media_services', 'class': 'StreamPackagingConfig'})
@cli_util.wrap_exceptions
def create_stream_packaging_config(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, distribution_channel_id, display_name, stream_packaging_format, segment_time_in_seconds, encryption, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['distributionChannelId'] = distribution_channel_id
    _details['displayName'] = display_name
    _details['streamPackagingFormat'] = stream_packaging_format
    _details['segmentTimeInSeconds'] = segment_time_in_seconds

    if encryption is not None:
        _details['encryption'] = cli_util.parse_json_parameter("encryption", encryption)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.create_stream_packaging_config(
        create_stream_packaging_config_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stream_packaging_config') and callable(getattr(client, 'get_stream_packaging_config')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_stream_packaging_config(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@stream_packaging_config_group.command(name=cli_util.override('media_services.create_stream_packaging_config_stream_packaging_config_encryption_aes128.command_name', 'create-stream-packaging-config-stream-packaging-config-encryption-aes128'), help=u"""Creates a new Packaging Configuration. \n[Command Reference](createStreamPackagingConfig)""")
@cli_util.option('--distribution-channel-id', required=True, help=u"""Unique identifier of the Distribution Channel that this stream packaging configuration belongs to.""")
@cli_util.option('--display-name', required=True, help=u"""The name of the stream Packaging Configuration. Avoid entering confidential information.""")
@cli_util.option('--stream-packaging-format', required=True, type=custom_types.CliCaseInsensitiveChoice(["HLS", "DASH"]), help=u"""The output format for the package.""")
@cli_util.option('--segment-time-in-seconds', required=True, type=click.INT, help=u"""The duration in seconds for each fragment.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--encryption-kms-key-id', help=u"""The identifier of the customer managed Vault KMS symmetric encryption key (null if Oracle managed).""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'media_services', 'class': 'StreamPackagingConfig'})
@cli_util.wrap_exceptions
def create_stream_packaging_config_stream_packaging_config_encryption_aes128(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, distribution_channel_id, display_name, stream_packaging_format, segment_time_in_seconds, freeform_tags, defined_tags, encryption_kms_key_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['encryption'] = {}
    _details['distributionChannelId'] = distribution_channel_id
    _details['displayName'] = display_name
    _details['streamPackagingFormat'] = stream_packaging_format
    _details['segmentTimeInSeconds'] = segment_time_in_seconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if encryption_kms_key_id is not None:
        _details['encryption']['kmsKeyId'] = encryption_kms_key_id

    _details['encryption']['algorithm'] = 'AES128'

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.create_stream_packaging_config(
        create_stream_packaging_config_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stream_packaging_config') and callable(getattr(client, 'get_stream_packaging_config')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_stream_packaging_config(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@stream_packaging_config_group.command(name=cli_util.override('media_services.create_stream_packaging_config_stream_packaging_config_encryption_none.command_name', 'create-stream-packaging-config-stream-packaging-config-encryption-none'), help=u"""Creates a new Packaging Configuration. \n[Command Reference](createStreamPackagingConfig)""")
@cli_util.option('--distribution-channel-id', required=True, help=u"""Unique identifier of the Distribution Channel that this stream packaging configuration belongs to.""")
@cli_util.option('--display-name', required=True, help=u"""The name of the stream Packaging Configuration. Avoid entering confidential information.""")
@cli_util.option('--stream-packaging-format', required=True, type=custom_types.CliCaseInsensitiveChoice(["HLS", "DASH"]), help=u"""The output format for the package.""")
@cli_util.option('--segment-time-in-seconds', required=True, type=click.INT, help=u"""The duration in seconds for each fragment.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'media_services', 'class': 'StreamPackagingConfig'})
@cli_util.wrap_exceptions
def create_stream_packaging_config_stream_packaging_config_encryption_none(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, distribution_channel_id, display_name, stream_packaging_format, segment_time_in_seconds, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['encryption'] = {}
    _details['distributionChannelId'] = distribution_channel_id
    _details['displayName'] = display_name
    _details['streamPackagingFormat'] = stream_packaging_format
    _details['segmentTimeInSeconds'] = segment_time_in_seconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['encryption']['algorithm'] = 'NONE'

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.create_stream_packaging_config(
        create_stream_packaging_config_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stream_packaging_config') and callable(getattr(client, 'get_stream_packaging_config')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_stream_packaging_config(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@media_asset_group.command(name=cli_util.override('media_services.delete_media_asset.command_name', 'delete'), help=u"""Deletes a MediaAsset resource by identifier. If DeleteChildren is passed in as the mode, all the assets with the parentMediaAssetId matching the ID will be deleted. If DeleteDerivatives is set as the mode, all the assets with the masterMediaAssetId matching the ID will be deleted. \n[Command Reference](deleteMediaAsset)""")
@cli_util.option('--media-asset-id', required=True, help=u"""Unique MediaAsset identifier""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--delete-mode', type=custom_types.CliCaseInsensitiveChoice(["DELETE_CHILDREN", "DELETE_DERIVATIONS"]), help=u"""DeleteMode decides whether to delete all the immediate children or all assets with the asset's ID as their masterMediaAssetId.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_media_asset(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, media_asset_id, if_match, delete_mode):

    if isinstance(media_asset_id, six.string_types) and len(media_asset_id.strip()) == 0:
        raise click.UsageError('Parameter --media-asset-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if delete_mode is not None:
        kwargs['delete_mode'] = delete_mode
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.delete_media_asset(
        media_asset_id=media_asset_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_media_asset') and callable(getattr(client, 'get_media_asset')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_media_asset(media_asset_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@media_asset_distribution_channel_attachment_group.command(name=cli_util.override('media_services.delete_media_asset_distribution_channel_attachment.command_name', 'delete'), help=u"""Deletes a MediaAsset from the DistributionChannel by identifiers. \n[Command Reference](deleteMediaAssetDistributionChannelAttachment)""")
@cli_util.option('--media-asset-id', required=True, help=u"""Unique MediaAsset identifier""")
@cli_util.option('--distribution-channel-id', required=True, help=u"""Unique DistributionChannel identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--version-parameterconflict', type=click.INT, help=u"""Version of the attachment.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_media_asset_distribution_channel_attachment(ctx, from_json, media_asset_id, distribution_channel_id, if_match, version_parameterconflict):

    if isinstance(media_asset_id, six.string_types) and len(media_asset_id.strip()) == 0:
        raise click.UsageError('Parameter --media-asset-id cannot be whitespace or empty string')

    if isinstance(distribution_channel_id, six.string_types) and len(distribution_channel_id.strip()) == 0:
        raise click.UsageError('Parameter --distribution-channel-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if version_parameterconflict is not None:
        kwargs['version'] = version_parameterconflict
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.delete_media_asset_distribution_channel_attachment(
        media_asset_id=media_asset_id,
        distribution_channel_id=distribution_channel_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@media_workflow_group.command(name=cli_util.override('media_services.delete_media_workflow.command_name', 'delete'), help=u"""The MediaWorkflow lifecycleState will change to DELETED. \n[Command Reference](deleteMediaWorkflow)""")
@cli_util.option('--media-workflow-id', required=True, help=u"""Unique MediaWorkflow identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_media_workflow(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, media_workflow_id, if_match):

    if isinstance(media_workflow_id, six.string_types) and len(media_workflow_id.strip()) == 0:
        raise click.UsageError('Parameter --media-workflow-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.delete_media_workflow(
        media_workflow_id=media_workflow_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_media_workflow') and callable(getattr(client, 'get_media_workflow')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_media_workflow(media_workflow_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@media_workflow_configuration_group.command(name=cli_util.override('media_services.delete_media_workflow_configuration.command_name', 'delete'), help=u"""Deletes a MediaWorkflowConfiguration resource by identifier. \n[Command Reference](deleteMediaWorkflowConfiguration)""")
@cli_util.option('--media-workflow-configuration-id', required=True, help=u"""Unique MediaWorkflowConfiguration identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_media_workflow_configuration(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, media_workflow_configuration_id, if_match):

    if isinstance(media_workflow_configuration_id, six.string_types) and len(media_workflow_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --media-workflow-configuration-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.delete_media_workflow_configuration(
        media_workflow_configuration_id=media_workflow_configuration_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_media_workflow_configuration') and callable(getattr(client, 'get_media_workflow_configuration')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_media_workflow_configuration(media_workflow_configuration_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@media_workflow_job_group.command(name=cli_util.override('media_services.delete_media_workflow_job.command_name', 'delete'), help=u"""This is an asynchronous operation. The MediaWorkflowJob lifecycleState will change to CANCELING temporarily until the job is completely CANCELED. \n[Command Reference](deleteMediaWorkflowJob)""")
@cli_util.option('--media-workflow-job-id', required=True, help=u"""Unique MediaWorkflowJob identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_media_workflow_job(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, media_workflow_job_id, if_match):

    if isinstance(media_workflow_job_id, six.string_types) and len(media_workflow_job_id.strip()) == 0:
        raise click.UsageError('Parameter --media-workflow-job-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.delete_media_workflow_job(
        media_workflow_job_id=media_workflow_job_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_media_workflow_job') and callable(getattr(client, 'get_media_workflow_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_media_workflow_job(media_workflow_job_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@stream_cdn_config_group.command(name=cli_util.override('media_services.delete_stream_cdn_config.command_name', 'delete'), help=u"""The StreamCdnConfig lifecycleState will change to DELETED. \n[Command Reference](deleteStreamCdnConfig)""")
@cli_util.option('--stream-cdn-config-id', required=True, help=u"""Unique StreamCdnConfig identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_stream_cdn_config(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, stream_cdn_config_id, if_match):

    if isinstance(stream_cdn_config_id, six.string_types) and len(stream_cdn_config_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-cdn-config-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.delete_stream_cdn_config(
        stream_cdn_config_id=stream_cdn_config_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stream_cdn_config') and callable(getattr(client, 'get_stream_cdn_config')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_stream_cdn_config(stream_cdn_config_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@stream_distribution_channel_group.command(name=cli_util.override('media_services.delete_stream_distribution_channel.command_name', 'delete'), help=u"""The Stream Distribution Channel lifecycleState will change to DELETED. \n[Command Reference](deleteStreamDistributionChannel)""")
@cli_util.option('--stream-distribution-channel-id', required=True, help=u"""Unique Stream Distribution Channel path identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_stream_distribution_channel(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, stream_distribution_channel_id, if_match):

    if isinstance(stream_distribution_channel_id, six.string_types) and len(stream_distribution_channel_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-distribution-channel-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.delete_stream_distribution_channel(
        stream_distribution_channel_id=stream_distribution_channel_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stream_distribution_channel') and callable(getattr(client, 'get_stream_distribution_channel')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_stream_distribution_channel(stream_distribution_channel_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@stream_packaging_config_group.command(name=cli_util.override('media_services.delete_stream_packaging_config.command_name', 'delete'), help=u"""The Stream Packaging Configuration lifecycleState will change to DELETED. \n[Command Reference](deleteStreamPackagingConfig)""")
@cli_util.option('--stream-packaging-config-id', required=True, help=u"""Unique Stream Packaging Configuration path identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_stream_packaging_config(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, stream_packaging_config_id, if_match):

    if isinstance(stream_packaging_config_id, six.string_types) and len(stream_packaging_config_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-packaging-config-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.delete_stream_packaging_config(
        stream_packaging_config_id=stream_packaging_config_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stream_packaging_config') and callable(getattr(client, 'get_stream_packaging_config')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_stream_packaging_config(stream_packaging_config_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@media_asset_group.command(name=cli_util.override('media_services.get_media_asset.command_name', 'get'), help=u"""Gets a MediaAsset by identifier. \n[Command Reference](getMediaAsset)""")
@cli_util.option('--media-asset-id', required=True, help=u"""Unique MediaAsset identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'media_services', 'class': 'MediaAsset'})
@cli_util.wrap_exceptions
def get_media_asset(ctx, from_json, media_asset_id):

    if isinstance(media_asset_id, six.string_types) and len(media_asset_id.strip()) == 0:
        raise click.UsageError('Parameter --media-asset-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.get_media_asset(
        media_asset_id=media_asset_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@media_asset_distribution_channel_attachment_group.command(name=cli_util.override('media_services.get_media_asset_distribution_channel_attachment.command_name', 'get'), help=u"""Gets a MediaAssetDistributionChannelAttachment for a MediaAsset by identifiers. \n[Command Reference](getMediaAssetDistributionChannelAttachment)""")
@cli_util.option('--media-asset-id', required=True, help=u"""Unique MediaAsset identifier""")
@cli_util.option('--distribution-channel-id', required=True, help=u"""Unique DistributionChannel identifier.""")
@cli_util.option('--version-parameterconflict', type=click.INT, help=u"""Version of the attachment.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'media_services', 'class': 'MediaAssetDistributionChannelAttachment'})
@cli_util.wrap_exceptions
def get_media_asset_distribution_channel_attachment(ctx, from_json, media_asset_id, distribution_channel_id, version_parameterconflict):

    if isinstance(media_asset_id, six.string_types) and len(media_asset_id.strip()) == 0:
        raise click.UsageError('Parameter --media-asset-id cannot be whitespace or empty string')

    if isinstance(distribution_channel_id, six.string_types) and len(distribution_channel_id.strip()) == 0:
        raise click.UsageError('Parameter --distribution-channel-id cannot be whitespace or empty string')

    kwargs = {}
    if version_parameterconflict is not None:
        kwargs['version'] = version_parameterconflict
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.get_media_asset_distribution_channel_attachment(
        media_asset_id=media_asset_id,
        distribution_channel_id=distribution_channel_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@media_workflow_group.command(name=cli_util.override('media_services.get_media_workflow.command_name', 'get'), help=u"""Gets a MediaWorkflow by identifier. \n[Command Reference](getMediaWorkflow)""")
@cli_util.option('--media-workflow-id', required=True, help=u"""Unique MediaWorkflow identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'media_services', 'class': 'MediaWorkflow'})
@cli_util.wrap_exceptions
def get_media_workflow(ctx, from_json, media_workflow_id):

    if isinstance(media_workflow_id, six.string_types) and len(media_workflow_id.strip()) == 0:
        raise click.UsageError('Parameter --media-workflow-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.get_media_workflow(
        media_workflow_id=media_workflow_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@media_workflow_configuration_group.command(name=cli_util.override('media_services.get_media_workflow_configuration.command_name', 'get'), help=u"""Gets a MediaWorkflowConfiguration by identifier \n[Command Reference](getMediaWorkflowConfiguration)""")
@cli_util.option('--media-workflow-configuration-id', required=True, help=u"""Unique MediaWorkflowConfiguration identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'media_services', 'class': 'MediaWorkflowConfiguration'})
@cli_util.wrap_exceptions
def get_media_workflow_configuration(ctx, from_json, media_workflow_configuration_id):

    if isinstance(media_workflow_configuration_id, six.string_types) and len(media_workflow_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --media-workflow-configuration-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.get_media_workflow_configuration(
        media_workflow_configuration_id=media_workflow_configuration_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@media_workflow_job_group.command(name=cli_util.override('media_services.get_media_workflow_job.command_name', 'get'), help=u"""Gets the MediaWorkflowJob. \n[Command Reference](getMediaWorkflowJob)""")
@cli_util.option('--media-workflow-job-id', required=True, help=u"""Unique MediaWorkflowJob identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'media_services', 'class': 'MediaWorkflowJob'})
@cli_util.wrap_exceptions
def get_media_workflow_job(ctx, from_json, media_workflow_job_id):

    if isinstance(media_workflow_job_id, six.string_types) and len(media_workflow_job_id.strip()) == 0:
        raise click.UsageError('Parameter --media-workflow-job-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.get_media_workflow_job(
        media_workflow_job_id=media_workflow_job_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@media_workflow_job_fact_group.command(name=cli_util.override('media_services.get_media_workflow_job_fact.command_name', 'get'), help=u"""Get the MediaWorkflowJobFact identified by the mediaWorkflowJobId and Fact ID. \n[Command Reference](getMediaWorkflowJobFact)""")
@cli_util.option('--media-workflow-job-id', required=True, help=u"""Unique MediaWorkflowJob identifier.""")
@cli_util.option('--key', required=True, type=click.INT, help=u"""Identifier of the MediaWorkflowJobFact within a MediaWorkflowJob.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'media_services', 'class': 'MediaWorkflowJobFact'})
@cli_util.wrap_exceptions
def get_media_workflow_job_fact(ctx, from_json, media_workflow_job_id, key):

    if isinstance(media_workflow_job_id, six.string_types) and len(media_workflow_job_id.strip()) == 0:
        raise click.UsageError('Parameter --media-workflow-job-id cannot be whitespace or empty string')

    if isinstance(key, six.string_types) and len(key.strip()) == 0:
        raise click.UsageError('Parameter --key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.get_media_workflow_job_fact(
        media_workflow_job_id=media_workflow_job_id,
        key=key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@stream_cdn_config_group.command(name=cli_util.override('media_services.get_stream_cdn_config.command_name', 'get'), help=u"""Gets a StreamCdnConfig by identifier. \n[Command Reference](getStreamCdnConfig)""")
@cli_util.option('--stream-cdn-config-id', required=True, help=u"""Unique StreamCdnConfig identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'media_services', 'class': 'StreamCdnConfig'})
@cli_util.wrap_exceptions
def get_stream_cdn_config(ctx, from_json, stream_cdn_config_id):

    if isinstance(stream_cdn_config_id, six.string_types) and len(stream_cdn_config_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-cdn-config-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.get_stream_cdn_config(
        stream_cdn_config_id=stream_cdn_config_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@stream_distribution_channel_group.command(name=cli_util.override('media_services.get_stream_distribution_channel.command_name', 'get'), help=u"""Gets a Stream Distribution Channel by identifier. \n[Command Reference](getStreamDistributionChannel)""")
@cli_util.option('--stream-distribution-channel-id', required=True, help=u"""Unique Stream Distribution Channel path identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'media_services', 'class': 'StreamDistributionChannel'})
@cli_util.wrap_exceptions
def get_stream_distribution_channel(ctx, from_json, stream_distribution_channel_id):

    if isinstance(stream_distribution_channel_id, six.string_types) and len(stream_distribution_channel_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-distribution-channel-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.get_stream_distribution_channel(
        stream_distribution_channel_id=stream_distribution_channel_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@stream_packaging_config_group.command(name=cli_util.override('media_services.get_stream_packaging_config.command_name', 'get'), help=u"""Gets a Stream Packaging Configuration by identifier. \n[Command Reference](getStreamPackagingConfig)""")
@cli_util.option('--stream-packaging-config-id', required=True, help=u"""Unique Stream Packaging Configuration path identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'media_services', 'class': 'StreamPackagingConfig'})
@cli_util.wrap_exceptions
def get_stream_packaging_config(ctx, from_json, stream_packaging_config_id):

    if isinstance(stream_packaging_config_id, six.string_types) and len(stream_packaging_config_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-packaging-config-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.get_stream_packaging_config(
        stream_packaging_config_id=stream_packaging_config_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@stream_distribution_channel_group.command(name=cli_util.override('media_services.ingest_stream_distribution_channel.command_name', 'ingest'), help=u"""Ingests an Asset into a Distribution Channel. \n[Command Reference](ingestStreamDistributionChannel)""")
@cli_util.option('--stream-distribution-channel-id', required=True, help=u"""Unique Stream Distribution Channel path identifier.""")
@cli_util.option('--ingest-payload-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["ASSET_METADATA_MEDIA_ASSET"]), help=u"""Ingest Payload Type""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'media_services', 'class': 'IngestStreamDistributionChannelResult'})
@cli_util.wrap_exceptions
def ingest_stream_distribution_channel(ctx, from_json, stream_distribution_channel_id, ingest_payload_type):

    if isinstance(stream_distribution_channel_id, six.string_types) and len(stream_distribution_channel_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-distribution-channel-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['ingestPayloadType'] = ingest_payload_type

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.ingest_stream_distribution_channel(
        stream_distribution_channel_id=stream_distribution_channel_id,
        ingest_stream_distribution_channel_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@stream_distribution_channel_group.command(name=cli_util.override('media_services.ingest_stream_distribution_channel_asset_metadata_entry_details.command_name', 'ingest-stream-distribution-channel-asset-metadata-entry-details'), help=u"""Ingests an Asset into a Distribution Channel. \n[Command Reference](ingestStreamDistributionChannel)""")
@cli_util.option('--stream-distribution-channel-id', required=True, help=u"""Unique Stream Distribution Channel path identifier.""")
@cli_util.option('--media-asset-id', required=True, help=u"""The Media Asset ID to ingest into the Distribution Channel.""")
@cli_util.option('--compartment-id', help=u"""The compartment ID where the Ingest Workflow Job will be run.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'media_services', 'class': 'IngestStreamDistributionChannelResult'})
@cli_util.wrap_exceptions
def ingest_stream_distribution_channel_asset_metadata_entry_details(ctx, from_json, stream_distribution_channel_id, media_asset_id, compartment_id):

    if isinstance(stream_distribution_channel_id, six.string_types) and len(stream_distribution_channel_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-distribution-channel-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['mediaAssetId'] = media_asset_id

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    _details['ingestPayloadType'] = 'ASSET_METADATA_MEDIA_ASSET'

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.ingest_stream_distribution_channel(
        stream_distribution_channel_id=stream_distribution_channel_id,
        ingest_stream_distribution_channel_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@media_asset_distribution_channel_attachment_collection_group.command(name=cli_util.override('media_services.list_media_asset_distribution_channel_attachments.command_name', 'list-media-asset-distribution-channel-attachments'), help=u"""Lists the MediaAssetDistributionChannelAttachments for a MediaAsset by identifier. \n[Command Reference](listMediaAssetDistributionChannelAttachments)""")
@cli_util.option('--media-asset-id', required=True, help=u"""Unique MediaAsset identifier""")
@cli_util.option('--display-name', help=u"""A filter to return only the resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["mediaAssetId", "distributionChannelId", "displayName", "version"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--distribution-channel-id', help=u"""Unique DistributionChannel identifier.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'media_services', 'class': 'MediaAssetDistributionChannelAttachmentCollection'})
@cli_util.wrap_exceptions
def list_media_asset_distribution_channel_attachments(ctx, from_json, all_pages, page_size, media_asset_id, display_name, limit, page, sort_order, sort_by, distribution_channel_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(media_asset_id, six.string_types) and len(media_asset_id.strip()) == 0:
        raise click.UsageError('Parameter --media-asset-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if distribution_channel_id is not None:
        kwargs['distribution_channel_id'] = distribution_channel_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_services', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_media_asset_distribution_channel_attachments,
            media_asset_id=media_asset_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_media_asset_distribution_channel_attachments,
            limit,
            page_size,
            media_asset_id=media_asset_id,
            **kwargs
        )
    else:
        result = client.list_media_asset_distribution_channel_attachments(
            media_asset_id=media_asset_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@media_asset_group.command(name=cli_util.override('media_services.list_media_assets.command_name', 'list'), help=u"""Returns a list of MediaAssetSummary. \n[Command Reference](listMediaAssets)""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only the resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only the resources with lifecycleState matching the given lifecycleState.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["compartmentId", "type", "lifecycleState", "parentMediaAssetId", "masterMediaAssetId", "displayName", "timeCreated", "timeUpdated"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--distribution-channel-id', help=u"""Unique DistributionChannel identifier.""")
@cli_util.option('--parent-media-asset-id', help=u"""Unique MediaAsset identifier of the asset from which this asset is derived.""")
@cli_util.option('--master-media-asset-id', help=u"""Unique MediaAsset identifier of the first asset upload.""")
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["AUDIO", "VIDEO", "PLAYLIST", "IMAGE", "CAPTION_FILE", "UNKNOWN"]), help=u"""Filter MediaAsset by the asset type.""")
@cli_util.option('--bucket-name', help=u"""Filter MediaAsset by the bucket where the object is stored.""")
@cli_util.option('--object-name', help=u"""Filter MediaAsset by the name of the object in object storage.""")
@cli_util.option('--media-workflow-job-id', help=u"""The ID of the MediaWorkflowJob used to produce this asset, if this parameter is supplied then the workflow ID must also be supplied.""")
@cli_util.option('--source-media-workflow-id', help=u"""The ID of the MediaWorkflow used to produce this asset.""")
@cli_util.option('--source-media-workflow-version', type=click.INT, help=u"""The version of the MediaWorkflow used to produce this asset.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'media_services', 'class': 'MediaAssetCollection'})
@cli_util.wrap_exceptions
def list_media_assets(ctx, from_json, all_pages, page_size, compartment_id, display_name, limit, page, lifecycle_state, sort_order, sort_by, distribution_channel_id, parent_media_asset_id, master_media_asset_id, type, bucket_name, object_name, media_workflow_job_id, source_media_workflow_id, source_media_workflow_version):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if distribution_channel_id is not None:
        kwargs['distribution_channel_id'] = distribution_channel_id
    if parent_media_asset_id is not None:
        kwargs['parent_media_asset_id'] = parent_media_asset_id
    if master_media_asset_id is not None:
        kwargs['master_media_asset_id'] = master_media_asset_id
    if type is not None:
        kwargs['type'] = type
    if bucket_name is not None:
        kwargs['bucket_name'] = bucket_name
    if object_name is not None:
        kwargs['object_name'] = object_name
    if media_workflow_job_id is not None:
        kwargs['media_workflow_job_id'] = media_workflow_job_id
    if source_media_workflow_id is not None:
        kwargs['source_media_workflow_id'] = source_media_workflow_id
    if source_media_workflow_version is not None:
        kwargs['source_media_workflow_version'] = source_media_workflow_version
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_services', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_media_assets,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_media_assets,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_media_assets(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@media_workflow_configuration_collection_group.command(name=cli_util.override('media_services.list_media_workflow_configurations.command_name', 'list-media-workflow-configurations'), help=u"""Returns a list of MediaWorkflowConfigurations. \n[Command Reference](listMediaWorkflowConfigurations)""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED"]), help=u"""A filter to return only the resources with lifecycleState matching the given lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return only the resources that match the entire display name given.""")
@cli_util.option('--id', help=u"""Unique MediaWorkflowConfiguration identifier.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'media_services', 'class': 'MediaWorkflowConfigurationCollection'})
@cli_util.wrap_exceptions
def list_media_workflow_configurations(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, display_name, id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if id is not None:
        kwargs['id'] = id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_services', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_media_workflow_configurations,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_media_workflow_configurations,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_media_workflow_configurations(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@media_workflow_job_fact_group.command(name=cli_util.override('media_services.list_media_workflow_job_facts.command_name', 'list'), help=u"""Internal API to get a point-in-time snapshot of a MediaWorkflowJob. \n[Command Reference](listMediaWorkflowJobFacts)""")
@cli_util.option('--media-workflow-job-id', required=True, help=u"""Unique MediaWorkflowJob identifier.""")
@cli_util.option('--key', type=click.INT, help=u"""Filter by MediaWorkflowJob ID and MediaWorkflowJobFact key.""")
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["runnableJob", "taskDeclaration", "workflow", "configuration", "parameterResolutionEvent"]), help=u"""Types of details to include.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["key"]), help=u"""Types of details to include.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'media_services', 'class': 'MediaWorkflowJobFactCollection'})
@cli_util.wrap_exceptions
def list_media_workflow_job_facts(ctx, from_json, all_pages, page_size, media_workflow_job_id, key, type, sort_by, sort_order, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(media_workflow_job_id, six.string_types) and len(media_workflow_job_id.strip()) == 0:
        raise click.UsageError('Parameter --media-workflow-job-id cannot be whitespace or empty string')

    kwargs = {}
    if key is not None:
        kwargs['key'] = key
    if type is not None:
        kwargs['type'] = type
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_services', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_media_workflow_job_facts,
            media_workflow_job_id=media_workflow_job_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_media_workflow_job_facts,
            limit,
            page_size,
            media_workflow_job_id=media_workflow_job_id,
            **kwargs
        )
    else:
        result = client.list_media_workflow_job_facts(
            media_workflow_job_id=media_workflow_job_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@media_workflow_job_group.command(name=cli_util.override('media_services.list_media_workflow_jobs.command_name', 'list'), help=u"""Lists the MediaWorkflowJobs. \n[Command Reference](listMediaWorkflowJobs)""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--id', help=u"""unique MediaWorkflowJob identifier""")
@cli_util.option('--media-workflow-id', help=u"""Unique MediaWorkflow identifier.""")
@cli_util.option('--display-name', help=u"""A filter to return only the resources that match the entire display name given.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help=u"""A filter to return only the resources with lifecycleState matching the given lifecycleState.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "workflowId", "lifecycleState"]), help=u"""The parameter sort by.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'media_services', 'class': 'MediaWorkflowJobCollection'})
@cli_util.wrap_exceptions
def list_media_workflow_jobs(ctx, from_json, all_pages, page_size, compartment_id, id, media_workflow_id, display_name, lifecycle_state, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if id is not None:
        kwargs['id'] = id
    if media_workflow_id is not None:
        kwargs['media_workflow_id'] = media_workflow_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_services', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_media_workflow_jobs,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_media_workflow_jobs,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_media_workflow_jobs(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@media_workflow_task_declaration_collection_group.command(name=cli_util.override('media_services.list_media_workflow_task_declarations.command_name', 'list-media-workflow-task-declarations'), help=u"""Returns a list of MediaWorkflowTaskDeclarations. \n[Command Reference](listMediaWorkflowTaskDeclarations)""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--name', help=u"""A filter to return only the resources with their system defined, unique name matching the given name.""")
@cli_util.option('--version-parameterconflict', type=click.INT, help=u"""A filter to select MediaWorkflowTaskDeclaration by version.""")
@cli_util.option('--is-current', type=click.BOOL, help=u"""A filter to only select the newest version for each MediaWorkflowTaskDeclaration name.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["name", "version"]), help=u"""The field to sort by. Only one sort order may be provided.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'media_services', 'class': 'MediaWorkflowTaskDeclarationCollection'})
@cli_util.wrap_exceptions
def list_media_workflow_task_declarations(ctx, from_json, all_pages, page_size, compartment_id, name, version_parameterconflict, is_current, sort_by, limit, page, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if name is not None:
        kwargs['name'] = name
    if version_parameterconflict is not None:
        kwargs['version'] = version_parameterconflict
    if is_current is not None:
        kwargs['is_current'] = is_current
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_services', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_media_workflow_task_declarations,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_media_workflow_task_declarations,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_media_workflow_task_declarations(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@media_workflow_group.command(name=cli_util.override('media_services.list_media_workflows.command_name', 'list'), help=u"""Lists the MediaWorkflows. \n[Command Reference](listMediaWorkflows)""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--id', help=u"""Unique MediaWorkflow identifier.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED"]), help=u"""A filter to return only the resources with lifecycleState matching the given lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return only the resources that match the entire display name given.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'media_services', 'class': 'MediaWorkflowCollection'})
@cli_util.wrap_exceptions
def list_media_workflows(ctx, from_json, all_pages, page_size, compartment_id, id, lifecycle_state, display_name, sort_order, sort_by, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if id is not None:
        kwargs['id'] = id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_services', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_media_workflows,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_media_workflows,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_media_workflows(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@stream_cdn_config_group.command(name=cli_util.override('media_services.list_stream_cdn_configs.command_name', 'list'), help=u"""Lists the StreamCdnConfig. \n[Command Reference](listStreamCdnConfigs)""")
@cli_util.option('--distribution-channel-id', required=True, help=u"""The Stream Distribution Channel identifier this CdnConfig belongs to.""")
@cli_util.option('--id', help=u"""Unique StreamCdnConfig identifier.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED"]), help=u"""A filter to return only the resources with lifecycleState matching the given lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return only the resources that match the entire display name given.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'media_services', 'class': 'StreamCdnConfigCollection'})
@cli_util.wrap_exceptions
def list_stream_cdn_configs(ctx, from_json, all_pages, page_size, distribution_channel_id, id, lifecycle_state, display_name, sort_order, sort_by, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_services', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_stream_cdn_configs,
            distribution_channel_id=distribution_channel_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_stream_cdn_configs,
            limit,
            page_size,
            distribution_channel_id=distribution_channel_id,
            **kwargs
        )
    else:
        result = client.list_stream_cdn_configs(
            distribution_channel_id=distribution_channel_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@stream_distribution_channel_group.command(name=cli_util.override('media_services.list_stream_distribution_channels.command_name', 'list'), help=u"""Lists the Stream Distribution Channels. \n[Command Reference](listStreamDistributionChannels)""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--id', help=u"""Unique Stream Distribution Channel identifier.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED"]), help=u"""A filter to return only the resources with lifecycleState matching the given lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return only the resources that match the entire display name given.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'media_services', 'class': 'StreamDistributionChannelCollection'})
@cli_util.wrap_exceptions
def list_stream_distribution_channels(ctx, from_json, all_pages, page_size, compartment_id, id, lifecycle_state, display_name, sort_order, sort_by, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if id is not None:
        kwargs['id'] = id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_services', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_stream_distribution_channels,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_stream_distribution_channels,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_stream_distribution_channels(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@stream_packaging_config_group.command(name=cli_util.override('media_services.list_stream_packaging_configs.command_name', 'list'), help=u"""Lists the Stream Packaging Configurations. \n[Command Reference](listStreamPackagingConfigs)""")
@cli_util.option('--distribution-channel-id', required=True, help=u"""Unique Stream Distribution Channel identifier.""")
@cli_util.option('--stream-packaging-config-id', help=u"""Unique Stream Packaging Configuration identifier.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED"]), help=u"""A filter to return only the resources with lifecycleState matching the given lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return only the resources that match the entire display name given.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'media_services', 'class': 'StreamPackagingConfigCollection'})
@cli_util.wrap_exceptions
def list_stream_packaging_configs(ctx, from_json, all_pages, page_size, distribution_channel_id, stream_packaging_config_id, lifecycle_state, display_name, sort_order, sort_by, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if stream_packaging_config_id is not None:
        kwargs['stream_packaging_config_id'] = stream_packaging_config_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_services', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_stream_packaging_configs,
            distribution_channel_id=distribution_channel_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_stream_packaging_configs,
            limit,
            page_size,
            distribution_channel_id=distribution_channel_id,
            **kwargs
        )
    else:
        result = client.list_stream_packaging_configs(
            distribution_channel_id=distribution_channel_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@media_workflow_group.command(name=cli_util.override('media_services.list_system_media_workflows.command_name', 'list-system'), help=u"""Lists the SystemMediaWorkflows that can be used to run a job by name or as a template to create a MediaWorkflow. \n[Command Reference](listSystemMediaWorkflows)""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--name', help=u"""A filter to return only the resources with their system defined, unique name matching the given name.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'media_services', 'class': 'SystemMediaWorkflowCollection'})
@cli_util.wrap_exceptions
def list_system_media_workflows(ctx, from_json, all_pages, page_size, compartment_id, name, sort_order, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if name is not None:
        kwargs['name'] = name
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_services', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_system_media_workflows,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_system_media_workflows,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_system_media_workflows(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@media_asset_group.command(name=cli_util.override('media_services.update_media_asset.command_name', 'update'), help=u"""Updates the MediaAsset. \n[Command Reference](updateMediaAsset)""")
@cli_util.option('--media-asset-id', required=True, help=u"""Unique MediaAsset identifier""")
@cli_util.option('--display-name', help=u"""Display name for the Media Asset. Does not have to be unique. Avoid entering confidential information.""")
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["AUDIO", "VIDEO", "PLAYLIST", "IMAGE", "CAPTION_FILE", "UNKNOWN"]), help=u"""The type of the media asset.""")
@cli_util.option('--parent-media-asset-id', help=u"""The ID of the parent asset from which this asset is derived.""")
@cli_util.option('--master-media-asset-id', help=u"""The ID of the senior most asset from which this asset is derived.""")
@cli_util.option('--metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Metadata.

This option is a JSON list with items of type Metadata.  For documentation on Metadata please see our API reference: https://docs.cloud.oracle.com/api/#/en/mediaservices/20211101/datatypes/Metadata.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--media-asset-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of tags for the MediaAsset.

This option is a JSON list with items of type MediaAssetTag.  For documentation on MediaAssetTag please see our API reference: https://docs.cloud.oracle.com/api/#/en/mediaservices/20211101/datatypes/MediaAssetTag.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'metadata': {'module': 'media_services', 'class': 'list[Metadata]'}, 'media-asset-tags': {'module': 'media_services', 'class': 'list[MediaAssetTag]'}, 'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'metadata': {'module': 'media_services', 'class': 'list[Metadata]'}, 'media-asset-tags': {'module': 'media_services', 'class': 'list[MediaAssetTag]'}, 'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'media_services', 'class': 'MediaAsset'})
@cli_util.wrap_exceptions
def update_media_asset(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, media_asset_id, display_name, type, parent_media_asset_id, master_media_asset_id, metadata, media_asset_tags, freeform_tags, defined_tags, if_match):

    if isinstance(media_asset_id, six.string_types) and len(media_asset_id.strip()) == 0:
        raise click.UsageError('Parameter --media-asset-id cannot be whitespace or empty string')
    if not force:
        if metadata or media_asset_tags or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to metadata and media-asset-tags and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if type is not None:
        _details['type'] = type

    if parent_media_asset_id is not None:
        _details['parentMediaAssetId'] = parent_media_asset_id

    if master_media_asset_id is not None:
        _details['masterMediaAssetId'] = master_media_asset_id

    if metadata is not None:
        _details['metadata'] = cli_util.parse_json_parameter("metadata", metadata)

    if media_asset_tags is not None:
        _details['mediaAssetTags'] = cli_util.parse_json_parameter("media_asset_tags", media_asset_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.update_media_asset(
        media_asset_id=media_asset_id,
        update_media_asset_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_media_asset') and callable(getattr(client, 'get_media_asset')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_media_asset(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@media_workflow_group.command(name=cli_util.override('media_services.update_media_workflow.command_name', 'update'), help=u"""Updates the MediaWorkflow. \n[Command Reference](updateMediaWorkflow)""")
@cli_util.option('--media-workflow-id', required=True, help=u"""Unique MediaWorkflow identifier.""")
@cli_util.option('--display-name', help=u"""Name for the MediaWorkflow. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--tasks', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The processing to be done in this workflow. Each key of the MediaWorkflowTasks in this array must be unique within the array.

This option is a JSON list with items of type MediaWorkflowTask.  For documentation on MediaWorkflowTask please see our API reference: https://docs.cloud.oracle.com/api/#/en/mediaservices/20211101/datatypes/MediaWorkflowTask.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--media-workflow-configuration-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configurations to be applied to all jobs for this workflow. Parameters in these configurations are overridden by parameters in the MediaWorkflowConfigurations of the MediaWorkflogJob and the parameters of the MediaWorkflowJob.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""JSON object representing named parameters and their default values that can be referenced throughout this workflow. The values declared here can be overridden by the MediaWorkflowConfigurations or parameters supplied when creating MediaWorkflowJobs from this MediaWorkflow.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'tasks': {'module': 'media_services', 'class': 'list[MediaWorkflowTask]'}, 'media-workflow-configuration-ids': {'module': 'media_services', 'class': 'list[string]'}, 'parameters': {'module': 'media_services', 'class': 'dict(str, object)'}, 'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'tasks': {'module': 'media_services', 'class': 'list[MediaWorkflowTask]'}, 'media-workflow-configuration-ids': {'module': 'media_services', 'class': 'list[string]'}, 'parameters': {'module': 'media_services', 'class': 'dict(str, object)'}, 'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'media_services', 'class': 'MediaWorkflow'})
@cli_util.wrap_exceptions
def update_media_workflow(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, media_workflow_id, display_name, tasks, media_workflow_configuration_ids, parameters, freeform_tags, defined_tags, if_match):

    if isinstance(media_workflow_id, six.string_types) and len(media_workflow_id.strip()) == 0:
        raise click.UsageError('Parameter --media-workflow-id cannot be whitespace or empty string')
    if not force:
        if tasks or media_workflow_configuration_ids or parameters or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to tasks and media-workflow-configuration-ids and parameters and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if tasks is not None:
        _details['tasks'] = cli_util.parse_json_parameter("tasks", tasks)

    if media_workflow_configuration_ids is not None:
        _details['mediaWorkflowConfigurationIds'] = cli_util.parse_json_parameter("media_workflow_configuration_ids", media_workflow_configuration_ids)

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.update_media_workflow(
        media_workflow_id=media_workflow_id,
        update_media_workflow_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_media_workflow') and callable(getattr(client, 'get_media_workflow')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_media_workflow(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@media_workflow_configuration_group.command(name=cli_util.override('media_services.update_media_workflow_configuration.command_name', 'update'), help=u"""Updates the MediaWorkflowConfiguration. \n[Command Reference](updateMediaWorkflowConfiguration)""")
@cli_util.option('--media-workflow-configuration-id', required=True, help=u"""Unique MediaWorkflowConfiguration identifier.""")
@cli_util.option('--display-name', help=u"""Name for the MediaWorkflowConfiguration. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Reuseable parameter values encoded as a JSON; the top and second level JSON elements are objects. Each key of the top level object refer to a task key that is unqiue to the workflow, each of the second level objects' keys refer to the name of a parameter that is unique to the task. taskKey -> parameterName -> parameterValue""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'parameters': {'module': 'media_services', 'class': 'dict(str, object)'}, 'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parameters': {'module': 'media_services', 'class': 'dict(str, object)'}, 'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'media_services', 'class': 'MediaWorkflowConfiguration'})
@cli_util.wrap_exceptions
def update_media_workflow_configuration(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, media_workflow_configuration_id, display_name, parameters, freeform_tags, defined_tags, if_match):

    if isinstance(media_workflow_configuration_id, six.string_types) and len(media_workflow_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --media-workflow-configuration-id cannot be whitespace or empty string')
    if not force:
        if parameters or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to parameters and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.update_media_workflow_configuration(
        media_workflow_configuration_id=media_workflow_configuration_id,
        update_media_workflow_configuration_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_media_workflow_configuration') and callable(getattr(client, 'get_media_workflow_configuration')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_media_workflow_configuration(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@media_workflow_job_group.command(name=cli_util.override('media_services.update_media_workflow_job.command_name', 'update'), help=u"""Updates the MediaWorkflowJob. \n[Command Reference](updateMediaWorkflowJob)""")
@cli_util.option('--media-workflow-job-id', required=True, help=u"""Unique MediaWorkflowJob identifier.""")
@cli_util.option('--display-name', help=u"""Name for the MediaWorkflowJob. Does not have to be unique. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'media_services', 'class': 'MediaWorkflowJob'})
@cli_util.wrap_exceptions
def update_media_workflow_job(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, media_workflow_job_id, display_name, freeform_tags, defined_tags, if_match):

    if isinstance(media_workflow_job_id, six.string_types) and len(media_workflow_job_id.strip()) == 0:
        raise click.UsageError('Parameter --media-workflow-job-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.update_media_workflow_job(
        media_workflow_job_id=media_workflow_job_id,
        update_media_workflow_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_media_workflow_job') and callable(getattr(client, 'get_media_workflow_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_media_workflow_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@stream_cdn_config_group.command(name=cli_util.override('media_services.update_stream_cdn_config.command_name', 'update'), help=u"""Updates the StreamCdnConfig. \n[Command Reference](updateStreamCdnConfig)""")
@cli_util.option('--stream-cdn-config-id', required=True, help=u"""Unique StreamCdnConfig identifier.""")
@cli_util.option('--display-name', help=u"""CDN Config display name.""")
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Whether CDN is enabled for publishing.""")
@cli_util.option('--config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'config': {'module': 'media_services', 'class': 'StreamCdnConfigSection'}, 'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'config': {'module': 'media_services', 'class': 'StreamCdnConfigSection'}, 'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'media_services', 'class': 'StreamCdnConfig'})
@cli_util.wrap_exceptions
def update_stream_cdn_config(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, stream_cdn_config_id, display_name, is_enabled, config, freeform_tags, defined_tags, if_match):

    if isinstance(stream_cdn_config_id, six.string_types) and len(stream_cdn_config_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-cdn-config-id cannot be whitespace or empty string')
    if not force:
        if config or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to config and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if is_enabled is not None:
        _details['isEnabled'] = is_enabled

    if config is not None:
        _details['config'] = cli_util.parse_json_parameter("config", config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.update_stream_cdn_config(
        stream_cdn_config_id=stream_cdn_config_id,
        update_stream_cdn_config_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stream_cdn_config') and callable(getattr(client, 'get_stream_cdn_config')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_stream_cdn_config(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@stream_cdn_config_group.command(name=cli_util.override('media_services.update_stream_cdn_config_akamai_manual_stream_cdn_config.command_name', 'update-stream-cdn-config-akamai-manual-stream-cdn-config'), help=u"""Updates the StreamCdnConfig. \n[Command Reference](updateStreamCdnConfig)""")
@cli_util.option('--stream-cdn-config-id', required=True, help=u"""Unique StreamCdnConfig identifier.""")
@cli_util.option('--display-name', help=u"""CDN Config display name.""")
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Whether CDN is enabled for publishing.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--config-origin-auth-sign-type', type=custom_types.CliCaseInsensitiveChoice(["ForwardURL"]), help=u"""The type of data used to compute the signature.""")
@cli_util.option('--config-origin-auth-sign-encryption', type=custom_types.CliCaseInsensitiveChoice(["SHA256-HMAC"]), help=u"""The type of encryption used to compute the signature.""")
@cli_util.option('--config-origin-auth-secret-key-a', help=u"""The shared secret key A, two for errorless key rotation.""")
@cli_util.option('--config-origin-auth-secret-key-nonce-a', help=u"""Nonce identifier for originAuthSecretKeyA (used to determine key used to sign).""")
@cli_util.option('--config-origin-auth-secret-key-b', help=u"""The shared secret key B, two for errorless key rotation.""")
@cli_util.option('--config-origin-auth-secret-key-nonce-b', help=u"""Nonce identifier for originAuthSecretKeyB (used to determine key used to sign).""")
@cli_util.option('--config-edge-hostname', help=u"""The hostname of the CDN edge server to use when building CDN URLs.""")
@cli_util.option('--config-edge-path-prefix', help=u"""The path to prepend when building CDN URLs.""")
@cli_util.option('--config-is-edge-token-auth', type=click.BOOL, help=u"""Whether token authentication should be used at the CDN edge.""")
@cli_util.option('--config-edge-token-key', help=u"""The encryption key to use for edge token authentication.""")
@cli_util.option('--config-edge-token-salt', help=u"""Salt to use when encrypting authentication token.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'media_services', 'class': 'StreamCdnConfig'})
@cli_util.wrap_exceptions
def update_stream_cdn_config_akamai_manual_stream_cdn_config(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, stream_cdn_config_id, display_name, is_enabled, freeform_tags, defined_tags, if_match, config_origin_auth_sign_type, config_origin_auth_sign_encryption, config_origin_auth_secret_key_a, config_origin_auth_secret_key_nonce_a, config_origin_auth_secret_key_b, config_origin_auth_secret_key_nonce_b, config_edge_hostname, config_edge_path_prefix, config_is_edge_token_auth, config_edge_token_key, config_edge_token_salt):

    if isinstance(stream_cdn_config_id, six.string_types) and len(stream_cdn_config_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-cdn-config-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['config'] = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if is_enabled is not None:
        _details['isEnabled'] = is_enabled

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if config_origin_auth_sign_type is not None:
        _details['config']['originAuthSignType'] = config_origin_auth_sign_type

    if config_origin_auth_sign_encryption is not None:
        _details['config']['originAuthSignEncryption'] = config_origin_auth_sign_encryption

    if config_origin_auth_secret_key_a is not None:
        _details['config']['originAuthSecretKeyA'] = config_origin_auth_secret_key_a

    if config_origin_auth_secret_key_nonce_a is not None:
        _details['config']['originAuthSecretKeyNonceA'] = config_origin_auth_secret_key_nonce_a

    if config_origin_auth_secret_key_b is not None:
        _details['config']['originAuthSecretKeyB'] = config_origin_auth_secret_key_b

    if config_origin_auth_secret_key_nonce_b is not None:
        _details['config']['originAuthSecretKeyNonceB'] = config_origin_auth_secret_key_nonce_b

    if config_edge_hostname is not None:
        _details['config']['edgeHostname'] = config_edge_hostname

    if config_edge_path_prefix is not None:
        _details['config']['edgePathPrefix'] = config_edge_path_prefix

    if config_is_edge_token_auth is not None:
        _details['config']['isEdgeTokenAuth'] = config_is_edge_token_auth

    if config_edge_token_key is not None:
        _details['config']['edgeTokenKey'] = config_edge_token_key

    if config_edge_token_salt is not None:
        _details['config']['edgeTokenSalt'] = config_edge_token_salt

    _details['config']['type'] = 'AKAMAI_MANUAL'

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.update_stream_cdn_config(
        stream_cdn_config_id=stream_cdn_config_id,
        update_stream_cdn_config_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stream_cdn_config') and callable(getattr(client, 'get_stream_cdn_config')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_stream_cdn_config(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@stream_cdn_config_group.command(name=cli_util.override('media_services.update_stream_cdn_config_edge_stream_cdn_config.command_name', 'update-stream-cdn-config-edge-stream-cdn-config'), help=u"""Updates the StreamCdnConfig. \n[Command Reference](updateStreamCdnConfig)""")
@cli_util.option('--stream-cdn-config-id', required=True, help=u"""Unique StreamCdnConfig identifier.""")
@cli_util.option('--display-name', help=u"""CDN Config display name.""")
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Whether CDN is enabled for publishing.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'media_services', 'class': 'StreamCdnConfig'})
@cli_util.wrap_exceptions
def update_stream_cdn_config_edge_stream_cdn_config(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, stream_cdn_config_id, display_name, is_enabled, freeform_tags, defined_tags, if_match):

    if isinstance(stream_cdn_config_id, six.string_types) and len(stream_cdn_config_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-cdn-config-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['config'] = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if is_enabled is not None:
        _details['isEnabled'] = is_enabled

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['config']['type'] = 'EDGE'

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.update_stream_cdn_config(
        stream_cdn_config_id=stream_cdn_config_id,
        update_stream_cdn_config_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stream_cdn_config') and callable(getattr(client, 'get_stream_cdn_config')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_stream_cdn_config(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@stream_distribution_channel_group.command(name=cli_util.override('media_services.update_stream_distribution_channel.command_name', 'update'), help=u"""Updates the Stream Distribution Channel. \n[Command Reference](updateStreamDistributionChannel)""")
@cli_util.option('--stream-distribution-channel-id', required=True, help=u"""Unique Stream Distribution Channel path identifier.""")
@cli_util.option('--display-name', help=u"""Stream Distribution channel display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'media_services', 'class': 'StreamDistributionChannel'})
@cli_util.wrap_exceptions
def update_stream_distribution_channel(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, stream_distribution_channel_id, display_name, freeform_tags, defined_tags, if_match):

    if isinstance(stream_distribution_channel_id, six.string_types) and len(stream_distribution_channel_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-distribution-channel-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.update_stream_distribution_channel(
        stream_distribution_channel_id=stream_distribution_channel_id,
        update_stream_distribution_channel_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stream_distribution_channel') and callable(getattr(client, 'get_stream_distribution_channel')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_stream_distribution_channel(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@stream_packaging_config_group.command(name=cli_util.override('media_services.update_stream_packaging_config.command_name', 'update'), help=u"""Updates the Stream Packaging Configuration. \n[Command Reference](updateStreamPackagingConfig)""")
@cli_util.option('--stream-packaging-config-id', required=True, help=u"""Unique Stream Packaging Configuration path identifier.""")
@cli_util.option('--display-name', help=u"""The name of the stream Packaging Configuration. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'media_services', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'media_services', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'media_services', 'class': 'StreamPackagingConfig'})
@cli_util.wrap_exceptions
def update_stream_packaging_config(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, stream_packaging_config_id, display_name, freeform_tags, defined_tags, if_match):

    if isinstance(stream_packaging_config_id, six.string_types) and len(stream_packaging_config_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-packaging-config-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('media_services', 'media_services', ctx)
    result = client.update_stream_packaging_config(
        stream_packaging_config_id=stream_packaging_config_id,
        update_stream_packaging_config_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stream_packaging_config') and callable(getattr(client, 'get_stream_packaging_config')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_stream_packaging_config(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
