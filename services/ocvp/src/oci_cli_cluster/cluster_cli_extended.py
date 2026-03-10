# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.ocvp.src.oci_cli_cluster.generated import cluster_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401

# oci ocvs cluster cluster-summary list-clusters -> oci ocvs cluster cluster-summary list
cli_util.rename_command(cluster_cli, cluster_cli.cluster_summary_group, cluster_cli.list_clusters, "list")


# Move commands under 'oci ocvs cluster cluster' -> 'oci ocvs cluster'
cluster_cli.cluster_root_group.commands.pop(cluster_cli.cluster_group.name)
cluster_cli.cluster_root_group.add_command(cluster_cli.create_cluster)
cluster_cli.cluster_root_group.add_command(cluster_cli.delete_cluster)
cluster_cli.cluster_root_group.add_command(cluster_cli.get_cluster)
cluster_cli.cluster_root_group.add_command(cluster_cli.update_cluster)


# Move commands under 'oci ocvs cluster cluster-summary' -> 'oci ocvs cluster'
cluster_cli.cluster_root_group.commands.pop(cluster_cli.cluster_summary_group.name)
cluster_cli.cluster_root_group.add_command(cluster_cli.list_clusters)


@cli_util.copy_params_from_generated_command(cluster_cli.create_cluster, params_to_exclude=['cluster_byol_allocation_details'])
@cluster_cli.cluster_group.command(name=cluster_cli.create_cluster.name, help=cluster_cli.create_cluster.help)
@cli_util.option('--byol-allocation-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'network-configuration': {'module': 'ocvp', 'class': 'NetworkConfiguration'}, 'datastores': {'module': 'ocvp', 'class': 'list[DatastoreInfo]'}, 'datastore-cluster-ids': {'module': 'ocvp', 'class': 'list[string]'}, 'cluster-byol-allocation-details': {'module': 'ocvp', 'class': 'ClusterByolAllocationDetails'}, 'freeform-tags': {'module': 'ocvp', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ocvp', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_cluster_extended(ctx, **kwargs):

    if 'byol_allocation_details' in kwargs:
        kwargs['cluster_byol_allocation_details'] = kwargs['byol_allocation_details']
        kwargs.pop('byol_allocation_details')

    ctx.invoke(cluster_cli.create_cluster, **kwargs)


@cli_util.copy_params_from_generated_command(cluster_cli.update_cluster, params_to_exclude=['cluster_byol_allocation_details'])
@cluster_cli.cluster_group.command(name=cluster_cli.update_cluster.name, help=cluster_cli.update_cluster.help)
@cli_util.option('--byol-allocation-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'network-configuration': {'module': 'ocvp', 'class': 'NetworkConfiguration'}, 'cluster-byol-allocation-details': {'module': 'ocvp', 'class': 'ClusterByolAllocationDetails'}, 'freeform-tags': {'module': 'ocvp', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ocvp', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ocvp', 'class': 'Cluster'})
@cli_util.wrap_exceptions
def update_cluster_extended(ctx, **kwargs):

    if 'byol_allocation_details' in kwargs:
        kwargs['cluster_byol_allocation_details'] = kwargs['byol_allocation_details']
        kwargs.pop('byol_allocation_details')

    ctx.invoke(cluster_cli.update_cluster, **kwargs)
