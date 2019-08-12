# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click

from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types
from services.dts.src.oci_cli_transfer_appliance.generated import transferappliance_cli


@cli_util.copy_params_from_generated_command(transferappliance_cli.create_transfer_appliance, params_to_exclude=['id', 'wait_for_state', 'max_wait_seconds', 'wait_interval_seconds', 'customer_shipping_address'])
@transferappliance_cli.transfer_appliance_root_group.command(name=transferappliance_cli.create_transfer_appliance.name, help=transferappliance_cli.create_transfer_appliance.help)
@cli_util.option('--job-id', required=True, help=u"""OCID of the Transfer Job""")
@cli_util.option('--customer-shipping-address', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'customer-shipping-address': {'module': 'dts', 'class': 'ShippingAddress'}})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'customer-shipping-address': {'module': 'dts', 'class': 'ShippingAddress'}}, output_type={'module': 'dts', 'class': 'TransferAppliance'})
@cli_util.wrap_exceptions
def create_transfer_appliance_extended(ctx, **kwargs):
    if 'job_id' in kwargs:
        kwargs['id'] = kwargs['job_id']
        kwargs.pop('job_id')
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
@cli_util.option('--customer-shipping-address', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'customer-shipping-address': {'module': 'dts', 'class': 'ShippingAddress'}})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'customer-shipping-address': {'module': 'dts', 'class': 'ShippingAddress'}}, output_type={'module': 'dts', 'class': 'TransferAppliance'})
@cli_util.wrap_exceptions
def update_shipping_address_transfer_appliance(ctx, **kwargs):
    if 'job_id' in kwargs:
        kwargs['id'] = kwargs['job_id']
        kwargs.pop('job_id')
    if 'appliance_label' in kwargs:
        kwargs['transfer_appliance_label'] = kwargs['appliance_label']
        kwargs.pop('appliance_label')
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
