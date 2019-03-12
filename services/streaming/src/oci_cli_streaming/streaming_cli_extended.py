# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from oci_cli_stream.generated import stream_cli
from oci_cli_stream_admin.generated import streamadmin_cli
from oci_cli_streaming.generated import streaming_service_cli
from oci_cli import cli_util

cli_util.rename_command(streaming_service_cli.streaming_service_group, streamadmin_cli.stream_admin_root_group, "admin")
cli_util.rename_command(stream_cli.cursor_group, stream_cli.create_cursor, "create-cursor")
cli_util.rename_command(stream_cli.cursor_group, stream_cli.create_group_cursor, "create-group-cursor")
cli_util.rename_command(stream_cli.group_group, stream_cli.consumer_heartbeat, "heartbeat")
cli_util.rename_command(stream_cli.group_group, stream_cli.consumer_commit, "commit")

# override help text that is not provided
cli_util.override_command_short_help_and_help(stream_cli.stream_root_group, "Stream operations")
cli_util.override_command_short_help_and_help(streamadmin_cli.stream_admin_root_group, "Admin operations for streaming service")

cli_util.SERVICES_REQUIRING_ENDPOINTS.append("stream")
