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
from services.ocvp.src.oci_cli_ocvp.generated import ocvs_service_cli


@click.command(cli_util.override('esxi_host.esxi_host_root_group.command_name', 'esxi-host'), cls=CommandGroupWithAlias, help=cli_util.override('esxi_host.esxi_host_root_group.help', """Use the Oracle Cloud VMware API to create SDDCs and manage ESXi hosts and software.
For more information, see [Oracle Cloud VMware Solution]."""), short_help=cli_util.override('esxi_host.esxi_host_root_group.short_help', """Oracle Cloud VMware Solution API"""))
@cli_util.help_option_group
def esxi_host_root_group():
    pass


@click.command(cli_util.override('esxi_host.esxi_host_group.command_name', 'esxi-host'), cls=CommandGroupWithAlias, help="""An ESXi host is a node in an SDDC. At a minimum, each SDDC has 3 ESXi hosts that are used to implement a functioning VMware environment.

In terms of implementation, an ESXi host is a Compute instance that is configured with the chosen bundle of VMware software.

Notice that an `EsxiHost` object has its own OCID (`id`), and a separate attribute for the OCID of the Compute instance (`computeInstanceId`).""")
@cli_util.help_option_group
def esxi_host_group():
    pass


@click.command(cli_util.override('esxi_host.esxi_host_summary_group.command_name', 'esxi-host-summary'), cls=CommandGroupWithAlias, help="""A summary of the ESXi host.""")
@cli_util.help_option_group
def esxi_host_summary_group():
    pass


ocvs_service_cli.ocvs_service_group.add_command(esxi_host_root_group)
esxi_host_root_group.add_command(esxi_host_group)
esxi_host_root_group.add_command(esxi_host_summary_group)


@esxi_host_group.command(name=cli_util.override('esxi_host.create_esxi_host.command_name', 'create'), help=u"""Adds another ESXi host to an existing SDDC. The attributes of the specified `Sddc` determine the VMware software and other configuration settings used by the ESXi host.

Use the [WorkRequest] operations to track the creation of the ESXi host. \n[Command Reference](createEsxiHost)""")
@cli_util.option('--sddc-id', required=True, help=u"""The [OCID] of the SDDC to add the ESXi host to.""")
@cli_util.option('--display-name', help=u"""A descriptive name for the ESXi host. It's changeable. Esxi Host name requirements are 1-16 character length limit, Must start with a letter, Must be English letters, numbers, - only, No repeating hyphens, Must be unique within the SDDC.

If this attribute is not specified, the SDDC's `instanceDisplayNamePrefix` attribute is used to name and incrementally number the ESXi host. For example, if you're creating the fourth ESXi host in the SDDC, and `instanceDisplayNamePrefix` is `MySDDC`, the host's display name is `MySDDC-4`.

Avoid entering confidential information.""")
@cli_util.option('--current-sku', type=custom_types.CliCaseInsensitiveChoice(["HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS"]), help=u"""The billing option currently used by the ESXi host. [ListSupportedSkus].""")
@cli_util.option('--next-sku', type=custom_types.CliCaseInsensitiveChoice(["HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS"]), help=u"""The billing option to switch to after the existing billing cycle ends. If `nextSku` is null or empty, `currentSku` continues to the next billing cycle. [ListSupportedSkus].""")
@cli_util.option('--compute-availability-domain', help=u"""The availability domain to create the ESXi host in. If keep empty, for AD-specific SDDC, new ESXi host will be created in the same availability domain; for multi-AD SDDC, new ESXi host will be auto assigned to the next availability domain following evenly distribution strategy.""")
@cli_util.option('--failed-esxi-host-id', help=u"""The [OCID] of the ESXi host that is failed. This is an optional parameter. If this parameter is specified, a new ESXi host will be created to replace the failed one, and the `failedEsxiHostId` field will be updated in the newly created Esxi host.""")
@cli_util.option('--host-shape-name', help=u"""The compute shape name of the ESXi host. [ListSupportedHostShapes].""")
@cli_util.option('--host-ocpu-count', type=click.FLOAT, help=u"""The OCPU count of the ESXi host.""")
@cli_util.option('--capacity-reservation-id', help=u"""The [OCID] of the Capacity Reservation.""")
@cli_util.option('--non-upgraded-esxi-host-id', help=u"""The [OCID] of the ESXi host that will be upgraded. This is an optional parameter. If this parameter is specified, an ESXi host with new version will be created to replace the original one, and the `nonUpgradedEsxiHostId` field will be updated in the newly created Esxi host.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'ocvp', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ocvp', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ocvp', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ocvp', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_esxi_host(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, sddc_id, display_name, current_sku, next_sku, compute_availability_domain, failed_esxi_host_id, host_shape_name, host_ocpu_count, capacity_reservation_id, non_upgraded_esxi_host_id, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['sddcId'] = sddc_id

    if display_name is not None:
        _details['displayName'] = display_name

    if current_sku is not None:
        _details['currentSku'] = current_sku

    if next_sku is not None:
        _details['nextSku'] = next_sku

    if compute_availability_domain is not None:
        _details['computeAvailabilityDomain'] = compute_availability_domain

    if failed_esxi_host_id is not None:
        _details['failedEsxiHostId'] = failed_esxi_host_id

    if host_shape_name is not None:
        _details['hostShapeName'] = host_shape_name

    if host_ocpu_count is not None:
        _details['hostOcpuCount'] = host_ocpu_count

    if capacity_reservation_id is not None:
        _details['capacityReservationId'] = capacity_reservation_id

    if non_upgraded_esxi_host_id is not None:
        _details['nonUpgradedEsxiHostId'] = non_upgraded_esxi_host_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('ocvp', 'esxi_host', ctx)
    result = client.create_esxi_host(
        create_esxi_host_details=_details,
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


@esxi_host_group.command(name=cli_util.override('esxi_host.delete_esxi_host.command_name', 'delete'), help=u"""Deletes the specified ESXi host. Before deleting the host, back up or migrate any VMware workloads running on it.

When you delete an ESXi host, Oracle does not remove the node configuration within the VMware environment itself. That is your responsibility.

**Note:** If you delete EXSi hosts from the SDDC to total less than 3, you are still billed for the 3 minimum recommended EXSi hosts. Also, you cannot add more VMware workloads to the SDDC until it again has at least 3 ESXi hosts.

Use the [WorkRequest] operations to track the deletion of the ESXi host. \n[Command Reference](deleteEsxiHost)""")
@cli_util.option('--esxi-host-id', required=True, help=u"""The [OCID] of the ESXi host.""")
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
def delete_esxi_host(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, esxi_host_id, if_match):

    if isinstance(esxi_host_id, six.string_types) and len(esxi_host_id.strip()) == 0:
        raise click.UsageError('Parameter --esxi-host-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ocvp', 'esxi_host', ctx)
    result = client.delete_esxi_host(
        esxi_host_id=esxi_host_id,
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


@esxi_host_group.command(name=cli_util.override('esxi_host.get_esxi_host.command_name', 'get'), help=u"""Gets the specified ESXi host's information. \n[Command Reference](getEsxiHost)""")
@cli_util.option('--esxi-host-id', required=True, help=u"""The [OCID] of the ESXi host.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ocvp', 'class': 'EsxiHost'})
@cli_util.wrap_exceptions
def get_esxi_host(ctx, from_json, esxi_host_id):

    if isinstance(esxi_host_id, six.string_types) and len(esxi_host_id.strip()) == 0:
        raise click.UsageError('Parameter --esxi-host-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ocvp', 'esxi_host', ctx)
    result = client.get_esxi_host(
        esxi_host_id=esxi_host_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@esxi_host_summary_group.command(name=cli_util.override('esxi_host.list_esxi_hosts.command_name', 'list-esxi-hosts'), help=u"""Lists the ESXi hosts in the specified SDDC. The list can be filtered by Compute instance OCID or ESXi display name.

Remember that in terms of implementation, an ESXi host is a Compute instance that is configured with the chosen bundle of VMware software. Each `EsxiHost` object has its own OCID (`id`), and a separate attribute for the OCID of the Compute instance (`computeInstanceId`). When filtering the list of ESXi hosts, you can specify the OCID of the Compute instance, not the ESXi host OCID. \n[Command Reference](listEsxiHosts)""")
@cli_util.option('--sddc-id', help=u"""The [OCID] of the SDDC.""")
@cli_util.option('--compute-instance-id', help=u"""The [OCID] of the Compute instance.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The lifecycle state of the resource.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ocvp', 'class': 'EsxiHostCollection'})
@cli_util.wrap_exceptions
def list_esxi_hosts(ctx, from_json, all_pages, page_size, sddc_id, compute_instance_id, display_name, limit, page, sort_order, sort_by, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if sddc_id is not None:
        kwargs['sddc_id'] = sddc_id
    if compute_instance_id is not None:
        kwargs['compute_instance_id'] = compute_instance_id
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
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ocvp', 'esxi_host', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_esxi_hosts,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_esxi_hosts,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_esxi_hosts(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@esxi_host_group.command(name=cli_util.override('esxi_host.update_esxi_host.command_name', 'update'), help=u"""Updates the specified ESXi host. \n[Command Reference](updateEsxiHost)""")
@cli_util.option('--esxi-host-id', required=True, help=u"""The [OCID] of the ESXi host.""")
@cli_util.option('--display-name', help=u"""A descriptive name for the ESXi host. It's changeable. Esxi Host name requirements are 1-16 character length limit, Must start with a letter, Must be English letters, numbers, - only, No repeating hyphens, Must be unique within the SDDC.

Avoid entering confidential information.""")
@cli_util.option('--next-sku', type=custom_types.CliCaseInsensitiveChoice(["HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS"]), help=u"""The billing option to switch to after the existing billing cycle ends. If `nextSku` is null or empty, `currentSku` continues to the next billing cycle. [ListSupportedSkus].""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'ocvp', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ocvp', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ocvp', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ocvp', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ocvp', 'class': 'EsxiHost'})
@cli_util.wrap_exceptions
def update_esxi_host(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, esxi_host_id, display_name, next_sku, freeform_tags, defined_tags, if_match):

    if isinstance(esxi_host_id, six.string_types) and len(esxi_host_id.strip()) == 0:
        raise click.UsageError('Parameter --esxi-host-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if next_sku is not None:
        _details['nextSku'] = next_sku

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('ocvp', 'esxi_host', ctx)
    result = client.update_esxi_host(
        esxi_host_id=esxi_host_id,
        update_esxi_host_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_esxi_host') and callable(getattr(client, 'get_esxi_host')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_esxi_host(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
