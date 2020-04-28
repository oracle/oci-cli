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


@click.command(cli_util.override('transfer_appliance.transfer_appliance_root_group.command_name', 'transfer-appliance'), cls=CommandGroupWithAlias, help=cli_util.override('transfer_appliance.transfer_appliance_root_group.help', """Data Transfer Service API Specification"""), short_help=cli_util.override('transfer_appliance.transfer_appliance_root_group.short_help', """Data Transfer Service API"""))
@cli_util.help_option_group
def transfer_appliance_root_group():
    pass


@click.command(cli_util.override('transfer_appliance.transfer_appliance_certificate_group.command_name', 'transfer-appliance-certificate'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def transfer_appliance_certificate_group():
    pass


@click.command(cli_util.override('transfer_appliance.transfer_appliance_group.command_name', 'transfer-appliance'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def transfer_appliance_group():
    pass


@click.command(cli_util.override('transfer_appliance.transfer_appliance_public_key_group.command_name', 'transfer-appliance-public-key'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def transfer_appliance_public_key_group():
    pass


@click.command(cli_util.override('transfer_appliance.transfer_appliance_encryption_passphrase_group.command_name', 'transfer-appliance-encryption-passphrase'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def transfer_appliance_encryption_passphrase_group():
    pass


dts_service_cli.dts_service_group.add_command(transfer_appliance_root_group)
transfer_appliance_root_group.add_command(transfer_appliance_certificate_group)
transfer_appliance_root_group.add_command(transfer_appliance_group)
transfer_appliance_root_group.add_command(transfer_appliance_public_key_group)
transfer_appliance_root_group.add_command(transfer_appliance_encryption_passphrase_group)


@transfer_appliance_group.command(name=cli_util.override('transfer_appliance.create_transfer_appliance.command_name', 'create'), help=u"""Create a new Transfer Appliance""")
@cli_util.option('--id', required=True, help=u"""ID of the Transfer Job""")
@cli_util.option('--customer-shipping-address', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["REQUESTED", "ORACLE_PREPARING", "SHIPPING", "DELIVERED", "PREPARING", "FINALIZED", "RETURN_DELAYED", "RETURN_SHIPPED", "RETURN_SHIPPED_CANCELLED", "ORACLE_RECEIVED", "ORACLE_RECEIVED_CANCELLED", "PROCESSING", "COMPLETE", "CUSTOMER_NEVER_RECEIVED", "ORACLE_NEVER_RECEIVED", "CUSTOMER_LOST", "CANCELLED", "DELETED", "REJECTED", "ERROR"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'customer-shipping-address': {'module': 'dts', 'class': 'ShippingAddress'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'customer-shipping-address': {'module': 'dts', 'class': 'ShippingAddress'}}, output_type={'module': 'dts', 'class': 'TransferAppliance'})
@cli_util.wrap_exceptions
def create_transfer_appliance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, id, customer_shipping_address):

    if isinstance(id, six.string_types) and len(id.strip()) == 0:
        raise click.UsageError('Parameter --id cannot be whitespace or empty string')

    kwargs = {}

    _details = {}

    if customer_shipping_address is not None:
        _details['customerShippingAddress'] = cli_util.parse_json_parameter("customer_shipping_address", customer_shipping_address)

    client = cli_util.build_client('dts', 'transfer_appliance', ctx)
    result = client.create_transfer_appliance(
        id=id,
        create_transfer_appliance_details=_details,
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


@transfer_appliance_public_key_group.command(name=cli_util.override('transfer_appliance.create_transfer_appliance_admin_credentials.command_name', 'create-transfer-appliance-admin-credentials'), help=u"""Creates an X.509 certificate from a public key""")
@cli_util.option('--id', required=True, help=u"""ID of the Transfer Job""")
@cli_util.option('--transfer-appliance-label', required=True, help=u"""Label of the Transfer Appliance""")
@cli_util.option('--public-key', help=u"""""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dts', 'class': 'TransferApplianceCertificate'})
@cli_util.wrap_exceptions
def create_transfer_appliance_admin_credentials(ctx, from_json, id, transfer_appliance_label, public_key):

    if isinstance(id, six.string_types) and len(id.strip()) == 0:
        raise click.UsageError('Parameter --id cannot be whitespace or empty string')

    if isinstance(transfer_appliance_label, six.string_types) and len(transfer_appliance_label.strip()) == 0:
        raise click.UsageError('Parameter --transfer-appliance-label cannot be whitespace or empty string')

    kwargs = {}

    _details = {}

    if public_key is not None:
        _details['publicKey'] = public_key

    client = cli_util.build_client('dts', 'transfer_appliance', ctx)
    result = client.create_transfer_appliance_admin_credentials(
        id=id,
        transfer_appliance_label=transfer_appliance_label,
        admin_public_key=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@transfer_appliance_group.command(name=cli_util.override('transfer_appliance.delete_transfer_appliance.command_name', 'delete'), help=u"""deletes a transfer Appliance""")
@cli_util.option('--id', required=True, help=u"""ID of the Transfer Job""")
@cli_util.option('--transfer-appliance-label', required=True, help=u"""Label of the Transfer Appliance""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_transfer_appliance(ctx, from_json, id, transfer_appliance_label):

    if isinstance(id, six.string_types) and len(id.strip()) == 0:
        raise click.UsageError('Parameter --id cannot be whitespace or empty string')

    if isinstance(transfer_appliance_label, six.string_types) and len(transfer_appliance_label.strip()) == 0:
        raise click.UsageError('Parameter --transfer-appliance-label cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('dts', 'transfer_appliance', ctx)
    result = client.delete_transfer_appliance(
        id=id,
        transfer_appliance_label=transfer_appliance_label,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@transfer_appliance_group.command(name=cli_util.override('transfer_appliance.get_transfer_appliance.command_name', 'get'), help=u"""Describes a transfer appliance in detail""")
@cli_util.option('--id', required=True, help=u"""ID of the Transfer Job""")
@cli_util.option('--transfer-appliance-label', required=True, help=u"""Label of the Transfer Appliance""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dts', 'class': 'TransferAppliance'})
@cli_util.wrap_exceptions
def get_transfer_appliance(ctx, from_json, id, transfer_appliance_label):

    if isinstance(id, six.string_types) and len(id.strip()) == 0:
        raise click.UsageError('Parameter --id cannot be whitespace or empty string')

    if isinstance(transfer_appliance_label, six.string_types) and len(transfer_appliance_label.strip()) == 0:
        raise click.UsageError('Parameter --transfer-appliance-label cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('dts', 'transfer_appliance', ctx)
    result = client.get_transfer_appliance(
        id=id,
        transfer_appliance_label=transfer_appliance_label,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@transfer_appliance_certificate_group.command(name=cli_util.override('transfer_appliance.get_transfer_appliance_certificate_authority_certificate.command_name', 'get-transfer-appliance-certificate-authority-certificate'), help=u"""Gets the x.509 certificate for the Transfer Appliance's dedicated Certificate Authority (CA)""")
@cli_util.option('--id', required=True, help=u"""ID of the Transfer Job""")
@cli_util.option('--transfer-appliance-label', required=True, help=u"""Label of the Transfer Appliance""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dts', 'class': 'TransferApplianceCertificate'})
@cli_util.wrap_exceptions
def get_transfer_appliance_certificate_authority_certificate(ctx, from_json, id, transfer_appliance_label):

    if isinstance(id, six.string_types) and len(id.strip()) == 0:
        raise click.UsageError('Parameter --id cannot be whitespace or empty string')

    if isinstance(transfer_appliance_label, six.string_types) and len(transfer_appliance_label.strip()) == 0:
        raise click.UsageError('Parameter --transfer-appliance-label cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('dts', 'transfer_appliance', ctx)
    result = client.get_transfer_appliance_certificate_authority_certificate(
        id=id,
        transfer_appliance_label=transfer_appliance_label,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@transfer_appliance_encryption_passphrase_group.command(name=cli_util.override('transfer_appliance.get_transfer_appliance_encryption_passphrase.command_name', 'get'), help=u"""Describes a transfer appliance encryptionPassphrase in detail""")
@cli_util.option('--id', required=True, help=u"""ID of the Transfer Job""")
@cli_util.option('--transfer-appliance-label', required=True, help=u"""Label of the Transfer Appliance""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dts', 'class': 'TransferApplianceEncryptionPassphrase'})
@cli_util.wrap_exceptions
def get_transfer_appliance_encryption_passphrase(ctx, from_json, id, transfer_appliance_label):

    if isinstance(id, six.string_types) and len(id.strip()) == 0:
        raise click.UsageError('Parameter --id cannot be whitespace or empty string')

    if isinstance(transfer_appliance_label, six.string_types) and len(transfer_appliance_label.strip()) == 0:
        raise click.UsageError('Parameter --transfer-appliance-label cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('dts', 'transfer_appliance', ctx)
    result = client.get_transfer_appliance_encryption_passphrase(
        id=id,
        transfer_appliance_label=transfer_appliance_label,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@transfer_appliance_group.command(name=cli_util.override('transfer_appliance.list_transfer_appliances.command_name', 'list'), help=u"""Lists Transfer Appliances associated with a transferJob""")
@cli_util.option('--id', required=True, help=u"""ID of the Transfer Job""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["REQUESTED", "ORACLE_PREPARING", "SHIPPING", "DELIVERED", "PREPARING", "FINALIZED", "RETURN_DELAYED", "RETURN_SHIPPED", "RETURN_SHIPPED_CANCELLED", "ORACLE_RECEIVED", "ORACLE_RECEIVED_CANCELLED", "PROCESSING", "COMPLETE", "CUSTOMER_NEVER_RECEIVED", "ORACLE_NEVER_RECEIVED", "CUSTOMER_LOST", "CANCELLED", "DELETED", "REJECTED", "ERROR"]), help=u"""filtering by lifecycleState""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dts', 'class': 'MultipleTransferAppliances'})
@cli_util.wrap_exceptions
def list_transfer_appliances(ctx, from_json, all_pages, id, lifecycle_state):

    if isinstance(id, six.string_types) and len(id.strip()) == 0:
        raise click.UsageError('Parameter --id cannot be whitespace or empty string')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('dts', 'transfer_appliance', ctx)
    result = client.list_transfer_appliances(
        id=id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@transfer_appliance_group.command(name=cli_util.override('transfer_appliance.update_transfer_appliance.command_name', 'update'), help=u"""Updates a Transfer Appliance""")
@cli_util.option('--id', required=True, help=u"""ID of the Transfer Job""")
@cli_util.option('--transfer-appliance-label', required=True, help=u"""Label of the Transfer Appliance""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PREPARING", "FINALIZED", "DELETED", "CUSTOMER_NEVER_RECEIVED", "CANCELLED"]), help=u"""""")
@cli_util.option('--customer-shipping-address', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The entity tag to match. Optional, if set, the update will be successful only if the object's tag matches the tag specified in the request.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["REQUESTED", "ORACLE_PREPARING", "SHIPPING", "DELIVERED", "PREPARING", "FINALIZED", "RETURN_DELAYED", "RETURN_SHIPPED", "RETURN_SHIPPED_CANCELLED", "ORACLE_RECEIVED", "ORACLE_RECEIVED_CANCELLED", "PROCESSING", "COMPLETE", "CUSTOMER_NEVER_RECEIVED", "ORACLE_NEVER_RECEIVED", "CUSTOMER_LOST", "CANCELLED", "DELETED", "REJECTED", "ERROR"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'customer-shipping-address': {'module': 'dts', 'class': 'ShippingAddress'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'customer-shipping-address': {'module': 'dts', 'class': 'ShippingAddress'}}, output_type={'module': 'dts', 'class': 'TransferAppliance'})
@cli_util.wrap_exceptions
def update_transfer_appliance(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, id, transfer_appliance_label, lifecycle_state, customer_shipping_address, if_match):

    if isinstance(id, six.string_types) and len(id.strip()) == 0:
        raise click.UsageError('Parameter --id cannot be whitespace or empty string')

    if isinstance(transfer_appliance_label, six.string_types) and len(transfer_appliance_label.strip()) == 0:
        raise click.UsageError('Parameter --transfer-appliance-label cannot be whitespace or empty string')
    if not force:
        if customer_shipping_address:
            if not click.confirm("WARNING: Updates to customer-shipping-address will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if lifecycle_state is not None:
        _details['lifecycleState'] = lifecycle_state

    if customer_shipping_address is not None:
        _details['customerShippingAddress'] = cli_util.parse_json_parameter("customer_shipping_address", customer_shipping_address)

    client = cli_util.build_client('dts', 'transfer_appliance', ctx)
    result = client.update_transfer_appliance(
        id=id,
        transfer_appliance_label=transfer_appliance_label,
        update_transfer_appliance_details=_details,
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
