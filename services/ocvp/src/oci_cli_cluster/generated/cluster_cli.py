# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230701

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
from services.ocvp.src.oci_cli_ocvp.generated import ocvs_service_cli


@click.command(cli_util.override('cluster.cluster_root_group.command_name', 'cluster'), cls=CommandGroupWithAlias, help=cli_util.override('cluster.cluster_root_group.help', """Use the Oracle Cloud VMware API to create SDDCs and manage ESXi hosts and software.
For more information, see [Oracle Cloud VMware Solution]."""), short_help=cli_util.override('cluster.cluster_root_group.short_help', """Oracle Cloud VMware Solution API"""))
@cli_util.help_option_group
def cluster_root_group():
    pass


@click.command(cli_util.override('cluster.cluster_group.command_name', 'cluster'), cls=CommandGroupWithAlias, help="""An [Oracle Cloud VMware Solution] Cluster contains the resources required for a functional VMware environment. Instances in a Cluster (see [EsxiHost]) run in a virtual cloud network (VCN) and are preconfigured with VMware and storage. Use the vCenter utility to manage and deploy VMware virtual machines (VMs) in the Cluster.

The Cluster uses a single management subnet for provisioning the Cluster. It also uses a set of VLANs for various components of the VMware environment (vSphere, vMotion, vSAN, and so on). See the Core Services API for information about VCN subnets and VLANs.""")
@cli_util.help_option_group
def cluster_group():
    pass


@click.command(cli_util.override('cluster.cluster_summary_group.command_name', 'cluster-summary'), cls=CommandGroupWithAlias, help="""A summary of the Cluster.""")
@cli_util.help_option_group
def cluster_summary_group():
    pass


ocvs_service_cli.ocvs_service_group.add_command(cluster_root_group)
cluster_root_group.add_command(cluster_group)
cluster_root_group.add_command(cluster_summary_group)


@cluster_group.command(name=cli_util.override('cluster.create_cluster.command_name', 'create'), help=u"""Create a vSphere Cluster in software-defined data center (SDDC).

Use the [WorkRequest] operations to track the creation of the Cluster.

**Important:** You must configure the Cluster's networking resources with the security rules detailed in [Security Rules for Oracle Cloud VMware Solution SDDCs]. Otherwise, provisioning the SDDC will fail. The rules are based on the requirements set by VMware. \n[Command Reference](createCluster)""")
@cli_util.option('--sddc-id', required=True, help=u"""The [OCID] of the SDDC that the Cluster belongs to.""")
@cli_util.option('--compute-availability-domain', required=True, help=u"""The availability domain to create the Cluster's ESXi hosts in. For multi-AD Cluster deployment, set to `multi-AD`.""")
@cli_util.option('--esxi-hosts-count', required=True, type=click.INT, help=u"""The number of ESXi hosts to create in the Cluster. You can add more hosts later (see [CreateEsxiHost]).

**Note:** If you later delete EXSi hosts from a production Cluster to make SDDC total host count less than 3, you are still billed for the 3 minimum recommended ESXi hosts. Also, you cannot add more VMware workloads to the Cluster until the SDDC again has at least 3 ESXi hosts.""")
@cli_util.option('--network-configuration', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A descriptive name for the Cluster. Cluster name requirements are 1-16 character length limit, Must start with a letter, Must be English letters, numbers, - only, No repeating hyphens, Must be unique within the region. Avoid entering confidential information.""")
@cli_util.option('--instance-display-name-prefix', help=u"""A prefix used in the name of each ESXi host and Compute instance in the Cluster. If this isn't set, the Cluster's `displayName` is used as the prefix.

For example, if the value is `myCluster`, the ESXi hosts are named `myCluster-1`, `myCluster-2`, and so on.""")
@cli_util.option('--initial-commitment', type=custom_types.CliCaseInsensitiveChoice(["HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS"]), help=u"""The billing option selected during Cluster creation. [ListSupportedCommitments].""")
@cli_util.option('--workload-network-cidr', help=u"""The CIDR block for the IP addresses that VMware VMs in the Cluster use to run application workloads.""")
@cli_util.option('--initial-host-shape-name', help=u"""The initial compute shape of the Cluster's ESXi hosts. [ListSupportedHostShapes].""")
@cli_util.option('--initial-host-ocpu-count', type=click.FLOAT, help=u"""The initial OCPU count of the Cluster's ESXi hosts.""")
@cli_util.option('--is-shielded-instance-enabled', type=click.BOOL, help=u"""Indicates whether shielded instance is enabled for this Cluster.""")
@cli_util.option('--capacity-reservation-id', help=u"""The [OCID] of the Capacity Reservation.""")
@cli_util.option('--datastores', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of datastore info for the Cluster. This value is required only when `initialHostShapeName` is a standard shape.

This option is a JSON list with items of type DatastoreInfo.  For documentation on DatastoreInfo please see our API reference: https://docs.cloud.oracle.com/api/#/en/cluster/20230701/datatypes/DatastoreInfo.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vmware-software-version', help=u"""The VMware software bundle to install on the ESXi hosts in the Cluster. To get a list of the available versions, use [ListSupportedVmwareSoftwareVersions].""")
@cli_util.option('--esxi-software-version', help=u"""The ESXi software bundle to install on the ESXi hosts in the Cluster. Only versions under the same vmwareSoftwareVersion and have been validate by Oracle Cloud VMware Solution will be accepted. To get a list of the available versions, use [ListSupportedVmwareSoftwareVersions].""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'network-configuration': {'module': 'ocvp', 'class': 'NetworkConfiguration'}, 'datastores': {'module': 'ocvp', 'class': 'list[DatastoreInfo]'}, 'freeform-tags': {'module': 'ocvp', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ocvp', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'network-configuration': {'module': 'ocvp', 'class': 'NetworkConfiguration'}, 'datastores': {'module': 'ocvp', 'class': 'list[DatastoreInfo]'}, 'freeform-tags': {'module': 'ocvp', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ocvp', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_cluster(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, sddc_id, compute_availability_domain, esxi_hosts_count, network_configuration, display_name, instance_display_name_prefix, initial_commitment, workload_network_cidr, initial_host_shape_name, initial_host_ocpu_count, is_shielded_instance_enabled, capacity_reservation_id, datastores, vmware_software_version, esxi_software_version, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['sddcId'] = sddc_id
    _details['computeAvailabilityDomain'] = compute_availability_domain
    _details['esxiHostsCount'] = esxi_hosts_count
    _details['networkConfiguration'] = cli_util.parse_json_parameter("network_configuration", network_configuration)

    if display_name is not None:
        _details['displayName'] = display_name

    if instance_display_name_prefix is not None:
        _details['instanceDisplayNamePrefix'] = instance_display_name_prefix

    if initial_commitment is not None:
        _details['initialCommitment'] = initial_commitment

    if workload_network_cidr is not None:
        _details['workloadNetworkCidr'] = workload_network_cidr

    if initial_host_shape_name is not None:
        _details['initialHostShapeName'] = initial_host_shape_name

    if initial_host_ocpu_count is not None:
        _details['initialHostOcpuCount'] = initial_host_ocpu_count

    if is_shielded_instance_enabled is not None:
        _details['isShieldedInstanceEnabled'] = is_shielded_instance_enabled

    if capacity_reservation_id is not None:
        _details['capacityReservationId'] = capacity_reservation_id

    if datastores is not None:
        _details['datastores'] = cli_util.parse_json_parameter("datastores", datastores)

    if vmware_software_version is not None:
        _details['vmwareSoftwareVersion'] = vmware_software_version

    if esxi_software_version is not None:
        _details['esxiSoftwareVersion'] = esxi_software_version

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('ocvp', 'cluster', ctx)
    result = client.create_cluster(
        create_cluster_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds
                if 'opc-work-request-id' not in result.headers:
                    click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state')
                    cli_util.render_response(result, ctx)
                    return

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@cluster_group.command(name=cli_util.override('cluster.delete_cluster.command_name', 'delete'), help=u"""Deletes the specified Cluster, along with the other resources that were created with the Cluster. For example: the Compute instances, DNS records, and so on.

Use the [WorkRequest] operations to track the deletion of the Cluster. \n[Command Reference](deleteCluster)""")
@cli_util.option('--cluster-id', required=True, help=u"""The [OCID] of the SDDC Cluster.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_cluster(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, cluster_id, if_match):

    if isinstance(cluster_id, six.string_types) and len(cluster_id.strip()) == 0:
        raise click.UsageError('Parameter --cluster-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ocvp', 'cluster', ctx)
    result = client.delete_cluster(
        cluster_id=cluster_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds
                if 'opc-work-request-id' not in result.headers:
                    click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state')
                    cli_util.render_response(result, ctx)
                    return

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@cluster_group.command(name=cli_util.override('cluster.get_cluster.command_name', 'get'), help=u"""Gets the specified Cluster's information. \n[Command Reference](getCluster)""")
@cli_util.option('--cluster-id', required=True, help=u"""The [OCID] of the SDDC Cluster.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ocvp', 'class': 'Cluster'})
@cli_util.wrap_exceptions
def get_cluster(ctx, from_json, cluster_id):

    if isinstance(cluster_id, six.string_types) and len(cluster_id.strip()) == 0:
        raise click.UsageError('Parameter --cluster-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ocvp', 'cluster', ctx)
    result = client.get_cluster(
        cluster_id=cluster_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cluster_summary_group.command(name=cli_util.override('cluster.list_clusters.command_name', 'list-clusters'), help=u"""Lists the Clusters in the specified compartment. \n[Command Reference](listClusters)""")
@cli_util.option('--sddc-id', help=u"""The [OCID] of the SDDC.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The lifecycle state of the resource.""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment as optional parameter.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ocvp', 'class': 'ClusterCollection'})
@cli_util.wrap_exceptions
def list_clusters(ctx, from_json, all_pages, page_size, sddc_id, display_name, limit, page, sort_order, sort_by, lifecycle_state, compartment_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if sddc_id is not None:
        kwargs['sddc_id'] = sddc_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ocvp', 'cluster', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_clusters,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_clusters,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_clusters(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@cluster_group.command(name=cli_util.override('cluster.update_cluster.command_name', 'update'), help=u"""Updates the specified Cluster.

**Important:** Updating a Cluster affects only certain attributes in the `Cluster` object and does not affect the VMware environment currently running in the Cluster. \n[Command Reference](updateCluster)""")
@cli_util.option('--cluster-id', required=True, help=u"""The [OCID] of the SDDC Cluster.""")
@cli_util.option('--display-name', help=u"""The [OCID] of the Cluster. Cluster name requirements are 1-16 character length limit, Must start with a letter, Must be English letters, numbers, - only, No repeating hyphens, Must be unique within the region.""")
@cli_util.option('--network-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vmware-software-version', help=u"""The version of bundled VMware software that the Oracle Cloud VMware Solution will install on any new ESXi hosts that you add to this Cluster in the future. To get a list of the available versions, use [ListSupportedVmwareSoftwareVersions].""")
@cli_util.option('--esxi-software-version', help=u"""The version of bundled ESXi software that the Oracle Cloud VMware Solution will install on any new ESXi hosts that you add to this Cluster in the future unless a specific version is configured on the ESXi level. To get a list of the available versions, use [ListSupportedVmwareSoftwareVersions].""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'network-configuration': {'module': 'ocvp', 'class': 'NetworkConfiguration'}, 'freeform-tags': {'module': 'ocvp', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ocvp', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'network-configuration': {'module': 'ocvp', 'class': 'NetworkConfiguration'}, 'freeform-tags': {'module': 'ocvp', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ocvp', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ocvp', 'class': 'Cluster'})
@cli_util.wrap_exceptions
def update_cluster(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, cluster_id, display_name, network_configuration, vmware_software_version, esxi_software_version, freeform_tags, defined_tags, if_match):

    if isinstance(cluster_id, six.string_types) and len(cluster_id.strip()) == 0:
        raise click.UsageError('Parameter --cluster-id cannot be whitespace or empty string')
    if not force:
        if network_configuration or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to network-configuration and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if network_configuration is not None:
        _details['networkConfiguration'] = cli_util.parse_json_parameter("network_configuration", network_configuration)

    if vmware_software_version is not None:
        _details['vmwareSoftwareVersion'] = vmware_software_version

    if esxi_software_version is not None:
        _details['esxiSoftwareVersion'] = esxi_software_version

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('ocvp', 'cluster', ctx)
    result = client.update_cluster(
        cluster_id=cluster_id,
        update_cluster_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_cluster') and callable(getattr(client, 'get_cluster')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_cluster(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
