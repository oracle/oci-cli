# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function

import click
import configparser
from enum import Enum
import os
import sys

from oci import exceptions
from oci import config as oci_config
from oci.dts.models.transfer_appliance import TransferAppliance

from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli.aliasing import CommandGroupWithAlias
from oci_cli.formatting import render_config_errors

from services.dts.src.oci_cli_dts.appliance_init_auth_spec import InitAuthSpec
from services.dts.src.oci_cli_dts.cli_utils import error_message_wrapper

from services.dts.src.oci_cli_dts.generated import dts_service_cli
from services.dts.src.oci_cli_dts.appliance_init_auth import InitAuth
from services.dts.src.oci_cli_dts.appliance_client_proxy import ApplianceClientProxy
from services.dts.src.oci_cli_dts.physical_appliance_control_plane.client.models.physical_transfer_appliance import \
    PhysicalTransferAppliance

from services.dts.src.oci_cli_dts.appliance_config_manager import ApplianceConfigManager
from services.dts.src.oci_cli_dts.appliance_constants import APPLIANCE_CONFIGS_BASE_DIR, ENDPOINT, APPLIANCE_PROFILE, \
    KEY_FILE_KEY, APPLIANCE_UPLOAD_USER_CONFIG_PATH, TEST_OBJECT, DEFAULT_PROFILE, CONFIG_DIR


"""
physical-appliance command
This is a local command set and not generated from spec, but created here.
These commands accesses the locally attached physical appliances.
"""


@click.command('physical-appliance', cls=CommandGroupWithAlias, help="""Physical Appliance Operations""")
@cli_util.help_option_group
def physical_appliance_group():
    pass


dts_service_cli.dts_service_group.add_command(physical_appliance_group)


@physical_appliance_group.command('initialize-authentication',
                                  help=u"""Initializes authentication between the Data Transfer Utility
                                  and the transfer appliance.""")
@cli_util.option('--job-id', required=False, help=u"""Transfer job ocid.""")
@cli_util.option('--appliance-label', required=False, help=u"""Appliance label.""")
@cli_util.option('--export-job-id', required=False, help=u"""Export job ocid.""")
@cli_util.option('--appliance-cert-fingerprint', required=True,
                 help=u"""The transfer appliance X.509/SSL certificate fingerprint.""")
@cli_util.option('--appliance-ip', required=True, help=u"""AThe IP address of the transfer appliance.""")
@cli_util.option('--appliance-port', required=False, type=click.INT, default=443, help=u"""Appliance label.""")
@cli_util.option('--profile', required=False, default="DEFAULT", help=u"""profile""")
@cli_util.option('--appliance-profile', required=False, default="DEFAULT", help=u"""Appliance profile""")
@cli_util.option('--access-token', required=False,
                 help=u"""the access token to authenticate with the transfer appliance.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={},
                                                      output_type={'module': 'dts', 'class': 'PhysicalAppliance'})
@cli_util.wrap_exceptions
def pa_initialize_authentication(ctx, from_json, job_id, appliance_label, export_job_id, appliance_cert_fingerprint,
                                 appliance_ip, appliance_port, access_token, profile, appliance_profile):

    kwargs = {}

    if job_id is not None and appliance_label is not None:
        if export_job_id is not None:
            raise click.UsageError('Either use --export-job-id or a combination of --job-id and --appliance-label')

        click.echo("Retrieving the Import Appliance Serial No. from OCI... ", nl=False)
        # Get the Transfer Appliance serial number from the control plane
        client = cli_util.build_client('dts', 'transfer_appliance', ctx)
        result = client.get_transfer_appliance(
            id=job_id,
            transfer_appliance_label=appliance_label,
            **kwargs
        )
        serial_number = result.data.serial_number
        click.echo("done")

    elif export_job_id is not None:
        if job_id is not None and appliance_label is not None:
            raise click.UsageError('Either use --export-job-id or a combination of --job-id and --appliance-label')

        click.echo("Retrieving the Export Appliance Serial No. from OCI... ", nl=False)
        client = cli_util.build_client('dts', 'appliance_export_job', ctx)
        kwargs_request = {'opc_request_id': cli_util.use_or_generate_request_id(ctx.obj['request_id'])}
        result = client.get_appliance_export_job(appliance_export_job_id=export_job_id, **kwargs_request)
        serial_number = result.data.appliance_serial_number
        click.echo("done")

    else:
        raise click.UsageError('Either use --export-job-id or a combination of --job-id and --appliance-label')

    pa_init_auth_helper(ctx, appliance_profile, appliance_cert_fingerprint, appliance_ip, appliance_port,
                        serial_number, access_token)

    if job_id is not None and appliance_label is not None:
        click.echo("Next action(s): Configuring Import Appliance Encryption")
        click.echo(" 1. oci dts physical-appliance show")
        click.echo(" 2. oci dts physical-appliance configure-encryption "
                   "--job-id {} --appliance-label {}".format(job_id, appliance_label))


def pa_init_auth_helper(ctx, appliance_profile, appliance_cert_fingerprint, appliance_ip, appliance_port,
                        serial_number, access_token):
    auth_spec = InitAuthSpec(cert_fingerprint=appliance_cert_fingerprint, appliance_ip=appliance_ip,
                             appliance_port=appliance_port, appliance_profile=appliance_profile,
                             serial_id=serial_number, access_token=access_token)

    init_auth = create_init_auth(auth_spec)
    init_auth.run()

    # The initialize-authentication shows the transfer appliance details the same as oci dts physical-appliance show
    appliance_client = create_appliance_client(ctx, appliance_profile)
    user_friendly_appliance_info = convert_to_user_friendly(appliance_client.get_physical_transfer_appliance())
    cli_util.render_response(user_friendly_appliance_info, ctx)


def create_init_auth(auth_spec):
    return InitAuth(auth_spec)


@physical_appliance_group.command('list', help=u"""Lists all appliances registered via initialize authentication.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={},
                                                      output_type={'module': 'dts', 'class': 'PhysicalAppliance'})
@cli_util.wrap_exceptions
def pa_list(ctx, from_json):
    result = []
    config_manager = ApplianceConfigManager(APPLIANCE_CONFIGS_BASE_DIR)
    for profile_name, config in config_manager.list_configs().items():
        result.append({
            ENDPOINT: config.get_appliance_url(),
            APPLIANCE_PROFILE: profile_name
        })
    cli_util.render(result, None, ctx)


@physical_appliance_group.command('unregister',
                                  help=u"""Unregister appliance registered via initialize authentication.""")
@cli_util.option('--appliance-profile', default="DEFAULT", required=False, help=u"""Appliance Profile""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def pa_unregister(ctx, from_json, appliance_profile):
    config_manager = ApplianceConfigManager(APPLIANCE_CONFIGS_BASE_DIR)
    config = config_manager.get_config(appliance_profile)
    if not click.confirm("Is it OK to unregister appliance with endpoint {}".format(config.get_appliance_url())):
        click.echo("Exiting...")
        sys.exit(-1)
    else:
        config_manager.delete_config(appliance_profile)
    click.echo("Unregistered the appliance")


@physical_appliance_group.command('configure-encryption',
                                  help=u"""Configures encryption on the transfer appliance.""")
@cli_util.option('--appliance-profile', required=False, default="DEFAULT", help=u"""Appliance Profile""")
@cli_util.option('--job-id', required=True, help=u"""Transfer job OCID.""")
@cli_util.option('--appliance-label', required=True, help=u"""Appliance label.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def pa_configure_encryption(ctx, from_json, appliance_profile, job_id, appliance_label):
    client = cli_util.build_client('dts', 'transfer_appliance', ctx)
    result = client.get_transfer_appliance(
        id=job_id,
        transfer_appliance_label=appliance_label
    )
    # If the appliance is not already in a preparing state, move it to a preparing state
    if result.data.lifecycle_state != TransferAppliance.LIFECYCLE_STATE_PREPARING:
        click.echo("Updating the state of the Appliance in OCI to PREPARING... ", nl=False)
        details = {
            "lifecycleState": TransferAppliance.LIFECYCLE_STATE_PREPARING
        }
        client.update_transfer_appliance(
            id=job_id,
            transfer_appliance_label=appliance_label,
            update_transfer_appliance_details=details,
        )
        click.echo("done")

    click.echo("Retrieving the Passphrase from OCI... ", nl=False)
    passphrase = client.get_transfer_appliance_encryption_passphrase(
        id=job_id,
        transfer_appliance_label=appliance_label
    ).data.encryption_passphrase
    appliance_client = create_appliance_client(ctx, appliance_profile)
    click.echo("done")

    click.echo("Configuring Appliance Encryption... ", nl=False)
    appliance_client.configure_encryption(passphrase_details={'passphrase': passphrase})
    click.echo("done")

    click.echo("Getting Appliance Info... ", nl=False)
    appliance_info = appliance_client.get_physical_transfer_appliance()
    click.echo("done")

    user_friendly_appliance_info = convert_to_user_friendly(appliance_info)
    cli_util.render_response(user_friendly_appliance_info, ctx)
    click.echo("Next action(s): Unlocking the Import Appliance")
    click.echo(" 1. oci dts physical-appliance unlock --job-id {} --appliance-label {}".format(job_id, appliance_label))


def create_appliance_client(ctx, appliance_profile):
    return ApplianceClientProxy(ctx, appliance_profile)


@physical_appliance_group.command('unlock',
                                  help=u"""Unlocks the transfer appliance.""")
@cli_util.option('--appliance-profile', required=False, default="DEFAULT", help=u"""Appliance Profile""")
@cli_util.option('--job-id', required=False, help=u"""Transfer job OCID.""")
@cli_util.option('--appliance-label', required=False, help=u"""Appliance label.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def pa_unlock(ctx, from_json, appliance_profile, job_id, appliance_label):
    if job_id is None or appliance_label is None:
        click.echo("Specify the --job-id and the --appliance-label to retrieve the passphrase from Oracle Cloud"
                   "Infrastructure or enter the passphrase")
        passphrase = click.prompt('Passphrase', hide_input=True)
        if passphrase is None:
            click.echo('No input provided. Exiting...')
            sys.exit(-1)
    else:
        click.echo("Retrieving the Passphrase from OCI... ", nl=False)
        client = cli_util.build_client('dts', 'transfer_appliance', ctx)
        passphrase = client.get_transfer_appliance_encryption_passphrase(
            id=job_id,
            transfer_appliance_label=appliance_label
        ).data.encryption_passphrase
        click.echo("done")
    pa_unlock_helper(ctx, appliance_profile, passphrase)
    click.echo("Next action(s): Creating NFS Datasets")
    click.echo(" 1. oci dts nfs-dataset create --name <dataset_name> --rw true --world true --ip <ip_address> "
               "--subnet-mask-length <subnet-mask>")


def pa_unlock_helper(ctx, appliance_profile, passphrase):
    click.echo("Unlocking Appliance... ", nl=False)
    appliance_client = create_appliance_client(ctx, appliance_profile)
    appliance_client.unlock_appliance(details={'passphrase': passphrase})
    click.echo("done")

    appliance_info = appliance_client.get_physical_transfer_appliance()
    user_friendly_appliance_info = convert_to_user_friendly(appliance_info)
    cli_util.render_response(user_friendly_appliance_info, ctx)


@physical_appliance_group.command('show', help=u"""Shows transfer appliance details.""")
@cli_util.option('--appliance-profile', required=False, default="DEFAULT", help=u"""Appliance Profile""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def pa_show(ctx, from_json, appliance_profile):
    appliance_client = create_appliance_client(ctx, appliance_profile)
    appliance_info = appliance_client.get_physical_transfer_appliance()
    user_friendly_appliance_info = convert_to_user_friendly(appliance_info)
    cli_util.render_response(user_friendly_appliance_info, ctx)


def pa_show_helper(ctx, from_json, appliance_profile):
    appliance_client = create_appliance_client(ctx, appliance_profile)
    appliance_info = appliance_client.get_physical_transfer_appliance()
    user_friendly_appliance_info = convert_to_user_friendly(appliance_info)
    return user_friendly_appliance_info


@physical_appliance_group.command('finalize', help=u"""Finalizes the appliance.""")
@cli_util.option('--appliance-profile', required=False, default="DEFAULT", help=u"""Appliance Profile""")
@cli_util.option('--job-id', required=True, help=u"""Transfer job OCID.""")
@cli_util.option('--appliance-label', required=True, help=u"""Appliance label.""")
@cli_util.option('--skip-upload-user-check', required=False, is_flag=True,
                 help=u"""Skip checking whether the upload user has the right credentials""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def pa_finalize(ctx, from_json, appliance_profile, job_id, appliance_label, skip_upload_user_check):
    click.echo("Retrieving the Upload Summary Object Name from OCI... ", nl=False)
    appliance_client = cli_util.build_client('dts', 'transfer_appliance', ctx)
    physical_appliance_client = create_appliance_client(ctx, appliance_profile)

    upload_summary_obj_name = appliance_client.get_transfer_appliance(
        id=job_id,
        transfer_appliance_label=appliance_label
    ).data.upload_status_log_uri
    click.echo("done")

    click.echo("Retrieving the Upload Bucket Name from OCI... ", nl=False)
    client = cli_util.build_client('dts', 'transfer_job', ctx)
    upload_bucket = client.get_transfer_job(id=job_id).data.upload_bucket_name
    upload_user_config = oci_config.from_file(APPLIANCE_UPLOAD_USER_CONFIG_PATH)
    click.echo("done")

    if not skip_upload_user_check:
        click.echo("Validating the Upload User Credentials...")
        validate_upload_user_credentials(ctx, upload_bucket, upload_user_config)

    click.echo("Storing the Upload User Configuration and Credentials on the Appliance... ", nl=False)
    upload_user_key_file = open(os.path.expanduser(upload_user_config[KEY_FILE_KEY])).read()
    upload_config = {
        'uploadBucket': upload_bucket,
        'overwrite': False,
        'objectNamePrefix': "",
        'uploadSummaryObjectName': upload_summary_obj_name,
        'uploadUserOciConfig': open(APPLIANCE_UPLOAD_USER_CONFIG_PATH).read(),
        'uploadUserPrivateKeyPem': upload_user_key_file
    }
    physical_appliance_client.set_object_storage_upload_config(upload_config=upload_config)
    click.echo("done")

    click.echo("Finalizing the Appliance... ", nl=False)
    physical_appliance_client.finalize_appliance()
    appliance_info = physical_appliance_client.get_physical_transfer_appliance()
    click.echo("done")

    click.echo("The Appliance is locked after finalize. Hence the finalize status will be shown as NA. "
               "Please unlock the Appliance again to see the correct finalize status")

    click.echo("Updating the State of the Appliance in OCI to FINALIZED... ", nl=False)
    current_state = appliance_client.get_transfer_appliance(
        id=job_id,
        transfer_appliance_label=appliance_label
    ).data.lifecycle_state
    if current_state != TransferAppliance.LIFECYCLE_STATE_FINALIZED:
        details = {
            "lifecycleState": TransferAppliance.LIFECYCLE_STATE_FINALIZED
        }
        appliance_client.update_transfer_appliance(
            id=job_id,
            transfer_appliance_label=appliance_label,
            update_transfer_appliance_details=details)
    click.echo("done")

    user_friendly_appliance_info = convert_to_user_friendly(appliance_info)
    cli_util.render_response(user_friendly_appliance_info, ctx)
    click.echo("Next action(s): Shipping the Import Appliance")
    click.echo(" 1. - Shut Down the Import Appliance -")
    click.echo(" 2. - Packing and Shipping the Import Appliance to Oracle -")


def get_upload_user_region():
    try:
        config = configparser.ConfigParser()
        config.read(APPLIANCE_UPLOAD_USER_CONFIG_PATH)
        return config.get(DEFAULT_PROFILE, 'region')
    except exceptions.ConfigFileNotFound as e:
        error_message_wrapper('Unable to parse the upload user config file %s: %s' % (APPLIANCE_UPLOAD_USER_CONFIG_PATH, e))


def get_upload_user_config():
    try:
        upload_user_config = oci_config.from_file(file_location=APPLIANCE_UPLOAD_USER_CONFIG_PATH,
                                                  profile_name="DEFAULT")
        return upload_user_config

    except exceptions.ConfigFileNotFound as e:
        error_message_wrapper('Unable to parse the upload user config file %s: %s' % (APPLIANCE_UPLOAD_USER_CONFIG_PATH, e))


def get_user(ctx):
    if 'user' in ctx.obj['config']:
        return ctx.obj['config']['user']
    return oci_config.from_file(ctx.obj['config_file'])['user']


def create_obj_storage_client(ctx):
    return cli_util.build_client('object_storage', 'object_storage', ctx)


def validate_upload_user_credentials(ctx, upload_bucket, upload_user_config=None):
    """
    There are two users, the admin user and the upload user
    The admin user is the one who has access to the user's tenancy and can perform operations like creating a job,
    requesting an appliance, etc.
    The upload user has enough permissions to just upload data to a particular user bucket. The upload user cannot
    delete objects from the bucket nor can it make modifications to the bucket or account. In essence it is a
    restricted user.
    The upload user is defined in ~/.oci/config_upload_user under the [DEFAULT] section. There is no way to change
    the file and the section. These are standards that are expected
    The idea of validation is to check whether the upload user has the ability to create objects, inspect the object
    and read the object's meta data from Oracle Cloud Infrastructure
    The procedure is this:
    1. Admin user tries to get the test object and delete it if it is present.
      - This is more of an error check when there is a stale object present from a previous failed run
      - Only the admin user, NOT the upload user, can delete an object
    2. Upload user creates the test object
    3. Upload user overwrites the test object
    4. Upload user gets the checksum of the test object
    5. Upload user gets the metadata of the test bucket
    6. Admin user deletes the test object
    :param upload_bucket: The bucket to upload to
    :param upload_user_config: config built from APPLIANCE_UPLOAD_USER_CONFIG_PATH
    :return: None
    """
    # Overriding any endpoint that was set. Need to get to the endpoint based on the config file, not based on the
    # override parameter
    ctx.endpoint = None
    ctx.obj['endpoint'] = None
    # To support cross region uploads. get the region from the Upload User file
    # For example, let's say the config file had us-phoenix-1 as the region and config_upload_user had us-ashburn-1
    # If the region is not changed in the context, the admin client would be talking to us-phoenix-1 whereas the
    # upload client would be talking to us-ashburn-1. That's not what we want.
    try:
        if not upload_user_config:
            upload_user_config = get_upload_user_config()
        oci_config.validate_config(upload_user_config)

    except exceptions.ProfileNotFound as e:
        error_message_wrapper('ProfileNotFound: Unable to parse the upload user config file %s: %s' % (APPLIANCE_UPLOAD_USER_CONFIG_PATH, e))

    except exceptions.InvalidConfig as bad_config:
        table = render_config_errors(bad_config)
        template = "InvalidConfig: The config file at {config_file} is invalid:\n\n{errors}"
        error_message_wrapper(template.format(
            config_file=APPLIANCE_UPLOAD_USER_CONFIG_PATH,
            errors=table
        ))

    admin_user = get_user(ctx)

    region = get_upload_user_region()

    if 'config' in ctx.obj:  # config loaded/present
        if 'region' in ctx.obj['config'] and ctx.obj['config']['region']:  # region present in ~/.oci/config
            if region:  # region present in APPLIANCE_UPLOAD_USER_CONFIG_PATH
                if ctx.obj['config']['region'].strip() != region.strip():
                    confirm_prompt = "WARNING: The config file under {config_path}/config: '{config_region}' has different region than "\
                                     "{upload_user_path}: '{upload_user_region}'. Are you sure you want to continue with "  \
                                     "'{upload_user_region}'?".format(config_path=CONFIG_DIR,
                                                                      upload_user_path=APPLIANCE_UPLOAD_USER_CONFIG_PATH,
                                                                      config_region=ctx.obj['config']['region'], upload_user_region=region)
                    if not click.confirm(click.style(confirm_prompt, fg="yellow")):
                        error_message_wrapper("Aborted. Exiting...")

                ctx.obj['region'] = region
                ctx.obj['config']['region'] = region
                object_storage_admin_client = create_obj_storage_client(ctx)
                # A bit hacky but gets the job done. Only two parameters need to be changed to get the upload user context,
                # the profile and the config file. All other parameters remain the same
                upload_user_ctx = ctx
                upload_user_ctx.obj['profile'] = 'DEFAULT'
                upload_user_ctx.obj['config_file'] = APPLIANCE_UPLOAD_USER_CONFIG_PATH
                # Overriding any endpoint that was set. Need to get to the endpoint based on the config_upload_user file
                upload_user_ctx.endpoint = None
                object_storage_upload_client = create_obj_storage_client(upload_user_ctx)
                namespace = object_storage_admin_client.get_namespace().data
                try:
                    try:
                        object_storage_admin_client.head_object(namespace, upload_bucket, TEST_OBJECT)
                        click.echo("Found test object in bucket. Deleting  it...")
                        object_storage_admin_client.delete_object(namespace, upload_bucket, TEST_OBJECT)
                    except exceptions.ServiceError as se:
                        if se.status != 404:
                            raise se
                except Exception as e:
                    raise exceptions.RequestException(
                        "Admin user {} failed to delete the test object {}: {}".format(admin_user, TEST_OBJECT, str(e)))

                test_object_content = "Bulk Data Transfer Test"

                operation = None
                test_object_exists = False
                try:
                    operation = "Create object {} in bucket {} using upload user".format(TEST_OBJECT, upload_bucket)
                    object_storage_upload_client.put_object(namespace, upload_bucket, TEST_OBJECT, test_object_content)
                    click.echo(operation)
                    test_object_exists = True

                    operation = "Overwrite object {} in bucket {} using upload user".format(TEST_OBJECT, upload_bucket)
                    object_storage_upload_client.put_object(namespace, upload_bucket, TEST_OBJECT, test_object_content)
                    click.echo(operation)

                    operation = "Inspect object {} in bucket {} using upload user".format(TEST_OBJECT, upload_bucket)
                    object_storage_upload_client.head_object(namespace, upload_bucket, TEST_OBJECT)
                    click.echo(operation)

                    operation = "Read bucket metadata {} using upload user".format(upload_bucket)
                    metadata = object_storage_upload_client.get_bucket(namespace, upload_bucket).data.metadata
                    click.echo(operation)
                except exceptions.ServiceError as se:
                    raise exceptions.RequestException(
                        "Failed to {} in tenancy {} as upload user: {}".format(operation, namespace, se.message))
                finally:
                    if test_object_exists:
                        try:
                            object_storage_admin_client.delete_object(namespace, upload_bucket, TEST_OBJECT)
                        except exceptions.ServiceError as se:
                            raise exceptions.ServiceError(
                                "Failed to delete test object {} as admin user {}: {}".format(TEST_OBJECT, admin_user, se.message))
            else:
                error_message_wrapper('Unable to parse the upload user config file. Region not found in %s' %
                                      APPLIANCE_UPLOAD_USER_CONFIG_PATH)
        else:
            error_message_wrapper('Unable to parse the config file. Region not found in %s/config' % CONFIG_DIR)
    else:
        error_message_wrapper('Unable to parse the config file at %s/config' % CONFIG_DIR)


def convert_to_user_friendly(appliance_info):
    if appliance_info.data['lockStatus'] == PhysicalTransferAppliance.LOCK_STATUS_NOT_LOCKED:
        appliance_info.data['availableSpaceInBytes'] = get_user_friendly_size(
            appliance_info.data['availableSpaceInBytes'])
        appliance_info.data['totalSpaceInBytes'] = get_user_friendly_size(appliance_info.data['totalSpaceInBytes'])
    else:
        appliance_info.data['availableSpaceInBytes'] = "Unknown"
        appliance_info.data['totalSpaceInBytes'] = "Unknown"
    return appliance_info


class SpaceUnit(Enum):
    KB = 1024
    MB = 1024 * 1024
    GB = 1024 * 1024 * 1024
    TB = 1024 * 1024 * 1024 * 1024


def get_unit(size_in_bytes):
    if SpaceUnit.TB.value < size_in_bytes:
        return SpaceUnit.TB
    elif SpaceUnit.GB.value < size_in_bytes:
        return SpaceUnit.GB
    elif SpaceUnit.MB.value < size_in_bytes:
        return SpaceUnit.MB
    return SpaceUnit.KB


def get_user_friendly_size(size_in_bytes):
    unit = get_unit(size_in_bytes)
    value = "%.2f" % float(int(size_in_bytes) / unit.value)
    return value + unit.name
