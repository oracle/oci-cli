# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.streaming.src.oci_cli_stream.generated import stream_cli
from services.streaming.src.oci_cli_stream_admin.generated import streamadmin_cli
from services.streaming.src.oci_cli_streaming.generated import streaming_service_cli
from oci_cli import cli_util
from oci_cli import custom_types

cli_util.rename_command(streamadmin_cli, streaming_service_cli.streaming_service_group, streamadmin_cli.stream_admin_root_group, "admin")
cli_util.rename_command(stream_cli, stream_cli.cursor_group, stream_cli.create_cursor, "create-cursor")
cli_util.rename_command(stream_cli, stream_cli.cursor_group, stream_cli.create_group_cursor, "create-group-cursor")
cli_util.rename_command(stream_cli, stream_cli.group_group, stream_cli.consumer_heartbeat, "heartbeat")
cli_util.rename_command(stream_cli, stream_cli.group_group, stream_cli.consumer_commit, "commit")

# override help text that is not provided
cli_util.override_command_short_help_and_help(stream_cli.stream_root_group, "Stream operations")
cli_util.override_command_short_help_and_help(streamadmin_cli.stream_admin_root_group, "Admin operations for streaming service")
cli_util.update_param_help(stream_cli.put_messages, 'messages', """The array of messages to put into a stream. Must be Base64 encoded.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)

cli_util.SERVICES_REQUIRING_ENDPOINTS.append("stream")
