# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.oci_control_center.src.oci_cli_occ_metrics.generated import occmetrics_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci oci-control-center metric-property-collection -> oci oci-control-center metric-property
cli_util.rename_command(occmetrics_cli, occmetrics_cli.occ_root_group, occmetrics_cli.metric_property_collection_group, "metric-property")


# oci oci-control-center metric-property-collection list-metric-properties -> oci oci-control-center metric-property-collection list
cli_util.rename_command(occmetrics_cli, occmetrics_cli.metric_property_collection_group, occmetrics_cli.list_metric_properties, "list")


# oci oci-control-center namespace-collection -> oci oci-control-center namespace
cli_util.rename_command(occmetrics_cli, occmetrics_cli.occ_root_group, occmetrics_cli.namespace_collection_group, "namespace")


# oci oci-control-center namespace-collection list-namespaces -> oci oci-control-center namespace-collection list
cli_util.rename_command(occmetrics_cli, occmetrics_cli.namespace_collection_group, occmetrics_cli.list_namespaces, "list")


# oci oci-control-center summarized-metric-data-collection -> oci oci-control-center metric-data
cli_util.rename_command(occmetrics_cli, occmetrics_cli.occ_root_group, occmetrics_cli.summarized_metric_data_collection_group, "metric-data")


# oci oci-control-center summarized-metric-data-collection request-summarized-metric-data -> oci oci-control-center summarized-metric-data-collection read
cli_util.rename_command(occmetrics_cli, occmetrics_cli.summarized_metric_data_collection_group, occmetrics_cli.request_summarized_metric_data, "read")
