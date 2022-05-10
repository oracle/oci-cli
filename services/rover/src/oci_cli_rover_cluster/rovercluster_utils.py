# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import json

import click
import six
from oci_cli import cli_util
from oci_cli.cli_util import formatted_flat_dict

from services.rover.src.constants import ROVER_CLUSTER_STATION_TYPE, ROVER_CLUSTER_STANDALONE_TYPE, \
    ROVER_WORKLOAD_TYPE_IMAGE
from services.rover.src.oci_cli_rover.rover_utils import create_master_key_policy_rover_resource, \
    remove_additional_params_after_policy, prompt_for_workload_delete, prompt_for_secrets, validate_bucket, \
    prepare_bucket_workload_data, validate_get_image, prepare_image_workload_data, export_compute_image_status_helper, \
    export_compute_image_helper
from services.rover.src.oci_cli_rover_cluster.generated import rovercluster_cli


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


def get_rover_cluster_helper(ctx, cluster_id):
    kwargs_request = {
        'opc_request_id': cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    }

    client = cli_util.build_client('rover', 'rover_cluster', ctx)

    return client.get_rover_cluster(
        rover_cluster_id=cluster_id,
        **kwargs_request
    )


def create_cluster_common(ctx, **kwargs):
    cluster_type = kwargs.pop('cluster_type')
    if cluster_type == ROVER_CLUSTER_STANDALONE_TYPE:
        if 5 > kwargs['cluster_size'] > 15:
            raise click.UsageError("Please enter cluster-size in valid range from 5 to 15")
    elif cluster_type == ROVER_CLUSTER_STATION_TYPE:
        if 15 > kwargs['cluster_size'] > 30:
            raise click.UsageError("Please enter cluster-size in valid range from 15 to 30")

    # set up policy for master key if provided
    if kwargs['master_key_id']:
        create_master_key_policy_rover_resource("cluster", ctx, **kwargs)
    elif kwargs['policy_name'] or kwargs['policy_compartment_id']:
        raise click.UsageError('policy-compartment-id or policy-name cannot be provided without master-key-id')
    # Remove additional parameters of policy from kwargs
    kwargs = remove_additional_params_after_policy(**kwargs)

    kwargs = complex_shipping_address_param(**kwargs)
    kwargs['cluster_type'] = cluster_type
    kwargs['cluster_workloads'] = []
    ctx.invoke(rovercluster_cli.create_rover_cluster, **kwargs)


def show_cluster_common(ctx, **kwargs):
    if isinstance(kwargs['cluster_id'], six.string_types) and len(kwargs['cluster_id'].strip()) == 0:
        raise click.UsageError('Parameter --cluster-id cannot be whitespace or empty string')

    result = get_rover_cluster_helper(ctx, kwargs['cluster_id'])
    cli_util.render_response(result, ctx)


def update_cluster_common(ctx, **kwargs):
    # Get the RoverCluster and check if the policy language has been added by Oracle
    client = cli_util.build_client('rover', 'rover_cluster', ctx)

    kwargs = complex_shipping_address_param(**kwargs)
    if not kwargs['lifecycle_state_details']:
        pending_lifecycle_state = "PENDING_SUBMISSION"
        click.echo("WARNING:Rover cluster will be updated with lifecycle state details " + pending_lifecycle_state)
        kwargs['lifecycle_state_details'] = pending_lifecycle_state
    kwargs.update({
        'rover_cluster_id': kwargs['cluster_id']
    })
    kwargs.pop('cluster_id')

    ctx.invoke(rovercluster_cli.update_rover_cluster, **kwargs)


def request_cluster_common(ctx, cluster_type, **kwargs):
    kwargs_request = {'rover_cluster_id': kwargs['cluster_id'],
                      'lifecycle_state': "ACTIVE",
                      'lifecycle_state_details': "PENDING_APPROVAL"}
    if cluster_type == ROVER_CLUSTER_STATION_TYPE:
        result = get_rover_cluster_helper(ctx, kwargs['cluster_id'])
        if result.data.lifecycle_state_details == "SUBSCRIPTION_ID_INCORRECT":
            if 'subscription_id' in kwargs:
                kwargs_request.update({'subscription_id': kwargs['subscription-id']})
            else:
                click.echo("Please update Subscription ID in order to request for approval")
                ctx.abort()
        else:
            if kwargs['subscription_id']:
                click.echo("Subscription ID update is not allowed")
                ctx.abort()
    click.echo("Changing the state of the RoverStandalone Cluster to PENDING_APPROVAL")
    ctx.invoke(rovercluster_cli.update_rover_cluster, **kwargs_request)


def delete_cluster_common(ctx, **kwargs):
    if isinstance(kwargs['cluster_id'], six.string_types) and len(kwargs['cluster_id'].strip()) == 0:
        raise click.UsageError('Parameter --cluster-id cannot be whitespace or empty string')

    kwargs_request = {}
    kwargs_request['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('rover', 'rover_cluster', ctx)
    result = client.delete_rover_cluster(
        rover_cluster_id=kwargs['cluster_id'],
        **kwargs_request
    )
    cli_util.render_response(result, ctx)


def set_secrets_cluster_common(ctx, **kwargs):
    kwargs_request = {'rover_cluster_id': kwargs['cluster_id']}
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

    ctx.invoke(rovercluster_cli.update_rover_cluster, **kwargs_request)


def change_cluster_compartment_common(ctx, **kwargs):

    if isinstance(kwargs['cluster_id'], six.string_types) and len(kwargs['cluster_id'].strip()) == 0:
        raise click.UsageError('Parameter --cluster-id cannot be whitespace or empty string')
    kwargs.update({'rover_cluster_id': kwargs['cluster_id']})
    kwargs.pop('cluster_id')
    ctx.invoke(rovercluster_cli.change_rover_cluster_compartment, **kwargs)


def add_workload_common(ctx, **kwargs):

    workload_data = image_id = workload_id = destination_uri = None
    result = get_rover_cluster_helper(ctx, kwargs['cluster_id'])

    if kwargs['type'].lower() == "bucket":
        result_bucket = validate_bucket(ctx, **kwargs)

        workload_id = result_bucket.data.name
        workload_data = prepare_bucket_workload_data(result_bucket, **kwargs)

    elif kwargs['type'].lower() == "image":
        compute_image_obj = validate_get_image(ctx, **kwargs)
        workload_id = image_id = kwargs['image_id']
        workload_data = prepare_image_workload_data(compute_image_obj, image_id)
        destination_uri = result.data.image_export_par + workload_data[0]['name'] + "_" + image_id + ".oci"
    confirm_prompt = "Would you like to submit the following workload information ? " + formatted_flat_dict(workload_data)
    if result.data.cluster_workloads and len(result.data.cluster_workloads) > 0 and any(existing_workload.id == workload_id for existing_workload in result.data.cluster_workloads):
        raise click.UsageError("Workload with {} is already attached".format(workload_id))

    if not kwargs['force'] and not click.confirm(click.style(confirm_prompt, fg="yellow")):
        click.echo("Aborting workload selection for Rover Cluster")
        ctx.abort()

    if kwargs['type'].lower() == "image":
        export_return_response = export_compute_image_helper(ctx, image_id, destination_uri)
        workload_data[0]["workRequestId"] = export_return_response.headers["opc-work-request-id"]
    if result.data.cluster_workloads:
        workload_data.extend(result.data.cluster_workloads)
    kwargs_request = {'rover_cluster_id': kwargs['cluster_id'],
                      'cluster_workloads': workload_data, 'force': kwargs['force']}
    ctx.invoke(rovercluster_cli.update_rover_cluster, **kwargs_request)


def delete_workload_common(ctx, **kwargs):

    result = get_rover_cluster_helper(ctx, kwargs['cluster_id'])
    workload_index = 0
    workload_data = result.data.cluster_workloads
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
        raise click.UsageError("Cluster has no associated workloads.")
    kwargs_request = {'rover_cluster_id': kwargs['cluster_id'],
                      'cluster_workloads': workload_data, 'force': kwargs['force']}
    ctx.invoke(rovercluster_cli.update_rover_cluster, **kwargs_request)


def list_workloads_common(ctx, **kwargs):
    result = get_rover_cluster_helper(ctx, kwargs['cluster_id'])
    workload_data = result.data.cluster_workloads
    if workload_data:
        for idx, each_workload in enumerate(workload_data, 1):
            if each_workload.workload_type.lower() == ROVER_WORKLOAD_TYPE_IMAGE:
                export_status = export_compute_image_status_helper(ctx, each_workload.work_request_id)
                workload_dict = json.loads(str(each_workload))
                export_status_dict = dict()
                export_status_dict["export_compute_image_status"] = export_status
                workload_dict.update(export_status_dict)
                click.echo("{}. {}".format(idx, formatted_flat_dict(workload_dict)))
            else:
                click.echo("{}. {}".format(idx, formatted_flat_dict(each_workload)))
    else:

        raise click.UsageError("Cluster has no associated workloads.")


def get_rover_cluster_certificate_common(ctx, **kwargs):
    rover_cluster_id = kwargs['cluster_id']
    output_file_path = kwargs['output_file_path']

    if isinstance(rover_cluster_id, six.string_types) and len(rover_cluster_id.strip()) == 0:
        raise click.UsageError('Parameter --cluster-id cannot be whitespace or empty string')

    if isinstance(output_file_path, six.string_types) and len(output_file_path.strip()) == 0:
        raise click.UsageError('Parameter --output-file-path cannot be whitespace or empty string')

    kwargs = {'opc_request_id': cli_util.use_or_generate_request_id(ctx.obj['request_id'])}
    client = cli_util.build_client('rover', 'rover_cluster', ctx)
    result = client.get_rover_cluster_certificate(
        rover_cluster_id=rover_cluster_id,
        **kwargs
    )

    crt_data = cli_util.to_dict(result.data)
    with open(output_file_path, "w") as f:
        for key, val in crt_data.items():
            f.write(str(key) + str(val))
