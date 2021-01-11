# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import oci_cli
import os
import time
import random
from tests import tag_data_container
from tests import test_config_container
from tests import util

CASSETTE_LIBRARY_DIR = 'services/identity/tests/cassettes'


@util.slow
def test_update_retire_reactivate_namespace_and_tag(identity_client, tag_namespace_and_tags):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('tag_management.yml'):
        if os.environ.get('OCI_CLI_TAG_MGMT_USE_EXISTING_TAG_AND_NAMESPACE'):
            tag_namespace_id = tag_data_container.tag_namespace.id
            tag_name = tag_data_container.tags[0].name
            print('Reusing existing tag namespace {} and tag {}'.format(tag_namespace_id, tag_name))

            tag_data_container.ensure_namespace_and_tags_active(invoke)
        else:
            suffix = str(random.randint(1, int(time.time())))
            namespace_name = ('cliTagNamespace_{}'.format(suffix)).lower()
            tag_name = ('cliTag_{}'.format(suffix)).lower()

            result = invoke(['iam', 'tag-namespace', 'create', '-c', util.COMPARTMENT_ID, '--name', namespace_name, '--description', 'initial description'])
            util.validate_response(result)
            parsed_result = json.loads(result.output)
            tag_namespace_id = parsed_result['data']['id']
            assert namespace_name == parsed_result['data']['name']
            assert 'initial description' == parsed_result['data']['description']
            assert not parsed_result['data']['is-retired']

            result = invoke(['iam', 'tag', 'create', '--tag-namespace-id', tag_namespace_id, '--name', tag_name, '--description', 'tag description'])
            util.validate_response(result)
            parsed_result = json.loads(result.output)
            assert tag_name == parsed_result['data']['name']
            assert 'tag description' == parsed_result['data']['description']
            assert not parsed_result['data']['is-retired']

        apply_tags_to_tag_namespace(tag_namespace_id)
        apply_tags_to_tag(tag_namespace_id, tag_name)
        update_retire_reactivate_operations(tag_namespace_id, tag_name)
        get_and_list_operations(identity_client, tag_namespace_id, tag_name)


def apply_tags_to_tag_namespace(tag_namespace_id):
    tag_data_container.ensure_namespace_and_tags_active(invoke)

    tag_names_to_values = {
        tag_data_container.tags[0].name: 'tag_ns_mgmt {}'.format(util.random_number_string())
    }
    tag_data_container.write_defined_tags_to_file(
        os.path.join('tests', 'temp', 'defined_tags_mgmt.json'),
        tag_data_container.tag_namespace,
        tag_names_to_values
    )

    # Apply tags
    expected_freeform = {'tagOne': 'value three'}
    expected_defined = {tag_data_container.tag_namespace.name: tag_names_to_values}
    result = invoke([
        'iam', 'tag-namespace', 'update',
        '--tag-namespace-id', tag_namespace_id,
        '--freeform-tags', 'file://tests/resources/tagging/freeform_tags_2.json',
        '--defined-tags', 'file://tests/temp/defined_tags_mgmt.json',
        '--force'
    ])
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    assert expected_freeform == parsed_result['data']['freeform-tags']
    assert expected_defined == parsed_result['data']['defined-tags']

    result = invoke(['iam', 'tag-namespace', 'get', '--tag-namespace-id', tag_namespace_id])
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    assert expected_freeform == parsed_result['data']['freeform-tags']
    assert expected_defined == parsed_result['data']['defined-tags']

    result = invoke(['iam', 'tag-namespace', 'list', '-c', util.COMPARTMENT_ID, '--all'])
    parsed_result = json.loads(result.output)
    found_namespace = False
    for pr in parsed_result['data']:
        if pr['id'] == tag_namespace_id:
            assert expected_freeform == pr['freeform-tags']
            assert expected_defined == pr['defined-tags']
            found_namespace = True
            break
    assert found_namespace

    # Overwrite with different tags
    tag_names_to_values = {
        tag_data_container.tags[1].name: 'tag_ns_mgmt update {}'.format(util.random_number_string())
    }
    tag_data_container.write_defined_tags_to_file(
        os.path.join('tests', 'temp', 'defined_tags_mgmt.json'),
        tag_data_container.tag_namespace,
        tag_names_to_values
    )
    expected_freeform = {'tagOne': 'value1', 'tag_Two': 'value two'}
    expected_defined = {tag_data_container.tag_namespace.name: tag_names_to_values}
    result = invoke([
        'iam', 'tag-namespace', 'update',
        '--tag-namespace-id', tag_namespace_id,
        '--freeform-tags', 'file://tests/resources/tagging/freeform_tags_1.json',
        '--defined-tags', 'file://tests/temp/defined_tags_mgmt.json',
        '--force'
    ])
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    assert expected_freeform == parsed_result['data']['freeform-tags']
    assert expected_defined == parsed_result['data']['defined-tags']

    result = invoke(['iam', 'tag-namespace', 'get', '--tag-namespace-id', tag_namespace_id])
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    assert expected_freeform == parsed_result['data']['freeform-tags']
    assert expected_defined == parsed_result['data']['defined-tags']

    # Clear tags
    result = invoke([
        'iam', 'tag-namespace', 'update',
        '--tag-namespace-id', tag_namespace_id,
        '--freeform-tags', '{}',
        '--defined-tags', '{}',
        '--force'
    ])
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    assert {} == parsed_result['data']['freeform-tags']
    assert {} == parsed_result['data']['defined-tags']

    result = invoke(['iam', 'tag-namespace', 'get', '--tag-namespace-id', tag_namespace_id])
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    assert {} == parsed_result['data']['freeform-tags']
    assert {} == parsed_result['data']['defined-tags']

    result = invoke(['iam', 'tag-namespace', 'list', '-c', util.COMPARTMENT_ID, '--all'])
    parsed_result = json.loads(result.output)
    found_namespace = False
    for pr in parsed_result['data']:
        if pr['id'] == tag_namespace_id:
            assert {} == pr['freeform-tags']
            assert {} == pr['defined-tags']
            found_namespace = True
            break
    assert found_namespace


def apply_tags_to_tag(tag_namespace_id, tag_name):
    tag_data_container.ensure_namespace_and_tags_active(invoke)

    tag_names_to_values = {}
    for t in tag_data_container.tags:
        tag_names_to_values[t.name] = 'tag_mgmt {}'.format(util.random_number_string())
    tag_data_container.write_defined_tags_to_file(
        os.path.join('tests', 'temp', 'defined_tags_mgmt.json'),
        tag_data_container.tag_namespace,
        tag_names_to_values
    )

    # Apply tags
    expected_freeform = {'tagOne': 'value1', 'tag_Two': 'value two'}
    expected_defined = {tag_data_container.tag_namespace.name: tag_names_to_values}
    result = invoke([
        'iam', 'tag', 'update',
        '--tag-namespace-id', tag_namespace_id,
        '--tag-name', tag_name,
        '--freeform-tags', 'file://tests/resources/tagging/freeform_tags_1.json',
        '--defined-tags', 'file://tests/temp/defined_tags_mgmt.json',
        '--force'
    ])
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    assert expected_freeform == parsed_result['data']['freeform-tags']
    assert expected_defined == parsed_result['data']['defined-tags']

    result = invoke([
        'iam', 'tag', 'get',
        '--tag-namespace-id', tag_namespace_id,
        '--tag-name', tag_name
    ])
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    assert expected_freeform == parsed_result['data']['freeform-tags']
    assert expected_defined == parsed_result['data']['defined-tags']

    result = invoke(['iam', 'tag', 'list', '--tag-namespace-id', tag_namespace_id, '--all'])
    parsed_result = json.loads(result.output)
    found_tag = False
    for pr in parsed_result['data']:
        if pr['name'] == tag_name:
            assert expected_freeform == pr['freeform-tags']
            assert expected_defined == pr['defined-tags']
            found_tag = True
            break
    assert found_tag

    # Overwrite with different tags
    tag_names_to_values.pop(tag_data_container.tags[0].name)
    tag_data_container.write_defined_tags_to_file(
        os.path.join('tests', 'temp', 'defined_tags_mgmt.json'),
        tag_data_container.tag_namespace,
        tag_names_to_values
    )
    expected_freeform = {'tagOne': 'value three'}
    expected_defined = {tag_data_container.tag_namespace.name: tag_names_to_values}
    result = invoke([
        'iam', 'tag', 'update',
        '--tag-namespace-id', tag_namespace_id,
        '--tag-name', tag_name,
        '--freeform-tags', 'file://tests/resources/tagging/freeform_tags_2.json',
        '--defined-tags', 'file://tests/temp/defined_tags_mgmt.json',
        '--force'
    ])
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    assert expected_freeform == parsed_result['data']['freeform-tags']
    assert expected_defined == parsed_result['data']['defined-tags']

    result = invoke([
        'iam', 'tag', 'get',
        '--tag-namespace-id', tag_namespace_id,
        '--tag-name', tag_name
    ])
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    assert expected_freeform == parsed_result['data']['freeform-tags']
    assert expected_defined == parsed_result['data']['defined-tags']

    # Clear tags
    result = invoke([
        'iam', 'tag', 'update',
        '--tag-namespace-id', tag_namespace_id,
        '--tag-name', tag_name,
        '--freeform-tags', '{}',
        '--defined-tags', '{}',
        '--force'
    ])
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    assert {} == parsed_result['data']['freeform-tags']
    assert {} == parsed_result['data']['defined-tags']

    result = invoke([
        'iam', 'tag', 'get',
        '--tag-namespace-id', tag_namespace_id,
        '--tag-name', tag_name
    ])
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    assert {} == parsed_result['data']['freeform-tags']
    assert {} == parsed_result['data']['defined-tags']

    result = invoke(['iam', 'tag', 'list', '--tag-namespace-id', tag_namespace_id, '--all'])
    parsed_result = json.loads(result.output)
    found_tag = False
    for pr in parsed_result['data']:
        if pr['name'] == tag_name:
            assert {} == pr['freeform-tags']
            assert {} == pr['defined-tags']
            found_tag = True
            break
    assert found_tag


def update_retire_reactivate_operations(tag_namespace_id, tag_name):
    result = invoke(['iam', 'tag-namespace', 'update', '--tag-namespace-id', tag_namespace_id, '--description', 'updated description'])
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    assert 'updated description' == parsed_result['data']['description']
    assert not parsed_result['data']['is-retired']

    result = invoke(['iam', 'tag', 'update', '--tag-namespace-id', tag_namespace_id, '--tag-name', tag_name, '--description', 'updated tag desc'])
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    assert 'updated tag desc' == parsed_result['data']['description']
    assert not parsed_result['data']['is-retired']

    result = invoke(['iam', 'tag', 'retire', '--tag-namespace-id', tag_namespace_id, '--tag-name', tag_name])
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    assert 'updated tag desc' == parsed_result['data']['description']  # Should not change
    assert parsed_result['data']['is-retired']

    result = invoke(['iam', 'tag', 'reactivate', '--tag-namespace-id', tag_namespace_id, '--tag-name', tag_name])
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    assert 'updated tag desc' == parsed_result['data']['description']  # Should not change
    assert not parsed_result['data']['is-retired']

    result = invoke(['iam', 'tag', 'retire', '--tag-namespace-id', tag_namespace_id, '--tag-name', tag_name])
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    assert parsed_result['data']['is-retired']

    result = invoke(['iam', 'tag-namespace', 'retire', '--tag-namespace-id', tag_namespace_id])
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    assert 'updated description' == parsed_result['data']['description']  # Should not change
    assert parsed_result['data']['is-retired']

    result = invoke(['iam', 'tag-namespace', 'reactivate', '--tag-namespace-id', tag_namespace_id])
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    assert 'updated description' == parsed_result['data']['description']  # Should not change
    assert not parsed_result['data']['is-retired']

    result = invoke(['iam', 'tag-namespace', 'retire', '--tag-namespace-id', tag_namespace_id])
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    assert parsed_result['data']['is-retired']


def get_and_list_operations(identity_client, tag_namespace_id, tag_name):
    result = invoke(['iam', 'tag-namespace', 'get', '--tag-namespace-id', tag_namespace_id])
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    assert 'updated description' == parsed_result['data']['description']
    assert parsed_result['data']['is-retired']

    result = oci_cli.cli_util.list_call_get_all_results(identity_client.list_tag_namespaces, compartment_id=util.COMPARTMENT_ID)
    filtered_results = list(filter(lambda d: d.id == tag_namespace_id, result.data))
    assert len(filtered_results) == 1
    assert 'updated description' == filtered_results[0].description
    assert filtered_results[0].is_retired

    result = invoke(['iam', 'tag-namespace', 'list', '-c', util.COMPARTMENT_ID, '--all'])
    parsed_result = json.loads(result.output)
    found_namespace = False
    for pr in parsed_result['data']:
        if pr['id'] == tag_namespace_id:
            assert 'updated description' == pr['description']
            assert pr['is-retired']
            found_namespace = True
            break
    assert found_namespace

    result = invoke(['iam', 'tag', 'get', '--tag-namespace-id', tag_namespace_id, '--tag-name', tag_name])
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    assert 'updated tag desc' == parsed_result['data']['description']
    assert parsed_result['data']['is-retired']

    result = oci_cli.cli_util.list_call_get_all_results(identity_client.list_tags, tag_namespace_id=tag_namespace_id)
    filtered_results = list(filter(lambda d: d.name == tag_name, result.data))
    assert len(filtered_results) == 1
    assert 'updated tag desc' == filtered_results[0].description
    assert filtered_results[0].is_retired

    result = invoke(['iam', 'tag', 'list', '--tag-namespace-id', tag_namespace_id, '--all'])
    parsed_result = json.loads(result.output)
    found_tag = False
    for pr in parsed_result['data']:
        assert pr['is-retired']  # since the namespace is retired, all tags under it should be retired
        if pr['name'] == tag_name:
            assert 'updated tag desc' == pr['description']
            found_tag = True
            break
    assert found_tag


def invoke(commands, debug=False, ** args):
    if debug is True:
        commands = ['--debug'] + commands

    return util.invoke_command(commands, ** args)
