# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from . import tag_data_container
from . import test_config_container
from . import util

import json
import os.path
import pytest
import time


@pytest.fixture(scope='module')
def network_resources():
    with test_config_container.create_vcr().use_cassette('test_tagging_fixture_network.yml'):
        vcn_name = util.random_name('cli_test_tagging')
        cidr_block = "10.0.0.0/16"
        vcn_dns_label = util.random_name('vcn', insert_underscore=False)

        result = invoke([
            'network', 'vcn', 'create',
            '--compartment-id', util.COMPARTMENT_ID,
            '--display-name', vcn_name,
            '--cidr-block', cidr_block,
            '--dns-label', vcn_dns_label,
            '--wait-for-state', 'AVAILABLE',
            '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS
        ])
        vcn_ocid = util.get_json_from_mixed_string(result.output)['data']['id']

        subnet_name = util.random_name('cli_test_compute_subnet')
        subnet_dns_label = util.random_name('subnet', insert_underscore=False)

        result = invoke([
            'network', 'subnet', 'create',
            '--compartment-id', util.COMPARTMENT_ID,
            '--availability-domain', util.availability_domain(),
            '--display-name', subnet_name,
            '--vcn-id', vcn_ocid,
            '--cidr-block', cidr_block,
            '--dns-label', subnet_dns_label,
            '--wait-for-state', 'AVAILABLE',
            '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS
        ])
        subnet_ocid = util.get_json_from_mixed_string(result.output)['data']['id']

        yield (vcn_ocid, subnet_ocid)

    with test_config_container.create_vcr().use_cassette('test_tagging_fixture_network_delete.yml'):
        result = invoke(['network', 'subnet', 'delete', '--subnet-id', subnet_ocid, '--force', '--wait-for-state', 'TERMINATED', '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS])
        util.validate_response(result, json_response_expected=False)

        result = util.invoke_command(['network', 'vcn', 'delete', '--vcn-id', vcn_ocid, '--force', '--wait-for-state', 'TERMINATED', '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS])
        util.validate_response(result, json_response_expected=False)


@util.slow
def test_launch_update_instance_with_tags(tag_namespace_and_tags, network_resources):
    with test_config_container.create_vcr().use_cassette('test_tagging_instance.yml'):
        tag_data_container.ensure_namespace_and_tags_active(invoke)

        tag_names_to_values = {}
        for t in tag_data_container.tags:
            tag_names_to_values[t.name] = 'launch_instance {}'.format(util.random_number_string())
        tag_data_container.write_defined_tags_to_file(
            os.path.join('tests', 'temp', 'defined_tags_1.json'),
            tag_data_container.tag_namespace,
            tag_names_to_values
        )

        instance_ocid = None
        try:
            # Launch with tags. Because of eventual consistency, we may get a 404 the first time we try a tag and if that happens
            # we should retry
            attempts = 0
            while attempts <= 3:
                result = invoke([
                    'compute', 'instance', 'launch',
                    '--compartment-id', util.COMPARTMENT_ID,
                    '--availability-domain', util.availability_domain(),
                    '--display-name', util.random_name('cli_tag_test_instance'),
                    '--subnet-id', network_resources[1],
                    '--image-id', util.oracle_linux_image(),
                    '--shape', 'VM.Standard1.1',
                    '--wait-for-state', 'RUNNING',
                    '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS,
                    '--freeform-tags', 'file://tests/resources/tagging/freeform_tags_1.json',
                    '--defined-tags', 'file://tests/temp/defined_tags_1.json'
                ])
                if result.exit_code == 0:  # This is a bit coarse-grained. We could also crack open the response and check that it's a 404
                    break
                else:
                    attempts += 1
                    time.sleep(5)
            util.validate_response(result, json_response_expected=False, expect_etag=True)
            instance_data = util.get_json_from_mixed_string(result.output)['data']
            instance_ocid = instance_data['id']

            expected_freeform = {'tagOne': 'value1', 'tag_Two': 'value two'}
            expected_defined = {tag_data_container.tag_namespace.name: tag_names_to_values}
            assert expected_freeform == instance_data['freeform-tags']
            assert expected_defined == instance_data['defined-tags']

            result = invoke([
                'compute', 'instance', 'get',
                '--instance-id', instance_ocid
            ])
            parsed_result = json.loads(result.output)
            assert expected_freeform == parsed_result['data']['freeform-tags']
            assert expected_defined == parsed_result['data']['defined-tags']

            # Update to different tags
            tag_names_to_values.pop(tag_data_container.tags[0].name)
            tag_data_container.write_defined_tags_to_file(
                os.path.join('tests', 'temp', 'defined_tags_1.json'),
                tag_data_container.tag_namespace,
                tag_names_to_values
            )

            attempts = 0
            while attempts <= 3:
                result = invoke([
                    'compute', 'instance', 'update',
                    '--instance-id', instance_ocid,
                    '--freeform-tags', 'file://tests/resources/tagging/freeform_tags_2.json',
                    '--defined-tags', 'file://tests/temp/defined_tags_1.json',
                    '--force'
                ])
                if result.exit_code == 0:
                    break
                else:
                    attempts += 1
                    time.sleep(5)
            util.validate_response(result)
            parsed_result = json.loads(result.output)

            expected_freeform = {'tagOne': 'value three'}
            expected_defined = {tag_data_container.tag_namespace.name: tag_names_to_values}
            assert expected_freeform == parsed_result['data']['freeform-tags']
            assert expected_defined == parsed_result['data']['defined-tags']

            result = invoke([
                'compute', 'instance', 'get',
                '--instance-id', instance_ocid
            ])
            parsed_result = json.loads(result.output)
            assert expected_freeform == parsed_result['data']['freeform-tags']
            assert expected_defined == parsed_result['data']['defined-tags']

            # Nuke tags by passing an empty JSON object
            result = invoke([
                'compute', 'instance', 'update',
                '--instance-id', instance_ocid,
                '--freeform-tags', '{}',
                '--defined-tags', '{}',
                '--force'
            ])
            util.validate_response(result)
            parsed_result = json.loads(result.output)
            assert {} == parsed_result['data']['freeform-tags']
            assert {} == parsed_result['data']['defined-tags']

            result = invoke([
                'compute', 'instance', 'get',
                '--instance-id', instance_ocid
            ])
            parsed_result = json.loads(result.output)
            assert {} == parsed_result['data']['freeform-tags']
            assert {} == parsed_result['data']['defined-tags']
        finally:
            if instance_ocid:
                result = invoke([
                    'compute', 'instance', 'terminate',
                    '--instance-id', instance_ocid,
                    '--force',
                    '--wait-for-state', 'TERMINATED',
                    '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS
                ])
                util.validate_response(result, json_response_expected=False)


@util.slow
def test_create_update_volume_with_tags(tag_namespace_and_tags):
    with test_config_container.create_vcr().use_cassette('test_tagging_volume.yml'):
        tag_data_container.ensure_namespace_and_tags_active(invoke)

        tag_names_to_values = {}
        tag_names_to_values[tag_data_container.tags[0].name] = 'create_volume {}'.format(util.random_number_string())
        tag_data_container.write_defined_tags_to_file(
            os.path.join('tests', 'temp', 'defined_tags_1.json'),
            tag_data_container.tag_namespace,
            tag_names_to_values
        )

        volume_id = None
        try:
            # Create with tags
            volume_name = util.random_name('cli_test_volume')

            attempts = 0
            while attempts <= 3:
                result = invoke([
                    'bv', 'volume', 'create',
                    '--availability-domain', util.availability_domain(),
                    '--compartment-id', util.COMPARTMENT_ID,
                    '--display-name', volume_name,
                    '--size-in-gbs', '50',
                    '--freeform-tags', 'file://tests/resources/tagging/freeform_tags_2.json',
                    '--defined-tags', 'file://tests/temp/defined_tags_1.json',
                    '--wait-for-state', 'AVAILABLE',
                    '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS
                ])
                if result.exit_code == 0:
                    break
                else:
                    attempts += 1
                    time.sleep(5)
            util.validate_response(result, json_response_expected=False)
            volume_data = util.get_json_from_mixed_string(result.output)['data']
            volume_id = volume_data['id']

            expected_freeform = {'tagOne': 'value three'}
            expected_defined = {tag_data_container.tag_namespace.name: tag_names_to_values}
            assert expected_freeform == volume_data['freeform-tags']
            assert expected_defined == volume_data['defined-tags']

            result = invoke(['bv', 'volume', 'get', '--volume-id', volume_id])
            parsed_result = json.loads(result.output)
            assert expected_freeform == parsed_result['data']['freeform-tags']
            assert expected_defined == parsed_result['data']['defined-tags']

            # Update to different tags replaces
            for t in tag_data_container.tags:
                tag_names_to_values[t.name] = 'create_volume {}'.format(util.random_number_string())
            tag_data_container.write_defined_tags_to_file(
                os.path.join('tests', 'temp', 'defined_tags_1.json'),
                tag_data_container.tag_namespace,
                tag_names_to_values
            )

            attempts = 0
            while attempts <= 3:
                result = invoke([
                    'bv', 'volume', 'update',
                    '--volume-id', volume_id,
                    '--freeform-tags', 'file://tests/resources/tagging/freeform_tags_1.json',
                    '--defined-tags', 'file://tests/temp/defined_tags_1.json',
                    '--force'
                ])
                if result.exit_code == 0:
                    break
                else:
                    attempts += 1
                    time.sleep(5)
            util.validate_response(result)
            parsed_result = json.loads(result.output)

            expected_freeform = {'tagOne': 'value1', 'tag_Two': 'value two'}
            expected_defined = {tag_data_container.tag_namespace.name: tag_names_to_values}
            assert expected_freeform == parsed_result['data']['freeform-tags']
            assert expected_defined == parsed_result['data']['defined-tags']

            result = invoke(['bv', 'volume', 'get', '--volume-id', volume_id])
            parsed_result = json.loads(result.output)
            assert expected_freeform == parsed_result['data']['freeform-tags']
            assert expected_defined == parsed_result['data']['defined-tags']

            # Nuke tags by passing empty JSON objects
            result = invoke([
                'bv', 'volume', 'update',
                '--volume-id', volume_id,
                '--freeform-tags', '{}',
                '--defined-tags', '{}',
                '--force'
            ])
            util.validate_response(result)
            parsed_result = json.loads(result.output)
            assert {} == parsed_result['data']['freeform-tags']
            assert {} == parsed_result['data']['defined-tags']

            result = invoke(['bv', 'volume', 'get', '--volume-id', volume_id])
            parsed_result = json.loads(result.output)
            assert {} == parsed_result['data']['freeform-tags']
            assert {} == parsed_result['data']['defined-tags']
        finally:
            if volume_id:
                result = invoke([
                    'bv', 'volume', 'delete',
                    '--volume-id', volume_id,
                    '--force'
                ])
                util.validate_response(result)


def invoke(commands, debug=False, ** args):
    if debug is True:
        commands = ['--debug'] + commands

    return util.invoke_command(commands, ** args)
