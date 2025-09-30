# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.ocvp.src.oci_cli_datastore_cluster.generated import datastorecluster_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci ocvs datastore-cluster datastore-cluster attach -> oci ocvs datastore-cluster datastore-cluster attach-to-esxi-host
cli_util.rename_command(datastorecluster_cli, datastorecluster_cli.datastore_cluster_group, datastorecluster_cli.attach_datastore_cluster_to_esxi_host, "attach-to-esxi-host")


# oci ocvs datastore-cluster datastore-cluster detach -> oci ocvs datastore-cluster datastore-cluster detach-from-esxi-host
cli_util.rename_command(datastorecluster_cli, datastorecluster_cli.datastore_cluster_group, datastorecluster_cli.detach_datastore_cluster_from_esxi_host, "detach-from-esxi-host")


# oci ocvs datastore-cluster datastore-cluster attach -> oci ocvs datastore-cluster datastore-cluster attach-to-cluster
cli_util.rename_command(datastorecluster_cli, datastorecluster_cli.datastore_cluster_group, datastorecluster_cli.attach_datastore_cluster_to_cluster, "attach-to-cluster")


# oci ocvs datastore-cluster datastore-cluster detach -> oci ocvs datastore-cluster datastore-cluster detach-from-cluster
cli_util.rename_command(datastorecluster_cli, datastorecluster_cli.datastore_cluster_group, datastorecluster_cli.detach_datastore_cluster_from_cluster, "detach-from-cluster")


# oci ocvs datastore-cluster datastore-cluster add -> oci ocvs datastore-cluster datastore-cluster add-datastore
cli_util.rename_command(datastorecluster_cli, datastorecluster_cli.datastore_cluster_group, datastorecluster_cli.add_datastore_to_datastore_cluster, "add-datastore")


# oci ocvs datastore-cluster datastore-cluster remove -> oci ocvs datastore-cluster datastore-cluster remove-datastore
cli_util.rename_command(datastorecluster_cli, datastorecluster_cli.datastore_cluster_group, datastorecluster_cli.remove_datastore_from_datastore_cluster, "remove-datastore")


# Move commands under 'oci ocvs datastore-cluster datastore-cluster' -> 'oci ocvs datastore-cluster'
datastorecluster_cli.datastore_cluster_root_group.commands.pop(datastorecluster_cli.datastore_cluster_group.name)
datastorecluster_cli.datastore_cluster_root_group.add_command(datastorecluster_cli.add_datastore_to_datastore_cluster)
datastorecluster_cli.datastore_cluster_root_group.add_command(datastorecluster_cli.attach_datastore_cluster_to_cluster)
datastorecluster_cli.datastore_cluster_root_group.add_command(datastorecluster_cli.attach_datastore_cluster_to_esxi_host)
datastorecluster_cli.datastore_cluster_root_group.add_command(datastorecluster_cli.change_datastore_cluster_compartment)
datastorecluster_cli.datastore_cluster_root_group.add_command(datastorecluster_cli.create_datastore_cluster)
datastorecluster_cli.datastore_cluster_root_group.add_command(datastorecluster_cli.delete_datastore_cluster)
datastorecluster_cli.datastore_cluster_root_group.add_command(datastorecluster_cli.detach_datastore_cluster_from_cluster)
datastorecluster_cli.datastore_cluster_root_group.add_command(datastorecluster_cli.detach_datastore_cluster_from_esxi_host)
datastorecluster_cli.datastore_cluster_root_group.add_command(datastorecluster_cli.get_datastore_cluster)
datastorecluster_cli.datastore_cluster_root_group.add_command(datastorecluster_cli.list_datastore_clusters)
datastorecluster_cli.datastore_cluster_root_group.add_command(datastorecluster_cli.remove_datastore_from_datastore_cluster)
datastorecluster_cli.datastore_cluster_root_group.add_command(datastorecluster_cli.update_datastore_cluster)
