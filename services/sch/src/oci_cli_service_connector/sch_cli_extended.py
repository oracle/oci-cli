# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from services.sch.src.oci_cli_service_connector.generated import serviceconnector_cli


@cli_util.copy_params_from_generated_command(serviceconnector_cli.create_service_connector, params_to_exclude=['source', 'target'])
@serviceconnector_cli.service_connector_group.command(name='create', help=serviceconnector_cli.create_service_connector.help)
@cli_util.option('--source', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u""" For documentation on SourceDetails please see our API reference: https://docs.oracle.com/en-us/iaas/api/#/en/serviceconnectors/20200909/datatypes/SourceDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--target', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u""" For documentation on TargetDetails please see our API reference: https://docs.oracle.com/en-us/iaas/api/#/en/serviceconnectors/20200909/datatypes/TargetDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source': {'module': 'sch', 'class': 'SourceDetails'}, 'tasks': {'module': 'sch', 'class': 'list[TaskDetails]'}, 'target': {'module': 'sch', 'class': 'TargetDetails'}, 'freeform-tags': {'module': 'sch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'sch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_service_connector(ctx, **kwargs):
    ctx.invoke(serviceconnector_cli.create_service_connector, **kwargs)


serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.create_service_connector_functions_target_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.create_service_connector_logging_source_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.create_service_connector_monitoring_target_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.create_service_connector_notifications_target_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.create_service_connector_object_storage_target_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.create_service_connector_streaming_target_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.update_service_connector_functions_target_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.update_service_connector_logging_source_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.update_service_connector_monitoring_target_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.update_service_connector_notifications_target_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.update_service_connector_object_storage_target_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.update_service_connector_streaming_target_details.name)


# Remove create-service-connector-logging-analytics-target-details from oci sch service-connector
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.create_service_connector_logging_analytics_target_details.name)


# Remove update-service-connector-logging-analytics-target-details from oci sch service-connector
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.update_service_connector_logging_analytics_target_details.name)

# Remove create-service-connector-streaming-source-details from oci sch service-connector
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.create_service_connector_streaming_source_details.name)


# Remove update-service-connector-streaming-source-details from oci sch service-connector
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.update_service_connector_streaming_source_details.name)


# Remove create-service-connector-monitoring-source-details from oci sch service-connector
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.create_service_connector_monitoring_source_details.name)


# Remove update-service-connector-monitoring-source-details from oci sch service-connector
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.update_service_connector_monitoring_source_details.name)
