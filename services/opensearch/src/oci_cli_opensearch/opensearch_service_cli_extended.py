# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.opensearch.src.oci_cli_opensearch.generated import opensearch_service_cli
from services.opensearch.src.oci_cli_opensearch_cluster.generated import opensearchcluster_cli
from services.opensearch.src.oci_cli_opensearch_cluster_backup.generated import opensearchclusterbackup_cli

from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci opensearch opensearch-cluster -> oci opensearch cluster
cli_util.rename_command(opensearch_service_cli, opensearch_service_cli.opensearch_service_group, opensearchcluster_cli.opensearch_cluster_root_group, "cluster")


# oci opensearch opensearch-cluster-backup -> oci opensearch backup
cli_util.rename_command(opensearch_service_cli, opensearch_service_cli.opensearch_service_group, opensearchclusterbackup_cli.opensearch_cluster_backup_root_group, "backup")
