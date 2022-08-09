# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.opensearch.src.oci_cli_opensearch_cluster_backup.generated import opensearchclusterbackup_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# Move commands under 'oci opensearch backup opensearch-cluster-backup' -> 'oci opensearch backup'
opensearchclusterbackup_cli.opensearch_cluster_backup_root_group.commands.pop(opensearchclusterbackup_cli.opensearch_cluster_backup_group.name)
opensearchclusterbackup_cli.opensearch_cluster_backup_root_group.add_command(opensearchclusterbackup_cli.delete_opensearch_cluster_backup)
opensearchclusterbackup_cli.opensearch_cluster_backup_root_group.add_command(opensearchclusterbackup_cli.get_opensearch_cluster_backup)
opensearchclusterbackup_cli.opensearch_cluster_backup_root_group.add_command(opensearchclusterbackup_cli.update_opensearch_cluster_backup)


# Move commands under 'oci opensearch backup opensearch-cluster-backup-collection' -> 'oci opensearch backup'
opensearchclusterbackup_cli.opensearch_cluster_backup_root_group.commands.pop(opensearchclusterbackup_cli.opensearch_cluster_backup_collection_group.name)
opensearchclusterbackup_cli.opensearch_cluster_backup_root_group.add_command(opensearchclusterbackup_cli.list_opensearch_cluster_backups)


# oci opensearch backup list-opensearch-cluster-backups -> oci opensearch backup list
cli_util.rename_command(opensearchclusterbackup_cli, opensearchclusterbackup_cli.opensearch_cluster_backup_root_group, opensearchclusterbackup_cli.list_opensearch_cluster_backups, "list")
