# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import six  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias

from services.rover.src.oci_cli_rover.generated import rover_service_cli
from services.rover.src.constants import ROVER_CLUSTER_STANDALONE_TYPE, \
    ROVER_CLUSTER_STATION_TYPE
from services.rover.src.oci_cli_rover_bundle.generated import roverbundle_cli
from services.rover.src.oci_cli_rover_cluster.generated import rovercluster_cli
from services.rover.src.oci_cli_rover_cluster.rovercluster_utils import delete_workload_common, \
    add_workload_common, change_cluster_compartment_common, set_secrets_cluster_common, delete_cluster_common, \
    request_cluster_common, update_cluster_common, show_cluster_common, create_cluster_common, list_workloads_common, \
    get_rover_cluster_certificate_common

cli_util.rename_command(rover_service_cli, rover_service_cli.rover_service_group, rovercluster_cli.rover_cluster_group, 'standalone-cluster')
cli_util.rename_command(rover_service_cli, rovercluster_cli.rover_cluster_group, rovercluster_cli.get_rover_cluster, 'show')
cli_util.rename_command(rover_service_cli, rovercluster_cli.rover_cluster_group, rovercluster_cli.list_rover_clusters, 'list')
cli_util.rename_command(rover_service_cli, rovercluster_cli.rover_cluster_group, rovercluster_cli.get_rover_cluster_certificate, 'get-certificate')


@click.command('station-cluster', cls=CommandGroupWithAlias, help="""Description of RoverStation.""")
@cli_util.help_option_group
def rover_station_group():
    pass


@click.command('rover-bundle-request', cls=CommandGroupWithAlias, help="""Rover Bundle Requests for Cluster.""")
@cli_util.help_option_group
def rover_bundle_request_group():
    pass


@click.command('rover-bundle', cls=CommandGroupWithAlias, help="""Rover Bundle for Cluster.""")
@cli_util.help_option_group
def rover_bundle_group():
    pass


@click.command('rover-bundle-version', cls=CommandGroupWithAlias, help="""Rover Bundle Version for Cluster.""")
@cli_util.help_option_group
def rover_bundle_version_group():
    pass


rover_service_cli.rover_service_group.add_command(rover_station_group)
rovercluster_cli.rover_cluster_group.add_command(rover_bundle_request_group)
rovercluster_cli.rover_cluster_group.add_command(rover_bundle_group)
rovercluster_cli.rover_cluster_group.add_command(rover_bundle_version_group)

#  oci rover rover-bundle rover-cluster list-rover-cluster-rover-bundle-requests -> oci rover standalone-cluster rover-bundle-request list
roverbundle_cli.rover_cluster_group.commands.pop(roverbundle_cli.list_rover_cluster_rover_bundle_requests.name)
rover_bundle_request_group.add_command(roverbundle_cli.list_rover_cluster_rover_bundle_requests)
cli_util.rename_command(roverbundle_cli, rover_bundle_request_group, roverbundle_cli.list_rover_cluster_rover_bundle_requests, "list")

#  oci rover rover-bundle rover-cluster request-bundle -> oci rover standalone-cluster rover-bundle copy-to-customer
roverbundle_cli.rover_cluster_group.commands.pop(roverbundle_cli.request_bundle_rover_cluster.name)
rover_bundle_group.add_command(roverbundle_cli.request_bundle_rover_cluster)
cli_util.rename_command(roverbundle_cli, rover_bundle_group, roverbundle_cli.request_bundle_rover_cluster, "copy-to-customer")

#  oci rover rover-bundle rover-cluster retrieve-bundle-status -> oci rover standalone-cluster rover-bundle get-status
roverbundle_cli.rover_cluster_group.commands.pop(roverbundle_cli.retrieve_bundle_status_rover_cluster.name)
rover_bundle_group.add_command(roverbundle_cli.retrieve_bundle_status_rover_cluster)
cli_util.rename_command(roverbundle_cli, rover_bundle_group, roverbundle_cli.retrieve_bundle_status_rover_cluster, "get-status")

#  oci rover rover-bundle rover-cluster retrieve-available-bundle-versions -> oci rover standalone-cluster rover-bundle-version get
roverbundle_cli.rover_cluster_group.commands.pop(roverbundle_cli.retrieve_available_bundle_versions_rover_cluster.name)
rover_bundle_version_group.add_command(roverbundle_cli.retrieve_available_bundle_versions_rover_cluster)
cli_util.rename_command(roverbundle_cli, rover_bundle_version_group, roverbundle_cli.retrieve_available_bundle_versions_rover_cluster, "get")

#  Remove request_additional_nodes
rovercluster_cli.rover_cluster_group.commands.pop(rovercluster_cli.request_additional_nodes.name)


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


@cli_util.copy_params_from_generated_command(rovercluster_cli.create_rover_cluster, params_to_exclude=['customer_shipping_address', 'cluster_workloads', 'data_validation_code', 'import_compartment_id', 'import_file_bucket', 'is_import_requested', 'super_user_password', 'unlock_passphrase', 'oracle_shipping_tracking_url', 'shipping_vendor', 'time_pickup_expected', 'subscription-id', 'cluster_size'])
@rovercluster_cli.rover_cluster_group.command(name=rovercluster_cli.create_rover_cluster.name, help=rovercluster_cli.create_rover_cluster.help)
@cli_util.option('--cluster-size', required=True, type=click.IntRange(5, 15), help=u"""Number of nodes desired in the RoverStandalone cluster, between 5 and 15.""")
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
@cli_util.option('--policy-compartment-id', help=u"""Compartment ID where the master key policy (if master key provided) would be created""")
@cli_util.option('--policy-name', help=u"""Display name for the policy to be created for the master key (if provided)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'customer-shipping-address': {'module': 'rover', 'class': 'ShippingAddress'}, 'cluster-workloads': {'module': 'rover', 'class': 'list[RoverWorkload]'}, 'freeform-tags': {'module': 'rover', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'rover', 'class': 'RoverCluster'})
@cli_util.wrap_exceptions
def create_rover_cluster_extended(ctx, **kwargs):
    kwargs['cluster_type'] = ROVER_CLUSTER_STANDALONE_TYPE
    create_cluster_common(ctx, **kwargs)


@rovercluster_cli.rover_cluster_group.command(name=rovercluster_cli.get_rover_cluster.name, help=rovercluster_cli.get_rover_cluster.help)
@cli_util.option('--cluster-id', required=True, help=u"""Unique RoverStandalone Cluster identifier""")
@cli_util.help_option
@json_skeleton_utils.get_cli_json_input_option({})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverCluster'})
@cli_util.wrap_exceptions
def show_rover_cluster_extended(ctx, **kwargs):
    show_cluster_common(ctx, **kwargs)


@cli_util.copy_params_from_generated_command(rovercluster_cli.update_rover_cluster, params_to_exclude=['customer_shipping_address', 'rover_cluster_id', 'cluster_workloads', 'data_validation_code', 'import_compartment_id', 'import_file_bucket', 'is_import_requested', 'super_user_password', 'unlock_passphrase', 'oracle_shipping_tracking_url', 'shipping_vendor', 'time_pickup_expected'])
@rovercluster_cli.rover_cluster_group.command(name=rovercluster_cli.update_rover_cluster.name, help=rovercluster_cli.update_rover_cluster.help)
@cli_util.option('--cluster-id', required=True, help=u"""Unique RoverStandalone Cluster identifier""")
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
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'customer-shipping-address': {'module': 'rover', 'class': 'ShippingAddress'}, 'cluster-workloads': {'module': 'rover', 'class': 'list[RoverWorkload]'}, 'freeform-tags': {'module': 'rover', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'rover', 'class': 'RoverCluster'})
@cli_util.wrap_exceptions
def update_rover_cluster_extended(ctx, **kwargs):
    update_cluster_common(ctx, **kwargs)


@rovercluster_cli.rover_cluster_group.command(name="request-approval", help=u"""Submit request for Rover Cluster""")
@cli_util.option('--cluster-id', required=True, help=u"""Unique RoverStandalone Cluster identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverCluster'})
@cli_util.wrap_exceptions
def request_rover_cluster(ctx, **kwargs):
    request_cluster_common(ctx, ROVER_CLUSTER_STANDALONE_TYPE, **kwargs)


@cli_util.copy_params_from_generated_command(rovercluster_cli.delete_rover_cluster, params_to_exclude=['rover_cluster_id'])
@rovercluster_cli.rover_cluster_group.command(name=rovercluster_cli.delete_rover_cluster.name, help=rovercluster_cli.delete_rover_cluster.help)
@cli_util.option('--cluster-id', required=True, help=u"""Unique RoverStandalone Cluster identifier""")
@cli_util.confirm_delete_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_rover_cluster_extended(ctx, **kwargs):
    delete_cluster_common(ctx, **kwargs)


@rovercluster_cli.rover_cluster_group.command(name="set-secrets", help=u"""Assign super-user-password and unlock-password for Rover Cluster""")
@cli_util.option('--cluster-id', required=True, help=u"""Unique RoverStandalone Cluster identifier""")
@cli_util.option('--super-user-password', required=False, is_flag=True, help=u"""Assign super-user-password for RoverCluster Identifier""")
@cli_util.option('--unlock-passphrase', required=False, is_flag=True, help=u"""Assign unlock-passphrase for RoverCluster Identifier""")
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverCluster'})
@cli_util.wrap_exceptions
def set_secrets_rover_cluster(ctx, **kwargs):
    set_secrets_cluster_common(ctx, **kwargs)


@cli_util.copy_params_from_generated_command(rovercluster_cli.change_rover_cluster_compartment, params_to_exclude=['rover_cluster_id'])
@rovercluster_cli.rover_cluster_group.command(name=rovercluster_cli.change_rover_cluster_compartment.name, help=rovercluster_cli.change_rover_cluster_compartment.help)
@cli_util.option('--cluster-id', required=True, help=u"""Unique RoverStandalone Cluster identifier""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_rover_cluster_compartment(ctx, **kwargs):
    change_cluster_compartment_common(ctx, **kwargs)


@rovercluster_cli.rover_cluster_group.command(name="add-workload", help=u"""Add workload information to Rover Cluster""")
@cli_util.option('--cluster-id', required=True, help=u"""Unique RoverStandalone Cluster identifier""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["BUCKET", "IMAGE"]), help=u"""Type of workload""")
@cli_util.option('--image-id', help=u"""Object Store Image OCID for the workload""")
@cli_util.option('--bucket-name', help=u"""Object Store Bucket name for the workload""")
@cli_util.option('--prefix', help=u"""List of objects with names matching this prefix would be part of this export job.""")
@cli_util.option('--range-start', help=u"""Object names returned by a list query must be greater or equal to this parameter.""")
@cli_util.option('--range-end', help=u"""Object names returned by a list query must be strictly less than this parameter.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverCluster'})
@cli_util.wrap_exceptions
def add_workload(ctx, **kwargs):
    add_workload_common(ctx, **kwargs)


@rovercluster_cli.rover_cluster_group.command(name="delete-workload", help=u"""Delete workload information from Rover Cluster""")
@cli_util.option('--cluster-id', required=True, help=u"""Unique RoverStandalone Cluster identifier""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverCluster'})
@cli_util.wrap_exceptions
def delete_workload(ctx, **kwargs):
    delete_workload_common(ctx, **kwargs)


@rovercluster_cli.rover_cluster_group.command(name="list-workloads", help=u"""List workload information of Rover Cluster""")
@cli_util.option('--cluster-id', required=True, help=u"""Unique RoverStandalone Cluster identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverCluster'})
@cli_util.wrap_exceptions
def list_workloads(ctx, **kwargs):
    list_workloads_common(ctx, **kwargs)


@cli_util.copy_params_from_generated_command(rovercluster_cli.get_rover_cluster_certificate, params_to_exclude=['rover_cluster_id'])
@rovercluster_cli.rover_cluster_group.command(name=rovercluster_cli.get_rover_cluster_certificate.name, help=rovercluster_cli.get_rover_cluster_certificate.help)
@cli_util.option('--cluster-id', required=True, help=u"""Unique RoverStandalone Cluster identifier""")
@cli_util.option('--output-file-path', required=True, help=u"""Save the CA certificate in specified location""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverClusterCertificate'})
@cli_util.wrap_exceptions
def get_rover_cluster_certificate_extended(ctx, **kwargs):
    get_rover_cluster_certificate_common(ctx, **kwargs)

# Station-cluster


@cli_util.copy_params_from_generated_command(rovercluster_cli.create_rover_cluster, params_to_exclude=['customer_shipping_address', 'cluster_workloads', 'super_user_password', 'unlock_passphrase', 'oracle_shipping_tracking_url', 'shipping_vendor', 'time_pickup_expected', 'cluster_size'])
@rover_station_group.command(name=cli_util.override('rover_cluster.create_rover_cluster.command_name', 'create'), help=u"""Creates a new RoverStation Cluster. \n[Command Reference](createRoverStation)""")
@cli_util.option('--subscription-id', required=True, help=u"""Subscription ID of RoverStation Cluster""")
@cli_util.option('--cluster-size', required=True, type=click.IntRange(15, 30), help=u"""Number of nodes desired in the RoverStation Cluster, between 15 and 30.""")
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
@cli_util.option('--master-key-id',
                 help=u"""Master key OCID in the customer tenancy that is used to encrypt customer secret information like superuser password and unlock passphrase""")
@cli_util.option('--policy-compartment-id', help=u"""Compartment ID where the master key policy (if master key provided) would be created""")
@cli_util.option('--policy-name', help=u"""Display name for the policy to be created for the master key (if provided)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'customer-shipping-address': {'module': 'rover', 'class': 'ShippingAddress'}, 'cluster-workloads': {'module': 'rover', 'class': 'list[RoverWorkload]'}, 'freeform-tags': {'module': 'rover', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'rover', 'class': 'RoverCluster'})
@cli_util.wrap_exceptions
def create_rover_station_extended(ctx, **kwargs):
    kwargs['cluster_type'] = ROVER_CLUSTER_STATION_TYPE
    create_cluster_common(ctx, **kwargs)


@rover_station_group.command(name=cli_util.override('rover_cluster.get_rover_cluster.command_name', 'show'), help=u"""Get a RoverStation.""")
@cli_util.option('--cluster-id', required=True, help=u"""Unique RoverStation Cluster identifier""")
@cli_util.help_option
@json_skeleton_utils.get_cli_json_input_option({})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverCluster'})
@cli_util.wrap_exceptions
def show_rover_station_extended(ctx, **kwargs):
    show_cluster_common(ctx, **kwargs)


@cli_util.copy_params_from_generated_command(rovercluster_cli.update_rover_cluster, params_to_exclude=['customer_shipping_address', 'rover_cluster_id', 'cluster_workloads', 'super_user_password', 'unlock_passphrase', 'oracle_shipping_tracking_url', 'shipping_vendor', 'time_pickup_expected'])
@rover_station_group.command(name=cli_util.override('rover_cluster.update_rover_cluster.command_name', 'update'), help=u"""Update a RoverStation.""")
@cli_util.option('--cluster-id', required=True, help=u"""Unique RoverStation Cluster identifier""")
@cli_util.option('--subscription-id', help=u"""Subscription ID of cluster""")
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
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'customer-shipping-address': {'module': 'rover', 'class': 'ShippingAddress'}, 'cluster-workloads': {'module': 'rover', 'class': 'list[RoverWorkload]'}, 'freeform-tags': {'module': 'rover', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'rover', 'class': 'RoverCluster'})
@cli_util.wrap_exceptions
def update_rover_station_extended(ctx, **kwargs):
    update_cluster_common(ctx, **kwargs)


@rover_station_group.command(name="request-approval", help=u"""Submit request for Rover Station""")
@cli_util.option('--cluster-id', required=True, help=u"""Unique RoverStation Cluster identifier""")
@cli_util.option('--subscription-id', help=u"""Subscription ID of RoverStation Cluster""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverCluster'})
@cli_util.wrap_exceptions
def request_rover_station(ctx, **kwargs):
    request_cluster_common(ctx, ROVER_CLUSTER_STATION_TYPE, **kwargs)


@cli_util.copy_params_from_generated_command(rovercluster_cli.delete_rover_cluster, params_to_exclude=['rover_cluster_id'])
@rover_station_group.command(name=rovercluster_cli.delete_rover_cluster.name,
                             help=rovercluster_cli.delete_rover_cluster.help)
@cli_util.option('--cluster-id', required=True, help=u"""Unique RoverStation Cluster identifier""")
@cli_util.confirm_delete_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_rover_station_extended(ctx, **kwargs):
    delete_cluster_common(ctx, **kwargs)


@rover_station_group.command(name="set-secrets", help=u"""Assign super-user-password and unlock-password for Rover Station.""")
@cli_util.option('--cluster-id', required=True, help=u"""Unique RoverStation Cluster identifier""")
@cli_util.option('--super-user-password', required=False, is_flag=True, help=u"""Assign super-user-password for RoverStation Identifier""")
@cli_util.option('--unlock-passphrase', required=False, is_flag=True, help=u"""Assign unlock-passphrase for RoverStation Identifier""")
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverCluster'})
@cli_util.wrap_exceptions
def set_secrets_rover_station(ctx, **kwargs):
    set_secrets_cluster_common(ctx, **kwargs)


@cli_util.copy_params_from_generated_command(rovercluster_cli.change_rover_cluster_compartment, params_to_exclude=['rover_cluster_id'])
@rover_station_group.command(name=rovercluster_cli.change_rover_cluster_compartment.name, help=rovercluster_cli.change_rover_cluster_compartment.help)
@cli_util.option('--cluster-id', required=True, help=u"""Unique RoverStation Cluster identifier""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_rover_station_compartment(ctx, **kwargs):
    change_cluster_compartment_common(ctx, **kwargs)


@rover_station_group.command(name="add-workload", help=u"""Add workload information to Rover Station""")
@cli_util.option('--cluster-id', required=True, help=u"""Unique RoverStation Cluster identifier""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["BUCKET", "IMAGE"]), help=u"""Type of workload""")
@cli_util.option('--image-id', help=u"""Object Store Image OCID for the workload""")
@cli_util.option('--bucket-name', help=u"""Object Store Bucket name for the workload""")
@cli_util.option('--prefix', help=u"""List of objects with names matching this prefix would be part of this export job.""")
@cli_util.option('--range-start', help=u"""Object names returned by a list query must be greater or equal to this parameter.""")
@cli_util.option('--range-end', help=u"""Object names returned by a list query must be strictly less than this parameter.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverCluster'})
@cli_util.wrap_exceptions
def add_workload_station(ctx, **kwargs):
    add_workload_common(ctx, **kwargs)


@rover_station_group.command(name="delete-workload", help=u"""Delete workload information from Rover Station""")
@cli_util.option('--cluster-id', required=True, help=u"""Unique RoverStation Cluster identifier""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverCluster'})
@cli_util.wrap_exceptions
def delete_workload_station(ctx, **kwargs):
    delete_workload_common(ctx, **kwargs)


@rover_station_group.command(name="list-workloads", help=u"""List workload information of Rover Cluster""")
@cli_util.option('--cluster-id', required=True, help=u"""Unique RoverStation Cluster identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverCluster'})
@cli_util.wrap_exceptions
def list_workloads_station(ctx, **kwargs):
    list_workloads_common(ctx, **kwargs)


@cli_util.copy_params_from_generated_command(rovercluster_cli.get_rover_cluster_certificate, params_to_exclude=['rover_cluster_id'])
@rover_station_group.command(name=rovercluster_cli.get_rover_cluster_certificate.name, help=rovercluster_cli.get_rover_cluster_certificate.help)
@cli_util.option('--cluster-id', required=True, help=u"""Unique RoverCluster identifier""")
@cli_util.option('--output-file-path', required=True, help=u"""Save the CA certificate in specified location""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverClusterCertificate'})
@cli_util.wrap_exceptions
def get_rover_station_certificate_extended(ctx, **kwargs):
    get_rover_cluster_certificate_common(ctx, **kwargs)
