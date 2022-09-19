# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestLoganalyticsCliExtended(unittest.TestCase):
    def setUp(self):
        pass

    # query renamed commands
    def test_query_renamed_commands(self):
        result = util.invoke_command(['log-analytics', 'query',
                                      'query'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'query',
                                      'export-query-result'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'query', 'search'])
        assert """Usage: oci log-analytics query search [OPTIONS]""" in result.output

        result = util.invoke_command(['log-analytics', 'query', 'export'])
        assert """Usage: oci log-analytics query export [OPTIONS]""" in result.output

    # query flattened params
    def test_query_flattened_params(self):
        result = util.invoke_command(['log-analytics', 'query', 'search', '--time-filter'])
        assert 'Error: no such option: --time-filter' in result.output

        result = util.invoke_command(['log-analytics', 'query', 'export', '--time-filter'])
        assert 'Error: no such option: --time-filter' in result.output

        result = util.invoke_command(['log-analytics', 'query', 'search', '--saved-search-id'])
        assert 'Error: no such option: --saved-search-id' in result.output

        result = util.invoke_command(['log-analytics', 'query', 'search', '--time-start'])
        assert 'Error: --time-start option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'query', 'search', '--time-end'])
        assert 'Error: --time-end option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'query', 'search', '--timezone'])
        assert 'Error: --timezone option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'query', 'export', '--time-start'])
        assert 'Error: --time-start option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'query', 'export', '--time-end'])
        assert 'Error: --time-end option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'query', 'export', '--timezone'])
        assert 'Error: --timezone option requires an argument' in result.output

    # query namespace aliases
    def test_query_namespace_aliases(self):
        result = util.invoke_command(['log-analytics', 'query', 'compare-content', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'query', 'compare-content', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'query', 'compare-content', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

    # query-work-request renamed command
    def test_query_work_request_renamed_command(self):
        result = util.invoke_command(['log-analytics', 'query-work-request',
                                      'put-query-work-request-background'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'query-work-request', 'background'])
        assert """Usage: oci log-analytics query-work-request background [OPTIONS]""" in result.output

    # ScheduledTask test removed command
    def test_scheduled_task_removed_command(self):
        # removed create
        result = util.invoke_command(['log-analytics', 'scheduled-task', 'create'])
        assert 'No such command' in result.output

    # ScheduledTask renamed command
    def test_scheduled_task_renamed_command(self):
        # create-standard-task
        result = util.invoke_command(['log-analytics', 'scheduled-task', 'create-standard-task'])
        assert """Usage: oci log-analytics scheduled-task create-standard-task """ in result.output

        # create-acceleration-task
        result = util.invoke_command(['log-analytics', 'scheduled-task', 'create-acceleration-task'])
        assert """Usage: oci log-analytics scheduled-task create-acceleration-task """ in result.output

    # ScheduledTask namespace aliases
    def test_scheduled_task_namespace_aliases(self):
        result = util.invoke_command(['log-analytics', 'scheduled-task', 'verify', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'scheduled-task', 'verify', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'scheduled-task', 'verify', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

    # object-collection-rule renamed commands
    def test_object_collection_rule_renamed_commands(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-object-collection-rule'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'object-collection-rule'])
        assert """Usage: oci log-analytics object-collection-rule [OPTIONS]""" in result.output

    # object-collection-rule flattened params
    def test_object_collection_rule_flattened_params(self):
        result = util.invoke_command(['log-analytics', 'object-collection-rule', 'get', '--log-analytics-object-collection-rule-id'])
        assert 'Error: no such option: --log-analytics-object-collection-rule-id' in result.output

        result = util.invoke_command(['log-analytics', 'object-collection-rule', 'delete', '--log-analytics-object-collection-rule-id'])
        assert 'Error: no such option: --log-analytics-object-collection-rule-id' in result.output

        result = util.invoke_command(['log-analytics', 'object-collection-rule', 'update', '--log-analytics-object-collection-rule-id'])
        assert 'Error: no such option: --log-analytics-object-collection-rule-id' in result.output

        result = util.invoke_command(['log-analytics', 'object-collection-rule', 'change-compartment', '--log-analytics-object-collection-rule-id'])
        assert 'Error: no such option: --log-analytics-object-collection-rule-id' in result.output

        result = util.invoke_command(['log-analytics', 'object-collection-rule', 'get', '--object-collection-rule-id'])
        assert 'Error: --object-collection-rule-id option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'object-collection-rule', 'delete', '--object-collection-rule-id'])
        assert 'Error: --object-collection-rule-id option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'object-collection-rule', 'update', '--object-collection-rule-id'])
        assert 'Error: --object-collection-rule-id option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'object-collection-rule', 'change-compartment', '--object-collection-rule-id'])
        assert 'Error: --object-collection-rule-id option requires an argument' in result.output

    # list-supported-char-encodings renamed command
    def test_list_supported_char_encodings_flattened_params(self):
        result = util.invoke_command(['log-analytics', 'char-encoding-collection', 'list-supported-char-encodings'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'char-encoding-collection', 'list-supported-encodings'])
        assert """Usage: oci log-analytics char-encoding-collection list-supported-encodings \n           [OPTIONS]""" in result.output

    # upload-log-file flattened params
    def test_upload_log_file_flattened_params(self):
        result = util.invoke_command(['log-analytics', 'upload', 'upload-log-file', '--upload-log-file-body'])
        assert 'Error: no such option: --upload-log-file-body' in result.output

        result = util.invoke_command(['log-analytics', 'upload', 'upload-log-file', '--file'])
        assert 'Error: --file option requires an argument' in result.output

    # upload-log-events-file flattened params
    def test_upload_log_events_file_flattened_params(self):
        result = util.invoke_command(['log-analytics', 'upload', 'upload-log-events-file', '--upload-log-events-file-details'])
        assert 'Error: no such option: --upload-log-events-file-details' in result.output

        result = util.invoke_command(['log-analytics', 'upload', 'upload-log-events-file', '--file'])
        assert 'Error: --file option requires an argument' in result.output

    # get-unprocessed-bucket renamed command
    def test_get_unprocessed_bucket_renamed_command(self):
        result = util.invoke_command(['log-analytics', 'upload', 'get-unprocessed-data-bucket'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'upload', 'get-unprocessed-bucket'])
        assert """Usage: oci log-analytics upload get-unprocessed-bucket [OPTIONS]""" in result.output

    # set-unprocessed-bucket renamed command
    def test_set_unprocessed_bucket_renamed_command(self):
        result = util.invoke_command(['log-analytics', 'upload', 'set-unprocessed-data-bucket'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'upload', 'set-unprocessed-bucket'])
        assert """Usage: oci log-analytics upload set-unprocessed-bucket [OPTIONS]""" in result.output

    # upload namespace aliases
    def test_upload_namespace_aliases(self):
        result = util.invoke_command(['log-analytics', 'upload', 'upload-log-file', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'upload', 'upload-log-file', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'upload', 'upload-log-file', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'upload', 'list', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'upload', 'list', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'upload', 'list', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'upload', 'get', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'upload', 'get', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'upload', 'get', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'upload', 'delete', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'upload', 'delete', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'upload', 'delete', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'upload', 'list-upload-files', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'upload', 'list-upload-files', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'upload', 'list-upload-files', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'upload', 'delete-upload-file', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'upload', 'delete-upload-file', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'upload', 'delete-upload-file', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'upload', 'list-upload-warnings', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'upload', 'list-upload-warnings', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'upload', 'list-upload-warnings', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'upload', 'delete-upload-warning', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'upload', 'delete-upload-warning', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'upload', 'delete-upload-warning', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'upload', 'validate-source-mapping', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'upload', 'validate-source-mapping', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'upload', 'validate-source-mapping', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'upload', 'validate-file', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'upload', 'validate-file', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'upload', 'validate-file', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'char-encoding-collection', 'list-supported-encodings', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'char-encoding-collection', 'list-supported-encodings', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'char-encoding-collection', 'list-supported-encodings', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'timezone-collection', 'list-supported-timezones', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'timezone-collection', 'list-supported-timezones', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'timezone-collection', 'list-supported-timezones', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'object-collection-rule', 'create', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'object-collection-rule', 'create', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'object-collection-rule', 'create', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'object-collection-rule', 'list', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'object-collection-rule', 'list', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'object-collection-rule', 'list', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'object-collection-rule', 'get', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'object-collection-rule', 'get', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'object-collection-rule', 'get', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'object-collection-rule', 'update', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'object-collection-rule', 'update', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'object-collection-rule', 'update', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'object-collection-rule', 'delete', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'object-collection-rule', 'delete', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'object-collection-rule', 'delete', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'object-collection-rule', 'change-compartment', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'object-collection-rule', 'change-compartment', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'object-collection-rule', 'change-compartment', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'upload', 'upload-log-events-file', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'upload', 'upload-log-events-file', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'upload', 'upload-log-events-file', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'upload', 'get-unprocessed-bucket', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'upload', 'get-unprocessed-bucket', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'upload', 'get-unprocessed-bucket', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'upload', 'set-unprocessed-bucket', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'upload', 'set-unprocessed-bucket', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'upload', 'set-unprocessed-bucket', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

    # log analytics entity type renamed root group command
    def test_entity_type_renamed_commands(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-entity-type'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'entity-type'])
        assert """Usage: oci log-analytics entity-type [OPTIONS] COMMAND [ARGS]""" in result.output

    def test_entity_type_flattened_params(self):
        result = util.invoke_command(['log-analytics', 'entity-type', 'get', '--entity-type-name'])
        assert 'Error: no such option: --entity-type-name' in result.output

        result = util.invoke_command(['log-analytics', 'entity-type', 'delete', '--entity-type-name'])
        assert 'Error: no such option: --entity-type-name' in result.output

        result = util.invoke_command(['log-analytics', 'entity-type', 'update', '--entity-type-name'])
        assert 'Error: no such option: --entity-type-name' in result.output

    # log analytics entity renamed root group command and entity commands
    def test_entity_renamed_commands(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-entity'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'entity'])
        assert """Usage: oci log-analytics entity [OPTIONS] COMMAND [ARGS]""" in result.output

        result = util.invoke_command(['log-analytics', 'log-analytics-entity', 'add'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'entity', 'add-associations'])
        assert """Usage: oci log-analytics entity add-associations [OPTIONS]""" in result.output

        result = util.invoke_command(['log-analytics', 'log-analytics-entity', 'get-log-analytics-entities-summary'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'entity', 'summary'])
        assert """Usage: oci log-analytics entity summary [OPTIONS]""" in result.output

        result = util.invoke_command(['log-analytics', 'log-analytics-entity', 'list-entity-associations'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'entity', 'list-associations'])
        assert """Usage: oci log-analytics entity list-associations [OPTIONS]""" in result.output

        result = util.invoke_command(['log-analytics', 'log-analytics-entity', 'remove'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'entity', 'remove-associations'])
        assert """Usage: oci log-analytics entity remove-associations [OPTIONS]""" in result.output

    def test_entity_flattened_params(self):
        result = util.invoke_command(['log-analytics', 'entity', 'change-compartment', '--log-analytics-entity-id'])
        assert 'Error: no such option: --log-analytics-entity-id' in result.output

        result = util.invoke_command(['log-analytics', 'entity', 'create', '--log-analytics-entity-id'])
        assert 'Error: no such option: --log-analytics-entity-id' in result.output

        result = util.invoke_command(['log-analytics', 'entity', 'delete', '--log-analytics-entity-id'])
        assert 'Error: no such option: --log-analytics-entity-id' in result.output

        result = util.invoke_command(['log-analytics', 'entity', 'get', '--log-analytics-entity-id'])
        assert 'Error: no such option: --log-analytics-entity-id' in result.output

        result = util.invoke_command(['log-analytics', 'entity', 'list', '--is_management_agent_id_null'])
        assert 'Error: no such option: --is_management_agent_id_null' in result.output

        result = util.invoke_command(['log-analytics', 'entity', 'update', '--management_agent_id'])
        assert 'Error: no such option: --management_agent_id' in result.output

        result = util.invoke_command(['log-analytics', 'entity', 'update', '--log-analytics-entity-id'])
        assert 'Error: no such option: --log-analytics-entity-id' in result.output

        result = util.invoke_command(['log-analytics', 'entity', 'add-associations', '--log-analytics-entity-id'])
        assert 'Error: no such option: --log-analytics-entity-id' in result.output

        result = util.invoke_command(['log-analytics', 'entity', 'list-associations', '--direct_or_all_associations'])
        assert 'Error: no such option: --direct_or_all_associations' in result.output

        result = util.invoke_command(['log-analytics', 'entity', 'list-associations', '--log-analytics-entity-id'])
        assert 'Error: no such option: --log-analytics-entity-id' in result.output

        result = util.invoke_command(['log-analytics', 'entity', 'remove-associations', '--log-analytics-entity-id'])
        assert 'Error: no such option: --log-analytics-entity-id' in result.output

    # log analytics em-bridge renamed root group command and em-bridge commands
    def test_em_bridge_renamed_commands(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-em-bridge'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'em-bridge'])
        assert """Usage: oci log-analytics em-bridge [OPTIONS] COMMAND [ARGS]""" in result.output

        result = util.invoke_command(['log-analytics', 'log-analytics-em-bridge', 'get-log-analytics-em-bridge-summary'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'em-bridge', 'summary'])
        assert """Usage: oci log-analytics em-bridge summary [OPTIONS]""" in result.output

    def test_em_bridge_flattened_params(self):
        result = util.invoke_command(['log-analytics', 'em-bridge', 'change-compartment', '--log-analytics-em-bridge-id'])
        assert 'Error: no such option: --log-analytics-em-bridge-id' in result.output

        result = util.invoke_command(['log-analytics', 'em-bridge', 'create', '--log-analytics-em-bridge-id'])
        assert 'Error: no such option: --log-analytics-em-bridge-id' in result.output

        result = util.invoke_command(['log-analytics', 'em-bridge', 'delete', '--log-analytics-em-bridge-id'])
        assert 'Error: no such option: --log-analytics-em-bridge-id' in result.output

        result = util.invoke_command(['log-analytics', 'em-bridge', 'get', '--log-analytics-em-bridge-id'])
        assert 'Error: no such option: --log-analytics-em-bridge-id' in result.output

        result = util.invoke_command(['log-analytics', 'em-bridge', 'update', '--log-analytics-em-bridge-id'])
        assert 'Error: no such option: --log-analytics-em-bridge-id' in result.output

    # namespace aliases
    def test_em_bridge_namespace_aliases(self):
        result = util.invoke_command(['log-analytics', 'em-bridge', 'change-compartment', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'em-bridge', 'change-compartment', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'em-bridge', 'change-compartment', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'em-bridge', 'create', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'em-bridge', 'create', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'em-bridge', 'create', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'em-bridge', 'delete', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'em-bridge', 'delete', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'em-bridge', 'delete', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'em-bridge', 'get', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'em-bridge', 'get', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'em-bridge', 'get', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'em-bridge', 'list', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'em-bridge', 'list', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'em-bridge', 'list', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'em-bridge', 'summary', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'em-bridge', 'summary', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'em-bridge', 'summary', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

        result = util.invoke_command(['log-analytics', 'em-bridge', 'update', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'em-bridge', 'update', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'em-bridge', 'update', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

    # log analytics entity-topology renamed commands
    def test_entity_topology_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-entity-summary', 'list-log-analytics-entity-topology'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'entity-topology', 'list'])
        assert """Usage: oci log-analytics entity-topology list""" in result.output

    def test_entity_topology_flattened_params(self):
        result = util.invoke_command(['log-analytics', 'entity-topology', 'list', '--log-analytics-entity-id'])
        assert 'Error: no such option: --log-analytics-entity-id' in result.output

    # log analytics entity-topology namespace aliases
    def test_entity_topology_namespace_aliases(self):
        result = util.invoke_command(['log-analytics', 'entity-topology', 'list', '--namespace-name'])
        assert 'Error: --namespace-name option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'entity-topology', 'list', '--namespace'])
        assert 'Error: --namespace option requires an argument' in result.output
        result = util.invoke_command(['log-analytics', 'entity-topology', 'list', '-ns'])
        assert 'Error: -ns option requires an argument' in result.output

    def test_validate_source_efds_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-source', 'validate-source-extended-field-details'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'source', 'validate-source-extfield-details'])
        assert """Usage: oci log-analytics source validate-source-extfield-details""" in result.output

    def test_get_association_summary_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-association', 'get-association-summary'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'assoc', 'get-assoc-summary'])
        assert """Usage: oci log-analytics assoc get-assoc-summary""" in result.output

    def test_delete_associations_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-association', 'delete-associations '])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'assoc', 'delete-assocs'])
        assert """Usage: oci log-analytics assoc delete-assocs""" in result.output

    def test_list_associated_entities_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-association', 'list-associated-entities'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'assoc', 'list-associated-entities'])
        assert """Usage: oci log-analytics assoc list-associated-entities""" in result.output

    def test_list_entity_source_associations_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-association', 'list-entity-source-associations'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'assoc', 'list-entity-source-assocs'])
        assert """Usage: oci log-analytics assoc list-entity-source-assocs""" in result.output

    def test_list_source_associations_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-association', 'list-source-associations'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'assoc', 'list-source-assocs'])
        assert """Usage: oci log-analytics assoc list-source-assocs""" in result.output

    def test_upsert_associations_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-association', 'upsert-associations'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'assoc', 'upsert-assocs'])
        assert """Usage: oci log-analytics assoc upsert-assocs""" in result.output

    def test_validate_association_parameters_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-association', 'validate-association-parameters'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'assoc', 'validate-assoc-params'])
        assert """Usage: oci log-analytics assoc validate-assoc-params""" in result.output

    def test_export_custom_content_changed_command(self):
        result = util.invoke_command(['log-analytics', 'binary', 'export-custom-content'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'content-export', 'export-custom-content'])
        assert """Usage: oci log-analytics content-export export-custom-content""" in result.output

    def test_get_config_work_request_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-config-work-request', 'get-config-work-request'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'config-work-request', 'get-config-work-request'])
        assert """Usage: oci log-analytics config-work-request get-config-work-request""" in result.output

    def test_list_config_work_requests_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-config-work-request', 'list-config-work-requests'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'config-work-request', 'list-config-work-requests'])
        assert """Usage: oci log-analytics config-work-request list-config-work-requests""" in result.output

    def test_get_field_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-field', 'get-field'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'field', 'get-field'])
        assert """Usage: oci log-analytics field get-field""" in result.output

    def test_get_label_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-label', 'get-label'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'label', 'get-label'])
        assert """Usage: oci log-analytics label get-label""" in result.output

    def test_list_lookups_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-lookup', 'list-lookups'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'lookup', 'list'])
        assert """Usage: oci log-analytics lookup list""" in result.output

    def test_get_lookup_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-lookup', 'get-lookup'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'lookup', 'get'])
        assert """Usage: oci log-analytics lookup get""" in result.output

    def test_update_lookup_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-lookup', 'update-lookup'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'lookup', 'update'])
        assert """Usage: oci log-analytics lookup update""" in result.output

    def test_delete_lookup_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-lookup', 'delete-lookup'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'lookup', 'delete'])
        assert """Usage: oci log-analytics lookup delete""" in result.output

    def test_append_lookup_data_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-lookup', 'append-lookup-data'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'lookup', 'append-data'])
        assert """Usage: oci log-analytics lookup append-data""" in result.output

    def test_update_lookup_data_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-lookup', 'update-lookup-data'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'lookup', 'update-data'])
        assert """Usage: oci log-analytics lookup update-data""" in result.output

    def test_list_warnings_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-warning', 'list-warnings'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'warning', 'list'])
        assert """Usage: oci log-analytics warning list""" in result.output

    def test_suppress_warning_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-warning', 'suppress-warning'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'warning', 'suppress'])
        assert """Usage: oci log-analytics warning suppress""" in result.output

    def test_unsuppress_warning_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-warning', 'unsuppress-warning'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'warning', 'unsuppress'])
        assert """Usage: oci log-analytics warning unsuppress""" in result.output

    def test_get_lookup_summary_changed_command(self):
        result = util.invoke_command(['log-analytics', 'lookup', 'get-lookup-summary'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'lookup', 'get-summary'])
        assert """Usage: oci log-analytics lookup get-summary""" in result.output

    def test_list_source_event_types_changed_command(self):
        result = util.invoke_command(['log-analytics', 'source', 'list-source-event-types'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'source', 'list-event-types'])
        assert """Usage: oci log-analytics source list-event-types""" in result.output

    def test_add_source_event_types_changed_command(self):
        result = util.invoke_command(['log-analytics', 'source', 'add'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'source', 'add-event-types'])
        assert """Usage: oci log-analytics source add-event-types""" in result.output

    def test_enable_source_event_types_changed_command(self):
        result = util.invoke_command(['log-analytics', 'source', 'enable-source-event-types'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'source', 'enable-event-types'])
        assert """Usage: oci log-analytics source enable-event-types""" in result.output

    def test_disable_source_event_types_changed_command(self):
        result = util.invoke_command(['log-analytics', 'source', 'disable-source-event-types'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'source', 'disable-event-types'])
        assert """Usage: oci log-analytics source disable-event-types""" in result.output

    def test_remove_source_event_types_changed_command(self):
        result = util.invoke_command(['log-analytics', 'source', 'remove'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'source', 'remove-event-types'])
        assert """Usage: oci log-analytics source remove-event-types""" in result.output

    def test_list_auto_associations_changed_command(self):
        result = util.invoke_command(['log-analytics', 'source', 'list-auto-associations'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'source', 'list-auto-assocs'])
        assert """Usage: oci log-analytics source list-auto-assocs""" in result.output

    def test_enable_auto_association_changed_command(self):
        result = util.invoke_command(['log-analytics', 'source', 'enable-auto-association'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'source', 'enable-auto-assoc'])
        assert """Usage: oci log-analytics source enable-auto-assoc""" in result.output

    def test_disable_auto_association_changed_command(self):
        result = util.invoke_command(['log-analytics', 'source', 'disable-auto-association'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'source', 'disable-auto-assoc'])
        assert """Usage: oci log-analytics source disable-auto-assoc""" in result.output

    def test_get_preferences_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-preference', 'get-preferences'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'preference', 'get'])
        assert """Usage: oci log-analytics preference get""" in result.output

    def test_remove_preferences_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-preference', 'remove'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'preference', 'remove'])
        assert """Usage: oci log-analytics preference remove""" in result.output

    def test_update_preferences_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-preference', 'update-preferences'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'preference', 'update'])
        assert """Usage: oci log-analytics preference update""" in result.output

    def test_list_categories_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-category', 'list-categories'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'category', 'list'])
        assert """Usage: oci log-analytics category list""" in result.output

    def test_get_category_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-category', 'get-category'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'category', 'get'])
        assert """Usage: oci log-analytics category get""" in result.output

    def test_list_resource_categories_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-category', 'list-resource-categories'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'category', 'list-resource-category'])
        assert """Usage: oci log-analytics category list-resource-category""" in result.output

    def test_remove_resource_categories_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-category', 'remove'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'category', 'remove-resource-category'])
        assert """Usage: oci log-analytics category remove-resource-category""" in result.output

    def test_update_resource_categories_changed_command(self):
        result = util.invoke_command(['log-analytics', 'log-analytics-category', 'update-resource-categories'])
        assert 'No such command' in result.output

        result = util.invoke_command(['log-analytics', 'category', 'update-resource-category'])
        assert """Usage: oci log-analytics category update-resource-category""" in result.output

    def test_get_log_group_removed_id_param(self):
        result = util.invoke_command(['log-analytics', 'log-group', 'get', '--log-analytics-log-group-id'])
        assert 'Error: no such option: --log-analytics-log-group-id' in result.output

    def test_update_log_group_removed_id_param(self):
        result = util.invoke_command(['log-analytics', 'log-group', 'update', '--log-analytics-log-group-id'])
        assert 'Error: no such option: --log-analytics-log-group-id' in result.output

    def test_change_log_group_compartment_removed_id_param(self):
        result = util.invoke_command(['log-analytics', 'log-group', 'change-compartment', '--log-analytics-log-group-id'])
        assert 'Error: no such option: --log-analytics-log-group-id' in result.output

    def test_delete_log_group_removed_id_param(self):
        result = util.invoke_command(['log-analytics', 'log-group', 'delete', '--log-analytics-log-group-id'])
        assert 'Error: no such option: --log-analytics-log-group-id' in result.output

    def test_list_associated_entities_removed_dname_param(self):
        result = util.invoke_command(['log-analytics', 'assoc', 'list-associated-entities', '--entity-type-display-name'])
        assert 'Error: no such option: --entity-type-display-name' in result.output

    def test_list_entity_source_assocs_removed_dname_param(self):
        result = util.invoke_command(['log-analytics', 'assoc', 'list-entity-source-assocs', '--entity-type-display-name'])
        assert 'Error: no such option: --entity-type-display-name' in result.output

    def test_import_custom_content_removed_params(self):
        result = util.invoke_command(['log-analytics', 'content-import', 'import-custom-content', '--import-custom-content-file-body'])
        assert 'Error: no such option: --import-custom-content-file-body' in result.output

        result = util.invoke_command(['log-analytics', 'content-import', 'import-custom-content', '--file'])
        assert 'Error: --file option requires an argument' in result.output

    def test_register_lookup_removed_params(self):
        result = util.invoke_command(['log-analytics', 'lookup', 'register-lookup', '--register-lookup-content-file-body'])
        assert 'Error: no such option: --register-lookup-content-file-body' in result.output

        result = util.invoke_command(['log-analytics', 'lookup', 'register-lookup', '--file'])
        assert 'Error: --file option requires an argument' in result.output

    def test_append_lookup_removed_params(self):
        result = util.invoke_command(['log-analytics', 'lookup', 'append-data', '--append-lookup-file-body'])
        assert 'Error: no such option: --append-lookup-file-body' in result.output

        result = util.invoke_command(['log-analytics', 'lookup', 'append-data', '--file'])
        assert 'Error: --file option requires an argument' in result.output

    def test_update_lookup_removed_params(self):
        result = util.invoke_command(['log-analytics', 'lookup', 'update-data', '--update-lookup-file-body'])
        assert 'Error: no such option: --update-lookup-file-body' in result.output

        result = util.invoke_command(['log-analytics', 'lookup', 'update-data', '--file'])
        assert 'Error: --file option requires an argument' in result.output

    def test_extract_field_paths_removed_params(self):
        result = util.invoke_command(['log-analytics', 'parser', 'extract-structured-log-field-paths', '--parser-ignoreline-characters'])
        assert 'Error: no such option: --parser-ignoreline-characters' in result.output

        result = util.invoke_command(['log-analytics', 'parser', 'extract-structured-log-field-paths', '--should-tokenize-original-text'])
        assert 'Error: no such option: --should-tokenize-original-text' in result.output

    def test_extract_header_paths_removed_params(self):
        result = util.invoke_command(['log-analytics', 'parser', 'extract-structured-log-header-paths', '--parser-ignoreline-characters'])
        assert 'Error: no such option: --parser-ignoreline-characters' in result.output

        result = util.invoke_command(['log-analytics', 'parser', 'extract-structured-log-header-paths', '--should-tokenize-original-text'])
        assert 'Error: no such option: --should-tokenize-original-text' in result.output

    def test_test_parser_removed_params(self):
        result = util.invoke_command(['log-analytics', 'parser', 'test-parser', '--parser-ignoreline-characters'])
        assert 'Error: no such option: --parser-ignoreline-characters' in result.output

        result = util.invoke_command(['log-analytics', 'parser', 'test-parser', '--should-tokenize-original-text'])
        assert 'Error: no such option: --should-tokenize-original-text' in result.output

    def test_upsert_parser_removed_params(self):
        result = util.invoke_command(['log-analytics', 'parser', 'upsert-parser', '--parser-ignoreline-characters'])
        assert 'Error: no such option: --parser-ignoreline-characters' in result.output

        result = util.invoke_command(['log-analytics', 'parser', 'upsert-parser', '--should-tokenize-original-text'])
        assert 'Error: no such option: --should-tokenize-original-text' in result.output

    def test_upsert_source_removed_efdns_param(self):
        result = util.invoke_command(['log-analytics', 'source', 'upsert-source', '--extended-field-definitions'])
        assert 'Error: no such option: --extended-field-definitions' in result.output

    def test_validate_source_removed_efdns_param(self):
        result = util.invoke_command(['log-analytics', 'source', 'validate-source', '--extended-field-definitions'])
        assert 'Error: no such option: --extended-field-definitions' in result.output

    def test_validate_source_efds_removed_params(self):
        result = util.invoke_command(['log-analytics', 'source', 'validate-source-extfield-details', '--association-count'])
        assert 'Error: no such option: --association-count' in result.output

        result = util.invoke_command(['log-analytics', 'source', 'validate-source-extfield-details', '--association-entity'])
        assert 'Error: no such option: --association-entity' in result.output

        result = util.invoke_command(['log-analytics', 'source', 'validate-source-extfield-details', '--extended-field-definitions'])
        assert 'Error: no such option: --extended-field-definitions' in result.output

        result = util.invoke_command(['log-analytics', 'source', 'validate-source-extfield-details', '--is-auto-association-enabled'])
        assert 'Error: no such option: --is-auto-association-enabled' in result.output

        result = util.invoke_command(['log-analytics', 'source', 'validate-source-extfield-details', '--is-auto-association-override'])
        assert 'Error: no such option: --is-auto-association-override' in result.output

    # Ingest time Rule test removed create command
    def test_ingest_time_rule_removed_create_command(self):
        # removed create
        result = util.invoke_command(['log-analytics', 'ingest-time-rule', 'create-ingest-time-rule-ingest-time-rule-field-condition'])
        assert 'No such command' in result.output

    # Ingest time Rule test removed update command
    def test_ingest_time_rule_removed_update_command(self):
        # removed update
        result = util.invoke_command(['log-analytics', 'ingest-time-rule', 'update-ingest-time-rule-ingest-time-rule-field-condition'])
        assert 'No such command' in result.output

    # Recall archived data test renamed param
    def test_recall_archived_data_renamed_params(self):
        result = util.invoke_command(['log-analytics', 'storage', 'recall-archived-data', '--query-parameterconflict'])
        assert 'Error: no such option: --query-parameterconflict' in result.output

        result = util.invoke_command(['log-analytics', 'storage', 'recall-archived-data', '--query-string'])
        assert 'Error: --query-string option requires an argument' in result.output
