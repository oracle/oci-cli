# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.container_instances.src.oci_cli_container_instance.generated import containerinstance_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci container-instances container-collection list-containers -> oci container-instances container-collection list
cli_util.rename_command(containerinstance_cli, containerinstance_cli.container_collection_group, containerinstance_cli.list_containers, "list")


# oci container-instances container-instance-collection list-container-instances -> oci container-instances container-instance-collection list
cli_util.rename_command(containerinstance_cli, containerinstance_cli.container_instance_collection_group, containerinstance_cli.list_container_instances, "list")


# oci container-instances container-instance-shape-collection list-container-instance-shapes -> oci container-instances container-instance-shape-collection list-shapes
cli_util.rename_command(containerinstance_cli, containerinstance_cli.container_instance_shape_collection_group, containerinstance_cli.list_container_instance_shapes, "list-shapes")


# oci container-instances work-request-summary-collection list-work-requests -> oci container-instances work-request-summary-collection list
cli_util.rename_command(containerinstance_cli, containerinstance_cli.work_request_summary_collection_group, containerinstance_cli.list_work_requests, "list")


# oci container-instances work-request-error-collection list-work-request-errors -> oci container-instances work-request-error-collection list-errors
cli_util.rename_command(containerinstance_cli, containerinstance_cli.work_request_error_collection_group, containerinstance_cli.list_work_request_errors, "list-errors")


# oci container-instances work-request-log-entry-collection list-work-request-logs -> oci container-instances work-request-log-entry-collection list-logs
cli_util.rename_command(containerinstance_cli, containerinstance_cli.work_request_log_entry_collection_group, containerinstance_cli.list_work_request_logs, "list-logs")


# Remove container-collection from oci container-instances
containerinstance_cli.container_instances_root_group.commands.pop(containerinstance_cli.container_collection_group.name)


# Remove container-instance-collection from oci container-instances
containerinstance_cli.container_instances_root_group.commands.pop(containerinstance_cli.container_instance_collection_group.name)


# Remove container-instance-shape-collection from oci container-instances
containerinstance_cli.container_instances_root_group.commands.pop(containerinstance_cli.container_instance_shape_collection_group.name)


# Remove work-request-summary-collection from oci container-instances
containerinstance_cli.container_instances_root_group.commands.pop(containerinstance_cli.work_request_summary_collection_group.name)


# Remove work-request-error-collection from oci container-instances
containerinstance_cli.container_instances_root_group.commands.pop(containerinstance_cli.work_request_error_collection_group.name)


# Remove work-request-log-entry-collection from oci container-instances
containerinstance_cli.container_instances_root_group.commands.pop(containerinstance_cli.work_request_log_entry_collection_group.name)


# oci container-instances container-collection list-containers -> oci container-instances container
containerinstance_cli.container_collection_group.commands.pop(containerinstance_cli.list_containers.name)
containerinstance_cli.container_group.add_command(containerinstance_cli.list_containers)


# oci container-instances container-instance-collection list-container-instances -> oci container-instances container-instance
containerinstance_cli.container_instance_collection_group.commands.pop(containerinstance_cli.list_container_instances.name)
containerinstance_cli.container_instance_group.add_command(containerinstance_cli.list_container_instances)


# oci container-instances container-instance-shape-collection list-container-instance-shapes -> oci container-instances container-instance
containerinstance_cli.container_instance_shape_collection_group.commands.pop(containerinstance_cli.list_container_instance_shapes.name)
containerinstance_cli.container_instance_group.add_command(containerinstance_cli.list_container_instance_shapes)


# oci container-instances work-request-summary-collection list-work-requests -> oci container-instances work-request
containerinstance_cli.work_request_summary_collection_group.commands.pop(containerinstance_cli.list_work_requests.name)
containerinstance_cli.work_request_group.add_command(containerinstance_cli.list_work_requests)


# oci container-instances work-request-error-collection list-work-request-errors -> oci container-instances work-request
containerinstance_cli.work_request_error_collection_group.commands.pop(containerinstance_cli.list_work_request_errors.name)
containerinstance_cli.work_request_group.add_command(containerinstance_cli.list_work_request_errors)


# oci container-instances work-request-log-entry-collection list-work-request-logs -> oci container-instances work-request
containerinstance_cli.work_request_log_entry_collection_group.commands.pop(containerinstance_cli.list_work_request_logs.name)
containerinstance_cli.work_request_group.add_command(containerinstance_cli.list_work_request_logs)
