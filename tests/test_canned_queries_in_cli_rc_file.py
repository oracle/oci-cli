# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from . import util
from . import test_config_container

import json
import os
import os.path
import pytest
import time


@pytest.fixture(scope="module")
def default_file_with_canned_queries():
    default_file_path = os.path.join('tests', 'temp', 'default_file_canned_queries_{}'.format(int(time.time())))
    if not os.path.exists(os.path.dirname(default_file_path)):
        os.makedirs(os.path.dirname(default_file_path))

    invoke(['setup', 'oci-cli-rc', '--file', default_file_path])

    yield default_file_path

    os.remove(default_file_path)


def test_query_when_listing_and_getting_instances(default_file_with_canned_queries):
    with test_config_container.create_vcr().use_cassette('test_canned_queries_listing_getting_instances.yml'):
        result = invoke(['compute', 'instance', 'list', '-c', util.COMPARTMENT_ID, '--query', 'query://get_id_and_display_name_from_list', '--defaults-file', default_file_with_canned_queries])
        assert result.exit_code == 0

        if result.output != '':
            parsed_result = json.loads(result.output)
            for d in parsed_result:
                keys = d.keys()
                assert len(keys) == 2
                assert 'id' in d.keys()
                assert 'display-name' in d.keys()

            if len(parsed_result) > 0:
                instance_id = parsed_result[0]['id']

                result = invoke(['compute', 'instance', 'get', '--instance-id', instance_id, '--query', 'query://get_id_and_display_name_from_single_result', '--defaults-file', default_file_with_canned_queries])
                assert result.exit_code == 0

                parsed_result = json.loads(result.output)
                assert len(parsed_result.keys()) == 2
                assert 'id' in parsed_result.keys()
                assert 'display-name' in parsed_result.keys()

                result = invoke(['compute', 'instance', 'get', '--instance-id', instance_id])
                parsed_result = json.loads(result.output)
                expected_string = '"{},{}'.format(parsed_result['data']['id'], parsed_result['data']['display-name'])

                result = invoke(['compute', 'instance', 'get', '--instance-id', instance_id, '--query', 'query://get_id_display_name_and_lifecycle_state_from_single_result_as_csv', '--defaults-file', default_file_with_canned_queries])
                assert result.exit_code == 0
                assert expected_string in result.output

            result = invoke(['compute', 'instance', 'list', '-c', util.COMPARTMENT_ID])
            parsed_result = json.loads(result.output)

            expected_result = []
            for d in parsed_result['data']:
                expected_result.append('"{},{}'.format(d['id'], d['display-name']))

            result = invoke(['compute', 'instance', 'list', '-c', util.COMPARTMENT_ID, '--query', 'query://get_id_display_name_and_lifecycle_state_from_list_as_csv', '--defaults-file', default_file_with_canned_queries])
            assert result.exit_code == 0

            result = invoke(['compute', 'instance', 'list', '-c', util.COMPARTMENT_ID, '--query', 'query://get_top_5_results', '--defaults-file', default_file_with_canned_queries])
            assert result.exit_code == 0
            parsed_result = json.loads(result.output)
            assert len(parsed_result) <= 5  # no guarantee of the exact number of results, but our JMESPath query shouldn't return any more than 5

            result = invoke(['compute', 'instance', 'list', '-c', util.COMPARTMENT_ID, '--query', 'query://get_last_2_results', '--defaults-file', default_file_with_canned_queries])
            assert result.exit_code == 0
            parsed_result = json.loads(result.output)
            assert len(parsed_result) <= 2  # no guarantee of the exact number of results, but our JMESPath query shouldn't return any more than 2

        # The display name we're matching on is junk, so should not match any result
        result = invoke(['compute', 'instance', 'list', '-c', util.COMPARTMENT_ID, '--query', 'query://filter_by_display_name_contains_text', '--defaults-file', default_file_with_canned_queries])
        assert result.exit_code == 0
        if result.output != '':
            assert 'Query returned empty result, no output to show' in result.output

        result = invoke(['compute', 'instance', 'list', '-c', util.COMPARTMENT_ID, '--query', 'query://filter_by_display_name_contains_text_and_get_attributes', '--defaults-file', default_file_with_canned_queries])
        assert result.exit_code == 0
        if result.output != '':
            assert 'Query returned empty result, no output to show' in result.output


def test_query_does_not_exist(default_file_with_canned_queries):
    result = invoke(['compute', 'instance', 'list', '-c', util.COMPARTMENT_ID, '--query', 'query://purple_monkey_dishwasher', '--defaults-file', default_file_with_canned_queries])
    assert 'Query {} is not defined in your OCI CLI configuration file: {}'.format('purple_monkey_dishwasher', default_file_with_canned_queries) in result.output


def invoke(commands, debug=False, **args):
    if debug is True:
        commands = ['--debug'] + commands

    return util.invoke_command(commands, **args)
