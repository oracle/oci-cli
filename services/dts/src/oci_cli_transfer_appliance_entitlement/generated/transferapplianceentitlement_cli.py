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


@click.command(cli_util.override('transfer_appliance_entitlement.transfer_appliance_entitlement_root_group.command_name', 'transfer-appliance-entitlement'), cls=CommandGroupWithAlias, help=cli_util.override('transfer_appliance_entitlement.transfer_appliance_entitlement_root_group.help', """Data Transfer Service API Specification"""), short_help=cli_util.override('transfer_appliance_entitlement.transfer_appliance_entitlement_root_group.short_help', """Data Transfer Service API"""))
@cli_util.help_option_group
def transfer_appliance_entitlement_root_group():
    pass


@click.command(cli_util.override('transfer_appliance_entitlement.transfer_appliance_entitlement_group.command_name', 'transfer-appliance-entitlement'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def transfer_appliance_entitlement_group():
    pass


dts_service_cli.dts_service_group.add_command(transfer_appliance_entitlement_root_group)
transfer_appliance_entitlement_root_group.add_command(transfer_appliance_entitlement_group)


@transfer_appliance_entitlement_group.command(name=cli_util.override('transfer_appliance_entitlement.create_transfer_appliance_entitlement.command_name', 'create'), help=u"""Create the Entitlement to use a Transfer Appliance. It requires some offline process of review and signatures before request is granted. \n[Command Reference](createTransferApplianceEntitlement)""")
@cli_util.option('--compartment-id', help=u"""""")
@cli_util.option('--display-name', help=u"""""")
@cli_util.option('--requestor-name', help=u"""""")
@cli_util.option('--requestor-email', help=u"""""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'dts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dts', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dts', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'dts', 'class': 'TransferApplianceEntitlement'})
@cli_util.wrap_exceptions
def create_transfer_appliance_entitlement(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, requestor_name, requestor_email, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if requestor_name is not None:
        _details['requestorName'] = requestor_name

    if requestor_email is not None:
        _details['requestorEmail'] = requestor_email

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('dts', 'transfer_appliance_entitlement', ctx)
    result = client.create_transfer_appliance_entitlement(
        create_transfer_appliance_entitlement_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_transfer_appliance_entitlement') and callable(getattr(client, 'get_transfer_appliance_entitlement')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_transfer_appliance_entitlement(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@transfer_appliance_entitlement_group.command(name=cli_util.override('transfer_appliance_entitlement.get_transfer_appliance_entitlement.command_name', 'get'), help=u"""Describes the Transfer Appliance Entitlement in detail \n[Command Reference](getTransferApplianceEntitlement)""")
@cli_util.option('--id', required=True, help=u"""Id of the Transfer Appliance Entitlement""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dts', 'class': 'TransferApplianceEntitlement'})
@cli_util.wrap_exceptions
def get_transfer_appliance_entitlement(ctx, from_json, id):

    if isinstance(id, six.string_types) and len(id.strip()) == 0:
        raise click.UsageError('Parameter --id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dts', 'transfer_appliance_entitlement', ctx)
    result = client.get_transfer_appliance_entitlement(
        id=id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@transfer_appliance_entitlement_group.command(name=cli_util.override('transfer_appliance_entitlement.list_transfer_appliance_entitlement.command_name', 'list'), help=u"""Lists Transfer Transfer Appliance Entitlement \n[Command Reference](listTransferApplianceEntitlement)""")
@cli_util.option('--compartment-id', required=True, help=u"""compartment id""")
@cli_util.option('--id', help=u"""filtering by Transfer Appliance Entitlement id""")
@cli_util.option('--display-name', help=u"""filtering by displayName""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dts', 'class': 'list[TransferApplianceEntitlementSummary]'})
@cli_util.wrap_exceptions
def list_transfer_appliance_entitlement(ctx, from_json, all_pages, compartment_id, id, display_name):

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if display_name is not None:
        kwargs['display_name'] = display_name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dts', 'transfer_appliance_entitlement', ctx)
    result = client.list_transfer_appliance_entitlement(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)
