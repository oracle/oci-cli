# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci
import sys

from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types

from services.dts.src.oci_cli_appliance_export_job.applianceexportjob_cli_extended import create_os_client
from services.dts.src.oci_cli_dts.cli_utils import setup_notifications_helper, error_message_wrapper
from services.dts.src.oci_cli_transfer_appliance.transferappliance_cli_extended import get_transfer_appliance_helper
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


def create_transfer_job_client(ctx):
    return cli_util.build_client('dts', 'transfer_job', ctx)


@cli_util.copy_params_from_generated_command(transferjob_cli.get_transfer_job, params_to_exclude=['id'])
@transferjob_cli.transfer_job_root_group.command(name='verify-upload-user-credentials', help="""Verifies the transfer disk or appliance upload user credentials.""")
@cli_util.option('--bucket', required=True, help=u"""Upload bucket name""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler({})
@cli_util.wrap_exceptions
def verify_upload_user_credentials_extended(ctx, from_json, bucket, **kwargs):

    create_transfer_job_client(ctx)
    try:
        validate_upload_user_credentials(ctx, bucket, None)
        click.echo("Successfully verified upload user credentials")
    except Exception as e:
        error_message_wrapper("Failed to verify upload user credentials: %s" % e)


def validate_bucket_belongs_to_compartment(ctx, bucket, compartment_id):
    ctx.endpoint = None
    ctx.obj['endpoint'] = None
    os_client = create_os_client(ctx)
    namespace = os_client.get_namespace().data

    bucket_obj = os_client.get_bucket(
        namespace_name=namespace,
        bucket_name=bucket
    )
    if bucket_obj.data.compartment_id != compartment_id:
        raise oci.exceptions.ClientError("The bucket {0} does not belong to compartment {1}".format(bucket, compartment_id))


@cli_util.copy_params_from_generated_command(transferjob_cli.create_transfer_job, params_to_exclude=['compartment_id', "upload_bucket_name", "display_name", "device_type", "freeform_tags", "defined_tags"])
@transferjob_cli.transfer_job_root_group.command(name='create', help=transferjob_cli.create_transfer_job.help)
@cli_util.option('--compartment-id', required=True, help=u"""Compartment OCID""")
@cli_util.option('--bucket', required=True, help=u"""Upload bucket name""")
@cli_util.option('--display-name', required=True, help=u"""Job display name""")
@cli_util.option('--device-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["DISK", "APPLIANCE"]), help=u"""Transfer device type""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"foo-value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--setup-notifications', is_flag=True, help=u"""Setup notifications for the transfer appliance""")
@cli_util.option('--skip-upload-user-check', required=False, is_flag=True,
                 help=u"""Skip checking whether the upload user has the right credentials""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'dts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dts', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dts', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'dts', 'class': 'TransferJob'})
@cli_util.wrap_exceptions
def create_transfer_job_extended(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, bucket, display_name, device_type, freeform_tags, defined_tags, setup_notifications, skip_upload_user_check):

    # Copied the generated command because the result is needed to setup notifications
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}

    if compartment_id is not None:
        details['compartmentId'] = compartment_id

    if bucket is not None:
        details['uploadBucketName'] = bucket

    if display_name is not None:
        details['displayName'] = display_name

    if device_type is not None:
        details['deviceType'] = device_type

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('dts', 'transfer_job', ctx)
    if not skip_upload_user_check:
        validate_bucket_belongs_to_compartment(ctx, bucket, compartment_id)
        validate_upload_user_credentials(ctx, bucket)

    result = client.create_transfer_job(
        create_transfer_job_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_transfer_job') and callable(getattr(client, 'get_transfer_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_transfer_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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

    if setup_notifications:
        setup_import_notifications(ctx, result.data.id)


def get_transfer_job_helper(ctx, from_json, id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dts', 'transfer_job', ctx)
    result = client.get_transfer_job(
        id=id,
        **kwargs
    )
    return result


def show_transfer_job_with_details(ctx, **kwargs):
    result = get_transfer_job_helper(ctx, kwargs['from_json'], kwargs['id'])
    transfer_job_obj = result.data
    # Embed appliance details in response_data
    appliances_list = []
    if transfer_job_obj.device_type == "APPLIANCE":
        if transfer_job_obj.attached_transfer_appliance_labels:
            for each_appliance_lbl in transfer_job_obj.attached_transfer_appliance_labels:
                appliance_obj = get_transfer_appliance_helper(ctx, kwargs['from_json'], kwargs['id'], each_appliance_lbl).data
                appliances_list.append({'label': each_appliance_lbl, 'serialNumber': appliance_obj.serial_number,
                                        'status': appliance_obj.lifecycle_state, 'uploadStatusLogURL': appliance_obj.upload_status_log_uri})

    result.data.attached_transfer_appliance_labels = appliances_list
    return result


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

    result = show_transfer_job_with_details(ctx, **kwargs)

    cli_util.render_response(result, ctx)


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


@transferjob_cli.transfer_job_root_group.command(name='setup-notifications', help=u"""Setup notifications for import job""")
@cli_util.option('--job-id', required=True, help=u"""OCID of the transfer job""")
@click.pass_context
@cli_util.help_option
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={},
                                                      output_type={'module': 'dts', 'class': 'TransferAppliance'})
@cli_util.wrap_exceptions
def setup_import_notifications_for_job_extended(ctx, job_id):
    setup_import_notifications(ctx, job_id)


def setup_import_notifications(ctx, job_id):
    # Create the topic, subscriptions and rule in the root compartment so that everything trickles down
    config = oci.config.from_file(file_location=ctx.obj['config_file'], profile_name=ctx.obj['profile'])
    root_compartment = config['tenancy']

    create_topic_details = {
        'name': 'DTSImportJobTopic_{}'.format(job_id[-6:]),
        'description': 'Topic for data transfer service import job with OCID {}'.format(job_id),
        'compartmentId': root_compartment
    }
    create_rule_kwargs = {
        'display_name': 'DTSImportJobRule_{}'.format(job_id[-6:]),
        'compartment_id': root_compartment,
        'description': 'Rule for data transfer service to send notifications for an import job with OCID {}'.format(job_id),
        'is_enabled': True,
        'condition': '{"eventType":"com.oraclecloud.datatransferservice.*transferjob","data":{"resourceId":"%s"}}' % job_id,
        'actions': {
            'actions': [
                {
                    'actionType': 'ONS',
                    'topicId': None,
                    'isEnabled': True
                }
            ]
        }
    }
    setup_notifications_helper(ctx, create_topic_details, create_rule_kwargs)
