# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
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
from services.apm_traces.src.oci_cli_apm_traces.generated import apm_traces_service_cli


@click.command(cli_util.override('trace.trace_root_group.command_name', 'trace'), cls=CommandGroupWithAlias, help=cli_util.override('trace.trace_root_group.help', """API for APM Trace service. Use this API to query the Traces and associated Spans."""), short_help=cli_util.override('trace.trace_root_group.short_help', """Apm Traces API"""))
@cli_util.help_option_group
def trace_root_group():
    pass


@click.command(cli_util.override('trace.trace_group.command_name', 'trace'), cls=CommandGroupWithAlias, help="""Definition of a trace object.""")
@cli_util.help_option_group
def trace_group():
    pass


@click.command(cli_util.override('trace.span_group.command_name', 'span'), cls=CommandGroupWithAlias, help="""Definition of a span object.""")
@cli_util.help_option_group
def span_group():
    pass


apm_traces_service_cli.apm_traces_service_group.add_command(trace_root_group)
trace_root_group.add_command(trace_group)
trace_root_group.add_command(span_group)


@span_group.command(name=cli_util.override('trace.get_span.command_name', 'get'), help=u"""Get the span details identified by spanId \n[Command Reference](getSpan)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM Domain Id the request is intended for.""")
@cli_util.option('--span-key', required=True, help=u"""Unique APM span identifier(spanId).""")
@cli_util.option('--trace-key', required=True, help=u"""Unique APM trace identifier(traceId).""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'apm_traces', 'class': 'Span'})
@cli_util.wrap_exceptions
def get_span(ctx, from_json, apm_domain_id, span_key, trace_key):

    if isinstance(span_key, six.string_types) and len(span_key.strip()) == 0:
        raise click.UsageError('Parameter --span-key cannot be whitespace or empty string')

    if isinstance(trace_key, six.string_types) and len(trace_key.strip()) == 0:
        raise click.UsageError('Parameter --trace-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('apm_traces', 'trace', ctx)
    result = client.get_span(
        apm_domain_id=apm_domain_id,
        span_key=span_key,
        trace_key=trace_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@trace_group.command(name=cli_util.override('trace.get_trace.command_name', 'get'), help=u"""Get the trace details identified by traceId \n[Command Reference](getTrace)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM Domain Id the request is intended for.""")
@cli_util.option('--trace-key', required=True, help=u"""Unique APM trace identifier(traceId).""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'apm_traces', 'class': 'Trace'})
@cli_util.wrap_exceptions
def get_trace(ctx, from_json, apm_domain_id, trace_key):

    if isinstance(trace_key, six.string_types) and len(trace_key.strip()) == 0:
        raise click.UsageError('Parameter --trace-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('apm_traces', 'trace', ctx)
    result = client.get_trace(
        apm_domain_id=apm_domain_id,
        trace_key=trace_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)
