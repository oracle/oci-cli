# Copyright (c) 2016, 2023, Oracle and/or its affiliates.
#
# This software is dual-licensed to you under the Universal Permissive License
# (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl and Apache License
# 2.0 as shown at https://www.apache.org/licenses/LICENSE-2.0. You may choose
# either license.
#
# If you elect to accept the software under the Apache License, Version 2.0,
# the following applies:
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
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
        assert 'attributes' in result.output
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
        assert 'log' in result.output
        assert 'trace-snapshot' in result.output
        assert 'aggregated-snapshot' in result.output
        assert '--help' in result.output

    def test_apm_traces_attributes(self):
        result = util.invoke_command(['apm-traces', 'attributes'])
        assert 'activate' in result.output
        assert 'deactivate' in result.output
        assert 'pin' in result.output
        assert 'unpin' in result.output
        assert 'update-notes' in result.output
        assert 'auto-activate-status' in result.output
        assert 'update-auto-activate' in result.output
        assert '--help' in result.output

    def test_apm_traces_scheduled_query(self):
        result = util.invoke_command(['apm-traces', 'scheduled-query'])
        assert 'create' in result.output
        assert 'delete' in result.output
        assert 'get' in result.output
        assert 'list' in result.output
        assert 'update' in result.output
        assert '--help' in result.output

    def test_run_query_options(self):
        result = util.invoke_command(['apm-traces', 'query', 'query-response', 'run-query'])
        assert 'Error: Missing option(s) --apm-domain-id, --start-time-gte, --start-time-lt.' in result.output  # Validating renaming of group query-result-response to query-response and query to run-query
        result = util.invoke_command(['apm-traces', 'query', 'query-response', 'run-query', '--apm-domain-id'])
        assert 'Error: Option \'--apm-domain-id\' requires an argument' in result.output  # Validating the required attribute
        result = util.invoke_command(['apm-traces', 'query', 'query-response', 'run-query', '--start-time-gte'])
        assert 'Error: Option \'--start-time-gte\' requires an argument' in result.output  # Validating the required attribute
        result = util.invoke_command(['apm-traces', 'query', 'query-response', 'run-query', '--start-time-lt'])
        assert 'Error: Option \'--start-time-lt\' requires an argument' in result.output  # Validating the required attribute
        result = util.invoke_command(['apm-traces', 'query', 'query-response', 'run-query', '--query-text'])
        assert 'Error: Option \'--query-text\' requires an argument' in result.output

    def test_list_quick_picks_options(self):
        result = util.invoke_command(['apm-traces', 'query', 'quick-picks', 'list'])
        assert 'Error: Missing option(s) --apm-domain-id' in result.output
        result = util.invoke_command(['apm-traces', 'query', 'quick-picks', 'list', '--apm-domain-id'])
        assert 'Error: Option \'--apm-domain-id\' requires an argument' in result.output  # Validating the required attribute

    def test_get_span_options(self):
        result = util.invoke_command(['apm-traces', 'trace', 'span', 'get'])
        assert 'Error: Missing option(s) --apm-domain-id, --span-key, --trace-key.' in result.output  # Validating the required attribute
        result = util.invoke_command(['apm-traces', 'trace', 'span', 'get', '--apm-domain-id'])
        assert 'Error: Option \'--apm-domain-id\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'trace', 'span', 'get', '--span-key'])
        assert 'Error: Option \'--span-key\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'trace', 'span', 'get', '--trace-key'])
        assert 'Error: Option \'--trace-key\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'trace', 'span', 'get', '--span-namespace'])
        assert 'Error: Option \'--span-namespace\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'trace', 'span', 'get', '--time-span-started-gte'])
        assert 'Error: Option \'--time-span-started-gte\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'trace', 'span', 'get', '--time-span-started-lt'])
        assert 'Error: Option \'--time-span-started-lt\' requires an argument' in result.output

    def test_get_log_options(self):
        result = util.invoke_command(['apm-traces', 'trace', 'log', 'get'])
        assert 'Error: Missing option(s) --apm-domain-id, --log-key, --start-time-lt, --start-time-gte.' in result.output  # Validating the required attribute
        result = util.invoke_command(['apm-traces', 'trace', 'log', 'get', '--apm-domain-id'])
        assert 'Error: Option \'--apm-domain-id\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'trace', 'log', 'get', '--log-key'])
        assert 'Error: Option \'--log-key\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'trace', 'log', 'get', '--start-time-gte'])
        assert 'Error: Option \'--start-time-gte\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'trace', 'log', 'get', '--start-time-lt'])
        assert 'Error: Option \'--start-time-lt\' requires an argument' in result.output

    def test_get_trace_options(self):
        result = util.invoke_command(['apm-traces', 'trace', 'trace', 'get'])
        assert 'Error: Missing option(s) --apm-domain-id, --trace-key.' in result.output  # Validating the required attribute
        result = util.invoke_command(['apm-traces', 'trace', 'trace', 'get', '--apm-domain-id'])
        assert 'Error: Option \'--apm-domain-id\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'trace', 'trace', 'get', '--trace-key'])
        assert 'Error: Option \'--trace-key\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'trace', 'trace', 'get', '--time-trace-started-gte'])
        assert 'Error: Option \'--time-trace-started-gte\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'trace', 'trace', 'get', '--time-trace-started-lt'])
        assert 'Error: Option \'--time-trace-started-lt\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'trace', 'trace', 'get', '--trace-namespace'])
        assert 'Error: Option \'--trace-namespace\' requires an argument' in result.output

    def test_get_aggregated_snapshot_options(self):
        result = util.invoke_command(['apm-traces', 'trace', 'aggregated-snapshot', 'get'])
        assert 'Error: Missing option(s) --apm-domain-id, --trace-key.' in result.output  # Validating the required attribute
        result = util.invoke_command(['apm-traces', 'trace', 'aggregated-snapshot', 'get', '--apm-domain-id'])
        assert 'Error: Option \'--apm-domain-id\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'trace', 'aggregated-snapshot', 'get', '--trace-key'])
        assert 'Error: Option \'--trace-key\' requires an argument' in result.output

    def test_get_trace_snapshot_options(self):
        result = util.invoke_command(['apm-traces', 'trace', 'trace-snapshot', 'get'])
        assert 'Error: Missing option(s) --apm-domain-id, --trace-key.' in result.output  # Validating the required attribute
        result = util.invoke_command(['apm-traces', 'trace', 'trace-snapshot', 'get', '--apm-domain-id'])
        assert 'Error: Option \'--apm-domain-id\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'trace', 'trace-snapshot', 'get', '--trace-key'])
        assert 'Error: Option \'--trace-key\' requires an argument' in result.output

    def test_activate_attributes_options(self):
        result = util.invoke_command(['apm-traces', 'attributes', 'activate'])
        assert 'Error: Missing option(s) --apm-domain-id, --attribute-details' in result.output  # Validating the required attribute
        result = util.invoke_command(['apm-traces', 'attributes', 'activate', '--apm-domain-id'])
        assert 'Error: Option \'--apm-domain-id\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'attributes', 'activate', '--attribute-details'])
        assert 'Error: Option \'--attribute-details\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'attributes', 'activate', '--attribute-details', 'attributeDetails : [{"attributeName": "test", "attributeType" : "NUMERIC"}]'])
        assert 'Error: Missing option(s) --apm-domain-id' in result.output

    def test_activate_status_options(self):
        result = util.invoke_command(['apm-traces', 'attributes', 'auto-activate-status'])
        assert 'Error: Missing option(s) --apm-domain-id, --data-key-type' in result.output  # Validating the required attribute
        result = util.invoke_command(['apm-traces', 'attributes', 'auto-activate-status', '--apm-domain-id'])
        assert 'Error: Option \'--apm-domain-id\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'attributes', 'auto-activate-status', '--data-key-type'])
        assert 'Error: Option \'--data-key-type\' requires an argument' in result.output

    def test_deactivate_attributes_options(self):
        result = util.invoke_command(['apm-traces', 'attributes', 'deactivate'])
        assert 'Error: Missing option(s) --apm-domain-id, --attribute-details' in result.output  # Validating the required attribute
        result = util.invoke_command(['apm-traces', 'attributes', 'deactivate', '--apm-domain-id'])
        assert 'Error: Option \'--apm-domain-id\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'attributes', 'deactivate', '--attribute-details'])
        assert 'Error: Option \'--attribute-details\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'attributes', 'activate', '--attribute-details', 'attributeDetails : [{"attributeName": "test"}]'])
        assert 'Error: Missing option(s) --apm-domain-id' in result.output

    def test_pin_attributes_options(self):
        result = util.invoke_command(['apm-traces', 'attributes', 'pin'])
        assert 'Error: Missing option(s) --apm-domain-id, --attribute-details' in result.output  # Validating the required attribute
        result = util.invoke_command(['apm-traces', 'attributes', 'pin', '--apm-domain-id'])
        assert 'Error: Option \'--apm-domain-id\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'attributes', 'pin', '--attribute-details'])
        assert 'Error: Option \'--attribute-details\' requires an argument' in result.output

    def test_unpin_attributes_options(self):
        result = util.invoke_command(['apm-traces', 'attributes', 'unpin'])
        assert 'Error: Missing option(s) --apm-domain-id, --attribute-details' in result.output  # Validating the required attribute
        result = util.invoke_command(['apm-traces', 'attributes', 'unpin', '--apm-domain-id'])
        assert 'Error: Option \'--apm-domain-id\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'attributes', 'unpin', '--attribute-details'])
        assert 'Error: Option \'--attribute-details\' requires an argument' in result.output

    def test_update_auto_activate_options(self):
        result = util.invoke_command(['apm-traces', 'attributes', 'update-auto-activate'])
        assert 'Error: Missing option(s) --apm-domain-id, --data-key-type, --auto-activate-value' in result.output  # Validating the required attribute
        result = util.invoke_command(['apm-traces', 'attributes', 'update-auto-activate', '--apm-domain-id'])
        assert 'Error: Option \'--apm-domain-id\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'attributes', 'update-auto-activate', '--data-key-type'])
        assert 'Error: Option \'--data-key-type\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'attributes', 'update-auto-activate', '--auto-activate-value'])
        assert 'Error: Option \'--auto-activate-value\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'attributes', 'update-auto-activate', '--data-key-type', 'PRIVATE_DATA_KEY'])
        assert 'Error: Missing option(s) --apm-domain-id, --auto-activate-value' in result.output
        result = util.invoke_command(['apm-traces', 'attributes', 'update-auto-activate', '--data-key-type', 'PUBLIC_DATA_KEY'])
        assert 'Error: Missing option(s) --apm-domain-id, --auto-activate-value' in result.output
        result = util.invoke_command(['apm-traces', 'attributes', 'update-auto-activate', '--data-key-type', 'PUBLIC_DATA_KEY', '--auto-activate-value', 'TRUE'])
        assert 'Error: Missing option(s) --apm-domain-id' in result.output

    def test_update_notes_options(self):
        result = util.invoke_command(['apm-traces', 'attributes', 'update-notes'])
        assert 'Error: Missing option(s) --apm-domain-id, --attribute-details' in result.output  # Validating the required attribute
        result = util.invoke_command(['apm-traces', 'attributes', 'update-notes', '--apm-domain-id'])
        assert 'Error: Option \'--apm-domain-id\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'attributes', 'update-notes', '--attribute-details'])
        assert 'Error: Option \'--attribute-details\' requires an argument' in result.output

    def test_update_attribute_options(self):
        result = util.invoke_command(['apm-traces', 'attributes', 'update-attribute'])
        assert 'Error: Missing option(s) --apm-domain-id, --attribute-details' in result.output  # Validating the required attribute
        result = util.invoke_command(['apm-traces', 'attributes', 'update-attribute', '--apm-domain-id'])
        assert 'Error: Option \'--apm-domain-id\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'attributes', 'update-attribute', '--attribute-details'])
        assert 'Error: Option \'--attribute-details\' requires an argument' in result.output

    def test_create_scheduled_query_options(self):
        result = util.invoke_command(['apm-traces', 'scheduled-query', 'create'])
        assert 'Error: Missing option(s) --apm-domain-id.' in result.output  # Validating the required attribute
        result = util.invoke_command(['apm-traces', 'scheduled-query', 'create', '--apm-domain-id'])
        assert 'Error: Option \'--apm-domain-id\' requires an argument' in result.output

    def test_delete_scheduled_query_options(self):
        result = util.invoke_command(['apm-traces', 'scheduled-query', 'delete'])
        assert 'Error: Missing option(s) --apm-domain-id, --id.' in result.output  # Validating the required attribute
        result = util.invoke_command(['apm-traces', 'scheduled-query', 'delete', '--apm-domain-id'])
        assert 'Error: Option \'--apm-domain-id\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'scheduled-query', 'delete', '--apm-domain-id', 'test', '--id'])
        assert 'Error: Option \'--id\' requires an argument' in result.output

    def test_get_scheduled_query_options(self):
        result = util.invoke_command(['apm-traces', 'scheduled-query', 'get'])
        assert 'Error: Missing option(s) --apm-domain-id, --id.' in result.output  # Validating the required attribute
        result = util.invoke_command(['apm-traces', 'scheduled-query', 'get', '--apm-domain-id'])
        assert 'Error: Option \'--apm-domain-id\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'scheduled-query', 'get', '--apm-domain-id', 'test', '--id'])
        assert 'Error: Option \'--id\' requires an argument' in result.output

    def test_list_scheduled_query_options(self):
        result = util.invoke_command(['apm-traces', 'scheduled-query', 'list'])
        assert 'Error: Missing option(s) --apm-domain-id.' in result.output  # Validating the required attribute
        result = util.invoke_command(['apm-traces', 'scheduled-query', 'list', '--apm-domain-id'])
        assert 'Error: Option \'--apm-domain-id\' requires an argument' in result.output

    def test_update_scheduled_query_options(self):
        result = util.invoke_command(['apm-traces', 'scheduled-query', 'update'])
        assert 'Error: Missing option(s) --apm-domain-id, --id.' in result.output  # Validating the required attribute
        result = util.invoke_command(['apm-traces', 'scheduled-query', 'update', '--apm-domain-id'])
        assert 'Error: Option \'--apm-domain-id\' requires an argument' in result.output
        result = util.invoke_command(['apm-traces', 'scheduled-query', 'update', '--apm-domain-id', 'test', '--id'])
        assert 'Error: Option \'--id\' requires an argument' in result.output
