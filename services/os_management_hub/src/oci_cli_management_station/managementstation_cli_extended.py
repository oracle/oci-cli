# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.os_management_hub.src.oci_cli_management_station.generated import managementstation_cli
from services.os_management_hub.src.oci_cli_os_management_hub.generated import os_management_hub_service_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci os-management-hub management-station management-station synchronize-single-mirrors -> oci os-management-hub management-station management-station sync-single-mirrors
cli_util.rename_command(managementstation_cli, managementstation_cli.management_station_group, managementstation_cli.synchronize_single_mirrors, "sync-single-mirrors")


# oci os-management-hub management-station management-station synchronize-mirrors -> oci os-management-hub management-station management-station sync-mirrors
cli_util.rename_command(managementstation_cli, managementstation_cli.management_station_group, managementstation_cli.synchronize_mirrors, "sync-mirrors")


# Move commands under 'oci os-management-hub management-station management-station' -> 'oci os-management-hub management-station'
managementstation_cli.management_station_root_group.commands.pop(managementstation_cli.management_station_group.name)
os_management_hub_service_cli.os_management_hub_service_group.commands.pop(managementstation_cli.management_station_root_group.name)
os_management_hub_service_cli.os_management_hub_service_group.add_command(managementstation_cli.management_station_group)


# Move commands under 'oci os-management-hub management-station mirrors-collection' -> 'oci os-management-hub management-station'
managementstation_cli.management_station_root_group.commands.pop(managementstation_cli.mirrors_collection_group.name)
managementstation_cli.management_station_group.add_command(managementstation_cli.list_mirrors)


@cli_util.copy_params_from_generated_command(managementstation_cli.create_management_station, params_to_exclude=['proxy_parameterconflict'])
@managementstation_cli.management_station_group.command(name=managementstation_cli.create_management_station.name, help=managementstation_cli.create_management_station.help)
@cli_util.option('--station-proxy', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.
 [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'station-proxy': {'module': 'os_management_hub', 'class': 'CreateProxyConfigurationDetails'}, 'mirror': {'module': 'os_management_hub', 'class': 'CreateMirrorConfigurationDetails'}, 'freeform-tags': {'module': 'os_management_hub', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'os_management_hub', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'os_management_hub', 'class': 'ManagementStation'})
@cli_util.wrap_exceptions
def create_management_station_extended(ctx, **kwargs):

    if 'station_proxy' in kwargs:
        kwargs['proxy_parameterconflict'] = kwargs['station_proxy']
        kwargs.pop('station_proxy')

    ctx.invoke(managementstation_cli.create_management_station, **kwargs)


@cli_util.copy_params_from_generated_command(managementstation_cli.list_management_stations, params_to_exclude=['id', 'location_not_equal_to'])
@managementstation_cli.management_station_group.command(name=managementstation_cli.list_management_stations.name, help=managementstation_cli.list_management_stations.help)
@cli_util.option('--management-station-id', help=u"""The OCID of the management station.""")
@cli_util.option('--location-ne', type=custom_types.CliCaseInsensitiveChoice(["ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", "GCP"]), multiple=True, help=u"""A filter to return only resources whose location does not match the given value.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management_hub', 'class': 'ManagementStationCollection'})
@cli_util.wrap_exceptions
def list_management_stations_extended(ctx, **kwargs):

    if 'management_station_id' in kwargs:
        kwargs['id'] = kwargs['management_station_id']
        kwargs.pop('management_station_id')

    if 'location_ne' in kwargs:
        kwargs['location_not_equal_to'] = kwargs['location_ne']
        kwargs.pop('location_ne')

    ctx.invoke(managementstation_cli.list_management_stations, **kwargs)


@cli_util.copy_params_from_generated_command(managementstation_cli.update_management_station, params_to_exclude=['proxy_parameterconflict'])
@managementstation_cli.management_station_group.command(name=managementstation_cli.update_management_station.name, help=managementstation_cli.update_management_station.help)
@cli_util.option('--station-proxy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'station-proxy': {'module': 'os_management_hub', 'class': 'UpdateProxyConfigurationDetails'}, 'mirror': {'module': 'os_management_hub', 'class': 'UpdateMirrorConfigurationDetails'}, 'freeform-tags': {'module': 'os_management_hub', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'os_management_hub', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'os_management_hub', 'class': 'ManagementStation'})
@cli_util.wrap_exceptions
def update_management_station_extended(ctx, **kwargs):

    if 'station_proxy' in kwargs:
        kwargs['proxy_parameterconflict'] = kwargs['station_proxy']
        kwargs.pop('station_proxy')

    ctx.invoke(managementstation_cli.update_management_station, **kwargs)
