# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import click  # noqa: F401
import copy
from contextlib import ExitStack
import io
import shutil
import six  # noqa: F401
import tempfile
from types import SimpleNamespace
from oci_cli import cli_util  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401
from services.generative_ai_sandbox.src.oci_cli_generative_ai_sandbox.generated import generativeaisandbox_cli


# Keep released command paths while adding shorter aliases.
create_from_snapshot = copy.copy(generativeaisandbox_cli.create_sandbox_sandbox_snapshot_source)
create_from_snapshot.name = 'create-from-snapshot'
generativeaisandbox_cli.sandbox_group.add_command(create_from_snapshot)


# oci generative-ai-sandbox sandbox-collection -> oci generative-ai-sandbox sandbox
generativeaisandbox_cli.sandbox_group.add_command(generativeaisandbox_cli.list_sandboxes)


# oci generative-ai-sandbox sandbox-command-event -> oci generative-ai-sandbox sandbox-command
generativeaisandbox_cli.sandbox_command_group.add_command(generativeaisandbox_cli.run_sandbox_command_and_stream)


# oci generative-ai-sandbox sandbox-command-collection -> oci generative-ai-sandbox sandbox-command
generativeaisandbox_cli.sandbox_command_group.add_command(generativeaisandbox_cli.list_sandbox_command)


# oci generative-ai-sandbox sandbox-command-output -> oci generative-ai-sandbox sandbox-command
generativeaisandbox_cli.sandbox_command_group.add_command(generativeaisandbox_cli.get_sandbox_command_output)


# oci generative-ai-sandbox sandbox-snapshot-collection -> oci generative-ai-sandbox sandbox-snapshot
generativeaisandbox_cli.sandbox_snapshot_group.add_command(generativeaisandbox_cli.list_sandbox_snapshots)


@cli_util.copy_params_from_generated_command(generativeaisandbox_cli.stream_sandbox_command_events, params_to_exclude=['file'])
@generativeaisandbox_cli.sandbox_command_group.command(name=generativeaisandbox_cli.stream_sandbox_command_events.name, help=generativeaisandbox_cli.stream_sandbox_command_events.help)
@cli_util.option('--file', type=click.File(mode='wb'), help="The name of the file that will receive the raw response data, or '-' to write to STDOUT. If omitted, render command events to STDOUT.")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def stream_sandbox_command_events_extended(ctx, **kwargs):

    sandbox_id = kwargs['sandbox_id']
    command_id = kwargs['command_id']

    if isinstance(sandbox_id, six.string_types) and len(sandbox_id.strip()) == 0:
        raise click.UsageError('Parameter --sandbox-id cannot be whitespace or empty string')

    if isinstance(command_id, six.string_types) and len(command_id.strip()) == 0:
        raise click.UsageError('Parameter --command-id cannot be whitespace or empty string')

    request_kwargs = {}
    if kwargs.get('from_seq') is not None:
        request_kwargs['from_seq'] = kwargs['from_seq']
    if kwargs.get('until_seq') is not None:
        request_kwargs['until_seq'] = kwargs['until_seq']
    request_kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    client = cli_util.build_client('generative_ai_sandbox', 'generative_ai_sandbox', ctx)
    result = client.stream_sandbox_command_events(
        sandbox_id=sandbox_id,
        command_id=command_id,
        **request_kwargs
    )
    file = kwargs.get('file')
    if file is None:
        cli_util.render_response(result, ctx)
    else:
        # The SDK wraps raw SSE responses; retain the released --file wire format.
        response = getattr(result.data, '_event_source', result.data)
        for chunk in response.raw.stream(1024 * 1024, decode_content=True):
            file.write(chunk)
        if isinstance(file, click.utils.LazyFile):
            file.open()


generativeaisandbox_cli.sandbox_command_event_group.add_command(stream_sandbox_command_events_extended)


@cli_util.copy_params_from_generated_command(generativeaisandbox_cli.write_sandbox_file, params_to_exclude=['file'])
@generativeaisandbox_cli.sandbox_file_group.command(name=generativeaisandbox_cli.write_sandbox_file.name, help=generativeaisandbox_cli.write_sandbox_file.help)
@cli_util.option('--file', help=u"""Raw file contents to write, passed literally. Specify exactly one of --file or --local-file.""")
@cli_util.option('--local-file', type=click.File(mode='rb'), help=u"""The local file whose bytes will be written to the sandbox, or '-' to read from STDIN. Specify exactly one of --file or --local-file.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'generative_ai_sandbox', 'class': 'SandboxFile'})
@cli_util.wrap_exceptions
def write_sandbox_file_extended(ctx, **kwargs):

    local_file = kwargs.pop('local_file', None)
    if (kwargs.get('file') is None) == (local_file is None):
        raise click.UsageError('Specify exactly one of --file or --local-file')
    with ExitStack() as stack:
        file = local_file
        if file is None:
            # A byte stream gives literal text the correct length and octet-stream type.
            file = stack.enter_context(io.BytesIO(kwargs['file'].encode('utf-8')))
        if not file.seekable():
            # Signing a pipe after Requests selects chunked framing produces conflicting headers.
            buffered_file = stack.enter_context(tempfile.SpooledTemporaryFile(max_size=1024 * 1024))
            shutil.copyfileobj(file, buffered_file)
            buffered_file.seek(0)
            file = buffered_file

        position = file.tell()
        if file.read(1):
            file.seek(position)
            kwargs['file'] = file
        else:
            # A non-iterable reader prevents chunked framing alongside Content-Length: 0.
            kwargs['file'] = SimpleNamespace(read=file.read, seek=file.seek, tell=file.tell)

        ctx.invoke(generativeaisandbox_cli.write_sandbox_file, **kwargs)


@cli_util.copy_params_from_generated_command(generativeaisandbox_cli.read_sandbox_file, params_to_exclude=['file'])
@generativeaisandbox_cli.sandbox_file_group.command(name=generativeaisandbox_cli.read_sandbox_file.name, help=generativeaisandbox_cli.read_sandbox_file.help)
@cli_util.option('--file', type=click.File(mode='wb'), help=u"""The name of the file that will receive the response data, or '-' to write to STDOUT. Specify exactly one of --file or --local-file.""")
@cli_util.option('--local-file', type=click.File(mode='wb'), help=u"""The name of the file that will receive the response data, or '-' to write to STDOUT. Specify exactly one of --file or --local-file.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def read_sandbox_file_extended(ctx, **kwargs):

    local_file = kwargs.pop('local_file', None)
    if (kwargs.get('file') is None) == (local_file is None):
        raise click.UsageError('Specify exactly one of --file or --local-file')
    if local_file is not None:
        kwargs['file'] = local_file

    ctx.invoke(generativeaisandbox_cli.read_sandbox_file, **kwargs)

    # Click never opens a lazy output file when the response contains no chunks.
    if isinstance(kwargs['file'], click.utils.LazyFile):
        kwargs['file'].open().close()
