# Copyright (c) 2016, 2023, Oracle and/or its affiliates.
#
# This software is dual-licensed to you under the Universal Permissive License
# (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl and Apache License
# 2.0 as shown at https://www.apache.org/licenses/LICENSE-2.0. You may choose
# either license.
#
# If you elect to accept the software under the Apache License, Version 2.0,
# the following applies:
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# coding: utf-8
import click  # noqa: F401
import json  # noqa: F401
from services.opensearch.src.oci_cli_opensearch_cluster_pipeline.generated import opensearchclusterpipeline_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401

# Move commands under 'oci opensearch pipeline opensearch-cluster-pipeline' -> 'oci opensearch pipeline'
opensearchclusterpipeline_cli.opensearch_cluster_pipeline_root_group.commands.pop(opensearchclusterpipeline_cli.opensearch_cluster_pipeline_group.name)
opensearchclusterpipeline_cli.opensearch_cluster_pipeline_root_group.add_command(opensearchclusterpipeline_cli.create_opensearch_cluster_pipeline)
opensearchclusterpipeline_cli.opensearch_cluster_pipeline_root_group.add_command(opensearchclusterpipeline_cli.get_opensearch_cluster_pipeline)
opensearchclusterpipeline_cli.opensearch_cluster_pipeline_root_group.add_command(opensearchclusterpipeline_cli.update_opensearch_cluster_pipeline)
opensearchclusterpipeline_cli.opensearch_cluster_pipeline_root_group.add_command(opensearchclusterpipeline_cli.delete_opensearch_cluster_pipeline)

# Move commands under 'oci opensearch pipeline opensearch-cluster-pipeline-collection' -> 'oci opensearch pipeline'
opensearchclusterpipeline_cli.opensearch_cluster_pipeline_root_group.commands.pop(opensearchclusterpipeline_cli.opensearch_cluster_pipeline_collection_group.name)
opensearchclusterpipeline_cli.opensearch_cluster_pipeline_root_group.add_command(opensearchclusterpipeline_cli.list_opensearch_cluster_pipelines)

# Rename the command 'oci opensearch pipeline list-opensearch-cluster-pipelines' -> 'oci opensearch pipeline list'
cli_util.rename_command(opensearchclusterpipeline_cli, opensearchclusterpipeline_cli.opensearch_cluster_pipeline_root_group, opensearchclusterpipeline_cli.list_opensearch_cluster_pipelines, "list")
