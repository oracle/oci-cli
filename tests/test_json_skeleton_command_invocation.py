# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import os
import os.path
import pytest
import random
import shutil
from . import test_config_container
from . import util


def json_template_list_buckets(namespace):
    JSON_TEMPLATE_LIST_BUCKETS = """{{
        "compartmentId": "{}",
        "namespace": "{}"
    }}""".format(util.COMPARTMENT_ID, namespace)
    return JSON_TEMPLATE_LIST_BUCKETS


# This intentionally has some camel and snake case in there to make sure we coerce correctly
CREATE_SECURITY_LIST_TEMPLATE = """
{{
  "compartmentId": "{}",
  "displayName": "JSON Skeleton Test List",
  "egressSecurityRules": [
    {{
        "destination": "0.0.0.0/0",
        "icmpOptions": null,
        "isStateless": null,
        "protocol": "all",
        "tcpOptions": null,
        "udpOptions": null
    }}
  ],
  "ingress-security-rules": [
    {{
        "icmpOptions": null,
        "isStateless": null,
        "protocol": "6",
        "source": "0.0.0.0/0",
        "tcpOptions": {{
            "destination-port-range": {{ "max": 22, "min": 22 }},
            "source-port-range": null
        }},
        "udpOptions": null
    }},
    {{
        "icmp-options": {{ "code": 4, "type": 3 }},
        "is-stateless": null,
        "protocol": "1",
        "source": "0.0.0.0/0",
        "tcp-options": null,
        "udp-options": null
    }},
    {{
        "icmp-options": {{ "code": null, "type": 3 }},
        "is-stateless": null,
        "protocol": "1",
        "source": "10.0.0.0/16",
        "tcp-options": null,
        "udp-options": null
    }}
  ],
  "vcnId": "{}"
}}
"""


INPUT_FILE_FOLDER = os.path.join('tests', 'resources', 'json_input', 'test_files')


@pytest.fixture(scope='module', autouse=True)
def prepare_input_file_folder():
    if not os.path.exists(INPUT_FILE_FOLDER):
        os.makedirs(INPUT_FILE_FOLDER)

    with open(os.path.join(INPUT_FILE_FOLDER, 'list_buckets.json'), 'w') as f:
        with test_config_container.create_vcr().use_cassette(
                'json_skeleton_command_invocation_object_storage_namespace_get.yml'):
            # Grab the Object Storage namespace
            result = invoke(['os', 'ns', 'get'])
            util.validate_response(result)
            namespace = json.loads(result.output)['data']
            f.write(json_template_list_buckets(namespace))

    yield

    shutil.rmtree(INPUT_FILE_FOLDER)


@pytest.mark.skip('Skipped to allow DEX-14528')
@pytest.fixture(scope='module')
def network_resources():
    with test_config_container.create_vcr().use_cassette('json_skeleton_command_invoke_fixture_network_resources.yml'):
        vcn_name = util.random_name('cli_test_json_skeleton')
        cidr_block = "10.0.0.0/16"
        vcn_dns_label = util.random_name('vcn', insert_underscore=False)

        result = invoke([
            'network', 'vcn', 'create',
            '--compartment-id', util.COMPARTMENT_ID,
            '--display-name', vcn_name,
            '--cidr-block', cidr_block,
            '--dns-label', vcn_dns_label
        ])
        vcn_ocid = util.find_id_in_response(result.output)
        util.wait_until(['network', 'vcn', 'get', '--vcn-id', vcn_ocid], 'AVAILABLE', max_wait_seconds=300)

        subnet_name = util.random_name('cli_test_compute_subnet')
        subnet_dns_label = util.random_name('subnet', insert_underscore=False)

        result = invoke([
            'network', 'subnet', 'create',
            '--compartment-id', util.COMPARTMENT_ID,
            '--availability-domain', util.availability_domain(),
            '--display-name', subnet_name,
            '--vcn-id', vcn_ocid,
            '--cidr-block', cidr_block,
            '--dns-label', subnet_dns_label
        ])
        subnet_ocid = util.find_id_in_response(result.output)
        util.validate_response(result, expect_etag=True)
        util.wait_until(['network', 'subnet', 'get', '--subnet-id', subnet_ocid], 'AVAILABLE', max_wait_seconds=300)

        yield (vcn_ocid, subnet_ocid)

        result = invoke(['network', 'subnet', 'delete', '--subnet-id', subnet_ocid, '--force'])
        util.validate_response(result)
        util.wait_until(['network', 'subnet', 'get', '--subnet-id', subnet_ocid], 'TERMINATED', max_wait_seconds=600, succeed_if_not_found=True)

        result = util.invoke_command(['network', 'vcn', 'delete', '--vcn-id', vcn_ocid, '--force'])
        util.validate_response(result)
        util.wait_until(['network', 'vcn', 'get', '--vcn-id', vcn_ocid], 'TERMINATED', max_wait_seconds=600, succeed_if_not_found=True)


@test_config_container.RecordReplayWithNoClickContext('json_skeleton_command_invoke')
def test_list_buckets():
    result = invoke(['os', 'bucket', 'list', '--from-json', 'file://{}'.format(os.path.join(INPUT_FILE_FOLDER, 'list_buckets.json'))])
    parsed_result = json.loads(result.output)
    assert len(parsed_result['data']) >= 0


@test_config_container.RecordReplayWithNoClickContext('json_skeleton_command_invoke')
def test_list_buckets_with_override():
    # This will use the "testing-fake-namespace" as it was directly provided
    result = invoke(['os', 'bucket', 'list', '--namespace', 'testing-fake-namespace', '--from-json', 'file://{}'.format(os.path.join(INPUT_FILE_FOLDER, 'list_buckets.json'))])
    assert result.output == ''


# This test cannot be mocked because VCR doesn't play nicely with the FileReadCallbackStream implementation in the Python SDK
def test_create_update_bucket_and_put_object():
    base_path = os.path.join('tests', 'resources', 'json_input')
    bucket_name = 'json_skeleton_bucket_{}'.format(random.randint(0, 10000))

    result = invoke(['os', 'bucket', 'create', '--compartment-id', util.COMPARTMENT_ID, '--namespace', util.NAMESPACE, '--name', bucket_name, '--from-json', 'file://{}'.format(os.path.join(base_path, 'bucket_create.json'))])
    parsed_result = json.loads(result.output)
    expected_metadata = {'key1': 'hello', 'key_with_underscores': 'world'}
    assert expected_metadata == parsed_result['data']['metadata']

    result = invoke(['os', 'bucket', 'update', '--namespace', util.NAMESPACE, '--name', bucket_name, '--from-json', 'file://{}'.format(os.path.join(base_path, 'bucket_update.json'))])
    parsed_result = json.loads(result.output)
    expected_metadata = {'key1': 'hello_updated', 'another_key_with_underscores': 'replace previous', 'history': 'previous', 'key_with_underscores': 'world'}
    assert expected_metadata == parsed_result['data']['metadata']

    result = invoke([
        'os', 'object', 'put',
        '--namespace', util.NAMESPACE,
        '--bucket-name', bucket_name,
        '--name', 'test_obj',
        '--file', os.path.join(base_path, 'bucket_create.json'),
        '--from-json', 'file://{}'.format(os.path.join(base_path, 'object_put.json'))
    ])

    result = invoke([
        'os', 'object', 'head',
        '--namespace', util.NAMESPACE,
        '--bucket-name', bucket_name,
        '--name', 'test_obj'
    ])
    parsed_result = json.loads(result.output)
    assert 'hello_updated' == parsed_result['opc-meta-key1']
    assert 'underscores rejected?' == parsed_result['opc-meta-another-key-with-snake']
    assert 'previous' == parsed_result['opc-meta-history']
    assert 'text/json' == parsed_result['content-type']

    invoke(['os', 'object', 'delete', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name, '--name', 'test_obj', '--force'])
    invoke(['os', 'bucket', 'delete', '--namespace', util.NAMESPACE, '--name', bucket_name, '--force'])


def test_create_with_complex_param_in_json(network_resources):
    with test_config_container.create_vcr().use_cassette('json_skeleton_command_invoke_create_with_complex_param_in_json.yml'):
        input_file_path = os.path.join(INPUT_FILE_FOLDER, 'create-security-list.json')
        with(open(input_file_path, 'w')) as f:
            f.write(CREATE_SECURITY_LIST_TEMPLATE.format(util.COMPARTMENT_ID, network_resources[0]))

        result = invoke(['network', 'security-list', 'create', '--from-json', 'file://{}'.format(input_file_path)])
        security_list_ocid = util.find_id_in_response(result.output)
        parsed_output = json.loads(result.output)

        expected_egress = [
            {'description': None, 'destination': '0.0.0.0/0', 'icmp-options': None, 'is-stateless': None, 'protocol': 'all',
             'tcp-options': None, 'udp-options': None}
        ]
        expected_ingress = [
            {
                'description': None,
                'protocol': '6',
                'udp-options': None,
                'is-stateless': None,
                'icmp-options': None,
                'tcp-options': {'source-port-range': None, 'destination-port-range': {'min': 22, 'max': 22}},
                'source': '0.0.0.0/0'
            },
            {
                'description': None,
                'protocol': '1',
                'udp-options': None,
                'is-stateless': None,
                'icmp-options': {'type': 3, 'code': 4},
                'tcp-options': None,
                'source': '0.0.0.0/0'
            },
            {
                'description': None,
                'protocol': '1',
                'udp-options': None,
                'is-stateless': None,
                'icmp-options': {'type': 3, 'code': None},
                'tcp-options': None,
                'source': '10.0.0.0/16'
            }
        ]

        # These seem to be new fields but not present under all testing conditions.
        if "CIDR_BLOCK" in str(parsed_output['data']):
            expected_egress[0]['destination-type'] = 'CIDR_BLOCK'
            expected_ingress[0]['source-type'] = 'CIDR_BLOCK'
            expected_ingress[1]['source-type'] = 'CIDR_BLOCK'
            expected_ingress[2]['source-type'] = 'CIDR_BLOCK'
        has_errors = False
        try:
            assert parsed_output['data']['display-name'] == 'JSON Skeleton Test List'
            assert parsed_output['data']['egress-security-rules'] == expected_egress
            assert parsed_output['data']['ingress-security-rules'] == expected_ingress
        except AssertionError as ae:
            print("test_create_with_complex_param_in_json: parsed_output data=" + str(parsed_output['data']))
            has_errors = True
        finally:
            print("terminating network security list")
            invoke(['network', 'security-list', 'delete', '--security-list-id', security_list_ocid, '--force'])
            util.wait_until(['network', 'security-list', 'get', '--security-list-id', security_list_ocid], 'TERMINATED', max_wait_seconds=600, succeed_if_not_found=True)
            if has_errors:
                raise AssertionError("test_create_with_complex_param_in_json data assertions failed.")


@util.slow
def test_launch_instance(network_resources):
    with test_config_container.create_vcr().use_cassette('json_skeleton_command_invoke_launch_instance.yml'):
        launch_instance_json = 'file://{}'.format(os.path.join('tests', 'resources', 'json_input', 'launch_instance.json'))
        image_id = util.oracle_linux_image()
        shape = 'VM.Standard1.1'  # This overrides the shape in the JSON which is VM.Standard1.2
        hostname_label = util.random_name('bminstance', insert_underscore=False)
        private_ip = '10.0.0.15'

        print("launching instance")
        launch_instance_result = util.invoke_command([
            'compute', 'instance', 'launch',
            '--compartment-id', util.COMPARTMENT_ID,
            '--availability-domain', util.availability_domain(),
            '--subnet-id', network_resources[1],
            '--image-id', image_id,
            '--shape', shape,
            '--hostname-label', hostname_label,
            '--private-ip', private_ip,
            '--from-json', launch_instance_json
        ])

        if (launch_instance_result.output and 'LimitExceeded' in launch_instance_result.output) or (launch_instance_result.exception and 'LimitExceeded' in str(launch_instance_result.exception)):
            pytest.skip('Skipping test_launch_instance as we received a limit exceeded error from the service')

        instance_ocid = util.find_id_in_response(launch_instance_result.output)

        parsed_result = json.loads(launch_instance_result.output)
        assert parsed_result['data']['shape'] == 'VM.Standard1.1'
        assert parsed_result['data']['display-name'] == 'From JSON Skeleton'
        assert parsed_result['data']['metadata'] == {'meta1': 'meta2', 'meta3': 'meta4'}

        expected_extended_metadata = {
            'a': '1',
            'b': {
                'c': '3',
                'd': {}
            },
            'preserve_underscore': 'underscores retained',
            'preserve-snake': 'snake casing-retained'
        }
        extended_metadata_result = parsed_result['data']['extended-metadata']
        assert expected_extended_metadata == extended_metadata_result

        content = None
        with open(os.path.join('tests', 'resources', 'ipxe_script_example.txt'), mode='r') as file:
            content = file.read()

        assert 'ipxe-script' in launch_instance_result.output
        # Just look at the first few characters. Once we hit a line break the formatting will differ.
        assert content[:5] in launch_instance_result.output

        util.wait_until(['compute', 'instance', 'get', '--instance-id', instance_ocid], 'RUNNING', max_wait_seconds=600)

        # We can also provide JSON as a string if desired
        result = invoke(['compute', 'instance', 'list-vnics', '--from-json', '{{"instanceId": "{}"}}'.format(instance_ocid)])
        parsed_result = json.loads(result.output)
        assert len(parsed_result['data']) == 1
        assert parsed_result['data'][0]['public-ip'] is None  # No public IP in launch_instance.json
        assert parsed_result['data'][0]['display-name'] == 'JSON Skeleton VNIC'
        assert parsed_result['data'][0]['private-ip'] == '10.0.0.15'

        print("terminating instance")
        result = invoke(['compute', 'instance', 'terminate', '--instance-id', instance_ocid, '--force'])
        util.validate_response(result)
        util.wait_until(['compute', 'instance', 'get', '--instance-id', instance_ocid], 'TERMINATED', max_wait_seconds=1200, succeed_if_not_found=True)


def test_generate_example_metadata_on_object_put():
    result = invoke(['os', 'object', 'put', '--generate-param-json-input', 'metadata'])
    parsed_result = json.loads(result.output)

    expected_json = {
        'string1': 'string',
        'string2': 'string'
    }
    assert expected_json == parsed_result


def test_generate_example_metadata_on_bucket_create_update():
    create_result = invoke(['os', 'bucket', 'create', '--generate-param-json-input', 'metadata'])
    update_result = invoke(['os', 'bucket', 'update', '--generate-param-json-input', 'metadata'])

    expected_json = {
        'string1': 'string',
        'string2': 'string'
    }
    assert expected_json == json.loads(create_result.output)
    assert expected_json == json.loads(update_result.output)


def test_generate_example_extended_metadata_on_instance_launch():
    result = invoke(['compute', 'instance', 'launch', '--generate-param-json-input', 'extended-metadata'])
    parsed_result = json.loads(result.output)

    expected_json = {
        'string1': {
            'string1': 'string',
            'string2': 'string'
        },
        'string2': {
            'string1': 'string',
            'string2': 'string'
        }
    }
    assert expected_json == parsed_result


def test_generate_example_json_create_update_policy():
    create_result = invoke(['iam', 'policy', 'create', '--generate-param-json-input', 'statements'])
    update_result = invoke(['iam', 'policy', 'update', '--generate-param-json-input', 'statements'])

    expected_json = ['string', 'string']

    assert expected_json == json.loads(create_result.output)
    assert expected_json == json.loads(update_result.output)


def test_generate_full_command_json_rc_alias():
    availability_domain_result = invoke(['db', 'system', 'launch', '--generate-full-command-json-input'])

    expected_json = 'string'

    parsed_result = json.loads(availability_domain_result.output)
    assert expected_json == parsed_result['availabilityDomain']


def invoke(commands, debug=False, ** args):
    if debug is True:
        commands = ['--debug'] + commands

    return util.invoke_command(commands, ** args)
