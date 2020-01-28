# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click

from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from services.dts.src.oci_cli_dts.generated import dts_service_cli
from services.dts.src.oci_cli_transfer_appliance.generated import transferappliance_cli


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


@cli_util.copy_params_from_generated_command(transferappliance_cli.create_transfer_appliance, params_to_exclude=['id', 'wait_for_state', 'max_wait_seconds', 'wait_interval_seconds', 'customer_shipping_address'])
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
    ctx.invoke(transferappliance_cli.create_transfer_appliance, **kwargs)


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


@cli_util.copy_params_from_generated_command(transferappliance_cli.update_transfer_appliance, params_to_exclude=['id', 'customer_shipping_address', 'transfer_appliance_label', 'lifecycle_state', 'max_wait_seconds', 'wait_interval_seconds', 'wait_for_state', 'if_match'])
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
