# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import six
import time
import oci
import json

from oci import exceptions
from oci.dts.models.update_appliance_export_job_details import UpdateApplianceExportJobDetails
from oci_cli import cli_util
from oci_cli import json_skeleton_utils

from services.dts.src.oci_cli_dts.appliance_constants import APPLIANCE_STATE_LOCKED, APPLIANCE_STATUS_NA
from services.dts.src.oci_cli_dts.cli_utils import setup_notifications_helper
from services.dts.src.oci_cli_dts.generated import dts_service_cli
from services.dts.src.oci_cli_appliance_export_job.generated import applianceexportjob_cli
from services.dts.src.oci_cli_transfer_appliance.transferappliance_cli_extended import customer_address_options
from services.dts.src.oci_cli_dts.physicalappliance_cli_extended import pa_init_auth_helper, pa_unlock_helper, \
    pa_show_helper
from services.dts.src.oci_cli_dts.nfsdataset_cli_extended import create_nfs_dataset_client, nfs_dataset_set_export, deactivate_nfs_dataset
from services.dts.src.oci_cli_appliance_export_job.manifest.manifest_iterator import CasperListIterator
from services.dts.src.oci_cli_appliance_export_job.manifest.manifest_stats_consumer import ManifestStatsConsumer
from services.dts.src.oci_cli_appliance_export_job.manifest.manifest_writer import ManifestWriter
from services.dts.src.oci_cli_appliance_export_job.manifest.object_uploader import ObjectUploader
from services.dts.src.oci_cli_appliance_export_job.applianceexportjob_constants import \
    LIFECYCLE_STATE_DETAILS_PENDING_SUBMISSION, LIFECYCLE_STATE_DETAILS_PENDING_APPROVAL, \
    LIFECYCLE_STATE_DETAILS_CUSTOMER_PROCESSING, OBJECT_STORAGE_BUCKET_TYPE_ARCHIVE, \
    LIFECYCLE_STATE_DETAILS_ORACLE_SHIPPED, LIFECYCLE_STATE_DETAILS_CUSTOMER_RECEIVED

cli_util.rename_command(dts_service_cli, dts_service_cli.dts_service_group, applianceexportjob_cli.appliance_export_job_root_group, 'export')
cli_util.rename_command(dts_service_cli, applianceexportjob_cli.appliance_export_job_root_group, applianceexportjob_cli.get_appliance_export_job, 'show')
applianceexportjob_cli.appliance_export_job_root_group.commands.pop(applianceexportjob_cli.appliance_export_job_group.name)
applianceexportjob_cli.appliance_export_job_root_group.add_command(applianceexportjob_cli.list_appliance_export_jobs)


@applianceexportjob_cli.appliance_export_job_root_group.command(name='setup-notifications', help=u"""Setup notifications for export""")
@click.pass_context
@cli_util.help_option
@cli_util.wrap_exceptions
def setup_notifications_extended(ctx):
    setup_export_notifications(ctx)


@cli_util.copy_params_from_generated_command(applianceexportjob_cli.create_appliance_export_job, params_to_exclude=['customer_shipping_address', 'compartment_id', 'bucket_name', 'display_name', 'prefix', 'range_start', 'range_end'])
@applianceexportjob_cli.appliance_export_job_root_group.command(name=applianceexportjob_cli.create_appliance_export_job.name, help=applianceexportjob_cli.create_appliance_export_job.help)
@cli_util.option('--compartment-id', required=True, help=u"""OCID of the compartment in which the export job is created""")
@cli_util.option('--bucket-name', required=True, help=u"""Name of the object storage bucket for this export job""")
@cli_util.option('--display-name', required=True, help=u"""User friendly name of the export job""")
@cli_util.option('--addressee', required=True, help=u"""Company or person to send the appliance to""")
@cli_util.option('--care-of', required=True, help=u"""Place/person to direct the package to.""")
@cli_util.option('--address1', required=True, help=u"""Address line 1.""")
@cli_util.option('--address2', help=u"""Optional address line 2.""")
@cli_util.option('--address3', help=u"""Optional address line 3.""")
@cli_util.option('--address4', help=u"""Optional address line 4.""")
@cli_util.option('--city-or-locality', required=True, help=u"""City or Locality.""")
@cli_util.option('--state-province-region', required=True, help=u"""State or Province or Region.""")
@cli_util.option('--country', required=True, help=u"""Country.""")
@cli_util.option('--zip-postal-code', required=True, help=u"""Zip or Postal Code""")
@cli_util.option('--phone-number', required=True, help=u"""Phone number.""")
@cli_util.option('--email', required=True, help=u"""Email address.""")
@cli_util.option('--setup-notifications', type=click.BOOL, help=u"""Setup notifications for export""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dts', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'dts', 'class': 'ApplianceExportJob'})
@cli_util.wrap_exceptions
def create_appliance_export_job_extended(ctx, **kwargs):

    ctx.endpoint = None
    ctx.obj['endpoint'] = None
    os_client = create_os_client(ctx)
    namespace = os_client.get_namespace().data

    result = os_client.get_bucket(
        namespace_name=namespace,
        bucket_name=kwargs['bucket_name']
    )

    if result.data.storage_tier == OBJECT_STORAGE_BUCKET_TYPE_ARCHIVE:
        raise click.UsageError('Export for Archive buckets is currently not supported')

    kwargs['customer_shipping_address'] = {}
    for option, value in customer_address_options.items():
        if option in kwargs:
            kwargs['customer_shipping_address'][value] = kwargs[option]
            kwargs.pop(option)

    if kwargs['setup_notifications'] is None:
        if click.confirm("It is a pre-requisite to setup notifications for export. Do you want to setup notifications?"):
            setup_export_notifications(ctx)
        else:
            click.echo("Continuing without setting up notifications. Please make sure that you have set it up")
    elif kwargs['setup_notifications']:
        setup_export_notifications(ctx)
    kwargs.pop('setup_notifications')
    ctx.invoke(applianceexportjob_cli.create_appliance_export_job, **kwargs)


def setup_export_notifications(ctx):
    # Create the topic, subscriptions and rule in the root compartment so that everything trickles down
    config = oci.config.from_file(file_location=ctx.obj['config_file'], profile_name=ctx.obj['profile'])
    root_compartment = config['tenancy']

    create_topic_details = {
        'name': 'DTSExportTopic',
        'description': 'Topic for data transfer service export jobs',
        'compartmentId': root_compartment
    }

    create_rule_kwargs = {
        'display_name': 'DTSExportRule',
        'compartment_id': root_compartment,
        'description': 'Rule for data transfer service to send notifications for export jobs',
        'is_enabled': True,
        'condition': '{"eventType":"com.oraclecloud.datatransferservice.*applianceexportjob"}',
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


def create_os_client(ctx):
    return cli_util.build_client('object_storage', 'object_storage', ctx)


def policy_printer(policy_name, bucket_access_policies):
    click.echo('NOTE: Sometimes you will need to replace a single quote with \'\"\'\"\'')
    create_policy_command = 'oci iam policy create --name {} --compartment-id $ROOT_COMPARTMENT ' \
                            '--statements \'{}\' --description "The policies to allow DTS to process the export job"'.format(policy_name, json.dumps(bucket_access_policies))
    click.echo(create_policy_command)


def get_bucket_access_policies(result):
    return result.data.bucket_access_policies


@cli_util.copy_params_from_generated_command(applianceexportjob_cli.change_appliance_export_job_compartment, params_to_exclude=['appliance_export_job_id'])
@applianceexportjob_cli.appliance_export_job_root_group.command(name=applianceexportjob_cli.change_appliance_export_job_compartment.name, help=applianceexportjob_cli.change_appliance_export_job_compartment.help)
@cli_util.option('--job-id', required=True, help=u"""OCID of the Export Job""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_appliance_export_job_compartment_extended(ctx, **kwargs):
    if 'job_id' in kwargs:
        kwargs['appliance_export_job_id'] = kwargs['job_id']
        kwargs.pop('job_id')
    ctx.invoke(applianceexportjob_cli.change_appliance_export_job_compartment, **kwargs)


@cli_util.copy_params_from_generated_command(applianceexportjob_cli.delete_appliance_export_job, params_to_exclude=['appliance_export_job_id'])
@applianceexportjob_cli.appliance_export_job_root_group.command(name=applianceexportjob_cli.delete_appliance_export_job.name, help=applianceexportjob_cli.delete_appliance_export_job.help)
@cli_util.option('--job-id', required=True, help=u"""OCID of the Export Job""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_appliance_export_job_extended(ctx, **kwargs):
    if 'job_id' in kwargs:
        kwargs['appliance_export_job_id'] = kwargs['job_id']
        kwargs.pop('job_id')
    ctx.invoke(applianceexportjob_cli.delete_appliance_export_job, **kwargs)


@cli_util.copy_params_from_generated_command(applianceexportjob_cli.get_appliance_export_job, params_to_exclude=['appliance_export_job_id'])
@applianceexportjob_cli.appliance_export_job_root_group.command(name=applianceexportjob_cli.get_appliance_export_job.name, help=applianceexportjob_cli.get_appliance_export_job.help)
@cli_util.option('--job-id', required=True, help=u"""OCID of the Export Job""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dts', 'class': 'ApplianceExportJob'})
@cli_util.wrap_exceptions
def show_appliance_export_job_extended(ctx, **kwargs):

    if isinstance(kwargs['job_id'], six.string_types) and len(kwargs['job_id'].strip()) == 0:
        raise click.UsageError('Parameter --appliance-export-job-id cannot be whitespace or empty string')

    kwargs_request = {
        'opc_request_id': cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    }
    client = cli_util.build_client('dts', 'appliance_export_job', ctx)
    result = client.get_appliance_export_job(
        appliance_export_job_id=kwargs['job_id'],
        **kwargs_request
    )
    # Should not display the encryption passphrase
    reset_passphrase(result)
    cli_util.render_response(result, ctx)


@applianceexportjob_cli.appliance_export_job_root_group.command(name="get-passphrase", help=u"""Get the passphrase of the export job""")
@cli_util.option('--job-id', required=True, help=u"""OCID of the Export Job""")
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dts', 'class': 'ApplianceExportJob'})
@cli_util.wrap_exceptions
def get_passphrase_export_job_extended(ctx, **kwargs):

    if isinstance(kwargs['job_id'], six.string_types) and len(kwargs['job_id'].strip()) == 0:
        raise click.UsageError('Parameter --appliance-export-job-id cannot be whitespace or empty string')

    kwargs_request = {
        'opc_request_id': cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    }
    ctx.endpoint = None
    ctx.obj['endpoint'] = None
    client = cli_util.build_client('dts', 'appliance_export_job', ctx)
    result = client.get_appliance_export_job(
        appliance_export_job_id=kwargs['job_id'],
        **kwargs_request
    )
    click.echo(result.data.appliance_decryption_passphrase)


def reset_passphrase(result):
    result.data.appliance_decryption_passphrase = "********"


@cli_util.copy_params_from_generated_command(applianceexportjob_cli.update_appliance_export_job, params_to_exclude=['appliance_export_job_id', 'customer_shipping_address', 'lifecycle_state', 'lifecycle_state_details', 'expected_return_date', 'pickup_window_start_time', 'pickup_window_end_time'])
@applianceexportjob_cli.appliance_export_job_root_group.command(name=applianceexportjob_cli.update_appliance_export_job.name, help=applianceexportjob_cli.update_appliance_export_job.help)
@cli_util.option('--job-id', required=True, help=u"""OCID of the Export Job""")
@cli_util.option('--addressee', help=u"""Company or person to send the appliance to""")
@cli_util.option('--care-of', help=u"""Place/person to direct the package to.""")
@cli_util.option('--address1', help=u"""Address line 1.""")
@cli_util.option('--address2', help=u"""Optional address line 2.""")
@cli_util.option('--address3', help=u"""Optional address line 3.""")
@cli_util.option('--address4', help=u"""Optional address line 4.""")
@cli_util.option('--city-or-locality', help=u"""City or Locality.""")
@cli_util.option('--state-province-region', help=u"""State or Province or Region.""")
@cli_util.option('--country', help=u"""Country.""")
@cli_util.option('--zip-postal-code', help=u"""Zip or Postal Code""")
@cli_util.option('--phone-number', help=u"""Phone number.""")
@cli_util.option('--email', help=u"""Email address.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dts', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'dts', 'class': 'ApplianceExportJob'})
@cli_util.wrap_exceptions
def update_appliance_export_job_extended(ctx, **kwargs):
    if 'job_id' in kwargs:
        kwargs['appliance_export_job_id'] = kwargs['job_id']
        kwargs.pop('job_id')
    kwargs['customer_shipping_address'] = {}
    for option, value in customer_address_options.items():
        if option in kwargs:
            kwargs['customer_shipping_address'][value] = kwargs[option]
            kwargs.pop(option)
    ctx.invoke(applianceexportjob_cli.update_appliance_export_job, **kwargs)


@applianceexportjob_cli.appliance_export_job_root_group.command(name="generate-manifest", help=u"""Generates a manifest file for the objects that need to be exported""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment OCID where the bucket resides""")
@cli_util.option('--job-id', required=True, help=u"""OCID of the Export Job""")
@cli_util.option('--bucket', required=True, help=u"""Name of the bucket for which export is requested""")
@cli_util.option('--prefix', help=u"""The subset of objects that needs to be exported whose names starts with this Prefix""")
@cli_util.option('--start', help=u"""The subset of objects that needs to be exported starting with this object (inclusive)""")
@cli_util.option('--end', help=u"""The subset of objects that needs to be exported upto this object (inclusive)""")
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dts', 'class': 'ApplianceExportJob'})
@cli_util.wrap_exceptions
def generate_manifest_appliance_export_job_extended(ctx, **kwargs):

    if isinstance(kwargs['compartment_id'], six.string_types) and len(kwargs['compartment_id'].strip()) == 0:
        raise click.UsageError('Parameter --compartment-id cannot be whitespace or empty string')

    if isinstance(kwargs['job_id'], six.string_types) and len(kwargs['job_id'].strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    if isinstance(kwargs['bucket'], six.string_types) and len(kwargs['bucket'].strip()) == 0:
        raise click.UsageError('Parameter --bucket cannot be whitespace or empty string')

    ctx_endpoint_dts = ctx.obj['endpoint']
    ctx.obj['endpoint'] = None
    os_client = create_os_client(ctx)
    namespace = os_client.get_namespace().data

    result = os_client.get_bucket(
        namespace_name=namespace,
        bucket_name=kwargs['bucket']
    )

    if result.data.storage_tier == OBJECT_STORAGE_BUCKET_TYPE_ARCHIVE:
        raise click.UsageError('Export for Archive buckets is currently not supported')

    click.echo("Starting manifest generation on bucket {}. This may take few minutes, please wait until it is completed ...".format(kwargs['bucket']))

    iterator = CasperListIterator(os_client, namespace, kwargs['bucket'], kwargs['prefix'], kwargs['start'], kwargs['end'])
    consumer = ManifestStatsConsumer()
    uploader = ObjectUploader(os_client, namespace, kwargs['bucket'], kwargs['job_id'])
    writer = ManifestWriter(iterator, uploader, consumer)

    _start_time = time.time()
    response = writer.write()
    if response:
        click.echo('Manifest file {} uploaded to bucket {}.'.format(response.get_manifest_object_name(), kwargs['bucket']))
        _total_time = time.time() - _start_time
        click.echo("\n************************* Manifest generation completed in {:.2f} mins **************************".format(_total_time / 60))
    else:
        click.echo("\n*********************************** Manifest generation failed **************************************")

    ctx.obj['endpoint'] = ctx_endpoint_dts
    kwargs_update = {
        'appliance_export_job_id': kwargs['job_id'],
        'lifecycle_state': UpdateApplianceExportJobDetails.LIFECYCLE_STATE_CREATING,
        'lifecycle_state_details': LIFECYCLE_STATE_DETAILS_PENDING_SUBMISSION,
        'manifest_file': response.get_manifest_object_name(),
        'manifest_md5': response.get_manifest_md5(),
        'prefix': kwargs['prefix'],
        'range_start': kwargs['start'],
        'range_end': kwargs['end'],
        'total_size_in_bytes': response.get_total_size(),
        'number_of_objects': response.get_total_count(),
        'first_object': response.get_first_object(),
        'last_object': response.get_last_object(),
        'next_object': response.get_next_start_with()
    }
    ctx.invoke(applianceexportjob_cli.update_appliance_export_job, **kwargs_update)
    click.echo("\n*** Export Job updated with above manifest details.")


@applianceexportjob_cli.appliance_export_job_root_group.command(name="create-policy", help=u"""Create the IAM policy for the export job""")
@cli_util.option('--job-id', required=True, help=u"""OCID of the Export Job""")
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dts', 'class': 'ApplianceExportJob'})
@cli_util.wrap_exceptions
def create_policy_extended(ctx, **kwargs):

    # Get the export job and check if the policy language has been added by Oracle
    kwargs_show = {
        'opc_request_id': cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    }

    client = cli_util.build_client('dts', 'appliance_export_job', ctx)
    result = client.get_appliance_export_job(
        appliance_export_job_id=kwargs['job_id'],
        **kwargs_show
    )
    if len(get_bucket_access_policies(result)) <= 1:
        click.echo("Addition of policy language by Oracle in progress. Retry this command after some time or contact Oracle support")
        return

    # The policy needs to be created in the root compartment of the tenancy in the home region
    config = oci.config.from_file(file_location=ctx.obj['config_file'], profile_name=ctx.obj['profile'])
    root_compartment = config['tenancy']
    policy_name = result.data.display_name + "_Policy"
    ctx.endpoint = None
    ctx.obj['endpoint'] = None
    # Get the home region through the region-subscription list command
    identity_client = cli_util.build_client('identity', 'identity', ctx)
    subscription_kwargs = {}
    subscriptions_result = identity_client.list_region_subscriptions(
        tenancy_id=root_compartment,
        **subscription_kwargs
    )

    # There is no need to change the home region if there is only one region available in the list
    if len(subscriptions_result.data) > 1:
        for subscription in subscriptions_result.data:
            if subscription.is_home_region:
                ctx.obj['region'] = subscription.region_name
                ctx.obj['config']['region'] = subscription.region_name
                break

    # Re-create the identity client with the home region set in the ctx
    identity_client = cli_util.build_client('identity', 'identity', ctx)

    click.echo('\nSetting up the following policies in the root compartment. If the following operation fails it means '
               'that you do not have enough privileges to create policies. Re-run the below command with the correct user')
    policy_printer(policy_name, get_bucket_access_policies(result))
    iam_kwargs = {}
    iam_details = {
        'compartmentId': root_compartment,
        'name': policy_name,
        'statements': result.data.bucket_access_policies,
        'description': "The policies to allow DTS to process the export job"
    }

    create_policy_result = identity_client.create_policy(
        create_policy_details=iam_details,
        **iam_kwargs
    )
    cli_util.render_response(create_policy_result, ctx)


@applianceexportjob_cli.appliance_export_job_root_group.command(name="request-appliance", help=u"""Request an appliance for export""")
@cli_util.option('--job-id', required=True, help=u"""OCID of the Export Job""")
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dts', 'class': 'ApplianceExportJob'})
@cli_util.wrap_exceptions
def request_appliance_export_job_extended(ctx, **kwargs):
    kwargs_update = {
        'appliance_export_job_id': kwargs['job_id'],
        'lifecycle_state': UpdateApplianceExportJobDetails.LIFECYCLE_STATE_ACTIVE,
        'lifecycle_state_details': LIFECYCLE_STATE_DETAILS_PENDING_APPROVAL
    }
    ctx.invoke(applianceexportjob_cli.update_appliance_export_job, **kwargs_update)


def appliance_state_update(appliance_lifecycle_state, appliance_lifecycle_state_details, **kwargs):
    '''
    Changes the state of the appliance if not already in IN_PROCESSING
    :param appliance_lifecycle_state: str
    :param kwargs: appliance details
    :return: updated kwargs with target-state
    '''

    if appliance_lifecycle_state == UpdateApplianceExportJobDetails.LIFECYCLE_STATE_INPROGRESS:
        if appliance_lifecycle_state_details == LIFECYCLE_STATE_DETAILS_CUSTOMER_PROCESSING:
            click.echo("Appliance lifecycle_state_details is already in {}.".format(LIFECYCLE_STATE_DETAILS_CUSTOMER_PROCESSING))
            return None
        kwargs_update = {'appliance_export_job_id': kwargs['job_id']}
        if appliance_lifecycle_state_details in [LIFECYCLE_STATE_DETAILS_ORACLE_SHIPPED, LIFECYCLE_STATE_DETAILS_CUSTOMER_RECEIVED]:
            kwargs_update.update({'lifecycle_state': appliance_lifecycle_state, 'lifecycle_state_details': LIFECYCLE_STATE_DETAILS_CUSTOMER_PROCESSING})
            click.echo("Updating the state of the job from {} to {}".format(appliance_lifecycle_state_details, LIFECYCLE_STATE_DETAILS_CUSTOMER_PROCESSING))
            return kwargs_update
        else:
            raise click.ClickException("The Appliance is not in state for export. Contact Oracle Support")
    else:
        click.echo("Appliance lifecycle-state is NOT {}.".format(UpdateApplianceExportJobDetails.LIFECYCLE_STATE_INPROGRESS))
        return None


def appliance_unlock(ctx, appliance_profile, passphrase, appliance_lock_status):
    '''
    Unlocks appliance if the lockStatus is LOCKED or NA
    :param ctx:
    :param appliance_profile: str
    :param passphrase: str
    :param appliance_lock_status: <state of appliance>
    :return: None if already in Unlocked state
    '''
    if appliance_lock_status in [APPLIANCE_STATE_LOCKED, APPLIANCE_STATUS_NA]:
        click.echo("Unlocking the appliance")
        pa_unlock_helper(ctx, appliance_profile, passphrase)
    else:
        click.echo("Appliance is already in UNLOCKED status")
        return None


def appliance_encryption_check(encryptionConfigured):
    '''
    :param encryptionConfigured: bool
    :return: raises exception if the encryptionConfigured is False
    '''
    if encryptionConfigured == 'False':
        raise exceptions.ClientError("The Appliance is not configured for export. Contact Oracle Support")
    else:
        click.echo("Appliance encryption is configured")


@applianceexportjob_cli.appliance_export_job_root_group.command(name="configure-physical-appliance", help=u"""Configure the physical appliance to copy data""")
@cli_util.option('--job-id', required=True, help=u"""OCID of the Export Job""")
@cli_util.option('--appliance-cert-fingerprint', required=True, help=u"""The transfer appliance X.509/SSL certificate fingerprint.""")
@cli_util.option('--appliance-ip', required=True, help=u"""AThe IP address of the transfer appliance.""")
@cli_util.option('--appliance-port', required=False, type=click.INT, default=443, help=u"""Appliance label.""")
@cli_util.option('--appliance-profile', required=False, default="DEFAULT", help=u"""Appliance profile""")
@cli_util.option('--access-token', required=False, help=u"""the access token to authenticate with the transfer appliance.""")
@cli_util.option('--rw', required=True, type=click.BOOL, help=u"""Read/Write option on export of dataset""")
@cli_util.option('--world', required=True, type=click.BOOL, help=u"""World option on export of dataset""")
@cli_util.option('--ip', help=u"""IP address to export dataset to""")
@cli_util.option('--subnet-mask-length', type=click.INT, help=u"""Subnet mask length for the IP address""")
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dts', 'class': 'ApplianceExportJob'})
@cli_util.wrap_exceptions
def configure_physical_appliance_export_job_extended(ctx, **kwargs):
    # Should do:
    #   - oci dts update the export job to be in CUSTOMER_PROCESSING
    #   - Get the passphrase by doing a show_appliance_export_job_extended and parsing the passphrase
    #       - Use the output in the init auth and unlock appliance commands
    #   - oci dts physical-appliance initialize-authentication
    #   - oci dts physical-appliance unlock
    #   - oci dts nfs-dataset list
    #   - oci dts nfs-dataset set-export
    #   - oci dts nfs-dataset activate
    if isinstance(kwargs['job_id'], six.string_types) and len(kwargs['job_id'].strip()) == 0:
        raise click.UsageError('Parameter --appliance-export-job-id cannot be whitespace or empty string')
    client = cli_util.build_client('dts', 'appliance_export_job', ctx)

    kwargs_request = {'opc_request_id': cli_util.use_or_generate_request_id(ctx.obj['request_id'])}
    result = client.get_appliance_export_job(appliance_export_job_id=kwargs['job_id'], **kwargs_request)

    click.echo("Getting the serial number and passphrase of the appliance")
    serial_number = result.data.appliance_serial_number
    passphrase = result.data.appliance_decryption_passphrase
    appliance_profile = kwargs['appliance_profile']

    # Initialize authentication with XA
    click.echo("Initializing authentication with the appliance")
    pa_init_auth_helper(ctx, appliance_profile, kwargs['appliance_cert_fingerprint'], kwargs['appliance_ip'],
                        kwargs['appliance_port'], serial_number, kwargs['access_token'])

    # Appliance state change
    appliance_lifecycle_state = result.data.lifecycle_state
    appliance_lifecycle_state_details = result.data.lifecycle_state_details
    kwargs_update = appliance_state_update(appliance_lifecycle_state, appliance_lifecycle_state_details, **kwargs)
    if kwargs_update:
        ctx.invoke(applianceexportjob_cli.update_appliance_export_job, **kwargs_update)

    # Get appliance info
    appliance_info = pa_show_helper(ctx=ctx, appliance_profile=appliance_profile, from_json=None)
    appliance_encryption_check(appliance_info.data['encryptionConfigured'])
    appliance_unlock(ctx, appliance_profile, passphrase, appliance_info.data['lockStatus'])

    # There is only one dataset. Get the name of that dataset and use it to set exports and activate it
    nfs_dataset_client = create_nfs_dataset_client(ctx, appliance_profile)
    click.echo("Getting the NFS dataset on the appliance")

    nfs_datasets = nfs_dataset_client.list_nfs_datasets()

    if len(nfs_datasets.data) != 1:
        raise exceptions.ClientError("No/multiple datasets exist on the appliance. Contact Oracle Support")
    nfs_dataset_name = nfs_datasets.data[0]['name']
    nfs_dataset = nfs_datasets.data[0]
    # Check if the dataset is ACTIVE, if INACTIVE, do nothing
    # Deactivate the dataset before setting the exports
    deactivate_nfs_dataset(ctx, appliance_profile, **nfs_dataset)

    # Set the exports
    nfs_kwargs = {
        'rw': kwargs['rw'],
        'world': kwargs['world'],
        'ip': kwargs['ip'],
        'subnet_mask_length': kwargs['subnet_mask_length'],
        'name': nfs_dataset_name,
        'appliance_profile': appliance_profile
    }
    ctx.invoke(nfs_dataset_set_export, **nfs_kwargs)

    click.echo("Activating dataset {}".format(nfs_dataset_name))
    nfs_dataset_client.activate_nfs_dataset(nfs_dataset_name)
    click.echo("Dataset {} activated".format(nfs_dataset_name))
