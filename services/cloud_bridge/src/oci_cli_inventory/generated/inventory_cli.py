# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
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
from services.cloud_bridge.src.oci_cli_cloud_bridge.generated import cloud_bridge_service_cli


@click.command(cli_util.override('inventory.inventory_root_group.command_name', 'inventory'), cls=CommandGroupWithAlias, help=cli_util.override('inventory.inventory_root_group.help', """API for Oracle Cloud Bridge service."""), short_help=cli_util.override('inventory.inventory_root_group.short_help', """Oracle Cloud Bridge API"""))
@cli_util.help_option_group
def inventory_root_group():
    pass


@click.command(cli_util.override('inventory.asset_collection_group.command_name', 'asset-collection'), cls=CommandGroupWithAlias, help="""Results of a set of asset summary.""")
@cli_util.help_option_group
def asset_collection_group():
    pass


@click.command(cli_util.override('inventory.asset_aggregation_group.command_name', 'asset-aggregation'), cls=CommandGroupWithAlias, help="""The result of an analytics aggregation on a set of assets.""")
@cli_util.help_option_group
def asset_aggregation_group():
    pass


@click.command(cli_util.override('inventory.asset_group.command_name', 'asset'), cls=CommandGroupWithAlias, help="""Description of an asset.""")
@cli_util.help_option_group
def asset_group():
    pass


@click.command(cli_util.override('inventory.inventory_group.command_name', 'inventory'), cls=CommandGroupWithAlias, help="""Description of inventory.""")
@cli_util.help_option_group
def inventory_group():
    pass


@click.command(cli_util.override('inventory.historical_metric_group.command_name', 'historical-metric'), cls=CommandGroupWithAlias, help="""Metric details.""")
@cli_util.help_option_group
def historical_metric_group():
    pass


cloud_bridge_service_cli.cloud_bridge_service_group.add_command(inventory_root_group)
inventory_root_group.add_command(asset_collection_group)
inventory_root_group.add_command(asset_aggregation_group)
inventory_root_group.add_command(asset_group)
inventory_root_group.add_command(inventory_group)
inventory_root_group.add_command(historical_metric_group)


@asset_aggregation_group.command(name=cli_util.override('inventory.analyze_assets.command_name', 'analyze-assets'), help=u"""Returns an aggregation of assets. Aggregation groups are sorted by groupBy property. Default sort order is ascending, but can be overridden by the sortOrder parameter. \n[Command Reference](analyzeAssets)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--aggregation-properties', required=True, multiple=True, help=u"""An array of properties on which to aggregate.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), help=u"""A filter to return only assets whose lifecycleState matches the given lifecycleState.""")
@cli_util.option('--source-key', help=u"""Source key from where the assets originate.""")
@cli_util.option('--external-asset-key', help=u"""External asset key.""")
@cli_util.option('--asset-type', type=custom_types.CliCaseInsensitiveChoice(["VMWARE_VM", "VM"]), help=u"""The type of asset.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--group-by', multiple=True, help=u"""The dimensions in which to group the aggregations.""")
@cli_util.option('--inventory-id', help=u"""Unique Inventory identifier.""")
@json_skeleton_utils.get_cli_json_input_option({'aggregation-properties': {'module': 'cloud_bridge', 'class': 'list[string]'}, 'group-by': {'module': 'cloud_bridge', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'aggregation-properties': {'module': 'cloud_bridge', 'class': 'list[string]'}, 'group-by': {'module': 'cloud_bridge', 'class': 'list[string]'}}, output_type={'module': 'cloud_bridge', 'class': 'AssetAggregationCollection'})
@cli_util.wrap_exceptions
def analyze_assets(ctx, from_json, compartment_id, aggregation_properties, limit, page, lifecycle_state, source_key, external_asset_key, asset_type, sort_order, group_by, inventory_id):

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if source_key is not None:
        kwargs['source_key'] = source_key
    if external_asset_key is not None:
        kwargs['external_asset_key'] = external_asset_key
    if asset_type is not None:
        kwargs['asset_type'] = asset_type
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if group_by is not None and len(group_by) > 0:
        kwargs['group_by'] = group_by
    if inventory_id is not None:
        kwargs['inventory_id'] = inventory_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_bridge', 'inventory', ctx)
    result = client.analyze_assets(
        compartment_id=compartment_id,
        aggregation_properties=aggregation_properties,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@asset_group.command(name=cli_util.override('inventory.change_asset_compartment.command_name', 'change-compartment'), help=u"""Moves an asset resource from one compartment to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeAssetCompartment)""")
@cli_util.option('--asset-id', required=True, help=u"""Unique asset identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_asset_compartment(ctx, from_json, asset_id, compartment_id, if_match):

    if isinstance(asset_id, six.string_types) and len(asset_id.strip()) == 0:
        raise click.UsageError('Parameter --asset-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('cloud_bridge', 'inventory', ctx)
    result = client.change_asset_compartment(
        asset_id=asset_id,
        change_asset_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@asset_group.command(name=cli_util.override('inventory.change_asset_tags.command_name', 'change-asset-tags'), help=u"""Change an asset's tag. \n[Command Reference](changeAssetTags)""")
@cli_util.option('--asset-id', required=True, help=u"""Unique asset identifier.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'cloud_bridge', 'class': 'Asset'})
@cli_util.wrap_exceptions
def change_asset_tags(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, asset_id, freeform_tags, defined_tags, if_match):

    if isinstance(asset_id, six.string_types) and len(asset_id.strip()) == 0:
        raise click.UsageError('Parameter --asset-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('cloud_bridge', 'inventory', ctx)
    result = client.change_asset_tags(
        asset_id=asset_id,
        change_asset_tags_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_asset') and callable(getattr(client, 'get_asset')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_asset(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@asset_group.command(name=cli_util.override('inventory.create_asset.command_name', 'create'), help=u"""Creates an asset. \n[Command Reference](createAsset)""")
@cli_util.option('--inventory-id', required=True, help=u"""Inventory ID to which an asset belongs.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment that the asset belongs to.""")
@cli_util.option('--source-key', required=True, help=u"""The source key to which the asset belongs.""")
@cli_util.option('--external-asset-key', required=True, help=u"""The key of the asset from the external environment.""")
@cli_util.option('--asset-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["VMWARE_VM", "VM"]), help=u"""The type of asset.""")
@cli_util.option('--display-name', help=u"""Asset display name.""")
@cli_util.option('--asset-source-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of asset source OCID.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'asset-source-ids': {'module': 'cloud_bridge', 'class': 'list[string]'}, 'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'asset-source-ids': {'module': 'cloud_bridge', 'class': 'list[string]'}, 'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'cloud_bridge', 'class': 'Asset'})
@cli_util.wrap_exceptions
def create_asset(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, inventory_id, compartment_id, source_key, external_asset_key, asset_type, display_name, asset_source_ids, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['inventoryId'] = inventory_id
    _details['compartmentId'] = compartment_id
    _details['sourceKey'] = source_key
    _details['externalAssetKey'] = external_asset_key
    _details['assetType'] = asset_type

    if display_name is not None:
        _details['displayName'] = display_name

    if asset_source_ids is not None:
        _details['assetSourceIds'] = cli_util.parse_json_parameter("asset_source_ids", asset_source_ids)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('cloud_bridge', 'inventory', ctx)
    result = client.create_asset(
        create_asset_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_asset') and callable(getattr(client, 'get_asset')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_asset(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@asset_group.command(name=cli_util.override('inventory.create_asset_create_vmware_vm_asset_details.command_name', 'create-asset-create-vmware-vm-asset-details'), help=u"""Creates an asset. \n[Command Reference](createAsset)""")
@cli_util.option('--inventory-id', required=True, help=u"""Inventory ID to which an asset belongs.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment that the asset belongs to.""")
@cli_util.option('--source-key', required=True, help=u"""The source key to which the asset belongs.""")
@cli_util.option('--external-asset-key', required=True, help=u"""The key of the asset from the external environment.""")
@cli_util.option('--display-name', help=u"""Asset display name.""")
@cli_util.option('--asset-source-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of asset source OCID.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compute', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vm', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vmware-vm', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vmware-v-center', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'asset-source-ids': {'module': 'cloud_bridge', 'class': 'list[string]'}, 'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}, 'compute': {'module': 'cloud_bridge', 'class': 'ComputeProperties'}, 'vm': {'module': 'cloud_bridge', 'class': 'VmProperties'}, 'vmware-vm': {'module': 'cloud_bridge', 'class': 'VmwareVmProperties'}, 'vmware-v-center': {'module': 'cloud_bridge', 'class': 'VmwareVCenterProperties'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'asset-source-ids': {'module': 'cloud_bridge', 'class': 'list[string]'}, 'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}, 'compute': {'module': 'cloud_bridge', 'class': 'ComputeProperties'}, 'vm': {'module': 'cloud_bridge', 'class': 'VmProperties'}, 'vmware-vm': {'module': 'cloud_bridge', 'class': 'VmwareVmProperties'}, 'vmware-v-center': {'module': 'cloud_bridge', 'class': 'VmwareVCenterProperties'}}, output_type={'module': 'cloud_bridge', 'class': 'Asset'})
@cli_util.wrap_exceptions
def create_asset_create_vmware_vm_asset_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, inventory_id, compartment_id, source_key, external_asset_key, display_name, asset_source_ids, freeform_tags, defined_tags, compute, vm, vmware_vm, vmware_v_center):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['inventoryId'] = inventory_id
    _details['compartmentId'] = compartment_id
    _details['sourceKey'] = source_key
    _details['externalAssetKey'] = external_asset_key

    if display_name is not None:
        _details['displayName'] = display_name

    if asset_source_ids is not None:
        _details['assetSourceIds'] = cli_util.parse_json_parameter("asset_source_ids", asset_source_ids)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if compute is not None:
        _details['compute'] = cli_util.parse_json_parameter("compute", compute)

    if vm is not None:
        _details['vm'] = cli_util.parse_json_parameter("vm", vm)

    if vmware_vm is not None:
        _details['vmwareVm'] = cli_util.parse_json_parameter("vmware_vm", vmware_vm)

    if vmware_v_center is not None:
        _details['vmwareVCenter'] = cli_util.parse_json_parameter("vmware_v_center", vmware_v_center)

    _details['assetType'] = 'VMWARE_VM'

    client = cli_util.build_client('cloud_bridge', 'inventory', ctx)
    result = client.create_asset(
        create_asset_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_asset') and callable(getattr(client, 'get_asset')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_asset(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@inventory_group.command(name=cli_util.override('inventory.create_inventory.command_name', 'create'), help=u"""Creates an inventory. \n[Command Reference](createInventory)""")
@cli_util.option('--display-name', required=True, help=u"""Inventory displayName.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the tenantId.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_inventory(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('cloud_bridge', 'inventory', ctx)
    result = client.create_inventory(
        create_inventory_details=_details,
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


@asset_group.command(name=cli_util.override('inventory.delete_asset.command_name', 'delete'), help=u"""Deletes an asset resource by identifier. \n[Command Reference](deleteAsset)""")
@cli_util.option('--asset-id', required=True, help=u"""Unique asset identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_asset(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, asset_id, if_match):

    if isinstance(asset_id, six.string_types) and len(asset_id.strip()) == 0:
        raise click.UsageError('Parameter --asset-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_bridge', 'inventory', ctx)
    result = client.delete_asset(
        asset_id=asset_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_asset') and callable(getattr(client, 'get_asset')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_asset(asset_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@inventory_group.command(name=cli_util.override('inventory.delete_inventory.command_name', 'delete'), help=u"""Deletes an inventory resource by identifier. \n[Command Reference](deleteInventory)""")
@cli_util.option('--inventory-id', required=True, help=u"""Inventory OCID.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_inventory(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, inventory_id, if_match):

    if isinstance(inventory_id, six.string_types) and len(inventory_id.strip()) == 0:
        raise click.UsageError('Parameter --inventory-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_bridge', 'inventory', ctx)
    result = client.delete_inventory(
        inventory_id=inventory_id,
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


@asset_group.command(name=cli_util.override('inventory.get_asset.command_name', 'get'), help=u"""Gets an asset by identifier. \n[Command Reference](getAsset)""")
@cli_util.option('--asset-id', required=True, help=u"""Unique asset identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_bridge', 'class': 'Asset'})
@cli_util.wrap_exceptions
def get_asset(ctx, from_json, asset_id):

    if isinstance(asset_id, six.string_types) and len(asset_id.strip()) == 0:
        raise click.UsageError('Parameter --asset-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_bridge', 'inventory', ctx)
    result = client.get_asset(
        asset_id=asset_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@inventory_group.command(name=cli_util.override('inventory.get_inventory.command_name', 'get'), help=u"""Gets an inventory by identifier. \n[Command Reference](getInventory)""")
@cli_util.option('--inventory-id', required=True, help=u"""Inventory OCID.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_bridge', 'class': 'Inventory'})
@cli_util.wrap_exceptions
def get_inventory(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, inventory_id):

    if isinstance(inventory_id, six.string_types) and len(inventory_id.strip()) == 0:
        raise click.UsageError('Parameter --inventory-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_bridge', 'inventory', ctx)
    result = client.get_inventory(
        inventory_id=inventory_id,
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


@inventory_group.command(name=cli_util.override('inventory.import_inventory.command_name', 'import'), help=u"""Import resources in inventory. \n[Command Reference](importInventory)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartmentId that resources import.""")
@cli_util.option('--inventory-id', required=True, help=u"""Inventory OCID.""")
@cli_util.option('--resource-type', type=custom_types.CliCaseInsensitiveChoice(["ASSET"]), help=u"""Import inventory resource type.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def import_inventory(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, inventory_id, resource_type, freeform_tags, defined_tags):

    if isinstance(inventory_id, six.string_types) and len(inventory_id.strip()) == 0:
        raise click.UsageError('Parameter --inventory-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    if resource_type is not None:
        _details['resourceType'] = resource_type

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('cloud_bridge', 'inventory', ctx)
    result = client.import_inventory(
        inventory_id=inventory_id,
        import_inventory_details=_details,
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


@inventory_group.command(name=cli_util.override('inventory.import_inventory_import_inventory_via_assets_details.command_name', 'import-inventory-import-inventory-via-assets-details'), help=u"""Import resources in inventory. \n[Command Reference](importInventory)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartmentId that resources import.""")
@cli_util.option('--inventory-id', required=True, help=u"""Inventory OCID.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data', help=u"""The file body to be sent in the request.""")
@cli_util.option('--asset-type', type=custom_types.CliCaseInsensitiveChoice(["VMWARE_VM", "VM"]), help=u"""The type of asset.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def import_inventory_import_inventory_via_assets_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, inventory_id, freeform_tags, defined_tags, data, asset_type):

    if isinstance(inventory_id, six.string_types) and len(inventory_id.strip()) == 0:
        raise click.UsageError('Parameter --inventory-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if data is not None:
        _details['data'] = data

    if asset_type is not None:
        _details['assetType'] = asset_type

    _details['resourceType'] = 'ASSET'

    client = cli_util.build_client('cloud_bridge', 'inventory', ctx)
    result = client.import_inventory(
        inventory_id=inventory_id,
        import_inventory_details=_details,
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


@asset_collection_group.command(name=cli_util.override('inventory.list_assets.command_name', 'list-assets'), help=u"""Returns a list of assets. \n[Command Reference](listAssets)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), help=u"""A filter to return only assets whose lifecycleState matches the given lifecycleState.""")
@cli_util.option('--source-key', help=u"""Source key from where the assets originate.""")
@cli_util.option('--external-asset-key', help=u"""External asset key.""")
@cli_util.option('--asset-type', type=custom_types.CliCaseInsensitiveChoice(["VMWARE_VM", "VM"]), help=u"""The type of asset.""")
@cli_util.option('--asset-id', help=u"""Unique asset identifier.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "timeUpdated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--inventory-id', help=u"""Unique Inventory identifier.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_bridge', 'class': 'AssetCollection'})
@cli_util.wrap_exceptions
def list_assets(ctx, from_json, all_pages, page_size, compartment_id, limit, page, lifecycle_state, source_key, external_asset_key, asset_type, asset_id, display_name, sort_order, sort_by, inventory_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if source_key is not None:
        kwargs['source_key'] = source_key
    if external_asset_key is not None:
        kwargs['external_asset_key'] = external_asset_key
    if asset_type is not None:
        kwargs['asset_type'] = asset_type
    if asset_id is not None:
        kwargs['asset_id'] = asset_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if inventory_id is not None:
        kwargs['inventory_id'] = inventory_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_bridge', 'inventory', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_assets,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_assets,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_assets(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@historical_metric_group.command(name=cli_util.override('inventory.list_historical_metrics.command_name', 'list'), help=u"""List asset historical metrics. \n[Command Reference](listHistoricalMetrics)""")
@cli_util.option('--asset-id', required=True, help=u"""Unique asset identifier.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "timeUpdated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_bridge', 'class': 'HistoricalMetricCollection'})
@cli_util.wrap_exceptions
def list_historical_metrics(ctx, from_json, all_pages, page_size, asset_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(asset_id, six.string_types) and len(asset_id.strip()) == 0:
        raise click.UsageError('Parameter --asset-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_bridge', 'inventory', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_historical_metrics,
            asset_id=asset_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_historical_metrics,
            limit,
            page_size,
            asset_id=asset_id,
            **kwargs
        )
    else:
        result = client.list_historical_metrics(
            asset_id=asset_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@inventory_group.command(name=cli_util.override('inventory.list_inventories.command_name', 'list'), help=u"""Returns a list of inventories. \n[Command Reference](listInventories)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "timeUpdated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED", "DELETING", "CREATING", "FAILED"]), help=u"""A filter to return inventory if the lifecycleState matches the given lifecycleState.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_bridge', 'class': 'InventoryCollection'})
@cli_util.wrap_exceptions
def list_inventories(ctx, from_json, all_pages, page_size, compartment_id, sort_order, sort_by, limit, page, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_bridge', 'inventory', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_inventories,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_inventories,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_inventories(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@historical_metric_group.command(name=cli_util.override('inventory.submit_historical_metrics.command_name', 'submit'), help=u"""Creates or updates all metrics related to the asset. \n[Command Reference](submitHistoricalMetrics)""")
@cli_util.option('--historical-metrics', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of asset historical metrics.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--asset-id', required=True, help=u"""Unique asset identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'historical-metrics': {'module': 'cloud_bridge', 'class': 'list[HistoricalMetric]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'historical-metrics': {'module': 'cloud_bridge', 'class': 'list[HistoricalMetric]'}}, output_type={'module': 'cloud_bridge', 'class': 'HistoricalMetricCollection'})
@cli_util.wrap_exceptions
def submit_historical_metrics(ctx, from_json, historical_metrics, asset_id, if_match):

    if isinstance(asset_id, six.string_types) and len(asset_id.strip()) == 0:
        raise click.UsageError('Parameter --asset-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['historicalMetrics'] = cli_util.parse_json_parameter("historical_metrics", historical_metrics)

    client = cli_util.build_client('cloud_bridge', 'inventory', ctx)
    result = client.submit_historical_metrics(
        asset_id=asset_id,
        submit_historical_metrics_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@asset_group.command(name=cli_util.override('inventory.update_asset.command_name', 'update'), help=u"""Updates the asset. \n[Command Reference](updateAsset)""")
@cli_util.option('--asset-id', required=True, help=u"""Unique asset identifier.""")
@cli_util.option('--asset-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["VMWARE_VM", "VM"]), help=u"""Asset type""")
@cli_util.option('--display-name', help=u"""Asset display name.""")
@cli_util.option('--asset-source-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of asset source OCID.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'asset-source-ids': {'module': 'cloud_bridge', 'class': 'list[string]'}, 'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'asset-source-ids': {'module': 'cloud_bridge', 'class': 'list[string]'}, 'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'cloud_bridge', 'class': 'Asset'})
@cli_util.wrap_exceptions
def update_asset(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, asset_id, asset_type, display_name, asset_source_ids, freeform_tags, defined_tags, if_match):

    if isinstance(asset_id, six.string_types) and len(asset_id.strip()) == 0:
        raise click.UsageError('Parameter --asset-id cannot be whitespace or empty string')
    if not force:
        if asset_source_ids or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to asset-source-ids and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['assetType'] = asset_type

    if display_name is not None:
        _details['displayName'] = display_name

    if asset_source_ids is not None:
        _details['assetSourceIds'] = cli_util.parse_json_parameter("asset_source_ids", asset_source_ids)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('cloud_bridge', 'inventory', ctx)
    result = client.update_asset(
        asset_id=asset_id,
        update_asset_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_asset') and callable(getattr(client, 'get_asset')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_asset(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@asset_group.command(name=cli_util.override('inventory.update_asset_update_vm_asset_details.command_name', 'update-asset-update-vm-asset-details'), help=u"""Updates the asset. \n[Command Reference](updateAsset)""")
@cli_util.option('--asset-id', required=True, help=u"""Unique asset identifier.""")
@cli_util.option('--display-name', help=u"""Asset display name.""")
@cli_util.option('--asset-source-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of asset source OCID.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'asset-source-ids': {'module': 'cloud_bridge', 'class': 'list[string]'}, 'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'asset-source-ids': {'module': 'cloud_bridge', 'class': 'list[string]'}, 'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'cloud_bridge', 'class': 'Asset'})
@cli_util.wrap_exceptions
def update_asset_update_vm_asset_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, asset_id, display_name, asset_source_ids, freeform_tags, defined_tags, if_match):

    if isinstance(asset_id, six.string_types) and len(asset_id.strip()) == 0:
        raise click.UsageError('Parameter --asset-id cannot be whitespace or empty string')
    if not force:
        if asset_source_ids or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to asset-source-ids and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if asset_source_ids is not None:
        _details['assetSourceIds'] = cli_util.parse_json_parameter("asset_source_ids", asset_source_ids)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['assetType'] = 'VM'

    client = cli_util.build_client('cloud_bridge', 'inventory', ctx)
    result = client.update_asset(
        asset_id=asset_id,
        update_asset_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_asset') and callable(getattr(client, 'get_asset')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_asset(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@asset_group.command(name=cli_util.override('inventory.update_asset_update_vmware_vm_asset_details.command_name', 'update-asset-update-vmware-vm-asset-details'), help=u"""Updates the asset. \n[Command Reference](updateAsset)""")
@cli_util.option('--asset-id', required=True, help=u"""Unique asset identifier.""")
@cli_util.option('--display-name', help=u"""Asset display name.""")
@cli_util.option('--asset-source-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of asset source OCID.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compute', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vm', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vmware-vm', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vmware-v-center', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'asset-source-ids': {'module': 'cloud_bridge', 'class': 'list[string]'}, 'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}, 'compute': {'module': 'cloud_bridge', 'class': 'ComputeProperties'}, 'vm': {'module': 'cloud_bridge', 'class': 'VmProperties'}, 'vmware-vm': {'module': 'cloud_bridge', 'class': 'VmwareVmProperties'}, 'vmware-v-center': {'module': 'cloud_bridge', 'class': 'VmwareVCenterProperties'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'asset-source-ids': {'module': 'cloud_bridge', 'class': 'list[string]'}, 'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}, 'compute': {'module': 'cloud_bridge', 'class': 'ComputeProperties'}, 'vm': {'module': 'cloud_bridge', 'class': 'VmProperties'}, 'vmware-vm': {'module': 'cloud_bridge', 'class': 'VmwareVmProperties'}, 'vmware-v-center': {'module': 'cloud_bridge', 'class': 'VmwareVCenterProperties'}}, output_type={'module': 'cloud_bridge', 'class': 'Asset'})
@cli_util.wrap_exceptions
def update_asset_update_vmware_vm_asset_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, asset_id, display_name, asset_source_ids, freeform_tags, defined_tags, compute, vm, vmware_vm, vmware_v_center, if_match):

    if isinstance(asset_id, six.string_types) and len(asset_id.strip()) == 0:
        raise click.UsageError('Parameter --asset-id cannot be whitespace or empty string')
    if not force:
        if asset_source_ids or freeform_tags or defined_tags or compute or vm or vmware_vm or vmware_v_center:
            if not click.confirm("WARNING: Updates to asset-source-ids and freeform-tags and defined-tags and compute and vm and vmware-vm and vmware-v-center will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if asset_source_ids is not None:
        _details['assetSourceIds'] = cli_util.parse_json_parameter("asset_source_ids", asset_source_ids)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if compute is not None:
        _details['compute'] = cli_util.parse_json_parameter("compute", compute)

    if vm is not None:
        _details['vm'] = cli_util.parse_json_parameter("vm", vm)

    if vmware_vm is not None:
        _details['vmwareVm'] = cli_util.parse_json_parameter("vmware_vm", vmware_vm)

    if vmware_v_center is not None:
        _details['vmwareVCenter'] = cli_util.parse_json_parameter("vmware_v_center", vmware_v_center)

    _details['assetType'] = 'VMWARE_VM'

    client = cli_util.build_client('cloud_bridge', 'inventory', ctx)
    result = client.update_asset(
        asset_id=asset_id,
        update_asset_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_asset') and callable(getattr(client, 'get_asset')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_asset(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@inventory_group.command(name=cli_util.override('inventory.update_inventory.command_name', 'update'), help=u"""Updates an inventory. \n[Command Reference](updateInventory)""")
@cli_util.option('--inventory-id', required=True, help=u"""Inventory OCID.""")
@cli_util.option('--display-name', help=u"""Inventory displayName.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED", "DELETING", "CREATING", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'cloud_bridge', 'class': 'Inventory'})
@cli_util.wrap_exceptions
def update_inventory(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, inventory_id, display_name, freeform_tags, defined_tags, if_match):

    if isinstance(inventory_id, six.string_types) and len(inventory_id.strip()) == 0:
        raise click.UsageError('Parameter --inventory-id cannot be whitespace or empty string')
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

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('cloud_bridge', 'inventory', ctx)
    result = client.update_inventory(
        inventory_id=inventory_id,
        update_inventory_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_inventory') and callable(getattr(client, 'get_inventory')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_inventory(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
