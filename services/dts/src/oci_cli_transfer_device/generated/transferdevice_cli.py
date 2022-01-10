# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
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
from services.dts.src.oci_cli_dts.generated import dts_service_cli


@click.command(cli_util.override('transfer_device.transfer_device_root_group.command_name', 'transfer-device'), cls=CommandGroupWithAlias, help=cli_util.override('transfer_device.transfer_device_root_group.help', """Data Transfer Service API Specification"""), short_help=cli_util.override('transfer_device.transfer_device_root_group.short_help', """Data Transfer Service API"""))
@cli_util.help_option_group
def transfer_device_root_group():
    pass


@click.command(cli_util.override('transfer_device.transfer_device_group.command_name', 'transfer-device'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def transfer_device_group():
    pass


dts_service_cli.dts_service_group.add_command(transfer_device_root_group)
transfer_device_root_group.add_command(transfer_device_group)


@transfer_device_group.command(name=cli_util.override('transfer_device.create_transfer_device.command_name', 'create'), help=u"""Create a new Transfer Device \n[Command Reference](createTransferDevice)""")
@cli_util.option('--id', required=True, help=u"""ID of the Transfer Job""")
@cli_util.option('--serial-number', help=u"""""")
@cli_util.option('--iscsi-iqn', help=u"""""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dts', 'class': 'NewTransferDevice'})
@cli_util.wrap_exceptions
def create_transfer_device(ctx, from_json, id, serial_number, iscsi_iqn):

    if isinstance(id, six.string_types) and len(id.strip()) == 0:
        raise click.UsageError('Parameter --id cannot be whitespace or empty string')

    kwargs = {}

    _details = {}

    if serial_number is not None:
        _details['serialNumber'] = serial_number

    if iscsi_iqn is not None:
        _details['iscsiIQN'] = iscsi_iqn

    client = cli_util.build_client('dts', 'transfer_device', ctx)
    result = client.create_transfer_device(
        id=id,
        create_transfer_device_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@transfer_device_group.command(name=cli_util.override('transfer_device.delete_transfer_device.command_name', 'delete'), help=u"""deletes a transfer Device \n[Command Reference](deleteTransferDevice)""")
@cli_util.option('--id', required=True, help=u"""ID of the Transfer Job""")
@cli_util.option('--transfer-device-label', required=True, help=u"""Label of the Transfer Device""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_transfer_device(ctx, from_json, id, transfer_device_label):

    if isinstance(id, six.string_types) and len(id.strip()) == 0:
        raise click.UsageError('Parameter --id cannot be whitespace or empty string')

    if isinstance(transfer_device_label, six.string_types) and len(transfer_device_label.strip()) == 0:
        raise click.UsageError('Parameter --transfer-device-label cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('dts', 'transfer_device', ctx)
    result = client.delete_transfer_device(
        id=id,
        transfer_device_label=transfer_device_label,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@transfer_device_group.command(name=cli_util.override('transfer_device.get_transfer_device.command_name', 'get'), help=u"""Describes a transfer package in detail \n[Command Reference](getTransferDevice)""")
@cli_util.option('--id', required=True, help=u"""ID of the Transfer Job""")
@cli_util.option('--transfer-device-label', required=True, help=u"""Label of the Transfer Device""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dts', 'class': 'TransferDevice'})
@cli_util.wrap_exceptions
def get_transfer_device(ctx, from_json, id, transfer_device_label):

    if isinstance(id, six.string_types) and len(id.strip()) == 0:
        raise click.UsageError('Parameter --id cannot be whitespace or empty string')

    if isinstance(transfer_device_label, six.string_types) and len(transfer_device_label.strip()) == 0:
        raise click.UsageError('Parameter --transfer-device-label cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('dts', 'transfer_device', ctx)
    result = client.get_transfer_device(
        id=id,
        transfer_device_label=transfer_device_label,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@transfer_device_group.command(name=cli_util.override('transfer_device.list_transfer_devices.command_name', 'list'), help=u"""Lists Transfer Devices associated with a transferJob \n[Command Reference](listTransferDevices)""")
@cli_util.option('--id', required=True, help=u"""ID of the Transfer Job""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PREPARING", "READY", "PACKAGED", "ACTIVE", "PROCESSING", "COMPLETE", "MISSING", "ERROR", "DELETED", "CANCELLED"]), help=u"""filtering by lifecycleState""")
@cli_util.option('--display-name', help=u"""filtering by displayName""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dts', 'class': 'MultipleTransferDevices'})
@cli_util.wrap_exceptions
def list_transfer_devices(ctx, from_json, all_pages, id, lifecycle_state, display_name):

    if isinstance(id, six.string_types) and len(id.strip()) == 0:
        raise click.UsageError('Parameter --id cannot be whitespace or empty string')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    client = cli_util.build_client('dts', 'transfer_device', ctx)
    result = client.list_transfer_devices(
        id=id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@transfer_device_group.command(name=cli_util.override('transfer_device.update_transfer_device.command_name', 'update'), help=u"""Updates a Transfer Device \n[Command Reference](updateTransferDevice)""")
@cli_util.option('--id', required=True, help=u"""ID of the Transfer Job""")
@cli_util.option('--transfer-device-label', required=True, help=u"""Label of the Transfer Device""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PREPARING", "READY", "CANCELLED"]), help=u"""""")
@cli_util.option('--if-match', help=u"""The entity tag to match. Optional, if set, the update will be successful only if the object's tag matches the tag specified in the request.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PREPARING", "READY", "PACKAGED", "ACTIVE", "PROCESSING", "COMPLETE", "MISSING", "ERROR", "DELETED", "CANCELLED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dts', 'class': 'TransferDevice'})
@cli_util.wrap_exceptions
def update_transfer_device(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, id, transfer_device_label, lifecycle_state, if_match):

    if isinstance(id, six.string_types) and len(id.strip()) == 0:
        raise click.UsageError('Parameter --id cannot be whitespace or empty string')

    if isinstance(transfer_device_label, six.string_types) and len(transfer_device_label.strip()) == 0:
        raise click.UsageError('Parameter --transfer-device-label cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if lifecycle_state is not None:
        _details['lifecycleState'] = lifecycle_state

    client = cli_util.build_client('dts', 'transfer_device', ctx)
    result = client.update_transfer_device(
        id=id,
        transfer_device_label=transfer_device_label,
        update_transfer_device_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_transfer_device') and callable(getattr(client, 'get_transfer_device')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_transfer_device(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
