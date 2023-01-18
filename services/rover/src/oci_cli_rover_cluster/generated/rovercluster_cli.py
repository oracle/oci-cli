# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
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


@click.command(cli_util.override('rover_cluster.rover_cluster_root_group.command_name', 'rover-cluster'), cls=CommandGroupWithAlias, help=cli_util.override('rover_cluster.rover_cluster_root_group.help', """A description of the RoverCloudService API."""), short_help=cli_util.override('rover_cluster.rover_cluster_root_group.short_help', """RoverCloudService API"""))
@cli_util.help_option_group
def rover_cluster_root_group():
    pass


@click.command(cli_util.override('rover_cluster.rover_cluster_group.command_name', 'rover-cluster'), cls=CommandGroupWithAlias, help="""Description of RoverCluster.""")
@cli_util.help_option_group
def rover_cluster_group():
    pass


@click.command(cli_util.override('rover_cluster.rover_cluster_certificate_group.command_name', 'rover-cluster-certificate'), cls=CommandGroupWithAlias, help="""The certificate response""")
@cli_util.help_option_group
def rover_cluster_certificate_group():
    pass


rover_service_cli.rover_service_group.add_command(rover_cluster_root_group)
rover_cluster_root_group.add_command(rover_cluster_group)
rover_cluster_root_group.add_command(rover_cluster_certificate_group)


@rover_cluster_group.command(name=cli_util.override('rover_cluster.change_rover_cluster_compartment.command_name', 'change-compartment'), help=u"""Moves a cluster into a different compartment. \n[Command Reference](changeRoverClusterCompartment)""")
@cli_util.option('--rover-cluster-id', required=True, help=u"""Unique RoverCluster identifier""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID]  of the compartment into which the resources should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_rover_cluster_compartment(ctx, from_json, rover_cluster_id, compartment_id, if_match):

    if isinstance(rover_cluster_id, six.string_types) and len(rover_cluster_id.strip()) == 0:
        raise click.UsageError('Parameter --rover-cluster-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('rover', 'rover_cluster', ctx)
    result = client.change_rover_cluster_compartment(
        rover_cluster_id=rover_cluster_id,
        change_rover_cluster_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@rover_cluster_group.command(name=cli_util.override('rover_cluster.create_rover_cluster.command_name', 'create'), help=u"""Creates a new RoverCluster. \n[Command Reference](createRoverCluster)""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment containing the RoverCluster.""")
@cli_util.option('--cluster-size', required=True, type=click.INT, help=u"""Number of nodes desired in the cluster, in standalone clusters, between 5 and 15 inclusive. In station clusters, between 15 and 30 inclusive.""")
@cli_util.option('--customer-shipping-address', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--cluster-workloads', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of existing workloads that should be provisioned on the nodes.

This option is a JSON list with items of type RoverWorkload.  For documentation on RoverWorkload please see our API reference: https://docs.cloud.oracle.com/api/#/en/rovercluster/20201210/datatypes/RoverWorkload.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--cluster-type', type=custom_types.CliCaseInsensitiveChoice(["STANDALONE", "STATION"]), help=u"""Type of cluster.""")
@cli_util.option('--super-user-password', help=u"""Root password for the rover cluster.""")
@cli_util.option('--enclosure-type', type=custom_types.CliCaseInsensitiveChoice(["RUGGADIZED", "NON_RUGGADIZED"]), help=u"""The type of enclosure rover nodes in this cluster are shipped in.""")
@cli_util.option('--unlock-passphrase', help=u"""Password to unlock the rover cluster.""")
@cli_util.option('--point-of-contact', help=u"""Name of point of contact for this order if customer is picking up.""")
@cli_util.option('--point-of-contact-phone-number', help=u"""Phone number of point of contact for this order if customer is picking up.""")
@cli_util.option('--shipping-preference', type=custom_types.CliCaseInsensitiveChoice(["ORACLE_SHIPPED", "CUSTOMER_PICKUP"]), help=u"""Preference for device delivery.""")
@cli_util.option('--shipping-vendor', help=u"""Shipping vendor of choice for orace to customer shipping.""")
@cli_util.option('--time-pickup-expected', type=custom_types.CLI_DATETIME, help=u"""Expected date when customer wants to pickup the cluster if they chose customer pickup.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--oracle-shipping-tracking-url', help=u"""Tracking Url for the shipped Rover Cluster.""")
@cli_util.option('--subscription-id', help=u"""ID provided to customer after successful subscription to Rover Stations.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The current state of the RoverCluster.""")
@cli_util.option('--lifecycle-state-details', help=u"""A property that can contain details on the lifecycle.""")
@cli_util.option('--is-import-requested', type=click.BOOL, help=u"""The flag indicating that customer requests data to be imported to OCI upon Rover cluster return.""")
@cli_util.option('--import-compartment-id', help=u"""An OCID of a compartment where data will be imported to upon Rover cluster return.""")
@cli_util.option('--import-file-bucket', help=u"""Name of a bucket where files from NFS share will be imported to upon Rover cluster return.""")
@cli_util.option('--data-validation-code', help=u"""Validation code returned by data validation tool. Required for return shipping label generation if data import was requested.""")
@cli_util.option('--master-key-id', help=u"""Customer provided master key ID to encrypt secret information. If not provided, Rover's master key will be used for encryption.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--system-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{orcl-cloud: {free-tier-retain: true}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'customer-shipping-address': {'module': 'rover', 'class': 'ShippingAddress'}, 'cluster-workloads': {'module': 'rover', 'class': 'list[RoverWorkload]'}, 'freeform-tags': {'module': 'rover', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'customer-shipping-address': {'module': 'rover', 'class': 'ShippingAddress'}, 'cluster-workloads': {'module': 'rover', 'class': 'list[RoverWorkload]'}, 'freeform-tags': {'module': 'rover', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'rover', 'class': 'RoverCluster'})
@cli_util.wrap_exceptions
def create_rover_cluster(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, cluster_size, customer_shipping_address, cluster_workloads, cluster_type, super_user_password, enclosure_type, unlock_passphrase, point_of_contact, point_of_contact_phone_number, shipping_preference, shipping_vendor, time_pickup_expected, oracle_shipping_tracking_url, subscription_id, lifecycle_state, lifecycle_state_details, is_import_requested, import_compartment_id, import_file_bucket, data_validation_code, master_key_id, freeform_tags, defined_tags, system_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['clusterSize'] = cluster_size

    if customer_shipping_address is not None:
        _details['customerShippingAddress'] = cli_util.parse_json_parameter("customer_shipping_address", customer_shipping_address)

    if cluster_workloads is not None:
        _details['clusterWorkloads'] = cli_util.parse_json_parameter("cluster_workloads", cluster_workloads)

    if cluster_type is not None:
        _details['clusterType'] = cluster_type

    if super_user_password is not None:
        _details['superUserPassword'] = super_user_password

    if enclosure_type is not None:
        _details['enclosureType'] = enclosure_type

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

    if oracle_shipping_tracking_url is not None:
        _details['oracleShippingTrackingUrl'] = oracle_shipping_tracking_url

    if subscription_id is not None:
        _details['subscriptionId'] = subscription_id

    if lifecycle_state is not None:
        _details['lifecycleState'] = lifecycle_state

    if lifecycle_state_details is not None:
        _details['lifecycleStateDetails'] = lifecycle_state_details

    if is_import_requested is not None:
        _details['isImportRequested'] = is_import_requested

    if import_compartment_id is not None:
        _details['importCompartmentId'] = import_compartment_id

    if import_file_bucket is not None:
        _details['importFileBucket'] = import_file_bucket

    if data_validation_code is not None:
        _details['dataValidationCode'] = data_validation_code

    if master_key_id is not None:
        _details['masterKeyId'] = master_key_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if system_tags is not None:
        _details['systemTags'] = cli_util.parse_json_parameter("system_tags", system_tags)

    client = cli_util.build_client('rover', 'rover_cluster', ctx)
    result = client.create_rover_cluster(
        create_rover_cluster_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_rover_cluster') and callable(getattr(client, 'get_rover_cluster')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_rover_cluster(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@rover_cluster_group.command(name=cli_util.override('rover_cluster.delete_rover_cluster.command_name', 'delete'), help=u"""Deletes a RoverCluster resource by identifier \n[Command Reference](deleteRoverCluster)""")
@cli_util.option('--rover-cluster-id', required=True, help=u"""Unique RoverCluster identifier""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_rover_cluster(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, rover_cluster_id, if_match):

    if isinstance(rover_cluster_id, six.string_types) and len(rover_cluster_id.strip()) == 0:
        raise click.UsageError('Parameter --rover-cluster-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('rover', 'rover_cluster', ctx)
    result = client.delete_rover_cluster(
        rover_cluster_id=rover_cluster_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_rover_cluster') and callable(getattr(client, 'get_rover_cluster')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_rover_cluster(rover_cluster_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@rover_cluster_group.command(name=cli_util.override('rover_cluster.get_rover_cluster.command_name', 'get'), help=u"""Gets a RoverCluster by identifier \n[Command Reference](getRoverCluster)""")
@cli_util.option('--rover-cluster-id', required=True, help=u"""Unique RoverCluster identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverCluster'})
@cli_util.wrap_exceptions
def get_rover_cluster(ctx, from_json, rover_cluster_id):

    if isinstance(rover_cluster_id, six.string_types) and len(rover_cluster_id.strip()) == 0:
        raise click.UsageError('Parameter --rover-cluster-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('rover', 'rover_cluster', ctx)
    result = client.get_rover_cluster(
        rover_cluster_id=rover_cluster_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@rover_cluster_certificate_group.command(name=cli_util.override('rover_cluster.get_rover_cluster_certificate.command_name', 'get'), help=u"""Get the certificate for a rover cluster \n[Command Reference](getRoverClusterCertificate)""")
@cli_util.option('--rover-cluster-id', required=True, help=u"""Unique RoverCluster identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverClusterCertificate'})
@cli_util.wrap_exceptions
def get_rover_cluster_certificate(ctx, from_json, rover_cluster_id):

    if isinstance(rover_cluster_id, six.string_types) and len(rover_cluster_id.strip()) == 0:
        raise click.UsageError('Parameter --rover-cluster-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('rover', 'rover_cluster', ctx)
    result = client.get_rover_cluster_certificate(
        rover_cluster_id=rover_cluster_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@rover_cluster_group.command(name=cli_util.override('rover_cluster.list_rover_clusters.command_name', 'list'), help=u"""Returns a list of RoverClusters. \n[Command Reference](listRoverClusters)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--cluster-type', type=custom_types.CliCaseInsensitiveChoice(["STANDALONE", "STATION"]), help=u"""A filter to return only Clusters of type matched with the given cluster type.""")
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
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverClusterCollection'})
@cli_util.wrap_exceptions
def list_rover_clusters(ctx, from_json, all_pages, page_size, compartment_id, display_name, cluster_type, limit, page, lifecycle_state, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if cluster_type is not None:
        kwargs['cluster_type'] = cluster_type
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
    client = cli_util.build_client('rover', 'rover_cluster', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_rover_clusters,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_rover_clusters,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_rover_clusters(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@rover_cluster_group.command(name=cli_util.override('rover_cluster.update_rover_cluster.command_name', 'update'), help=u"""Updates the RoverCluster \n[Command Reference](updateRoverCluster)""")
@cli_util.option('--rover-cluster-id', required=True, help=u"""Unique RoverCluster identifier""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--cluster-size', type=click.INT, help=u"""Number of nodes desired in the cluster, in standalone clusters, between 5 and 15 inclusive. In station clusters, between 15 and 30 inclusive.""")
@cli_util.option('--customer-shipping-address', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--cluster-workloads', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of existing workloads that should be provisioned on the nodes.

This option is a JSON list with items of type RoverWorkload.  For documentation on RoverWorkload please see our API reference: https://docs.cloud.oracle.com/api/#/en/rovercluster/20201210/datatypes/RoverWorkload.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--super-user-password', help=u"""Root password for the rover cluster.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The current state of the RoverCluster.""")
@cli_util.option('--lifecycle-state-details', help=u"""A property that can contain details on the lifecycle.""")
@cli_util.option('--unlock-passphrase', help=u"""Password to unlock the rover cluster.""")
@cli_util.option('--enclosure-type', type=custom_types.CliCaseInsensitiveChoice(["RUGGADIZED", "NON_RUGGADIZED"]), help=u"""The type of enclosure rover nodes in this cluster are shipped in.""")
@cli_util.option('--point-of-contact', help=u"""Name of point of contact for this order if customer is picking up.""")
@cli_util.option('--point-of-contact-phone-number', help=u"""Phone number of point of contact for this order if customer is picking up.""")
@cli_util.option('--shipping-preference', type=custom_types.CliCaseInsensitiveChoice(["ORACLE_SHIPPED", "CUSTOMER_PICKUP"]), help=u"""Preference for device delivery.""")
@cli_util.option('--oracle-shipping-tracking-url', help=u"""Tracking Url for the shipped Rover Cluster.""")
@cli_util.option('--subscription-id', help=u"""ID provided to customer after successful subscription to Rover Stations.""")
@cli_util.option('--shipping-vendor', help=u"""Shipping vendor of choice for orace to customer shipping.""")
@cli_util.option('--time-pickup-expected', type=custom_types.CLI_DATETIME, help=u"""Expected date when customer wants to pickup the device if they chose customer pickup.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--is-import-requested', type=click.BOOL, help=u"""The flag indicating that customer requests data to be imported to OCI upon Rover cluster return.""")
@cli_util.option('--import-compartment-id', help=u"""An OCID of a compartment where data will be imported to upon Rover cluster return.""")
@cli_util.option('--import-file-bucket', help=u"""Name of a bucket where files from NFS share will be imported to upon Rover cluster return.""")
@cli_util.option('--data-validation-code', help=u"""Validation code returned by data validation tool. Required for return shipping label generation if data import was requested.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--system-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{orcl-cloud: {free-tier-retain: true}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'customer-shipping-address': {'module': 'rover', 'class': 'ShippingAddress'}, 'cluster-workloads': {'module': 'rover', 'class': 'list[RoverWorkload]'}, 'freeform-tags': {'module': 'rover', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'customer-shipping-address': {'module': 'rover', 'class': 'ShippingAddress'}, 'cluster-workloads': {'module': 'rover', 'class': 'list[RoverWorkload]'}, 'freeform-tags': {'module': 'rover', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'rover', 'class': 'RoverCluster'})
@cli_util.wrap_exceptions
def update_rover_cluster(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, rover_cluster_id, display_name, cluster_size, customer_shipping_address, cluster_workloads, super_user_password, lifecycle_state, lifecycle_state_details, unlock_passphrase, enclosure_type, point_of_contact, point_of_contact_phone_number, shipping_preference, oracle_shipping_tracking_url, subscription_id, shipping_vendor, time_pickup_expected, is_import_requested, import_compartment_id, import_file_bucket, data_validation_code, freeform_tags, defined_tags, system_tags, if_match):

    if isinstance(rover_cluster_id, six.string_types) and len(rover_cluster_id.strip()) == 0:
        raise click.UsageError('Parameter --rover-cluster-id cannot be whitespace or empty string')
    if not force:
        if customer_shipping_address or cluster_workloads or freeform_tags or defined_tags or system_tags:
            if not click.confirm("WARNING: Updates to customer-shipping-address and cluster-workloads and freeform-tags and defined-tags and system-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if cluster_size is not None:
        _details['clusterSize'] = cluster_size

    if customer_shipping_address is not None:
        _details['customerShippingAddress'] = cli_util.parse_json_parameter("customer_shipping_address", customer_shipping_address)

    if cluster_workloads is not None:
        _details['clusterWorkloads'] = cli_util.parse_json_parameter("cluster_workloads", cluster_workloads)

    if super_user_password is not None:
        _details['superUserPassword'] = super_user_password

    if lifecycle_state is not None:
        _details['lifecycleState'] = lifecycle_state

    if lifecycle_state_details is not None:
        _details['lifecycleStateDetails'] = lifecycle_state_details

    if unlock_passphrase is not None:
        _details['unlockPassphrase'] = unlock_passphrase

    if enclosure_type is not None:
        _details['enclosureType'] = enclosure_type

    if point_of_contact is not None:
        _details['pointOfContact'] = point_of_contact

    if point_of_contact_phone_number is not None:
        _details['pointOfContactPhoneNumber'] = point_of_contact_phone_number

    if shipping_preference is not None:
        _details['shippingPreference'] = shipping_preference

    if oracle_shipping_tracking_url is not None:
        _details['oracleShippingTrackingUrl'] = oracle_shipping_tracking_url

    if subscription_id is not None:
        _details['subscriptionId'] = subscription_id

    if shipping_vendor is not None:
        _details['shippingVendor'] = shipping_vendor

    if time_pickup_expected is not None:
        _details['timePickupExpected'] = time_pickup_expected

    if is_import_requested is not None:
        _details['isImportRequested'] = is_import_requested

    if import_compartment_id is not None:
        _details['importCompartmentId'] = import_compartment_id

    if import_file_bucket is not None:
        _details['importFileBucket'] = import_file_bucket

    if data_validation_code is not None:
        _details['dataValidationCode'] = data_validation_code

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if system_tags is not None:
        _details['systemTags'] = cli_util.parse_json_parameter("system_tags", system_tags)

    client = cli_util.build_client('rover', 'rover_cluster', ctx)
    result = client.update_rover_cluster(
        rover_cluster_id=rover_cluster_id,
        update_rover_cluster_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_rover_cluster') and callable(getattr(client, 'get_rover_cluster')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_rover_cluster(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
