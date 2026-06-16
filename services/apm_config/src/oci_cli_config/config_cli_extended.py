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


# oci apm-config config create-config-create-options-details -> oci apm-config config create-options
cli_util.rename_command(config_cli, config_cli.config_group, config_cli.create_config_create_options_details, "create-options")


# oci apm-config config update-config-update-options-details -> oci apm-config config update-options
cli_util.rename_command(config_cli, config_cli.config_group, config_cli.update_config_update_options_details, "update-options")


# oci apm-config metric-group retrieve-namespace-metrics -> oci apm-config metric-group get-namespace-metrics
cli_util.rename_command(config_cli, config_cli.metric_group_group, config_cli.retrieve_namespace_metrics, "get-namespace-metrics")


# oci apm-config metric-group retrieve-namespaces -> oci apm-config metric-group get-namespaces
cli_util.rename_command(config_cli, config_cli.metric_group_group, config_cli.retrieve_namespaces, "get-namespaces")


# oci apm-config span-filter validate-span-filter-pattern -> oci apm-config span-filter validate-pattern
cli_util.rename_command(config_cli, config_cli.span_filter_group, config_cli.validate_span_filter_pattern, "validate-pattern")


# oci apm-config test-output test -> oci apm-config test-output test
cli_util.rename_command(config_cli, config_cli.test_output_group, config_cli.test, "test")


# oci apm-config test-output test-test-span-enrichment-details -> oci apm-config test-output span-enrichment-group
cli_util.rename_command(config_cli, config_cli.test_output_group, config_cli.test_test_span_enrichment_details, "span-enrichment-group")


# oci apm-config test-output -> oci apm-config test
cli_util.rename_command(config_cli, config_cli.apm_config_root_group, config_cli.test_output_group, "test")


# oci apm-config export-configuration-details copy-configuration -> oci apm-config export-configuration-details copy
cli_util.rename_command(config_cli, config_cli.export_configuration_details_group, config_cli.copy_configuration, "copy")


# oci apm-config export-configuration-details export-configuration -> oci apm-config export-configuration-details export
cli_util.rename_command(config_cli, config_cli.export_configuration_details_group, config_cli.export_configuration, "export")


# oci apm-config import-configuration-details import-configuration -> oci apm-config import-configuration-details import
cli_util.rename_command(config_cli, config_cli.import_configuration_details_group, config_cli.import_configuration, "import")


# oci apm-config export-configuration-details -> oci apm-config export-configuration
cli_util.rename_command(config_cli, config_cli.apm_config_root_group, config_cli.export_configuration_details_group, "export-configuration")


# oci apm-config import-configuration-details -> oci apm-config import-configuration
cli_util.rename_command(config_cli, config_cli.apm_config_root_group, config_cli.import_configuration_details_group, "import-configuration")


# oci apm-config config create-config-create-agent-config-details -> oci apm-config config create-agent
cli_util.rename_command(config_cli, config_cli.config_group, config_cli.create_config_create_agent_config_details, "create-agent")


# oci apm-config config create-config-create-macs-apm-extension-details -> oci apm-config config create-macs-extension
cli_util.rename_command(config_cli, config_cli.config_group, config_cli.create_config_create_macs_apm_extension_details, "create-macs-extension")


# oci apm-config config update-config-update-agent-config-details -> oci apm-config config update-agent
cli_util.rename_command(config_cli, config_cli.config_group, config_cli.update_config_update_agent_config_details, "update-agent")


# oci apm-config config update-config-update-macs-apm-extension-details -> oci apm-config config update-macs-extension
cli_util.rename_command(config_cli, config_cli.config_group, config_cli.update_config_update_macs_apm_extension_details, "update-macs-extension")


# oci apm-config data-file-summary-collection list-data-files -> oci apm-config data-file-summary-collection list
cli_util.rename_command(config_cli, config_cli.data_file_summary_collection_group, config_cli.list_data_files, "list")


# oci apm-config data-file-summary-collection -> oci apm-config data-file-collection
cli_util.rename_command(config_cli, config_cli.apm_config_root_group, config_cli.data_file_summary_collection_group, "data-file-collection")


@cli_util.copy_params_from_generated_command(config_cli.put_data_file, params_to_exclude=['put_data_file_body'])
@config_cli.data_file_group.command(name=config_cli.put_data_file.name, help=config_cli.put_data_file.help)
@cli_util.option('--data-file-body', required=True, help=u"""The data file to be uploaded. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def put_data_file_extended(ctx, **kwargs):

    if 'data_file_body' in kwargs:
        kwargs['put_data_file_body'] = kwargs['data_file_body']
        kwargs.pop('data_file_body')

    ctx.invoke(config_cli.put_data_file, **kwargs)
