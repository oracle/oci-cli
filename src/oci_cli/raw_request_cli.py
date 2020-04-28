# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click
import json
import oci
import six.moves

from .cli_root import cli
from . import cli_util
from . import custom_types


@cli.command('raw-request', help="""Makes a raw request against an OCI service based on a provided URI, HTTP method and payload. This operation currently only supports JSON payloads.
This operation will output a JSON structure that looks like:

\b
    {
        "data": <a JSON array or object containing the parsed response body>,
        "headers": <a JSON object where each header is a key and the value is the header value>,
        "status": <the HTTP status code and reason, e.g. '200 OK', '404 Not Found'>
    }
""", short_help="""Makes a raw request against an OCI service""")
@cli_util.option('--target-uri', required=True, help="""The URI to make the request against""")
@cli_util.option('--http-method', type=custom_types.CliCaseInsensitiveChoice(["DELETE", "GET", "HEAD", "POST", "PUT"]), required=True, help="""The HTTP method to use""")
@cli_util.option('--request-body', type=custom_types.CLI_COMPLEX_TYPE, help="""Data to send in the body of the request. """ + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--request-headers', type=custom_types.CLI_COMPLEX_TYPE, help="""Additional headers to send as part of the request. """ + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def make_raw_request(ctx, target_uri, http_method, request_body, request_headers):
    _make_raw_request(ctx, target_uri, http_method, request_body, request_headers)


def _make_raw_request(ctx, target_uri, http_method, request_body, request_headers):
    # Endpoint doesn't make sense because we're asking someone for a --target-uri. We could also just use the --endpoint parameter but that
    # feels like an overloading of that concept (which is declared in cli_root)
    if ctx.obj['endpoint']:
        raise click.UsageError('The --endpoint parameter cannot be specified with this command')

    # Table output may not make too much sense here because we're also dumping out headers and status code, in addition
    # to the data
    if ctx.obj['output'] == 'table':
        raise click.UsageError('The table output format is not supported with this command')

    if ctx.obj['debug']:
        six.moves.http_client.HTTPConnection.debuglevel = 1

    jmespath_expression = cli_util.get_jmespath_expression_from_context(ctx)

    # Deliberately a bit open as we can permit an empty string through as an empty request body
    parsed_request_body = ''
    if request_body is not None and request_body.strip() != '':
        request_body_as_dict = cli_util.parse_json_parameter('request_body', request_body)
        parsed_request_body = json.dumps(request_body_as_dict)

    additional_headers = {}
    if request_headers:
        additional_headers = cli_util.parse_json_parameter('request_headers', request_headers)

    retry_strategy = oci.retry.DEFAULT_RETRY_STRATEGY
    if ctx.obj['no_retry']:
        retry_strategy = oci.retry.NoneRetryStrategy()

    # Make a request and output the results. The retry strategy should make sure that we can ride out
    # connection errors or timeouts, but its logic around ServiceError will not kick in because that's our
    # construct and not something which requests raises.
    #
    # However, with the spirit of this operation I think that is OK because really we just want to make a
    # call and then display the result (even if the result of that call is not a 2xx), so even a 4xx or 5xx
    # would be considered successful from this operation's perspective as it was able to hit a URI and get
    # a response
    with cli_util.build_raw_requests_session(ctx) as requests_session:
        response = retry_strategy.make_retrying_call(
            requests_session.request,
            method=http_method,
            url=target_uri,
            data=parsed_request_body,
            headers=additional_headers
        )

        result_dict = {
            'status': '{} {}'.format(response.status_code, response.reason),
            'headers': {key: value for (key, value) in response.headers.items()}
        }
        try:
            dict_from_response_body = response.json()
            if jmespath_expression:
                result_dict['data'] = jmespath_expression.search(dict_from_response_body)
            else:
                result_dict['data'] = dict_from_response_body
        except ValueError:
            # We may not have gotten valid JSON. In that case, do our best and just display something
            result_dict['data'] = response.text

        print(cli_util.pretty_print_format(result_dict))
