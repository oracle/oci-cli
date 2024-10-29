# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
import click  # noqa: F401
import json  # noqa: F401
from services.cloud_bridge.src.oci_cli_inventory.generated import inventory_cli

from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401

# oci cloud-bridge inventory asset create-asset-create-vmware-vm-asset-details -> oci cloud-bridge inventory asset
# create-vmware-vm
cli_util.rename_command(inventory_cli, inventory_cli.asset_group,
                        inventory_cli.create_asset_create_vmware_vm_asset_details, "create-vmware-vm")

# oci cloud-bridge inventory asset update-asset-update-vm-asset-details
# -> oci cloud-bridge inventory asset update-vm-asset
cli_util.rename_command(inventory_cli, inventory_cli.asset_group, inventory_cli.update_asset_update_vm_asset_details,
                        "update-vm")

# oci cloud-bridge inventory asset update-asset-update-vmware-vm-asset-details ->
# oci cloud-bridge inventory asset update-vmware-vm
cli_util.rename_command(inventory_cli, inventory_cli.asset_group,
                        inventory_cli.update_asset_update_vmware_vm_asset_details, "update-vmware-vm")

# oci cloud-bridge inventory inventory import-inventory-import-inventory-via-assets-details ->
# oci cloud-bridge inventory inventory import-inventory-via-assets
cli_util.rename_command(inventory_cli, inventory_cli.inventory_group,
                        inventory_cli.import_inventory_import_inventory_via_assets_details,
                        "import-inventory-via-assets")

inventory_cli.inventory_root_group.commands.pop(inventory_cli.asset_collection_group.name)
inventory_cli.asset_group.add_command(inventory_cli.list_assets)
cli_util.rename_command(inventory_cli, inventory_cli.asset_group, inventory_cli.list_assets, "list")

cli_util.rename_command(inventory_cli, inventory_cli.asset_group, inventory_cli.change_asset_tags, "change-tags")

cli_util.rename_command(inventory_cli, inventory_cli.inventory_group,
                        inventory_cli.import_inventory_import_inventory_via_assets_details, "import-via-assets")

# Consolidate the polymorphic CLI commands for create
inventory_cli.asset_group.commands.pop(inventory_cli.create_asset.name)
inventory_cli.asset_group.commands.pop(inventory_cli.create_asset_create_vmware_vm_asset_details.name)
inventory_cli.asset_group.commands.pop(inventory_cli.update_asset.name)
inventory_cli.asset_group.commands.pop(inventory_cli.update_asset_update_vm_asset_details.name)
inventory_cli.asset_group.commands.pop(inventory_cli.update_asset_update_vmware_vm_asset_details.name)


@cli_util.copy_params_from_generated_command(inventory_cli.create_asset, params_to_exclude=[''])
@cli_util.option('--compute', type=custom_types.CLI_COMPLEX_TYPE,
                 help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vm', type=custom_types.CLI_COMPLEX_TYPE,
                 help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vmware-vm', type=custom_types.CLI_COMPLEX_TYPE,
                 help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vmware-v-center', type=custom_types.CLI_COMPLEX_TYPE,
                 help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--aws-ebs', type=custom_types.CLI_COMPLEX_TYPE,
                 help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--aws-ec2', type=custom_types.CLI_COMPLEX_TYPE,
                 help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--aws-ec2-cost', type=custom_types.CLI_COMPLEX_TYPE,
                 help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--attached-ebs-volumes-cost', type=custom_types.CLI_COMPLEX_TYPE,
                 help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@inventory_cli.asset_group.command(
    name=cli_util.override(
        'inventory.create_asset.command_name',
        'create'),
    help=u"""Creates an asset. \n[Command Reference](createAsset)""")
@json_skeleton_utils.get_cli_json_input_option({
    'asset-source-ids': {
        'module': 'cloud_bridge',
        'class': 'list[string]'},
    'freeform-tags': {
        'module': 'cloud_bridge',
        'class': 'dict(str, string)'},
    'defined-tags': {
        'module': 'cloud_bridge',
        'class': 'dict(str, dict(str, object))'},
    'compute': {
        'module': 'cloud_bridge',
        'class': 'ComputeProperties'},
    'vm': {
        'module': 'cloud_bridge',
        'class': 'VmProperties'},
    'vmware-vm': {
        'module': 'cloud_bridge',
        'class': 'VmwareVmProperties'},
    'vmware-v-center': {
        'module': 'cloud_bridge',
        'class': 'VmwareVCenterProperties'},
    'aws-ebs': {
        'module': 'cloud_bridge',
        'class': 'AwsEbsProperties'},
    'aws-ec2': {
        'module': 'cloud_bridge',
        'class': 'AwsEc2Properties'},
    'aws-ec2-cost': {
        'module': 'cloud_bridge',
        'class': 'MonthlyCostSummary'},
    'attached-ebs-volumes-cost': {
        'module': 'cloud_bridge',
        'class': 'MonthlyCostSummary'}})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'asset-source-ids': {'module': 'cloud_bridge',
                             'class': 'list[string]'},
        'freeform-tags': {'module': 'cloud_bridge',
                          'class': 'dict(str, string)'},
        'defined-tags': {'module': 'cloud_bridge',
                         'class': 'dict(str, dict(str, object))'},
        'compute': {'module': 'cloud_bridge',
                    'class': 'ComputeProperties'},
        'vm': {'module': 'cloud_bridge',
               'class': 'VmProperties'},
        'vmware-vm': {'module': 'cloud_bridge',
                      'class': 'VmwareVmProperties'},
        'vmware-v-center': {'module': 'cloud_bridge',
                            'class': 'VmwareVCenterProperties'},
        'aws-ebs': {'module': 'cloud_bridge',
                    'class': 'AwsEbsProperties'},
        'aws-ec2': {'module': 'cloud_bridge',
                    'class': 'AwsEc2Properties'},
        'aws-ec2-cost': {'module': 'cloud_bridge',
                         'class': 'MonthlyCostSummary'},
        'attached-ebs-volumes-cost': {'module': 'cloud_bridge',
                                      'class': 'MonthlyCostSummary'}},
    output_type={'module': 'cloud_bridge',
                 'class': 'Asset'})
@cli_util.wrap_exceptions
def create_asset(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, inventory_id, compartment_id,
                 source_key, external_asset_key, asset_type, display_name, asset_source_ids, freeform_tags,
                 defined_tags, compute, vm, vmware_vm, vmware_v_center,
                 aws_ebs, aws_ec2, aws_ec2_cost, attached_ebs_volumes_cost):
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

    if compute is not None:
        _details['compute'] = cli_util.parse_json_parameter("compute", compute)

    if vm is not None:
        _details['vm'] = cli_util.parse_json_parameter("vm", vm)

    if vmware_vm is not None:
        _details['vmwareVm'] = cli_util.parse_json_parameter("vmware_vm", vmware_vm)

    if vmware_v_center is not None:
        _details['vmwareVCenter'] = cli_util.parse_json_parameter("vmware_v_center", vmware_v_center)

    if aws_ebs is not None:
        _details['awsEbs'] = cli_util.parse_json_parameter("aws_ebs", aws_ebs)

    if aws_ec2 is not None:
        _details['awsEc2'] = cli_util.parse_json_parameter("aws_ec2", aws_ec2)

    if aws_ec2_cost is not None:
        _details['awsEc2Cost'] = cli_util.parse_json_parameter("aws_ec2_cost", aws_ec2_cost)

    if attached_ebs_volumes_cost is not None:
        _details['attachedEbsVolumesCost'] = cli_util.parse_json_parameter("attached_ebs_volumes_cost", attached_ebs_volumes_cost)

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

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state),
                           file=sys.stderr)
                result = oci.wait_until(client, client.get_asset(result.data.id), 'lifecycle_state', wait_for_state,
                                        **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo(
                    'Failed to wait until the resource entered the specified state. Outputting last known resource state',
                    file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo(
                    'Encountered error while waiting for resource to enter the specified state. Outputting last known resource state',
                    file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@cli_util.copy_params_from_generated_command(inventory_cli.update_asset, params_to_exclude=[''])
@inventory_cli.asset_group.command(name=cli_util.override('inventory.update_asset.command_name', 'update'),
                                   help=u"""Updates the asset. \n[Command Reference](updateAsset)""")
@cli_util.option('--compute', type=custom_types.CLI_COMPLEX_TYPE,
                 help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vm', type=custom_types.CLI_COMPLEX_TYPE,
                 help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vmware-vm', type=custom_types.CLI_COMPLEX_TYPE,
                 help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vmware-v-center', type=custom_types.CLI_COMPLEX_TYPE,
                 help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--aws-ebs', type=custom_types.CLI_COMPLEX_TYPE,
                 help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--aws-ec2', type=custom_types.CLI_COMPLEX_TYPE,
                 help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--aws-ec2-cost', type=custom_types.CLI_COMPLEX_TYPE,
                 help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--attached-ebs-volumes-cost', type=custom_types.CLI_COMPLEX_TYPE,
                 help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'asset-source-ids': {'module': 'cloud_bridge', 'class': 'list[string]'},
                                                'freeform-tags': {'module': 'cloud_bridge',
                                                                  'class': 'dict(str, string)'},
                                                'defined-tags': {'module': 'cloud_bridge',
                                                                 'class': 'dict(str, dict(str, object))'},
                                                'compute': {'module': 'cloud_bridge', 'class': 'ComputeProperties'},
                                                'vm': {'module': 'cloud_bridge', 'class': 'VmProperties'},
                                                'vmware-vm': {'module': 'cloud_bridge', 'class': 'VmwareVmProperties'},
                                                'vmware-v-center': {'module': 'cloud_bridge',
                                                                    'class': 'VmwareVCenterProperties'},
                                                'aws-ebs': {'module': 'cloud_bridge',
                                                            'class': 'AwsEbsProperties'},
                                                'aws-ec2': {'module': 'cloud_bridge',
                                                            'class': 'AwsEc2Properties'},
                                                'aws-ec2-cost': {'module': 'cloud_bridge',
                                                                 'class': 'MonthlyCostSummary'},
                                                'attached-ebs-volumes-cost': {'module': 'cloud_bridge',
                                                                              'class': 'MonthlyCostSummary'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={'asset-source-ids': {'module': 'cloud_bridge', 'class': 'list[string]'},
                                   'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'},
                                   'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'},
                                   'compute': {'module': 'cloud_bridge', 'class': 'ComputeProperties'},
                                   'vm': {'module': 'cloud_bridge', 'class': 'VmProperties'},
                                   'vmware-vm': {'module': 'cloud_bridge', 'class': 'VmwareVmProperties'},
                                   'vmware-v-center': {'module': 'cloud_bridge', 'class': 'VmwareVCenterProperties'},
                                   'aws-ebs': {'module': 'cloud_bridge', 'class': 'AwsEbsProperties'},
                                   'aws-ec2': {'module': 'cloud_bridge', 'class': 'AwsEc2Properties'},
                                   'aws-ec2-cost': {'module': 'cloud_bridge', 'class': 'MonthlyCostSummary'},
                                   'attached-ebs-volumes-cost': {'module': 'cloud_bridge', 'class': 'MonthlyCostSummary'}},
    output_type={'module': 'cloud_bridge', 'class': 'Asset'})
@cli_util.wrap_exceptions
def update_asset(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, asset_id, asset_type,
                 display_name, asset_source_ids, freeform_tags, defined_tags, compute, vm, vmware_vm, vmware_v_center,
                 aws_ebs, aws_ec2, aws_ec2_cost, attached_ebs_volumes_cost, if_match):
    if isinstance(asset_id, six.string_types) and len(asset_id.strip()) == 0:
        raise click.UsageError('Parameter --asset-id cannot be whitespace or empty string')
    if not force:
        if asset_source_ids or freeform_tags or defined_tags:
            if not click.confirm(
                    "WARNING: Updates to asset-source-ids and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
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

    if compute is not None:
        _details['compute'] = cli_util.parse_json_parameter("compute", compute)

    if vm is not None:
        _details['vm'] = cli_util.parse_json_parameter("vm", vm)

    if vmware_vm is not None:
        _details['vmwareVm'] = cli_util.parse_json_parameter("vmware_vm", vmware_vm)

    if vmware_v_center is not None:
        _details['vmwareVCenter'] = cli_util.parse_json_parameter("vmware_v_center", vmware_v_center)

    if aws_ebs is not None:
        _details['awsEbs'] = cli_util.parse_json_parameter("aws_ebs", aws_ebs)

    if aws_ec2 is not None:
        _details['awsEc2'] = cli_util.parse_json_parameter("aws_ec2", aws_ec2)

    if aws_ec2_cost is not None:
        _details['awsEc2Cost'] = cli_util.parse_json_parameter("aws_ec2_cost", aws_ec2_cost)

    if attached_ebs_volumes_cost is not None:
        _details['attachedEbsVolumesCost'] = cli_util.parse_json_parameter("attached_ebs_volumes_cost", attached_ebs_volumes_cost)

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

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state),
                           file=sys.stderr)
                result = oci.wait_until(client, client.get_asset(result.data.id), 'lifecycle_state', wait_for_state,
                                        **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo(
                    'Failed to wait until the resource entered the specified state. Outputting last known resource state',
                    file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo(
                    'Encountered error while waiting for resource to enter the specified state. Outputting last known resource state',
                    file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


# Remove create-asset-create-aws-ebs-asset-details from oci cloud-bridge inventory asset
inventory_cli.asset_group.commands.pop(inventory_cli.create_asset_create_aws_ebs_asset_details.name)


# Remove create-asset-create-aws-ec2-asset-details from oci cloud-bridge inventory asset
inventory_cli.asset_group.commands.pop(inventory_cli.create_asset_create_aws_ec2_asset_details.name)


# Remove create-asset-create-inventory-asset-details from oci cloud-bridge inventory asset
# inventory_cli.asset_group.commands.pop(inventory_cli.create_asset_create_inventory_asset_details.name)


# Remove update-asset-update-aws-ebs-asset-details from oci cloud-bridge inventory asset
inventory_cli.asset_group.commands.pop(inventory_cli.update_asset_update_aws_ebs_asset_details.name)


# Remove update-asset-update-aws-ec2-asset-details from oci cloud-bridge inventory asset
inventory_cli.asset_group.commands.pop(inventory_cli.update_asset_update_aws_ec2_asset_details.name)


# Remove update-asset-update-inventory-asset-details from oci cloud-bridge inventory asset
# inventory_cli.asset_group.commands.pop(inventory_cli.update_asset_update_inventory_asset_details.name)
