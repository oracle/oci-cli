# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


# pytest -s services/apm_traces/tests/unit/test_apm_traces_cli_extended.py
class TestAPMTraces(unittest.TestCase):
    def setUp(self):
        pass

    def test_apm_traces(self):
        result = util.invoke_command(['apm-traces'])
        assert 'query' in result.output
        assert 'trace' in result.output
        assert '--help' in result.output

    def test_apm_traces_query(self):
        result = util.invoke_command(['apm-traces', 'query'])
        assert 'query-response' in result.output
        assert 'quick-picks' in result.output
        assert '--help' in result.output

    def test_apm_traces_trace(self):
        result = util.invoke_command(['apm-traces', 'trace'])
        assert 'trace' in result.output
        assert 'span' in result.output
        assert '--help' in result.output

    def test_run_query_options(self):
        result = util.invoke_command(['apm-traces', 'query', 'query-response', 'run-query'])
        assert 'Error: Missing option(s) --apm-domain-id, --start-time-gte, --start-time-lt.' in result.output  # Validating renaming of group query-result-response to query-response and query to run-query
        result = util.invoke_command(['apm-traces', 'query', 'query-response', 'run-query', '--apm-domain-id'])
        assert 'Error: --apm-domain-id option requires an argument' in result.output  # Validating the required attribute
        result = util.invoke_command(['apm-traces', 'query', 'query-response', 'run-query', '--start-time-gte'])
        assert 'Error: --start-time-gte option requires an argument' in result.output  # Validating the required attribute
        result = util.invoke_command(['apm-traces', 'query', 'query-response', 'run-query', '--start-time-lt'])
        assert 'Error: --start-time-lt option requires an argument' in result.output  # Validating the required attribute
        result = util.invoke_command(['apm-traces', 'query', 'query-response', 'run-query', '--query-text'])
        assert 'Error: --query-text option requires an argument' in result.output

    def test_list_quick_picks_options(self):
        result = util.invoke_command(['apm-traces', 'query', 'quick-picks', 'list'])
        assert 'Error: Missing option(s) --apm-domain-id' in result.output
        result = util.invoke_command(['apm-traces', 'query', 'quick-picks', 'list', '--apm-domain-id'])
        assert 'Error: --apm-domain-id option requires an argument' in result.output  # Validating the required attribute

    def test_get_span_options(self):
        result = util.invoke_command(['apm-traces', 'trace', 'span', 'get'])
        assert 'Error: Missing option(s) --apm-domain-id, --span-key, --trace-key.' in result.output  # Validating the required attribute
        result = util.invoke_command(['apm-traces', 'trace', 'span', 'get', '--apm-domain-id'])
        assert 'Error: --apm-domain-id option requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'trace', 'span', 'get', '--span-key'])
        assert 'Error: --span-key option requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'trace', 'trace', 'get', '--trace-key'])
        assert 'Error: --trace-key option requires an argument' in result.output

    def test_get_trace_options(self):
        result = util.invoke_command(['apm-traces', 'trace', 'trace', 'get'])
        assert 'Error: Missing option(s) --apm-domain-id, --trace-key.' in result.output  # Validating the required attribute
        result = util.invoke_command(['apm-traces', 'trace', 'span', 'get', '--apm-domain-id'])
        assert 'Error: --apm-domain-id option requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'trace', 'trace', 'get', '--trace-key'])
        assert 'Error: --trace-key option requires an argument' in result.output
