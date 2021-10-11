# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.apm_config.src.oci_cli_config.generated import config_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci apm-config config create-config-create-apdex-rules-details -> oci apm-config config create-apdex-rules
cli_util.rename_command(config_cli, config_cli.config_group, config_cli.create_config_create_apdex_rules_details, "create-apdex-rules")


# oci apm-config config create-config-create-metric-group-details -> oci apm-config config create-metric-group
cli_util.rename_command(config_cli, config_cli.config_group, config_cli.create_config_create_metric_group_details, "create-metric-group")


# oci apm-config config create-config-create-span-filter-details -> oci apm-config config create-span-filter
cli_util.rename_command(config_cli, config_cli.config_group, config_cli.create_config_create_span_filter_details, "create-span-filter")


# oci apm-config config update-config-update-apdex-rules-details -> oci apm-config config update-apdex-rules
cli_util.rename_command(config_cli, config_cli.config_group, config_cli.update_config_update_apdex_rules_details, "update-apdex-rules")


# oci apm-config config update-config-update-metric-group-details -> oci apm-config config update-metric-group
cli_util.rename_command(config_cli, config_cli.config_group, config_cli.update_config_update_metric_group_details, "update-metric-group")


# oci apm-config config update-config-update-span-filter-details -> oci apm-config config update-span-filter
cli_util.rename_command(config_cli, config_cli.config_group, config_cli.update_config_update_span_filter_details, "update-span-filter")


# oci apm-config config-collection list-configs -> oci apm-config config-collection list
cli_util.rename_command(config_cli, config_cli.config_collection_group, config_cli.list_configs, "list")


# Remove create from oci apm-config config
config_cli.config_group.commands.pop(config_cli.create_config.name)


# Remove update from oci apm-config config
config_cli.config_group.commands.pop(config_cli.update_config.name)
