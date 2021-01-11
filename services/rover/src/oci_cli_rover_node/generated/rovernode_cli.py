# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
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
from services.rover.src.oci_cli_rover.generated import rover_service_cli


@click.command(cli_util.override('rover_node.rover_node_root_group.command_name', 'rover-node'), cls=CommandGroupWithAlias, help=cli_util.override('rover_node.rover_node_root_group.help', """A description of the RoverCloudService API."""), short_help=cli_util.override('rover_node.rover_node_root_group.short_help', """RoverCloudService API"""))
@cli_util.help_option_group
def rover_node_root_group():
    pass


@click.command(cli_util.override('rover_node.rover_node_certificate_group.command_name', 'rover-node-certificate'), cls=CommandGroupWithAlias, help="""The certificate response""")
@cli_util.help_option_group
def rover_node_certificate_group():
    pass


@click.command(cli_util.override('rover_node.rover_node_encryption_key_group.command_name', 'rover-node-encryption-key'), cls=CommandGroupWithAlias, help="""The response containing encryption key for a rover node.""")
@cli_util.help_option_group
def rover_node_encryption_key_group():
    pass


@click.command(cli_util.override('rover_node.rover_node_group.command_name', 'rover-node'), cls=CommandGroupWithAlias, help="""Information about a RoverNode.""")
@cli_util.help_option_group
def rover_node_group():
    pass


@click.command(cli_util.override('rover_node.rover_node_set_key_group.command_name', 'rover-node-set-key'), cls=CommandGroupWithAlias, help="""Information about the success of setting a rover node's resource principal public key.""")
@cli_util.help_option_group
def rover_node_set_key_group():
    pass


@click.command(cli_util.override('rover_node.rover_node_get_rpt_group.command_name', 'rover-node-get-rpt'), cls=CommandGroupWithAlias, help="""The resource principal token response.""")
@cli_util.help_option_group
def rover_node_get_rpt_group():
    pass


rover_service_cli.rover_service_group.add_command(rover_node_root_group)
rover_node_root_group.add_command(rover_node_certificate_group)
rover_node_root_group.add_command(rover_node_encryption_key_group)
rover_node_root_group.add_command(rover_node_group)
rover_node_root_group.add_command(rover_node_set_key_group)
rover_node_root_group.add_command(rover_node_get_rpt_group)


@rover_node_group.command(name=cli_util.override('rover_node.change_rover_node_compartment.command_name', 'change-compartment'), help=u"""Moves a rover node into a different compartment. \n[Command Reference](changeRoverNodeCompartment)""")
@cli_util.option('--rover-node-id', required=True, help=u"""Unique RoverNode identifier""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID]  of the compartment into which the resources should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_rover_node_compartment(ctx, from_json, rover_node_id, compartment_id, if_match):

    if isinstance(rover_node_id, six.string_types) and len(rover_node_id.strip()) == 0:
        raise click.UsageError('Parameter --rover-node-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('rover', 'rover_node', ctx)
    result = client.change_rover_node_compartment(
        rover_node_id=rover_node_id,
        change_rover_node_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@rover_node_group.command(name=cli_util.override('rover_node.create_rover_node.command_name', 'create'), help=u"""Creates a new RoverNode. \n[Command Reference](createRoverNode)""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment containing the RoverNode.""")
@cli_util.option('--customer-shipping-address', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--node-workloads', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of existing workloads that should be provisioned on the node.

This option is a JSON list with items of type RoverWorkload.  For documentation on RoverWorkload please see our API reference: https://docs.cloud.oracle.com/api/#/en/rovernode/20201210/datatypes/RoverWorkload.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--super-user-password', help=u"""Root password for the rover node.""")
@cli_util.option('--unlock-passphrase', help=u"""Passphrase to unlock the rover node.""")
@cli_util.option('--point-of-contact', help=u"""Name of point of contact for this order if customer is picking up.""")
@cli_util.option('--point-of-contact-phone-number', help=u"""Phone number of point of contact for this order if customer is picking up.""")
@cli_util.option('--shipping-preference', type=custom_types.CliCaseInsensitiveChoice(["ORACLE_SHIPPED", "CUSTOMER_PICKUP"]), help=u"""Preference for device delivery.""")
@cli_util.option('--shipping-vendor', help=u"""Shipping vendor of choice for orace to customer shipping.""")
@cli_util.option('--time-pickup-expected', type=custom_types.CLI_DATETIME, help=u"""Expected date when customer wants to pickup the device if they chose customer pickup.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--public-key', help=u"""The public key of the resource principal""")
@cli_util.option('--time-return-window-starts', type=custom_types.CLI_DATETIME, help=u"""Start time for the window to pickup the device from customer.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-return-window-ends', type=custom_types.CLI_DATETIME, help=u"""End time for the window to pickup the device from customer.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The current state of the RoverNode.""")
@cli_util.option('--enclosure-type', type=custom_types.CliCaseInsensitiveChoice(["RUGGADIZED", "NON_RUGGADIZED"]), help=u"""The type of enclosure rover nodes in this cluster are shipped in.""")
@cli_util.option('--lifecycle-state-details', help=u"""A property that can contain details on the lifecycle.""")
@cli_util.option('--serial-number', help=u"""Serial number of the node.""")
@cli_util.option('--oracle-shipping-tracking-url', help=u"""Tracking Url for the shipped FmsRoverNode.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--system-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{orcl-cloud: {free-tier-retain: true}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'customer-shipping-address': {'module': 'rover', 'class': 'ShippingAddress'}, 'node-workloads': {'module': 'rover', 'class': 'list[RoverWorkload]'}, 'freeform-tags': {'module': 'rover', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'customer-shipping-address': {'module': 'rover', 'class': 'ShippingAddress'}, 'node-workloads': {'module': 'rover', 'class': 'list[RoverWorkload]'}, 'freeform-tags': {'module': 'rover', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'rover', 'class': 'RoverNode'})
@cli_util.wrap_exceptions
def create_rover_node(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, customer_shipping_address, node_workloads, super_user_password, unlock_passphrase, point_of_contact, point_of_contact_phone_number, shipping_preference, shipping_vendor, time_pickup_expected, public_key, time_return_window_starts, time_return_window_ends, lifecycle_state, enclosure_type, lifecycle_state_details, serial_number, oracle_shipping_tracking_url, freeform_tags, defined_tags, system_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id

    if customer_shipping_address is not None:
        _details['customerShippingAddress'] = cli_util.parse_json_parameter("customer_shipping_address", customer_shipping_address)

    if node_workloads is not None:
        _details['nodeWorkloads'] = cli_util.parse_json_parameter("node_workloads", node_workloads)

    if super_user_password is not None:
        _details['superUserPassword'] = super_user_password

    if unlock_passphrase is not None:
        _details['unlockPassphrase'] = unlock_passphrase

    if point_of_contact is not None:
        _details['pointOfContact'] = point_of_contact

    if point_of_contact_phone_number is not None:
        _details['pointOfContactPhoneNumber'] = point_of_contact_phone_number

    if shipping_preference is not None:
        _details['shippingPreference'] = shipping_preference

    if shipping_vendor is not None:
        _details['shippingVendor'] = shipping_vendor

    if time_pickup_expected is not None:
        _details['timePickupExpected'] = time_pickup_expected

    if public_key is not None:
        _details['publicKey'] = public_key

    if time_return_window_starts is not None:
        _details['timeReturnWindowStarts'] = time_return_window_starts

    if time_return_window_ends is not None:
        _details['timeReturnWindowEnds'] = time_return_window_ends

    if lifecycle_state is not None:
        _details['lifecycleState'] = lifecycle_state

    if enclosure_type is not None:
        _details['enclosureType'] = enclosure_type

    if lifecycle_state_details is not None:
        _details['lifecycleStateDetails'] = lifecycle_state_details

    if serial_number is not None:
        _details['serialNumber'] = serial_number

    if oracle_shipping_tracking_url is not None:
        _details['oracleShippingTrackingUrl'] = oracle_shipping_tracking_url

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if system_tags is not None:
        _details['systemTags'] = cli_util.parse_json_parameter("system_tags", system_tags)

    client = cli_util.build_client('rover', 'rover_node', ctx)
    result = client.create_rover_node(
        create_rover_node_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_rover_node') and callable(getattr(client, 'get_rover_node')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_rover_node(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@rover_node_group.command(name=cli_util.override('rover_node.delete_rover_node.command_name', 'delete'), help=u"""Deletes a RoverNode resource by identifier \n[Command Reference](deleteRoverNode)""")
@cli_util.option('--rover-node-id', required=True, help=u"""Unique RoverNode identifier""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_rover_node(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, rover_node_id, if_match):

    if isinstance(rover_node_id, six.string_types) and len(rover_node_id.strip()) == 0:
        raise click.UsageError('Parameter --rover-node-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('rover', 'rover_node', ctx)
    result = client.delete_rover_node(
        rover_node_id=rover_node_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_rover_node') and callable(getattr(client, 'get_rover_node')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_rover_node(rover_node_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@rover_node_group.command(name=cli_util.override('rover_node.get_rover_node.command_name', 'get'), help=u"""Gets a RoverNode by identifier. \n[Command Reference](getRoverNode)""")
@cli_util.option('--rover-node-id', required=True, help=u"""Unique RoverNode identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverNode'})
@cli_util.wrap_exceptions
def get_rover_node(ctx, from_json, rover_node_id):

    if isinstance(rover_node_id, six.string_types) and len(rover_node_id.strip()) == 0:
        raise click.UsageError('Parameter --rover-node-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('rover', 'rover_node', ctx)
    result = client.get_rover_node(
        rover_node_id=rover_node_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@rover_node_certificate_group.command(name=cli_util.override('rover_node.get_rover_node_certificate.command_name', 'get'), help=u"""Get the certificate for a rover node \n[Command Reference](getRoverNodeCertificate)""")
@cli_util.option('--rover-node-id', required=True, help=u"""Unique RoverNode identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverNodeCertificate'})
@cli_util.wrap_exceptions
def get_rover_node_certificate(ctx, from_json, rover_node_id):

    if isinstance(rover_node_id, six.string_types) and len(rover_node_id.strip()) == 0:
        raise click.UsageError('Parameter --rover-node-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('rover', 'rover_node', ctx)
    result = client.get_rover_node_certificate(
        rover_node_id=rover_node_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@rover_node_encryption_key_group.command(name=cli_util.override('rover_node.get_rover_node_encryption_key.command_name', 'get'), help=u"""Get the data encryption key for a rover node. \n[Command Reference](getRoverNodeEncryptionKey)""")
@cli_util.option('--rover-node-id', required=True, help=u"""Serial number of the rover node.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverNodeEncryptionKey'})
@cli_util.wrap_exceptions
def get_rover_node_encryption_key(ctx, from_json, rover_node_id):

    if isinstance(rover_node_id, six.string_types) and len(rover_node_id.strip()) == 0:
        raise click.UsageError('Parameter --rover-node-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('rover', 'rover_node', ctx)
    result = client.get_rover_node_encryption_key(
        rover_node_id=rover_node_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@rover_node_get_rpt_group.command(name=cli_util.override('rover_node.get_rover_node_get_rpt.command_name', 'get'), help=u"""Get the resource principal token for a rover node \n[Command Reference](getRoverNodeGetRpt)""")
@cli_util.option('--rover-node-id', required=True, help=u"""Unique RoverNode identifier""")
@cli_util.option('--jwt', required=True, help=u"""The Java Web Token which is a signature of the request that is signed with the resource's private key This is meant solely in the context of getRpt""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverNodeGetRpt'})
@cli_util.wrap_exceptions
def get_rover_node_get_rpt(ctx, from_json, rover_node_id, jwt):

    if isinstance(rover_node_id, six.string_types) and len(rover_node_id.strip()) == 0:
        raise click.UsageError('Parameter --rover-node-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('rover', 'rover_node', ctx)
    result = client.get_rover_node_get_rpt(
        rover_node_id=rover_node_id,
        jwt=jwt,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@rover_node_group.command(name=cli_util.override('rover_node.list_rover_nodes.command_name', 'list'), help=u"""Returns a list of RoverNodes. \n[Command Reference](listRoverNodes)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources their lifecycleState matches the given lifecycleState.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverNodeCollection'})
@cli_util.wrap_exceptions
def list_rover_nodes(ctx, from_json, all_pages, page_size, compartment_id, display_name, limit, page, lifecycle_state, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('rover', 'rover_node', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_rover_nodes,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_rover_nodes,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_rover_nodes(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@rover_node_set_key_group.command(name=cli_util.override('rover_node.rover_node_action_set_key.command_name', 'rover-node-action-set-key'), help=u"""Get the resource principal public key for a rover node \n[Command Reference](roverNodeActionSetKey)""")
@cli_util.option('--rover-node-id', required=True, help=u"""Unique RoverNode identifier""")
@cli_util.option('--jwt', required=True, help=u"""The Java Web Token which is a signature of the request that is signed with the resource's private key This is meant solely in the context of getRpt""")
@cli_util.option('--public-key', help=u"""The public key of the resource principal""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverNodeSetKey'})
@cli_util.wrap_exceptions
def rover_node_action_set_key(ctx, from_json, rover_node_id, jwt, public_key, if_match):

    if isinstance(rover_node_id, six.string_types) and len(rover_node_id.strip()) == 0:
        raise click.UsageError('Parameter --rover-node-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if public_key is not None:
        _details['publicKey'] = public_key

    client = cli_util.build_client('rover', 'rover_node', ctx)
    result = client.rover_node_action_set_key(
        rover_node_id=rover_node_id,
        jwt=jwt,
        rover_node_action_set_key_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@rover_node_group.command(name=cli_util.override('rover_node.update_rover_node.command_name', 'update'), help=u"""Updates the RoverNode \n[Command Reference](updateRoverNode)""")
@cli_util.option('--rover-node-id', required=True, help=u"""Unique RoverNode identifier""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--serial-number', help=u"""Serial number of the node.""")
@cli_util.option('--customer-shipping-address', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--node-workloads', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of existing workloads that should be provisioned on the node.

This option is a JSON list with items of type RoverWorkload.  For documentation on RoverWorkload please see our API reference: https://docs.cloud.oracle.com/api/#/en/rovernode/20201210/datatypes/RoverWorkload.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--super-user-password', help=u"""Root password for the rover node.""")
@cli_util.option('--unlock-passphrase', help=u"""Password to unlock the rover node.""")
@cli_util.option('--point-of-contact', help=u"""Name of point of contact for this order if customer is picking up.""")
@cli_util.option('--point-of-contact-phone-number', help=u"""Phone number of point of contact for this order if customer is picking up.""")
@cli_util.option('--oracle-shipping-tracking-url', help=u"""Tracking Url for the shipped FmsRoverNode.""")
@cli_util.option('--shipping-preference', type=custom_types.CliCaseInsensitiveChoice(["ORACLE_SHIPPED", "CUSTOMER_PICKUP"]), help=u"""Preference for device delivery.""")
@cli_util.option('--shipping-vendor', help=u"""Shipping vendor of choice for orace to customer shipping.""")
@cli_util.option('--time-pickup-expected', type=custom_types.CLI_DATETIME, help=u"""Expected date when customer wants to pickup the device if they chose customer pickup.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The current state of the RoverNode.""")
@cli_util.option('--enclosure-type', type=custom_types.CliCaseInsensitiveChoice(["RUGGADIZED", "NON_RUGGADIZED"]), help=u"""The type of enclosure rover nodes in this cluster are shipped in.""")
@cli_util.option('--lifecycle-state-details', help=u"""A property that can contain details on the lifecycle.""")
@cli_util.option('--time-return-window-starts', type=custom_types.CLI_DATETIME, help=u"""Start time for the window to pickup the device from customer.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-return-window-ends', type=custom_types.CLI_DATETIME, help=u"""End time for the window to pickup the device from customer.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--public-key', help=u"""The public key of the resource principal""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--system-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{orcl-cloud: {free-tier-retain: true}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'customer-shipping-address': {'module': 'rover', 'class': 'ShippingAddress'}, 'node-workloads': {'module': 'rover', 'class': 'list[RoverWorkload]'}, 'freeform-tags': {'module': 'rover', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'customer-shipping-address': {'module': 'rover', 'class': 'ShippingAddress'}, 'node-workloads': {'module': 'rover', 'class': 'list[RoverWorkload]'}, 'freeform-tags': {'module': 'rover', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'rover', 'class': 'RoverNode'})
@cli_util.wrap_exceptions
def update_rover_node(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, rover_node_id, display_name, serial_number, customer_shipping_address, node_workloads, super_user_password, unlock_passphrase, point_of_contact, point_of_contact_phone_number, oracle_shipping_tracking_url, shipping_preference, shipping_vendor, time_pickup_expected, lifecycle_state, enclosure_type, lifecycle_state_details, time_return_window_starts, time_return_window_ends, public_key, freeform_tags, defined_tags, system_tags, if_match):

    if isinstance(rover_node_id, six.string_types) and len(rover_node_id.strip()) == 0:
        raise click.UsageError('Parameter --rover-node-id cannot be whitespace or empty string')
    if not force:
        if customer_shipping_address or node_workloads or freeform_tags or defined_tags or system_tags:
            if not click.confirm("WARNING: Updates to customer-shipping-address and node-workloads and freeform-tags and defined-tags and system-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if serial_number is not None:
        _details['serialNumber'] = serial_number

    if customer_shipping_address is not None:
        _details['customerShippingAddress'] = cli_util.parse_json_parameter("customer_shipping_address", customer_shipping_address)

    if node_workloads is not None:
        _details['nodeWorkloads'] = cli_util.parse_json_parameter("node_workloads", node_workloads)

    if super_user_password is not None:
        _details['superUserPassword'] = super_user_password

    if unlock_passphrase is not None:
        _details['unlockPassphrase'] = unlock_passphrase

    if point_of_contact is not None:
        _details['pointOfContact'] = point_of_contact

    if point_of_contact_phone_number is not None:
        _details['pointOfContactPhoneNumber'] = point_of_contact_phone_number

    if oracle_shipping_tracking_url is not None:
        _details['oracleShippingTrackingUrl'] = oracle_shipping_tracking_url

    if shipping_preference is not None:
        _details['shippingPreference'] = shipping_preference

    if shipping_vendor is not None:
        _details['shippingVendor'] = shipping_vendor

    if time_pickup_expected is not None:
        _details['timePickupExpected'] = time_pickup_expected

    if lifecycle_state is not None:
        _details['lifecycleState'] = lifecycle_state

    if enclosure_type is not None:
        _details['enclosureType'] = enclosure_type

    if lifecycle_state_details is not None:
        _details['lifecycleStateDetails'] = lifecycle_state_details

    if time_return_window_starts is not None:
        _details['timeReturnWindowStarts'] = time_return_window_starts

    if time_return_window_ends is not None:
        _details['timeReturnWindowEnds'] = time_return_window_ends

    if public_key is not None:
        _details['publicKey'] = public_key

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if system_tags is not None:
        _details['systemTags'] = cli_util.parse_json_parameter("system_tags", system_tags)

    client = cli_util.build_client('rover', 'rover_node', ctx)
    result = client.update_rover_node(
        rover_node_id=rover_node_id,
        update_rover_node_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_rover_node') and callable(getattr(client, 'get_rover_node')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_rover_node(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
