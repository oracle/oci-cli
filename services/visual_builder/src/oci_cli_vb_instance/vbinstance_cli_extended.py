# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.visual_builder.src.oci_cli_vb_instance.generated import vbinstance_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci visual-builder application-summary-collection -> oci visual-builder application
cli_util.rename_command(vbinstance_cli, vbinstance_cli.visual_builder_root_group, vbinstance_cli.application_summary_collection_group, "application")


# oci visual-builder work-request-error-collection -> oci visual-builder work-request-error
cli_util.rename_command(vbinstance_cli, vbinstance_cli.visual_builder_root_group, vbinstance_cli.work_request_error_collection_group, "work-request-error")


# oci visual-builder work-request-error-collection list-work-request-errors -> oci visual-builder work-request-error-collection list
cli_util.rename_command(vbinstance_cli, vbinstance_cli.work_request_error_collection_group, vbinstance_cli.list_work_request_errors, "list")


# oci visual-builder work-request-log-entry-collection -> oci visual-builder work-request-log-entry
cli_util.rename_command(vbinstance_cli, vbinstance_cli.visual_builder_root_group, vbinstance_cli.work_request_log_entry_collection_group, "work-request-log-entry")


# oci visual-builder work-request-log-entry-collection list-work-request-logs -> oci visual-builder work-request-log-entry-collection list
cli_util.rename_command(vbinstance_cli, vbinstance_cli.work_request_log_entry_collection_group, vbinstance_cli.list_work_request_logs, "list")


# oci visual-builder work-request-summary-collection list-work-requests -> oci visual-builder work-request-summary-collection list
cli_util.rename_command(vbinstance_cli, vbinstance_cli.work_request_summary_collection_group, vbinstance_cli.list_work_requests, "list")


# oci visual-builder vb-instance-summary-collection list-vb-instances -> oci visual-builder vb-instance-summary-collection list
cli_util.rename_command(vbinstance_cli, vbinstance_cli.vb_instance_summary_collection_group, vbinstance_cli.list_vb_instances, "list")


# Move commands under 'oci visual-builder work-request-summary-collection' -> 'oci visual-builder work-request'
vbinstance_cli.visual_builder_root_group.commands.pop(vbinstance_cli.work_request_summary_collection_group.name)


# Move commands under 'oci visual-builder vb-instance-summary-collection' -> 'oci visual-builder vb-instance'
vbinstance_cli.visual_builder_root_group.commands.pop(vbinstance_cli.vb_instance_summary_collection_group.name)
vbinstance_cli.vb_instance_group.add_command(vbinstance_cli.list_vb_instances)


@cli_util.copy_params_from_generated_command(vbinstance_cli.list_work_requests, params_to_exclude=['vb_instance_id'])
@vbinstance_cli.work_request_group.command(name=vbinstance_cli.list_work_requests.name, help=vbinstance_cli.list_work_requests.help)
@cli_util.option('--id', help=u"""The Vb Instance identifier to use to filter results""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'visual_builder', 'class': 'WorkRequestSummaryCollection'})
@cli_util.wrap_exceptions
def list_work_requests_extended(ctx, **kwargs):
    if 'id' in kwargs:
        kwargs['vb_instance_id'] = kwargs['id']
        kwargs.pop('id')

    ctx.invoke(vbinstance_cli.list_work_requests, **kwargs)


@cli_util.copy_params_from_generated_command(vbinstance_cli.change_vb_instance_compartment, params_to_exclude=['vb_instance_id'])
@vbinstance_cli.vb_instance_group.command(name=vbinstance_cli.change_vb_instance_compartment.name, help=vbinstance_cli.change_vb_instance_compartment.help)
@cli_util.option('--id', required=True, help=u"""Unique Vb Instance identifier. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_vb_instance_compartment_extended(ctx, **kwargs):
    if 'id' in kwargs:
        kwargs['vb_instance_id'] = kwargs['id']
        kwargs.pop('id')

    ctx.invoke(vbinstance_cli.change_vb_instance_compartment, **kwargs)


@cli_util.copy_params_from_generated_command(vbinstance_cli.delete_vb_instance, params_to_exclude=['vb_instance_id'])
@vbinstance_cli.vb_instance_group.command(name=vbinstance_cli.delete_vb_instance.name, help=vbinstance_cli.delete_vb_instance.help)
@cli_util.option('--id', required=True, help=u"""Unique Vb Instance identifier. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_vb_instance_extended(ctx, **kwargs):
    if 'id' in kwargs:
        kwargs['vb_instance_id'] = kwargs['id']
        kwargs.pop('id')

    ctx.invoke(vbinstance_cli.delete_vb_instance, **kwargs)


@cli_util.copy_params_from_generated_command(vbinstance_cli.get_vb_instance, params_to_exclude=['vb_instance_id'])
@vbinstance_cli.vb_instance_group.command(name=vbinstance_cli.get_vb_instance.name, help=vbinstance_cli.get_vb_instance.help)
@cli_util.option('--id', required=True, help=u"""Unique Vb Instance identifier. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'visual_builder', 'class': 'VbInstance'})
@cli_util.wrap_exceptions
def get_vb_instance_extended(ctx, **kwargs):
    if 'id' in kwargs:
        kwargs['vb_instance_id'] = kwargs['id']
        kwargs.pop('id')

    ctx.invoke(vbinstance_cli.get_vb_instance, **kwargs)


@cli_util.copy_params_from_generated_command(vbinstance_cli.start_vb_instance, params_to_exclude=['vb_instance_id'])
@vbinstance_cli.vb_instance_group.command(name=vbinstance_cli.start_vb_instance.name, help=vbinstance_cli.start_vb_instance.help)
@cli_util.option('--id', required=True, help=u"""Unique Vb Instance identifier. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def start_vb_instance_extended(ctx, **kwargs):
    if 'id' in kwargs:
        kwargs['vb_instance_id'] = kwargs['id']
        kwargs.pop('id')

    ctx.invoke(vbinstance_cli.start_vb_instance, **kwargs)


@cli_util.copy_params_from_generated_command(vbinstance_cli.stop_vb_instance, params_to_exclude=['vb_instance_id'])
@vbinstance_cli.vb_instance_group.command(name=vbinstance_cli.stop_vb_instance.name, help=vbinstance_cli.stop_vb_instance.help)
@cli_util.option('--id', required=True, help=u"""Unique Vb Instance identifier. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def stop_vb_instance_extended(ctx, **kwargs):
    if 'id' in kwargs:
        kwargs['vb_instance_id'] = kwargs['id']
        kwargs.pop('id')

    ctx.invoke(vbinstance_cli.stop_vb_instance, **kwargs)


@cli_util.copy_params_from_generated_command(vbinstance_cli.update_vb_instance, params_to_exclude=['vb_instance_id'])
@vbinstance_cli.vb_instance_group.command(name=vbinstance_cli.update_vb_instance.name, help=vbinstance_cli.update_vb_instance.help)
@cli_util.option('--id', required=True, help=u"""Unique Vb Instance identifier. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'visual_builder', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'visual_builder', 'class': 'dict(str, dict(str, object))'}, 'custom-endpoint': {'module': 'visual_builder', 'class': 'UpdateCustomEndpointDetails'}, 'alternate-custom-endpoints': {'module': 'visual_builder', 'class': 'list[UpdateCustomEndpointDetails]'}, 'network-endpoint-details': {'module': 'visual_builder', 'class': 'UpdateNetworkEndpointDetails'}})
@cli_util.wrap_exceptions
def update_vb_instance_extended(ctx, **kwargs):
    if 'id' in kwargs:
        kwargs['vb_instance_id'] = kwargs['id']
        kwargs.pop('id')

    ctx.invoke(vbinstance_cli.update_vb_instance, **kwargs)


# oci visual-builder application request-summarized-applications -> oci visual-builder application list
cli_util.rename_command(vbinstance_cli, vbinstance_cli.application_summary_collection_group, vbinstance_cli.request_summarized_applications, "list")


@cli_util.copy_params_from_generated_command(vbinstance_cli.request_summarized_applications, params_to_exclude=['vb_instance_id'])
@vbinstance_cli.application_summary_collection_group.command(name=vbinstance_cli.request_summarized_applications.name, help=vbinstance_cli.request_summarized_applications.help)
@cli_util.option('--id', required=True, help=u"""Unique Vb Instance identifier. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'visual_builder', 'class': 'ApplicationSummaryCollection'})
@cli_util.wrap_exceptions
def request_summarized_applications_extended(ctx, **kwargs):
    if 'id' in kwargs:
        kwargs['vb_instance_id'] = kwargs['id']
        kwargs.pop('id')

    ctx.invoke(vbinstance_cli.request_summarized_applications, **kwargs)
