# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.cluster_placement_groups.src.oci_cli_cluster_placement_groups_cp.generated import clusterplacementgroupscp_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci cluster-placement-groups work-request-log-entry list-work-request-logs -> oci cluster-placement-groups work-request-log-entry list
cli_util.rename_command(clusterplacementgroupscp_cli, clusterplacementgroupscp_cli.work_request_log_entry_group, clusterplacementgroupscp_cli.list_work_request_logs, "list")


# Move commands under 'oci cluster-placement-groups cluster-placement-group-collection' -> 'oci cluster-placement-groups cluster-placement-group'
clusterplacementgroupscp_cli.cpg_root_group.commands.pop(clusterplacementgroupscp_cli.cluster_placement_group_collection_group.name)
clusterplacementgroupscp_cli.cluster_placement_group_group.add_command(clusterplacementgroupscp_cli.list_cluster_placement_groups)


@cli_util.copy_params_from_generated_command(clusterplacementgroupscp_cli.create_cluster_placement_group, params_to_exclude=['cluster_placement_group_type'])
@clusterplacementgroupscp_cli.cluster_placement_group_group.command(name=clusterplacementgroupscp_cli.create_cluster_placement_group.name, help=clusterplacementgroupscp_cli.create_cluster_placement_group.help)
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["STANDARD"]), help=u"""ClusterPlacementGroup Identifier. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'placement-instruction': {'module': 'cluster_placement_groups', 'class': 'PlacementInstructionDetails'}, 'capabilities': {'module': 'cluster_placement_groups', 'class': 'CapabilitiesCollection'}, 'freeform-tags': {'module': 'cluster_placement_groups', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cluster_placement_groups', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'cluster_placement_groups', 'class': 'ClusterPlacementGroup'})
@cli_util.wrap_exceptions
def create_cluster_placement_group_extended(ctx, **kwargs):

    if 'type' in kwargs:
        kwargs['cluster_placement_group_type'] = kwargs['type']
        kwargs.pop('type')

    ctx.invoke(clusterplacementgroupscp_cli.create_cluster_placement_group, **kwargs)


# oci cpg cluster-placement-group list-cluster-placement-groups -> oci cpg cluster-placement-group list
cli_util.rename_command(clusterplacementgroupscp_cli, clusterplacementgroupscp_cli.cluster_placement_group_group, clusterplacementgroupscp_cli.list_cluster_placement_groups, "list")
