# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.gdp.src.oci_cli_guarded_data_pipeline.generated import guardeddatapipeline_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci gdp gdp-work-request -> oci gdp work-request
cli_util.rename_command(guardeddatapipeline_cli, guardeddatapipeline_cli.gdp_root_group, guardeddatapipeline_cli.gdp_work_request_group, "work-request")


# oci gdp gdp-pipeline -> oci gdp pipeline
cli_util.rename_command(guardeddatapipeline_cli, guardeddatapipeline_cli.gdp_root_group, guardeddatapipeline_cli.gdp_pipeline_group, "pipeline")


# oci gdp work-request-error list-gdp -> oci gdp work-request-error list
cli_util.rename_command(guardeddatapipeline_cli, guardeddatapipeline_cli.work_request_error_group, guardeddatapipeline_cli.list_gdp_work_request_errors, "list")


# oci gdp work-request-log-entry list-gdp-work-request-logs -> oci gdp work-request-log-entry list
cli_util.rename_command(guardeddatapipeline_cli, guardeddatapipeline_cli.work_request_log_entry_group, guardeddatapipeline_cli.list_gdp_work_request_logs, "list")


# Remove rotate-gdp-pipeline-keys from oci gdp gdp-pipeline
guardeddatapipeline_cli.gdp_pipeline_group.commands.pop(guardeddatapipeline_cli.rotate_gdp_pipeline_keys.name)


@cli_util.copy_params_from_generated_command(guardeddatapipeline_cli.create_gdp_pipeline, params_to_exclude=['is_file_override_in_destination_enabled', 'is_chunking_enabled'])
@guardeddatapipeline_cli.gdp_pipeline_group.command(name=guardeddatapipeline_cli.create_gdp_pipeline.name, help=guardeddatapipeline_cli.create_gdp_pipeline.help)
@cli_util.option('--is-fileoverride-enabled', type=click.BOOL, help=u"""Enable file override feature in destination bucket""")
@cli_util.option('--is-chunking-enabled', type=click.BOOL, help=u"""Specifies whether the file should be chunked during transfer. This option needs for both SENDER and Receiver pipelines. Chunking is required for large file transfers and recommended for optimal performance.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'file-types': {'module': 'gdp', 'class': 'list[string]'}, 'bucket-details': {'module': 'gdp', 'class': 'list[BucketDetailsDefinition]'}, 'freeform-tags': {'module': 'gdp', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'gdp', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_gdp_pipeline_extended(ctx, **kwargs):

    if 'is_fileoverride_enabled' in kwargs:
        kwargs['is_file_override_in_destination_enabled'] = kwargs['is_fileoverride_enabled']
        kwargs.pop('is_fileoverride_enabled')

    ctx.invoke(guardeddatapipeline_cli.create_gdp_pipeline, **kwargs)


@cli_util.copy_params_from_generated_command(guardeddatapipeline_cli.update_gdp_pipeline, params_to_exclude=['is_file_override_in_destination_enabled', 'is_chunking_enabled'])
@guardeddatapipeline_cli.gdp_pipeline_group.command(name=guardeddatapipeline_cli.update_gdp_pipeline.name, help=guardeddatapipeline_cli.update_gdp_pipeline.help)
@cli_util.option('--is-fileoverride-enabled', type=click.BOOL, help=u"""Enable file override feature in destination bucket""")
@cli_util.option('--is-chunking-enabled', type=click.BOOL, help=u"""Specifies whether the file should be chunked during transfer. This option needs for both SENDER and Receiver pipelines. Chunking is required for large file transfers and recommended for optimal performance.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'file-types': {'module': 'gdp', 'class': 'list[string]'}, 'freeform-tags': {'module': 'gdp', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'gdp', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_gdp_pipeline_extended(ctx, **kwargs):

    if 'is_fileoverride_enabled' in kwargs:
        kwargs['is_file_override_in_destination_enabled'] = kwargs['is_fileoverride_enabled']
        kwargs.pop('is_fileoverride_enabled')

    ctx.invoke(guardeddatapipeline_cli.update_gdp_pipeline, **kwargs)
