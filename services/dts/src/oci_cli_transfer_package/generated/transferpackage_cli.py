# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
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


@click.command(cli_util.override('transfer_package.transfer_package_root_group.command_name', 'transfer-package'), cls=CommandGroupWithAlias, help=cli_util.override('transfer_package.transfer_package_root_group.help', """Data Transfer Service API Specification"""), short_help=cli_util.override('transfer_package.transfer_package_root_group.short_help', """Data Transfer Service API"""))
@cli_util.help_option_group
def transfer_package_root_group():
    pass


@click.command(cli_util.override('transfer_package.attach_devices_details_group.command_name', 'attach-devices-details'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def attach_devices_details_group():
    pass


@click.command(cli_util.override('transfer_package.transfer_package_group.command_name', 'transfer-package'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def transfer_package_group():
    pass


dts_service_cli.dts_service_group.add_command(transfer_package_root_group)
transfer_package_root_group.add_command(attach_devices_details_group)
transfer_package_root_group.add_command(transfer_package_group)


@attach_devices_details_group.command(name=cli_util.override('transfer_package.attach_devices_to_transfer_package.command_name', 'attach'), help=u"""Attaches Devices to a Transfer Package""")
@cli_util.option('--id', required=True, help=u"""ID of the Transfer Job""")
@cli_util.option('--transfer-package-label', required=True, help=u"""Label of the Transfer Package""")
@cli_util.option('--device-labels', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of TransferDeviceLabel's""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'device-labels': {'module': 'dts', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'device-labels': {'module': 'dts', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def attach_devices_to_transfer_package(ctx, from_json, id, transfer_package_label, device_labels):

    if isinstance(id, six.string_types) and len(id.strip()) == 0:
        raise click.UsageError('Parameter --id cannot be whitespace or empty string')

    if isinstance(transfer_package_label, six.string_types) and len(transfer_package_label.strip()) == 0:
        raise click.UsageError('Parameter --transfer-package-label cannot be whitespace or empty string')

    kwargs = {}

    _details = {}

    if device_labels is not None:
        _details['deviceLabels'] = cli_util.parse_json_parameter("device_labels", device_labels)

    client = cli_util.build_client('dts', 'transfer_package', ctx)
    result = client.attach_devices_to_transfer_package(
        id=id,
        transfer_package_label=transfer_package_label,
        attach_devices_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@transfer_package_group.command(name=cli_util.override('transfer_package.create_transfer_package.command_name', 'create'), help=u"""Create a new Transfer Package""")
@cli_util.option('--id', required=True, help=u"""ID of the Transfer Job""")
@cli_util.option('--original-package-delivery-tracking-number', help=u"""""")
@cli_util.option('--return-package-delivery-tracking-number', help=u"""""")
@cli_util.option('--package-delivery-vendor', help=u"""""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PREPARING", "SHIPPING", "RECEIVED", "PROCESSING", "PROCESSED", "RETURNED", "DELETED", "CANCELLED", "CANCELLED_RETURNED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dts', 'class': 'TransferPackage'})
@cli_util.wrap_exceptions
def create_transfer_package(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, id, original_package_delivery_tracking_number, return_package_delivery_tracking_number, package_delivery_vendor):

    if isinstance(id, six.string_types) and len(id.strip()) == 0:
        raise click.UsageError('Parameter --id cannot be whitespace or empty string')

    kwargs = {}

    _details = {}

    if original_package_delivery_tracking_number is not None:
        _details['originalPackageDeliveryTrackingNumber'] = original_package_delivery_tracking_number

    if return_package_delivery_tracking_number is not None:
        _details['returnPackageDeliveryTrackingNumber'] = return_package_delivery_tracking_number

    if package_delivery_vendor is not None:
        _details['packageDeliveryVendor'] = package_delivery_vendor

    client = cli_util.build_client('dts', 'transfer_package', ctx)
    result = client.create_transfer_package(
        id=id,
        create_transfer_package_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_transfer_package') and callable(getattr(client, 'get_transfer_package')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_transfer_package(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@transfer_package_group.command(name=cli_util.override('transfer_package.delete_transfer_package.command_name', 'delete'), help=u"""deletes a transfer Package""")
@cli_util.option('--id', required=True, help=u"""ID of the Transfer Job""")
@cli_util.option('--transfer-package-label', required=True, help=u"""Label of the Transfer Package""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_transfer_package(ctx, from_json, id, transfer_package_label):

    if isinstance(id, six.string_types) and len(id.strip()) == 0:
        raise click.UsageError('Parameter --id cannot be whitespace or empty string')

    if isinstance(transfer_package_label, six.string_types) and len(transfer_package_label.strip()) == 0:
        raise click.UsageError('Parameter --transfer-package-label cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('dts', 'transfer_package', ctx)
    result = client.delete_transfer_package(
        id=id,
        transfer_package_label=transfer_package_label,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@transfer_package_group.command(name=cli_util.override('transfer_package.detach_devices_from_transfer_package.command_name', 'detach'), help=u"""Detaches Devices from a Transfer Package""")
@cli_util.option('--id', required=True, help=u"""ID of the Transfer Job""")
@cli_util.option('--transfer-package-label', required=True, help=u"""Label of the Transfer Package""")
@cli_util.option('--device-labels', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of TransferDeviceLabel's""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'device-labels': {'module': 'dts', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'device-labels': {'module': 'dts', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def detach_devices_from_transfer_package(ctx, from_json, id, transfer_package_label, device_labels):

    if isinstance(id, six.string_types) and len(id.strip()) == 0:
        raise click.UsageError('Parameter --id cannot be whitespace or empty string')

    if isinstance(transfer_package_label, six.string_types) and len(transfer_package_label.strip()) == 0:
        raise click.UsageError('Parameter --transfer-package-label cannot be whitespace or empty string')

    kwargs = {}

    _details = {}

    if device_labels is not None:
        _details['deviceLabels'] = cli_util.parse_json_parameter("device_labels", device_labels)

    client = cli_util.build_client('dts', 'transfer_package', ctx)
    result = client.detach_devices_from_transfer_package(
        id=id,
        transfer_package_label=transfer_package_label,
        detach_devices_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@transfer_package_group.command(name=cli_util.override('transfer_package.get_transfer_package.command_name', 'get'), help=u"""Describes a transfer package in detail""")
@cli_util.option('--id', required=True, help=u"""ID of the Transfer Job""")
@cli_util.option('--transfer-package-label', required=True, help=u"""Label of the Transfer Package""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dts', 'class': 'TransferPackage'})
@cli_util.wrap_exceptions
def get_transfer_package(ctx, from_json, id, transfer_package_label):

    if isinstance(id, six.string_types) and len(id.strip()) == 0:
        raise click.UsageError('Parameter --id cannot be whitespace or empty string')

    if isinstance(transfer_package_label, six.string_types) and len(transfer_package_label.strip()) == 0:
        raise click.UsageError('Parameter --transfer-package-label cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('dts', 'transfer_package', ctx)
    result = client.get_transfer_package(
        id=id,
        transfer_package_label=transfer_package_label,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@transfer_package_group.command(name=cli_util.override('transfer_package.list_transfer_packages.command_name', 'list'), help=u"""Lists Transfer Packages associated with a transferJob""")
@cli_util.option('--id', required=True, help=u"""ID of the Transfer Job""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PREPARING", "SHIPPING", "RECEIVED", "PROCESSING", "PROCESSED", "RETURNED", "DELETED", "CANCELLED", "CANCELLED_RETURNED"]), help=u"""filtering by lifecycleState""")
@cli_util.option('--display-name', help=u"""filtering by displayName""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dts', 'class': 'MultipleTransferPackages'})
@cli_util.wrap_exceptions
def list_transfer_packages(ctx, from_json, all_pages, id, lifecycle_state, display_name):

    if isinstance(id, six.string_types) and len(id.strip()) == 0:
        raise click.UsageError('Parameter --id cannot be whitespace or empty string')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    client = cli_util.build_client('dts', 'transfer_package', ctx)
    result = client.list_transfer_packages(
        id=id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@transfer_package_group.command(name=cli_util.override('transfer_package.update_transfer_package.command_name', 'update'), help=u"""Updates a Transfer Package""")
@cli_util.option('--id', required=True, help=u"""ID of the Transfer Job""")
@cli_util.option('--transfer-package-label', required=True, help=u"""Label of the Transfer Package""")
@cli_util.option('--original-package-delivery-tracking-number', help=u"""""")
@cli_util.option('--return-package-delivery-tracking-number', help=u"""""")
@cli_util.option('--package-delivery-vendor', help=u"""""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["SHIPPING", "CANCELLED"]), help=u"""""")
@cli_util.option('--if-match', help=u"""The entity tag to match. Optional, if set, the update will be successful only if the object's tag matches the tag specified in the request.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PREPARING", "SHIPPING", "RECEIVED", "PROCESSING", "PROCESSED", "RETURNED", "DELETED", "CANCELLED", "CANCELLED_RETURNED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dts', 'class': 'TransferPackage'})
@cli_util.wrap_exceptions
def update_transfer_package(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, id, transfer_package_label, original_package_delivery_tracking_number, return_package_delivery_tracking_number, package_delivery_vendor, lifecycle_state, if_match):

    if isinstance(id, six.string_types) and len(id.strip()) == 0:
        raise click.UsageError('Parameter --id cannot be whitespace or empty string')

    if isinstance(transfer_package_label, six.string_types) and len(transfer_package_label.strip()) == 0:
        raise click.UsageError('Parameter --transfer-package-label cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if original_package_delivery_tracking_number is not None:
        _details['originalPackageDeliveryTrackingNumber'] = original_package_delivery_tracking_number

    if return_package_delivery_tracking_number is not None:
        _details['returnPackageDeliveryTrackingNumber'] = return_package_delivery_tracking_number

    if package_delivery_vendor is not None:
        _details['packageDeliveryVendor'] = package_delivery_vendor

    if lifecycle_state is not None:
        _details['lifecycleState'] = lifecycle_state

    client = cli_util.build_client('dts', 'transfer_package', ctx)
    result = client.update_transfer_package(
        id=id,
        transfer_package_label=transfer_package_label,
        update_transfer_package_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_transfer_package') and callable(getattr(client, 'get_transfer_package')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_transfer_package(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
