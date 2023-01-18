# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

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
from services.queue.src.oci_cli_queue.generated import queue_service_cli


@click.command(cli_util.override('queue.queue_root_group.command_name', 'queue'), cls=CommandGroupWithAlias, help=cli_util.override('queue.queue_root_group.help', """A description of the Queue API"""), short_help=cli_util.override('queue.queue_root_group.short_help', """Queue API"""))
@cli_util.help_option_group
def queue_root_group():
    pass


@click.command(cli_util.override('queue.get_message_group.command_name', 'get-message'), cls=CommandGroupWithAlias, help="""A message consumed from a queue.""")
@cli_util.help_option_group
def get_message_group():
    pass


@click.command(cli_util.override('queue.queue_stats_group.command_name', 'queue-stats'), cls=CommandGroupWithAlias, help="""The stats for a queue and its dead letter queue.""")
@cli_util.help_option_group
def queue_stats_group():
    pass


@click.command(cli_util.override('queue.put_message_group.command_name', 'put-message'), cls=CommandGroupWithAlias, help="""A message that has been published in a queue.""")
@cli_util.help_option_group
def put_message_group():
    pass


@click.command(cli_util.override('queue.updated_message_group.command_name', 'updated-message'), cls=CommandGroupWithAlias, help="""An updated message with the new visibility.""")
@cli_util.help_option_group
def updated_message_group():
    pass


queue_service_cli.queue_service_group.add_command(queue_root_group)
queue_root_group.add_command(get_message_group)
queue_root_group.add_command(queue_stats_group)
queue_root_group.add_command(put_message_group)
queue_root_group.add_command(updated_message_group)
# oci queue queue --> oci queue
queue_service_cli.queue_service_group.commands.pop(queue_root_group.name)
queue_service_cli.queue_service_group.add_command(get_message_group)
queue_service_cli.queue_service_group.add_command(queue_stats_group)
queue_service_cli.queue_service_group.add_command(put_message_group)
queue_service_cli.queue_service_group.add_command(updated_message_group)


@get_message_group.command(name=cli_util.override('queue.delete_message.command_name', 'delete-message'), help=u"""Deletes from the queue the message represented by the receipt. \n[Command Reference](deleteMessage)""")
@cli_util.option('--queue-id', required=True, help=u"""unique Queue identifier""")
@cli_util.option('--message-receipt', required=True, help=u"""The receipt of the message retrieved from a GetMessages call.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_message(ctx, from_json, queue_id, message_receipt):

    if isinstance(queue_id, six.string_types) and len(queue_id.strip()) == 0:
        raise click.UsageError('Parameter --queue-id cannot be whitespace or empty string')

    if isinstance(message_receipt, six.string_types) and len(message_receipt.strip()) == 0:
        raise click.UsageError('Parameter --message-receipt cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('queue', 'queue', ctx)
    result = client.delete_message(
        queue_id=queue_id,
        message_receipt=message_receipt,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@get_message_group.command(name=cli_util.override('queue.delete_messages.command_name', 'delete-messages'), help=u"""Deletes multiple messages from the queue. \n[Command Reference](deleteMessages)""")
@cli_util.option('--queue-id', required=True, help=u"""unique Queue identifier""")
@cli_util.option('--entries', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The array of messages to delete from a queue.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'entries': {'module': 'queue', 'class': 'list[DeleteMessagesDetailsEntry]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'entries': {'module': 'queue', 'class': 'list[DeleteMessagesDetailsEntry]'}}, output_type={'module': 'queue', 'class': 'DeleteMessagesResult'})
@cli_util.wrap_exceptions
def delete_messages(ctx, from_json, queue_id, entries):

    if isinstance(queue_id, six.string_types) and len(queue_id.strip()) == 0:
        raise click.UsageError('Parameter --queue-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['entries'] = cli_util.parse_json_parameter("entries", entries)

    client = cli_util.build_client('queue', 'queue', ctx)
    result = client.delete_messages(
        queue_id=queue_id,
        delete_messages_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@get_message_group.command(name=cli_util.override('queue.get_messages.command_name', 'get-messages'), help=u"""Consumes message from the queue. \n[Command Reference](getMessages)""")
@cli_util.option('--queue-id', required=True, help=u"""unique Queue identifier""")
@cli_util.option('--visibility-in-seconds', type=click.INT, help=u"""If the visibilityInSeconds parameter is set, messages will be hidden for visibilityInSeconds seconds and won't be consumable by other consumers during that time. If it isn't set it defaults to the value set at the queue level. The minimum is 0 and the maximum is 43,200 (12 hours). Using a visibilityInSeconds of 0, effectively acts as a peek functionality. Messages retrieved that way, aren't meant to be deleted because they will most likely be delivered to another consumer as their visibility won't change, but will still increase the delivery count by one.""")
@cli_util.option('--timeout-in-seconds', type=click.INT, help=u"""If the timeoutInSeconds parameter isn't set or set to a value greater than zero, the request is using the long-polling mode and will only return when a message is available for consumption (it does not wait for limit messages but still only returns at-most limit messages) or after timeoutInSeconds seconds (in which case it will return an empty response) whichever comes first. If the parameter is set to zero, the request is using the short-polling mode and immediately returns whether messages have been retrieved or not. In same rare-cases a long-polling request could be interrupted (returned with empty response) before the end of the timeout. The minimum is 0 (long polling disabled), the maximum is 30 seconds and default is 30 seconds.""")
@cli_util.option('--limit', type=click.INT, help=u"""The limit parameter controls how many messages is returned at-most. The default is 1, the minimum is 1 and the maximum is 32.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'queue', 'class': 'GetMessages'})
@cli_util.wrap_exceptions
def get_messages(ctx, from_json, queue_id, visibility_in_seconds, timeout_in_seconds, limit):

    if isinstance(queue_id, six.string_types) and len(queue_id.strip()) == 0:
        raise click.UsageError('Parameter --queue-id cannot be whitespace or empty string')

    kwargs = {}
    if visibility_in_seconds is not None:
        kwargs['visibility_in_seconds'] = visibility_in_seconds
    if timeout_in_seconds is not None:
        kwargs['timeout_in_seconds'] = timeout_in_seconds
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('queue', 'queue', ctx)
    result = client.get_messages(
        queue_id=queue_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@queue_stats_group.command(name=cli_util.override('queue.get_stats.command_name', 'get-stats'), help=u"""Gets the statistics for the queue and its dead letter queue. \n[Command Reference](getStats)""")
@cli_util.option('--queue-id', required=True, help=u"""unique Queue identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'queue', 'class': 'QueueStats'})
@cli_util.wrap_exceptions
def get_stats(ctx, from_json, queue_id):

    if isinstance(queue_id, six.string_types) and len(queue_id.strip()) == 0:
        raise click.UsageError('Parameter --queue-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('queue', 'queue', ctx)
    result = client.get_stats(
        queue_id=queue_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@put_message_group.command(name=cli_util.override('queue.put_messages.command_name', 'put-messages'), help=u"""Puts messages in the queue \n[Command Reference](putMessages)""")
@cli_util.option('--queue-id', required=True, help=u"""unique Queue identifier""")
@cli_util.option('--messages', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The array of messages to put into a queue.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'messages': {'module': 'queue', 'class': 'list[PutMessagesDetailsEntry]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'messages': {'module': 'queue', 'class': 'list[PutMessagesDetailsEntry]'}}, output_type={'module': 'queue', 'class': 'PutMessages'})
@cli_util.wrap_exceptions
def put_messages(ctx, from_json, queue_id, messages):

    if isinstance(queue_id, six.string_types) and len(queue_id.strip()) == 0:
        raise click.UsageError('Parameter --queue-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['messages'] = cli_util.parse_json_parameter("messages", messages)

    client = cli_util.build_client('queue', 'queue', ctx)
    result = client.put_messages(
        queue_id=queue_id,
        put_messages_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@updated_message_group.command(name=cli_util.override('queue.update_message.command_name', 'update-message'), help=u"""Updates the visibility of the message represented by the receipt. \n[Command Reference](updateMessage)""")
@cli_util.option('--queue-id', required=True, help=u"""unique Queue identifier""")
@cli_util.option('--message-receipt', required=True, help=u"""The receipt of the message retrieved from a GetMessages call.""")
@cli_util.option('--visibility-in-seconds', required=True, type=click.INT, help=u"""The new visibility of the message relative to the current time (as-per the clock of the server receiving the request).""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'queue', 'class': 'UpdatedMessage'})
@cli_util.wrap_exceptions
def update_message(ctx, from_json, queue_id, message_receipt, visibility_in_seconds):

    if isinstance(queue_id, six.string_types) and len(queue_id.strip()) == 0:
        raise click.UsageError('Parameter --queue-id cannot be whitespace or empty string')

    if isinstance(message_receipt, six.string_types) and len(message_receipt.strip()) == 0:
        raise click.UsageError('Parameter --message-receipt cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['visibilityInSeconds'] = visibility_in_seconds

    client = cli_util.build_client('queue', 'queue', ctx)
    result = client.update_message(
        queue_id=queue_id,
        message_receipt=message_receipt,
        update_message_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@get_message_group.command(name=cli_util.override('queue.update_messages.command_name', 'update-messages'), help=u"""Updates multiple messages in the queue. \n[Command Reference](updateMessages)""")
@cli_util.option('--queue-id', required=True, help=u"""unique Queue identifier""")
@cli_util.option('--entries', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The array of messages to update in a queue.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'entries': {'module': 'queue', 'class': 'list[UpdateMessagesDetailsEntry]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'entries': {'module': 'queue', 'class': 'list[UpdateMessagesDetailsEntry]'}}, output_type={'module': 'queue', 'class': 'UpdateMessagesResult'})
@cli_util.wrap_exceptions
def update_messages(ctx, from_json, queue_id, entries):

    if isinstance(queue_id, six.string_types) and len(queue_id.strip()) == 0:
        raise click.UsageError('Parameter --queue-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['entries'] = cli_util.parse_json_parameter("entries", entries)

    client = cli_util.build_client('queue', 'queue', ctx)
    result = client.update_messages(
        queue_id=queue_id,
        update_messages_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
