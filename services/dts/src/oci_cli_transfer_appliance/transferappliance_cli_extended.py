# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci
import six
import sys

from oci_cli import cli_util
from oci_cli import custom_types
from oci_cli import json_skeleton_utils
from services.dts.src.oci_cli_dts.generated import dts_service_cli
from services.dts.src.oci_cli_transfer_appliance.generated import transferappliance_cli
from services.dts.src.oci_cli_dts.cli_utils import setup_notifications_helper


customer_address_options = {
    'addressee': 'addressee',
    'care_of': 'careOf',
    'address1': 'address1',
    'address2': 'address2',
    'address3': 'address3',
    'address4': 'address4',
    'city_or_locality': 'cityOrLocality',
    'state_province_region': 'stateOrRegion',
    'country': 'country',
    'zip_postal_code': 'zipcode',
    'phone_number': 'phoneNumber',
    'email': 'email'
}


cli_util.rename_command(dts_service_cli, dts_service_cli.dts_service_group, transferappliance_cli.transfer_appliance_root_group, 'appliance')
cli_util.rename_command(dts_service_cli, transferappliance_cli.transfer_appliance_root_group, transferappliance_cli.create_transfer_appliance, 'request')
cli_util.rename_command(dts_service_cli, transferappliance_cli.transfer_appliance_root_group, transferappliance_cli.get_transfer_appliance, 'show')
cli_util.rename_command(dts_service_cli, transferappliance_cli.transfer_appliance_root_group, transferappliance_cli.get_transfer_appliance_encryption_passphrase, 'get-passphrase')
transferappliance_cli.transfer_appliance_root_group.commands.pop(transferappliance_cli.transfer_appliance_group.name)
transferappliance_cli.transfer_appliance_root_group.commands.pop(transferappliance_cli.transfer_appliance_encryption_passphrase_group.name)
transferappliance_cli.transfer_appliance_root_group.commands.pop(transferappliance_cli.transfer_appliance_certificate_group.name)
transferappliance_cli.transfer_appliance_root_group.commands.pop(transferappliance_cli.transfer_appliance_public_key_group.name)


@cli_util.copy_params_from_generated_command(transferappliance_cli.create_transfer_appliance, params_to_exclude=['id', 'customer_shipping_address', 'wait_for_state'])
@transferappliance_cli.transfer_appliance_root_group.command(name="request", help=transferappliance_cli.create_transfer_appliance.help)
@cli_util.option('--job-id', required=True, help=u"""OCID of the Transfer Job""")
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
@cli_util.option('--setup-notifications', is_flag=True, help=u"""Setup notifications for the transfer appliance""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["REQUESTED", "ORACLE_PREPARING", "SHIPPING", "DELIVERED", "PREPARING", "FINALIZED", "RETURN_DELAYED", "RETURN_SHIPPED", "RETURN_SHIPPED_CANCELLED", "ORACLE_RECEIVED", "ORACLE_RECEIVED_CANCELLED", "PROCESSING", "COMPLETE", "CUSTOMER_NEVER_RECEIVED", "ORACLE_NEVER_RECEIVED", "CUSTOMER_LOST", "CANCELLED", "DELETED", "REJECTED", "ERROR"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler({})
@cli_util.wrap_exceptions
def create_transfer_appliance_extended(ctx, **kwargs):
    if 'job_id' in kwargs:
        kwargs['id'] = kwargs['job_id']
        kwargs.pop('job_id')
    kwargs['customer_shipping_address'] = {}
    for option, value in customer_address_options.items():
        if option in kwargs:
            kwargs['customer_shipping_address'][value] = kwargs[option]
            kwargs.pop(option)

    id = kwargs['id']
    customer_shipping_address = kwargs['customer_shipping_address']
    wait_for_state = kwargs['wait_for_state']
    max_wait_seconds = kwargs['max_wait_seconds']
    wait_interval_seconds = kwargs['wait_interval_seconds']
    setup_notifications = kwargs['setup_notifications']
    minimum_storage_capacity_in_terabytes = kwargs['minimum_storage_capacity_in_terabytes']

    # Copied from the generated file because the result of the create is required to setup notifications
    if isinstance(id, six.string_types) and len(id.strip()) == 0:
        raise click.UsageError('Parameter --id cannot be whitespace or empty string')

    kwargs = {}

    details = {}

    if customer_shipping_address is not None:
        details['customerShippingAddress'] = cli_util.parse_json_parameter("customer_shipping_address", customer_shipping_address)

    if minimum_storage_capacity_in_terabytes is not None:
        details['minimumStorageCapacityInTerabytes'] = cli_util.parse_json_parameter("minimum_storage_capacity_in_terabytes", minimum_storage_capacity_in_terabytes)

    client = cli_util.build_client('dts', 'transfer_appliance', ctx)
    result = client.create_transfer_appliance(
        id=id,
        create_transfer_appliance_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_transfer_appliance') and callable(getattr(client, 'get_transfer_appliance')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_transfer_appliance(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
        setup_import_notifications(ctx, result.data.label)


def get_transfer_appliance_helper(ctx, from_json, id, transfer_appliance_label):

    kwargs = {}
    client = cli_util.build_client('dts', 'transfer_appliance', ctx)
    result = client.get_transfer_appliance(
        id=id,
        transfer_appliance_label=transfer_appliance_label,
        **kwargs
    )
    return result


@cli_util.copy_params_from_generated_command(transferappliance_cli.get_transfer_appliance, params_to_exclude=['id', 'transfer_appliance_label'])
@transferappliance_cli.transfer_appliance_root_group.command(name=transferappliance_cli.get_transfer_appliance.name, help=transferappliance_cli.get_transfer_appliance.help)
@cli_util.option('--job-id', required=True, help=u"""OCID of the Transfer Job""")
@cli_util.option('--appliance-label', required=True, help=u"""Appliance label""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler({})
@cli_util.wrap_exceptions
def show_transfer_appliance_extended(ctx, **kwargs):
    if 'job_id' in kwargs:
        kwargs['id'] = kwargs['job_id']
        kwargs.pop('job_id')
    if 'appliance_label' in kwargs:
        kwargs['transfer_appliance_label'] = kwargs['appliance_label']
        kwargs.pop('appliance_label')
    ctx.invoke(transferappliance_cli.get_transfer_appliance, **kwargs)


@cli_util.copy_params_from_generated_command(transferappliance_cli.list_transfer_appliances, params_to_exclude=['id', 'lifecycle_state', 'all'])
@transferappliance_cli.transfer_appliance_root_group.command(
    name=transferappliance_cli.list_transfer_appliances.name,
    help=transferappliance_cli.list_transfer_appliances.help)
@cli_util.option('--job-id', required=True, help=u"""OCID of the Transfer Job""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler({})
@cli_util.wrap_exceptions
def list_transfer_appliances_extended(ctx, **kwargs):
    if 'job_id' in kwargs:
        kwargs['id'] = kwargs['job_id']
        kwargs.pop('job_id')
    ctx.invoke(transferappliance_cli.list_transfer_appliances, **kwargs)


@cli_util.copy_params_from_generated_command(transferappliance_cli.get_transfer_appliance, params_to_exclude=['id', 'transfer_appliance_label'])
@transferappliance_cli.transfer_appliance_root_group.command(name="never-receive", help="""Mark the transfer appliance NEVER RECEIVED. """)
@cli_util.option('--job-id', required=True, help=u"""OCID of the Transfer Job""")
@cli_util.option('--appliance-label', required=True, help=u"""Appliance label""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler({})
@cli_util.wrap_exceptions
def never_receive_transfer_appliance_extended(ctx, **kwargs):
    if 'job_id' in kwargs:
        kwargs['id'] = kwargs['job_id']
        kwargs.pop('job_id')
    if 'appliance_label' in kwargs:
        kwargs['transfer_appliance_label'] = kwargs['appliance_label']
        kwargs.pop('appliance_label')
    kwargs["lifecycle_state"] = "CUSTOMER_NEVER_RECEIVED"
    ctx.invoke(transferappliance_cli.update_transfer_appliance, **kwargs)


@cli_util.copy_params_from_generated_command(transferappliance_cli.get_transfer_appliance, params_to_exclude=['id', 'transfer_appliance_label'])
@transferappliance_cli.transfer_appliance_root_group.command(name="cancel", help="""Cancels the transfer appliance.""")
@cli_util.option('--job-id', required=True, help=u"""OCID of the Transfer Job""")
@cli_util.option('--appliance-label', required=True, help=u"""Appliance label""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler({})
@cli_util.wrap_exceptions
def cancel_transfer_appliance_extended(ctx, **kwargs):
    if 'job_id' in kwargs:
        kwargs['id'] = kwargs['job_id']
        kwargs.pop('job_id')
    if 'appliance_label' in kwargs:
        kwargs['transfer_appliance_label'] = kwargs['appliance_label']
        kwargs.pop('appliance_label')
    kwargs["lifecycle_state"] = "CANCELLED"
    ctx.invoke(transferappliance_cli.update_transfer_appliance, **kwargs)


@cli_util.copy_params_from_generated_command(transferappliance_cli.delete_transfer_appliance, params_to_exclude=['id', 'transfer_appliance_label'])
@transferappliance_cli.transfer_appliance_root_group.command(name=transferappliance_cli.delete_transfer_appliance.name, help=transferappliance_cli.delete_transfer_appliance.name)
@cli_util.option('--job-id', required=True, help=u"""OCID of the Transfer Job""")
@cli_util.option('--appliance-label', required=True, help=u"""Appliance label""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler({})
@cli_util.wrap_exceptions
def delete_transfer_appliance_extended(ctx, **kwargs):
    if 'job_id' in kwargs:
        kwargs['id'] = kwargs['job_id']
        kwargs.pop('job_id')
    if 'appliance_label' in kwargs:
        kwargs['transfer_appliance_label'] = kwargs['appliance_label']
        kwargs.pop('appliance_label')
    kwargs["lifecycle_state"] = "DELETED"
    ctx.invoke(transferappliance_cli.update_transfer_appliance, **kwargs)


@cli_util.copy_params_from_generated_command(transferappliance_cli.update_transfer_appliance, params_to_exclude=['id', 'customer_shipping_address', 'transfer_appliance_label', 'lifecycle_state', 'max_wait_seconds', 'wait_interval_seconds', 'wait_for_state', 'if_match', 'minimum_storage_capacity_in_terabytes', 'expected_return_date', 'pickup_window_start_time', 'pickup_window_end_time'])
@transferappliance_cli.transfer_appliance_root_group.command(name='update-shipping-address', help="""Updates the shipping address""")
@cli_util.option('--job-id', required=True, help=u"""OCID of the Transfer Job""")
@cli_util.option('--appliance-label', required=True, help=u"""Appliance label""")
@cli_util.option('--addressee', required=True, help=u"""Company or person to send the appliance to""")
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
@json_skeleton_utils.json_skeleton_generation_handler({})
@cli_util.wrap_exceptions
def update_shipping_address_transfer_appliance(ctx, **kwargs):
    if 'job_id' in kwargs:
        kwargs['id'] = kwargs['job_id']
        kwargs.pop('job_id')
    if 'appliance_label' in kwargs:
        kwargs['transfer_appliance_label'] = kwargs['appliance_label']
        kwargs.pop('appliance_label')
    kwargs['customer_shipping_address'] = {}
    for option, value in customer_address_options.items():
        if option in kwargs:
            kwargs['customer_shipping_address'][value] = kwargs[option]
            kwargs.pop(option)
    ctx.invoke(transferappliance_cli.update_transfer_appliance, **kwargs)


@cli_util.copy_params_from_generated_command(transferappliance_cli.get_transfer_appliance_encryption_passphrase, params_to_exclude=['id', 'transfer_appliance_label'])
@transferappliance_cli.transfer_appliance_root_group.command(name=transferappliance_cli.get_transfer_appliance_encryption_passphrase.name, help="""Gets the transfer appliance encryption passphrase.""")
@cli_util.option('--job-id', required=True, help=u"""OCID of the Transfer Job""")
@cli_util.option('--appliance-label', required=True, help=u"""Appliance label""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler({})
@cli_util.wrap_exceptions
def get_passphrase_extended(ctx, **kwargs):
    if 'job_id' in kwargs:
        kwargs['id'] = kwargs['job_id']
        kwargs.pop('job_id')
    if 'appliance_label' in kwargs:
        kwargs['transfer_appliance_label'] = kwargs['appliance_label']
        kwargs.pop('appliance_label')
    ctx.invoke(transferappliance_cli.get_transfer_appliance_encryption_passphrase, **kwargs)


@transferappliance_cli.transfer_appliance_root_group.command(name='setup-notifications', help=u"""Setup notifications for appliance import""")
@cli_util.option('--appliance-label', required=True, help=u"""Appliance Label""")
@click.pass_context
@cli_util.help_option
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={},
                                                      output_type={'module': 'dts', 'class': 'TransferAppliance'})
@cli_util.wrap_exceptions
def setup_import_notifications_for_appliance_extended(ctx, appliance_label):
    setup_import_notifications(ctx, appliance_label)


def setup_import_notifications(ctx, appliance_label):
    # Create the topic, subscriptions and rule in the root compartment so that everything trickles down
    config = oci.config.from_file(file_location=ctx.obj['config_file'], profile_name=ctx.obj['profile'])
    root_compartment = config['tenancy']

    create_topic_details = {
        'name': 'DTSImportApplianceTopic_{}'.format(appliance_label),
        'description': 'Topic for data transfer service appliance import with label {}'.format(appliance_label),
        'compartmentId': root_compartment
    }
    create_rule_kwargs = {
        'display_name': 'DTSImportApplianceRule_{}'.format(appliance_label),
        'compartment_id': root_compartment,
        'description': 'Rule for data transfer service to send notifications for a transfer appliance with label {}'.format(appliance_label),
        'is_enabled': True,
        'condition': '{"eventType":"com.oraclecloud.datatransferservice.*transferappliance","data":{"additionalDetails":{"applianceLabel":"%s"}}}' % appliance_label,
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


@cli_util.copy_params_from_generated_command(transferappliance_cli.get_transfer_appliance, params_to_exclude=['id', 'transfer_appliance_label'])
@transferappliance_cli.transfer_appliance_root_group.command(name="update-minimum-storage-capacity", help="""Updates the minimum storage capacity""")
@cli_util.option('--job-id', required=True, help=u"""OCID of the Transfer Job""")
@cli_util.option('--appliance-label', required=True, help=u"""Appliance label""")
@cli_util.option('--minimum-storage-capacity-in-terabytes', required=True, type=click.INT, help=u"""Minimum storage capacity of the device, in terabytes. Valid options are 50, 95 and 150.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler({})
@cli_util.wrap_exceptions
def update_minimum_storage_capacity_transfer_appliance(ctx, **kwargs):
    if 'job_id' in kwargs:
        kwargs['id'] = kwargs['job_id']
        kwargs.pop('job_id')
    if 'appliance_label' in kwargs:
        kwargs['transfer_appliance_label'] = kwargs['appliance_label']
        kwargs.pop('appliance_label')
    ctx.invoke(transferappliance_cli.update_transfer_appliance, **kwargs)
