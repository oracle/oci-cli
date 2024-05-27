# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.capacity_management.src.oci_cli_capacity_management.generated import capacitymanagement_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci capacity-management occ-capacity-request-collection list-occ-capacity-requests -> oci capacity-management occ-capacity-request-collection list
cli_util.rename_command(capacitymanagement_cli, capacitymanagement_cli.occ_capacity_request_collection_group, capacitymanagement_cli.list_occ_capacity_requests, "list")


# oci capacity-management occ-capacity-request-collection list-occ-capacity-requests-internal -> oci capacity-management occ-capacity-request-collection list-internal
cli_util.rename_command(capacitymanagement_cli, capacitymanagement_cli.occ_capacity_request_collection_group, capacitymanagement_cli.list_occ_capacity_requests_internal, "list-internal")


# oci capacity-management occ-customer-group-collection list-occ-customer-groups -> oci capacity-management occ-customer-group-collection list
cli_util.rename_command(capacitymanagement_cli, capacitymanagement_cli.occ_customer_group_collection_group, capacitymanagement_cli.list_occ_customer_groups, "list")


# oci capacity-management occ-availability-catalog get-occ-availability-catalog-content -> oci capacity-management occ-availability-catalog get-catalog-content
cli_util.rename_command(capacitymanagement_cli, capacitymanagement_cli.occ_availability_catalog_group, capacitymanagement_cli.get_occ_availability_catalog_content, "get-catalog-content")


# oci capacity-management occ-availability-catalog-collection list-occ-availability-catalogs -> oci capacity-management occ-availability-catalog-collection list
cli_util.rename_command(capacitymanagement_cli, capacitymanagement_cli.occ_availability_catalog_collection_group, capacitymanagement_cli.list_occ_availability_catalogs, "list")


# oci capacity-management occ-availability-catalog-collection list-occ-availability-catalogs-internal -> oci capacity-management occ-availability-catalog-collection list-internal
cli_util.rename_command(capacitymanagement_cli, capacitymanagement_cli.occ_availability_catalog_collection_group, capacitymanagement_cli.list_occ_availability_catalogs_internal, "list-internal")


# oci capacity-management occ-availability-collection list-occ-availabilities -> oci capacity-management occ-availability-collection list
cli_util.rename_command(capacitymanagement_cli, capacitymanagement_cli.occ_availability_collection_group, capacitymanagement_cli.list_occ_availabilities, "list")


# oci capacity-management occ-overview-collection list-occ-overviews -> oci capacity-management occ-overview-collection list
cli_util.rename_command(capacitymanagement_cli, capacitymanagement_cli.occ_overview_collection_group, capacitymanagement_cli.list_occ_overviews, "list")


@cli_util.copy_params_from_generated_command(capacitymanagement_cli.create_occ_capacity_request, params_to_exclude=['region_parameterconflict'])
@capacitymanagement_cli.occ_capacity_request_group.command(name=capacitymanagement_cli.create_occ_capacity_request.name, help=capacitymanagement_cli.create_occ_capacity_request.help)
@cli_util.option('--target-region', required=True, help=u"""The name of the region for which the capacity request is made. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'capacity_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'capacity_management', 'class': 'dict(str, dict(str, object))'}, 'details': {'module': 'capacity_management', 'class': 'list[OccCapacityRequestBaseDetails]'}}, output_type={'module': 'capacity_management', 'class': 'OccCapacityRequest'})
@cli_util.wrap_exceptions
def create_occ_capacity_request_extended(ctx, **kwargs):

    if 'target_region' in kwargs:
        kwargs['region_parameterconflict'] = kwargs['target_region']
        kwargs.pop('target_region')

    ctx.invoke(capacitymanagement_cli.create_occ_capacity_request, **kwargs)
