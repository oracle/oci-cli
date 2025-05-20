# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.opensearch.src.oci_cli_opensearch_cluster.generated import opensearchcluster_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# Move commands under 'oci opensearch cluster opensearch-cluster' -> 'oci opensearch cluster'
opensearchcluster_cli.opensearch_cluster_root_group.commands.pop(opensearchcluster_cli.opensearch_cluster_group.name)
opensearchcluster_cli.opensearch_cluster_root_group.add_command(opensearchcluster_cli.backup_opensearch_cluster)
opensearchcluster_cli.opensearch_cluster_root_group.add_command(opensearchcluster_cli.create_opensearch_cluster)
opensearchcluster_cli.opensearch_cluster_root_group.add_command(opensearchcluster_cli.delete_opensearch_cluster)
opensearchcluster_cli.opensearch_cluster_root_group.add_command(opensearchcluster_cli.get_opensearch_cluster)
opensearchcluster_cli.opensearch_cluster_root_group.add_command(opensearchcluster_cli.opensearch_cluster_restore)
opensearchcluster_cli.opensearch_cluster_root_group.add_command(opensearchcluster_cli.resize_opensearch_cluster_horizontal)
opensearchcluster_cli.opensearch_cluster_root_group.add_command(opensearchcluster_cli.resize_opensearch_cluster_vertical)
opensearchcluster_cli.opensearch_cluster_root_group.add_command(opensearchcluster_cli.update_opensearch_cluster)
opensearchcluster_cli.opensearch_cluster_root_group.add_command(opensearchcluster_cli.configure_outbound_cluster)
opensearchcluster_cli.opensearch_cluster_root_group.add_command(opensearchcluster_cli.upgrade_open_search_cluster)


# Move commands under 'oci opensearch cluster opensearch-cluster-collection' -> 'oci opensearch cluster'
opensearchcluster_cli.opensearch_cluster_root_group.commands.pop(opensearchcluster_cli.opensearch_cluster_collection_group.name)
opensearchcluster_cli.opensearch_cluster_root_group.add_command(opensearchcluster_cli.list_opensearch_clusters)


# Move commands under 'oci opensearch cluster opensearch-versions-collection' -> 'oci opensearch cluster'
opensearchcluster_cli.opensearch_cluster_root_group.commands.pop(opensearchcluster_cli.opensearch_versions_collection_group.name)
opensearchcluster_cli.opensearch_cluster_root_group.add_command(opensearchcluster_cli.list_opensearch_versions)


# oci opensearch cluster resize-opensearch-cluster-horizontal -> oci opensearch cluster resizehorizontal
cli_util.rename_command(opensearchcluster_cli, opensearchcluster_cli.opensearch_cluster_root_group, opensearchcluster_cli.resize_opensearch_cluster_horizontal, "resizehorizontal")


# oci opensearch cluster resize-opensearch-cluster-vertical -> oci opensearch cluster resizevertical
cli_util.rename_command(opensearchcluster_cli, opensearchcluster_cli.opensearch_cluster_root_group, opensearchcluster_cli.resize_opensearch_cluster_vertical, "resizevertical")

# oci opensearch cluster configure_outbound_cluster -> oci opensearch cluster configureoutboundcluster
cli_util.rename_command(opensearchcluster_cli, opensearchcluster_cli.opensearch_cluster_root_group, opensearchcluster_cli.configure_outbound_cluster, "configureoutboundcluster")

# oci opensearch cluster opensearch-cluster-restore -> oci opensearch cluster restore
cli_util.rename_command(opensearchcluster_cli, opensearchcluster_cli.opensearch_cluster_root_group, opensearchcluster_cli.opensearch_cluster_restore, "restore")


# oci opensearch cluster list-opensearch-clusters -> oci opensearch cluster list
cli_util.rename_command(opensearchcluster_cli, opensearchcluster_cli.opensearch_cluster_root_group, opensearchcluster_cli.list_opensearch_clusters, "list")


# oci opensearch cluster list-opensearch-versions -> oci opensearch cluster list-versions
cli_util.rename_command(opensearchcluster_cli, opensearchcluster_cli.opensearch_cluster_root_group, opensearchcluster_cli.list_opensearch_versions, "list-versions")

# oci opensearch cluster upgrade_open_search_cluster -> oci opensearch cluster upgrade
cli_util.rename_command(opensearchcluster_cli, opensearchcluster_cli.opensearch_cluster_root_group, opensearchcluster_cli.upgrade_open_search_cluster, "upgrade")

# oci opensearch cluster work-request-error-collection -> oci opensearch cluster work-request-error
cli_util.rename_command(opensearchcluster_cli, opensearchcluster_cli.opensearch_cluster_root_group, opensearchcluster_cli.work_request_error_collection_group, "work-request-error")


# oci opensearch cluster work-request-log-entry-collection -> oci opensearch cluster work-request-log-entry
cli_util.rename_command(opensearchcluster_cli, opensearchcluster_cli.opensearch_cluster_root_group, opensearchcluster_cli.work_request_log_entry_collection_group, "work-request-log-entry")


# oci opensearch cluster work-request-error list-work-request-errors -> oci opensearch cluster work-request-error list
cli_util.rename_command(opensearchcluster_cli, opensearchcluster_cli.work_request_error_collection_group, opensearchcluster_cli.list_work_request_errors, "list")


# oci opensearch cluster work-request-log-entry list-work-request-logs -> oci opensearch cluster work-request-log-entry list
cli_util.rename_command(opensearchcluster_cli, opensearchcluster_cli.work_request_log_entry_collection_group, opensearchcluster_cli.list_work_request_logs, "list")


# Move commands under 'oci opensearch cluster work-request-collection' -> 'oci opensearch cluster work-request'
opensearchcluster_cli.opensearch_cluster_root_group.commands.pop(opensearchcluster_cli.work_request_collection_group.name)
opensearchcluster_cli.work_request_group.add_command(opensearchcluster_cli.list_work_requests)


# oci opensearch cluster work-request list-work-requests -> oci opensearch cluster work-request list
cli_util.rename_command(opensearchcluster_cli, opensearchcluster_cli.work_request_group, opensearchcluster_cli.list_work_requests, "list")

# oci opensearch cluster shapes-details list-opensearch-cluster-shapes -> oci opensearch cluster shapes-details list
cli_util.rename_command(opensearchcluster_cli, opensearchcluster_cli.shapes_details_group, opensearchcluster_cli.list_opensearch_cluster_shapes, "list")
