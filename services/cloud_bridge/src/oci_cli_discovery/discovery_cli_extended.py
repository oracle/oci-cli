# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
import click  # noqa: F401
import json  # noqa: F401

from services.cloud_bridge.src.oci_cli_discovery.generated import discovery_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401

# oci cloud-bridge discovery asset-source create-asset-source-create-vm-ware-asset-source-details ->
# oci cloud-bridge discovery asset-source create-vmware
cli_util.rename_command(discovery_cli, discovery_cli.asset_source_group,
                        discovery_cli.create_asset_source_create_vm_ware_asset_source_details, "create-vmware")

# oci cloud-bridge discovery asset-source update-asset-source-update-vm-ware-asset-source-details ->
# oci cloud-bridge discovery asset-source update-vmware
cli_util.rename_command(discovery_cli, discovery_cli.asset_source_group,
                        discovery_cli.update_asset_source_update_vm_ware_asset_source_details, "update-vmware")

# Consolidate the polymorphic CLI commands for create and update
discovery_cli.asset_source_group.commands.pop(discovery_cli.create_asset_source.name)
discovery_cli.asset_source_group.commands.pop(
    discovery_cli.create_asset_source_create_vm_ware_asset_source_details.name)
discovery_cli.asset_source_group.commands.pop(discovery_cli.update_asset_source.name)
discovery_cli.asset_source_group.commands.pop(
    discovery_cli.update_asset_source_update_vm_ware_asset_source_details.name)


@cli_util.copy_params_from_generated_command(discovery_cli.create_asset_source, params_to_exclude=[''])
@cli_util.option('--vcenter-endpoint',
                 help=u"""Endpoint for VMware asset discovery and replication in the form of ```https://<host>:<port>/sdk```""")
@cli_util.option('--discovery-credentials', type=custom_types.CLI_COMPLEX_TYPE,
                 help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--are-historical-metrics-collected', type=click.BOOL,
                 help=u"""Flag indicating whether historical metrics are collected for assets, originating from this asset source.""")
@cli_util.option('--are-realtime-metrics-collected', type=click.BOOL,
                 help=u"""Flag indicating whether real-time metrics are collected for assets, originating from this asset source.""")
@cli_util.option('--is-cost-information-collected', type=click.BOOL,
                 help=u"""Flag indicating whether cost data collection is enabled for assets, originating from this asset source.""")
@cli_util.option('--aws-region', help=u"""AWS region information, from where the resources are discovered.""")
@cli_util.option('--aws-account-key', help=u"""The key of customer's aws account to be discovered/migrated.""")
@discovery_cli.asset_source_group.command(
    name=cli_util.override('discovery.create_asset_source.command_name', 'create'),
    help=u"""Creates an asset source. \n[Command Reference](createAssetSource)""")
@json_skeleton_utils.get_cli_json_input_option(
    {'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'},
     'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'},
     'system-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'},
     'discovery-credentials': {'module': 'cloud_bridge', 'class': 'AssetSourceCredentials'},
     'replication-credentials': {'module': 'cloud_bridge', 'class': 'AssetSourceCredentials'}})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'},
                                   'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'},
                                   'system-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'},
                                   'discovery-credentials': {'module': 'cloud_bridge',
                                                             'class': 'AssetSourceCredentials'},
                                   'replication-credentials': {'module': 'cloud_bridge',
                                                               'class': 'AssetSourceCredentials'}},
    output_type={'module': 'cloud_bridge', 'class': 'AssetSource'})
@cli_util.wrap_exceptions
def create_asset_source(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, type, compartment_id,
                        environment_id, inventory_id, assets_compartment_id, vcenter_endpoint, discovery_credentials,
                        are_historical_metrics_collected, are_realtime_metrics_collected, is_cost_information_collected,
                        display_name, discovery_schedule_id, aws_region, aws_account_key, freeform_tags, defined_tags, system_tags):
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['type'] = type
    _details['compartmentId'] = compartment_id
    _details['environmentId'] = environment_id
    _details['inventoryId'] = inventory_id
    _details['assetsCompartmentId'] = assets_compartment_id
    _details['vcenterEndpoint'] = vcenter_endpoint
    _details['discoveryCredentials'] = cli_util.parse_json_parameter("discovery_credentials", discovery_credentials)
    _details['awsRegion'] = aws_region
    _details['awsAccountKey'] = aws_account_key

    if are_historical_metrics_collected is not None:
        _details['areHistoricalMetricsCollected'] = are_historical_metrics_collected

    if are_realtime_metrics_collected is not None:
        _details['areRealtimeMetricsCollected'] = are_realtime_metrics_collected

    if is_cost_information_collected is not None:
        _details['isCostInformationCollected'] = is_cost_information_collected

    if display_name is not None:
        _details['displayName'] = display_name

    if discovery_schedule_id is not None:
        _details['discoveryScheduleId'] = discovery_schedule_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if system_tags is not None:
        _details['systemTags'] = cli_util.parse_json_parameter("system_tags", system_tags)

    if type.lower() == 'vmware':
        if discovery_credentials is None or vcenter_endpoint is None:
            raise click.UsageError('If parameter --type is VMWARE, then parameters --discovery-credentials and --vcenter-endpoint must be provided')

    if type.lower() == 'aws':
        if discovery_credentials is None or aws_region is None or aws_account_key is None:
            raise click.UsageError('If parameter --type is AWS, then parameters --discovery-credentials, '
                                   '--aws-region and --aws-account-key must be provided')

    client = cli_util.build_client('cloud_bridge', 'discovery', ctx)
    result = client.create_asset_source(
        create_asset_source_details=_details,
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

                click.echo(
                    'Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state),
                    file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']),
                                        'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo(
                    'Failed to wait until the work request entered the specified state. Outputting last known resource state',
                    file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo(
                    'Encountered error while waiting for work request to enter the specified state. Outputting last known resource state',
                    file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@cli_util.copy_params_from_generated_command(discovery_cli.update_asset_source, params_to_exclude=[''])
@discovery_cli.asset_source_group.command(
    name=cli_util.override('discovery.update_asset_source.command_name', 'update'),
    help=u"""Updates the asset source. \n[Command Reference](updateAssetSource)""")
@cli_util.option('--vcenter-endpoint',
                 help=u"""Endpoint for VMware asset discovery and replication in the form of ```https://<host>:<port>/sdk```""")
@cli_util.option('--discovery-credentials', type=custom_types.CLI_COMPLEX_TYPE,
                 help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--replication-credentials', type=custom_types.CLI_COMPLEX_TYPE,
                 help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--are-historical-metrics-collected', type=click.BOOL,
                 help=u"""Flag indicating whether historical metrics are collected for assets, originating from this asset source.""")
@cli_util.option('--are-realtime-metrics-collected', type=click.BOOL,
                 help=u"""Flag indicating whether real-time metrics are collected for assets, originating from this asset source.""")
@cli_util.option('--is-cost-information-collected', type=click.BOOL,
                 help=u"""Flag indicating whether cost data collection is enabled for assets, originating from this asset source.""")
@cli_util.option('--discovery-schedule-id',
                 help=u"""The [OCID] of the discovery schedule that is going to be assigned to an asset source.""")
@json_skeleton_utils.get_cli_json_input_option(
    {'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'},
     'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'},
     'system-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'},
     'discovery-credentials': {'module': 'cloud_bridge', 'class': 'AssetSourceCredentials'},
     'replication-credentials': {'module': 'cloud_bridge', 'class': 'AssetSourceCredentials'}})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'},
                                   'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'},
                                   'system-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'},
                                   'discovery-credentials': {'module': 'cloud_bridge',
                                                             'class': 'AssetSourceCredentials'},
                                   'replication-credentials': {'module': 'cloud_bridge',
                                                               'class': 'AssetSourceCredentials'}})
@cli_util.wrap_exceptions
def update_asset_source(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, asset_source_id,
                        type, display_name, assets_compartment_id, freeform_tags, defined_tags, system_tags,
                        vcenter_endpoint, discovery_credentials, replication_credentials,
                        are_historical_metrics_collected, are_realtime_metrics_collected, is_cost_information_collected,
                        discovery_schedule_id, if_match):
    if isinstance(asset_source_id, six.string_types) and len(asset_source_id.strip()) == 0:
        raise click.UsageError('Parameter --asset-source-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or system_tags:
            if not click.confirm(
                    "WARNING: Updates to freeform-tags and defined-tags and system-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['type'] = type

    if display_name is not None:
        _details['displayName'] = display_name

    if assets_compartment_id is not None:
        _details['assetsCompartmentId'] = assets_compartment_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if system_tags is not None:
        _details['systemTags'] = cli_util.parse_json_parameter("system_tags", system_tags)

    if vcenter_endpoint is not None:
        _details['vcenterEndpoint'] = vcenter_endpoint

    if discovery_credentials is not None:
        _details['discoveryCredentials'] = cli_util.parse_json_parameter("discovery_credentials", discovery_credentials)

    if replication_credentials is not None:
        _details['replicationCredentials'] = cli_util.parse_json_parameter("replication_credentials",
                                                                           replication_credentials)

    if are_historical_metrics_collected is not None:
        _details['areHistoricalMetricsCollected'] = are_historical_metrics_collected

    if are_realtime_metrics_collected is not None:
        _details['areRealtimeMetricsCollected'] = are_realtime_metrics_collected

    if is_cost_information_collected is not None:
        _details['isCostInformationCollected'] = is_cost_information_collected

    if discovery_schedule_id is not None:
        _details['discoveryScheduleId'] = discovery_schedule_id

    client = cli_util.build_client('cloud_bridge', 'discovery', ctx)
    result = client.update_asset_source(
        asset_source_id=asset_source_id,
        update_asset_source_details=_details,
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

                click.echo(
                    'Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state),
                    file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']),
                                        'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo(
                    'Failed to wait until the work request entered the specified state. Outputting last known resource state',
                    file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo(
                    'Encountered error while waiting for work request to enter the specified state. Outputting last known resource state',
                    file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


# oci cloud-bridge discovery supported-cloud-region-summary list-supported-cloud-regions -> oci cloud-bridge discovery supported-cloud-region-summary list
cli_util.rename_command(discovery_cli, discovery_cli.supported_cloud_region_summary_group, discovery_cli.list_supported_cloud_regions, "list")


# oci cloud-bridge discovery supported-cloud-region-summary -> oci cloud-bridge discovery supported-cloud-regions
cli_util.rename_command(discovery_cli, discovery_cli.discovery_root_group, discovery_cli.supported_cloud_region_summary_group, "supported-cloud-regions")


# Remove create-asset-source-create-aws-asset-source-details from oci cloud-bridge discovery asset-source
discovery_cli.asset_source_group.commands.pop(discovery_cli.create_asset_source_create_aws_asset_source_details.name)


# Remove update-asset-source-update-aws-asset-source-details from oci cloud-bridge discovery asset-source
discovery_cli.asset_source_group.commands.pop(discovery_cli.update_asset_source_update_aws_asset_source_details.name)
