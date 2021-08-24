# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestNoSQLCliExtended(unittest.TestCase):
    def setUp(self):
        pass

    def test_nosql_query(self):
        result = util.invoke_command(['nosql', 'query'])
        assert 'query' in result.output
        assert 'prepare' in result.output
        result = util.invoke_command(['nosql', 'query', 'prepare'])
        assert 'Error: Missing option(s)' in result.output
        result = util.invoke_command(['nosql', 'query', 'summarize-statement'])
        assert "Error: No such command 'summarize-statement'." in result.output

    def test_nosql_work_request_error(self):
        result = util.invoke_command(['nosql', 'work-request-error', 'list'])
        assert 'Error: Missing option(s)' in result.output

    def test_nosql_work_request_log(self):
        result = util.invoke_command(['nosql', 'work-request-log', 'list'])
        assert 'Error: Missing option(s)' in result.output

    def test_nosql_row_update(self):
        result = util.invoke_command(['nosql', 'row', 'update', '--ttl-use-default'])
        assert 'requires an argument' in result.output
        result = util.invoke_command(['nosql', 'row', 'update', '--is-ttl-use-table-default'])
        assert 'Error: no such option' in result.output

    def test_nosql_query_query(self):
        result = util.invoke_command(['nosql', 'query', 'execute', '--max-read-in-kbs'])
        assert 'requires an argument' in result.output

    def test_nosql_index_create(self):
        result = util.invoke_command(['nosql', 'index', 'create'])
        assert 'index-name' in result.output
        result = util.invoke_command(['nosql', 'index', 'create', '--index-name'])
        assert 'requires an argument' in result.output
