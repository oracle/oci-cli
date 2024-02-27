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
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
from services.sch.src.oci_cli_service_connector.generated import serviceconnector_cli
from services.sch.src.oci_cli_sch.generated import sch_service_cli

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

# Remove create-service-connector-plugin-source-details from oci sch service-connector
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.create_service_connector_plugin_source_details.name)


# Remove update-service-connector-plugin-source-details from oci sch service-connector
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.update_service_connector_plugin_source_details.name)


serviceconnector_cli.service_connector_root_group.commands.pop(serviceconnector_cli.service_connector_group.name)
serviceconnector_cli.service_connector_root_group.commands.pop(serviceconnector_cli.work_request_error_group.name)
serviceconnector_cli.service_connector_root_group.commands.pop(serviceconnector_cli.work_request_log_entry_group.name)
serviceconnector_cli.service_connector_root_group.commands.pop(serviceconnector_cli.work_request_group.name)

sch_service_cli.sch_service_group.add_command(serviceconnector_cli.service_connector_group)
sch_service_cli.sch_service_group.add_command(serviceconnector_cli.work_request_group)
sch_service_cli.sch_service_group.add_command(serviceconnector_cli.work_request_log_entry_group)
sch_service_cli.sch_service_group.add_command(serviceconnector_cli.work_request_error_group)
