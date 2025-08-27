# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.managed_kafka.src.oci_cli_kafka_cluster.generated import kafkacluster_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci kafka kafka-cluster -> oci kafka cluster
cli_util.rename_command(kafkacluster_cli, kafkacluster_cli.kafka_root_group, kafkacluster_cli.kafka_cluster_group, "cluster")


# oci kafka kafka-cluster-config -> oci kafka cluster-config
cli_util.rename_command(kafkacluster_cli, kafkacluster_cli.kafka_root_group, kafkacluster_cli.kafka_cluster_config_group, "cluster-config")


# oci kafka kafka-cluster-config-version -> oci kafka cluster-config-version
cli_util.rename_command(kafkacluster_cli, kafkacluster_cli.kafka_root_group, kafkacluster_cli.kafka_cluster_config_version_group, "cluster-config-version")


# oci kafka kafka-cluster-config-version-collection list-kafka-cluster-config-versions -> oci kafka kafka-cluster-config-version-collection list
cli_util.rename_command(kafkacluster_cli, kafkacluster_cli.kafka_cluster_config_version_collection_group, kafkacluster_cli.list_kafka_cluster_config_versions, "list")


# Move commands under 'oci kafka kafka-cluster-config-version-collection' -> 'oci kafka cluster-config-version'
kafkacluster_cli.kafka_root_group.commands.pop(kafkacluster_cli.kafka_cluster_config_version_collection_group.name)
kafkacluster_cli.kafka_cluster_config_version_group.add_command(kafkacluster_cli.list_kafka_cluster_config_versions)


@cli_util.copy_params_from_generated_command(kafkacluster_cli.list_kafka_cluster_config_versions, params_to_exclude=['kafka_cluster_config_id'])
@kafkacluster_cli.kafka_cluster_config_version_collection_group.command(name=kafkacluster_cli.list_kafka_cluster_config_versions.name, help=kafkacluster_cli.list_kafka_cluster_config_versions.help)
@cli_util.option('--config-id', required=True, help=u"""The [OCID] of the KafkaClusterConfig. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'managed_kafka', 'class': 'KafkaClusterConfigVersionCollection'})
@cli_util.wrap_exceptions
def list_kafka_cluster_config_versions_extended(ctx, **kwargs):

    if 'config_id' in kwargs:
        kwargs['kafka_cluster_config_id'] = kwargs['config_id']
        kwargs.pop('config_id')

    ctx.invoke(kafkacluster_cli.list_kafka_cluster_config_versions, **kwargs)
