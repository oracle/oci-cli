# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util

'''
Tests verifying that moved/renamed commands appear as expected.
'''


class TestDataCatalog(unittest.TestCase):
    def setUp(self):
        pass

    def test_list_attributes(self):
        result = util.invoke_command(['data-catalog', 'attribute', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert 'catalog-id' in result.output
        assert 'data-asset-key' in result.output
        assert 'entity-key' in result.output

    def test_list_attribute_tags(self):
        result = util.invoke_command(['data-catalog', 'attribute-tag', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert 'catalog-id' in result.output
        assert 'data-asset-key' in result.output
        assert 'entity-key' in result.output
        assert 'attribute-key' in result.output

    def test_list_connections(self):
        result = util.invoke_command(['data-catalog', 'connection', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert 'catalog-id' in result.output
        assert 'data-asset-key' in result.output

    def test_list_data_assets(self):
        result = util.invoke_command(['data-catalog', 'data-asset', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert 'catalog-id' in result.output

    def test_list_data_asset_tags(self):
        result = util.invoke_command(['data-catalog', 'data-asset-tag', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert 'catalog-id' in result.output
        assert 'data-asset-key' in result.output

    def test_list_entity_tags(self):
        result = util.invoke_command(['data-catalog', 'entity-tag', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert 'catalog-id' in result.output
        assert 'data-asset-key' in result.output
        assert 'entity-key' in result.output

    def test_list_folders(self):
        result = util.invoke_command(['data-catalog', 'folder', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert 'catalog-id' in result.output
        assert 'data-asset-key' in result.output

    def test_list_folder_tags(self):
        result = util.invoke_command(['data-catalog', 'folder-tag', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert 'catalog-id' in result.output
        assert 'data-asset-key' in result.output
        assert 'folder-key' in result.output

    def test_list_jobs(self):
        result = util.invoke_command(['data-catalog', 'job', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert 'catalog-id' in result.output

    def test_list_job_definitions(self):
        result = util.invoke_command(['data-catalog', 'job-definition', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert 'catalog-id' in result.output

    def test_list_job_executions(self):
        result = util.invoke_command(['data-catalog', 'job-execution', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert 'catalog-id' in result.output
        assert 'job-key' in result.output

    def test_list_job_logs(self):
        result = util.invoke_command(['data-catalog', 'job-log', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert 'catalog-id' in result.output
        assert 'job-key' in result.output
        assert 'job-execution-key' in result.output

    def test_list_job_metrics(self):
        result = util.invoke_command(['data-catalog', 'job-metric', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert 'catalog-id' in result.output
        assert 'job-key' in result.output
        assert 'job-execution-key' in result.output

    def test_list_types(self):
        result = util.invoke_command(['data-catalog', 'type', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert 'catalog-id' in result.output

    def test_list_tags(self):
        result = util.invoke_command(['data-catalog', 'tag', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert 'catalog-id' in result.output

    def test_search_query(self):
        result = util.invoke_command(['data-catalog', 'search', 'query'])
        assert 'Error: Missing option(s)' in result.output
        assert 'catalog-id' in result.output
        # DCAT-2654 - this should be marked as required in the spec
        # assert 'query' in result.output
        result = util.invoke_command(['data-catalog', 'search', 'query', '--query-text', 'dummy', '--catalog-id', 'dummy'])
        assert "ServiceError" in result.output
