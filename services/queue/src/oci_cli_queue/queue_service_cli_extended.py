# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.queue.src.oci_cli_queue.generated import queue_service_cli
from services.queue.src.oci_cli_queue.generated import queue_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci queue get-message -> oci queue messages
cli_util.rename_command(queue_service_cli, queue_service_cli.queue_service_group, queue_cli.get_message_group, "messages")


# Remove put-message from oci queue
queue_service_cli.queue_service_group.commands.pop(queue_cli.put_message_group.name)


# Remove updated-message from oci queue
queue_service_cli.queue_service_group.commands.pop(queue_cli.updated_message_group.name)


# Remove queue-stats from oci queue
queue_service_cli.queue_service_group.commands.pop(queue_cli.queue_stats_group.name)


# oci queue put-message put-messages -> oci queue get-message
queue_cli.put_message_group.commands.pop(queue_cli.put_messages.name)
queue_cli.get_message_group.add_command(queue_cli.put_messages)


# oci queue queue-stats get-stats -> oci queue get-message
queue_cli.queue_stats_group.commands.pop(queue_cli.get_stats.name)
queue_cli.get_message_group.add_command(queue_cli.get_stats)


# oci queue updated-message update-message -> oci queue get-message
queue_cli.updated_message_group.commands.pop(queue_cli.update_message.name)
queue_cli.get_message_group.add_command(queue_cli.update_message)


# oci queue channel-collection -> oci queue channels
cli_util.rename_command(queue_service_cli, queue_service_cli.queue_service_group, queue_cli.channel_collection_group, "channels")
