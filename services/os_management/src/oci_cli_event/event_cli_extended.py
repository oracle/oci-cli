# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.os_management.src.oci_cli_event.generated import event_cli
from oci_cli import cli_util

# Event - move and rename commands
event_root_group = event_cli.event_root_group

event_root_group.commands.pop(event_cli.binary_group.name)
event_root_group.add_command(event_cli.get_event_content)
cli_util.rename_command(event_cli, event_root_group, event_cli.get_event_content, "get-content")

event_root_group.commands.pop(event_cli.event_group.name)
event_root_group.add_command(event_cli.get_event)
event_root_group.add_command(event_cli.update_event)

event_root_group.commands.pop(event_cli.event_collection_group.name)
event_root_group.add_command(event_cli.list_events)
cli_util.rename_command(event_cli, event_root_group, event_cli.list_events, "list")

event_root_group.commands.pop(event_cli.event_content_group.name)
event_root_group.add_command(event_cli.delete_event_content)
cli_util.rename_command(event_cli, event_root_group, event_cli.delete_event_content, "delete-content")
event_root_group.add_command(event_cli.upload_event_content)
cli_util.rename_command(event_cli, event_root_group, event_cli.upload_event_content, "upload-content")

event_root_group.commands.pop(event_cli.event_report_group.name)
event_root_group.add_command(event_cli.get_event_report)
cli_util.rename_command(event_cli, event_root_group, event_cli.get_event_report, "get-report")

event_root_group.commands.pop(event_cli.related_event_collection_group.name)
event_root_group.add_command(event_cli.list_related_events)
