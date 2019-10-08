# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click

from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types
from services.dts.src.oci_cli_transfer_job.generated import transferjob_cli
from services.dts.src.oci_cli_dts.physicalappliance_cli_extended import validate_upload_user_credentials


close_exclude_list = ['id', 'lifecycle_state', 'device_type', 'if_match', 'wait_for_state', 'max_wait_seconds', 'wait_interval_seconds', 'freeform_tags', 'defined_tags', 'display_name', 'force']


@cli_util.copy_params_from_generated_command(transferjob_cli.update_transfer_job, params_to_exclude=close_exclude_list)
@transferjob_cli.transfer_job_root_group.command(name='close', help="""Closes the transfer disk or appliance job.""")
@cli_util.option('--job-id', required=True, help=u"""OCID of the Transfer Job""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler({})
@cli_util.wrap_exceptions
def close_transfer_job_extended(ctx, **kwargs):
    if 'job_id' in kwargs:
        kwargs['id'] = kwargs['job_id']
        kwargs.pop('job_id')
    kwargs["lifecycle_state"] = "CLOSED"
    ctx.invoke(transferjob_cli.update_transfer_job, **kwargs)


@cli_util.copy_params_from_generated_command(transferjob_cli.get_transfer_job, params_to_exclude=['id'])
@transferjob_cli.transfer_job_root_group.command(name='verify-upload-user-credentials', help="""Verifies the transfer disk or appliance upload user credentials.""")
@cli_util.option('--bucket', required=True, help=u"""Upload bucket name""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler({})
@cli_util.wrap_exceptions
def verify_upload_user_credentials_extended(ctx, from_json, bucket, **kwargs):
    validate_upload_user_credentials(ctx, bucket)


@cli_util.copy_params_from_generated_command(transferjob_cli.create_transfer_job, params_to_exclude=['compartment_id', "upload_bucket_name", "display_name", "device_type", "freeform_tags", "defined_tags"])
@transferjob_cli.transfer_job_root_group.command(name='create', help=transferjob_cli.create_transfer_job.help)
@cli_util.option('--compartment-id', required=True, help=u"""Compartment OCID""")
@cli_util.option('--bucket', required=True, help=u"""Upload bucket name""")
@cli_util.option('--display-name', required=True, help=u"""Job display name""")
@cli_util.option('--device-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["DISK", "APPLIANCE"]), help=u"""Transfer device type""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"foo-value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'dts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dts', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dts', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'dts', 'class': 'TransferJob'})
@cli_util.wrap_exceptions
def create_transfer_job_extended(ctx, **kwargs):
    if 'bucket' in kwargs:
        kwargs['upload_bucket_name'] = kwargs['bucket']
        kwargs.pop('bucket')
    ctx.invoke(transferjob_cli.create_transfer_job, **kwargs)


@cli_util.copy_params_from_generated_command(transferjob_cli.get_transfer_job, params_to_exclude=['id'])
@transferjob_cli.transfer_job_root_group.command(name=transferjob_cli.get_transfer_job.name, help=transferjob_cli.get_transfer_job.help)
@cli_util.option('--job-id', required=True, help=u"""OCID of the Transfer Job""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler({})
@cli_util.wrap_exceptions
def show_transfer_job_extended(ctx, **kwargs):
    if 'job_id' in kwargs:
        kwargs['id'] = kwargs['job_id']
        kwargs.pop('job_id')
    ctx.invoke(transferjob_cli.get_transfer_job, **kwargs)


update_exclude_list = ['id', 'lifecycle_state', 'device_type', 'if_match', 'wait_for_state', 'max_wait_seconds', 'wait_interval_seconds', "freeform_tags", "defined_tags"]


@cli_util.copy_params_from_generated_command(transferjob_cli.update_transfer_job, params_to_exclude=update_exclude_list)
@transferjob_cli.transfer_job_root_group.command(name=transferjob_cli.update_transfer_job.name, help=transferjob_cli.update_transfer_job.help)
@cli_util.option('--job-id', required=True, help=u"""OCID of the Transfer Job""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"foo-value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'dts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dts', 'class': 'dict(str, dict(str, object))'}})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dts', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'dts', 'class': 'TransferJob'})
@cli_util.wrap_exceptions
def update_transfer_job_extended(ctx, **kwargs):
    if 'job_id' in kwargs:
        kwargs['id'] = kwargs['job_id']
        kwargs.pop('job_id')
    ctx.invoke(transferjob_cli.update_transfer_job, **kwargs)


delete_exclude_list = ['id', 'wait_for_state', 'max_wait_seconds', 'wait_interval_seconds']


@cli_util.copy_params_from_generated_command(transferjob_cli.delete_transfer_job, params_to_exclude=delete_exclude_list)
@transferjob_cli.transfer_job_root_group.command(name=transferjob_cli.delete_transfer_job.name, help=transferjob_cli.delete_transfer_job.help)
@cli_util.option('--job-id', required=True, help=u"""OCID of the Transfer Job""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler({})
@cli_util.wrap_exceptions
def delete_transfer_job_extended(ctx, **kwargs):
    if 'job_id' in kwargs:
        kwargs['id'] = kwargs['job_id']
        kwargs.pop('job_id')
    ctx.invoke(transferjob_cli.delete_transfer_job, **kwargs)


@cli_util.copy_params_from_generated_command(transferjob_cli.change_transfer_job_compartment, params_to_exclude=['transfer_job_id'])
@transferjob_cli.transfer_job_root_group.command(name=transferjob_cli.change_transfer_job_compartment.name, help=transferjob_cli.change_transfer_job_compartment.help)
@cli_util.option('--job-id', required=True, help=u"""ID of the Transfer Job""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler({})
@cli_util.wrap_exceptions
def change_transfer_job_compartment_extended(ctx, **kwargs):
    if 'job_id' in kwargs:
        kwargs['transfer_job_id'] = kwargs['job_id']
        kwargs.pop('job_id')
    ctx.invoke(transferjob_cli.change_transfer_job_compartment, **kwargs)
