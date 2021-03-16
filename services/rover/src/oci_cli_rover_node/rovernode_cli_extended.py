# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
import json
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from services.rover.src.constants import ROVER_WORKLOAD_TYPE_IMAGE
from services.rover.src.oci_cli_rover.generated import rover_service_cli
from services.rover.src.oci_cli_rover.rover_utils import get_compute_image_helper, export_compute_image_helper, \
    prompt_for_secrets, prompt_for_workload_delete, export_compute_image_status_helper, modify_image_workload_name
from services.rover.src.oci_cli_rover_node.generated import rovernode_cli
from oci.util import formatted_flat_dict

cli_util.rename_command(rover_service_cli, rover_service_cli.rover_service_group, rovernode_cli.rover_node_group, 'node')
cli_util.rename_command(rover_service_cli, rovernode_cli.rover_node_group, rovernode_cli.get_rover_node, 'show')
cli_util.rename_command(rover_service_cli, rovernode_cli.rover_node_group, rovernode_cli.list_rover_nodes, 'list')
cli_util.rename_command(rover_service_cli, rovernode_cli.rover_node_group, rovernode_cli.get_rover_node_encryption_key, 'get-encryption-key')
cli_util.rename_command(rover_service_cli, rovernode_cli.rover_node_group, rovernode_cli.get_rover_node_certificate, 'get-certificate')


def complex_shipping_address_param(**kwargs):

    kwargs['customer_shipping_address'] = {}
    empty_shipping_address = True
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
    for option, value in customer_address_options.items():
        if option in kwargs:
            if kwargs[option]:
                empty_shipping_address = False
            kwargs['customer_shipping_address'][value] = kwargs[option]
            kwargs.pop(option)
    if empty_shipping_address:
        kwargs['customer_shipping_address'] = None
    return kwargs


def get_rover_node_helper(ctx, node_id):
    kwargs_request = {
        'opc_request_id': cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    }

    client = cli_util.build_client('rover', 'rover_node', ctx)
    return client.get_rover_node(
        rover_node_id=node_id,
        **kwargs_request
    )


def setup_identity_helper(ctx, **kwargs):

    config = oci.config.from_file(file_location=ctx.obj['config_file'], profile_name=ctx.obj['profile'])

    root_compartment = config['tenancy']
    ctx.endpoint = None
    ctx.obj['endpoint'] = None
    rover_node_id = kwargs['rover_node_id']
    compartment_id = kwargs['compartment_id']
    policy_name = kwargs['display_name'] + "-" + rover_node_id[-8:] + "-policy"
    dynamic_group_name = kwargs['display_name'] + "-" + rover_node_id[-8:] + "-dynamic-group"

    # setting up home region and configuration in ctx
    identity_client = cli_util.build_client('identity', 'identity', ctx)
    subscription_kwargs = {}
    subscriptions_result = identity_client.list_region_subscriptions(
        tenancy_id=root_compartment,
        **subscription_kwargs
    )

    if len(subscriptions_result.data) > 1:
        for subscription in subscriptions_result.data:
            if subscription.is_home_region:
                ctx.obj['region'] = subscription.region_name
                ctx.obj['config']['region'] = subscription.region_name
                break

    # setting up dynamic group
    identity_client = cli_util.build_client('identity', 'identity', ctx)

    click.echo('Setting up the dynamic_group in the root compartment.')

    dgroup_kwargs = {}
    dgroup_details = {
        'compartmentId': root_compartment,
        'name': dynamic_group_name,
        'matchingRule': "All{resource.id=" + rover_node_id + "}",
        'description': "Dynamic group of Rover node"
    }

    create_dynamic_group_result = identity_client.create_dynamic_group(
        create_dynamic_group_details=dgroup_details,
        **dgroup_kwargs
    )

    # setting up policies
    click.echo('Setting up the policies in the compartment.')
    statement_1 = "Allow dynamic-group " + dynamic_group_name + " to manage object-family in compartment ID " + compartment_id
    iam_kwargs = {}
    iam_details = {
        'compartmentId': compartment_id,
        'name': policy_name,
        'statements': [statement_1],
        'description': "The policies to allow Rover Nodes to data-sync"
    }

    create_policies_result = identity_client.create_policy(
        create_policy_details=iam_details,
        **iam_kwargs
    )
    return create_policies_result


@cli_util.copy_params_from_generated_command(rovernode_cli.create_rover_node, params_to_exclude=['customer_shipping_address', 'node_workloads', 'public_key', 'serial_number', 'super_user_password', 'unlock_passphrase', 'oracle_shipping_tracking_url', 'shipping_vendor', 'time_pickup_expected'])
@rovernode_cli.rover_node_group.command(name=rovernode_cli.create_rover_node.name, help=rovernode_cli.create_rover_node.help)
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
@cli_util.option('--setup-identity', help=u"""Creating dynamic group and Assigning Policies for Rover node""", is_flag=True)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'customer-shipping-address': {'module': 'rover', 'class': 'ShippingAddress'}, 'node-workloads': {'module': 'rover', 'class': 'list[object]'}, 'freeform-tags': {'module': 'rover', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'rover', 'class': 'RoverNode'})
@cli_util.wrap_exceptions
def create_rover_node_extended(ctx, **kwargs):
    kwargs = complex_shipping_address_param(**kwargs)
    kwargs['node_workloads'] = []
    _details = {}
    _details['displayName'] = kwargs['display_name']
    _details['compartmentId'] = kwargs['compartment_id']

    if kwargs['customer_shipping_address'] is not None:
        _details['customerShippingAddress'] = cli_util.parse_json_parameter("customer_shipping_address", kwargs['customer_shipping_address'])

    if kwargs['node_workloads'] is not None:
        _details['nodeWorkloads'] = cli_util.parse_json_parameter("node_workloads", kwargs['node_workloads'])

    if kwargs['point_of_contact'] is not None:
        _details['pointOfContact'] = kwargs['point_of_contact']

    if kwargs['point_of_contact_phone_number'] is not None:
        _details['pointOfContactPhoneNumber'] = kwargs['point_of_contact_phone_number']

    if kwargs['shipping_preference'] is not None:
        _details['shippingPreference'] = kwargs['shipping_preference']

    if kwargs['time_return_window_starts'] is not None:
        _details['timeReturnWindowStarts'] = kwargs['time_return_window_starts']

    if kwargs['time_return_window_ends'] is not None:
        _details['timeReturnWindowEnds'] = kwargs['time_return_window_ends']

    if kwargs['lifecycle_state'] is not None:
        _details['lifecycleState'] = kwargs['lifecycle_state']

    if kwargs['enclosure_type'] is not None:
        _details['enclosureType'] = kwargs['enclosure_type']

    if kwargs['lifecycle_state_details'] is not None:
        _details['lifecycleStateDetails'] = kwargs['lifecycle_state_details']

    if kwargs['freeform_tags'] is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", kwargs['freeform_tags'])

    if kwargs['defined_tags'] is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", kwargs['defined_tags'])

    if kwargs['system_tags'] is not None:
        _details['systemTags'] = cli_util.parse_json_parameter("system_tags", kwargs['system_tags'])

    # creating rover node

    rover_node_kwrags = {}
    rover_node_kwrags['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('rover', 'rover_node', ctx)

    result = client.create_rover_node(
        create_rover_node_details=_details,
        **rover_node_kwrags
    )
    rover_node_id = result.data.id
    wait_for_state = kwargs['wait_for_state']
    if wait_for_state:
        if hasattr(client, 'get_rover_node') and callable(getattr(client, 'get_rover_node')):
            try:
                wait_period_kwargs = {}
                if kwargs['max_wait_seconds'] is not None:
                    wait_period_kwargs['max_wait_seconds'] = kwargs['max_wait_seconds']
                if kwargs['wait_interval_seconds'] is not None:
                    wait_period_kwargs['max_interval_seconds'] = kwargs['wait_interval_seconds']

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
            return click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)

    # setting up identity
    confirm_prompt = "Do you want to setup the policies of node for data sync in the compartment"
    value = None
    if not kwargs['setup_identity']:
        value = click.confirm(click.style(confirm_prompt, fg="yellow"))
    if value:
        identity_kwargs = {}
        identity_kwargs["rover_node_id"] = rover_node_id
        identity_kwargs['compartment_id'] = kwargs['compartment_id']
        identity_kwargs['display_name'] = kwargs['display_name']
        policy_result = setup_identity_helper(ctx, **identity_kwargs)
    cli_util.render_response(result, ctx)


@cli_util.copy_params_from_generated_command(rovernode_cli.get_rover_node, params_to_exclude=['rover_node_id'])
@rovernode_cli.rover_node_group.command(name=rovernode_cli.get_rover_node.name, help=rovernode_cli.get_rover_node.help)
@cli_util.option('--node-id', required=True, help=u"""Unique RoverCluster identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverNode'})
@cli_util.wrap_exceptions
def show_rover_node_extended(ctx, **kwargs):

    if isinstance(kwargs['node_id'], six.string_types) and len(kwargs['node_id'].strip()) == 0:
        raise click.UsageError('Parameter --node-id cannot be whitespace or empty string')

    result = get_rover_node_helper(ctx, kwargs['node_id'])
    cli_util.render_response(result, ctx)


@cli_util.copy_params_from_generated_command(rovernode_cli.update_rover_node, params_to_exclude=['customer_shipping_address', 'rover_node_id', 'node_workloads', 'public_key', 'serial_number', 'super_user_password', 'unlock_passphrase', 'oracle_shipping_tracking_url', 'shipping_vendor', 'time_pickup_expected'])
@rovernode_cli.rover_node_group.command(name=rovernode_cli.update_rover_node.name, help=rovernode_cli.update_rover_node.help)
@cli_util.option('--node-id', required=True, help=u"""Unique RoverNode identifier""")
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
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'customer-shipping-address': {'module': 'rover', 'class': 'ShippingAddress'}, 'node-workloads': {'module': 'rover', 'class': 'list[object]'}, 'freeform-tags': {'module': 'rover', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'rover', 'class': 'RoverNode'})
@cli_util.wrap_exceptions
def update_rover_node_extended(ctx, **kwargs):

    client = cli_util.build_client('rover', 'rover_node', ctx)

    kwargs = complex_shipping_address_param(**kwargs)
    kwargs['lifecycle_state_details'] = "PENDING_SUBMISSION"
    kwargs.update({
        'rover_node_id': kwargs['node_id']
    })
    kwargs.pop('node_id')
    ctx.invoke(rovernode_cli.update_rover_node, **kwargs)


@rovernode_cli.rover_node_group.command(name="request-approval", help=u"""Submit request for Rover Node""")
@cli_util.option('--node-id', required=True, help=u"""Unique RoverNode identifier""")
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.get_cli_json_input_option({})
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'customer-shipping-address': {'module': 'rover', 'class': 'ShippingAddress'}, 'node-workloads': {'module': 'rover', 'class': 'list[object]'}, 'freeform-tags': {'module': 'rover', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'rover', 'class': 'RoverNode'})
@cli_util.wrap_exceptions
def request_rover_node(ctx, **kwargs):

    kwargs_request = {'rover_node_id': kwargs['node_id'],
                      'lifecycle_state': "ACTIVE", 'lifecycle_state_details': "PENDING_APPROVAL"}
    click.echo("Changing the state of the rover node to PENDING_APPROVAL")
    ctx.invoke(rovernode_cli.update_rover_node, **kwargs_request)


@cli_util.copy_params_from_generated_command(rovernode_cli.delete_rover_node, params_to_exclude=['rover_node_id'])
@rovernode_cli.rover_node_group.command(name=rovernode_cli.delete_rover_node.name, help=rovernode_cli.delete_rover_node.help)
@cli_util.option('--node-id', required=True, help=u"""Unique RoverNode identifier""")
@cli_util.confirm_delete_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_rover_node_extended(ctx, **kwargs):

    if isinstance(kwargs['node_id'], six.string_types) and len(kwargs['node_id'].strip()) == 0:
        raise click.UsageError('Parameter --node-id cannot be whitespace or empty string')

    kwargs_request = {}
    kwargs_request['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('rover', 'rover_node', ctx)
    result = client.delete_rover_node(
        rover_node_id=kwargs['node_id'],
        **kwargs_request
    )
    cli_util.render_response(result, ctx)


@rovernode_cli.rover_node_group.command(name="add-workload", help=u"""Add workload information to Rover Node""")
@cli_util.option('--node-id', required=True, help=u"""Unique RoverNode identifier""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Id of Bucket""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["BUCKET", "IMAGE"]), help=u"""Type of workload""")
@cli_util.option('--image-id', help=u"""Object Store Image OCID for the workload""")
@cli_util.option('--bucket-id', help=u"""Object Store Bucket OCID for the workload""")
@cli_util.option('--bucket-name', help=u"""Object Store Bucket name for the workload""")
@cli_util.option('--prefix', help=u"""List of objects with names matching this prefix would be part of this export job.""")
@cli_util.option('--range-start', help=u"""Object names returned by a list query must be greater or equal to this parameter.""")
@cli_util.option('--range-end', help=u"""Object names returned by a list query must be strictly less than this parameter.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverNode'})
@cli_util.wrap_exceptions
def add_workload(ctx, **kwargs):

    workload_data = image_id = workload_id = compute_obj = destination_uri = None
    result = get_rover_node_helper(ctx, kwargs['node_id'])

    if kwargs['type'].lower() == "bucket":
        if not ('bucket_id' in kwargs and kwargs['bucket_id']) or not ('bucket_name' in kwargs and kwargs['bucket_name']):
            raise click.UsageError('Parameter bucket-id and bucket-name cannot be whitespace or empty string')
        workload_id = kwargs['bucket_id']
        workload_data = [{
            "workloadType": "BUCKET", "id": kwargs['bucket_id'], "name": kwargs['bucket_name'], "compartmentId": kwargs['compartment_id'],
            'prefix': kwargs['prefix'], 'rangeStart': kwargs['range_start'], 'rangeEnd': kwargs['range_end']
        }]

    elif kwargs['type'].lower() == "image":
        if 'image_id' in kwargs and not kwargs['image_id']:
            raise click.UsageError('Parameter image-id cannot be whitespace or empty string')
        workload_id = image_id = kwargs['image_id']
        compute_image_obj = get_compute_image_helper(ctx, image_id)
        compute_image_obj_name = modify_image_workload_name(compute_image_obj.data.display_name)
        destination_uri = result.data.image_export_par + compute_image_obj_name + "_" + image_id + ".oci"
        workload_data = [
            {'workloadType': "IMAGE", 'id': image_id, 'name': compute_image_obj_name,
             'size': compute_image_obj.data.size_in_mbs, 'compartmentId': kwargs['compartment_id'],
             }
        ]
    confirm_prompt = "Would you like to submit the following workload information ? " + formatted_flat_dict(workload_data)
    if result.data.node_workloads:
        if any(existing_workload.id == workload_id for existing_workload in result.data.node_workloads):
            raise click.UsageError("Workload with {} is already attached".format(workload_id))

    if not kwargs['force']:
        if not click.confirm(click.style(confirm_prompt, fg="yellow")):
            click.echo("Aborting workload selection for Rover Cluster")
            ctx.abort()

    if kwargs['type'].lower() == "image":
        export_return_response = export_compute_image_helper(ctx, image_id, destination_uri)
        workload_data[0]["workRequestId"] = export_return_response.headers["opc-work-request-id"]

    if result.data.node_workloads:
        workload_data.extend(result.data.node_workloads)
    kwargs_request = {'rover_node_id': kwargs['node_id'],
                      'node_workloads': workload_data, 'force': kwargs['force']}
    ctx.invoke(rovernode_cli.update_rover_node, **kwargs_request)


@rovernode_cli.rover_node_group.command(name="delete-workload", help=u"""Delete workload information from Rover Node""")
@cli_util.option('--node-id', required=True, help=u"""Unique RoverNode identifier""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverNode'})
@cli_util.wrap_exceptions
def delete_workload(ctx, **kwargs):

    result = get_rover_node_helper(ctx, kwargs['node_id'])
    workload_index = 0
    workload_data = result.data.node_workloads
    if workload_data:
        if len(workload_data) > 1:
            for idx, each_workload in enumerate(workload_data, 1):
                click.echo("{}. {}".format(idx, formatted_flat_dict(each_workload)))
            workload_index = prompt_for_workload_delete()
            if workload_index > len(workload_data) or workload_index < 1:
                raise click.UsageError("Please try again with valid selection")
        if not kwargs['force']:
            confirm_prompt = "Are you sure you want to delete following workload ? " + formatted_flat_dict(
                workload_data[workload_index - 1])
            if not click.confirm(click.style(confirm_prompt, fg="yellow")):
                raise click.UsageError("Aborting workload deletion from Rover Cluster")
        workload_data.pop(workload_index - 1)
    else:
        raise click.UsageError("Node has no associated workloads.")

    kwargs_request = {'rover_node_id': kwargs['node_id'],
                      'node_workloads': workload_data, 'force': kwargs['force']}
    ctx.invoke(rovernode_cli.update_rover_node, **kwargs_request)


@rovernode_cli.rover_node_group.command(name="list-workload", help=u"""List workload information of Rover Node""")
@cli_util.option('--node-id', required=True, help=u"""Unique RoverNode identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverNode'})
@cli_util.wrap_exceptions
def list_workload(ctx, **kwargs):

    result = get_rover_node_helper(ctx, kwargs['node_id'])
    workload_data = result.data.node_workloads
    if workload_data:
        for idx, each_workload in enumerate(workload_data, 1):
            if each_workload.workload_type.lower() == ROVER_WORKLOAD_TYPE_IMAGE:
                export_status = export_compute_image_status_helper(ctx, each_workload.work_request_id)
                export_status = export_compute_image_status_helper(ctx, each_workload.work_request_id)
                workload_dict = json.loads(str(each_workload))
                export_status_dict = dict()
                export_status_dict["export_compute_image_status"] = export_status
                workload_dict.update(export_status_dict)
                click.echo("{}. {}".format(idx, formatted_flat_dict(workload_dict)))
            else:
                click.echo("{}. {}".format(idx, formatted_flat_dict(each_workload)))
    else:
        raise click.UsageError("Node has no associated workloads.")


@cli_util.copy_params_from_generated_command(rovernode_cli.change_rover_node_compartment, params_to_exclude=['rover_node_id'])
@rovernode_cli.rover_node_group.command(name=rovernode_cli.change_rover_node_compartment.name, help=rovernode_cli.change_rover_node_compartment.help)
@cli_util.option('--node-id', required=True, help=u"""Unique RoverNode identifier""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID]  of the compartment into which the resources should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_rover_node_compartment(ctx, **kwargs):

    if isinstance(kwargs['node_id'], six.string_types) and len(kwargs['node_id'].strip()) == 0:
        raise click.UsageError('Parameter --node-id cannot be whitespace or empty string')
    kwargs.update({'rover_node_id': kwargs['node_id']})
    kwargs.pop('node_id')
    ctx.invoke(rovernode_cli.change_rover_node_compartment, **kwargs)


@rovernode_cli.rover_node_group.command(name="set-secrets", help=u"""Assign super-user-password and unlock-password for Rover Node""")
@cli_util.option('--node-id', required=True, help=u"""Unique RoverNode identifier""")
@cli_util.option('--super-user-password', required=False, is_flag=True, help=u"""Assign super-user-password for RoverNode Identifier""")
@cli_util.option('--unlock-passphrase', required=False, is_flag=True, help=u"""Assign unlock-passphrase for RoverNode Identifier""")
@cli_util.help_option
@json_skeleton_utils.get_cli_json_input_option({})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverNode'})
@cli_util.wrap_exceptions
def set_secrets_rover_node(ctx, **kwargs):

    kwargs_request = {'rover_node_id': kwargs['node_id']}

    if kwargs['super_user_password'] or (not kwargs['super_user_password'] and not kwargs['unlock_passphrase']):
        super_user_password = prompt_for_secrets("super_user_password")
        if not super_user_password:
            raise click.UsageError('Super user password cannot be whitespace or empty string')
        kwargs_request['super_user_password'] = super_user_password

    if kwargs['unlock_passphrase'] or (not kwargs['super_user_password'] and not kwargs['unlock_passphrase']):
        unlock_passphrase = prompt_for_secrets("unlock_passphrase")
        if not unlock_passphrase:
            raise click.UsageError('Unlock passphrase cannot be whitespace or empty string')
        kwargs_request['unlock_passphrase'] = unlock_passphrase

    ctx.invoke(rovernode_cli.update_rover_node, **kwargs_request)


@cli_util.copy_params_from_generated_command(rovernode_cli.get_rover_node_encryption_key, params_to_exclude=['rover_node_id'])
@rovernode_cli.rover_node_group.command(name=rovernode_cli.get_rover_node_encryption_key.name, help=rovernode_cli.get_rover_node_encryption_key.help)
@cli_util.option('--node-id', required=True, help=u"""Unique RoverNode identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverNodeEncryptionKey'})
@cli_util.wrap_exceptions
def get_rover_node_encryption_key_extended(ctx, **kwargs):

    if isinstance(kwargs['node_id'], six.string_types) and len(kwargs['node_id'].strip()) == 0:
        raise click.UsageError('Parameter --node-id cannot be whitespace or empty string')
    kwargs.update({'rover_node_id': kwargs['node_id']})
    kwargs.pop('node_id')
    ctx.invoke(rovernode_cli.get_rover_node_encryption_key, **kwargs)


@cli_util.copy_params_from_generated_command(rovernode_cli.get_rover_node_certificate, params_to_exclude=['rover_node_id'])
@rovernode_cli.rover_node_group.command(name=rovernode_cli.get_rover_node_certificate.name, help=rovernode_cli.get_rover_node_certificate.help)
@cli_util.option('--node-id', required=True, help=u"""Unique RoverNode identifier""")
@cli_util.option('--output-file-path', required=True, help=u"""Save the CA certificate in specified location""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverNodeCertificate'})
@cli_util.wrap_exceptions
def get_rover_node_certificate_extended(ctx, **kwargs):
    rover_node_id = kwargs['node_id']
    output_file_path = kwargs['output_file_path']

    if isinstance(rover_node_id, six.string_types) and len(rover_node_id.strip()) == 0:
        raise click.UsageError('Parameter --node-id cannot be whitespace or empty string')

    if isinstance(output_file_path, six.string_types) and len(output_file_path.strip()) == 0:
        raise click.UsageError('Parameter --output-file-path cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('rover', 'rover_node', ctx)
    result = client.get_rover_node_certificate(
        rover_node_id=rover_node_id,
        **kwargs
    )

    crt_data = cli_util.to_dict(result.data)
    with open(output_file_path, "w") as f:
        for key, val in crt_data.items():
            f.write(str(key) + str(val))


@rovernode_cli.rover_node_group.command(name="setup-identity", help=u"""Creating dynamic group and Assigning Policies for Rover node""")
@cli_util.option('--node-id', required=True, help=u"""Unique RoverNode identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverNode'})
@cli_util.wrap_exceptions
def setup_identity_extended(ctx, **kwargs):
    rover_node_id = kwargs['node_id']

    if isinstance(rover_node_id, six.string_types) and len(rover_node_id.strip()) == 0:
        raise click.UsageError('Parameter --node-id cannot be whitespace or empty string')

    kwargs_show = {
        'opc_request_id': cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    }

    # extracting rover node information
    client = cli_util.build_client('rover', 'rover_node', ctx)

    node_result = client.get_rover_node(
        rover_node_id=rover_node_id,
        **kwargs_show
    )

    kwargs = {}
    kwargs["rover_node_id"] = rover_node_id
    kwargs["compartment_id"] = node_result.data.compartment_id
    kwargs["display_name"] = node_result.data.display_name

    result = setup_identity_helper(ctx, **kwargs)
    cli_util.render_response(result, ctx)
