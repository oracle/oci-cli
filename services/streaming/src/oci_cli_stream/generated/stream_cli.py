# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from oci_cli_streaming.generated import streaming_service_cli


@click.command(cli_util.override('stream_root_group.command_name', 'stream'), cls=CommandGroupWithAlias, help=cli_util.override('stream_root_group.help', """The API for the Streaming Service."""), short_help=cli_util.override('stream_root_group.short_help', """Streaming Service API"""))
@cli_util.help_option_group
def stream_root_group():
    pass


@click.command(cli_util.override('cursor_group.command_name', 'cursor'), cls=CommandGroupWithAlias, help="""A cursor that indicates the position in the stream from which you want to begin consuming messages and which is required by the [GetMessages] operation.""")
@cli_util.help_option_group
def cursor_group():
    pass


@click.command(cli_util.override('message_group.command_name', 'message'), cls=CommandGroupWithAlias, help="""A message in a stream.""")
@cli_util.help_option_group
def message_group():
    pass


@click.command(cli_util.override('group_group.command_name', 'group'), cls=CommandGroupWithAlias, help="""Represents the current state of a consumer group, including partition reservations and committed offsets.""")
@cli_util.help_option_group
def group_group():
    pass


streaming_service_cli.streaming_service_group.add_command(stream_root_group)
stream_root_group.add_command(cursor_group)
stream_root_group.add_command(message_group)
stream_root_group.add_command(group_group)


@group_group.command(name=cli_util.override('consumer_commit.command_name', 'consumer-commit'), help=u"""Provides a mechanism to manually commit offsets, if not using commit-on-get consumer semantics. This commits offsets assicated with the provided cursor, extends the timeout on each of the affected partitions, and returns an updated cursor.

The top level --endpoint parameter must be supplied for this operation.""")
@cli_util.option('--stream-id', required=True, help=u"""The OCID of the stream for which the group is committing offsets.""")
@cli_util.option('--cursor', required=True, help=u"""The group-cursor representing the offsets of the group. This cursor is retrieved from the CreateGroupCursor API call.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'streaming', 'class': 'Cursor'})
@cli_util.wrap_exceptions
def consumer_commit(ctx, from_json, stream_id, cursor):

    if isinstance(stream_id, six.string_types) and len(stream_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('stream', ctx)
    result = client.consumer_commit(
        stream_id=stream_id,
        cursor=cursor,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@group_group.command(name=cli_util.override('consumer_heartbeat.command_name', 'consumer-heartbeat'), help=u"""Allows long-running processes to extend the timeout on partitions reserved by a consumer instance.

The top level --endpoint parameter must be supplied for this operation.""")
@cli_util.option('--stream-id', required=True, help=u"""The OCID of the stream for which the group is committing offsets.""")
@cli_util.option('--cursor', required=True, help=u"""The group-cursor representing the offsets of the group. This cursor is retrieved from the CreateGroupCursor API call.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'streaming', 'class': 'Cursor'})
@cli_util.wrap_exceptions
def consumer_heartbeat(ctx, from_json, stream_id, cursor):

    if isinstance(stream_id, six.string_types) and len(stream_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('stream', ctx)
    result = client.consumer_heartbeat(
        stream_id=stream_id,
        cursor=cursor,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cursor_group.command(name=cli_util.override('create_cursor.command_name', 'create'), help=u"""Creates a cursor. Cursors are used to consume a stream, starting from a specific point in the partition and going forward from there. You can create a cursor based on an offset, a time, the trim horizon, or the most recent message in the stream. As the oldest message inside the retention period boundary, using the trim horizon effectively lets you consume all messages in the stream. A cursor based on the most recent message allows consumption of only messages that are added to the stream after you create the cursor. Cursors expire five minutes after you receive them from the service.

The top level --endpoint parameter must be supplied for this operation.""")
@cli_util.option('--stream-id', required=True, help=u"""The OCID of the stream to create a cursor for.""")
@cli_util.option('--partition', required=True, help=u"""The partition to get messages from.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["AFTER_OFFSET", "AT_OFFSET", "AT_TIME", "LATEST", "TRIM_HORIZON"]), help=u"""The type of cursor, which determines the starting point from which the stream will be consumed:

- `AFTER_OFFSET:` The partition position immediately following the offset you specify. (Offsets are assigned when you successfully append a message to a partition in a stream.) - `AT_OFFSET:` The exact partition position indicated by the offset you specify. - `AT_TIME:` A specific point in time. - `LATEST:` The most recent message in the partition that was added after the cursor was created. - `TRIM_HORIZON:` The oldest message in the partition that is within the retention period window.""")
@cli_util.option('--offset', type=click.INT, help=u"""The offset to consume from if the cursor type is `AT_OFFSET` or `AFTER_OFFSET`.""")
@cli_util.option('--time', type=custom_types.CLI_DATETIME, help=u"""The time to consume from if the cursor type is `AT_TIME`, expressed in [RFC 3339] timestamp format.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'streaming', 'class': 'Cursor'})
@cli_util.wrap_exceptions
def create_cursor(ctx, from_json, stream_id, partition, type, offset, time):

    if isinstance(stream_id, six.string_types) and len(stream_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['partition'] = partition
    details['type'] = type

    if offset is not None:
        details['offset'] = offset

    if time is not None:
        details['time'] = time

    client = cli_util.build_client('stream', ctx)
    result = client.create_cursor(
        stream_id=stream_id,
        create_cursor_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cursor_group.command(name=cli_util.override('create_group_cursor.command_name', 'create-group'), help=u"""Creates a group-cursor.

The top level --endpoint parameter must be supplied for this operation.""")
@cli_util.option('--stream-id', required=True, help=u"""The OCID of the stream to create a cursor for.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["AT_TIME", "LATEST", "TRIM_HORIZON"]), help=u"""The type of the cursor. This value is only used when the group is created.""")
@cli_util.option('--group-name', required=True, help=u"""Name of the consumer group.""")
@cli_util.option('--time', type=custom_types.CLI_DATETIME, help=u"""The time to consume from if type is AT_TIME.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--instance-name', help=u"""A unique identifier for the instance joining the consumer group. If an instanceName is not provided, a UUID will be generated and used.""")
@cli_util.option('--timeout-in-ms', type=click.INT, help=u"""The amount of a consumer instance inactivity time, before partition reservations are released.""")
@cli_util.option('--commit-on-get', type=click.BOOL, help=u"""When using consumer-groups, the default commit-on-get behaviour can be overriden by setting this value to false. If disabled, a consumer must manually commit their cursors.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'streaming', 'class': 'Cursor'})
@cli_util.wrap_exceptions
def create_group_cursor(ctx, from_json, stream_id, type, group_name, time, instance_name, timeout_in_ms, commit_on_get):

    if isinstance(stream_id, six.string_types) and len(stream_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['type'] = type
    details['groupName'] = group_name

    if time is not None:
        details['time'] = time

    if instance_name is not None:
        details['instanceName'] = instance_name

    if timeout_in_ms is not None:
        details['timeoutInMs'] = timeout_in_ms

    if commit_on_get is not None:
        details['commitOnGet'] = commit_on_get

    client = cli_util.build_client('stream', ctx)
    result = client.create_group_cursor(
        stream_id=stream_id,
        create_group_cursor_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@group_group.command(name=cli_util.override('get_group.command_name', 'get'), help=u"""Returns the current state of a consumer group.

The top level --endpoint parameter must be supplied for this operation.""")
@cli_util.option('--stream-id', required=True, help=u"""The OCID of the stream, on which the group is operating.""")
@cli_util.option('--group-name', required=True, help=u"""The name of the consumer group.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'streaming', 'class': 'Group'})
@cli_util.wrap_exceptions
def get_group(ctx, from_json, stream_id, group_name):

    if isinstance(stream_id, six.string_types) and len(stream_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-id cannot be whitespace or empty string')

    if isinstance(group_name, six.string_types) and len(group_name.strip()) == 0:
        raise click.UsageError('Parameter --group-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('stream', ctx)
    result = client.get_group(
        stream_id=stream_id,
        group_name=group_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@message_group.command(name=cli_util.override('get_messages.command_name', 'get'), help=u"""Returns messages from the specified stream using the specified cursor as the starting point for consumption. By default, the number of messages returned is undefined, but the service returns as many as possible. To get messages, you must first obtain a cursor using the [CreateCursor] operation. In the response, retrieve the value of the 'opc-next-cursor' header to pass as a parameter to get the next batch of messages in the stream.

The top level --endpoint parameter must be supplied for this operation.""")
@cli_util.option('--stream-id', required=True, help=u"""The OCID of the stream to get messages from.""")
@cli_util.option('--cursor', required=True, help=u"""The cursor used to consume the stream.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of messages to return. You can specify any value up to 10000. By default, the service returns as many messages as possible. Consider your average message size to help avoid exceeding throughput on the stream.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'streaming', 'class': 'list[Message]'})
@cli_util.wrap_exceptions
def get_messages(ctx, from_json, stream_id, cursor, limit):

    if isinstance(stream_id, six.string_types) and len(stream_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('stream', ctx)
    result = client.get_messages(
        stream_id=stream_id,
        cursor=cursor,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@message_group.command(name=cli_util.override('put_messages.command_name', 'put'), help=u"""Emits messages to a stream. There's no limit to the number of messages in a request, but the total size of a message or request must be 1 MiB or less. The service calculates the partition ID from the message key and stores messages that share a key on the same partition. If a message does not contain a key or if the key is null, the service generates a message key for you. The partition ID cannot be passed as a parameter.

The top level --endpoint parameter must be supplied for this operation.""")
@cli_util.option('--stream-id', required=True, help=u"""The OCID of the stream where you want to put messages.""")
@cli_util.option('--messages', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The array of messages to put into a stream.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'messages': {'module': 'streaming', 'class': 'list[PutMessagesDetailsEntry]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'messages': {'module': 'streaming', 'class': 'list[PutMessagesDetailsEntry]'}}, output_type={'module': 'streaming', 'class': 'PutMessagesResult'})
@cli_util.wrap_exceptions
def put_messages(ctx, from_json, stream_id, messages):

    if isinstance(stream_id, six.string_types) and len(stream_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['messages'] = cli_util.parse_json_parameter("messages", messages)

    client = cli_util.build_client('stream', ctx)
    result = client.put_messages(
        stream_id=stream_id,
        put_messages_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@group_group.command(name=cli_util.override('update_group.command_name', 'update'), help=u"""Forcefully changes the current location of a group as a whole; reseting processing location of all consumers to a particular location in the stream.

The top level --endpoint parameter must be supplied for this operation.""")
@cli_util.option('--stream-id', required=True, help=u"""The OCID of the stream, on which the group is operating.""")
@cli_util.option('--group-name', required=True, help=u"""The name of the consumer group.""")
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["AT_TIME", "LATEST", "TRIM_HORIZON"]), help=u"""The type of the cursor.""")
@cli_util.option('--time', type=custom_types.CLI_DATETIME, help=u"""The time to consume from if type is AT_TIME.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_group(ctx, from_json, stream_id, group_name, type, time):

    if isinstance(stream_id, six.string_types) and len(stream_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-id cannot be whitespace or empty string')

    if isinstance(group_name, six.string_types) and len(group_name.strip()) == 0:
        raise click.UsageError('Parameter --group-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}

    if type is not None:
        details['type'] = type

    if time is not None:
        details['time'] = time

    client = cli_util.build_client('stream', ctx)
    result = client.update_group(
        stream_id=stream_id,
        group_name=group_name,
        update_group_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
